apt-get update
apt-get upgrade
apt-get install python-pip
pip install virtualenv
virtualenv -p python venv
pip install -r Requirements.txt
source it_kgb/venv/bin/activate
chmod +x manage.py
python3 manage.py runserver
