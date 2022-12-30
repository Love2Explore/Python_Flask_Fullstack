from flask import Flask , render_template, request
import datetime
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient("mongodb+srv://rewati123:Vw06crJfnetNdBf7@cluster0.x2sw8.mongodb.net/?retryWrites=true&w=majority") #(os.environ.get("MONGODB_URL"))
app.db = client.myFirstDatabase

total_entries = []

@app.route("/" , methods=["GET","POST"])
def home(): 
    if request.method == "POST":
        entry_content = request.form.get("content")
        date_format = datetime.datetime.today().strftime("%Y-%m-%d")
        total_entries.append((entry_content,date_format))
        #insert in DB
        app.db.macroblog.insert({"content":entry_content,"dateTime":date_format})
            ###
    entry_with_date = [ ( 
            entry["content"],
            entry["dateTime"],
            datetime.datetime.strptime(entry["dateTime"],"%Y-%m-%d").strftime("%b %d")
            )  for entry in app.db.macroblog.find({}) ]
            # for entry in total_entries:
            #     entry_with_date.append((entry[0],entry[1],datetime.datetime.strptime(entry[1],"%Y-%m-%d").strftime("%b %d")))
    return render_template("home.html",entries = entry_with_date)

