import json
import os

#The data model we're following, where each entity is stored in a JSON format
Data_Files = {
    "users": "users.json",
    "homes": "homes.json",
    "rooms": "rooms.json",
    "devices": "devices.json"
}


def load_data(entity):
    '''Loads data from a JSON File and also checks for errors'''

    try:
        if not os.path.exists(Data_Files[entity]):
            print("Entity does not exist, we'll create one.")
            return create_empty_data(entity) #Returning an empty structure
        
        with open(Data_Files[entity], 'r') as f:
            return json.load(f)
        
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error Loading {entity}: {e}. Returning default structure.")
        return create_empty_data(entity)


def create_empty_data(entity):
    '''Returns and empty structure based on the entity type'''

    if entity in Data_Files:
        return {entity: []} #return empty entity
    else:
        raise ValueError(f"Unknown entity type: {entity}.") #Error messge preventing unknown types


def save_data(entity, data):
    '''Writing data to a JSON file from an Entity'''
    
    try:
        with open(Data_Files[entity], 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise IOError(f'Failed to save {entity}: {e}')


def create_entity(entity, new_item):
    '''Creates a new item to the specified entity while error checking'''

    data = load_data(entity)    #Load existing data

    #Error check for duplicate entity
    if any(item['id'] == new_item['id'] for item in data[entity]):
        raise ValueError(f'{entity} with ID {new_item['id']} already exists.')

    data[entity].append(new_item)   #Append new entity
    save_data(entity, data)         #Save back to JSON

    return new_item #Return newly created entity


def get_entity(entity, entity_id):
    '''Retrieves an entity by its ID'''

    data = load_data(entity)    #Load existing data

    #Error checking to see if id exits
    result = next((item for item in data[entity] if item['id'] == entity_id), None)

    if result is None:
        raise KeyError(f'{entity} with ID {entity_id} not found.')
    else:
        return result   #Return entity if it holds an actual value


def update_entity(entity, entity_id, updates):
    '''Updates an existitng entity'''

    data = load_data(entity)
    for item in data[entity]:   #Ensuring the id exists
        if item["id"] == entity_id:
            item.udpate(updates)
            return item #If we find a match, return the updated entity
        
    raise KeyError(f'{entity} with ID {entity_id} not found.')  #Error message in case entity does not exist 


def delete_entity(entity, entity_id):
    '''Deletes an entity by ID'''

    data = load_data(entity)

    new_data = [item for item in data[entity] if item['id'] != entity_id]

    if(len(new_data) == len(data[entity])):
        raise KeyError(f'{entity} with ID {entity_id} not found.')

    data[entity] = new_data #Update data
    save_data(entity,data)  #Save changes 

    return True #Indicates success