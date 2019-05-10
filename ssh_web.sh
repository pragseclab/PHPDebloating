db_id=$(sudo docker ps | grep web | cut -d' ' -f 1)
sudo docker exec -it $db_id /bin/bash
