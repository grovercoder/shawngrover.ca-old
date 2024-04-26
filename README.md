# Shawn Grover Website

See [shawngrover.ca](https://shawngrover.ca) to see this code in production.  This site is hosted on a virtual cloud server running Linux.

Shawn Grover is an experienced web application developer.  He focuses on Open Source technologies, but is also familiar with Windows and Windows Servers.  His skills cover low level networking, server installation/management, system design, both backend and frontend development, project management, and team management.  This is not a comprehensive list as each of these connects to many related skills.

This website paints Shawn Grover as a consultant for hire.  It serves as both an example of his coding styles, and as an addition to his online presence.

This website is a work in progress.  See the [TODO](TODO.md) file for known outstanding tasks.


## A note on styles

SASS/SCSS is used to generate the CSS styles.  This is reflected in the `css/styles.scss` file.  A separate include file is used for meaningful sections, as a way to help keep the code organized.

The CSS is generated via the Live SASS Complier extension for VSCode.  This allows generating the CSS files in place, in a live way.  

The SCSS files are included in the repository, but are not referred to directly in the HTML.  This has been deemed suitable for this personal website project.  For a customer's production site, the deployment process would be configured to handle these steps.  Perhaps via something like Webpack to generate a "dist" folder containing only the public items.

## Setup

1. Clone the repository
2. Set up and activate your virtual environment

    ```bash
    # for example
    cd cloned_project_directory
    python3 -m venv .venv

    source .venv/bin/activate
    ```

3. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```
4. Copy the `.env.EXAMPLE` to `.env` file and edit it for your needs

    ```bash
    cp .env.EXAMPLE .env
    ```

4. Run the application

    ```bash
    python3 main.py
    ```

For production use there are a few more steps:

1. Copy the `configs/nginx.conf` file to the production server, or use it as a guide for creating your own configuration.  Edit the file to meet your needs, and ensure the site is "active" for nginx.

    ```bash
    sudo cp configs/nginx.conf /etc/nginx/sites-available/mysite.conf
    # Edit the new file as needed
    ln -s /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf
    sudo nginx -t
    # fix any errors that may be reported
    sudo nginx -s reload #reload the config files
    # OR just restart the nginx service
    sudo systemctl restart nginx
    ```

1. Check the site is available in the browser.  At this point it should be using the manually started fastapi service.  This is fine for development purposes and testing, but production requires the service to be more robust. We'll do this be creating a Systemd service.

    ```bash
    sudo cp configs/systemd.service /etc/systemd/system/myapp.service
    # edit that file to ensure the paths point to the correct project folder
    # ensure the `project/.venv/bin` path is used for python3 to make use of the virtual environment
    sudo systemctl daemon-reload    # ensure systemd is aware of the new file
    # Make sure the "myapp.service" text matches the name of the file you created in `/etc/systemd/system`.
    sudo systemctl start myapp.service
    ```

1. Check the state of the service with `sudo systemctl status myapp.service`. Fix any errors that may be reported.
1. Open the now public site in your browser and confirm everything is working as expected.




