from selenium import webdriver


def setup():
    # These parts might need to be updated
    wis_url = "https://wis.fit.vutbr.cz/FIT/st/"
    thesis_base_url = "https://wis.fit.vutbr.cz/FIT/st/bci-prj-z.php.en?typ="


    thesis_type = {
        "BIT": "BP1",
        "MBI": "DP18",
        "MBS": "DP21",
        "MGM": "DP25",
        "MIN": "DP24",
        "MIS": "DP23",
        "MMI": "DP17",
        "MMM": "DP20",
        "MPS": "DP5",
        "MPV": "DP22",
        "MSK": "DP19",

    }

    chrome_driver = webdriver.Chrome("C:\\chromedriver.exe")
    chrome_driver.get(wis_url)

    user_input = raw_input("Three character, course ID ( for example 'BIT','MBI')\n")

    chrome_driver.get(thesis_base_url + thesis_type[user_input])



    return chrome_driver
