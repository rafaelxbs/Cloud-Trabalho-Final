terraform {
  backend "s3" {
    bucket = "trabalho-final-aoj75-339035"
    key    = "trabalhofinal"
    region = "us-east-1"
  }
}