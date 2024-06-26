#!/usr/bin/env python3

"""
Personal Project that interacts with The Star Wars API (https://swapi.dev/).
Queries Topics, Subjects and then the Stats and Info for Subjects, and Outputs
in Print Statements.  Interaction is done through Inputs.  
Requirements: Python 3.12.3 (or greater)
By John Hawkins | johnhawkins3d@gmail.com | linkedin.com/in/johnhawkins3d 
"""


import urllib.error, urllib.request, json


MAIN_URL = "https://swapi.dev/api/"
topics_list = []  # what's used to store the tpics in swapi.dev/api/*
subjects_list = []  # what's printed after selecting a topic
count = 1
index = 1
valid = 1


# Using this def to grab the main topics, and then the subjects derived from those topics
# each of these end up outputting to two lists (topics list from main url and then subject
# list from chosen topics)
def get_url_info(site_url: str):

    with urllib.request.urlopen(site_url) as url:
        data = json.load(url)

    return data


# Using this def to pick a int that corresponds to an index from topic and subjects picked.
# in addition, since indexs start from 0, but user seletion start from 1,
# then subtracking -1 from user inptu to match the index chosen.
def pick_selection(selection: int, url_list: str):

    while True:

        if selection.isdigit():
            selection = int(selection)

            if (selection - 1) in range(
                len(url_list)
            ):  # Subtracking 1 from user's picked index so it matches the list index
                break

            else:
                selection = input("Number selected not in range!  Pick from [1-X]: ")

        else:
            selection = input("Not a number.  Pick from [1-X]: ")

    return selection


if __name__ == "__main__":
    # Requesting the url info from SWAPI, which contains the topics, and appending them
    # to a list to print them out to the print console.
    site_topics = get_url_info(MAIN_URL)

    for x, y in site_topics.items():
        topics_list.append(y)

    print("Welcome to SWAPI, please pick from the following topics:")
    for x in topics_list:
        print(
            "["
            + str(index)
            + "] "
            + x[
                22:-1
            ]  # The index adds a [number] before the topic to make selection easier while
        )  # Printing out the topics to console, and slicing unecessary bits.
        index += 1

    pick_topic = input("Selection: ")
    picked_topic = pick_selection(pick_topic, topics_list)
    get_topic = topics_list[(int(pick_topic) - 1)]
    get_count = get_url_info(
        topics_list[picked_topic - 1]
    )  # goes to the topic list main diretory, which has a count of total entries

    print(
        "Thanks for picking the topic "
        + get_topic[22:-1]
        + " - we found "
        + str(get_count["count"])
        + " entries!  Now select from the following subjects: "
    )

    # Once selection is made, iterates through the json list.  Since some entries return 200, or 404, only counts twoard
    # The total valid entries (i.e. return 200) up to the official count from get_count, and ignores the 404 ones.
    while valid < get_count["count"] + 1:

        test_url = topics_list[picked_topic - 1] + str(count) + "/"

        try:
            get_code = urllib.request.urlopen(test_url)
            subjects_list.append(topics_list[picked_topic - 1] + str(count) + "/")

            count += 1
            valid += 1

        except urllib.error.URLError:
            count += 1

    # Parses the data cleanly and only gets the names or titles returned instead of the
    # whole json or dict file, which is not very user-readable in console.
    # SWAPI only seems to have either a 'name' or 'title' for most of the subjects in the topics covered.
    index = 1
    for x in subjects_list:
        print_subjects = get_url_info(x)

        for x, y in print_subjects.items():
            if x == "name" or x == "title":
                print(
                    "[" + str(index) + "] " + y
                )  # the index adds a [number] before the subject to make selection easier
        index += 1

    pick_subject = input("Selection: ")
    picked_subject = pick_selection(pick_subject, subjects_list)
    get_subjects = get_url_info(subjects_list[picked_subject - 1])

    try:
        print("Retrieving Info and Stats for " + get_subjects["name"] + ".")

    except:
        print("Retrieving Info and Stats for " + get_subjects["title"] + ".")

    # this is just breaking down the data in the returned json format to something a little
    # cleaner that outputs in the console.
    for x, y in get_subjects.items():
        try:
            for i in y:
                get_stats_info = get_url_info(i)

                try:
                    print(x + ":", get_stats_info["name"])
                except:
                    print(x + ":", get_stats_info["title"])

        except:
            print(x + ":", y)

    exit
