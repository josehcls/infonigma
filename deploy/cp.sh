echo 'Copying Gunicorn and Nginx Files'
sudo cp infonigma.service /etc/systemd/system/infonigma.service
sudo cp infonigma.socket /etc/systemd/system/infonigma.socket
sudo cp infonigma.conf /etc/tmpfiles.d/infonigma.conf
sudo cp infonigma /etc/nginx/sites-available/infonigma
sudo ln -s /etc/nginx/sites-available/infonigma /etc/nginx/sites-enabled
mkdir /home/infonigma/logs
touch /home/infonigma/logs/gunicorn.error
touch /home/infonigma/logs/gunicorn.access
echo 'Done!'
