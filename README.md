# XS-Group

1. Project discription
The squirrel tracking project aims to keep track of squirrels in Central Park. 
On our django based webpage, the location of squirrel sightings are dispalyed on a map. The details of each sighting are listed in a table, allowing for viewing and updating. Users can also create a new sighting to update the database. General statitics analysis was conducted to visualize the squirrel sighting trend in October, 2018, as well as the age distribution in different locations.

2. Group information
  -Group name: XS Group, Section 1
  -UNIs: [xg2352, ss6159]
  -Server link: since deploy is not required in this project, there's no server link.

3. Install

  (1)clone project

  ```shell
  git clone https://github.com/Xi-chen-GAO/XS-Group
  ```

  (2)install requirements

  ```shell
  pip install -r requirements.txt
  ```

  (3)migrate db

  ```shell
  cd tracker
  python manage.py migrate
  ```

  (4)import data

  ```shell
  python manage.py import_squirrel_data /path/to/file.csv
  ```

  (5)export data

  ```shell
  python manage.py export_squirrel_data /path/to/file.csv
  ```

  (6)run server

  ```shell
  python manage.py runserver
  ```

