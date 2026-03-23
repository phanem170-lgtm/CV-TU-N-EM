from googleapiclient.discovery import build

# credentials https://console.cloud.google.com/
api_key = "AIzaSyB_Gp0sgVARxKhD163Fcd_-b4n2GV_MXLA"
video_id = "qjwOVRiBxj4"

# build a resource for youtube
resource = build('youtube', 'v3', developerKey=api_key)

# create a request to get 20 comments on the video
request = resource.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=20,  # get 20 comments
    order="relevance"  # top comments
)

# execute the request
response = request.execute()

# get first 10 items from 20 comments
items = response["items"][:10]

print("----------------------------------------")

for item in items:
    item_info = item["snippet"]
    
    # the top level comment can have sub reply comments
    topLevelComment = item_info["topLevelComment"]
    comment_info = topLevelComment["snippet"]
    
    print("Comment By:", comment_info["authorDisplayName"])
    print("Comment Text:", comment_info["textDisplay"])
    print("Likes on Comment:", comment_info["likeCount"])
    print("Comment Date:", comment_info["publishedAt"])
    print("--------\n")