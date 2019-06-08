import requests
import os

def main():
	## DOB data portal for DOB job permits 1/1/2001-Present 
	## https://data.cityofnewyork.us/Housing-Development/DOB-Job-Application-Filings/ic3t-wcy2/data
	dob_job_csv_url = 'https://data.cityofnewyork.us/api/views/ic3t-wcy2/rows.csv?accessType=DOWNLOAD'
	r = requests.get(dob_job_csv_url)
	data_path = os.path.join('..', 'data', 'raw', 'DOB_job_application.csv')

	with open(data_path, 'wb') as f:
	    f.write(r.content)

	dob_permits_csv_url = 'https://data.cityofnewyork.us/api/views/ipu4-2q9a/rows.csv?accessType=DOWNLOAD'
	r = requests.get(dob_permits_csv_url)
	data_path = os.path.join('..', 'data', 'raw', 'DOB_job_permits.csv')

	with open(data_path, 'wb') as f:
	    f.write(r.content)

if __name__ == "__main__":
	main()