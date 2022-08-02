import urllib.request
from moviepy.editor import VideoFileClip
import os

def convert_video_to_gif(url: str):
   
    #Download video from URL to current directory
    urllib.request.urlretrieve(url, 'tiktok_video.mp4')
    
    #Specify the relative path of the video
    video = VideoFileClip("tiktok_video.mp4")

    #Convert video to GIF
    video.write_gif("tiktok_gif.gif")

    #Get the current working directory
    cwd = os.getcwd()

    #Concatenate absolute and relative pass
    result = cwd + '/tiktok_gif.gif'

    return result


if __name__ == "__main__":
    # Usage example
    url = '''https://v16-webapp.tiktok.com/c7cd22ba817fbe3698a94de6051b5baf/62e90b22/video/tos/useast2a/tos-useast2a-ve-0068c002/177a89a409a84b5d9d6179fc4d9995dc/?a=1988&amp;ch=0&amp;cr=0&amp;dr=0&amp;lr=tiktok_m&amp;cd=0%7C0%7C1%7C0&amp;cv=1&amp;br=1334&amp;bt=667&amp;btag=80000&amp;cs=0&amp;ds=3&amp;ft=gKSYZ8hNo0PD17pC4sg9w1PE75LiaQ2D~bT&amp;mime_type=video_mp4&amp;qs=0&amp;rc=PGhoZmdkOTg4aWc5Nzc0NkBpanI7dTk6Zms7ZTMzNzczM0BgMmAzMDRgXzMxMC4zMS9eYSM0MWdvcjRfYl9gLS1kMTZzcw%3D%3D&amp;l=202208020531330102231000350F8C8560'''
    res = convert_video_to_gif(url)
    print(res)
