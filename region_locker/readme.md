# Dome9 Region Locker - defines region's policy for newly created AWS Security Groups

## What is it?
- A little python script that sets the Dome9 policy for newly detected Security Groups (Read Only, Full Protection or Region Lock)
- This is very useful for highly secured environments that do not permit changes outside of a clearly defined update window.

## Installation instructions
- Make sure that you have python installed (version 2.6 and up, ver. 3.X is supported as well).
- Make sure that the python module 'requests' is installed:  https://pypi.python.org/pypi/requests
- Git clone this repo or download the repository zip file (https://github.com/Dome9/dome9_tools/archive/master.zip)
- Set execute permissions for the script file:

```bash
cd region_locker
chmod +x d9_newly_detected_sg_handling_policy.py
```

- (Optional) For ease of use, set your Dome9 user(email) / api key (found in your Dome9 console-> Setting page) in environment variables : 

```
export d9_user=my@email.com
export d9_api_sec=XXXXXXXXXXX
```

## Usage

```
./d9_newly_detected_sg_handling_policy.py --help
```

usage: d9_sg_locker.py [-h]  [--accid ACCID ]
                       [--region REGION] [-v] [--mode MODE] [-u USER]
                       [-p APISECRET]

optional arguments:

  -h, --help            show this help message and exit
  
  --accid ACCID
                        Dome9 AWS account ids.
                        
  --region REGION
                        Region String in Dome9 format (use underscore, not dash)
						
    
  --mode MODE
                        [ReadOnly|FullManage|RegionLock]
						
  -u USER, --user USER  Dome9 user name (your email)
  
  -p APISECRET, --apisecret APISECRET
                        Your Dome9 api key. Found under settings.
						
  					
## Examples
./d9_newly_detected_sg_handling_policy.py -u v2id -p v2key --d9AcctID 7825-361b-2523-ycef-3042df7f7320 --region us-east-1 --mode ReadOnly
./d9_newly_detected_sg_handling_policy.py -u v2id -p v2key --d9AcctID 7825-361b-2523-ycef-3042df7f7320 --region us-east-1 --mode FullManage
./d9_newly_detected_sg_handling_policy.py -u v2id -p v2key --d9AcctID 7825-361b-2523-ycef-3042df7f7320 --region us-east-1 --mode RegionLock
