FROM adoptopenjdk:13-jre-hotspot


WORKDIR app
COPY  ./target/scala-2.13/kube_play-assembly-0.1.jar ./kube_play.jar

ENTRYPOINT java -jar kube_play.jar
