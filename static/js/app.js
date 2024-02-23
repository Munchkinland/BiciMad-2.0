document.addEventListener('DOMContentLoaded', function() {
    var mymap = L.map('map').setView([40.416775, -3.703790], 13); // Coordenadas centradas en Madrid
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(mymap);

    // Manejar el envío del formulario
    document.getElementById('rutaForm').addEventListener('submit', function(e) {
        e.preventDefault(); // Evitar el envío real del formulario

        var estacionInicio = document.getElementById('estacionInicio').value;
        var estacionDestino = document.getElementById('estacionDestino').value;

        // Aquí, envía los nombres de las estaciones al backend mediante AJAX
        fetch('/calcular-ruta', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                estacionInicio: estacionInicio,
                estacionDestino: estacionDestino,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Asumiendo que 'data' incluye las coordenadas de la ruta como un array de latitudes y longitudes
            var ruta = L.polyline(data.ruta, {color: 'red'}).addTo(mymap);
            mymap.fitBounds(ruta.getBounds());
        })
        .catch(error => console.error('Error al cargar la ruta:', error));
    });
});
