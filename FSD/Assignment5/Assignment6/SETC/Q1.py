from flask import Flask

app = Flask(__name__)

@app.route('/')
def employee_list():

    employees = [
        ("Ajinkya Shinde", "IT", 45000),
        ("Karan Sharma", "HR", 40000),
        ("Amit Shrivastav", "Finance", 50000),
        ("Aditya Singh", "Marketing", 42000),
        ("Vedant Singh", "IT", 55000)
    ]

    result = "<h2>Employee Details</h2>"

    for name, department, salary in employees:
        result += f"""
            Name  : {name}<br>
            Department : {department}<br>
            Salary : ₹{salary}<br><br>
        """
    return result

if __name__ == "__main__":
    app.run(debug=True)



    