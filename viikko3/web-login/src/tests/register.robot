*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Succeed  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long and contain only lowercase letters


Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle1
    Set Password Confirmation  kalle1
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kalleeee
    Set Password Confirmation  kalleeee
    Submit Registration
    Registration Should Fail With Message  Password must contain both letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kall
    Submit Registration
    Registration Should Fail With Message  Password and confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username is already taken

*** Keywords ***
Submit Registration
    Click Button  Register 

Registration Should Succeed
    Welcome Page Should Be Open
    Page Should Contain  $(message)

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
