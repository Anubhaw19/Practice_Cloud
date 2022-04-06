
## Nginx commands
- Install nginx 

```bash
  sudo apt install nginx
```
    
- ubuntu firewall app list

```bash
  sudo ufw app list
```
- allow HTTP request in firewall 

```bash
  sudo ufw allow 'Nginx HTTP'
```
    
- see status of firewall 

```bash
  sudo ufw status
```
- activate firewall if inactive
```bash
  sudo ufw enable
```
    
- see Nginx status

```bash
  sudo systemctl status nginx
```

- find public IP of VM

```bash
  curl -f icanhazip.com
```
- stop Nginx

```bash
  sudo systemctl stop nginx
```
- start or restart Nginx webserver

```bash
  sudo systemctl start nginx
```
```bash
  sudo systemctl restart nginx
```
- apply configuration changes without restart

```bash
  sudo systemctl reload nginx
```
- disable nginx on system startup

```bash
  sudo systemctl disable nginx
```
