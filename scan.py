import os
import json
import time
import requests
import shutil
import pickle

def getAnalysisId(url, apikey, file_src_str):
    params = {'apikey': apikey}
    files = {'file': open(file_src_str, 'rb')}
    response = requests.post(url, params=params, files=files)
    return response.json()['resource']

def main():
    print("---------")
    apikey = "your api key"
    url1 = 'https://www.virustotal.com/vtapi/v2/file/scan'
    test_floder = './dataset2/00241_1/'
    pickle_file = open('./pickle/00241_1.pkl','wb')
    response_dict = {}
    for root, dirs, files in os.walk(test_floder):
        for f in files:
            file_src = os.path.join(root, f)
            response_dict[file_src] = getAnalysisId(url1, apikey, file_src)
            print("upload one")
    pickle.dump(response_dict, pickle_file)
    pickle_file.close()

# scan a folder and store the hash value into a pickle
if __name__=='__main__':
    main()
