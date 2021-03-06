import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videopop.settings')

import django
django.setup()

from youName import getVideoName
from youParse import crawl
from app.models import Video

def populate():
    print "inside populate"
    videoList = crawl(
        "https://www.youtube.com/watch?v=CevxZvSJLk8&list=PLWRJVI4Oj4IaYIWIpFlnRJ_v_fIaIl6Ey")
    

    for url in videoList:
        videoid = url.split("=")[1]
        name = getVideoName(videoid)
        add_video(name, url, videoid)
        print url

        
    
def add_video(name, url, videoid):
    v = Video.objects.get_or_create(name = name)[0]
    v.url = url
    v.videoid = videoid
    v.correctAnswer = name
    v.save()
    return v

# Start execution here!
if __name__ == '__main__':
    print "Starting VideoPop population script..."
    populate()

