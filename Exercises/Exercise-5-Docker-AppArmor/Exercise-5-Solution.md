# Exercise 5: Docker Security with AppArmor and Python

## Objective
To containerize a Flask application, use the Docker SDK for Python, inspect container security options, and test restricted actions.

## Implementation
1. Created a Flask application that listens on port 5000.
2. Created a Dockerfile and built the image `flask-apparmor:latest`.
3. Ran the Flask container and tested its availability.
4. Installed and used the Docker SDK for Python.
5. Created `apply_apparmor.py` to build the image, start a container, inspect its security options, and stop and remove the container.
6. Created `test_restricted_actions.py` to test reading `/etc/passwd` and executing `/bin/bash`.

## Results

| Test | Observed result |
|---|---|
| Docker image build | Successful |
| Flask container | Started successfully |
| Docker SDK script | Ran successfully |
| Security option inspection | No explicit security options configured |
| Read `/etc/passwd` | Exit code 0; file was readable |
| Execute `/bin/bash` | Exit code 0; command executed |
| Test container cleanup | Successful |

## AppArmor Limitation
The lab was performed on macOS using Docker Desktop. Docker reported `seccomp` and `cgroupns` in its security options, but did not list AppArmor support. Therefore, an AppArmor profile could not be verified as loaded or enforced in this environment.

The restricted-action tests were executed without verified AppArmor enforcement. The successful file read and shell execution do not demonstrate AppArmor restrictions.

To complete actual AppArmor enforcement testing, the profile must be loaded and applied on a compatible Linux environment with AppArmor enabled.

## Questions and Answers

**1. What is the purpose of using AppArmor with Docker containers?**

AppArmor applies security policies that confine applications and limit their access to files, resources, and other system features.

**2. How do AppArmor profiles help secure a Docker container?**

Profiles define which operations an application is allowed or denied, providing an additional layer of access control.

**3. Why restrict access to `/etc/` and `/var/`?**

These directories contain system configuration and other important files. Restricting access can reduce unauthorized reading or modification.

**4. What other capabilities can be restricted using AppArmor?**

AppArmor can restrict file access, binary execution, network operations, and other application behaviors according to the profile.

**5. How can you verify whether an AppArmor profile is applied?**

Inspect the container's security options using Docker or the Docker SDK, and verify enforcement using appropriate Linux AppArmor tools. Configuration inspection alone does not prove that a policy is enforcing the intended restrictions.

## Conclusion
The Flask image, Docker SDK workflow, and restricted-action test script were implemented successfully. The tests showed that file reading and shell execution remained possible in the current environment. Actual AppArmor enforcement remains unverified because the macOS Docker Desktop environment did not report AppArmor support.
