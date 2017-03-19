#!/usr/bin/env ruby
require 'insta_scrape'

#hashtags = ['ferraricollector_davidlee', 'millionaire_mentor', 'andreeacristina', 'mikeescamilla', 'coryrichards', 'baddiewinkle', 'freddieharrel', 'camillecharriere', 'styleismything', 'alealimay', 'krystal_bick', 'gabifresh', 'blakevond', 'thatschic', 'garypeppergirl', 'chrisellelim', 'margaret__zhang', 'Zanitazanita', 'Alexnoiret', 'ThriftsandThreads', 'SylviaHaghjoo', 'SrhMikaela', 'hannastefansson', 'hannelim', 'blackbeautybag', 'girlwithcurves', 'mybelonging', 'rhodesaaron', 'michaelturchinart', 'paulwheatthins', 'chrissalgardo', 'markelwilliams', 'stevenkelly', 'summerferguson', 'maryleest', 'alancummingsnaps', 'violetchachki', 'samuelanthony', 'nicoleguerriero', 'jilly_peppa', 'arikasato', 'annlestyle', 'marke_miller', 'rhodesaustin', 'mattdallas', 'asenseofhuber', 'stassiebaby', 'sapirazulaybe', 'gregorymichael']
hashtags = ['stevenkelly', 'summerferguson', 'maryleest', 'alancummingsnaps', 'violetchachki', 'samuelanthony', 'nicoleguerriero', 'jilly_peppa', 'arikasato', 'annlestyle', 'marke_miller', 'rhodesaustin', 'mattdallas', 'asenseofhuber', 'stassiebaby', 'sapirazulaybe', 'gregorymichael']

hashtags.each do |hashtag|
  scrape_result = InstaScrape.long_scrape_hashtag(hashtag, 30, include_meta_data: true)
  filename = 'output_hashtag/' + hashtag + ".txt"
  file = File.open(filename, "w:UTF-8")
  file.puts 'hashtag, post_id, image, link, text, date, user_id'

  scrape_result.each do |post|
    post_id = post.link.split('/')[4]
    content = [hashtag.delete(','), post_id.delete(','), post.image.delete(','), post.link.delete(','), post.text.delete(','), post.date.delete(','), '-1'].join(",")
    file.puts content
  end

  puts 'Finish collecting ' + hashtag + ' => ' +scrape_result.length.to_s
end