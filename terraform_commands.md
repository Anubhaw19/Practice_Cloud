
## Terraform Commands
### installation (-debian)
- Create a working directory
```bash
  sudo mkdir -p /opt/terraform
  cd /opt/terraform 
```
- Download Terraform from Hasicorp website
```bash
  sudo wget https://releases.hashicorp.com/terraform/0.15.3/terraform_0.15.3_linux_amd64.zip
```

- Unzip Terraform Zip file
```bash
  sudo unzip terraform_0.15.3_linux_amd64.zip
```

- Add terraform to PATH
```bash
  sudo mv /opt/terraform/terraform /usr/bin/
  terraform -version
```
### Commands
- Initialize (after declaring the provider)

```bash
  terraform init
```
- compare between current state and existing template
```bash
  terraform plan
```    
- apply the template 

```bash
  terraform apply
  terraform apply -auto-approve
```
- destroy everything/ a resource 

```bash
  terraform destroy
  terraform destroy -target aws_subnet.dev-subnet-2

  better way is to delete the corresponding resource from the template and apply Terraform config file
```
- show list of resources/datasources for the current state

```bash
  terraform state list
  terraform state show <resource name>
```
