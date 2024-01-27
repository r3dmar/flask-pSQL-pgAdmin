# Demo project

**Requirements**

- Flask [app](./dockerfile/flask-app.py) with 2 endpoints wrapped in Helm Chart.
- [PostgreSQL](https://artifacthub.io/packages/helm/bitnami/postgresql) deployed via Helm Chart
- [PgAdmin](https://artifacthub.io/packages/helm/runix/pgadmin4), also deployed by Helm Chart, acts as an interface.
- Also implemented a Github CI that sends images to ghcr.
- All deployment is implemented using [Helmfile.](https://medium.com/geekculture/helmfile-introduction-f63c42244dcc)

**Before Deploy:**

- Install Helmfile on you machine. [Reference](https://helmfile.readthedocs.io/en/latest/#installation)

- Create namespaces
```
kubectl create ns monitoring cert-manager nginx-ingress
```
- Deploy Kubernetes Secret with wildcard cert for your URL's and change Ingresses in flask-app & pgaadmin4 Helm Charts

- If needed, make changes in [publish-ghcr.yaml](./.github/workflows/publish-ghcr.yaml)

- Than go to Project repo main folder and run following command: 
```
helmfile sync
```
 
**After Deploy**

- Check status of all components: 
```
kubectl get pod --all-namespaces
```

- Go to PgAdmin Control plane

```
login: chart@domain.com
pass:  SuperSecret
```
- Connect to our pSQL DB. 

```
DB name: flaskdb
DB pass: flask0375
```

- Than go back to Terminal window and create User and Pass for Flask App:
```
htpasswd -c auth USERNAME-HERE

kubectl create secret generic basic-auth --from-file=auth
```
***We suggest making Kubernetes secret so as not to forget the password for the new user.***



- Than go back to Terminal window and try Endpoints: 

```
add random data:

curl -XPOST -u USERNAME-HERE:PASS-HERE https://flask-app.demoapps.win/add_random_data

delete random data:

curl -XDELETE -u USERNAME-HERE:PASS-HERE https://flask-app.demoapps.win/delete_all_data
```

- The last thing, check in PgAdmin changes in our DB. 


That's all. 