# flasip

[![Docker Repository on Quay](https://quay.io/repository/thoba/flasip/status "Docker Repository on Quay")](https://quay.io/repository/thoba/flasip)
[![](https://images.microbadger.com/badges/version/thoba/flasip.svg)](http://microbadger.com/images/thoba/flasip "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/thoba/flasip.svg)](https://microbadger.com/images/thoba/flasip "Get your own image badge on microbadger.com")

[![flasip](http://dockeri.co/image/thoba/flasip)](https://hub.docker.com/r/thoba/flasip/)

## Running locally

1.  Download the [Google App Engine Python SDK](https://cloud.google.com/appengine/downloads) for your platform.

2.  Many samples require extra libraries to be installed. If there is a `requirements.txt`, you will need to install the dependencies with [`pip`](pip.readthedocs.org).

        pip install -t lib -r requirements.txt

3.  Use `dev_appserver.py` to run the sample:

        dev_appserver.py app.yaml

4.  Visit `http://localhost:8080` to view your application.

Some samples may require additional setup. Refer to individual sample READMEs.

## Deploying to GAE

1.  Download the [Google App Engine Python SDK](https://cloud.google.com/appengine/downloads) for your platform.
2.  Many samples require extra libraries to be installed. If there is a `requirements.txt`, you will need to install the dependencies with [`pip`](pip.readthedocs.org).

        pip install -t lib -r requirements.txt

3.  Use `gcloud` to deploy the sample, you will need to specify your Project ID and a version number:

        gcloud app deploy --project your-app-id -v your-version

4.  Visit `https://your-app-id.appost.com` to view your application.

## Additional resources

For more information on App Engine:

> https://cloud.google.com/appengine

For more information on Python on App Engine:

> https://cloud.google.com/appengine/docs/python

![FlasIp](https://raw.githubusercontent.com/thobalose/flasip/master/flasip_app.png)
