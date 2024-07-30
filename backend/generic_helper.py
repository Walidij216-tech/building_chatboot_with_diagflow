import re
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""
def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result
    

if __name__ =="__main__":
    print(extract_session_id("projects/texas-fast-food-restauran-ctp9/agent/sessions/95ad47e-9e9e-59fe-82ee-389a6045b8ed/contexts/on-going-order"))
    print(get_str_from_food_dict({"pizza":2,"sandwitch":3}))

