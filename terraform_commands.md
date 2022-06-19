
## Terraform Commands
### Installation (-debian)
- Create a working directory
```bash
  $ sudo mkdir -p /opt/terraform
  $ cd /opt/terraform 
```
- Download Terraform from Hasicorp website
```bash
  $ sudo wget https://releases.hashicorp.com/terraform/0.15.3/terraform_0.15.3_linux_amd64.zip
```

- Unzip Terraform Zip file
```bash
  $ sudo unzip terraform_0.15.3_linux_amd64.zip
```

- Add terraform to PATH
```bash
  $ sudo mv /opt/terraform/terraform /usr/bin/
  $ terraform -version
```
### Commands
- Initialize (after declaring the provider)

```bash
  $ terraform init
```
- compare between current state and existing template
```bash
  $ terraform plan
```    
- apply the template 

```bash
  $ terraform apply
  $ terraform apply --auto-approve
```
- destroy everything/ a resource 

```bash
  $ terraform destroy
  $ terraform destroy -target aws_subnet.dev-subnet-2

  better way is to delete the corresponding resource from the template and apply Terraform config file
```
- show list of resources/datasources for the current state

```bash
  $ terraform state list
  $ terraform state show <RESOURCE-NAME>
```
#### Variable Files
- default variable file is **terraform.tfvars** , no need to mention specifically while apply

```bash
  $ terraform apply
```
- if there are different variable files like( terraform-dev.tfvars ) then

```bash
  $ terraform apply -var-file <FILE-NAME>
```
- instead of mentioning the AWS credentials in config file,better use environment variables

```bash
  $ export AWS_ACCESS_KEY_ID="anaccesskey"
  $ export AWS_SECRET_ACCESS_KEY="asecretkey"
  $ export AWS_REGION="us-west-2"
```
- custom Terraform environment variables using **TF_VAR** _<VARIABLE-NAME>

```bash
  $ export TF_VAR_<VARIABLE-NAME>=<VALUE>
```
- check the environment variables

```bash
  $ env | grep AWS
```
  - configure AWS credentials globally using **AWS-CLI** 

```bash
  $ sudo apt install awscli
  $ aws configure
  AWS Access Key ID [None]: XXXXXXXXXXXXXX
  AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXX
  Default region name [None]: us-east-1
  Default output format [None]: 
```
- check the AWS config and credentials files

```bash
  $ cat ~/.aws/credentials
  $ cat ~/.aws/config
```
