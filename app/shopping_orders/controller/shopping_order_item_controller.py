from fastapi import HTTPException, Response

from starlette.responses import JSONResponse
from app.products.exceptions import ProductNotFoundError, ProductOutOfStockError
from app.products.services import ProductService
from app.shopping_orders.exceptions import ShoppingOrderItemNotFoundError, ShoppingOrderNotFoundError
from app.shopping_orders.services import ShoppingOrderItemService, ShoppingOrderService


class ShoppingOrderItemController:
    """Shopping Order Item Controller"""

    @staticmethod
    def create(quantity: int, product_id: str, shopping_order_id: str) -> object:
        """
        It creates a shopping order item, updates the quantity in stock for the product and updates the total price for
        the shopping order
        :param quantity: int
        :type quantity: int
        :param product_id: The id of the product to be added to the shopping order
        :type product_id: str
        :param shopping_order_id: The id of the shopping order that the item is being added to
        :type shopping_order_id: str
        :return: Shopping order item object
        """

        try:
            # checking if input valid
            ShoppingOrderService.read_by_id(shopping_order_id)
            product = ProductService.read_by_id(product_id)

            # checking quantity in stock
            if product.quantity_in_stock < quantity:
                raise HTTPException(status_code=ProductOutOfStockError().code, detail=ProductOutOfStockError().message)

            # creating shopping order
            shopping_order_item = ShoppingOrderItemService.create(quantity, product_id, shopping_order_id)

            # updating quantity in stock for product
            ProductService.update_quantity_in_stock(product_id, quantity, subtract=True)

            # getting total cost of item
            item_price = product.price * quantity

            # updating shopping order total cost
            ShoppingOrderService.update_total_price_for_amount(shopping_order_id, item_price)

            return shopping_order_item
        except ProductNotFoundError as exc:
            raise HTTPException(status_code=400, detail=exc.message)
        except ShoppingOrderNotFoundError as exc:
            raise HTTPException(status_code=400, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_by_id(shopping_order_item_id: str) -> object:
        try:
            shopping_order_item = ShoppingOrderItemService.read_by_id(shopping_order_item_id)
            return shopping_order_item
        except ShoppingOrderItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_all() -> list[object]:
        try:
            shopping_order_items = ShoppingOrderItemService.read_all()
            return shopping_order_items
        except ShoppingOrderItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="There is no shopping order items in system.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def delete_by_id(shopping_order_item_id: str) -> Response:
        try:
            ShoppingOrderItemService.delete_by_id(shopping_order_item_id)
            return JSONResponse(
                status_code=200, content=f"Shopping order item with id - {shopping_order_item_id} deleted."
            )
        except ShoppingOrderItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))

    @staticmethod
    def read_items_by_shopping_order_id(shopping_order_id: str) -> list[object]:
        """
        It reads the shopping order items by shopping order id
        :param shopping_order_id: str
        :type shopping_order_id: str
        :return: A list of shopping order items.
        """

        try:
            ShoppingOrderService.read_by_id(shopping_order_id)
            shopping_order_items = ShoppingOrderItemService.read_items_by_shopping_order_id(shopping_order_id)
            return shopping_order_items
        except ShoppingOrderNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except ShoppingOrderItemNotFoundError as exc:
            raise HTTPException(status_code=exc.code, detail="There is no shopping order items in this order.")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc))
