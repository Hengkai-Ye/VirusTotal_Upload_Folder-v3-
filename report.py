import os
import json
import time
import requests
import shutil
import pickle

def getReport(url, apikey, response_json):
    params2 = {'apikey': apikey, 'resource': response_json}
    response = requests.get(url, params=params2)
    return response

def main():
    count = 0
    apikey = "your api key"
    url2 = 'https://www.virustotal.com/vtapi/v2/file/report'
    benign_folder = "./benign/"
    report_pickle = open('./report/00241_1.pkl', 'wb')
    report_dict = {}
    pickle_file = open('./pickle/00241_1.pkl', 'rb')
    response_dict = pickle.load(pickle_file)
    #print(response_dict)
    pickle_file.close()
    for file_name, file_id in response_dict.items():
        print(file_name)
        print("got one")
        report = getReport(url2, apikey, file_id)
        print(report)
        total_num = report.json()['total']
        positive_num = report.json()['positives']
        report_dict[file_name] = positive_num
        if positive_num < 5:
            result_log = open('./result.txt', 'a+')
            print(file_name,' ',total_num,' ', positive_num,  file=result_log)
            print('', file=result_log)
            shutil.move(file_name, benign_folder)
            count += 1
            result_log.close()
        time.sleep(20)
    print(count)
    pickle.dump(report_dict, report_pickle)
    report_pickle.close()

if __name__=='__main__':
    main()
#retrieve report. If less than 5 engines detect malicious, move the file to 'benign' folder.
#The detection details are stored in the report folder.
