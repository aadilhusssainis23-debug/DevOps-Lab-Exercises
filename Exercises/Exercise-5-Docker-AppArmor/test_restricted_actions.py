
import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor:latest",
    detach=True,
    name="flask-apparmor-restricted-test"
)

try:
    print("Container started:", container.short_id)

    # Demonstrate an attempt to read /etc/passwd.
    exit_code, output = container.exec_run(
        ["cat", "/etc/passwd"]
    )
    print("Read /etc/passwd exit code:", exit_code)
    print(output.decode(errors="replace"))

    # Demonstrate an attempt to execute /bin/bash.
    exit_code, output = container.exec_run(
        ["/bin/bash", "-c", "echo bash-executed"]
    )
    print("Execute /bin/bash exit code:", exit_code)
    print(output.decode(errors="replace"))

    print(
        "Note: These actions are not guaranteed to be blocked. "
        "AppArmor enforcement was not verified on this Docker environment."
    )
finally:
    container.stop()
    container.remove()
    print("Container stopped and removed.")
