# KtoNadaje.pl  
> Here goes your awesome project description!  
  
## Table of contents  
- [General info](#general-info)  
- [Screenshots](#screenshots)  
- [Technologies](#technologies)  
- [Setup](#setup)  
-- [Development on Ubuntu](#Development-on-Linux-Ubuntu-18+)  
-- [Development on Windows](#Development-on-Windows-10)
- [Features](#features)  
- [Status](#status)  
- [Inspiration](#inspiration)  
- [Contact](#contact)  
  
## General info  
Add more general information about project. What the purpose of the project is? Motivation?
  
## Screenshots  
![Example screenshot](./img/screenshot.png)  
  
## Technologies  
| name   | version | description |  
| ---    | ---     | --- |  
| Python | 3.8.2   |     |  
| Flask  | 1.1.2   |     |  
| SQLALchemy | 1.3.16 |  |  
| PostrgeSQL | 10.12  |  |  
  
## Setup  
### Mockup  
Link to the mockup of this app, 
[here](https://sites.google.com/view/ktonadajenavbar/).  
### Development on Linux Ubuntu 18+  
#### Clone project
To run the project locally, you need to have Python 3.8+ and PostgreSQL 10.12+ 
installed. If you already have it, go to the next steps.  
  
Copy the source code to your machine:  
```bash
git clone git@github.com:MaciejAmbroziak/Stream.git YYY
cd YYY
```  
#### Create Python environment  
Then create a virtual environment, checkout to branch `develop` and install 
all requirements. `virtualenv` is used to isolate Python modules so they 
don’t pollute your system. Our referenced version of the `virtualenv` in at 
least 16.7.8.  
```bash
virtualenv env
source env/bin/activate
git checkout develop
pip install -r requirements.txt
```  
#### Prepare local env with autoenv  
To set up the application with environment variables, we suggest to use 
`autoenv`. This program allows us to set commands that will run every time 
we `cd` into our directory. In order to use it, we will need to install it 
globally. First, exit out of your virtual environment in the terminal, 
install `autoenv`, and then add a **.env** file:  
```bash
deactivate
pip install autoenv==1.0.0
touch .env
```  
Next, in your **.env** file, add the following:  
```
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql:///ktonadaje_dev"
```  
Run the following to update and then refresh your _.bashrc_:  
```bash
echo "source `which activate.sh`" >> ~/.bashrc
source ~/.bashrc
```  
Now, if you move up a directory and then `cd` back into it, the virtual environment will automatically be started and the APP_SETTINGS variable is declared.  
  
#### Create local dev database  
```bash
psql
CREATE DATABASE ktonadaje_dev;
\q
```  
And then apply the upgrades from migrates to your database:  
```bash
python manage.py db upgrade
```  
#### Check it out!  
Finally, check that the project works:  
```bash
python app.py
```  
Optionally, you can also insert sample data into your database. Just use the already prepared script:  
```bash
python insert_sample_data_dev_db.py
```  
### Development on Windows 10  
#### Clone project
To run the project locally, you need to have Python 3.8+ \([link](https://realpython.com/installing-python/#windows)) and PostgreSQL 10.12+ \([link](https://www.postgresqltutorial.com/install-postgresql/)) installed. Also this instruction assumes that you have Git installed with Bash extension \([link](https://phoenixnap.com/kb/how-to-install-git-windows)). If you already have it, go to the next steps.  
  
Open `Git Bash`, go to the directory where you want to clone the project and copy it to your machine:  
```bash
$ git clone git@github.com:MaciejAmbroziak/Stream.git YYY
$ cd YYY
```  
#### Create Python environment  
Then create a virtual environment, checkout to branch `develop` and install all requirements. `virtualenv` is used to isolate Python modules so they don’t pollute your system. Our referenced version of the `virtualenv` is at least 16.7.8.  
  
This instruction uses the `py` shortcut, which can be set when installing Python on Windows 10. If you do not have this option set, use the full word `python` instead.  
  
**(!)** If you already have `virtualenv` installed, skip that one line below.  
```bash
$ py -m pip install virtualenv
```  
```bash
$ py -m virtualenv env
$ source env/Scripts/activate
$ git checkout develop
$ py -m pip install -r requirements.txt
```  
#### Prepare local env with autoenv  
To set up the application with environment variables, we suggest to use [autoenv](https://github.com/inishchith/autoenv/blob/master/README.md). This program allows us to set commands that will run every time we `cd` into our directory. In order to use it, we will need to install it globally. First, exit out of your virtual environment in the Git Bash, install `autoenv`, and then add a **.env** file:  
```bash
$ deactivate
$ py -m pip install autoenv==1.0.0
$ touch .env
```  
Next, in your **.env** file, add the following:  
```
source env/Scripts/activate
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://postgres:password@localhost/ktonadaje_dev"
```  
You can read more about connection URI format (the last line in this code snippet above) [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format).  
  
Now, run the following to install `autoenv`, create \(or update) _.bashrc_ and then refresh your terminal with updated _.bashrc_:  
```bash
$ git clone git://github.com/inishchith/autoenv.git ~/.autoenv
$ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
$ source ~/.bashrc
```  
Now, if you move up a directory and then `cd` back into it, the virtual environment will automatically be started and the APP_SETTINGS variable is declared.  
  
#### Create local dev database  
Create new database with tiping into **`SQL Shell (psql)`**:  
```bash
CREATE DATABASE ktonadaje_dev;
\q
```  
And then (into **`Git Bash`**) apply the database structure to your database:  
```bash
$ py manage.py db upgrade
```  
#### Check it out!  
Finally, check that the project works:  
```bash
$ py app.py
```  
And, optionally, you can also insert sample data into your database. Just use the already prepared script:  
```bash
$ py insert_sample_data_dev_db.py
```  
## Code Examples  
Show examples of usage:  
`put-your-code-here`  
  
## Features  
List of features ready and TODOs for future development  
* Awesome feature 1  
* Awesome feature 2  
* Awesome feature 3  
  
To-do list:  
* Wow improvement to be done 1  
* Wow improvement to be done 2  
  
## Status  
Project is: _in progress_  
  
## Contact  
Created by [@BINA.work](http://www.bina.work):  
* Maciej Ambroziak (dev),  
* [Krzysztof S. Matejak "Kris" \(dev)](https://www.linkedin.com/in/matejak/),  
* Wiktor Świątkowski (pm),  
* Monika Zabdyr (ux, design)  

Feel free to contact us!  
  