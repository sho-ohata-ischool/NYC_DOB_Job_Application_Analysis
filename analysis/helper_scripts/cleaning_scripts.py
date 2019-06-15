import pandas as pd
import re
from datetime import datetime

def get_month(s):
	"""Fast retrieval of months from timestamp"""
	month = {timestamp: pd.to_datetime(timestamp).month for timestamp in s.unique()}
	return(s.map(month))

def get_year(s):
	"""Fast retrieval of year from timestamp"""
	year = {timestamp: pd.to_datetime(timestamp).year for timestamp in s.unique()}
	return(s.map(year))

def get_timestamp(s):
	"""Fast retrieval of timestamp connversion from string"""
	timestamps = {timestamp: pd.to_datetime(timestamp) for timestamp in s.unique()}
	return(s.map(timestamps))

def get_date(s):
	"""Fast retrieval of timestamp connversion from string"""
	dates = {timestamp: pd.to_datetime(timestamp).date() for timestamp in s.unique()}
	return(s.map(dates))

def clean_col_name(x):
	"""Pandas column name clean-up of DOB files"""
	x = re.sub("['-.]", "", x)
	x = re.sub('#', 'Num', x)
	x = re.sub(r'\s+', '_', x.strip())
	return(x)

def dollar_to_num(x):
	"""Convert strings with $ sign to float"""
	try:
		if x[0] == "$":
			return(float(x[1:]))
		else:
			return(float(x))
	except:
		return(0)
    
def get_dollar_to_num(s):
	"""Fast lookup of dollar_to_num function""" 
	dollar_num = {dollar: dollar_to_num(dollar) for dollar in s.unique()}
	return(s.map(dollar_num))

def clean_other_desc(x):
	"""
	This function will clean-up the other description column in the DOB Job application dataset
	"""
	try:
		x = re.sub("['-.()]", " ", x).strip().upper()
		x = re.sub(r'\s+', '_', x)
		## attempt to match the string General Construction as much as possible and change to G_C
		if (re.match('GEN+',  x) and re.match('.*CO', x)) or x == 'G_C': 
			if re.match('.*/', x):
				x = '/'.join(['GC']+[x.split('/')[1]])
			elif x != 'GENERATOR':
				x = 'GC'
			else:
				next
		return(x)
	except:
		return(x)

def get_clean_other_desc(s):
	"""Fast lookup of clean_other_desc function""" 
	cleaned_pther_desc = {other_desc: clean_other_desc(other_desc) for other_desc in s.unique()}
	return(s.map(cleaned_pther_desc))

def create_sum_rolling_dates(df, rolling, start, end):
	"""
	Creates a dataframe with the index as consecutive dates with rolling summed features
	df - original data frame that contains some features that will be converted to rolling df. index must be date type
	rolling - number of rows it should be rolling
	start - beginning date 
	end - end date 
	"""
	
	## Initialize the df_rolling with dates as index 
	df_rolling = pd.DataFrame(index=pd.date_range(start=start, end=end))	
	df_rolling = pd.merge(df_rolling, df, left_index=True, right_index=True, how='left')
	df_rolling.fillna(0,inplace=True)
	df_rolling = df_rolling.transform(lambda x: x.rolling(rolling).sum())
	return(df_rolling)