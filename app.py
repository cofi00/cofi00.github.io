from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

rase_pasa = ["Bokser", "Labrador Retriver", "Nemački Ovčar", "Zlatni Retriver", "Buldog", "Pudla", "Beagle", "Rottweiler", "Njufaundlender", "Dalmatinac", "Doberman", "Čivava", "Samojed", "Ši Cu", "Haski", "Malamut", "Mops", "Jorkširski Terijer", "Border Koli", "Akita", "Baset", "Bernardinac", "Koker Španijel", "Dogo Argentino", "Engleski Mastif"]
Istorija =[]

@app.route('/')
def home():
    return render_template('home.html',content = Istorija)

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
    if 'Bokser'not in Istorija:
        Istorija.append(rase_pasa[0])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[0]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"
    
@app.route('/dogs/Labrador Retriver')
def Labrador_Retriver():
    if 'Labrador Retriver'not in Istorija:
        Istorija.append(rase_pasa[1])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[1]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Nemački Ovčar')
def Nemački_Ovčar():
    if 'Nemački Ovčar'not in Istorija:
        Istorija.append(rase_pasa[2])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[2]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Zlatni Retriver')
def Zlatni_Retriver():
    if 'Zlatni Retriver'not in Istorija:
        Istorija.append(rase_pasa[3])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[3]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Buldog')
def Buldog():
    if 'Buldog'not in Istorija:
        Istorija.append(rase_pasa[4])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[4]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Pudla')
def Pudla():
    if 'Pudla'not in Istorija:
        Istorija.append(rase_pasa[5])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[5]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Beagle')
def Beagle():
    if 'Beagle'not in Istorija:
        Istorija.append(rase_pasa[6])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[6]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Rottweiler')
def Rottweiler():
    if 'Rottweiler'not in Istorija:
        Istorija.append(rase_pasa[7])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[7]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Njufaundlender')
def Njufaundlender():
    if 'Njufaundlender'not in Istorija:
        Istorija.append(rase_pasa[8])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[8]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Dalmatinac')
def Dalmatinac():
    if 'Dalmatinac'not in Istorija:
        Istorija.append(rase_pasa[9])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[9]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Doberman')
def Doberman():
    if 'Doberman'not in Istorija:
        Istorija.append(rase_pasa[10])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[10]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Čivava')
def Čivava():
    if 'Čivava'not in Istorija:
        Istorija.append(rase_pasa[11])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[11]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Samojed')
def Samojed():
    if 'Samojed'not in Istorija:
        Istorija.append(rase_pasa[12])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[12]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Ši Cu')
def Ši_Cu():
    if 'Ši Cu'not in Istorija:
        Istorija.append(rase_pasa[13])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[13]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Haski')
def Haski():
    if 'Haski'not in Istorija:
        Istorija.append(rase_pasa[14])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[14]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Malamut')
def Malamut():
    if 'Malamut'not in Istorija:
        Istorija.append(rase_pasa[15])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[15]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Mops')
def Mops():
    if 'Mops'not in Istorija:
        Istorija.append(rase_pasa[16])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[16]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Jorkširski Terijer')
def Jorkširski_Terijer():
    if 'Jorkširski Terijer'not in Istorija:
        Istorija.append(rase_pasa[17])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[17]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Border Koli')
def Border_Koli():
    if 'Border Koli'not in Istorija:
        Istorija.append(rase_pasa[18])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[18]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Akita')
def Akita():
    if 'Akita'not in Istorija:
        Istorija.append(rase_pasa[19])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[19]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Baset')
def Baset():
    if 'Baset'not in Istorija:
        Istorija.append(rase_pasa[20])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[20]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Bernardinac')
def Bernardinac():
    if 'Bernardinac'not in Istorija:
        Istorija.append(rase_pasa[21])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[21]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Koker Španijel')
def Koker_Španijel():
    if 'Koker Španijel'not in Istorija:
        Istorija.append(rase_pasa[22])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[22]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Dogo Argentino')
def Dogo_Argentino():
    if 'Dogo Argentino'not in Istorija:
        Istorija.append(rase_pasa[23])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[23]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

@app.route('/dogs/Engleski Mastif')
def Engleski_Mastif():
    if 'Engleski Mastif'not in Istorija:
        Istorija.append(rase_pasa[24])
        if len(Istorija) > 5:
            Istorija.pop(0)
    return f"<h1>ovo je {rase_pasa[24]}</h1><br><a href='/'><button>Nazad na početnu</button></a>"

if __name__ == '__main__':
    app.run(debug=False, host = "0.0.0.0")

