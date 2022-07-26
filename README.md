# Practice_Cloud


### Appendix

 - [Generate key and SSH from one VM to another VM](https://github.com/Anubhaw19/Practice_Cloud/blob/main/generateKey%26SSH.md)
 - [Docker Commands](https://github.com/Anubhaw19/Practice_Cloud/blob/main/docker_commands.md)
 - [Nginx Commands](https://github.com/Anubhaw19/Practice_Cloud/blob/main/nginx.md)
 - [Jenkins Setup](https://www.jenkins.io/doc/book/installing/linux/)
 - [Terraform Commands](https://github.com/Anubhaw19/Practice_Cloud/blob/main/terraform_commands.md)
 - [Kubernetes Commands](https://github.com/Anubhaw19/Practice_Cloud/blob/main/kubernetes.md)





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

## Jenkins Setup
```bash
 #!/bin/bash
          sudo apt install openjdk-11-jdk -y
          export JAVA_HOME=/usr/lib/jvm/openjdk-11
          export PATH=$PATH:$JAVA_HOME/bin
          echo "export JAVA_HOME=/usr/lib/jvm/openjdk-11" | sudo tee --append /etc/profile
          echo "export PATH=\$PATH:\$JAVA_HOME/bin" | sudo tee --append /etc/profile
          curl -fsSL https://pkg.jenkins.io/debian/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
          echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee  /etc/apt/sources.list.d/jenkins.list > /dev/null
          sudo apt-get update -y
          sudo apt-get install jenkins -y
          sudo systemctl start jenkins.service
          sudo ufw allow 8080
          sudo ufw allow OpenSSH
          sudo ufw --force enable
```
