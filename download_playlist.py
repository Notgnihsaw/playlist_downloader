#!/usr/bin/env
import os
from bs4 import BeautifulSoup as bs
import requests
import re
import json
import pandas as pd
import sys

def get_playlist_dict(soup_text):
    # the script we want should be the 33rd script, or it is for this trial
    key_script = soup_text.find_all("script")[33]
    # delete the initial variable setting so we just have the JSON object
    key_script_json = str(key_script.contents[0]).replace("var ytInitialData = ", "")
    
    # delete the final semicolon at the end (if it exists)
    if key_script_json[-1] == ";":
        key_script_json = key_script_json[:-1]
    
    # convert the string into JSON
    playlist_dict = json.loads(key_script_json)
    
    return(playlist_dict)

def get_video_list(playlist_dict):
    
    # extract the meaningful information
    tab_renderer = playlist_dict['contents']["twoColumnBrowseResultsRenderer"]["tabs"][0]['tabRenderer']['content']
    section_renderer = tab_renderer['sectionListRenderer']['contents']
    video_list = section_renderer[0]['itemSectionRenderer']['contents'][0]['playlistVideoListRenderer']['contents']
    
    return(video_list)

def get_participant_info(playlist_dict):
    # get the title of the playlist
    playlist_title = playlist_dict['metadata']['playlistMetadataRenderer']['title']
    
    # separate into participant and type of playlist
    info_list = playlist_title.split()
    
    return({'participant': info_list[0], 'playlist_type':info_list[1].lower()})

def get_video_info(video_element):
    song_title = video_element['playlistVideoRenderer']['title']['runs'][0]['text']
    song_byline = video_element['playlistVideoRenderer']['shortBylineText']['runs'][0]['text']
    
    song_url = 'youtube.com' + video_element['playlistVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    
    if song_byline[-8:] == ' - Topic':
        song_byline = song_byline.replace(' - Topic', '')
    if ' Official' in song_byline:
        song_byline = song_byline.replace(' Official', '')
        
    
    return({"title": song_title, "artist": song_byline, "url": song_url})

def get_full_playlist_info(playlist_link, info=False):
    # get the HTML from the link
    r = requests.get(playlist_link)
    soup = bs(r.text,'html.parser')

    # construct the playlist dictionary
    if info: print('extracting playlist dict')
    full_playlist_dict = get_playlist_dict(soup)
    
    # get the participant info
    if info: print('extracting participant info')
    participant_info = get_participant_info(full_playlist_dict)
    
    # get the video info
    if info: print('extracting vide list')
    video_list = get_video_list(full_playlist_dict)
    
    extracted_videos = []
    
    current_video = 0
    for video in video_list:
        if current_video > 99:
            break
            
        if info: print('adding video', current_video, 'of ', len(video_list), 'videos.')
        extracted_videos.append(get_video_info(video))
        
        current_video += 1
    
    if info: print('building dictionary.')

    output_dict = {'participant': participant_info['participant'], 
                    'playlist_type': participant_info['playlist_type'],
                    'videos': extracted_videos}
    
    return output_dict

def output_dict_to_df(output_dict):
    out_df = pd.DataFrame.from_dict(output_dict['videos'])

    out_df['subject'] = output_dict['participant']
    out_df['playlist_type'] = output_dict['playlist_type']
    
    return out_df

# Run the program with the given arguments

def main(args=None):
    # Isolate args from global arguments
    if args is None:
        # Handle no arguments
        try:
            # Divide options from args
            opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
            args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
        except IndexError:
            raise SystemExit(f"Usage: {sys.argv[0]} [options: -v] [playlist url] [output path]")

        if len(args) < 3:
            raise SystemExit(f"Usage: {sys.argv[0]} [options: -v] [playlist url] [output path]")

        # load in text file of videos to download
        if "-v" in opts:
            verbose = True
        
        # Run the program, first extracting links from the playlist
        playlist_dict = get_full_playlist_info(args[0], verbose)
        output_path = args[1]

        output_df = output_dict_to_df(playlist_dict)

        output_df.to_csv(output_path)


if __name__ == '__main__':
    main()