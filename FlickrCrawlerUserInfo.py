import flickrapi
import urllib
import string
import os
import time

api_key = 'your_api_key'
secret = 'your_secret'

# author of python flickapi
# for more details please refer to http://stuvel.eu/flickrapi
query_user = '73509078@N00'
friends_0 = []
friends_1 = []

friend_file = open(query_user + '.friend.txt', 'w')
friend_graph_file = open(query_user + '.friend.graph.txt', 'w')

# flickr api
flickr = flickrapi.FlickrAPI(api_key)
root = flickr.contacts_getPublicList(user_id = query_user)
friend_file.write(query_user + '\n')
for child in root[0]:
    nsid = child.attrib['nsid']
    friend_graph_file.write(query_user + '\t' + nsid + '\n')
    friends_0.append(nsid)
    friend_file.write(nsid + '\n')
    print nsid
time.sleep(1)

for friend_0 in friends_0:
    root = flickr.contacts_getPublicList(user_id = friend_0)
    for child in root[0]:
        nsid = child.attrib['nsid']
	friend_graph_file.write(friend_0 + '\t' + nsid + '\n')
	if nsid != query_user and not nsid in friends_0 and not nsid in friends_1:
	    friends_1.append(nsid)
	    friend_file.write(nsid + '\n')
	    print nsid
    time.sleep(1)

friend_file.close()
friend_graph_file.close()

print len(friends_0)
print len(friends_1)
