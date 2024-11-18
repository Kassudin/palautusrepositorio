*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Bob
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Bo
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  Bob
    Set Password  Bob1234
    Set Password Confirmation  Bob1234
    Submit Registration
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  Bob
    Set Password  BobBobBob
    Set Password Confirmation  BobBobBob
    Submit Registration
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  Bob
    Set Password  Bob12345
    Set Password Confirmation  Bob123456
    Submit Registration
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Registration
    Register Should Fail With Message  Username is already taken



Login After Successful Registration
    Set Username  Bob
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Registration
    Register Should Succeed
    Press Continue To Main Page
    Main Page Should Be Open
    Press Logout 
    Login Page Should Be Open
    set Login Username  Bob
    Set Login Password  Bob12345
    Submit Login 
    Login Should Succeed

Login After Failed Registration
    Set Username  Bo
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 characters long
    Press Login
    set Login Username  Bo
    Set Login Password  Bob12345
    Submit Login 
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Press Continue To Main Page
    Click Link  Continue to main page

Press Logout
    Click Button  Logout

Press Login
    Click Link  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Login
    Click Button  Login

Set Login Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Login Password
    [Arguments]  ${password}
    Input Password  password  ${password}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

#robot --variable BROWSER:firefox src/tests/register.robot 

