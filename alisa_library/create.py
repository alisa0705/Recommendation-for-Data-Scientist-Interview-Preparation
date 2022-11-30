from youtubesearchpython import *

Viedo_suggestions = Suggestions(language = 'en', region = 'US')

'''Get the youtube video suggestion for Data Scientist Interview Preparation'''
print(Viedo_suggestions.get('Data Scientist Interview Preparation', mode = ResultMode.json))


'''Search only channels for Data Scientist Interview Preparation'''
channels_Search = ChannelsSearch('Data Scientist Interview Preparation', limit = 6, region = 'US')

print(channels_Search.result())


'''Search only playlists for Data Scientist Interview Preparation'''


playlists_Search = PlaylistsSearch('Data Scientist Interview Preparation', limit = 2)

print(playlists_Search.result())