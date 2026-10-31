# Agile Accounts Management Platform

A learning project demonstrating Agile planning, a Flask REST API, GitHub Actions CI, Docker packaging, Kubernetes manifests, and a Tekton pipeline template.

## Run locally on Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
pytest -q
python app.py
```

Open `http://127.0.0.1:5000`.

## REST API examples

Create:
```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/accounts -ContentType "application/json" -Body '{"name":"Ada Lovelace","email":"ada@example.com"}'
```

List:
```powershell
Invoke-RestMethod http://127.0.0.1:5000/accounts
```

Read:
```powershell
Invoke-RestMethod http://127.0.0.1:5000/accounts/1
```

Update:
```powershell
Invoke-RestMethod -Method Put -Uri http://127.0.0.1:5000/accounts/1 -ContentType "application/json" -Body '{"name":"Ada Byron"}'
```

Delete:
```powershell
Invoke-WebRequest -Method Delete http://127.0.0.1:5000/accounts/1
```

The starter stores accounts in memory, so data resets when the server restarts. It is intended for a course lab, not production use.

## Docker

```powershell
docker build -t accounts-api:local .
docker run --rm -p 5000:5000 accounts-api:local
```

## Kubernetes

Build the image in the same runtime used by your local cluster, then:
```powershell
kubectl apply -f k8s/deployment.yaml
kubectl get deployments,pods,services
kubectl port-forward service/accounts-api 5000:5000
```

For Minikube, if Docker uses a different image store, run `minikube image load accounts-api:local` after building.

## GitHub Actions

The workflow is `.github/workflows/ci-build.yaml`. Push the repository to GitHub and check the Actions tab for a real run. Add the workflow badge only after the workflow is available.

## Tekton

`tekton/pipeline.yaml` is a starting template. Replace the repository placeholder, ensure your cluster supports the Tekton Hub resolver and catalog task version, then install/apply and run it in your cluster. Tekton resources and cluster setup vary by environment; do not claim a pipeline succeeded until you have run it and saved the actual logs.

## Agile planning starter

Create a GitHub Project with columns: Product Backlog, Sprint Backlog, In Progress, Review, Done. Add issues from the story template and apply labels such as `user-story`, `bug`, `technical-debt`, `priority:high`, `priority:medium`, and `priority:low`.

Suggested user stories:
1. As an account manager, I want to create an account so that new customers can be recorded.
2. As an account manager, I want to view one account so that I can verify its details.
3. As an account manager, I want to list accounts so that I can review all records.
4. As an account manager, I want to update account details so that records remain accurate.
5. As an account manager, I want to delete an account so that obsolete records can be removed.
6. As a developer, I want automated tests to run on every push so that regressions are caught early.
7. As an operator, I want a container image so that the service runs consistently.
8. As an operator, I want Kubernetes health probes so that unhealthy containers can be detected.

## Evidence checklist

Capture genuine screenshots from your own account and runtime:
- Module 1 repository, story template, stories, backlog, labels, Kanban board
- Module 2 setup, technical debt, and successful API create/read/list/update/delete requests
- Module 3 Sprint 2 plan, successful Actions run, badge, CI Kanban, security checks
- Module 4 Sprint 3 plan, app output, Docker image, Dockerfile URL, deployment and Kubernetes output
- Module 5 CD Kanban and complete Tekton pipeline run log (`pipelinerun.txt`)
