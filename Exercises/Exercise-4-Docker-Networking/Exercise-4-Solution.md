# Exercise 4: Docker Networking with Multiple Containers

## Objective
To understand Docker bridge networking and configure a multi-container application containing Flask, MySQL, and Redis.

## Implementation
1. Created a custom bridge network named `my-bridge-net`.
2. Created a Flask REST API using Python and Flask.
3. Built the Docker image `flask-api:latest`.
4. Started the MySQL container using `mysql:8`.
5. Started the Redis container using `redis:latest`.
6. Started the Flask container and mapped host port 5001 to container port 5001.
7. Tested the Flask API using the `/about` endpoint.
8. Inspected the bridge network to verify that all three containers were connected.

## Results

| Component | Result |
|---|---|
| Docker network | `my-bridge-net` created |
| Flask API | Returned the expected JSON response |
| MySQL container | Connected to the bridge network |
| Redis container | Connected to the bridge network |
| Flask container | Connected to the bridge network |
| Network inspection | All three containers listed |

## Questions and Answers

**1. What is the purpose of the `--net` flag in `docker run`?**

It specifies which Docker network the container should join.

**2. How do containers communicate on the same network?**

They can communicate using container names or IP addresses, provided the relevant service is listening and network access is allowed.

**3. What is the difference between bridge and host networking?**

A bridge network gives containers an isolated network. Host networking shares the host's network stack.

**4. How can you expose a container's port to the host machine?**

Use the `-p` option, such as `-p 5001:5001`.

## Conclusion
The Flask API worked successfully, and Docker network inspection confirmed that Flask, MySQL, and Redis were attached to the same custom bridge network. This demonstrates Docker networking and container-name-based service discovery.
