import urllib.request
import json
import matplotlib.pyplot as plt

def printresults(data):
    theJSON = json.loads(data)
    data_dict = {}
    for i in theJSON["features"]:
      feltreport = i["properties"]["felt"]
      magnitude = i["properties"]["mag"]
      place = i["properties"]["place"]
      if feltreport is not None and feltreport > 0:
            if place in data_dict:
                data_dict[place]["felt_reports"] += feltreport
                data_dict[place]["magnitudes"].append(magnitude)
            else:
                data_dict[place] = {"felt_reports": feltreport,"magnitudes": [magnitude],}
      for place, data in data_dict.items():
        print(place,", Total Magnitude=",sum(data["magnitudes"]),", Total Felt Reports:",data["felt_reports"])
  # Create a bar chart to show the total felt reports for each earthquake location
    places = data_dict.keys()
    felt_reports = [data["felt_reports"] for data in data_dict.values()]
    plt.figure(figsize=(12, 6))
    plt.bar(places, felt_reports)
    plt.xlabel('Earthquake Location')
    plt.ylabel('Total Number of Felt Reports')
    plt.title('Total Felt Reports for Earthquake Locations')
    plt.xticks(rotation=90) # Rotate x-axis labels for better readability
    plt.show()

def main():
    urlData="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl=urllib.request.urlopen(urlData)
    print("Result code: " + str(weburl.getcode()))
    if (weburl.getcode()==200):
        data=weburl.read()
        printresults(data)
    else:
        print("Received an error from server, can't print results ",weburl.getcode())
if __name__=="__main__":
    main()