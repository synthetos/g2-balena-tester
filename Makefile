local:
	echo "Pushing to local"
	balena push d98b35e.local

ssh:
	balena ssh 192.168.1.92

build:
	echo "Pushing to remote"
	balena push g2-tester
