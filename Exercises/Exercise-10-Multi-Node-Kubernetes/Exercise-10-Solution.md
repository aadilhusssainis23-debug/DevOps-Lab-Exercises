# Exercise 10: Multi-Node Kubernetes Deployment

## Objective
Deploy Product Catalog (AppA) and Shopping Cart (AppB) on a three-node Minikube cluster, expose them through Kubernetes services, and distribute replicas using pod anti-affinity.

## Cluster Setup
- Minikube profile: devops-multinode
- Number of nodes: 3
- Kubernetes context: devops-multinode

## Product Catalog (AppA)
- Deployment: product-catalog
- Desired replicas: 2
- Image: product-catalog:latest
- Endpoint: GET /products
- Result: Successfully returned Laptop (1200), Phone (800), and Headphones (150).

## Shopping Cart (AppB)
- Deployment: shopping-cart
- Desired replicas: 3
- Image: shopping-cart:v2
- Endpoints: GET /cart and POST /cart
- Result: GET returned an empty cart initially. POST successfully added a Laptop item.

## Scheduling
Both deployments use required pod anti-affinity with topology key kubernetes.io/hostname to spread replicas across nodes.

The Shopping Cart rolling-update strategy was set to maxSurge: 0 and maxUnavailable: 1 to allow updates with strict pod anti-affinity.

## Services and Testing
Services:
- product-catalog-service
- shopping-cart-service

Local testing used kubectl port-forward:
- Product Catalog: localhost:8081
- Shopping Cart: localhost:8082

Commands tested:
- curl http://127.0.0.1:8081/products
- curl http://127.0.0.1:8082/cart
- POST request adding a Laptop to the Shopping Cart

All three tests returned successful responses.

## Replica Distribution
Shopping Cart: three running replicas, one each on devops-multinode, devops-multinode-m02, and devops-multinode-m03.

Product Catalog: two running replicas verified on separate nodes.

## Conclusion
Both applications were deployed and tested successfully on the three-node Minikube cluster. Services provided access to the application endpoints, and pod anti-affinity distributed replicas across nodes.

Note: Shopping Cart data is stored in memory and is not shared between replicas or persisted across pod restarts.
