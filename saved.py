import instaloader

def download_stories(username):
    try:
        L = instaloader.Instaloader()

        # Log in to your Instagram account
        L.login("lifefactsshorts365", "prathamjain399826")

        profile = instaloader.Profile.from_username(L.context, username)

        # Download stories
        L.download_stories(userids=[profile.userid], filename_target='static/insta')

        print("Stories downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")


    # Replace 'nostalgikmusix' with the username from which you want to download stories
download_stories('nostalgikmusix')
