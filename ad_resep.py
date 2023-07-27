import requests

url = "http://localhost:5000/add_resep"

data = {
    "bahan": [
        {
            "bahan": "sbssnjs",
            "jumlah": "",
            "satuan": ""
        }
    ],
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/kulinerfit-31796.appspot.com/o/imgResep%2F1689899418537.jpg?alt=media&token=092eac5e-34ee-4c51-9d50-04254b0a06ef",
    "langkah": ["sbbs"],
    "nama": "yessnsz",
    "timestamp": "Fri, 21 Jul 2023 00:30:18 GMT",
    "userID": "9YWd0lDCg1S230y609GjzdY9gkC3"
}

response = requests.post(url, json=data)
print(response.json())
