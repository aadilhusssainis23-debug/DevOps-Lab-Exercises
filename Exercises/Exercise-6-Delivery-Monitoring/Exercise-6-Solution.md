# Exercise 6: Grafana Real-Time Monitoring of Quick-Commerce App

## Objective
To monitor delivery-service metrics using Python, Prometheus, and Grafana, configure alert rules, and use Jenkins to check service health.

## Implementation

### 1. Python Delivery Metrics
Created `delivery_metrics.py` using the Prometheus Python client. The application exposes metrics on port 8000:
- `total_deliveries`
- `pending_deliveries`
- `on_the_way_deliveries`
- `average_delivery_time`

### 2. Prometheus
Configured `prometheus.yml` to scrape the Python delivery service and Prometheus itself. Verified that both targets were UP.

### 3. Alert Rules
Created `alert_rules.yml` with two alerts:
- **HighPendingDeliveries:** triggers when pending deliveries exceed 10 for 15 seconds.
- **HighAverageDeliveryTime:** triggers when average delivery time exceeds 30 seconds for 15 seconds.

Verified that Prometheus loaded the alert rules.

### 4. Grafana Dashboard
Created a dashboard named **ZAPPTTO Delivery Monitoring** with Stat panels displaying total deliveries, pending deliveries, deliveries on the way, and average delivery time.

### 5. Jenkins Pipeline
Created `Delivery-Monitoring-Pipeline` in the Jenkins UI. The pipeline checks the availability of the Python metrics endpoint, Prometheus, and Grafana.

## Platform Note
The lab was implemented on macOS using Docker Desktop. Docker networking uses `host.docker.internal` to reach the Python service from containers. The Jenkins pipeline performs health checks; it does not build or deploy Docker images.

## Result
The Python metrics endpoint, Prometheus scraping, alert rules, Grafana dashboard, and Jenkins health checks were configured and tested. Prometheus targets were UP, and the alert rules were evaluated.
