# Calorie Tracker

A simple web-based calorie tracking application built with Django. The application allows users to add food items with their calorie values, view their daily food intake, calculate total calories, remove individual food items, and reset the daily calorie record.

## Features

* Add food items with their calorie count.
* Store food records in a database.
* Display all food items added for the day.
* Automatically calculate total daily calories.
* Remove individual food items.
* Reset the entire daily calorie record.
* 
## Technologies Used

* Python 
* Django
* SQLite

## Project Structure

```text
calorie tracker/
│
├── calorie_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── calorie/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── db.sqlite3
├── manage.py
└── README.md
```


## How It Works

### Adding Food

The user enters:

* Food name
* Number of calories

When the form is submitted, Django receives the data through a `POST` request and creates a new `Food` record in the database.

### Viewing Food

The application retrieves all stored food records using Django's ORM and displays them dynamically on the home page.

### Calculating Calories

The application adds the calorie values of all stored food items to calculate the total daily calorie intake.

### Removing Food

Each food item has a **Remove** option. When selected, Django identifies the food using its database ID and deletes that individual record.

### Resetting the Day

The **Reset Day** option removes all food records from the database. A confirmation message is displayed before the reset is performed to help prevent accidental deletion.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

### 2. Create a Virtual Environment

python -m venv venv


Activate it:

venv\Scripts\activate

### 3. Install Django

pip install django

### 4. Apply Database Migrations

python manage.py makemigrations

Then:
python manage.py migrate


### 5. Start the Development Server

python manage.py runserver

Open the development server in your browser:

## Using the Application

1. Open the application in your browser.
2. Enter the name of a food item.
3. Enter its calorie count.
4. Click **Add Food**.
5. The food item will appear in the daily food list.
6. The total calorie count will update automatically.
7. Use **Remove** to delete an individual food item.
8. Use **Reset Day** to clear all food records after confirming the action.

## Future Improvements

Possible future improvements include:

* Adding food categories.
* Adding dates to food records.
* Tracking calories across multiple days.
* Adding daily calorie goals.
* Adding user accounts and authentication.
* Improving form validation and error messages.

## Author

**Rowan Hadegu**


