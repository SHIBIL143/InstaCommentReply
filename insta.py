from instabot import Bot
import time

# Initialize bot instance
bot = Bot()

# Login to Instagram
bot.login(username="shibil_gamer", password="pass")

# Define Reels with corresponding keywords and reply messages
reels_keywords_responses = {
    "C_GX3xTPClo": {
        "Link": "Thank You For Watching Reel !  Download Link: https://shibilgamer.online/mc-download",
        "link": "Thank You For Watching Reel !  Download Link: https://shibilgamer.online/mc-download"
    },
    "reel_id_2": {
        "cool": "Glad you liked Reel 2! Check your DMs for something special.",
        "free": "Yes, Reel 2 content is free! More details sent to your DM."
    },
    # Add more Reels and keyword-response pairs as needed
}

# Monitor comments and auto-reply based on keywords per reel
def monitor_comments():
    for reel_id, keywords_responses in reels_keywords_responses.items():
        # Fetch the comments on the specific Reel
        comments = bot.get_media_comments(reel_id)

        for comment in comments:
            comment_text = comment['text'].lower()
            # Check if the comment contains any of the keywords for this specific Reel
            for keyword, response in keywords_responses.items():
                if keyword in comment_text:
                    user_id = comment['user']['pk']
                    bot.send_message(response, user_id)
                    print(f"Sent DM to {comment['user']['username']} for Reel {reel_id} with message: {response}")

# Run the monitor_comments function periodically
while True:
    monitor_comments()
    time.sleep(60)  # Check every 60 seconds
