import requests
import datetime
import os

# Fetch Cybersecurity News from News API
def fetch_cyber_news_news_api():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "cybersecurity",
        "apiKey": "f7158671106546ca93b28ee03443b5b1",
        "pageSize": 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        return []

# Fetch Cybersecurity Posts from Social Searcher
def fetch_cyber_posts_social_searcher():
    url = "https://api.social-searcher.com/v2/search"
    params = {
        "query": "cybersecurity",
        "key": "9926920fe0c4f870504844f448ee62d6",
        "page": 1,
        "size": 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        posts = response.json().get("posts", [])
        return posts
    else:
        return []

# Save news articles to a markdown file
def save_news(articles, platform):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"cyber_news_{platform}_{date}.md"
    with open(filename, "w") as f:
        f.write(f"# Cybersecurity News from {platform} for {date}\n\n")
        for article in articles:
            title = article.get("title", "No Title")
            link = article.get("url", "No URL")
            f.write(f"- [{title}]({link})\n")
    return filename

# Function to commit changes to the repo
def make_commit(filename):
    os.system(f"git add {filename}")
    os.system(f'git commit -m "Add cybersecurity news from {filename}"')

if __name__ == "__main__":
    # Fetch news from News API and Social Searcher
    news_articles = fetch_cyber_news_news_api()
    social_posts = fetch_cyber_posts_social_searcher()

    if news_articles:
        news_filename = save_news(news_articles, "News API")
        make_commit(news_filename)
    else:
        print("No news fetched from News API. Skipping commit.")

    if social_posts:
        social_filename = save_news(social_posts, "Social Searcher")
        make_commit(social_filename)
    else:
        print("No posts fetched from Social Searcher. Skipping commit.")
