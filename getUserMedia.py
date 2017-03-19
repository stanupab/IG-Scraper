import os
import csv
import sys
import json
import time
import random
from datetime import datetime
from time import gmtime, strftime

#usernames = ['ferraricollector_davidlee', 'millionaire_mentor', 'andreeacristina', 'mikeescamilla', 'coryrichards', 'baddiewinkle', 'freddieharrel', 'camillecharriere', 'styleismything', 'alealimay', 'krystal_bick', 'gabifresh', 'blakevond', 'thatschic', 'garypeppergirl', 'chrisellelim', 'margaret__zhang', 'Zanitazanita', 'Alexnoiret', 'ThriftsandThreads', 'SylviaHaghjoo', 'SrhMikaela', 'hannastefansson', 'hannelim', 'blackbeautybag', 'girlwithcurves', 'mybelonging', 'rhodesaaron', 'michaelturchinart', 'paulwheatthins', 'chrissalgardo', 'markelwilliams', 'stevenkelly', 'summerferguson', 'maryleest', 'alancummingsnaps', 'violetchachki', 'samuelanthony', 'nicoleguerriero', 'jilly_peppa', 'arikasato', 'annlestyle', 'marke_miller', 'rhodesaustin', 'mattdallas', 'asenseofhuber', 'stassiebaby', 'sapirazulaybe', 'gregorymichael']

## Directory hirarchy
## output
## - username
##  - account_stat
##  - account_media
##  - account_comment

def init():
    # Create directories
    directory = './output/account_stat'
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = './output/account_media'
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = './output/account_comment'
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = './output/account_media_around'
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_stat(username):
    # Get Stat
    datetime = strftime("%Y-%m-%d", gmtime())
    outfile = './output/account_stat/ig_stat_'+username+'.txt'
    os.system('instagram-scrape-account-stats -u %s > %s' % (username, outfile))

def get_media(username):
    # Get all media
    print('Collecting media from', username)
    outfile = './output/account_media/ig_post_'+username+'.txt'
    os.system("instagram-screen-scrape posts --username %s > %s" % (username, outfile))
    time.sleep(random.uniform(0, 5))

def get_comments(username):
    # Get comment
    filename = './output/account_media/ig_post_'+username+'.txt'
    with open(filename) as data_file:
        lines = json.load(data_file)
        for line in lines:
            post_id = line['id']
            post_date = datetime.fromtimestamp(line['time'])
            if post_date.day < 5 and post_date.month <= 2 and post_date.year <= 2017:
                break
            outpath = './output/account_comment/'
            outfile_lookup = 'ig_comment_'+username+'_'+post_id+'.txt'
            for root, dirs, files in os.walk(outpath):
                if outfile_lookup not in files:
                    try:
                        print('Collecting comments for %s on %s at %s' % (username, post_id, post_date))
                        outfile = './output/account_comment/ig_comment_'+username+'_'+post_id+'.txt'
                        os.system('instagram-screen-scrape comments --post %s > %s' % (post_id, outfile))
                        time.sleep(random.uniform(0, 5))
                    except:
                        time.sleep(15*60)
                else:
                    print('file exists')
                    break

def main():
    method = sys.argv[1]
    
    csvfile = open("../microceleb-users.csv", "r",encoding='utf-8', errors='ignore')
    #users = csv.DictReader(csvfile, delimiter=',')
    # TODO: Remove nexts
    #for i in range(1, 35):
    #    next(users)
    users = ['rachelc00k']
    error = []
    for u in users:
        #username = u['ig_name'].strip()
        username = u
        print(username)
        
        if method == 'init':
            init()
        elif method == 'stat':
            get_stat(username)
        elif method == 'post':
            get_media(username)
        elif method == 'comment':
            get_comments(username)
        elif method == 'all':
            get_stat(username)
            get_media(username)
            get_comments(username)



if __name__ == '__main__':
    main()
