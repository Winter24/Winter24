import requests
import re

# Define the target URL and desired theme
url = "https://github-profile-summary-cards.vercel.app/demo.html"
theme = {
    "bg_color": "2b213a",
    "title_color": "FF66C4",
    "text_color": "C9D1D9",
    "icon_color": "F8D866",
    "border_color": "30363D"
}
username = "winter24"

# Fetch the HTML content of the demo page
response = requests.get(url)
if response.status_code != 200:
    print("Failed to fetch the page")
    exit()

html_content = response.text

# Extract the SVG content from the HTML
svg_match = re.search(r'(<svg[^>]*>.*?</svg>)', html_content, re.DOTALL)
if not svg_match:
    print("Failed to find SVG content")
    exit()

svg_content = svg_match.group(1)

# Update the SVG with the username and theme colors
svg_content = svg_content.replace("Demo User", username)
svg_content = svg_content.replace("bg_color='FFFFFF'", f"bg_color='{theme['bg_color']}'")
svg_content = svg_content.replace("title_color='0969DA'", f"title_color='{theme['title_color']}'")
svg_content = svg_content.replace("text_color='333'", f"text_color='{theme['text_color']}'")
svg_content = svg_content.replace("icon_color='586069'", f"icon_color='{theme['icon_color']}'")
svg_content = svg_content.replace("border_color='D0D7DE'", f"border_color='{theme['border_color']}'")

# Write the updated SVG content into a file
output_file = "./cards/stats.svg"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(svg_content)

print(f"SVG file created: {output_file}")
