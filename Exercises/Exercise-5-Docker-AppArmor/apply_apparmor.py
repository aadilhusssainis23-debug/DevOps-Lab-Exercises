
import docker

client = docker.from_env()

print("Building Docker image...")
image, logs = client.images.build(
    path=".",
    tag="flask-apparmor:latest"
)
print("Image built:", image.tags)

print("Starting test container...")
container = client.containers.run(
    "flask-apparmor:latest",
    ports={"5000/tcp": 5002},
    detach=True,
    name="flask-apparmor-sdk-test"
)

print("Container started:", container.short_id)

info = client.api.inspect_container(container.id)
print("Configured security options:", info["HostConfig"]["SecurityOpt"])

container.stop()
container.remove()
print("Container stopped and removed.")

print(
    "Note: AppArmor enforcement was not verified. "
    "The current Docker environment does not list AppArmor support."
)
