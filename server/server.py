from flask import Flask ,request ,jsonify
from flask_cors import CORS
import util

app=Flask(__name__)
CORS(app)
# @app.route('/heloo')
# def heloo():
#     return "3*4"



@app.route('/predict_stress_level',methods=['GET','POST'])
def predict_stress_level():
    try:
        humidity=float(request.form['humidity'])
        temperature=float(request.form['temperature'])
        step_count=int(request.form['step_count'])
    
    except KeyError as e:
        return jsonify({"error": f"Missing parameter: {e.args[0]}"}), 400
    except ValueError as e:
        return jsonify({"error": "Invalid parameter type"}), 400
    
    estimated_stress_level = util.get_stressLevel(humidity,temperature,step_count)
    estimated_stress_level = int(estimated_stress_level)
    
    response=jsonify(
        {
            'estimated_stress_level': estimated_stress_level
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__=="__main__":
    print("Starting Python Flask Server")
    util.load_saved_artifacts()
    app.run(debug=True)