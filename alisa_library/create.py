from youtubesearchpython import *

def viedo_suggestions(search):
    '''Get the youtube video suggestion'''
    viedo_suggestions = Suggestions(language = 'en', region = 'US')
    viedo_suggestions=viedo_suggestions.get(search, mode = ResultMode.json)
    return viedo_suggestions


def channels_Search(search):
    '''Search only channels'''
    ChannelsSearch=ChannelsSearch(search, limit = 6, region = 'US')
    return channels_Search.result()

def playlists_Search(search):
    '''Search only playlists'''
    playlists_Search = PlaylistsSearch(search, limit = 2)
    return playlists_Search.result()
