import re
import json
import requests

def convert_to_json(data):
    result = []
    current_name = None
    current_description = None

    for item in data:
        # Match the pattern '1.', '2.', etc., to find names
        match = re.match(r'^\d+\.\s*(.*)', item)
        if match:
            if current_name and current_description:
                # Add the previous place to the result
                result.append({"name": current_name, "description": current_description})
            
            # Update current place name and reset description
            current_name = match.group(1).strip()
            current_description = None
        elif current_name and not current_description and item:
            # The first sentence after the name is the description
            current_description = item.split(".")[0].strip() + "."
    
    # Add the last place if present
    if current_name and current_description:
        result.append({"name": current_name, "description": current_description})

    return result


# DB에 여행지 데이터 입력용 반복문
from GoTravel.models import jeju, gyeongju, jeonju, yeosu

def input_data_toDB(destinations):
    for destination in destinations:
        entry = gyeongju(title = destination["name"], desc = destination["description"])
        entry.save()