from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)
accounts = {}
next_id = 1

PAGE = """
<!doctype html><html><head><meta charset="utf-8"><title>Accounts Management</title>
<style>body{font:16px Arial;margin:40px auto;max-width:900px;padding:0 20px;color:#172033}
h1{color:#175cd3}.card{padding:20px;border:1px solid #d0d5dd;border-radius:12px;margin:16px 0}
code{background:#f2f4f7;padding:3px 6px;border-radius:4px}</style></head><body>
<h1>Accounts Management API</h1><p>Sample application for Agile planning, REST API testing, CI/CD and container deployment.</p>
<div class="card"><h2>API endpoints</h2><ul>
<li><code>GET /health</code> — health check</li><li><code>POST /accounts</code> — create account</li>
<li><code>GET /accounts</code> — list accounts</li><li><code>GET /accounts/&lt;id&gt;</code> — read account</li>
<li><code>PUT /accounts/&lt;id&gt;</code> — update account</li><li><code>DELETE /accounts/&lt;id&gt;</code> — delete account</li></ul></div>
<div class="card"><h2>Try it</h2><p>Use curl, Postman, or the included tests to exercise the JSON API.</p>
<p>Example: <code>curl http://127.0.0.1:5000/accounts</code></p></div></body></html>
"""

@app.get("/")
def home():
    return render_template_string(PAGE)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.post("/accounts")
def create_account():
    global next_id
    data = request.get_json(silent=True) or {}
    if not data.get("name") or not data.get("email"):
        return jsonify(error="Both name and email are required"), 400
    account = {"id": next_id, "name": str(data["name"]), "email": str(data["email"])}
    accounts[next_id] = account
    next_id += 1
    return jsonify(account), 201

@app.get("/accounts")
def list_accounts():
    return jsonify(list(accounts.values())), 200

@app.get("/accounts/<int:account_id>")
def read_account(account_id):
    account = accounts.get(account_id)
    if account is None:
        return jsonify(error="Account not found"), 404
    return jsonify(account), 200

@app.put("/accounts/<int:account_id>")
def update_account(account_id):
    account = accounts.get(account_id)
    if account is None:
        return jsonify(error="Account not found"), 404
    data = request.get_json(silent=True) or {}
    if "name" in data:
        account["name"] = str(data["name"])
    if "email" in data:
        account["email"] = str(data["email"])
    return jsonify(account), 200

@app.delete("/accounts/<int:account_id>")
def delete_account(account_id):
    if accounts.pop(account_id, None) is None:
        return jsonify(error="Account not found"), 404
    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
