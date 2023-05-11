import requests
from tqdm import tqdm

def download_file_from_google_drive(url, output_file):
    session = requests.Session()

    response = session.get(url, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    save_response_content(response, output_file)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, output_file):
    CHUNK_SIZE = 1024 * 1024 * 16  # 16 MB chunk size
    total_size = int(response.headers.get('content-length', 0))

    with open(output_file, "wb") as f, tqdm(total=total_size, unit='B', unit_scale=True) as progress_bar:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                progress_bar.update(len(chunk))

gdrive_link = "https://drive.google.com/file/d/1-brdf55nN46BGmrDkH5bjPLwiuFaaRO5/view"

try:
    file_id = gdrive_link.split('/')[-2]
    download_url = "https://drive.google.com/uc?id=" + file_id + "&export=download"
    download_file_from_google_drive(download_url, "video.mp4")
    print('Downloaded video.mp4')
except Exception as e:
    print('Error:', e)
https://jiji.co.ke/nairobi-central/tools-accessories/geemy-professional-shaving-machine-BFqIBHIBmdK1SmHvsUv7kPjh.html?page=1&pos=6&cur_pos=6&ads_per_page=23&ads_count=1505&lid=wLs_eG1sDn-zK1l3&indexPosition=5