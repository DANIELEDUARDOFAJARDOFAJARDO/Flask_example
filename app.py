from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for the table
data = [
    {'name': 'John', 'age': 25, 'gender': 'Male'},
    {'name': 'Alice', 'age': 30, 'gender': 'Female'},
    {'name': 'Bob', 'age': 35, 'gender': 'Male'},
    {'name': 'Eve', 'age': 28, 'gender': 'Female'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user input from the form
        name_filter = request.form.get('name')
        age_filter = request.form.get('age')
        gender_filter = request.form.get('gender')

        # Filter the data based on user input
        filtered_data = filter_data(name_filter, age_filter, gender_filter)
    else:
        # Display the unfiltered data
        filtered_data = data

    return render_template('index.html', data=filtered_data)

def filter_data(name_filter, age_filter, gender_filter):
    # Apply the filters to the data
    filtered_data = data

    if name_filter:
        filtered_data = [item for item in filtered_data if item['name'] == name_filter]

    if age_filter:
        filtered_data = [item for item in filtered_data if item['age'] == int(age_filter)]

    if gender_filter:
        filtered_data = [item for item in filtered_data if item['gender'] == gender_filter]

    return filtered_data

if __name__ == '__main__':
    app.run(debug=True)
