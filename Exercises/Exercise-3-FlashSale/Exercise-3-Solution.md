# Exercise 3: Scaling Flask App Using Kubernetes ReplicaSets

## Objective
To deploy a Flask-based Flash Sale application on Kubernetes, scale its replicas, and observe automatic pod replacement.

## Application Endpoints
- `/` — Displays the Big Sale welcome message and the pod hostname.
- `/buy?user=123` — Simulates a purchase and returns the selected product, user, and serving pod.
- `/health` — Returns the health status of the application.

## Implementation
1. Created a Flask application in `app.py`.
2. Created a Dockerfile using Python 3.11, Flask, and Gunicorn.
3. Built the Docker image `flashsale:1.0`.
4. Loaded the image into Minikube.
5. Created a Kubernetes ReplicaSet and Service in `flashsale-replicaset.yaml`.
6. Deployed three replicas and verified that all three pods were running.
7. Scaled the ReplicaSet from three to five replicas.
8. Deleted one pod and verified that Kubernetes created a replacement automatically.

## Results

| Test | Observed result |
|---|---|
| Initial deployment | 3 ready replicas |
| Scaling | 5 ready replicas |
| Pod deletion | Replacement pod created |
| Final state | 5 desired, 5 current, 5 ready |
| Application test | Homepage returned the welcome message and pod hostname |

## Conclusion
The exercise demonstrated Kubernetes ReplicaSets, horizontal scaling, health probes, and self-healing. The ReplicaSet maintained five running pods after one pod was deleted, and the Flask application responded successfully through the Kubernetes Service.
