from controllers.product.product import Product


class ProductHTTP():

    def __init__(self, controller_product: Product) -> None:
        self.controller_product = controller_product

    def create_product_request(self, body):
        try:
            self.controller_product.create()
        except Exception as e:
            return self.response_format(500, str(e))

    def delete_product_request(self, id):
        try:
            self.controller_product.delete(id)
            return self.response_format(200, "deleted")
        except Exception as e:
            return self.response_format(500, str(e))

    def retrieve_product_request(self):
        try:
            res = self.controller_product.readAllProducts()
            return self.response_format(200, res)
        except Exception as e:
            return self.response_format(500, str(e))

    def update_product_request(self, id, body):
        try:
            self.controller_product.update(body, id)
        except Exception as e:
            return self.response_format(500, str(e))

    def retrieve_one_product_request(self, id):
        try:
            id = int(id)
            res =  self.controller_product.readOne(id)
            return self.response_format(200, res)
        except Exception as e:
            return self.response_format(500, str(e))

    def response_format(self, code, result):
        return {
            "code": code,
            "result": result
    }