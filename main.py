
from htmlManager import *
import os
import pandas as pd

seasonLink = "http://nba.win007.com/League/Index_cn.aspx?SclassID=1"
command = 1
path = os.getcwd()
html = path+"\\download" +"\\2004-2005_常规赛_1"

if __name__ =="__main__":
   downloadNbaData(seasonLink)
   #analysHtml(html)

#test


