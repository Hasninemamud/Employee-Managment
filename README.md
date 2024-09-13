# Employee Management System

This is a Django-based **Employee Management System** that allows users to manage employee data efficiently. The system provides the ability to view a list of employees, add new employees, edit existing employees, and delete employees from the system. The project uses **Tailwind CSS** for modern styling, ensuring a responsive and interactive user interface. Additionally, it features a left-side navigation bar for easy access to different pages within the system.

## Features

- **Employee List**: View a list of all employees with options to edit or delete them.
- **Add Employee**: A form to add new employees to the system, including their profile picture.
- **Edit Employee**: Modify existing employee details through the form.
- **Delete Employee**: Remove employees from the system after confirming the action.
- **Live Photo Preview**: Upload a profile picture and see a live preview before submitting.
- **Search & Pagination**: Search employees by name or email, with pagination to display a limited number of employees per page.
- **Responsive Layout**: Works across all screen sizes with a mobile-friendly design.

## Technologies Used

- **Django**: Backend framework used for server-side logic and database management.
- **Tailwind CSS**: Utility-first CSS framework for clean and responsive design.
- **SQLite**: Default lightweight database used for storing employee data.
- **JavaScript**: Used for live photo preview functionality.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/employee-management-system.git
    cd employee-management-system
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    Visit `http://127.0.0.1:8000/` in your browser.



