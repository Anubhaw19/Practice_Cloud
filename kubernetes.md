
## Kubernetes Commands
### Kubectl -CURD commands
- create   `deployment`
```bash
  kubectl create deployment <DEPLOYMENT-NAME> --image=<IMAGE-NAME>
  ex-
  kubectl create deployment nginx-depl --image=nginx
```
- create   `namespace`
```bash
  kubectl create namespace <NAMESPACE-NAME> 
  ex-
  kubectl create namespace my-namespace
```

- edit   `deployment`
```bash
  kubectl edit deployment <DEPLOYMENT-NAME> 
  ex-
  kubectl edit deployment nginx-depl 
```

- delete   `deployment`
```bash
  kubectl delete deployment <DEPLOYMENT-NAME> 
  ex-
  kubectl delete deployment nginx-depl 
```
### Status of different `K8s components`
- get all components that is inside the `Cluster`
```bash
  kubectl get all  
```
- get `nodes`
```bash
  kubectl get nodes  
```
- get `pod`
```bash
  kubectl get pod  
```
- get `pod` with more info (IP Address)
```bash
  kubectl get pod -o wide
```
- get `services`
```bash
  kubectl get services  
```
- get `replicaset`
```bash
  kubectl get replicaset  
```
- get `deployment`
```bash
  kubectl get deployment  
```
### Debugging pods

- log to `console`
```bash
  kubectl log <POD-NAME> 
```
- get  `Interactive Terminal`
```bash
  kubectl exec -it <POD-NAME> --bin/bash
```
- get info about `pod` (extra toubleshooting info)
```bash
  kubectl describe pod <POD-NAME>
```

### Use configuration file for CURD

- apply a `Configuration file`
```bash
  kubectl apply -f <FILE-NAME>
```
- apply a `Configuration file` inside a `namespace`
```bash
  kubectl apply -f <FILE-NAME> --namespace=<NAMESPACE-NAME>
```
- to get the `component` created inside a specific `namespace`
```bash
  kubectl get <COMPONENT_NAME> -n <NAMESPACE-NAME>
```
- delete with `Configuration file`
```bash
  kubectl delete -f <FILE-NAME>
```
- get status of the  `deployment`  stored in `etcd`
```bash
  kubectl get deployment <DEPLOYMENT-NAME> -o yaml
```
### Local setup `minikube`
- start `minikube` for single node cluster having both master and worker node for local setup
```bash
  minikube start
```
- Kubernetes Dashboard (for additional insight into cluster state)
```bash
  minikube dashboard
```
- assign `external service` a `public IP Address` (for local setup)
```bash
  minikube service <SERVICE-NAME>
```
- configure `ingress controller` (this will automatically starts the K8s Nginx implementation of Ingress Controller)
```bash
  minikube addons enable ingress
```
