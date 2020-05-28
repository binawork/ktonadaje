# KtoNadaje.pl  

> Livestream and videochat aggregator  
  
## Table of contents  

- [General info](#general-info)  
- [Technologies](#technologies)  
- [Business Documentation](#business-documentation)  
- [Setup](#setup)  
-- [Development on Ubuntu](#development-on-linux-ubuntu-18)  
-- [Development on Windows](#development-on-windows-10)
- [Features](#features)  
- [Status](#status)  
- [Inspiration](#inspiration)  
- [Contact](#contact)  
  
## General info  

> The web application created as part of [BINA.work](https://www.notion.so/BINA-work-56326159aff1491ca1d587b2519a65f9). The main motivation to start work was the COVID-19 pandemic and the desire to help creators promote their online activity.  
  
## Technologies  

| name   | version | description |  
| ---    | ---     | --- |  
| Python | 3.8.2   |     |  
| Flask  | 1.1.2   |     |  
| SQLALchemy | 1.3.16 |  |  
| PostrgeSQL | 10.12  |  |  
  
## Business Documantation
  
- [Business project documentation and workspace](https://www.notion.so/Ktonadaje-pl-1cbf7341c6d54c4fb37582c02308f813).  
- [Link to application mockup](https://sites.google.com/view/ktonadajenavbar/).  
  
## Setup  
  
### Development on Linux Ubuntu 18+  

#### Clone project

To run the project locally, you need to have Python 3.8+ and PostgreSQL 10.12+ installed. If you already have it, go to the next steps.  
  
Copy the source code to your machine:  
  
```bash
git clone git@github.com:kMatejak/ktonadaje.git YYY
cd YYY
```  
  
#### Create Python environment  

Then create a virtual environment, checkout to branch `develop` and install all requirements. `virtualenv` is used to isolate Python modules so they don’t pollute your system. Our referenced version of the `virtualenv` in at least 16.7.8.  

```bash
virtualenv env
source env/bin/activate
git checkout develop
pip install -r requirements.txt
```  

#### (OPTIONAL) Set local variables with `autoenv`  

To set up the application with environment variables you use `autoenv` \([link](https://github.com/inishchith/autoenv)). This program allows us to set commands that will run every time we `cd` into our directory. In order to use it, we will need to install it globally. First, exit out of your virtual environment in the terminal, install `autoenv` and then add an **.env** file:  

```bash
deactivate
pip install autoenv==1.0.0
touch .env
```  

Next, in your **.env** file, add the following:  

```bash
source env/bin/activate
export FLASK_ENV=development
export FLASK_DEBUG=True
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=postgresql://postgres:password@localhost/ktonadaje_dev
```  

Run the following to update and then refresh your _.bashrc_:  

```bash
echo "source `which activate.sh`" >> ~/.bashrc
source ~/.bashrc
```  

Now, if you move up a directory and then `cd` back into it, the virtual environment will automatically be started and the APP_SETTINGS variable is declared.  
  
#### Set local variables for development environment  

>This step is not necessary if you have passed the previous one. Skip to [the next step](#create-local-dev-database).  
  
To configure the application with environment variables, add the file **.env** in the project root and paste the following into it:  

```bash
FLASK_ENV=development
FLASK_DEBUG=True
APP_SETTINGS=config.DevelopmentConfig
DATABASE_URL=postgresql://postgres:password@localhost/ktonadaje_dev
```  

You can read more about connection URI format (the last line in this code snippet above) [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format).  
  
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
$ git clone git@github.com:kMatejak/ktonadaje.git YYY
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

#### Set local variables for development environment  

To configure the application with environment variables, add the file **.env** in the project root and paste the following into it:  

```bash
FLASK_ENV=development
FLASK_DEBUG=True
APP_SETTINGS=config.DevelopmentConfig
DATABASE_URL=postgresql://postgres:password@localhost/ktonadaje_dev
```  

You can read more about connection URI format (the last line in this code snippet above) [here](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format).  
  
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
  
## Features  

List of features ready and TODOs for future development  

- Displaying table with events  
  
To-do list:  

- Adding events via the form
- Register and login users  
- Sorting table contents  
  
## Status  

Project is: _in progress_  
  
## Contact  

Created by [@BINA.work](http://www.bina.work):  

- [Wiktor Świątkowski \(project manager & product owner)](https://www.linkedin.com/in/wiktorswiatkowski/),  
- [Krzysztof S. Matejak "Kris" \(dev)](https://www.linkedin.com/in/matejak/),  
- [Tomasz Leszczyński \(dev)](https://www.linkedin.com/in/tomasz-leszczy%C5%84ski-515b0022/),  
- [Monika Zabdyr \(ux/ui, design)](https://www.linkedin.com/in/monika-zabdyr/)  
- [Maciej Ambroziak \(dev)](https://github.com/MaciejAmbroziak),  

Feel free to contact us!  
  