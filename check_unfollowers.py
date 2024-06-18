def load_followers(filename):
    with open(filename, 'r') as f:
        return set(f.read().splitlines())

current_followers = load_followers('followers_current.txt')
previous_followers = load_followers('followers_previous.txt')

unfollowers = previous_followers - current_followers

print("Unfollowers:", unfollowers)

with open('followers_previous.txt', 'w') as f:
    for follower in current_followers:
        f.write(follower + '\n')