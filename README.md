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

2.Launch the Vagrant VM (vagrant up)

3.Log into Vagrant VM (vagrant ssh)

4.Navigate to cd/vagrant

5.Create the data by running:
  ```python database_setup.py```

    ```python addreading.py```

6.Run your scan application within the VM (python /vagrant/scanapplication/scanapplication.py)
   by typing ```python scanapplication.py```

7.Access and test your application by visiting http://localhost:8000 locally

8.Run your user application within the VM (python /vagrant/userapplication/userapplication.py)
   by typing ```python userapplication.py```

9.Access and test your application by visiting http://localhost:5000 locally

##Thanks

-Many thanks to Tom Igoe for sharing his code of how to read from Serial port, the file used is wsServer.js

## Contributing

-The application can be modified to have more functionality such as
 including chart of data.

## Author
 Nadia Ahmed