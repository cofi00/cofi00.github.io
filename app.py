from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

rase_pasa = ["Bokser", "Labrador Retriver", "Nemački Ovčar", "Zlatni Retriver", "Buldog", "Pudla", "Beagle", "Rottweiler", "Njufaundlender", "Dalmatinac", "Doberman", "Čivava", "Samojed", "Ši Cu", "Haski", "Malamut", "Mops", "Jorkširski Terijer", "Border Koli", "Akita", "Baset", "Bernardinac", "Koker Španijel", "Dogo Argentino", "Engleski Mastif"]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trazenje')
def index():
    return render_template('index.html')

@app.route('/pretraga', methods=['GET'])
def pretraga():
    unos = request.args.get('q').lower()  
    rezultati = [rasa for rasa in rase_pasa if unos in rasa.lower()]
    return jsonify(rezultati)

@app.route('/dogs/Bokser') 
def bokser():
    return f"<h1>ovo je {rase_pasa[0]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"
    
@app.route('/dogs/Labrador Retriver')
def Labrador_Retriver():
    return f"<h1>ovo je {rase_pasa[1]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Nemački Ovčar')
def Nemački_Ovčar():
  
    return f"<h1>ovo je {rase_pasa[2]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Zlatni Retriver')
def Zlatni_Retriver():
   
    return f"<h1>ovo je {rase_pasa[3]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Buldog')
def Buldog():
    
    return f"<h1>ovo je {rase_pasa[4]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Pudla')
def Pudla():
   
    return f"<h1>ovo je {rase_pasa[5]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Beagle')
def Beagle():
   
    return f"<h1>ovo je {rase_pasa[6]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Rottweiler')
def Rottweiler():
    
    return f"<h1>ovo je {rase_pasa[7]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Njufaundlender')
def Njufaundlender():
    
    return f"<h1>ovo je {rase_pasa[8]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Dalmatinac')
def Dalmatinac():
  
    return f"<h1>ovo je {rase_pasa[9]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Doberman')
def Doberman():
    
    return f"<h1>ovo je {rase_pasa[10]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Čivava')
def Čivava():
    
    return f"<h1>ovo je {rase_pasa[11]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Samojed')
def Samojed():
   
    return f"<h1>ovo je {rase_pasa[12]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Ši Cu')
def Ši_Cu():
    
    return f"<h1>ovo je {rase_pasa[13]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Haski')
def Haski():
    
    return f"<h1>ovo je {rase_pasa[14]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Malamut')
def Malamut():
   
    return f"<h1>ovo je {rase_pasa[15]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Mops')
def Mops():
    
    return f"<h1>ovo je {rase_pasa[16]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Jorkširski Terijer')
def Jorkširski_Terijer():
    
    return f"<h1>ovo je {rase_pasa[17]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Border Koli')
def Border_Koli():
    
    return f"<h1>ovo je {rase_pasa[18]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Akita')
def Akita():
    
    return f"<h1>ovo je {rase_pasa[19]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Baset')
def Baset():
    
    return f"<h1>ovo je {rase_pasa[20]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Bernardinac')
def Bernardinac():
    
    return f"<h1>ovo je {rase_pasa[21]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Koker Španijel')
def Koker_Španijel():
   
    return f"<h1>ovo je {rase_pasa[22]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Dogo Argentino')
def Dogo_Argentino():
    
    return f"<h1>ovo je {rase_pasa[23]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Engleski Mastif')
def Engleski_Mastif():
    
    return f"<h1>ovo je {rase_pasa[24]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

if __name__ == '__main__':
    app.run(debug=False, host = "0.0.0.0")

