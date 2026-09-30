from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"name":"SentrixDigital AU","market":"AU","repo":"dghx23/sentrixdigital-au","domain":"sentrixdigital.com.au","status":"Canonical public site"},
    {"name":"AU Compass","market":"AU","repo":"dghx23/aucompass","domain":"compass.sentrixdigital.com.au","status":"Canonical"},
    {"name":"ClaimThread","market":"AU","repo":"dghx23/claimthread","domain":"Railway preview","status":"Standalone"},
    {"name":"RentReady VIC","market":"AU","repo":"dghx23/rentreadyvic","domain":"rentready.com.au","status":"Standalone repo"},
    {"name":"RiskAtlas","market":"ZA","repo":"dghx23/riskatlas","domain":"riskatlas.co.za","status":"Domain still on legacy SentrixDigital service"},
    {"name":"ClinicalAtlas ZA","market":"ZA","repo":"dghx23/clinicalatlas-za","domain":"clinical.riskatlas.co.za","status":"Dedicated repo exists; domain migration pending"},
    {"name":"SchemeBook","market":"ZA","repo":"dghx23/schemebook","domain":"schemebook.riskatlas.co.za","status":"Dedicated repo exists; domain migration pending"},
    {"name":"Compass ZA","market":"ZA","repo":"dghx23/compass-za","domain":"compass.riskatlas.co.za","status":"Dedicated repo exists; domain migration pending"},
    {"name":"Demand Desk","market":"ZA","repo":"dghx23/demand-desk","domain":"demand.riskatlas.co.za","status":"Standalone repo ready; domain migration pending"},
    {"name":"RiskAtlas Tools","market":"ZA","repo":"dghx23/riskatlas-tools","domain":"tools.riskatlas.co.za","status":"Dedicated repo exists; domain migration pending"},
    {"name":"ClaimHub / ClaimBuddy","market":"ZA","repo":"dghx23/claimhubmain","domain":"claimhub.co.za / buddy.claimhub.co.za","status":"New canonical rebuild"},
]

@app.get("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.get("/health")
def health():
    return {"status":"ok","service":"portfolio-control-room"}
