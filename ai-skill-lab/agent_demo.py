from skills.github_skill import get_repo_info
from rich import print
from skills.webpage_skill import summarize_webpage

import sys
sys.stdout.reconfigure(encoding = 'utf-8')
def run_agent():
    url = input("input github repo url:")

    # info = get_repo_info(url)

    # print("\n[bold green]repo info[/bold green]")

    # for k, v in info.items():
    #     print(f"{k}:{v}")

    summary = summarize_webpage(url)
    print(summary)
    
if __name__ == "__main__":
    run_agent() 