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
    return render_template('Bokser.html')
    
@app.route('/dogs/Labrador Retriver')
def Labrador_Retriver():
    return render_template('Labrador Retriver.html')

@app.route('/dogs/Nemački Ovčar')
def Nemački_Ovčar():
    return render_template('Nemački Ovčar.html')

@app.route('/dogs/Zlatni Retriver')
def Zlatni_Retriver():
   
    return render_template('Zlatni Retriver.html')

@app.route('/dogs/Buldog')
def Buldog():
    
    return render_template('Buldog.html')

@app.route('/dogs/Pudla')
def Pudla():
   
    return render_template('Pudla.html')

@app.route('/dogs/Beagle')
def Beagle():
   
    return render_template('Beagle.html')

@app.route('/dogs/Rottweiler')
def Rottweiler():
    
    return render_template('Rottweiler.html')

@app.route('/dogs/Njufaundlender')
def Njufaundlender():
    
    return render_template('Njufaundlender.html')

@app.route('/dogs/Dalmatinac')
def Dalmatinac():
  
    return render_template('Dalmatinac.html')

@app.route('/dogs/Doberman')
def Doberman():
    
    return render_template('Doberman.html')

@app.route('/dogs/Čivava')
def Čivava():
    
    return render_template('Čivava.html')

@app.route('/dogs/Samojed')
def Samojed():
   
    return render_template('Samojed.html')

@app.route('/dogs/Ši Cu')
def Ši_Cu():
    
    return render_template('Ši Cu.html')

@app.route('/dogs/Haski')
def Haski():
    
    return render_template('Haski.html')

@app.route('/dogs/Malamut')
def Malamut():
   
    return render_template('Malamut.html')

@app.route('/dogs/Mops')
def Mops():
    
    return render_template('Mops.html')

@app.route('/dogs/Jorkširski Terijer')
def Jorkširski_Terijer():
    
    return render_template('Jorkširski Terije.html')

@app.route('/dogs/Border Koli')
def Border_Koli():
    
    return render_template('Border Koli.html')

@app.route('/dogs/Akita')
def Akita():
    
    return render_template('Akita.html')

@app.route('/dogs/Baset')
def Baset():
    
    return render_template('Baset.html')

@app.route('/dogs/Bernardinac')
def Bernardinac():
    
    return render_template('Bernardinac.html')

@app.route('/dogs/Koker Španijel')
def Koker_Španijel():
   
    return render_template('Koker Španijel.html')

@app.route('/dogs/Dogo Argentino')
def Dogo_Argentino():
    
    return render_template('Dogo Argentino.html')

@app.route('/dogs/Engleski Mastif')
def Engleski_Mastif():
    
    return render_template('Engleski Mastif.html')

if __name__ == '__main__':
    app.run(debug=False,'0.0.0.0')

