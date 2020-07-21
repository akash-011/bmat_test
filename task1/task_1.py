import json
import pandas as pd
from pymongo import MongoClient

data = pd.read_csv('db_works_test.csv')
data_json = json.loads(data.to_json(orient='records'))
results = []
client = MongoClient('localhost', 27017)
print("Connected to MongoDB")
db = client['bmat_test']
collections = db['records']


def add_new_record(row):
	result = {
		"ISWC": row["ISWC"],
		"titles": [],
		"right_owners": [{
			"name": row["RIGHT OWNER"],
			"role": row["ROLE"],
			"ipi": row["IPI NUMBER"]
		}],
		"_id": row['ID SOCIETY'],
	}
	if row['ORIGINAL TITLE']:
		title = {
			"name": row['ORIGINAL TITLE'],
			"type": "OriginalTitle"
		}
		result['titles'].append(title)

	if row['ALTERNATIVE TITLE 1']:
		alt_title_1 = {
			"name": row["ALTERNATIVE TITLE 1"],
			"type": "AlternateTitle1"
		}
		result['titles'].append(alt_title_1)

	if row[" ALTERNATIVE TITLE 2"]:
		alt_title_2 = {
			"name": row[" ALTERNATIVE TITLE 2"],
			"type": "AlternateTitle2"
		}
		result['titles'].append(alt_title_2)

	if row['ALTERNATIVE TITLE 3']:
		alt_title_3 = {
			"name": row["ALTERNATIVE TITLE 3"],
			"type": "AlternateTitle3"
		}
		result['titles'].append(alt_title_3)

	return result


def add_new_owner(row):

	owner = {
		"name": row["RIGHT OWNER"],
		"role": row["ROLE"],
		"ipi": row["IPI NUMBER"]
	}
	return owner


for row in data_json:
	if not any(result["ISWC"] == row["ISWC"] for result in results):
		results.append(add_new_record(row))
	else:
		results[-1]["right_owners"].append(add_new_owner(row))

collections.insert_many(results)
print("Records have been added to MongoDB")
