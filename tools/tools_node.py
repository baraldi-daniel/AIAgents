
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

from langchain_experimental.utilities import PythonREPL
import streamlit as st



@tool
def selenium_search(query: str):
    """
    Search the web for realtime and latest information urls if needed
    for examples, news, stock market, weather updates etc.
    
    Args:
    query: The search query
    """

    from selenium import webdriver

    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    driver.get("https://duckduckgo.com/")

    search_bar = driver.find_element(By.ID, "searchbox_input")

    search_bar.click()
    search_bar.click()
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)


    import time
    time.sleep(1)



    elements = driver.find_elements(By.TAG_NAME,"a")
    urls=set([i.get_attribute('href') for i in elements if "duck" not in str(i.get_attribute('href')) and "http" in str(i.get_attribute("href"))])
    return urls



@tool
def python_executor(code: str):
    """
    PythonREPL to execute python code. You must pass only the code to execute and nothing else. You can execute python code to create charts, calculate something, create games or draw images.
    
    
    Args:
    code: The python code to execute
    """
    from langchain_experimental.utilities import PythonREPL

    python_repl = PythonREPL()



    output=python_repl.run(code)
    return output
 


tools = [selenium_search, python_executor]