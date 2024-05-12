from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://ismis.usc.edu.ph/StudentEvaluation")
driver.get("")

# EVALUATION
for i in range(1, 32):
  #ITEMS EVALUATION
  if (1 <= i < 6):
    stronglyDisagree = 1
    disagree = 2
    agree = 3
    stronglyAgree  = 4
    xpath = "//input[@value='" + str(stronglyAgree) + "," + str(i) + "']"
  elif (6 <= i < 26):
    # TEACHING QUALITY EVAL && TEACHER-LEARNER SUPPORT
    stronglyDisagree = 5
    disagree = 6
    agree = 7
    stronglyAgree  = 8
    xpath = "//input[@value='" + str(agree) + "," + str(i) + "']"
  elif (26 <= i < 31):
    # STUDENT OUTCOMES 
    stronglyDisagree = 9
    disagree = 10
    agree = 11
    stronglyAgree  = 12
    xpath = "//input[@value='" + str(stronglyAgree) + "," + str(i) + "']"
  elif (i == 31):
    xpath = "//input[@value='20," + str(i) + "']"
  eval = driver.find_element(by=By.XPATH, value=xpath)
  eval.click()

## What do you like about the course
likedaboutcourse_eval = driver.find_element(by=By.ID, value="comments_0__Remarks")
likedaboutcourse_eval.send_keys("")

## Aspects to be improved
tobeimproved_eval = driver.find_element(by=By.ID, value="comments_1__Remarks")
tobeimproved_eval.send_keys("")

## Experience about course
experienceCourse_eval = driver.find_element(by=By.ID, value="comments_2__Remarks")
experienceCourse_eval.send_keys("")

## Recommend
element = driver.find_element(by=By.NAME, value="comments[3].Score")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
element.click()

reccomend_teacher = driver.find_element(by=By.ID, value="comments_3__Remarks")
reccomend_teacher.send_keys("Maam Pena is the best")

# Submit
submit_button = driver.find_element(by=By.CLASS_NAME, value="btn")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()
