Library    OperatingSystem

*** Variables ***

${cli}    /home/QA-2022/qa_kp01_Sysoeva/lab1/cli.py

*** Test Cases ***

Dir create
    ${result} =    Run Process    python3   ${cli}    post    directory    name\=root      max_elems\=100
    Should Contain    ${result.stdout}   Status code: 200

Dir move
    ${result} =    Run Process    python3   ${cli}    patch    directory    name\=name    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

Dir delete
    ${result} =    Run Process    python3   ${cli}    delete    directory    name\=name
    Should Contain    ${result.stdout}   Status code: 200

Dir read
    ${result} =    Run Process    python3   ${cli}    get    directory    name\=name    parent\=root
    Should Contain    ${result.stdout}   Status code: 200

