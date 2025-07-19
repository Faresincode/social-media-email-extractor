# 🌀 Social Media Email Extractor (SMEE)

This is a Python-based tool built with **Streamlit** and **Selenium** to extract email addresses from targeted websites using Bing search engine. It allows you to target by country, domain, or email provider (ESP) and download verified results in CSV format.

---

## 📥 Install the Software

### 1. Install Python & ChromeDriver

#### 1.1 Install the latest version of Python:
👉 [Download Python](https://www.python.org/downloads/)

Make sure to check the box **“Add Python to PATH”** during installation.

#### 1.2 Install ChromeDriver:
👉 [Download ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)

- Download the correct version that matches your Chrome browser.
- Extract the ZIP file.
- Place `chromedriver.exe` directly into your project folder.

> ⚠️ **Important**: Do not move `chromedriver.exe` outside of the project directory.

---

### 2. Install Dependencies and Set Up the Virtual Environment

Open **Command Prompt in the project folder**, then paste this one-line command:

pip install -r requirements.txt && pip install virtualenv && virtualenv smee && smee\Scripts\activate && pip install -r requirements.txt

▶️ Run the Software
To start the software:

Open Command Prompt in the same project folder again

Paste the following to activate the environment and launch the tool:

smee\Scripts\activate && streamlit run prog.py


social-media-email-extractor/
├── prog.py
├── xpath_locators.py
├── esp.txt
├── all_countries.txt
├── targeted_sites.txt
├── requirements.txt
└── chromedriver.exe   ← This is downloaded separately
