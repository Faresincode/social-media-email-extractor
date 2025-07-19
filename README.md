# social-media-email-extractor
Streamlit + Selenium app to extract emails from websites using Bing. Export to CSV by targeting domains, ESPs, and countries.

Note: This script was originally written in 2022, so some XPath elements may need to be updated if the target websites (like Bing) have changed their structure.
# 🌀 Social Media Email Extractor (SMEE)

**SMEE** is a browser-based tool built with **Python**, **Streamlit**, and **Selenium** that allows you to extract verified email addresses from targeted websites using Bing search.

It’s designed for:
- 📨 Lead generation
- 📊 Market research
- 🤖 Automation & data scraping projects

You can search by **country**, **email provider (ESP)**, and **website**, then export results as a clean CSV file.

---

## 🚀 Features

✅ Streamlit Web Interface  
✅ Works with Bing search engine  
✅ Filters by:
- Country
- Domain
- Email service provider (ESP)
- Keyword & location

✅ Regex-based email extraction  
✅ Export to `.csv`  
✅ Download-ready interface  
✅ Virtual environment setup script included

---

## 📥 Installation

### Step 1: Install Python & ChromeDriver

- 📦 [Download Python](https://www.python.org/downloads/) and install (check the box "Add to PATH")
- 🌐 [Download ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable) it depend on your system
  - Make sure the version matches your Chrome browser
  - Extract the ZIP and **place `chromedriver.exe` inside the project folder**

---

### Step 2: Install Requirements and Setup

Open **Command Prompt** in the project folder and paste:

```bash
pip install -r requirements.txt && pip install virtualenv && virtualenv smee && smee\Scripts\activate && pip install -r requirements.txt

▶️ Run the Tool
Still in the same Command Prompt, paste: or later open the command prompt in the project folder to have the path automaticlly and past this

smee\Scripts\activate && streamlit run prog.py
