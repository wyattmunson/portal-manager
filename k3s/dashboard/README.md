# Dashboard

- Run 01-...sh script to deploy dashboard
- Apply admin user
- Apply admin user role
-

```bash
sudo k3s kubectl create -f dashboard.admin-user.yml -f dashboard.admin-user-role.yml
```

Get bearer token

```bash
sudo k3s kubectl -n kubernetes-dashboard create token admin-user
```

Dashboard is now accessable at: `http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`

Sign in with admin user bearer token.

```bash
# script loaded
https://raw.githubusercontent.com/kubernetes/dashboard/v3.0.0-alpha0/aio/deploy/recommended.yaml
# correct format
https://raw.githubusercontent.com/kubernetes/dashboard/v3.0.0-alpha0/charts/kubernetes-dashboard.yaml
```
