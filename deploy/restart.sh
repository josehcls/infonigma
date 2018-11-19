echo '(Re)Starting Gunicorn and Nginx'
sudo systemctl daemon-reload
sudo systemctl enable infonigma
sudo systemctl restart infonigma
sudo systemctl enable nginx
sudo systemctl restart nginx
sudo systemctl enable infonigma.socket
sudo systemctl restart infonigma.socket
echo 'Done!'
