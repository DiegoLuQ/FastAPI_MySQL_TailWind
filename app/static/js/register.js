console.log('Hola')
const url = 'http://127.0.0.1:8000/v1/productos/agregar'
const btnRegistrar = document.querySelector('#btn-registrar')

btnRegistrar.addEventListener('click', obtenerDatos)
const prod_nombre = document.querySelector('.prod_nombre')
const prod_peso = document.querySelector('.prod_peso')
const prod_pventa = document.querySelector('.prod_pventa')
const prod_pcosto = document.querySelector('.prod_pcosto')
const prod_stock = document.querySelector('.prod_stock')
const prod_fecha = document.querySelector('.prod_fecha')
const id_proveedor = document.querySelector('.id_proveedor')


function obtenerDatos(e){
    e.preventDefault()
    const datos = {
        prod_nombre: (prod_nombre.value).toLowerCase(),
        prod_peso: parseFloat(prod_peso.value),
        prod_pventa: parseInt(prod_pventa.value),
        prod_pcosto: parseInt(prod_pcosto.value),
        prod_stock: parseInt(prod_stock.value),
        prod_fecha: prod_fecha.value,
        id_proveedor: parseInt(id_proveedor.value)
    }
    registar(datos, url)
}

async function registar(data, url) {
    console.log(data, url)
    try {
        await fetch(url, {
            method:"POST",
            headers: {'Content-Type': 'application/json', 'Accept':'application/json'},
            body: JSON.stringify(data)
        })
        .then(dato => dato.json() )
        .then(response => {
            console.log(response)
            console.log(response.message)
        })
    } catch (error) {
        console.log(error)
    }
}