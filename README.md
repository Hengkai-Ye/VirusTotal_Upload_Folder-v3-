# VirusTotal_Upload_Folder
* If the folder contains many files.(eg. a virusshare dataset contains 60+ files). Run `devide.py` to devide the folder.
* Run `scan.py` to upload files and obtain their hash values. These hash values are stored in a pickle file.
* Run `report.py` to retrieve report.If less than 5 engines detect malicious, move the file to 'benign' folder. The detection details are stored in the report folder.

