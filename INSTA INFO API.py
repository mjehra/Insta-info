from flask import Flask, jsonify
import instaloader

# Initialize Flask app
app = Flask(__name__)
loader = instaloader.Instaloader()

@app.route("/instagram/<username>", methods=["GET"])
def get_instagram_info(username):
    """ Fetch Instagram profile info by username """
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        # Structured JSON response with better formatting
        user_info = {
            "status": "success",
            "data": {
                "username": profile.username,
                "full_name": profile.full_name,
                "bio": profile.biography,
                "followers": profile.followers,
                "following": profile.followees,
                "total_posts": profile.mediacount,
                "profile_picture_url": profile.profile_pic_url
            },
            "message": "Public profile data retrieved successfully.",
            "developer": {
                "name": "Mehraj [Ehra]",
                "github": "https://github.com/mjehra",
                "telegram": "@MYEHRA"
            }
        }
        return jsonify(user_info), 200  # HTTP 200 OK

    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({
            "status": "error",
            "message": "Profile does not exist or is private.",
            "developer": {
                "name": "Mehraj [Ehra]",
                "github": "https://github.com/MJEHRA",
                "telegram": "@MYEHRA"
            }
        }), 404  # HTTP 404 Not Found

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
