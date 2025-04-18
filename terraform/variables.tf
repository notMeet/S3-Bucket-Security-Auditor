variable "aws_region" {
  default = "us-east-1"
}

variable "image_url" {
  description = "The ECR image URL"
  type        = string
}

variable "app_name" {
  default = "cloudguard"
}
