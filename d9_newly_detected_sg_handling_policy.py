#! /usr/bin/env python
#
#   Dome9 Newly Detected Security Groups Handling Policy Updater.
#   Use it to update how Dome9 handles newly detected security groupsupdate how Dome9 handles newly detected security groups.
#   Modes are: ReadOnly, FullManage, RegionLock
#
#   Chen Burshan <chen@dome9.com>
#   Copyright (c) 2017, Dome9 Security, Ltd. See LICENSE file
#
# Execution examples:
#./d9_newly_detected_sg_handling_policy.py -u v2id -p v2key --d9AcctID 6b387825-361b-2523-ycef-3042df7f7320 --region us-east-1 --mode ReadOnly
#./d9_newly_detected_sg_handling_policy.py -u v2id -p v2key --d9AcctID 6b387825-361b-2523-ycef-3042df7f7320 --region us-east-1 --mode FullManage
#./d9_newly_detected_sg_handling_policy.py -u v2id -p v2key --d9AcctID 6b387825-361b-2523-ycef-3042df7f7320 --region us-east-1 --mode RegionLock


import argparse, json, requests, csv, sys, os, urllib, time
from requests.auth import HTTPBasicAuth

# Python 2.x. vs 3 raw_input compatibility
try: input = raw_input
except NameError: pass

if __name__ == "__main__":
    # --- Command line argument parsing ---
    parser = argparse.ArgumentParser(description='Update Dome9  Newly Detected Security Groups Handling Policy.\nThisutility uses Dome9 V2 APIs and must be used with V2 API key')
    parser.add_argument('--region', help='Region selector', required=True)
    parser.add_argument('--mode',help='Service Selector', required=True)
    parser.add_argument('--hidden',help='Region Visibility Settings', default="false")
    parser.add_argument('--d9AcctID',help='Dome9 AWS Account ID', required=True)
    parser.add_argument('-u','--user', help='Dome9 V2 API Key ID')
    parser.add_argument('-p','--apisecret', help='Your Dome9 V2 API Key.')
    parser.add_argument('--ack', help='Supress acknowledgement message before perfroming changes (recommended only for automated use-cases)',  action="store_true")
    args = parser.parse_args()

    email = args.user or os.getenv('d9_user')
    if not email:
        print("either provide --user parameter or d9_user environement variable")
        sys.exit()
    key = args.apisecret or os.getenv('d9_api_sec')
    if not key:
        print("either provide --apisecret parameter or d9_api_sec environement variable")
        sys.exit()

    region = args.region
    if not region:
        print("Please provide region for which the IP list will be constructed or updated.")
        sys.exit()

    mode = args.mode
    if not mode:
        print("Please provide handling mode. Hnadling modes can be: ReadOnly | FullManage | RegionLock .")
        sys.exit()

    hidden = args.hidden
    if not hidden:
        print("Please provide visibility mode. Visibility is defined as hidden mode (either false or true). ")
        sys.exit()

    d9AcctID  = args.d9AcctID
    if not d9AcctID:
        print("Please provide Dome9 AWS account ID. The Account ID can be retrived from Dome9 Central, Cloud Accounts Page, by highlighting the AWS account and extracting the ID from the URL.")
        sys.exit()

    print("Newly detected Security Groups handling policy will be updated to {} for region {} of account {}.".format(mode, region, d9AcctID))

    api_end_point = "https://api.dome9.com/v2/cloudaccounts/" + d9AcctID
    print(api_end_point)

    if (mode !="ReadOnly" and mode !="FullManage" and  mode!="RegionLock"):
        print("Mode can be either ReadOnly or FullManage or RegionLock")
        sys.exit()
    if (mode=="RegionLock"):
        mode="Reset"

    if (hidden!="false" and hidden!="true"):
        print("Visibility can be either false or true")
        sys.exit()
    reqBody = {"netSec":{"regions":[{"region":region,"hidden":hidden,"newGroupBehavior":mode}]}}
    reqBodyTxt = json.dumps(reqBody)
    print(reqBodyTxt)

    r = requests.patch(api_end_point, auth=HTTPBasicAuth(email, key), data=reqBodyTxt, headers={"Content-Type": "application/json; charset=UTF-8"})
    print(r)
