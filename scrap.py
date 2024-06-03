import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.kdnuggets.com/")



soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# h2 = soup.find("h2").text
# print(h2)

# b = soup.find("b").text
# print(b)

# p = soup.find("p").text
# print(p)

# h2_tags = soup.find_all("h2")
# for h2 in h2_tags:
#     print(h2.text)
# b_tags = soup.find_all("b")
# for b in b_tags:
#     print(b.text)
# p_tags = soup.find_all("p")
# for p in p_tags:
#     print(p.text)

# a_tag  = soup.find("a")
# for a in a_tag:
#   print(a_tag["href"])

a_tags = soup.find_all("a")
for a in a_tags:
    print(a["href"])

# list = soup.find_all("li",attrs={"class": "li-has-thumb"})
# for li in list:
#     print(list)    

# a_specific = soup.find("a")
# print(a_specific)

a_has_attrs = soup.find("a")
print(a_has_attrs.has_attr("class"))