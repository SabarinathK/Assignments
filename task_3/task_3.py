
cloud = {
    "AZR": {"Medium":["HMZ-VPCX-8132HDFV4B4F45E"],
    "Large":["HMZ-VPCX-C6738C744C6D55E"] },
    "AWS":
    {"Small":["HMZ-VPCX-C67345D3NSB4F45E","HMZ-VPCX-YCX2C744B4F45E"] },
    "GCP":
    {"Medium":["HMZ-VPCX-FG916C744B4F45E"]}
 }


def task(DICT):
    name=DICT.keys()
    for i in name:
        print ('Cloud name :', i,', Size:',list(DICT[i].keys()))
        
task(cloud)