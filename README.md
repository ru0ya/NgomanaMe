# NgomanaMe

## Overview
NgomanaMe is a Django-based platform dedicated to democratizing access to musical information by providing a **DIY hub** where educators across different regions in Kenya can share their methods and materials for building musical instruments. 

The platform fosters community engagement by allowing users to:
- Share their experiences and step-by-step guides for instrument creation.
- Comment on existing solutions to improve or discuss methodologies.
- Provide additional resources to help educators further their musical knowledge and enhance student learning.

## Features
- **User Authentication:** Secure user registration and login system.
- **DIY Instrument Guides:** A repository where educators can submit detailed guides on making musical instruments.
- **Commenting System:** Users can comment and provide feedback on the available DIY guides.
- **Resource Sharing:** A dedicated section for sharing musical education materials and external learning resources.
- **Search and Filter:** Users can easily search and filter through available guides and resources.
- **Responsive Design:** Optimized for both desktop and mobile users.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- Django (>=4.0)
- PostgreSQL or SQLite (for development)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/NgomanaMe.git
   cd NgomanaMe
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the application at `http://127.0.0.1:8000/`

## Usage
- Educators can sign up and contribute DIY instrument-making guides.
- Users can browse existing guides, comment on them, and suggest improvements.
- A section dedicated to additional learning resources is available for educators and students.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Description of changes"
   ```
4. Push the changes:
   ```sh
   git push origin feature-name
   ```
5. Open a Pull Request.

## License
NgomanaMe is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries, please reach out via mwangiruoya@gmail.com or open an issue on the repository.
