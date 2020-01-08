# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s krks.d3print -t test_printer.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src krks.d3print.testing.KRKS_D3PRINT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/krks/d3print/tests/robot/test_printer.robot
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

Scenario: As a site administrator I can add a printer
  Given a logged-in site administrator
    and an add printer form
   When I type 'My printer' into the title field
    and I submit the form
   Then a printer with the title 'My printer' has been created

Scenario: As a site administrator I can view a printer
  Given a logged-in site administrator
    and a printer 'My printer'
   When I go to the printer view
   Then I can see the printer title 'My printer'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add printer form
  Go To  ${PLONE_URL}/++add++printer

a printer 'My printer'
  Create content  type=printer  id=my-printer  title=My printer

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the printer view
  Go To  ${PLONE_URL}/my-printer
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a printer with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the printer title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
