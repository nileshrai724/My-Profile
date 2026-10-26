# 8. Kubernetes web deployment

Example Nginx Deployment and ClusterIP Service. The manifest is declarative;
it does not deploy anything until you apply it to a Kubernetes cluster.

## Run

Requires a local Kubernetes cluster such as kind or minikube:

```bash
kubectl apply -f deployment.yaml
kubectl get deployments,pods,services
kubectl port-forward service/learning-web 8080:80
```

Visit `http://localhost:8080`. Clean up with
`kubectl delete -f deployment.yaml`.

## Try next

Add a ConfigMap for a custom page, a readiness probe, or resource requests
and limits that match your test environment.
