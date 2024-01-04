import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up!")
        else:
            print(f"{url} is down (Status Code: {response.status_code})")
    except requests.ConnectionError:
        print(f"{url} is down!")

if __name__ == "__main__":
    website_urls = [
        "https://discord.jerrywalter802.repl.co/",
        "https://25303a28-3201-42a3-9157-52249a68a919-00-37s5ctn51v55t.spock.replit.dev/"
    ]
    interval = 60  # Check every 1 minute
    run_time = 1500  # 25 minutes in seconds

    total_time = 0
    while total_time < run_time:
        for url in website_urls:
            check_website(url)
        time.sleep(interval)
        total_time += interval
