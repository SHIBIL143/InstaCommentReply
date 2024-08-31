import os
import logging
from instagrapi import Client

# Configure logging
logging.basicConfig(filename='instabot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Initialize the client
    cl = Client()

    # Log in using environment variables for better security
    username = os.getenv("shibil_gamer")
    password = os.getenv("@SHIBIL@SANU@6238910801@")
    cl.login(username, password)
    logging.info("Logged in successfully.")

    # The reel link and DM message content
    reel_link = "https://www.instagram.com/reel/C_GX3xTPClo/"
    dm_message = "Here is the link you requested: [Your Link]"

    # Get the media PK (Primary Key) from the reel link
    reel_pk = cl.media_pk_from_url(reel_link)
    logging.info(f"Reel PK: {reel_pk}")

    # Fetch the comments from the reel
    comments = cl.media_comments(reel_pk)
    logging.info(f"Total comments fetched: {len(comments)}")

    # Loop through each comment and send a DM if it contains the keyword "LINK"
    for comment in comments:
        if "test" in comment.text.upper():
            user_id = comment.user.pk  # Get the user ID from the comment
            cl.direct_send(dm_message, [user_id])
            logging.info(f"Sent DM to {comment.user.username}")

    # Logout after the operations are complete
    cl.logout()
    logging.info("Logged out successfully.")

except Exception as e:
    logging.error(f"An error occurred: {e}")
