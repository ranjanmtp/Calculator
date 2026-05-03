from flask import Flask, render_template, request, jsonify
import ast, operator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def safe_eval(node):
    if isinstance(node, ast.BinOp):
        return ops[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.Constant):   # 🔥 fix
        return node.value
    else:
        raise Exception("Invalid")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expr = data["expression"]

    try:
        node = ast.parse(expr, mode='eval').body
        result = safe_eval(node)
        return jsonify({"result": result})
    except:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run()