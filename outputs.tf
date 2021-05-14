# ------------- #
# EC2 - IIS - 1 #
# ------------- #
output "id-ec2-iis-dev-1" {
  description = "List of IDs of instances"
  value       = module.ec2-iis-dev-1.*.id
}

output "arn-ec2-ec2-iis-dev-1" {
  description = "List of ARNs of instances"
  value       = module.ec2-iis-dev-1.arn
}

output "key_name-ec2-iis-dev-1" {
  description = "List of key names of instances"
  value       = module.ec2-iis-dev-1.key_name
}

output "private_ip-ec2-iis-dev-1" {
  description = "List of private IP addresses assigned to the instances"
  value       = module.ec2-iis-dev-1.private_ip
}