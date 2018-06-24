#! /usr/bin/python
# Example App
# @author ksdme
import pytextbelt, sys

# Usage:
# 	./cli-sms.py <Phone> <Message>

def main():
  # command line arguments.
	phone, message = sys.argv[1:]

	recepient = pytextbelt.Textbelt.Recipient(phone)
	print "Sent Successfully!" if recepient.send(message)["success"] else "Sending Failed!"


if __name__ == "__main__":
  main()
