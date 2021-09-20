from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)

@app.route("/")
def home_page():
     # Find one record of data from the mongo database
    online_users = mongo.db.users.find({"online": True})
     # Return template and data
    return render_template("index.html",
        online_users=online_users)

@app.route("/scrape")
def scrape():
    # Running the Scrape Function
    mars_data = scrape_mars.scrape_info()

    # Updating the Mongo Database
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Going Back to Homepage
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
