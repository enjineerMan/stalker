from django.shortcuts import render
from django.http import HttpResponse
from .utils import google_search
import json

# Create your views here.
def profiles(request):
    if request.method == 'GET':
        fields = {
            "first_name" : request.GET.get('firstNameInput', ''),
            "last_name" : request.GET.get('lastNameInput', ''),
            "high_school" : request.GET.get('highSchoolInput', ''),
            "college" : request.GET.get('collegeInput', ''),
        }
        search_string = ""
        for field in fields:
            search_string += fields[field] + " "
        print(search_string)
        raw_data = google_search(search_string.strip())

    results = []
    for item in raw_data.get('items', []):
        metatags = item.get('pagemap', {}).get('metatags', [{}])[0]
        result = {
            "website": item.get("displayLink"),
            "link": item.get("link"),
            "description": metatags.get("og:description")
        }
        results.append(result)

    # Format the results as a JSON object
    filtered_data = json.dumps(results, indent=4)
    print(filtered_data)

    formatted_data = {}
    for item in filtered_data:
        if item["website"] not in formatted_data:
            formatted_data[item["website"]] = [
                {
                    "link": item.get("link"),
                    "description": item.get("description")
                }
            ]
        else:
            formatted_data[item.get("website")].append({
                "link": item.get("link"),
                "description": item.get("description")      
            })
    print(formatted_data)
        # Process the data (e.g., save to database, perform search, etc.)

    return render(request, 'profiles/webpage.html')