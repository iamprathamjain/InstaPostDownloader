import instaloader,os
import shutil
from random import randint as ri

def download_instagram_reel(url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()
    uniqueID=ri(1000,9999)

    # Load the Instagram post
    try:
        
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])      
        # print('post',post)
        # print('post',post.comments)
        # print('post',post.likes)
        # print('post',post.caption)
        # print("Reel URL:", post.url)
        # print("Owner username:", post.owner_username)
        postdetails={"id":uniqueID,'caption':post.caption,"owner":post.owner_username,'url':post.url,'likes':post.likes,"comments":post.comments}
        loader.download_post(post, target=f"just{uniqueID}")
        print("Instagram reel downloaded successfully.")
        return postdetails
    except Exception as e:
        print("Failed to download Instagram reel:", str(e))

# Example usage

# reel_url = "https://www.instagram.com/reels/CtSoNueAswy/"
# download_instagram_reel(reel_url)

