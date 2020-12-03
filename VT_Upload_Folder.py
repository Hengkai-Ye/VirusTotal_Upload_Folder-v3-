import os
import json
import time
import requests

def getAnalysisId(url, apikey, file_src_str):
    headers = {'x-apikey':apikey}
    files = {'file':open(file_src_str,'rb')}
    response = requests.post(url, headers = headers, files = files)
    AnalysisId = response.json()['data']['id']
    return AnalysisId

def getReport(url, apikey, analysis_id):
    url_final = url + analysis_id
    headers = {'x-apikey':apikey}
    response = requests.get(url_final, headers = headers)
    return response

def main():
    apikey = "df141845cee3aa45bd306ab93745daa2c44ee477265533b1583e5e09c4c12841"
    url1 = "https://www.virustotal.com/api/v3/files"
    url2 = "https://www.virustotal.com/api/v3/analyses/"
    file_folder_src = input("Please input file folder source:")
    file_folder_src_str = str(file_folder_src)
    for root, dirs, files in os.walk(file_folder_src_str):
        for f in files:
            file_src_str = os.path.join(root, f)
            AnalysisId = getAnalysisId(url1, apikey, file_src_str)
            report = getReport(url2, apikey, AnalysisId)
            undetected_num = report.json()['data']['attributes']['stats']['undetected']
            malicious_num = report.json()['data']['attributes']['stats']['malicious']
            print(f, 'undetected_num is:', undetected_num)
            print(f, 'malicious_num is:', malicious_num)
            time.sleep(16)

if __name__=='__main__':
    main()


