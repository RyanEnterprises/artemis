import requests
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': input("Text: "),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json()['output'])