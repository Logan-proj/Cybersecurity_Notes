# Open-source intelligence (OSINT)

## About OSINT
Open-source intelligence (OSINT) gathers research from publicly available information to identify attack vectors. OSINT research can include information collected from the open/indexed internet, deep web, and dark web. Publicly available information can include:
- Internet; Websites, search engines, about pages
- Media: Social media, news articles, photos, and videos
- Journals; Research journals/articles, library records
- Geospatial information: Online maps, satellite images

## Techniques
### Google Dorks
Google Dorks is utilizing Google's advanced query terms to narrow search results. For example, researchers can use Google Dorks to search for specified file types, specific words or phrases, misconfigurations, etc.
- inurl: will search for specified words within a URL
- filetype: searches for specified file type
- site: searches for the specified domain
- cache: gets the latest cached website version

### WHOIS Lookup
Websites such as [WHOIS lookup](https://who.is/) makes public domain information easily accessible and searchable. These websites can be used to gather Personal Identifiable Information (PII) for phishing attacks.

### Robots.txt
A document that tells search engines what pages to hide from public search results or prevent search engines from crawling a specific website. This document is publicly accessible and can be used to find other addresses that the website owners don't want to be accessible through search engines.
- Find a website's robot.txt file by appending it to the end of the website URL.

### Breached Database Search
Websites like [haveibeenpwned](https://haveibeenpwned.com/) serve as a database of significant company data breaches and are used to check if your email or password has been compromised in a data breach. These data breaches can include valuable information to attackers, such as:
- Usernames
- Email addresses
- Phone numbers
- Passwords
Attackers can use these data breaches to try and access users' accounts who reuse their passwords and emails.

### GitHub Repos
GitHub is a hosting website where developers can upload, develop, and manage their code. However, misconfigurations within repository settings can make it publically accessible and can cause leakage of critical information such as passwords and access tokens.
