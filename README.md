# flasip

[![Docker Repository on Quay](https://quay.io/repository/thoba/flasip/status "Docker Repository on Quay")](https://quay.io/repository/thoba/flasip)
[![](https://images.microbadger.com/badges/version/thoba/flasip.svg)](http://microbadger.com/images/thoba/flasip "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/thoba/flasip.svg)](https://microbadger.com/images/thoba/flasip "Get your own image badge on microbadger.com")

[![flasip](http://dockeri.co/image/thoba/flasip)](https://hub.docker.com/r/thoba/flasip/)

![FlasIp](https://raw.githubusercontent.com/thobalose/flasip/master/flasip_app.png)

## Up and Running

Prerequisites

- [docker](https://docs.docker.com/)

### Build and run

To build a docker image for the flasip app and run it inside a container execute

```sh
docker build -t thoba/flasip .
```

The above with create an image with the `latest` tag. To run the container execute

```sh
docker run -it -p 5000:5000 thoba/flasip
```

Visit http://localhost:5000 in your browser.
