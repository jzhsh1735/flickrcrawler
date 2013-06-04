import flickrapi
import urllib
import string
import os
import time

api_key = 'your_api_key'
secret = 'your_secret'

# read query
query_retrieve_num = 1000
query_file = open('query_user.txt', 'r')
query_users = string.split(query_file.read())
query_file.close()
#for query_user in query_users:
#    print query_user
print len(query_users)

# flickr api
flickr = flickrapi.FlickrAPI(api_key)
for query_user in query_users:
    path = 'img' + os.path.sep + 'user' + os.path.sep + query_user
    if not os.path.exists(path):
        os.mkdir(path)
    photos = flickr.walk(user_id = query_user, extras = 'tags, url_m')
    tag_file = open(path + os.path.sep + 'tag.txt', 'w')
    current_num = 0
    for photo in photos:
        time.sleep(1)
        url = photo.get('url_m')
        if url is not None:
            print query_user, current_num, url
            print photo.get('tags')
            file_name = path + os.path.sep + str(current_num) + '.jpg'
	    success = False
	    while not success:
                try:
	            urllib.urlretrieve(url, file_name)
		    success = True
		except:
		    pass
	    tag_file.write(photo.get('tags').encode('UTF-8') + '\n')
            current_num += 1
            if current_num >= query_retrieve_num:
                break
        else:
            print 'url is None'
    tag_file.close()
    #temp_path = 'img' + os.path.sep + query_user + '.tar.gz'
    #cmd = 'tar -zcf %s -C %s %s' % (temp_path, 'img' + os.path.sep + 'user', query_user)
    #print cmd
    #os.system(cmd)
    #cmd = 'md5sum %s > %s' % (temp_path, path + '.tar.gz.md5')
    #print cmd
    #os.system(cmd)
    #cmd = 'mv %s %s' % (temp_path, path + '.tar.gz')
    #print cmd
    #os.system(cmd)
