import requests
from bs4 import BeautifulSoup

def youtube_spider(max_pages):
    page = 1
    vid_num = 0

    #main loop
    while page <= max_pages:
        url = "https://www.youtube.com/results?q=python+tutorial&page=" + str(page)
        source = requests.get(url)
        text = source.text
        soup = BeautifulSoup(text, "html.parser")

        #finds the amount of results.
        results_amount = soup.find('p', {'class': 'num-results'})
        result_num = results_amount.string
        print('Found', str.lower(result_num), "in total. \n")

        #gets the links and titles for the videos.
        for link in soup.findAll('a', {'class': 'yt-uix-tile-link'}):
            title = link.get('title')
            yt_link = "(https://www.youtube.com" + link.get('href') + ") \n"
            href = link.get('href')
            vid_num += 1;

            #finds out which results is a video, playlist, or channel.
            if "watch" and "&list=" in href:
                print("Playlist:", title, yt_link)
            elif "watch" in href:
                print("Video:", title, yt_link)
            elif "user" or "channel" in href:
                print("Channel:", title, yt_link)

        print("Showing", vid_num, "Results")
        page += 1

youtube_spider(2)