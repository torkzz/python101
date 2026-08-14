"""
Web Scraping with BeautifulSoup4 (bs4)

Concepts:
- Parsing HTML text or local files (`BeautifulSoup(data, "html.parser")`).
- Finding single elements (`soup.find(tag, attrs={...})`).
- Finding collection of elements (`soup.find_all(tag, attrs={...})`).
- Extracting and cleaning text (`element.get_text().strip()`).
"""

from bs4 import BeautifulSoup

# Sample HTML document simulating scraped data
SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<head><title>NHL Teams</title></head>
<body>
    <h1>NHL Hockey Teams since 1990</h1>
    <table class="table">
        <tr class="team">
            <td class="name">Boston Bruins</td>
            <td class="year">1990</td>
            <td class="wins">44</td>
            <td class="losses">24</td>
        </tr>
        <tr class="team">
            <td class="name">Buffalo Sabres</td>
            <td class="year">1990</td>
            <td class="wins">31</td>
            <td class="losses">30</td>
        </tr>
        <tr class="team">
            <td class="name">Calgary Flames</td>
            <td class="year">1990</td>
            <td class="wins">46</td>
            <td class="losses">26</td>
        </tr>
    </table>
</body>
</html>
"""


def parse_nhl_teams(html_content: str) -> None:
    soup = BeautifulSoup(html_content, "html.parser")

    # Find main table element
    table_data = soup.find("table", attrs={"class": "table"})
    if not table_data:
        print("Table not found!")
        return

    print("NHL Hockey Teams since 1990:")

    # Find all table rows matching class 'team'
    teams = table_data.find_all("tr", attrs={"class": "team"})
    for tr in teams:
        hockey_team = tr.find("td", attrs={"class": "name"}).get_text().strip()
        year = tr.find("td", attrs={"class": "year"}).get_text().strip()
        wins = tr.find("td", attrs={"class": "wins"}).get_text().strip()
        losses = tr.find("td", attrs={"class": "losses"}).get_text().strip()

        print(f"  - {year} {hockey_team}: {wins}W / {losses}L")


if __name__ == "__main__":
    parse_nhl_teams(SAMPLE_HTML)
