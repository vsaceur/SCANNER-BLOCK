# SCANNER-BLOCK
A pythonscript that mimics a webserver on nonstandard ports and sends the IP ADDR TO MQTT
A NODERED SETUP that SUBSCRIBES TO THE MQQTT and INFORMS SHOREWALL TO BLOCK TAHT IP ADDR
Another NODERED  SETUP THAT LIST ALL IPADDRESSES THAT HAVE BEEN DYNAMICALLY BLOCKED AND PERFORMS A NMAP CHECK OF OPEN PORTS
FINALLY FILLS A DATBASE THAT CAN BE QUERIED AND ANALIZED IN A LOCAL DJANGOWEBPLACE
