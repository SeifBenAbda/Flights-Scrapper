import time
from concurrent.futures import ThreadPoolExecutor

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tabulate import tabulate