import requests

def acortar_enllaç(api_key, long_url):
    url_acortada = ""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "long_url": long_url,
        "domain": "bit.ly"
    }

    response = requests.post(url_acortada, headers=headers, json=data)

    if response.status_code == 200:
        enllaç_curt = response.json()["id"]
        return enllaç_curt
    else:
        print(f"Error al acortar l'enllaç {response.text}")
        return None


# Utilització.
api_key_bitly = "your_api_key"
enllaç_llarg = "https://educaciodigital.cat/iescastellet/moodle/course/view.php?id=7155"

enllaç_curt = acortar_enllaç(api_key_bitly, enllaç_llarg)

if enllaç_llarg:
    print(f"enllaç_llarg: {enllaç_llarg}")
    print(f"enllaç_curt: {enllaç_curt}")