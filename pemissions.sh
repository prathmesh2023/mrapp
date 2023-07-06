sudo ufw app info "Apache Full"

sudo ufw allow in "Apache Full"

sudo chown :www-data mrapp
sudo chown :www-data mrapp/db.sqlite3
sudo chown :www-data mrapp/static/
sudo chown :www-data mrapp/static/bootstrap/
sudo chown :www-data mrapp/static/css/
sudo chown :www-data mrapp/static/js
sudo chown :www-data mrapp/static/res


sudo chown :www-data mrapp/media/
sudo chown :www-data mrapp/media/profiles
sudo chown :www-data mrapp/media/slides




sudo chmod -R 775 mrapp/

sudo chmod -R 775 mrapp/db.sqlite3
sudo chmod -R 775 mrapp/static/
sudo chmod -R 775 mrapp/static/bootstrap/
sudo chmod -R 775 mrapp/static/css/
sudo chmod -R 775 mrapp/static/js
sudo chmod -R 775 mrapp/static/res


sudo chmod -R 775 mrapp/media/
sudo chmod -R 775 mrapp/media/profiles
sudo chmod -R 775 mrapp/media/slides


 sudo systemctl restart apache2