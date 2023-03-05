from behave import *
import time
from hamcrest import *
from features.utility.UtilityClass import UtilityClass
from features.pages.LandingPageClass import LandingPageClass


@given("Chrome is opened and Unacademy page is opened")
def step_impl(context):
    # context.driver.implicitly_wait(10)
    time.sleep(1)
    expectedTitle = "Goals | Unacademy"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
'''''''''
@when("User clicks on start learning button")
def step_impl(context):
   StartLearning=LandingPageClass(context.driver)
   StartLearning.click_startlearning_link()
   time.sleep(5)
'''
@then("User navigates to list of courses page")
def step_impl(context):
    print("User Navigated")

@when("User clicks on CUET Course in the left hand side")
def step_impl(context):
    Cuet=LandingPageClass(context.driver)
    Cuet.click_cuet_link()
    print("User can see List of courses under CUET")
    time.sleep(3)

@then("It displays the list of CUET Courses")
def step_impl(context):
    print("It displays the list of CUET courses")

@step("It closes Browser")
def step_impl(context):
    pass
'''''''''
@When("User clicks on start learning button in page")
def step_impl(context):
    StartLearning = LandingPageClass(context.driver)
    StartLearning.click_startlearning_link()
    time.sleep(3)
'''

@when("User enters for {searchval}")
def step_impl(context, searchval):
    context.driver.implicitly_wait(5)
    searchvalelement=LandingPageClass(context.driver)
    searchvalelement.click_search_link(searchval)
    #time.sleep(3)

@then("It does not displays Courses")
def step_impl(context):
    print("It does not displays any courses")

@when("User clicks on CUET(Language and General) Course")
def step_impl(context):
    #context.driver.implicitly_wait(5)
    cuetlang=LandingPageClass(context.driver)
    cuetlang.click_cuet_lang_link()
    time.sleep(3)


@step("User navigates to CUET(Language and General) Course page")
def step_impl(context):
    print("User navigated to CUET(Language and General) Course page")

@when("User clicks on Educators Link")
def step_impl(context):
    #context.driver.implicitly_wait(2)
    educators = LandingPageClass(context.driver)
    educators.click_educators_link()
    print("Educators Link")
    time.sleep(1)

@when("User clicks on Batch Link")
def step_impl(context):
    #context.driver.implicitly_wait(2)
    batch=LandingPageClass(context.driver)
    batch.click_batch_link()
    time.sleep(2)


@when("User clicks on Free videos")
def step_impl(context):
    context.driver.implicitly_wait(5)
    freevideos=LandingPageClass(context.driver)
    freevideos.click_freevideos_link()
    time.sleep(3)

@step("User navigated to watch video page")
def step_impl(context):
    print("User navigated to watch video page")


@when("User clicks on View Profile")
def step_impl(context):
    context.driver.back()
    #context.driver.implicitly_wait(3)
    viewprofile=LandingPageClass(context.driver)
    viewprofile.click_viewprofile_link()
    time.sleep(2)


@step("User navigated to View Profile page")
def step_impl(context):
    print("User navigated to view profile page")


