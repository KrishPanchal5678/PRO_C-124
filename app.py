from flask import Flask, jsonify, request 

app = Flask(__name__)

contacts = [
 {
    "ID" : 1 ,
    "Name" : "Steve" ,
    "Contact" : "1259874569" ,
    "Done" : False
 },

 {
    "ID" : 2 ,
    "Name" : "Alex" ,
    "Contact" : "1259878569" ,
    "Done" : False
 },

 {
    "ID" : 3 ,
    "Name" : "Herobrine" ,
    "Contact" : "1259074569" ,
    "Done" : False
 }

]

@app.route("/") 

def hello_world(): 
    return "Hello World!"

@app.route("/add-data", methods=["POST"]) 

def add_contact(): 
    if not request.json: 
        return jsonify({ "status":"error", "message": "Please provide the data!" },400) 

    else:
        contact = { 
            'ID': contacts[-1]['ID'] + 1 , 
            'Name': request.json['Name'] , 
            'Contact': request.json.get('Contact', "") , 
            'Done': False 
            } 

        contacts.append(contact) 

        return jsonify({ "status":"success", "message": "Contact registered succesfully!" })

@app.route("/get-data") 

def get_contact(): 
    return jsonify({ "data" : contacts }) 
   
if (__name__ == "__main__"): 
    app.run(debug=True)