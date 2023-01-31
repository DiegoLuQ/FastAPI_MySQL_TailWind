console.log("Hola");

const prod_nombre = document.querySelector(".prod_nombre");
const prod_peso = document.querySelector(".prod_peso");
const prod_pventa = document.querySelector(".prod_pventa");
const prod_pcosto = document.querySelector(".prod_pcosto");
const prod_stock = document.querySelector(".prod_stock");
const prod_fecha = document.querySelector(".prod_fecha");
const id_proveedor = document.querySelector(".id_proveedor");
const boxBtn = document.querySelector("#boxbtn");

const url = "http://localhost:8000/v1/productos/agregar";
const btnRegistrar = document.querySelector("#btn-registrar");


btnRegistrar.addEventListener("click", obtenerDatos);

function CapturarDatos() {
  const datos = {
    prod_nombre: prod_nombre.value.toLowerCase(),
    prod_peso: parseFloat(prod_peso.value),
    prod_pventa: parseInt(prod_pventa.value),
    prod_pcosto: parseInt(prod_pcosto.value),
    prod_stock: parseInt(prod_stock.value),
    prod_fecha: prod_fecha.value,
    id_proveedor: parseInt(id_proveedor.value),
  };
  return datos;
}

function obtenerDatos(e) {
  e.preventDefault();

  if (
    prod_nombre.value == "" &&
    prod_peso.value == "" &&
    prod_pcosto.value == "" &&
    prod_pventa.value == "" &&
    prod_stock.value == "" &&
    prod_fecha.value == ""
  ) {
    setTimeout(() => {
      boxBtn.classList.add("text-red-500");
      boxBtn.textContent = "Debes llenar todos los campos";
      setTimeout(() => {
        boxBtn.classList.remove("text-red-500");
        boxBtn.textContent = "";
      }, 5000);
    }, 10);

    return;
  } else {
    const datos = {
      prod_nombre: prod_nombre.value.toLowerCase(),
      prod_peso: parseFloat(prod_peso.value),
      prod_pventa: parseInt(prod_pventa.value),
      prod_pcosto: parseInt(prod_pcosto.value),
      prod_stock: parseInt(prod_stock.value),
      prod_fecha: prod_fecha.value,
      id_proveedor: parseInt(id_proveedor.value),
    };
    registar(datos, url);
  }
}

async function registar(data, url) {
  console.log(data, url);
  try {
    await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((dato) => dato.json())
      .then((response) => {
        console.log(response);
        console.log(response.message);
        if (response.code === 201) {
          setTimeout(() => {
            boxBtn.textContent = response.message;
            boxBtn.classList.add('text-green-400')
            setTimeout(() => {
              boxBtn.classList.remove('text-green-400')
              boxBtn.textContent = "";
            }, 5000);
          }, 10);
        } else {
          setTimeout(() => {
            boxBtn.textContent = response.message;
          }, 2000);
        }
      });
  } catch (error) {
    console.log(error);
  }
}
