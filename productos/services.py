# services.py
from .models import ProductType
from .mongodb import MongoDBClient
from bson import ObjectId, errors


class InventoryService:

    @staticmethod
    def register_product(data):
        product_type = ProductType.objects.get(id=data['product_type_id'])
        product_data = {
            'name': data['name'],
            'quantity': data['quantity'],
            'product_code': data['product_code'],
            'date': data['date'],
            'product_type': product_type.name,
            'status': data['status'],
        }
        MongoDBClient().collection.insert_one(product_data)
        return "Producto registrado con éxito"
    
    @staticmethod
    def list_inventory():
        # Obtener todos los documentos incluyendo el campo _id
        registros = MongoDBClient().collection.find()

        # Convertir los ObjectId a strings
        lista_inventario = []
        for registro in registros:
            registro['_id'] = str(registro['_id'])
            lista_inventario.append(registro)

        return lista_inventario
    
    @staticmethod
    def deliver_product(product_name):
        result = MongoDBClient().collection.update_one(
            {'name': product_name, 'status': 'Disponible'},
            {'$set': {'status': 'Entregado'}}
        )
        if result.matched_count > 0:
            return "Producto entregado con éxito"
        else:
            return "Producto ya entregado o no encontrado"

    @staticmethod
    def update_product(product_id, data):
        try:
            # Intenta convertir product_id a ObjectId
            object_id = ObjectId(product_id)
        except errors.InvalidId:
            return "Error: El ID del producto no es válido"
        
        # Buscar el producto por _id
        product = MongoDBClient().collection.find_one({'_id': object_id})
        if not product:
            return "Error: El producto no existe"
        
        # Actualizar los campos del producto
        update_fields = {}
        if 'name' in data:
            update_fields['name'] = data['name']
        if 'quantity' in data:
            update_fields['quantity'] = int(data['quantity'])
        if 'product_code' in data:
            update_fields['product_code'] = data['product_code']
        if 'date' in data:
            update_fields['date'] = data['date']
        if 'product_type_id' in data:
            update_fields['product_type_id'] = data ['product_type_id']
        if 'status' in data:
            update_fields['status'] = data['status']
        
        # Realizar la actualización en MongoDB
        MongoDBClient().collection.update_one(
            {'_id': object_id},
            {'$set': update_fields}
        )
        return "Producto actualizado con éxito"

    @staticmethod
    def delete_product(product_id):
        try:
            object_id = ObjectId(product_id)
        except errors.InvalidId:
            return "Error: El ID del producto no es válido"
        
        product = MongoDBClient().collection.find_one({'_id': object_id})
        if not product:
            return "Error: El producto no existe"

        MongoDBClient().collection.delete_one({'_id': object_id})
        return "Producto eliminado con éxito"

        