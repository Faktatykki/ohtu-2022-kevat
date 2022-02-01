*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  Pena
    Set Password  Penansalasana1234::
    Set Password Confirmation  Penansalasana1234::
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Pe
    Set Password  Penansalasana1234::
    Set Password Confirmation  Penansalasana1234::
    Submit Register Credentials
    Register Should Fail With Message  Username must be over 2 letters

Register With Valid Username And Too Short Password
    Set Username  Pena
    Set Password  sala12
    Set Password  sala12
    Submit Register Credentials
    Register Should Fail With Message  Password must be over 7 characters long and have one nonalphabetic character

Register With Nonmatching Password And Password Confirmation
    Set Username  Pena
    Set Password  salasana1234
    Set Password Confirmation  salasana4321
    Submit Register Credentials
    Register Should Fail With Message  Password and confirmation does not match

Login After Successful Registration
    Set Username  Penja
    Set Password  salasana1234
    Set Password Confirmation  salasana1234
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  Penja
    Set Password  salasana1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  Pena
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Register Credentials
    Register Should Fail With Message  Password must be over 7 characters long and have one nonalphabetic character
    Go To Login Page
    Set Username  Pena
    Set Password  salasana
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Create User And Go To Register Page
    Go To Register Page
    Register Page Should Be Open

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}