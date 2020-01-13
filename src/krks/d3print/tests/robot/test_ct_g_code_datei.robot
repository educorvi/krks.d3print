# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s krks.d3print -t test_g_code_datei.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src krks.d3print.testing.KRKS_D3PRINT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/krks/d3print/tests/robot/test_g_code_datei.robot
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

Scenario: As a site administrator I can add a GCode Datei
  Given a logged-in site administrator
    and an add Drucker form
   When I type 'My GCode Datei' into the title field
    and I submit the form
   Then a GCode Datei with the title 'My GCode Datei' has been created

Scenario: As a site administrator I can view a GCode Datei
  Given a logged-in site administrator
    and a GCode Datei 'My GCode Datei'
   When I go to the GCode Datei view
   Then I can see the GCode Datei title 'My GCode Datei'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Drucker form
  Go To  ${PLONE_URL}/++add++Drucker

a GCode Datei 'My GCode Datei'
  Create content  type=Drucker  id=my-g_code_datei  title=My GCode Datei

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the GCode Datei view
  Go To  ${PLONE_URL}/my-g_code_datei
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a GCode Datei with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the GCode Datei title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
