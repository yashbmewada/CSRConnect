from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/allngos')
def get_all_ngos():
    ngos = [{
"id": 1,
"name": "NGO1",
"Description": "",
"Score": 76.7,
"No_of_Donation_Year_per_yr": 12,
"cost_per_dollar_spent": 0.7,
"donar_retention_rate": 0.2,
"optout_rate":4,
"new_projects":3,
"extension_rate":4,
"company_connected":[1,2],
"donation_money":5000,
"donation_resources":[{"type":"laptops","amount":456}],
"category":["No Poverty","Zero Hunger","Quality Education","Gender Equality","Water & Sanitation",
    "Affordable & Clean energy","Climate Action","Wildlife & Oceanlife"]
}]

    return jsonify(ngos)



if __name__ == '__main__':
    app.run()


