#should be quite a simple program thus one class should suffice
import os,sys
downloadsPath = ""

docs = ['pdf','docx','doc','pptx','ppt','pps','odp','rtf'] #split into presentations/pdfs and txt files
data = ['csv','txt','json','yaml','xlsx','xls','xlsm','sql','html','data','xml','cfg']
media = ['png','jpg','mp3','mp4','m4v','mkv','swf','flv','avi','gif','wav','bmp','jpeg','ico','ps','psd','svg']
archives = ['zip','tar.xz','rar','7z','iso'] #check for xz then check for a 'tar' before it
runnables = ['exe','msi','jar','py','js','bat','c','cpp','h'] 
torrents = ['torrent']
Other = []
ignore = []

def move(oldPath,newPath):
    print("moved")

def checkFolder():
    downloadsPath