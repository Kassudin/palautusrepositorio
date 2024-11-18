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
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Bo
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  Bob
    Set Password  Bob1234
    Set Password Confirmation  Bob1234
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  Bob
    Set Password  BobBobBob
    Set Password Confirmation  BobBobBob
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  Bob
    Set Password  Bob12345
    Set Password Confirmation  Bob123456
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  Bob12345
    Set Password Confirmation  Bob12345
    Submit Credentials
    Register Should Fail With Message  Username is already taken

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
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

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

#robot --variable BROWSER:firefox src/tests/register.robot 

