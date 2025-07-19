from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#...webdriver import
from webdriver_manager.chrome import ChromeDriverManager
import time
#..import regex
import re
from selenium.webdriver.support import expected_conditions as EC
import regex
import xpath_locators as xp
import streamlit as  st
import base64
import plotly.express as px
import pandas as pd
from selenium.webdriver.common.by import By

import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
cwd = os.getcwd()


def ProgramVariableXpath():
    email_regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    EmailRegexValidator="^[\w_.-]+@[\w_.+-]+\.[\w]{2,4}$"
    BingSearchEngineLink="https://www.bing.com/"
    BingSearchEngineSettingLink='https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f&FORM=O2HV65'
    BingSettinResultsSectiongOpenLinkFromSearchResultsCheckboxXpath='//*[@name="newwnd"]'
    BingSettinResultsSectiongOpenLinkFromNewsResultsCheckboxXpath='//*[@name="newsnt"]'
    BingSettingSaveButtonXpath='//*[@class="btn blue"][1]'
    bing_search_input_xpath = "//*[@id='sb_form_q']"
    bing_searcch_button_xpath = "//*[@id='search_icon']//*[name()='svg']" 
    search_results_links_xpath = "//h2/a" 
    NextPageButtonClass = "sb_pagN_bp b_widePag sb_bp"
    EndsearchPageNoResultClass="sb_inactP sb_pagN sb_pagN_bp b_widePag sb_bp"
    ToolsButtonXpath="//*[contains(text(),'Tools')][1]"
    NewTabButtonActiveClass="ntf_img  toggle_on  toggle_img"
    NewTabButtonXpath='//*[@class="nt_val toggle_ctrl"]'
    next_page_button_list_xpath = """//*[@title='Next page']"""
    next_page_button_list_xpath ="""//*[@class="sb_pagN sb_pagN_bp b_widePag sb_bp "]"""
    next_page_button_xpath = """//*[@class="sb_pagN sb_pagN_bp b_widePag sb_bp "]"""

global driver
global Allemailprogramescraping
garbedgcaracter="/"
st.set_page_config(page_title = 'SMEE',page_icon = '🌀',layout = 'wide')

def get_esplist_fromtextfile():
    global esp_domainmail_list
    # Get a list from esp.txt
    with open('esp.txt', 'r',encoding='utf-8') as esp:
        content_list = esp.readlines()
    esp.close()
    esp_domainmail_list = []
    for espmail in content_list :
        espmail = espmail.strip().lower()
        esp_domainmail_list.append(espmail)
    esp_domainmail_list=list(filter(None, esp_domainmail_list))
    esp_domainmail_list=esp_domainmail_list
get_esplist_fromtextfile()

def get_siteslist_from_text_file():
    global targeted_sites
    # get countries list from profiles_data.txt
    with open ("targeted_sites.txt" ,"r" ,encoding='utf-8') as sites:
        content_list=sites.readlines ()#line:92
    sites.close()
    targeted_sites = []
    for site in content_list:
        site=site.strip().lower()
        targeted_sites.append(site)
    targeted_sites=list(filter(None,targeted_sites))
    targeted_sites=targeted_sites
get_siteslist_from_text_file()

def get_countries_list_from_text_file():
    global countries_list 
    # get countries list from profiles_data.txt
    with open ("all_countries.txt" ,"r" ,encoding='utf-8') as country:
        count_list1=country.readlines ()#line:92
    country.close()
    country_list=[]
    for countr in count_list1:
        clean_countr=countr.strip()
        country_list.append(clean_countr)
    country_list=list(filter(None, country_list))
    countries_list=country_list
get_countries_list_from_text_file()


st.header("Social Media Email Extractor")

country=st.selectbox("Country",countries_list )
site=st.selectbox("Targeted Site ",targeted_sites)
esp=st.selectbox("Targeted Esp ",esp_domainmail_list)
keyword =st.text_area("Enter your keywords in seperate line ")
st.write("If you want to target location address (do not select country)")
locationadress=st.text_input("Targeted Address ")
st.text('to verify emails go to this website (Free) [https://check.emailverifier.online/]')
keywords_list=keyword.split("\n")

def ConfigureBingSetting():
    global driver
    driver.implicitly_wait(50)
    driver.get(xp.BingSearchEngineSettingLink)
    driver.execute_script(f"window.scrollBy(0,442)")
    BingSettinResultsSectiongOpenLinkFromSearchResultsCheckbox=driver.find_element(By.XPATH,xp.BingSettinResultsSectiongOpenLinkFromSearchResultsCheckboxXpath)
    BingSettinResultsSectiongOpenLinkFromSearchResultsCheckbox.click()
    BingSettinResultsSectiongOpenLinkFromNewsResultsCheckbox=driver.find_element(By.XPATH,xp.BingSettinResultsSectiongOpenLinkFromNewsResultsCheckboxXpath)
    BingSettinResultsSectiongOpenLinkFromNewsResultsCheckbox.click()
    BingSettingSaveButton=driver.find_element(By.XPATH,xp.BingSettingSaveButtonXpath)
    BingSettingSaveButton.click()

def search_proces():
    global driver
    global keyword
    global esp
    driver.get(xp.BingSearchEngineLink)
    if country=='No Country':
        search_query = "site: "+ site + ' "'+esp+'" '+ ' '+keyword+' ' +locationadress
    else:
        search_query = "site: "+ site + ' "'+esp+'" '+ ' '+keyword+' ' +country

    bing_search_input = driver.find_element(By.XPATH,xp.bing_search_input_xpath)
    bing_search_input.clear()
    bing_search_input.send_keys(search_query)
    try:
        bing_search_input.send_keys(Keys.ENTER)
    except:
        bing_searcch_button = driver.find_element(By.XPATH,xp.bing_searcch_button_xpath)
        bing_searcch_button.click()


def EmailsTo_CSV():
    global csv
    global Allemailprogramescraping
    Allemailprogramescraping=list(set(Allemailprogramescraping))
    my_data=pd.DataFrame(Allemailprogramescraping)
    csv=my_data.to_csv(index=False,header=False).encode("utf-8")
    return csv

def run_all_program():
    global keyword
    global driver
    global esp
    global Allemailprogramescraping
    global NumberOfEmail
    global element
    NumberOfEmail=0
    Allemailprogramescraping=[]
    driver = webdriver.Chrome()
    driver.maximize_window()
    ConfigureBingSetting()
    if esp=="all":
        del esp_domainmail_list[0]
        for keyword in keywords_list:
            for esp in esp_domainmail_list:
                search_proces()
                while True:
                    # Wait until document.readyState == "complete"
                    WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
                    # Then wait for key element (optional)
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]')))
                    pagehtml = driver.find_element(by=By.TAG_NAME, value='body')
                    allpagehtml = pagehtml.get_attribute('innerHTML')
                    if xp.NextPageButtonClass in allpagehtml and  xp.EndsearchPageNoResultClass not in allpagehtml :
                        next_page_button = driver.find_element(By.XPATH, xp.next_page_button_xpath)
                        actions = ActionChains(driver)
                        actions.move_to_element(next_page_button).perform()
                        page_text = driver.find_element(by=By.TAG_NAME, value='body').text
                        if "WEB" in page_text:
                            page_text=page_text.replace("WEB"," ")
                        page_text = page_text.lower()
                                # scrape element list with regex
                        extracted_email_list1 = re.findall(xp.email_regex, page_text)
                        extracted_email_list1=list(filter(None, extracted_email_list1))
                        new_clean_list1=list(set(extracted_email_list1))
                        for element in new_clean_list1:
                            if garbedgcaracter in element:
                                continue
                            if re.search(xp.EmailRegexValidator,element):
                                Allemailprogramescraping=list(set(Allemailprogramescraping))
                                if element not in Allemailprogramescraping:
                                    Allemailprogramescraping.append(element)
                                    st.text(element)
                            else:
                                continue

                        next_page_button.click()
                    else:
                        break

        driver.quit()
        st.download_button(label="Download",data=EmailsTo_CSV(),file_name="EmailsData.csv",mime="text/csv")
    else:
        for keyword in keywords_list:
            search_proces()
            while True:
                pagehtml = driver.find_element(by=By.TAG_NAME, value='body')
                allpagehtml=pagehtml.get_attribute('innerHTML')
                if xp.NextPageButtonClass in allpagehtml and  xp.EndsearchPageNoResultClass not in allpagehtml :
                    next_page_button = driver.find_element(By.XPATH, xp.next_page_button_xpath)
            
                    ActionChains(driver).move_to_element(next_page_button).perform().click()
                    page_text = driver.find_element(by=By.TAG_NAME, value='body').text
                    if "WEB" in page_text:
                        page_text=page_text.replace("WEB"," ")
                    page_text = page_text.lower()
                            # scrape element list with regex
                    extracted_email_list1 = re.findall(xp.email_regex, page_text)
                    extracted_email_list1=list(filter(None, extracted_email_list1))
                    new_clean_list1=list(set(extracted_email_list1))
                    for element in new_clean_list1:
                        if esp not in element:
                            continue
                        if garbedgcaracter in element:
                            continue
                        if re.search(xp.EmailRegexValidator,element):
                            Allemailprogramescraping=list(set(Allemailprogramescraping))
                            if element not in Allemailprogramescraping:
                                Allemailprogramescraping.append(element)
                                st.text(element)
                        else:
                            continue

                    next_page_button.click()
                else:
                    break

        driver.quit()
        st.download_button(label="Download",data=EmailsTo_CSV(),file_name="EmailsData.csv",mime="text/csv")

run_btn = st.button("Generate Emails")
st.write("If you want to stop the software click in (Refresh) button a lot of time")
if 'refresh' not in st.session_state:
    st.session_state.refresh = 0
def refresh_state():
    st.session_state.refresh += 1
st.button('Refresh', on_click=refresh_state)
if run_btn:
    st.write("To download the emails scroll to the bottom of the page and click Download button once his finish")
    run_all_program()




    










