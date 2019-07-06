# Smart Garbage System
The **Smart Garbage System** develop an system of tracking the waste /recycle garbage data of houses by adding a barcode to these bin that will be scanned by truck garbage collector and saved with the corresponding weight of waste/recycle . These data will be saved in a database that can be accessed later by individual.

## Skills applied
 -Python

 -Flask

 -SQLAchemy

 -HTML
 
 -CSS
 
 


## Prerequisites
To run this project you need to install python, you'll need database software (provided by a Linux virtual machine) and the database (readingweight.db) .

The database includes three tables:

-usre table : save the user information

-measurementrecycle table : save the data of recycle bin

-measurementwaste table : save the data of waste bin

## Project content
The project have these content

+database_setup.py : The inital model of  the database.

+addreading.py : This file will add data to the table 

Also will have three folder:

+scanServer: It have wsServer.js file that will run contiously to read from the
serial port of scale .
-To run this file use this line in command prompt, note that scale is connected to COM4 :
node wsServer.js "COM4"

+scanapplication folder: it have scanapplication.py the application
on the  http://localhost:8000 .This application should be used by the truck labor to save garbae data with the barcode , for scanning the barcode it uses 
barcode to pc server mobile app , that it server should be run smiluntasly on the pc . 
To run n scanapplication.py use the vagrant server with this command:
python scanapplication.py

+userapplication folder : it have userapplication.py the application
on the  http://localhost:5000. This application should be used by end user to retrive it's waste/recycle data .
To run n userapplication.py use the vagrant server with this command:
python userapplication.py

## How to run

1.Install Vagrant and VirtualBox

2.Clone the [fullstack-nan laodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

3.Launch the Vagrant VM (vagrant up)

4.Log into Vagrant VM (vagrant ssh)

5.Navigate to cd/vagrant

6.Create the data by running:
  ```python database_setup.py```

    ```python lotsofmenus.py```

7.Run your application within the VM (python /vagrant/catalog2/project.py)
   by typing ```python project.py```

8.Access and test your application by visiting http://localhost:8000 locally

9.When creating new or editting Category/item the name should be unique.

## JSON API ENDPOINT
 The user can have the json api by these url

 Category JSON: `/catalog/<string:category_name>/items/JSON`

 Item JSON: `/catalog/<string:category_name>/<string:category_item>/JSON`

## Contributing

-The application can be modified to have more functionality such as
 image CRUD, recent item added and also the css style can be enhanced.

## Author
 Nadia Ahmed