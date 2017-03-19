from six.moves.urllib.request import urlopen
import csv
import time
import random

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

hashtags = ['ferraricollector_davidlee', 'millionaire_mentor', 'andreeacristina', 'mikeescamilla', 'coryrichards', 'baddiewinkle', 'freddieharrel', 'camillecharriere', 'styleismything', 'alealimay', 'krystal_bick', 'gabifresh', 'blakevond', 'thatschic', 'garypeppergirl', 'chrisellelim', 'margaret__zhang', 'Zanitazanita', 'Alexnoiret', 'ThriftsandThreads', 'SylviaHaghjoo', 'SrhMikaela', 'hannastefansson', 'hannelim', 'blackbeautybag', 'girlwithcurves', 'mybelonging', 'rhodesaaron', 'michaelturchinart', 'paulwheatthins', 'chrissalgardo', 'markelwilliams', 'stevenkelly', 'summerferguson', 'maryleest', 'alancummingsnaps', 'violetchachki', 'samuelanthony', 'nicoleguerriero', 'jilly_peppa', 'arikasato', 'annlestyle', 'marke_miller', 'rhodesaustin', 'mattdallas', 'asenseofhuber', 'stassiebaby', 'sapirazulaybe', 'gregorymichael']

for hashtag in hashtags:
    filename_in = 'output_hashtag/' + hashtag + '.txt'
    filename_out = 'output_hashtag_info/' + hashtag + '_info.txt'
    with open(filename_in, 'r') as f_in:
        with open(filename_out, 'w') as f_out:
            header = next(f_in)
            #f_out.write(header.strip('\n') + ', user_id\n')
            for row in f_in:
                row = row.strip('\n')
                post_id = row.split(',')[1]
                user_id = row.split(',')[6]
                if user_id == '-1':
                    try:
                        link = 'https://www.instagram.com/p/'+ post_id
                        response = urlopen(link)
                        content = str(response.read());

                        start_index = (content.index('"owner": {"id": "')) + len('"owner": {"id": "')

                        test_string = ''

                        for collect in range(14):
                            test_string = test_string + content[start_index]
                            start_index = start_index + 1

                        edit_string = ''

                        for char in test_string:
                            if is_number(char) == True:
                                edit_string = edit_string + char
                            else:
                                edit_string = edit_string + ''
                        content = row.strip('\n') + ',' + edit_string + '\n'
                        f_out.write(content)
                        time.sleep(random.uniform(0, 5))
                    except:
                        print('timeout: sleep for 15 mins')
                        time.sleep(15*60)