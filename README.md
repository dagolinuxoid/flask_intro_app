Requirements and how to deploy/build locally
```
python3
virtual environment
sqlite3 (for master branch)
postgresql (for postgre-branch branch)

clone this repo (flask_intro_app)
cd flask_intro_app

There we go | sqlite version (git checkout master)
virtualenv ve
source ve/bin/activate or . ve/bin/activate
pip install -r requirements.txt
sqlite3 data.db < schema.sql
python route.py

in your browser — localhost:5000/

| postgresql version (git checkout postgre-branch)
pretty mutch the same except :
pip install -r requirements.txt
createdb --owner=someUser nameOfYourPosgtreSQLdb
psql nameOfYourPostgreSQLdb < schema.sql
change db=SQL('...') in routes.py accordingly
```
