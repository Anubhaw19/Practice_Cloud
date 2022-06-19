# initilizing the provider (AWS)
provider "aws" {
  region = "us-east-1"
  # access_key = "XXXXXXXXXXXXXX"
  # secret_key = "XXXXXXXXXXXXXXXXXX"
}

# declaring a variable  and initializing them in terraform.tfvars file
variable "vpc_cidr" {
  description = "vpc CIDR block"
  default = "10.0.0.0/16"
  type = string
}
variable "subnet2_cidr" {
  description = "subnet2 cidr block"
  default = "10.0.20.0/24"
  type=string
   
 }

# creating a new resource 
resource "aws_vpc" "vpc_anu" {
  cidr_block = var.vpc_cidr
   tags = {
    Name = "anu_vpc"
  }

}

resource "aws_subnet" "subnet1" {
  vpc_id     = aws_vpc.vpc_anu.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "subnet_anu1"
  }
  availability_zone="us-east-1a"
}

# refrencing already created/existing resources using datasource

data "aws_vpc" "existing_vpc" {
  id = "xxxxxxxxxxxxxx"
}

resource "aws_subnet" "subnet2" {
  vpc_id            = data.aws_vpc.existing_vpc.id
  cidr_block        = var.subnet2_cidr
   tags = {
    Name = "subnet_anu2"
  }
}

# output the created resource attributes in the console
output "vpc-id" {
  value= aws_vpc.vpc_anu.id
}
