#import random
import requests
from bs4 import BeautifulSoup

def youtube_spider(max_pages):

    write_to_file = False
    page = 1
    vid_num = 0

    print("Please input what you want to search...")
    search_item = input("")
    search_item.replace(" ", "+")
    print("Searching...")

    #file writing
    file_name = "youtube search results " + search_item + ".txt"

    print("Would you like to save these results to a file?")
    yn = input("")

    if yn is "n":
        print("Exiting...")
    elif yn is "y":
        print("Creating file...")
        fw = open(file_name, "w")
        write_to_file = True

    #main loop
    while page <= max_pages:
        url = "https://www.youtube.com/results?q=" + search_item + "&page=" + str(page)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, "html.parser")

        #finds the amount of results.
        results_amount = soup.find('p', {'class': 'num-results'})
        result_num = results_amount.string
        print('Found', str.lower(result_num), "in total. \n")

        #vid_results = soup.find('span', {'aria-hidden': 'true'})
        #vid_time = link.string

        #gets the links and titles for the videos.
        for link in soup.findAll('a', {'class': 'yt-uix-tile-link'}):
            title = link.get('title')
            yt_link = "(https://www.youtube.com" + link.get('href') + ")"
            href = link.get('href')
            vid_num += 1

            video = "Video: " + title + yt_link + "\n"
            playlist = "Playlist: " + title + yt_link + "\n"
            channel = "Channel: " + title + yt_link + "\n"

            #finds out which results is a video, playlist, or channel.
            if "watch" and "&list=" in href:
                if write_to_file:
                    fw.write(playlist)
                    print(playlist)
                else:
                    print(playlist)
            elif "watch" in href:
                if write_to_file:
                    fw.write(playlist)
                    print(video)
                else:
                    print(video)
            elif "user" or "channel" in href:
                if write_to_file:
                    fw.write(playlist)
                    print(channel)
                else:
                    print(channel)

            #for test in soup.findAll('span', {'class': 'video-time'}):
                #vid_test = test.string
                #print(vid_test)

        page += 1

        print("Showing", vid_num, "Results \n")

        if write_to_file:
            fw.close()
        else:
            break

youtube_spider(1)
