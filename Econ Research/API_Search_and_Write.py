# @author: Vinay Maruri, vmaruri1@berkeley.edu
# @version: 1.4
#a program that uses google's custom search API
#to return the URLs associated with the top 5 search results.
#outputting them to a CSV file.

import os
assert 'SYSTEMROOT' in os.environ
import csv
from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyD_P-nedrBRHr6TD52H7c0q0tArfqRffNo"
my_cse_id = "008233753726675857215:niwqjfsigge"

#method collects user input and returns the index of search results
# to be parsed
def collectqueryfromuser(query):
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res['items']
    return google_search(query, my_api_key, my_cse_id, num=5)
# here any query can be entered as a string into collectqueryfromuser
results = collectqueryfromuser("Hewlett Packard Enterprise")
temp = []
#this final for loop prints and adds the formatted URLs
#to be outputted into a CSV
for result in results:
    pprint.pprint(result['formattedUrl'])
    temp.append(result['formattedUrl'])

with open('results.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["query: Hewlett Packard Enterprise"])
    writer.writerow(["results:", temp])
