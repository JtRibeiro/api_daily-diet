from flask import Flask, request, jsonify
from database import db
from model.diet import Diet

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

@app.route("/diet", methods=["POST"])
def create_diet():
    data = request.json

    name = data.get("name")
    description = data.get('description')
    is_active = data.get("is_active")
    try:
        diet = Diet(name=name, description=description, is_active=is_active)
        db.session.add(diet)
        db.session.commit()
        return jsonify(diet.to_dict()), 201
    except:
        return jsonify({"message": "Campo name é obrigatório!"}), 400

@app.route("/diet/<int:id_diet>", methods=['PUT'])
def update_diet(id_diet):
    data = request.json
    diet = Diet.query.get(id_diet)
    print(diet)

    if diet:
        if 'name' in data and data['name'] is not None:
            diet.name = data.get("name")

        if 'description' in data and data['description'] is not None:
            diet.description = data.get("description")
            
        diet.is_active = data.get("is_active")
        db.session.commit()

        return jsonify(diet.to_dict())

    return jsonify({"message": "Dieta não cadastrada no sistema!"}), 404

@app.route("/diet/<int:id_diet>", methods=['DELETE'])
def delet_diet(id_diet):
    diet = Diet.query.get(id_diet)
    print(f"Id da dieta: {diet}")

    if diet:
        db.session.delete(diet)
        db.session.commit()
        return jsonify({"message": f"A Dieta {id_diet} foi deletado com sucesso!" })
    
    return jsonify({"message": "Dieta para deleção não cadastrada no sistema!"}), 404

@app.route("/diet/<int:id_diet>", methods=["GET"])
def read_diet_by_id(id_diet):
    diet = Diet.query.get(id_diet)

    if diet:
        return jsonify(diet.to_dict())

    return jsonify({"message": "Dieta não cadastrada no sistema!"}), 404

@app.route("/diets", methods=['GET'])
def read_diets():
    diets = Diet.query.all()

    if len(diets) > 0:
        diet_list = [diet.to_dict() for diet in diets]

        output = {
            "diets": diet_list,
            "total_diet": len(diet_list)
        }

        return jsonify(output)

    return jsonify({"message": "Nenhuma dieta  cadastrada no sistema!"}), 404



if __name__ == "__main__":
    app.run(debug=True)

