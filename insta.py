import instaloader

def download_instagram_reel(url):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    # Load the Instagram post
    try:
        
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        print(post)
        # Download the Instagram reel
        loader.download_post(post, target=f"reels/")
        print("Instagram reel downloaded successfully.")
    except Exception as e:
        print("Failed to download Instagram reel:", str(e))

# Example usage

reel_url = "https://www.instagram.com/p/CuXeKtHAgqv/"
download_instagram_reel(reel_url)
loader = instaloader.Instaloader()
try:
    loader.download_saved_posts()
    print("Saved posts downloaded successfully!")
except instaloader.exceptions.QueryReturnedNotFoundException:
    print("No saved posts found.")