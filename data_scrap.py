import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from urllib.parse import urljoin

webpage = [
    "https://www.daiict.ac.in/faculty",
    "https://www.daiict.ac.in/adjunct-faculty",
    "https://www.daiict.ac.in/adjunct-faculty-international",
    "https://www.daiict.ac.in/distinguished-professor",
    "https://www.daiict.ac.in/professor-practice"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

faculty_data = []   # ✅ Move this OUTSIDE the loop

for url in webpage:

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    faculty_cards = soup.select("div.facultyInformation ul li")

    for card in faculty_cards:
        # Name + Profile URL
        name_tag = card.select_one("h3 a")
        name = name_tag.get_text(strip=True) if name_tag else ""
        profile_url = urljoin(url, name_tag["href"]) if name_tag else ""

        # Education
        edu_tag = card.select_one("div.facultyEducation")
        education = edu_tag.get_text(strip=True) if edu_tag else ""

        # Research Area / Bio
        bio_tag = card.select_one("div.areaSpecialization p")
        bio_text = bio_tag.get_text(strip=True) if bio_tag else ""

        # Email
        try:
            e = card.find("div", class_="contactDetails") \
                    .find("span", class_="facultyemail") \
                    .get_text(strip=True)
            e = e.replace("[at]", "@").replace("[dot]", ".")
        except:
            e = np.nan

        # Contact Number
        try:
            contact_number = card.find("span", class_="facultyNumber").get_text(strip=True)
        except:
            contact_number = np.nan

        try:
            photo_url = urljoin(url, card.find("div", class_="facultyPhoto").find("img")["src"])
        except:
            photo_url = np.nan

        faculty_data.append({
            "Name": name,
            "Education": education,
            "Research_area": bio_text,
            "Profile_URL": profile_url,
            "Email": e,
            "Contact_Number": contact_number,
            "Photo": photo_url
        })

df = pd.DataFrame(faculty_data)
df.to_csv("daiictfaculty.csv", index=False)

print(df.info())
