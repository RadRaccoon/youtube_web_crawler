import requests
from bs4 import BeautifulSoup

def youtube_spider():

    max_pages = 1
    write_to_file = False
    page = 1
    vid_num = 0

    print("Please input what you want to search...")
    search_item = input("")
    search_item.replace(" ", "+")

    #file writing
    file_name = "youtube search results " + search_item + ".txt"

    print("Would you like to save these results to a file? y/n")
    yn = input("")

    if yn is "n":
        print("Exiting...")
    elif yn is "y":
        print("Creating file...")
        fw = open(file_name, "w", encoding='utf-8')
        write_to_file = True
    print("Searching...")

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
            yt_link = "(https://www.youtube.com" + link.get('href') + ")"

            video = "Video: " + link.get('title') + yt_link + "\n"
            playlist = "Playlist: " + link.get('title') + yt_link + "\n"
            channel = "Channel: " + link.get('title') + yt_link + "\n"

            vid_num += 1

            #finds out which results is a video, playlist, or channel.
            if "watch" and "&list=" in link.get('href'):
                if write_to_file:
                    fw.write(playlist)
                    print(playlist)
                else:
                    print(playlist)
            elif "watch" in link.get('href'):
                if write_to_file:
                    fw.write(video)
                    print(video)
                else:
                    print(video)
            elif "user" or "channel" in link.get('href'):
                if write_to_file:
                    fw.write(channel)
                    print(channel)
                else:
                    print(channel)


            #for test in soup.findAll('span', {'class': 'video-time'}):
                #vid_test = test.string
                #print(vid_test)

        page += 1

        print("Showing", vid_num, "Results \n")

        print("Show more results? y/n \n")
        yn2 = input("")

        if yn2 is "n":
            if write_to_file:
                fw.close()
            else:
                break
        elif yn2 is "y":
            max_pages += 1

youtube_spider()