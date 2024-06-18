import instaloader

L = instaloader.Instaloader()

username = ''
password = ''

try:
    L.login(username, password)
except instaloader.exceptions.TwoFactorAuthRequiredException:
    print("Two-factor authentication is required.")
    two_factor_code = input("Enter the 2FA code: ")
    L.two_factor_login(two_factor_code)

print("Login successful!")

profile = instaloader.Profile.from_username(L.context, username)
followers = set([follower.username for follower in profile.get_followers()])

with open('followers_current.txt', 'w') as f:
    for follower in followers:
        f.write(follower + '\n')

print("Followers downloaded and saved to followers_current.txt")
