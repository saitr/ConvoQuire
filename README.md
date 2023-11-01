# ConvoQuire

ConvoQuire is a simple web application for sharing posts and engaging in discussions. It provides a platform for users to post questions and comments on various topics.

## Features

- **User Authentication:** Users can sign up, log in, and log out.
- **Post Creation:** Registered users can create new posts with headings and descriptions.
- **Like and Comment:** Users can like and comment on posts.
- **View All Posts:** A page to view all posts created by users.
- **Post Detail:** View details of a specific post, including comments.
- **Django and Jinja Templating:** The application is built using Django and utilizes Jinja templating for dynamic web pages.
- **Responsive Design:** Designed with a responsive and user-friendly interface.
- **Bootstrap:** Stylish and user-friendly UI created using Bootstrap.
- **Docker Containerization:** Containerized using Docker for easy deployment.
- **GitHub Version Control:** Utilized GitHub for version control and collaboration.
- **Vercel Deployment:** Deployed the application on Vercel.

## Usage

- <b>Visit the deployed application</b>: [ConvoQuire](https://convo-quire-git-main-saitrs-projects.vercel.app/all_posts/)

- <b>To run the application using Docker</b>:

    1. Pull the Docker image:

        ```bash
        docker pull saitreddy/convoquire:r_v1
        ```

    2. Run the Docker container:
        ```bash
        docker run -p 8000:8000 saitreddy/convoquire:r_v1
        ```
    3. Run the Docker container in detatched mode:

        ```bash
        docker run -d -p 8000:8000 saitreddy/convoquire:r_v1
        ```
  
    4. Access the application in your browser: `http://127.0.0.1:8000/`



- <b>To run the application locally, follow these steps</b>:

    1. Clone the repository:

        ```bash
        git clone https://github.com/saitr/ConvoQuire.git
        cd convoquire
        ```

    2. Create a Python virtual environment (recommended):

        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

    3. Install project dependencies:

        ```bash
        pip install -r requirements.txt
        ```

    4. Apply database migrations:

        ```bash
        python manage.py migrate
        ```

    5. Start the development server:

        ```bash
        python manage.py runserver
        ```

    6. Access the application in your browser: `http://127.0.0.1:8000/`




**Developed with ❤️ by Sai Thimma Reddy D**

For inquiries and collaborations, please contact [saithimmareddy480@gmail.com] or visit my [portfolio](https://saitr.github.io/Sai_TR_Resume/).


