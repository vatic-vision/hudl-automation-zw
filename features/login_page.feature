Feature: Login Page
    - Tests for Hudl login page
    
    Scenario: User can log in
        When I enter my username
        And I click continue
        And I enter my password
        And I click continue
        Then I am directed to the "/home" page

    Scenario: User unable to log in with incorrect password
        When I enter my username
        And I click continue
        And I enter the password "lolwrongpassword"
        And I click continue
        Then a "password" error appears incluing text "Your email or password is incorrect. Try again."

    Scenario: Edit email in username field
        When I enter the username "user@example.com"
        And I click continue
        And I click Edit on the email input
        And I enter my username
        And I click continue
        And I enter my password
        And I click continue
        Then I am directed to the "/home" page

    Scenario: Nav to create account
        When I click create account
        Then I am directed to the "/signup" page

    Scenario: Nav to forgot password
        When I enter my username
        And I click continue
        And I click forgot password
        Then I am directed to the "/reset-password" page

    Scenario: XSS attempt doesn't result in alert
        When I enter the username "<script>alert('Uh oh, you shouldn't see this')</script>)"
        And I click continue
        Then an alert does not appear
        And a "username" error appears incluing text "Enter a valid email."