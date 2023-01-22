from flask import Flask,jsonify,request
app=Flask(__name__)
data=[
    {
        "contact":"9987644456",
        "name":"Raju",
        "done":"false",
        "id":1
    

    },

    {
        "contact":"9876543222",
        "name":"Rajul ",
        "done":False,
        "id":2
    

    },
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        },400)
    task={
        "id":data[-1]["id"]+1,
        "title":request.json['name'],
        "contact":request.json.get('contact',""),
        "done":False
       
        }
    data.append(task)
    return jsonify({
            "status":"success",
            "message":"name added successfully "
        })

@app.route("/get-data")
def get_task():
    return jsonify(
        {
            "data":data

        }
    )
if __name__=="__main__":
    app.run(debug=True)