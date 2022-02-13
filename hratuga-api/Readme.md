# go to backend folder
`cd hratuga-api/`

# create venv
`virtualenv venv`

# activate venv
`source venv/bin/activate`

Mac, Linux: ( `pipenv install` )
             `pipenv shell`

# install
`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py add_users`

Mac, Linux:
`python manage.py loaddata data/test-data/*.json`

Windows: `python manage.py add_fixtures test-data`

`python manage.py runserver`

# deactivate venv
`deactivate`

# PostGres for MacOS
`brew install postgresql`


# docker
docker run -ti -e AWS_PROFILE=default -v "$(pwd):/var/task" -v ~/.aws/:/root/.aws  --rm lambci/lambda:build-python3.8 bash

# create venv
`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`zappa update dev`
