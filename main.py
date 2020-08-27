#should be quite a simple program thus one class should suffice
import os,sys
downloadsPath = ""

docs = ['pdf','docx','doc','pptx','ppt',] #split into presentations/pdfs and txt files
data = ['csv','txt','json','yaml','xlsx','sql','html']
media = ['png','jpg','mp3','mp4','gif']
archives = ['zip','tar.xz','rar','7z','iso'] #check for xz then check for a 'tar' before it
runnables = ['exe','msi','jar','py','js'] 
torrents = ['torrent']
Other = []
ignore = []

def move(oldPath,newPath):
    print("moved")

def checkFolder():
    downloadsPath