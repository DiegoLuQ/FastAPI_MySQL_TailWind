const btnEliminar = document.querySelector(".btneliminar");

btnEliminar.addEventListener("click", eliminarDato);
const boxBtn = document.querySelector("#boxbtn");
const prod_nombre = document.querySelector(".prod_nombre");
const prod_peso = document.querySelector(".prod_peso");
const prod_pventa = document.querySelector(".prod_pventa");
const prod_pcosto = document.querySelector(".prod_pcosto");
const prod_stock = document.querySelector(".prod_stock");
const prod_fecha = document.querySelector(".prod_fecha");
const id_proveedor = document.querySelector(".id_proveedor");
const idProd = document.querySelector(".idproducto")

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

const deleteModal = document.querySelector(".btn-eliminar");
const modalOn = document.querySelector(".modal-on");
const modalOff = document.querySelector(".modal-off");

deleteModal.addEventListener("click", modalRender);
modalOff.addEventListener("click", FuncModalOff);

function modalRender(e) {
  e.preventDefault(e);
  modalOn.classList.remove("hidden");
}
function FuncModalOff(e) {
  e.preventDefault();
  modalOn.classList.add("hidden");
}


function eliminarDato(e) {
  e.preventDefault();
  const id = parseInt(idProd.value)
  const url_eliminar = `http://127.0.0.1:8000/v1/productos/eliminar_producto/${id}`;

  try {
    fetch(url_eliminar, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((dato) => dato.json())
      .then((response) => {
        console.log(response);
        console.log(response.message);
        if (response.code === 201 || response.code === 200) {
          setTimeout(() => {
            boxBtn.textContent = response.message;
            boxBtn.classList.add('text-red-500')
            limpiarCampos()
            setTimeout(() => {
              boxBtn.textContent = "";
            }, 5000);
          }, 10);
        } else {
          setTimeout(() => {
            boxBtn.textContent = response.message;
            boxBtn.classList.remove(('text-red-500'))
          }, 2000);
        }
        modalOn.classList.add("hidden");
      });
  } catch (error) {
    console.log(error);
  }
}


function limpiarCampos(){
    prod_nombre.value = ''
    prod_peso.value = ''
    prod_pventa.value = ''
    prod_pcosto.value = ''
    prod_stock.value = ''
    prod_fecha.value = ''
    idProd.value = ''
    id_proveedor.value = ''
}