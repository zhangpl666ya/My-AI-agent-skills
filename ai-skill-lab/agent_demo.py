from skills.github_skill import get_repo_info
from rich import print

def run_agent():
    repo = input("input github repo url:")

    info = get_repo_info(repo)

    print("\n[bold green]repo info[/bold green]")

    for k, v in info.items():
        print(f"{k}:{v}")
    
if __name__ == "__main__":
    run_agent() 