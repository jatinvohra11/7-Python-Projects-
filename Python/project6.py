import requests
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        print("Joke Time! ")
        print(joke['setup'])
        print(joke['punchline'])

    else:
        print("Oops! couldn't fetch a joke at the moment....")
get_joke()

