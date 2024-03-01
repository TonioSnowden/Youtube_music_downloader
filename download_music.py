import pandas as pd
import re
import requests
import time
import webbrowser

def extract_video_id(url):
    match = re.search(r'v=([^\&]*)', url)
    return match.group(1) if match else None

def download_from_link(video_id):
    BASE = "https://360ytmp3.com/fr/youtube/"
    link_360 = BASE + video_id
    
    webbrowser.open(link_360)

    time.sleep(5)

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0...'
    }

    # CONVERT
    url = "https://360ytmp3.com/api/convert"
    payload = {
        "cdn": "https://v1.yt-cdn.xyz/sv2",
        "id": video_id,
        "t": "320kbps"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to convert {video_id}")
        return

    # CHECKFILE (Assuming immediate response is possible, otherwise consider retries with delays)
    id = response.json()["id"]
    if not id:
        print(f"Failed to get ID for {video_id}")
        return
    time.sleep(5)
    checkfile_url = "https://360ytmp3.com/api/checkfile"
    payload = {"id": id, "t": "320kbps", "cdn": "https://v1.yt-cdn.xyz/sv2"}
    response = requests.post(checkfile_url, json=payload, headers=headers)
    if response.status_code != 200:
        print(f"Failed to check file for {video_id}")
        return

    # DOWNLOAD
    response_data = response.json()
    download_url = response_data['cdnConvert']
    local_filename = response_data['fileName']

    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"File downloaded successfully: {local_filename}")

# Load Excel file
excel_path = 'links.xlsx'  # Update this path
df = pd.read_excel(excel_path)

# Assuming the links are in the first column
for link in df.iloc[:, 0]:  # Adjust the column index as necessary
    video_id = extract_video_id(link)
    if video_id:
        download_from_link(video_id)
    else:
        print(f"Failed to extract video ID from {link}")