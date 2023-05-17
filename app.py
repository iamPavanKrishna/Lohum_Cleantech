from flask import Flask, request, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# API call to get the latest price
@app.route('/price', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def get_price():
    """
    This method web scrapes the data from the url and returns the latest price
    """

    # Checking if the request method is valid or not
    if request.method in ['POST', 'HEAD', 'PUT', 'DELETE']:
        return "INVALID REQUEST!"
    else:
        # Getting the url
        r = requests.get("https://www.metal.com/Lithium-ion-Battery/202303240001")
        soup = BeautifulSoup(r.text, "html.parser")  # Web sraping the url using BeautifulSoup from bs4 library

        # Finding the span tag which contains the latest price information
        price = soup.find("span", {"class": "strong___1JlBD priceDown___2TbRQ"})

        return "Latest price: "+ price.text  # Returning the price back to the client(User)



if __name__ == '__main__':
    app.run()
