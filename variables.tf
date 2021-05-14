################################################################################
# AWS
################################################################################
variable "AWS_DEFAULT_REGION" {
  type        = string
  description = "AWS region in wich resources shall be created"
}

variable "AWS_SECRET_ACCESS_KEY" {
  type        = string
  description = "AWS access key"
}

variable "AWS_ACCESS_KEY_ID" {
  type        = string
  description = "AWS access key ID"
}

variable "WORKSPACE_INFRACORE" {
  description = "WORKSPACE_INFRACORE"
  type        = string
  default     = "aws-development-account-infracore"
}

variable "ec2_ami_id" {
  type        = string
  description = "Id of the ami"
  default     = "ami-0f93c815788872c5d"
}

variable "environment" {
  description = "Variable to set environment"
  default     = "homologation"
}

variable "terraform_workspace" {
  description = "Terraform Cloud Workspace"
  default     = "aws-homologation-horus-resources"
}