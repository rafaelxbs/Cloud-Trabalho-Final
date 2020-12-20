output "arn_sqs_principal" {
  value = "${aws_sqs_queue.terraform_main_queue.arn}"
}

output "arn_sqs" {
  value = "${aws_sqs_queue.terraform_queue.arn}"
}

output "arn_dlq_principal" {
  value = "${aws_sqs_queue.terraform_queue_deadletter.arn}"
}

output "arn_sns" {
  value = "${aws_sns_topic.user_updates.arn}"
}

output "url_sqs_principal" {
  value = "${aws_sqs_queue.terraform_main_queue.id}"
}

