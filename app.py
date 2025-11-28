from flask import Flask, request ,render_template , url_for
import joblib
model = joblib.load('model.pkl')
print("hello hii ")

app =Flask(__name__)

# @app.route('/')
# def home():
#     return "hello this is my insurance claim charges webpage "
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/project',methods= ['POST',"GET"])
def predict():
    if request.method=='POST':
        age = int(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']
        dt1 = {
    "male":0,
    "female":1
}
        sex = dt1[sex]
        dt2 = {
    "yes":0,
    "no":1
}
        smoker = dt2[smoker]
        dt3 = {
    'southwest':0, 
    'southeast':1,
    'northwest':2, 
    'northeast':3
}
        region = dt3[region]
        lst = [[age, sex , bmi, children, smoker, region]]
        print("output", lst)
        pred = model.predict(lst)
        print("generated ans",pred)

        return render_template('project.html', prediction=round(pred[0], 2))



        
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)

