import random


data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States',
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal',
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and Actress',
        'country': 'United States',
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and Former Professional Wrestler',
        'country': 'United States',
    },
]
points = 0
account_b = random.choice(data)
playing = True

while playing:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    def account_data(account):
        name = account['name']
        follower_count = account['follower_count']
        description = account['description']
        country = account['country']
        return f"{name}, a {description}, from {country}"

    def compare_answers(follower_a, follower_b):
        if guess == "a" and follower_a > follower_b:
            return "You win"
        elif guess == "b" and follower_b > follower_a:
            return "You win"
        else:
            return "You lose"

    print(f"Compare A: {account_data(account_a)}")
    print(f"Compare B: {account_data(account_b)}")

    guess = input("Who has more followers 'A' or 'B':\n").lower()

    f_c_b = account_b['follower_count']
    f_c_a = account_a['follower_count']

    
    results = compare_answers(follower_a=f_c_a, follower_b=f_c_b)
    print(results)


    if results == "You win":
        points += 1
        print(f"Score is currently {points}")
    else:
        print(f"Your final score is {points}")
        playing = False
        
# still_playing = input("Do you want to play again Y/N")
