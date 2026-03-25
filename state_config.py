"""
State configuration for this AmericanSamoaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "AS"
STATE_NAME = "American Samoa"
APP_NAME = "AmericanSamoaDischargeWatch"
APP_TAGLINE = "American Samoa Discharge Monitoring"
DOMAIN = "americansamoadischargewatch.org"
DATA_FILE = "as_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@americansamoadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "SST"
EPA_REGION = 9
