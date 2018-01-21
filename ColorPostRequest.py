import requests
import json

def getColor(url):
    APIKey = "AIzaSyCRk3JpIHYG1iRGnukBEjLtqGpeG1Js59o"

    data = {
      "requests":[
        {
          "image":{
            "source":{
              "imageUri":url
            }
          },
          "features":[
            {
              "type":"IMAGE_PROPERTIES",
              "maxResults":1
            }
          ]
        }
      ]
    }

    r = requests.post('https://vision.googleapis.com/v1/images:annotate?key='+APIKey, json=data)
    data = json.loads(r.text)
    colordata = data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][0]["color"]
    return [colordata['red'], colordata['green'], colordata['blue']]
