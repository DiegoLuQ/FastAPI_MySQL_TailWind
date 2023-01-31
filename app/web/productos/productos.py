from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from core.db.repository import repo_productos
from core.db.session import get_db
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")

router = APIRouter(include_in_schema=False)


@router.get('/')
async def Home(request: Request, db: Session = Depends(get_db)):
    datos = await repo_productos.get_productos(db)
    return templates.TemplateResponse("productos/productos_lista.html", {"request": request, "productos": datos})


@router.get('/productos')
async def Productos(request: Request):
    return templates.TemplateResponse('productos/register.html', {"request": request, 'btn': "Registrar", "back_btn": "btn-registrar", 'title':"Registro de Productos"})


@router.get('/productos/{id}')
async def Productos_Edit(id:int, request: Request, db:Session=Depends(get_db)):
    datos = await repo_productos.get_producto(id, db)
    return templates.TemplateResponse('productos/register.html', {'request': request, 'btn': "Modificar", "back_btn": "btn-modificar", 'title':"Modificar Producto", "datos":datos})
