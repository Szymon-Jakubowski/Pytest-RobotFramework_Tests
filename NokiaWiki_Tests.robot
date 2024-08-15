*** Settings ***
Library     SeleniumLibrary
Suite Setup    Set Default Timeout

*** Variables ***
${BROWSER}                 Firefox
${URL}                     https://www.google.com/
${SEARCH_TERM}             nokia wikipedia
${EXPECTED_FOUNDING_YEAR}  1865
${GOOGLE_SEARCH_INPUT}     //*[@name="q"]
${GOOGLE_SEARCH_BUTTON}    (//input[@name='btnK'])[2]
${ACCEPT_COOKIES_BUTTON}   //button[@id="L2AGLb"]
${WIKIPEDIA_LINK}          //h3[contains(text(),'Wikipedia')]
${NOKIA_FOUNDING_YEAR}     //*[@class="infobox"]/tbody/tr[6]/td/p/a[2]
${SCREENSHOT_FILENAME}     nokia_wikipedia_screenshot.png

*** Test Cases ***
Nokia Wikipedia Search Test
    [Documentation]    This test case searches for "nokia wikipedia" on Google, navigates to the Wikipedia page, and verifies the founding year of Nokia.
    Open Browser To Google
    Accept Cookies If Found
    Search For Nokia Wikipedia
    Verify And Click Wikipedia Link
    Capture Screenshot And Verify Nokia Page
    Close Browser

*** Keywords ***
Set Default Timeout
    Set Selenium Timeout    30 seconds

Open Browser To Google
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Accept Cookies If Found
    ${cookie_button}    Wait Until Element Is Visible     ${ACCEPT_COOKIES_BUTTON}    timeout=10s
    Run Keyword If  '${cookie_button}' != ''  Click Button  ${ACCEPT_COOKIES_BUTTON}

Search For Nokia Wikipedia
    Input Text    ${GOOGLE_SEARCH_INPUT}    ${SEARCH_TERM}
    Click Button    ${GOOGLE_SEARCH_BUTTON}
    Wait Until Page Contains Element    ${WIKIPEDIA_LINK}

Verify And Click Wikipedia Link
    ${elements}=    Get WebElements    ${WIKIPEDIA_LINK}
    Run Keyword If    ${elements}    Click Element    ${WIKIPEDIA_LINK}
    ...    ELSE    Fail    Wikipedia link not found in search results

Capture Screenshot And Verify Nokia Page
    Wait Until Page Contains    Nokia
    Capture Page Screenshot    ${SCREENSHOT_FILENAME}
    ${title}=    Get Title
    Should Contain    ${title}    Nokia

    ${founding_year}=    Get Text    ${NOKIA_FOUNDING_YEAR}
    Should Be Equal As Numbers    ${founding_year}    ${EXPECTED_FOUNDING_YEAR}

