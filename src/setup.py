import os
from data import raw_data_download

data_path_parent = os.path.join('..', 'data')

for folder in ['raw', 'interim', 'processed']:
	dir_path = os.path.join(data_path_parent, folder)
	os.makedirs(dir_path, exist_ok=True)

raw_data_download.main()
