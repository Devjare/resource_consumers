import requests


url = "https://zenodo.org/record/3227177/files/Android.tar.gz?download=1"
data = requests.get(url)

print("Data obtained: ", data)
