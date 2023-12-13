# build_files.sh
pip install -r ./requirements/development.txt

# make migrations
python3 manage.py migrate 
python3 manage.py collectstatic
