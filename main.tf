# ----------------------------------------------------------------------------------------------------------------------
# Provider
# ----------------------------------------------------------------------------------------------------------------------
provider "aws" {
  region = var.AWS_DEFAULT_REGION
}

data "terraform_remote_state" "infracore" {
  backend = "remote"

  config = {
    hostname     = "app.terraform.io"
    organization = "grupoboticario-AWS"

    workspaces = {
      name = var.WORKSPACE_INFRACORE
    }
  }
}

# ------------- #
# EC2 - IIS - 1 #
# ------------- #
module "ec2-iis-dev-1" {
  source  = "app.terraform.io/grupoboticario-AWS/ec2/aws"
  version = "1.0.2"

  name           = "IIS-SITES-DEV-1"
  instance_count = 1
  ami            = "ami-0f93c815788872c5d" # Microsoft Windows Server 2019 Base
  instance_type  = var.instance_type
  key_name       = "${var.environment}-ec2-iis-dev-1"
  monitoring     = false
  vpc_id         = data.terraform_remote_state.infracore.outputs.vpc_id
  vpc_cidr_block = [data.terraform_remote_state.infracore.outputs.vpc_cidr]
  subnet_id      = data.terraform_remote_state.infracore.outputs.private_subnet_ids[0]

  root_block_device = [{
    volume_size = "30"
  }]
  ebs_block_device = [{
    volume_size = "50"
    device_name = "/dev/xvdb"
  }]

  tags = {
    App         = "iis-sites"
    Vs          = "colaborador"
    Environment = var.environment
    Squad       = "colaborador"
    Product     = "iis-sites"
    Tier        = "frontend"
    Terraform   = var.terraform_workspace
  }
  
  volume_tags = {
    App         = "iis-sites"
    Vs          = "colaborador"
    Environment = var.environment
    Squad       = "colaborador"
    Product     = "iis-sites"
    Tier        = "frontend"
    Terraform   = var.terraform_workspace
  }
}