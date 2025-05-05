# Django Learning Project

## 🧠 Overview

This repository showcases a Django project I built while learning web development using Django's **Model-View-Template (MVT)** architecture. I followed the [CodeWithHarry Django series](https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME), which provided an excellent foundation for understanding Django's core concepts.

> 🚀 This project documents my journey to understand how Django works under the hood — from models and routing to templates and the admin panel.

## 📚 What I Learned

- **Project Structure**: Setting up and configuring a Django project
- **MVT Architecture**: Understanding Django's Model-View-Template pattern
- **App Development**: Creating and linking Django apps
- **URL Routing**: Defining URL patterns and views
- **Database Management**: Working with Django models and the ORM
- **Template Integration**: Passing data from views to templates
- **Admin Interface**: Using Django's built-in admin panel
- **Form Handling**: Creating forms and processing user input

## 💡 Frontend Implementation

The UI was adapted from the tutorial's Bootstrap-based design. My focus for this project was primarily on developing backend functionality with Django rather than custom frontend styling. The templates use Bootstrap for responsive layouts and basic styling.

## 🛠️ Tech Stack

- **Backend**: 
  - Python 3.9+
  - Django 4.2
  
- **Frontend**: 
  - HTML5
  - CSS3 (Bootstrap 5)
  
- **Database**: 
  - SQLite (Django's default)

## 🔧 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/E-commerce-Blog.git
   cd E-commerce-Blog
   ```

2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv env
   
   # On Windows
   env\Scripts\activate
   
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (Optional - for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/


## 🎥 Credits

Big thanks to [CodeWithHarry](https://www.youtube.com/c/CodeWithHarry) for the excellent Django tutorial series on YouTube. This project was directly inspired by that series and helped me effectively grasp Django fundamentals.

## 🤝 Contributing

While this is primarily a personal learning project, feedback and suggestions are welcome! If you're also learning Django and want to suggest improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## 📌 Reflection

This project marks my first proper experience building with Django. While the frontend design follows the tutorial structure, my focus was on understanding Django's backend logic and architecture. I've gained valuable insights into how Django works and am excited to build more complex applications in the future.
