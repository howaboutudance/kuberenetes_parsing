build:
	eval $(minikube docker-env)
	docker build ./ -f=docker/header_metadata_parser/Dockerfile -t hematite/scalaprint
