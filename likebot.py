import requests
import re
import sys
from pprint import pprint

at = ""

def launch():
    global at
    #add your access token here:
    at = str('2l4bfxpO7e51RtJn6T0BhPIH8SnOl7MKMvFmikGh')
    print("Here are your ten most recent groups:")
    groups_data = print_all_groups_with_number_beside_each()
    try:
        group_number = int(raw_input("Enter the number of the group you would like to analyze:"))
        like_number = str(raw_input("Like-0, Dislike-1: "))
        likeUsername = str(raw_input("Enter Groupme Name: "))
        group_id = get_group_id(groups_data, group_number)
        group_name = get_group_name(groups_data, group_id)
        number_of_messages = get_number_of_messages_in_group(groups_data, group_id)
        print("Likeboting " + str(number_of_messages) + " messages from " + group_name)
        analyze_group(group_id, number_of_messages, like_number, likeUsername)
    except ValueError:
        print("Not a number")

def analyze_group(group_id, number_of_messages, like_number, likeUsername):
    response = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+at)
    data = response.json()
    message_with_only_alphanumeric_characters = ''
    message_id = 0
    iterations = 0.0
    while True:
        for i in range(20):  # api 20 message cycle
            try:
                iterations += 1
                name = data['response']['messages'][i]['name']  # sender name
                message = data['response']['messages'][i]['text']  # message text
                timeStamp = data['response']['messages'][i]['created_at']

                try:
                    #  strips out special characters
                    message_with_only_alphanumeric_characters = re.sub(r'\W+', ' ', str(message))
                except ValueError:
                    pass  # special char catch
                sender_id = data['response']['messages'][i]['sender_id']  # sender id
            except IndexError:
                print("Finished")


            if ((str(name) == str(likeUsername))):
                if ((str(like_number) == "0")):

                    requests.post('https://api.groupme.com/v3/messages/' + group_id + '/' + str(
                    data['response']['messages'][i]['id']) + '/like?token=' + at)
                else:
                    requests.post('https://api.groupme.com/v3/messages/' + group_id + '/' + str(
                    data['response']['messages'][i]['id']) + '/unlike?token=' + at)

        if i == 19:
                message_id = data['response']['messages'][i]['id']
                remaining = iterations/number_of_messages
                remaining *= 100
                remaining = round(remaining, 2)
                print(str(remaining)+' percent done, timestamp: ' + str(timeStamp))

        payload = {'before_id': message_id}
        response = requests.get('https://api.groupme.com/v3/groups/'+group_id+'/messages?token='+at, params=payload)
        data = response.json()

#extra Functions
def print_all_groups_with_number_beside_each():
    response = requests.get('https://api.groupme.com/v3/groups?token='+at)
    data = response.json()
    if len(data['response']) == 0:
        print("You are not part of any groups.")
        return
    for i in range(len(data['response'])):
        group = data['response'][i]['name']
        print(str(i)+"\'"+group+"\'")
    return data

def get_group_id(groups_data, group_number):
    group_id = groups_data['response'][group_number]['id']
    return group_id

def get_group_name(groups_data, group_id):
    i = 0
    while True:
        if group_id == groups_data['response'][i]['group_id']:
            return groups_data['response'][i]['name']
        i += 1

def get_number_of_messages_in_group(groups_data, group_id):
    i = 0
    while True:
        if group_id == groups_data['response'][i]['group_id']:
            return groups_data['response'][i]['messages']['count']
        i += 1


launch()

