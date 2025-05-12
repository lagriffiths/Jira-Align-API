import requests
import pandas as pd
#import numpy as np
#import pandasql as psql
#from datetime import datetime
import base64

JA_end_point_data = pd.DataFrame()

#https://xxx.jiraalign.com/rest/align/api/docs/index/html

def get_data(url):

    #lets set up the authorisation for Jira Align - this really shouldn't live here.

    # This assume you're jira align is in the cloud and not hosted locally.
    username = "aaa.aaa@aaa.com"
    api_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Get this from the Atlassian portal id.atlassian.com/manage-profile/security/api-tokens
    combined = f"{username}:{api_token}"

    # Cloud Jira requires a base64 encoded token for authentication
    encoded_token = base64.b64encode(combined.encode().decode())
    #print(encoded_token)

    auth_details = {
        "method": "GET",
        "url": url,
        "headers": {
            "Authorization": f"Basic {encoded_token}" # This is for cloud jira
    #        "Authorization" : f"bearer {api_token}" # This is for local hosted jira
        }
    }

    # Make the API request
    response = requests.get(auth_details["url"], headers=auth_details["headers"]) # , verify=False) #This is used if there is an SSL error (I should look into this)
    #print(response)

    #check if the request was successful
    if response.status_code == 200:
        #parse the json response
        try:
            data = response.json()
            df = pd.DataFrame(data)
            return df
        except ValueError:
            print("The repose is not valid json")
    else:
        print(f"Fail to retrive dataL {response.status_code}")

if __name__ == "__main__":
    
    list_of_urls = [
    "https://xxxx.jiraalign.com/rest/align/api/2/....end_point1",
    "https://xxxx.jiraalign.com/rest/align/api/2/....end_point2",
    "https://xxxx.jiraalign.com/rest/align/api/2/....end_point3",
    "https://xxxx.jiraalign.com/rest/align/api/2/....end_point4"
    ]

    for url in list_of_urls:
        JA_end_point_data = get_data(url)