
## 📘 Instagram Followers Tracker

### 📜 Project Description
This project helps you track your Instagram followers over time. It compares the current list of followers with a previous list to identify users who have unfollowed you.

### 🔧 Prerequisites
- Python 3.x
- Instaloader library

### 📦 Installation
1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2. **Install Instaloader**: Open your terminal or command prompt and run:
   ```bash
   pip install instaloader
   ```

### 📂 Files
1. **`instagram_followers.py`**: Logs into Instagram, retrieves the current list of followers, and saves it to `followers_current.txt`.
2. **`check_unfollowers.py`**: Compares the current list of followers with the previous list and identifies users who have unfollowed you.

### 🚀 Usage

#### Step 1: Download Current Followers
1. Open `instagram_followers.py`.
2. Enter your Instagram username and password:
   ```python
   username = 'your_username'
   password = 'your_password'
   ```
3. Run the script:
   ```bash
   python instagram_followers.py
   ```
4. Follow the prompts if two-factor authentication is required.
5. The current list of followers will be saved to `followers_current.txt`.

#### Step 2: Check Unfollowers
1. Ensure `followers_previous.txt` contains the previous list of followers. If this is your first time running the scripts, manually copy `followers_current.txt` to `followers_previous.txt`.
2. Run `check_unfollowers.py`:
   ```bash
   python check_unfollowers.py
   ```
3. The script will output the list of unfollowers and update `followers_previous.txt` with the current followers list for future comparisons.

### 📋 Example

**Running `instagram_followers.py`:**
```bash
python instagram_followers.py
```
Output:
```
Login successful!
Followers downloaded and saved to followers_current.txt
```

**Running `check_unfollowers.py`:**
```bash
python check_unfollowers.py
```
Output:
```
Unfollowers: {'unfollower1', 'unfollower2'}
```

### 📝 Notes
- Keep your Instagram credentials secure and do not share them.
- If you encounter a `TwoFactorAuthRequiredException`, enter the 2FA code when prompted.



### 🎉 Happy Tracking!
