# Docker raw notes

## Different OS in containers

* Alpine
  * Url: https://alpinelinux.org/
  * Imagename: alpine
  * Shorty: It's very small.
  * Package manager: apk
  * Shells: /bin/sh
  * Size: Few MBs - current tag needs 2.7MB

* Jessie aka Debian 8
  * Url: https://wiki.debian.org/DebianJessie
  * Imagename: debian:jessie
  * Shorty: No LTS anymore
  * Package manager: apt
  * Shells: /bin/bash
  * Size: ~50MB

* Stretch aka Debian 9
  * Url: https://wiki.debian.org/DebianStretch
  * Imagename: Debian:Stretch
  * Shorty: LTS is running out
  * Package manager: apt
  * Shells: /bin/bash and many more
  * Size: ~40MB

* Buster aka Debian 10
  * Url: https://wiki.debian.org/DebianBuster
  * Imagename: debian:Buster
  * Shorty: All you need, but newer
  * Package manager: apt
  * Shells: /bin/bash and many more
  * Size: ~50MB

* Bullseye aka Debian 11
  * Url: https://wiki.debian.org/DebianBullseye
  * Imagename: Debian:Bullseye
  * Shorty: Newest Debian
  * Shells: /bin/bash and many more
  * Size: ~50MB

* Ubuntu based on Debian
  * Url: https://hub.docker.com/_/ubuntu
  * Imagename: ubuntu
  * Shorty: All you need
  * Package manager: apt
  * Shells: /bin/bash and more
  * Size: ~25MB

[source](https://stackoverflow.com/questions/52083380/in-docker-image-names-what-is-the-difference-between-alpine-jessie-stretch-an)

