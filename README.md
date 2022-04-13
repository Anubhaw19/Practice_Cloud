# Practice_Cloud


### Appendix

 - [Generate key and SSH from one VM to another VM](https://github.com/Anubhaw19/Practice_Cloud/blob/main/generateKey%26SSH.md)
 - [Docker Commands](https://github.com/Anubhaw19/Practice_Cloud/blob/main/docker_commands.md)
 - [Nginx Commands](https://github.com/Anubhaw19/Practice_Cloud/blob/main/nginx.md)
 - [Jenkins Setup](https://www.jenkins.io/doc/book/installing/linux/)





## ssh 

* create a public and private ssh-keys in local host 

```bash
  ssh-keygen -t rsa
```

* copy the public-key to remote host for authentication
```bash
  ssh-copy-id user@ip
```
* ssh into a VM
```bash
  ssh user@ip
```


