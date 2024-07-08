# Secret management

## Start listening to service

```sh
kubectl port-forward -n sealed service/login-service 5000:80
```


## test the login username password
```sh
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "<username>", "password": "<password>"}'
```


## folder structure

``` sh
my-repo/
│
├── kustomize/
│   ├── kustomization.yaml
│   ├── helm-chart/
│   │   └── my-app/
│   │       └── Chart.yaml
│   │       └── values.yaml
│   │       └── templates/
│   │           └── ...
│   └── sealed-secrets/
│       └── my-secret.yaml
```