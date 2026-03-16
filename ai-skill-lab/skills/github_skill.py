import requests

def get_repo_info(repo_url:str):
    '''Skill:get info from Github'''
    parts = repo_url.strip('/').split('/')
    owner = parts[-2]
    repo_name = parts[-1]

    api = f"https://api.github.com/repos/{owner}/{repo_name}"

    r = requests.get(api)
    
    data = r.json()

    result = {
        "name":data["name"],
        "description":data["description"],
        "stars":data["stargazers_count"],
        "language":data["language"],
        "url":data["html_url"]

    }

    return result