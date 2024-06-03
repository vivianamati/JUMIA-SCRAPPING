import requests
from bs4 import BeautifulSoup
nws_page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
# print(nws_page.content)

nws_soup = BeautifulSoup(nws_page.content,"html.parser")
# print(nws_soup.prettify)

seven_days = nws_soup.find(id="seven-day-forecast-body")
print(seven_days)

forecast_day = seven_days.find_all(class_="tombstone-container")
print(forecast_day)

# overnight = forecast_day[0]
# print(overnight.prettify)

# period = overnight.find(class_="period name").get_text()
# temp = overnight.find(class_="temp").get_text()
# desc = overnight.find(class_="short-desc").get_text()
# print(period)
# print(temp)
# print(desc)

# friday = forecast_day[1]
# print(friday.prettify)
# period1 = friday.find(class_="period-name").get_text()
# temp1 = friday.find(class_ = "temp").get_text()
# desc1 = friday.find(class_ = "short-desc").get_text()
# print(period1)
# print(temp1)
# print(desc1)

# fridaynight = forecast_day[2]
# print(fridaynight.prettify)
# period2 = fridaynight.find(class_="period-name").get_text()
# temp2 = fridaynight.find(class_ = "temp").get_text()
# desc2= fridaynight.find(class_ = "short-desc").get_text()
# print(period2)
# print(temp2)
# print(desc2)

# saturday = forecast_day[3]
# print(saturday.prettify)
# period3 = saturday.find(class_="period-name").get_text()
# temp3 = saturday.find(class_ = "temp").get_text()
# desc3= saturday.find(class_ = "short-desc").get_text()
# print(period3)
# print(temp3)
# print(desc3)

# saturdaynight = forecast_day[4]
# print(saturdaynight.prettify)
# period4 = saturdaynight.find(class_="period-name").get_text()
# temp4 = saturdaynight.find(class_ = "temp").get_text()
# desc4= saturdaynight.find(class_ = "short-desc").get_text()
# print(period4)
# print(temp4)
# print(desc4)

# sunday = forecast_day[5]
# print(sunday.prettify)
# period5 = sunday.find(class_="period-name").get_text()
# temp5 = sunday.find(class_ = "temp").get_text()
# desc5= sunday.find(class_ = "short-desc").get_text()
# print(period5)
# print(temp5)
# print(desc5)

# sundaynight = forecast_day[6]
# print(sundaynight.prettify)
# period6 = sundaynight.find(class_="period-name").get_text()
# temp6 = sundaynight.find(class_ = "temp").get_text()
# desc6= sundaynight.find(class_ = "short-desc").get_text()
# print(period6)
# print(temp6)
# print(desc6)



