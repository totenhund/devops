
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}


variable "access" {
  type = string
}

variable "secret" {
  type = string
}

provider "aws" {
  region     = "us-east-2"
  access_key = var.access
  secret_key = var.secret
  profile = "default"
}

resource "aws_instance" "app" {
  ami = "ami-00399ec92321828f5"
  instance_type = "t2.micro"
  tags = {
    Name = "mytag"
  }
}