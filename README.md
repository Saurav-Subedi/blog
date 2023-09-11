# Django Blog Posting Website

Welcome to the Django Blog Posting Website!
This web application allows users to create, read, update, and delete blog posts after signing up for an account.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Authentication and User Management (django-allauth)](#authentication-and-user-management-django-allauth)
  - [Rich Text Editing (django-ckeditor)](#rich-text-editing-django-ckeditor)
  - [Admin Interface (django-jazzmin)](#admin-interface-django-jazzmin)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication (using django-allauth).
- Create, read, update, and delete blog posts.
- Rich text editing with the CKEditor (using django-ckeditor).
- Custom admin interface with Jazzmin (using django-jazzmin).
- Responsive design for various screen sizes.
- 
## Getting Started

### Prerequisites

- Python (3.7+)
- Django (3.0+)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Saurav-Subedi/blog
   ```

2. Navigate to the project directory:

   ```shell
   cd django-blog-website
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```shell
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Usage

1. Migrate the database:

   ```shell
   python manage.py migrate
   ```

2. Create a superuser to manage the application:

   ```shell
   python manage.py createsuperuser
   ```

3. Start the development server:

   ```shell
   python manage.py runserver
   ```

4. Access the website in your web browser at `http://localhost:8000`.

5. Log in with your superuser account or sign up for a new account to start posting blogs.

6. Customize the website according to your project needs.

#### Authentication and User Management (django-allauth)

- Configure the authentication and user management settings in your project's settings.py file.
- Customize the templates and views for registration, login, and profile pages as needed.
- For more information, refer to the [django-allauth documentation](https://django-allauth.readthedocs.io/en/latest/).

#### Rich Text Editing (django-ckeditor)

- Integrate CKEditor into your blog post creation/editing forms.
- Customize CKEditor settings and configurations in your project's settings.py file.
- For more information, refer to the [django-ckeditor documentation](https://github.com/django-ckeditor/django-ckeditor).

#### Admin Interface (django-jazzmin)

- Experience a customized admin interface with Jazzmin.
- Customize Jazzmin's appearance and functionality in your project's settings.py file.
- For more information, refer to the [django-jazzmin documentation](https://github.com/farridav/django-jazzmin).

### Contributing

If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them.
- Push your changes to your fork.
- Submit a pull request to the main repository.

### License

[License information goes here, e.g., MIT License]

---
