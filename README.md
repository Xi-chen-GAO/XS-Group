***Project Overview***

 

The goal of this project is to track squirrels in Central Park. To achieve this goal, we designed a Django based website as our application, which consisted of 2 management commands (import and export) and 5 views (map, view, update, add, stats).  

 

***Management Commands:***

The import and export commands were achieved by creating two customized commands using the “BaseCommand” function of Django. The import command could import the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) data to the database and the export command could download the edited version of data in CSV format from the database.

***Views:***

-map 

This view shows a map which displays 100 locations of squirrel sightings on an OpenStreets map. We chose the latitude and longitude data from the database as our input and used the given template to plot the points.

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/map.png) 

-view

This view lists the unique squirrel ID and date of all squirrel sightings. Since there are more than 3000 records of squirrel sightings, it would be dauting to show all the records in one huge table. We employed the Django function “ListView” to separate records in 303 pages with 10 records in one page. Each record has a unique number in the beginning to identify it. Users could click “Next Page” button to see all squirrel sightings. 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/pages.png) 

This view also has a button called “view” which displays detailed information of that specific squirrel sighting once clicked. 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/views.png) 

When users click the “view” button, a new window will pop up, which is built according to the “Modal” in “bootstrap”. In the meanwhile, ajax is used to send a request to the server to get data needed in the window. 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/view2.png) 

 

-update

 

This view is used to edit a squirrel sighting and it is located on the left of “view” button. 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/update.png) 

 

When users click the “update” button, a new window will be pop up (similarly built by bootstrap) and ajax is used to send a request to the server to get data needed in the window. When the front end receives the response from the back end that it has finished the update process, JavaScript was employed to refresh the page to obtain the newest data. In this way, users could observe the change of a particular sighting on the webpage immediately.

 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/update2.png) 

 

 

-add

 

This view is used to create a new squirrel sighting, and it is located on the right corner of squirrel sightings table. 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/add2.png) 

When clicking the “Add sighting” button, users will be directed to a new window (built by bootstrap) to input the new sighting data. We also used JavaScript here to refresh the page to obtain the newest data. Users could click the “Nextpage” button to scroll down to the last page and they will find that a new squirrel sighting record is added to the squirrel sightings table. 

 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/add.png) 

 

-stat

This view displays general statistics analysis of squirrel sightings. We used “ECharts” to draw these two graphs.

 

The first graph is “squirrel sighting trend in October 2018”, showing the number of squirrels in some day in October 2018. We used ID, date and color fields from the database to draw this graph. The number of squirrels each day are separated by fur colors (Black, Cinnamon, Gray).

 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/state1.png) 

 

The second graph is “age distribution in different locations”. Location and age fields are used to draw this graph. It provides a general idea of the relationship between age of squirrels and the location squirrels are found. It can be observed that adult squirrels are more likely to be found on ground plane.

 

![img](https://github.com/Xi-chen-GAO/XS-Group/blob/main/img/state2.png) 



***Install:***

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



***Group information***

-Group name: XS Group, Section 1  
-UNIs: [xg2352, ss6159]  
-Server link: since deploy is not required in this project, there's no server link.  



***Reference***

- [Bootstrap,https://v4.bootcss.com/,Bootstrap · The most popular HTML, CSS, and JS library in the world.](https://v4.bootcss.com/)
- [echarts](https://echarts.apache.org/en/tutorial.html#5%20%E5%88%86%E9%92%9F%E4%B8%8A%E6%89%8B%20ECharts)

