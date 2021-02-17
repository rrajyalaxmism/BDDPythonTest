Feature: to countdown the egg timer
  Scenario: countdown happens with the time set
    Given the url e.ggtimer.com is open
    When I set the timer to 25 and click on start button
    Then Count down starts by decrementing by 1 second
    And After the countdown ends a alert is displayed