# Contributors:
# Harshit Gupta 2022209
# Abhay Kohli 2022015
# Arpan Verma 2022105 
import csv
import requests
file1=open("song.csv",'w')
w=csv.writer(file1)

def getTopAlbums(name):
  url1=f'http://ws.audioscrobbler.com/2.0?method=artist.gettoptracks&artist={name}&api_key=6a8bf03a627917e208476ca6772a097d&format=json'
  res=requests.get(url1)
  data=res.json()
  albums=data["toptracks"]["track"]
  
  return albums
def printTopAlbums(name):
  albums=getTopAlbums(name)
  w.writerow(["song name","last.fm url","youtube url"])
  for i in albums[:min(len(albums),10)]:
    w.writerow([i["name"],i["url"],getSongUrl(i["name"])])
    print(i["name"],i["url"])
    
def getSong(name):
  url2=f'https://www.googleapis.com/youtube/v3/search?key=AIzaSyBnNug4UvlxanhrhXz_uWhjat-Ie0LBLhQ&q={name}&type=video'
  key='AIzaSyBnNug4UvlxanhrhXz_uWhjat-Ie0LBLhQ'
  res=requests.get(url2)
  data=res.json()
  # print(data)
  desc=data["items"][0]["id"]["videoId"]
  url3=f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={desc}&key={key}'
  res=requests.get(url3)
  data=res.json()
  return data
def getSongUrl(name):
   
  data=getSong(name)
  return f'https://www.youtube.com/watch?v={data["items"][0]["id"]}'
def getWriter(name):
  data=getSong(name)
  t=data["items"][0]["snippet"]["description"].lower().split('\n\n')
  # print(t)
  for i in t:
    # print(i)
    # print('...')
    k=i.split('\n')
    l=[]
    for j in k:
      # print(j)
      if "lyrics" in j and len(j)>8:
        
        l.append(j)
  return l
def printWriter(name):
  l=getWriter(name)
  for i in l:
    print(i)

def getSongFromAandW(artist,writer):
  albums=getTopAlbums(artist)
  for  i in albums:
    writers=getWriter(i['name'])
    for j in writers:
      if writer in j.lower():
        w.writerow([artist,i["name"],i["url"],getSongUrl(i["name"]),writer])
        print(i["name"],i["url"])
    
        break
        

while True:
  print('''
  press:
  1: to get top album of a artist
  2:to get the song from the singer and writer
  3:to get url of a song
  4:to get writer of a song
  ''')
  cmd=int(input("Enter Corresponding number: "))
  if cmd==1:
    name=input("Enter Artist Name: ")
    printTopAlbums(name)
  if cmd==2:
    name=input("Enter Singer Name: ")
    lyrics=input("Enter writers name: ")
    print(getSongFromAandW(name,lyrics))
  if cmd==3:
    name=input("Enter Song name")
    print(getSongUrl(name))

  if cmd==4:
    name=input("Enter Song Name: ")
    print(printWriter(name))
  if cmd==5:
    break
file1.close()

    