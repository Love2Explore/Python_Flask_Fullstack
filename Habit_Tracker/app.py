from flask import Flask , render_template , request
import datetime

app = Flask(__name__)
habits = ["Test Habit","OPPP"]

# @app.context_processor
# def add_calc_date_range():
def date_range(start:datetime.date):
        dates = [ start + datetime.timedelta(days=diff) for diff in range(-3,4)]
        return dates
    # return {"date_range":date_range}

@app.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    return render_template("index.html",
                        habits=habits , 
                        tittle="Habit Tracker - Home",
                        date_range=date_range,
                        selected_date=selected_date)

@app.route("/add", methods=["GET","POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template("add_habit.html",
            tittle="Habit Tracker - Add Habit",
            selected_date=datetime.date.today())

