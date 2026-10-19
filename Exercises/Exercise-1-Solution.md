# Exercise 1: Hello Pod — Kubernetes

## Objective
Deploy an Nginx web server as a Kubernetes Pod using Minikube and access it through a NodePort Service.

## Tools Used
- Docker Desktop
- Minikube
- kubectl
- Kubernetes
- Nginx

## Procedure

### 1. Start the Kubernetes cluster
```bash
minikube start --driver=docker
```

### 2. Create the Nginx Pod
```bash
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod
```bash
kubectl get pods
```

**Observed result:** The `hello-k8s` Pod reached `Running` status, with `1/1` containers ready and zero restarts.

### 4. Expose the Pod as a Service
```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Verify the Service
```bash
kubectl get services
```

**Observed result:** The `hello-k8s` service was created with type `NodePort` and port `80`.

### 6. Access the application
```bash
minikube service hello-k8s
```

**Observed result:** The Nginx welcome page opened successfully in the browser.

## Conclusion
Successfully deployed an Nginx Pod on a local Kubernetes cluster using Minikube and exposed it through a NodePort Service. The application was accessible through the browser.

## Evidence
- Screenshot of the Nginx welcome page.
- Screenshot of the Pod status from `kubectl get pods`.
- Screenshot of the Service from `kubectl get services`.