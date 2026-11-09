from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/archivo')
def archivo():
    return render_template("archivo.html")
@app.route('/about')
def about():
   return render_template("about.html")
# app.py
@app.route('/presentacion')
def presentacion():
    # Videos para la página de inicio
    videos_inicio = [
        {"titulo": "Despedida Promoción 2026", "embed_url": "https://www.facebook.com/andres.rubiano.874356/videos/1637855408068805/?idorvanity=1480710870651658", "tipo": "facebook"},
        {"titulo": "Presentacion Ciclas", "embed_url": "https://www.youtube.com/embed/ikpZ6Oj-Rf0", "tipo": "youtube"},
        {"titulo": "1103 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/aIXn614w-tQ", "tipo": "youtube"},
        {"titulo": "Presentación Profes", "embed_url": "https://www.youtube.com/embed/6NTPqKBrwpw", "tipo": "youtube"},
        {"titulo": "1102 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/Ban8ucWQUG0", "tipo": "youtube"},
        {"titulo": "1101 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/T7ls8C5UIkg", "tipo": "youtube"},
        {"titulo": "1102 Presentacion 2 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/yBKU0Ws80PQ", "tipo": "youtube"},
        {"titulo": "704 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/AZK19OdJ-WQ", "tipo": "youtube"},
        {"titulo": "8 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/n8GOmRsWAfo", "tipo": "youtube"},
        {"titulo": "1104 Jornada Mañana", "embed_url": "https://www.youtube.com/embed/QM-CwhOGdHM", "tipo": "youtube"},

        # Videos de Facebook
        {"titulo": "Presentación 1001", "embed_url": "https://www.facebook.com/andres.rubiano.874356/videos/1431772288559915/?idorvanity=1480710870651658", "tipo": "facebook"},
        {"titulo": "Presentación 1002", "embed_url": "https://www.facebook.com/andres.rubiano.874356/videos/2239171483694482/?idorvanity=1480710870651658", "tipo": "facebook"}
    ]
    return render_template("presentacion.html", videos=videos_inicio)
@app.route('/previo')
def previo():
    videos = [
        {"titulo": "Previo al Carnaval", "embed_url": "https://www.youtube.com/embed/CXvVwf6zFr4"},
        {"titulo": "Previo al Carnaval", "embed_url": "https://www.youtube.com/embed/L72C9o8bzBw?si=_MjMQJi8cfyeC2w_"},
        {"titulo": "Previo al Carnaval", "embed_url": "https://www.youtube.com/embed/kZGQ5a8Y0zE?si=9CFMm-i-ZOmnGZC8"}
    ]

    imagenes = [
        {"titulo": "Previo al Carnaval", "url": "IMG_1696.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1680.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1693.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1591.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1592.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1595.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1596.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1597.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1600.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1601.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1605.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1607.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1608.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1614.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1616.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1620.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1622.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1625.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1626.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1628.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1631.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1632.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1635.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1638.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1639.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1643.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1644.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1645.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1646.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1647.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1648.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1649.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1650.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1651.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1653.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1655.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1656.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1657.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1659.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1660.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1665.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1587.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1688.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1691.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1692.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1589.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1582.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1703.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1704.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1705.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1708.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1709.jpeg"},
        {"titulo": "Previo al Carnaval", "url": "IMG_1715.jpeg"}
    ]
    return render_template("previo.html", videos=videos, imagenes=imagenes)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)
