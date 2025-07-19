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
