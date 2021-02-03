from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method =="GET"):
        return render_template("index.html")
    else:
        if(request.form["valor1"] != "" and request.form["valor2"] != ""):
            num1=request.form["valor1"]
            num2=request.form["valor2"]
            operacao=request.form["operacao"]
        # cálculos
            soma = int(num1) + int(num2)
            subt = int(num1) - int(num2)
            mult = int(num1) * int(num2)
            divi=int(num1) / int(num2)

            if(operacao == "soma"):    
               return str(soma)
            elif(operacao == "subt"):
               return str(subt)
            elif(operacao == "mult"):
               return str(mult)
            else:
                return str(divi)
        else:
            return "<h1>Favor, preencha todos os campos do formulario!<h1>"
    
# @app.route("/por padrão é string, convertendo para int <:id>")
# @app.route("/<int:id>")
# def Home_id(id):
#     return str (id) + 1

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")


# semelhante ao app.listen(porta)
app.run(port=8080, debug=True)


