# youtube_video

```py
pip install youtube-videos-py
```
Search videos , get video's informations.

# Start

```py
import youtube_video as youtube

Search=youtube.Search("query")
Video=youtube.Video("url")
```
# Usage
### Search videos
```py
import youtube_video as youtube

Search=youtube.Search("query")

Search.videos() #get a list of videos
```
### Video's informations

```py
import youtube_video as youtube

Video=youtube.Video("url")

Video.title() #get video's title

Video.description() #get video's description

Video.thumbnails() #get video's thumbnails

Video.channelId() #get video's channelId

Video.publishedAt() #get video's publishedAt

Video.Id() #get video's Id

Video.channelTitle() #get video's channelTitle

Video.etag() #get video's etag

Video.caption() #get video's caption

Video.defaultAudioLanguage() #get video's defaultAudioLanguage

Video.categoryId() #get video's categoryId

Video.liveBroadcastContent() #get video's liveBroadcastContent

Video.defaultLanguage() #get video's defaultLanguage
```
