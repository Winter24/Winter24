import requests

response = requests.get("https://api.github.com/users/winter24")
data = response.json()

svg_template = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="200" viewBox="0 0 700 200">
  <rect x="1" y="1" width="698" height="198" fill="#2b213a" stroke="#30363D" />
  <text x="30" y="40" font-size="22" fill="#FF66C4">GitHub User: {data['login']}</text>
  <text x="30" y="70" font-size="16" fill="#C9D1D9">Repositories: {data['public_repos']}</text>
</svg>
"""

with open("/home/winter24/Winter24/cards/stats.svg", "w") as file:
    file.write(svg_template)
