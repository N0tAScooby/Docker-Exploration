# Docker-Exploration

Im Container läuft ein einfaches Python Skript, welches einfach eine Zeile in eine Textdatei einfügt.

## Dockerfile vs Image

Das Image wird an Hand des Dockerfiles gebaut. Das Dockerfile stellt somit das Rezept für ein gebautes Image dar. 

## Wie baue ich ein Image? 

```sh
docker build . -t demo_image
```

Der Progress Output des Builds wird ab der Verwendung von "Buildkit" anders dargestellt. 
Um die Zwischenschritte detaillierter mit Hashes anzuzeigen wird folgender Befehl benötigt:

```sh
docker build . --progress=plain -t demo_image
```

## Was ist ein Image? 
Ein Image ist eine Datei, welche ein Template für einen Container darstellt.
Das Image ist aus mehreren read-only Layers aufgebaut. Jedes Layer repräsentiert eine Anweisung aus dem Dockerfile, welches 
benutzt wurde um den Container zu bauen.

### Hilfreiche Analogien: 

Image ist Klasse -> Container ist Instanz der Klasse


### Layer anschauen: 

```sh
docker history demo_image
```

## Was ist ein Container? 

[Docker Doku](https://docs.docker.com/storage/storagedriver/#container-size-on-disk)

Wenn ein Image eine Klasse darstellt, dann ist ein Container die Instanz dieser Klasse.

### Wie passiert das genauer?

Um aus einem Image einen Container zu erstellen passiert unter anderem folgendes:

* read-write filesystem drauflegen ("Container Layer")
* network port, container name, id und ressourcen Limits festlegen

Hier liegt auch der Unterschied zu einem Image. Ein Container kann gestoppt werden oder exiten ohne dieses
read-write layer zu verlieren. Somit können zwischen starten und stoppen Daten persistiert werden. 

### Was zur Verwirrung führen kann hier, dass ein "docker run" jedes Mal einen neuen Container erstellt. Das ist also kein Stop / Start

### Docker Container stoppen: 

```sh
docker stop demo_image
```

### Docker Container wieder starten

```sh
docker start demo_image
```

## Was ist ein Volume? 

[Docker Doku](https://docs.docker.com/storage/volumes/)

Ein Volume ist ein Teil des Host Filesystems und wird von Docker gemanaged.

Nimmt man Docker Volumes statt dem Writable Layer eines Containers hat das diverse Vorteile:

* Einfache Backups
* Können zwischen Containern geteilt werden
* Erhöht nicht die Größe des Containers
* Ist persistent selbst, wenn der Docker Container entfernt wird

### Wieso möchte ich ein Volume länger als meinen Container behalten?

Hat man einen Container aus Image der Anwendung X mit Version 1.1 laufen und ersetzt ihn durch Container mit Image Version 1.2
kann dieser Container die Daten aus dem Volume sofort wieder verwenden. So können Container und Daten entkoppelt werden.

### Volume erstellen 

´´´sh
docker volume create new_volume
´´´

### Container mit gemountetem Volume starten

```sh
docker run -v new_volume:/demo demo_image
```

Bei öfterem ausführen kann man n Container ausführen, welche das File im Volume anpassen.

