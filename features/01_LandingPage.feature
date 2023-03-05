Feature: CUET Course
  Scenario: To validate that user navigates to List of CUET Course on that page
    Given Chrome is opened and Unacademy page is opened
    #When User clicks on start learning button
    Then User navigates to list of courses page
    When User clicks on CUET Course in the left hand side
    Then It displays the list of CUET Courses
    And It closes Browser
@functionaltests
   Scenario Outline: To validate Search in Explore page
     Given Chrome is opened and Unacademy page is opened
      #When User clicks on start learning button
      Then User navigates to list of courses page
      When User enters for <valid course>
      Then It displays the list of CUET Courses
      And It closes Browser
    Examples:
      |valid course|
      |CUET        |
@functionaltests
  Scenario Outline: To validate Search in Explore page
     Given Chrome is opened and Unacademy page is opened
      #When User clicks on start learning button
      Then User navigates to list of courses page
      When User enters for <invalid course>
      Then It does not displays Courses
      And It closes Browser
    Examples:
      |invalid course|
      |@@@        |

  Scenario: To validate while clicking on CUET(Language and General) user navigates to that Particular course page
    Given Chrome is opened and Unacademy page is opened
    When User clicks on CUET(Language and General) Course
    Then User navigates to CUET(Language and General) Course page
    When User clicks on Educators Link
    When User clicks on Batch Link

  Scenario: To validate Course page videos
    Given Chrome is opened and Unacademy page is opened
    When User clicks on CUET(Language and General) Course
    When User clicks on Free videos
    And User navigated to watch video page
    When User clicks on View Profile
    And User navigated to View Profile page