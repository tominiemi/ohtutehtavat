*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  kalle123
    Output Should Contain  Username is shorter than 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ööööö  kalle123
    Output Should Contain  Username must consist only of characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle1
    Output Should Contain  Password is shorter than 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password only contains letters