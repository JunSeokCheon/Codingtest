import re

def solution(new_id):
    answer = ''
    
    temp_id = new_id.lower()
    temp_id = re.sub('[^a-z0-9-_.]', '', temp_id)
    temp_id = re.sub('\.\.+', '.', temp_id)
    temp_id = temp_id.strip('.')
    
    if len(temp_id) == 0:
        temp_id = "a"
        
    if len(temp_id) >= 16:
        temp_id = temp_id[:15]
        temp_id = temp_id.rstrip(".")
            
    if len(temp_id) < 3:
        while len(temp_id) < 3:
            temp_id = temp_id + temp_id[-1]

    answer = temp_id
    return answer