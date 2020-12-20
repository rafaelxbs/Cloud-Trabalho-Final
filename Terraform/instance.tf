
resource "aws_sqs_queue" "terraform_queue_deadletter" {
  name = "DLQ-Principal-${terraform.workspace}"
  delay_seconds = 90
  max_message_size = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  /*tags = {
    Name = "DLQ-Principal-${terraform.workspace}"
  }*/
}

resource "aws_sqs_queue" "terraform_main_queue" {
  name                      = "SQS-Principal-${terraform.workspace}"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.terraform_queue_deadletter.arn
    maxReceiveCount     = 1
  })
  /*tags = {
    Name = "SQS-Principal-${terraform.workspace}"
  }*/
}

resource "aws_sns_topic" "user_updates" {
  /*tags = {
    Name = "SNS-${terraform.workspace}"
  }*/
  name = "SNS-${terraform.workspace}"
}

resource "aws_sqs_queue" "terraform_queue" {
  name = "SQS-2-${terraform.workspace}"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10

  /*tags = {
    Name = "SQS-2-${terraform.workspace}"
  }*/
}
