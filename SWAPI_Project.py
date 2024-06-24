#!/usr/bin/env python3

"""
Personal Project that interacts with The Star Wars API (https://swapi.dev/).
Queries Topics, Subjects and then the Stats and Info for Subjects, and Outputs
in Print Statements.  Interaction is done through Inputs.  
Requirements: Python 3.12.3 (or greater)
By John Hawkins | johnhawkins3d@gmail.com | linkedin.com/in/johnhawkins3d 
"""


import urllib.error
import urllib.request, json
import requests


main_url = "https://swapi.dev/api/"
topics_list = []  # what's used to store the tpics in swapi.dev/api/*
subjects_list = []
tries = 30
count = 1
index = 1


# Using this def to grab the main topics, and then the subjects derived from those topics
# each of these end up outputting to two lists (topics list from main url and then subject
# list from chosen topics)
def get_url_info(site_url: str):

    with urllib.request.urlopen(site_url) as url:
        data = json.load(url)

    return data


# Using this def to pick a int that corresponds to an index from topic and subjects picked.
# in addition, since indexs start from 0, but user seletion start from 1,
# Im subtracking -1 from user inptu to match the index chosen.
def pick_selection(selection: int, url_list: str):

    while True:

        if selection.isdigit():
            selection = int(selection)

            if (selection - 1) in range(
                len(url_list)
            ):  # i did a subtract 1 from user's picked index it matches the list index
                break

            else:
                selection = input("Number selected not in range!  Pick from [1-X]: ")

        else:
            selection = input("Not a number.  Pick from [1-X]: ")

    return selection


if __name__ == "__main__":
    # Im requesting the url info from SWAPI, which contains the topics, and appending them
    # to a list to print them out to the print console.
    site_topics = get_url_info(main_url)

    for x, y in site_topics.items():
        topics_list.append(y)

    print("Welcome to SWAPI, please pick from the following topics:")
    for x in topics_list:
        print(
            "[" + str(index) + "] " + x[22:-1] # the index adds a [number] before the topic to make selection easier
        )  # Printing out the topics to console, and slicing unecessary bits.
        index += 1

    pick_topic = input("Selection: ")
    picked_topic = pick_selection(pick_topic, topics_list)
    get_topic = topics_list[(int(pick_topic) - 1)]

    count = 1

    # I added this part in, because SWAPIs dictionaries iterate through numbers for each topic or subjects,
    # but ran into an issue where some numbers are blank and return 404, while the following are good.
    # So I had the python script give a max try amounts as it iterates through the list.  If a certain amount of
    # 404 requests are reached then it will stop printing out results.
    while tries != 0:

        test = topics_list[picked_topic - 1] + str(count) + "/"
        r = requests.head(test)

        if r.status_code == 200:

            subjects_list.append(topics_list[picked_topic - 1] + str(count) + "/")

        else:
            tries -= 1

            if tries == 0:
                break

        count += 1

    print(
        "Thanks for picking the topic "
        + get_topic[22:-1]
        + "!  Now select from the following subjects: "
    )

    # I wante to parse the data cleanly and only get the names or titles returned instead of the
    # whole json or dict file, which is not very user-readable in console.  # SWAPI only seems to
    # have either a 'name' or 'title' for most of the subjects in the topics covered.
    index = 1
    for x in subjects_list:
        with urllib.request.urlopen(x) as url:
            data = json.load(url)

        for x, y in data.items():
            if x == "name" or x == "title":
                print("[" + str(index) + "] " + y) # the index adds a [number] before the subject to make selection easier
        index += 1

    pick_subject = input("Selection: ")
    picked_subject = pick_selection(pick_subject, subjects_list)

    with urllib.request.urlopen(subjects_list[picked_subject - 1]) as url:
        data = json.load(url)

    try:
        print("Retrieving Info and Stats for " + data["name"] + ".")

    except:
        print("Retrieving Info and Stats for " + data["title"] + ".")

    # this is just breaking down the data in the returned json format to something a little
    # cleaner that outputs in the console.
    for x, y in data.items():
        if y != None or y != "[]":
            print(x + ":", y)

    exit
