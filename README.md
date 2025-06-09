# Phishing-site
# Phishing Page Simulation

A small local web app that serves a fake login page and captures submitted credentials for educational/demo purposes in a sandboxed environment.

> ⚠️ **Ethics & Safety**  
> - **Do NOT** deploy this publicly or send the link to anyone.  
> - **Do NOT** use real credentials.  
> - This is strictly for a controlled, local lab environment.

---

## Project Structure

```
phish-sim/
├── backend/
│   ├── app.py                # Flask server code
│   └── creds.txt             # Auto-created on first login submission
│
├── frontend/
│   ├── fake_login.html       # Fake login form HTML
│   └── static/
│       └── style.css         # Styles for the login page
│
└── README.md                 # This file
```

---

## Quick Start

### 1. Backend (PyCharm)

1. **Open** `phish-sim/backend` in PyCharm.
2. **Create or select** a Python 3 virtual environment:
   - Settings → Project Interpreter → Add Interpreter → Virtualenv
   - Point Base Interpreter to your Python 3.12 install.
   - Uncheck “Inherit global site-packages.”
3. **Install Flask** in the venv:
   ```bash
   pip install Flask
   ```
4. **Create a Run Configuration**:
   - Run → Edit Configurations → + → Python
   - Script: `app.py`
   - Working directory: `<project-root>/backend`
   - Interpreter: your new venv
5. **Run** the “Flask Server” config. You should see:
   ```
   * Serving Flask app "app.py"
   * Debug mode: on
   * Running on http://127.0.0.1:5000/
   ```

---

### 2. Frontend (Browser or IntelliJ IDEA)

1. **Open** `phish-sim/frontend/fake_login.html` in your browser (or IntelliJ → Open in Browser).
2. You’ll see the styled login form.
3. When you click **Login**, the form posts to `http://127.0.0.1:5000/login`.

---

### 3. Verify Captured Credentials

- After submitting, a file `creds.txt` appears in `backend/`.
- Open it to see entries like:
  ```
  alice@example.com : password123
  bob@domain.com   : hunter2
  ```

---

## File Details

### `backend/app.py`

- Serves `fake_login.html` at `/`
- Logs `username` & `password` into `creds.txt` on POST to `/login`
- Returns a “Login Failed” page

### `frontend/fake_login.html`

- Simple HTML form (`action="http://127.0.0.1:5000/login"`, method POST)
- Links to `static/style.css` for styling

### `frontend/static/style.css`

- Card-style centered login form
- Responsive and clean design

---

## Tips & Customization

- **Form Target:** Change the `action` URL if your Flask server runs elsewhere.
- **CSS Tweaks:** Modify colors, fonts, or add a logo in `style.css`.
- **Template Engine:** Swap `render_template_string` for `render_template` if you add more HTML files.
- **Credential Storage:** Replace `creds.txt` with a database (SQLite) or CSV as an exercise.

---

## Cleanup

1. Stop the Flask server in PyCharm.
2. Delete `creds.txt` if it contains dummy data.
3. (Optional) Remove the `venv/` folder to reclaim disk space.

---

**Use responsibly, and only in safe, isolated test environments for learning and demonstration purposes.**
