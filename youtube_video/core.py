import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os
from dotenv import load_dotenv
load_dotenv()

try:
    DEVELOPER_KEY = 'AIzaSyDs3yLNqC_J_QL6d7wqkbp2ex_inGqYAF8'
    youtube = build('youtube', 'v3', developerKey=os.getenv("DEVELOPER_KEY"))
except Exception as e:
    print(e)

class Search:
    
    def __init__(self,query:str) -> None:

        self.query=query
         
    def videos(self) -> list:
       
        request = youtube.search().list(
            part="snippet",   
            q=self.query
        )      
        response = request.execute()

        videos=[]

        for i in response["items"]:

            if "channelId" in i["id"]:
                videos.append("channelId:{}".format(i["id"]["channelId"]))
            elif "videoId" in i["id"]:
                video="https://www.youtube.com/watch?v={}".format(i["id"]["videoId"])
                videos.append(video)

        return videos

class Video:

    def __init__(self,url:str):

        self.url=url

    def title(self):
            
        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["title"]
    
    def description(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["description"]
    
    def thumbnails(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["thumbnails"]["medium"]["url"]
    
    def channelId(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["channelId"]
    
    def publishedAt(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["publishedAt"]
    
    def Id(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["id"]
    
    def channelTitle(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["item"][0]["snippet"]["channelTitle"]
    
    def etag(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["etag"]
    
    def caption(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["etag"][0]["snippet"]["tags"][0]
    
    def defaultAudioLanguage(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["etag"][0]["snippet"]["defaultAudioLanguage"]
    
    def categoryId(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["etag"][0]["snippet"]["categoryId"]
    
    def liveBroadcastContent(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["etag"][0]["snippet"]["liveBroadcastContent"]

    def defaultLanguage(self):

        id=self.url[self.url.index("v")+2:self.url.index("&")]
        
        request = youtube.videos().list(
            part= "snippet", 
            id= id 
        )
            
        res=request.execute()
        
        return res["etag"][0]["snippet"]["defaultLanguage"] 