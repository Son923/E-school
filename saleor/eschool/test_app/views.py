import requests
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

import requests
import json

from ..constants import app_id, app_name, app_token

# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
query = """
{
  products(first: 2) {
    edges {
      node {
        id
        name
      }
    }
  }
}
"""


def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    headers = {"Authorization": f"Bearer {app_token}"}
    request = requests.post('http://localhost:8000/graphql/', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

def index(request):
    result = run_query(query) # Execute the query
    products = result["data"] # Drill down the dictionary
    return HttpResponse(f"Body- {products}")
