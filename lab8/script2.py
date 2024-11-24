import json

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as file:
    for i, repo in enumerate(data):
        if i >= 5:
            break
        
        name = repo.get("name", "")
        html_url = repo.get("html_url", "")
        updated_at = repo.get("updated_at", "")
        visibility = repo.get("visibility", "")
        
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        
        file.write(line)
