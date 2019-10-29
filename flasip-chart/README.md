# flasip Chart

A Helm chart for the flasip-app

## Installing the Chart

To install the chart:

```sh
helm install --name flasip-app .
```

> If you are in the flasip-chart DIR use `.`, otherwise provide chart DIR.

## Chart status

After installation succeeds, you can get a status of Chart

```sh
helm status flasip-app
```

## Application URL

To get the application url on Minikube, execute:

### Get service name

```sh
minikube service list

|----------------------|---------------------------|-----------------------------|-----|
|      NAMESPACE       |           NAME            |         TARGET PORT         | URL |
|----------------------|---------------------------|-----------------------------|-----|
| default              | flasip-flasip-chart       | http://192.168.39.151:30000 |
...
```

### Get the application url

```sh
minikube service flasip-flasip-chart --url
http://192.168.39.151:30000
```

## Deleting the Chart

If you want to delete your Chart, use this command:

```sh
helm delete --purge flasip-app
```
