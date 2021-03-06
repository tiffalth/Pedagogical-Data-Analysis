import json

from pathlib import *

import pandas as pd

import plotly.express as px

from datetime import datetime, timedelta
from dateutil import parser

path = Path("./data/echirp_censored.json")
limit = 100_000

lines = []
"""for testing with small json dataset"""
# with path.open("r", errors="ignore") as json_file:
#     while True:
#         line_string = json_file.readline()
#         if not line_string:
#             break  # End of file
#         line_json = json.loads(line_string)
#         lines.append(line_json)

"""for testing with the bigger json dataset"""
with path.open("r", errors="ignore") as json_file:
    curr_line = 0
    while curr_line < limit or limit == -1:
        curr_line += 1
        line_string = json_file.readline()
        if not line_string:
            break
        line_json = json.loads(line_string)
        lines.append(line_json)


'''question 1'''
'''How many times did students access the video'''
'''NOTE: the code below plots out a bar graph instead'''
'''the range of values for x-axis needs to be changed'''

student_data = {}
for user in lines:
    student = user['actor']['account']['name']
    actionAndDate = {'action': user['verb']['display']['en-US'], 'date': user['timestamp']}
    if student in student_data.keys():
        student_data[student].append(actionAndDate)
    else:
        student_data[student] = [actionAndDate]
#print(student_data)

"""
helper function to get the number of views for a single student
"""
def get_view_count(student_action: list):
    view_count = 0
    for i in student_action:
        if i['action'] == 'viewed':  # verb will be either 'viewed' or 'played'
            view_count += 1

    return view_count

"""
helper function to get number of views for all students
"""
def get_view_count_list(student_data: dict):
    view_count_list = []
    for student, student_action in student_data.items():
        count = get_view_count(student_data[student])
        view_count_list.append(count)

    return view_count_list

# getting list of number of views
view_count = get_view_count_list(student_data)
# getting list of student IDs
studentID = list(student_data.keys())

# combining student IDs and no. of views into one dataframe
df = pd.DataFrame(zip(studentID, view_count))
df = df.rename(columns={0: "studentID", 1: "view_count"})
df = df.sort_values(by="studentID", ascending=False)
#print(df)

# plotting histogram of number of views by student
fig = px.histogram(df, x='studentID', y='view_count')
fig.show()

"""question 4"""
"""Does interactivity within a video encourages more interaction
        than a video where students choose when to pause"""
"""the code below looks at only [interactive] videos"""
"""the code for both [interactive] and [non-interactive] videos
        are with Kush"""

data = {}
for user in lines:
    video = user["object"]['id']
    action = user['verb']['display']['en-US']
    if video in data.keys():
        data[video].append(action)
    elif "player.html" in video:  # all videos end with a "player.html" link
        data[video] = [action]
#print(data)

student_data1 = {}
for video, action in data.items():
    if "answered" in action:
        student_data1[video] = len(action)  # count the number of actions done in a single video
#print(student_data1)

# converting dictionary into Dataframe and re-formating it
df1 = pd.DataFrame.from_dict(student_data1, orient="index")
df1 = df1.reset_index()
df1 = df1.rename(columns={"index": "video", 0: "counts of interaction"})
#print(df1)

fig1 = px.line(df1, x="video", y="counts of interaction", markers=True)
fig1 = fig1.update_xaxes(showticklabels=False)
fig1.show()

"""question 3"""
"""How did students use/progress through the video
        (click / pause / play / seek """

student_data2 = {}
for user in lines:
    video = user["object"]['id']
    student = user['actor']['account']['name']
    action = user['verb']['display']['en-US']
    if video in student_data2.keys():
        if student in student_data2[video].keys():
            student_data2[video][student].append(action)
        elif student not in student_data2[video].keys():
            student_data2[video][student] = [action]
    elif "player.html" in video:
        student_data2[video] = {}
        student_data2[video][student] = [action]
# print(student_data2)

# initializing empty list for:
# progression through the video
# actions done per student per video
# student and the particular video they watched
step_list = []
action_list = []
student_video_list = []

i = 1
for video in student_data2.keys():
    video_link = f'Video {i} <a href="' + video + '">Link</a>'  # creating hyperlink for video
    for student in student_data2[video].keys():
        steps = []
        step_number = 1
        for action in student_data2[video][student]:
            steps.append(step_number)
            step_number += 1  # counting the progression step through the video
            action_list.append(action)
            student_video_list.append("{}, {}".format(student, video_link))
        step_list.extend(steps)
    i += 1

# creating dict from the 3 lists, then converting that into a Dataframe
dict2 = {'student_video': student_video_list,
         'action': action_list,
         'step': step_list}
df2 = pd.DataFrame(dict2)
#print(df2)

fig2 = px.scatter(df2, x='step', y='student_video', color='action', symbol='action')
fig2.show()
