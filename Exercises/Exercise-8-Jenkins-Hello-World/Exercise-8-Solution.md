# Exercise 8: Creating a Hello World Jenkins Job

## Objective
To create a simple shell script, store it in GitHub, and execute it through a Jenkins Freestyle project.

## 1. GitHub Repository
Created a public repository named `devops-sample-code` and uploaded `hello-world.sh`.

Repository: https://github.com/aadilhusssainis23-debug/devops-sample-code

## 2. Shell Script
Created `hello-world.sh` with the following content:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

Made the script executable and verified it locally.

## 3. Jenkins Configuration
Created a Freestyle project named `HelloWorld`.

- **Source Code Management:** Git
- **Repository URL:** `https://github.com/aadilhusssainis23-debug/devops-sample-code.git`
- **Branch:** `*/main`
- **Build step:** Execute shell
- **Command:** `sh hello-world.sh`

## 4. Execution Result
Jenkins successfully cloned the repository and executed the shell script.

Expected console output:

```text
Hello, Jenkins!
Finished: SUCCESS
```

## Conclusion
The Hello World Jenkins job was configured and executed successfully. This exercise demonstrated how Jenkins retrieves code from GitHub and runs a shell script through a Freestyle project.

## Note
The job was triggered manually using **Build Now**. Automatic triggering on GitHub pushes was not configured as part of this completed test.
