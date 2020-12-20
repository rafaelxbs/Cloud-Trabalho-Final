resource "aws_s3_bucket" "b" {
  bucket = "trabalho-final-aoj75-339035"
  acl    = "private"

  tags = {
    Name        = "trabalho-final-aoj75-339035"
    Environment = "admin"
  }
}