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
'''py
import youtube_video as youtube

Video=youtube.Video("url")

Video.title()

Video.description()

Video.thumbnails()

Video.channelId()

Video.publishedAt()

Video.Id()

Video.channelTitle()

Video.etag()

Video.caption()

Video.defaultAudioLanguage()

Video.categoryId()

Video.liveBroadcastContent()

Video.defaultLanguage()
```
