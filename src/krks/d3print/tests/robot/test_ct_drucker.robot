# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s krks.d3print -t test_drucker.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src krks.d3print.testing.KRKS_D3PRINT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/krks/d3print/tests/robot/test_drucker.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Drucker
  Given a logged-in site administrator
    and an add Drucker form
   When I type 'My Drucker' into the title field
    and I submit the form
   Then a Drucker with the title 'My Drucker' has been created

Scenario: As a site administrator I can view a Drucker
  Given a logged-in site administrator
    and a Drucker 'My Drucker'
   When I go to the Drucker view
   Then I can see the Drucker title 'My Drucker'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Drucker form
  Go To  ${PLONE_URL}/++add++Drucker

a Drucker 'My Drucker'
  Create content  type=Drucker  id=my-drucker  title=My Drucker

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Drucker view
  Go To  ${PLONE_URL}/my-drucker
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Drucker with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Drucker title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
