*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Pena  penansalasana1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  Pe  salasana1234
    Output Should Contain  Username must be over 2 letters

Register With Valid Username And Too Short Password
    Input Credentials  Pena  salasa7
    Output Should Contain  Password must be over 7 characters long and have one nonalphabetic character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  Pena  salasana
    Output Should Contain  Password must be over 7 characters long and have one nonalphabetic character
    
*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

