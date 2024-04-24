# Shawn Grover Website

Shawn Grover is an experienced web application developer.  He focuses on Open Source technologies, but is also familiar with Windows and Windows Servers.  His skills cover low level networking, server installation/management, system design, both backend and frontend development, project management, and team management.  This is not a comprehensive list as each of these connects to many related skills.

This website paints Shawn Grover as a consultant for hire.  It serves as both an example of his coding styles, and as an addition to his online presence.

This website is a work in progress.  See the [TODO](TODO.md) file for know outstanding tasks.


## A note on styles

I use SASS/SCSS to generate the CSS styles.  This is reflected in the `css/styles.scss` file.  A separate include file is used for meaningful sections, as a way to help keep the code organized.

I generate the CSS via the Live SASS Complier extension for VSCode.  This allows me to generate the CSS files in place, in a live way.  

The SCSS files are included in the repository, but are not referred to directly in the HTML.  This is acceptable for my own personal website.  For a customer's production site, I would configure the deployment system to ONLY move the CSS files, or utilize a build system like Webpack to generate a "dist" folder containing only the public items.