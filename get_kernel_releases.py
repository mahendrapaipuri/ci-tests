import sys
import json
import urllib.request

try:
    # Fetch the JSON data
    with urllib.request.urlopen('https://www.kernel.org/releases.json') as response:
        data = json.loads(response.read())
    
    # Extract and print all source URLs
    urls = []
    for release in data['releases']:
        for source in release.get('source', []):
            urls.append(source)
    
    # Output all URLs
    print(json.dump(urls))
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
