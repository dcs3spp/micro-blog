# Welcome to Wellfound's microblog assessment!

## Goal

Your task is to update the home page of this Flask app to display all of the rows in the blog posts table instead of just the static single row. Make this change on a separate branch (not ‘main’), and create a merge request. After you complete this, you’re done!

<BR><BR>

## Contributions

Feel free to clone this repo locally and use your own editor of choice.

If you would rather use the Gitpod development environment for this app:

- Change the dropdown that says "Web IDE" to "Gitpod" (if it already says "Gitpod" skip this step)
- Click the button that says "Gitpod"

## Screenshot

**English**
![English](https://i.ibb.co/FwwdBFH/english.png "english")

**Spanish**
![Spanish](https://i.ibb.co/9bXPC13/spanish.png "spanish")

## Running the Solution

Issue the following commands to build the docker image and start a docker-compose stack as
a background task:

```bash
# build docker image
make build

# run docker-compose stack as background task
make up
```

Subsequently, perform the following steps:

- Visit `http://localhost:5000` in web browser
- Register a new user and login
- Once logged in there will be a navigation link provided, `posts`, and the user is redirected to `explore` endpoint
- Use the `posts` navigation link to add some posts
- After submitting each post, the user is redirected to the `explore` endpoint to display posts in descending order by time

## Solution

- Update the Jinja template to loop through posts
- Create a new route for creating a post and redirecting user to explore endpoint after submission
- Ensure the language is set for new post instances, using best matches from requests babel
- Update language translation files for new language navbar link publicacions
- Add jinja2 template to display isoformat excluding microseconds, use filter in display of posts table
- Add a docker-compose file that contains a service for the Flask microblog API
- Update the Dockerfile base image to use Python 3.10.6, problems were encountered with installing Python 3.11 on macOS environment
- Add a Makefile with make rules for building the docker image, in addition to starting and stopping the docker-compose stack
