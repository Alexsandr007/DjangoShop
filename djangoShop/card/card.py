from django.conf import settings
from catalog.models import Product


class Card(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        card = self.session.get(settings.CARD_SESSION_ID)
        if not card:
            # сохраняем ПУСТУЮ корзину в сессии
            card = self.session[settings.CARD_SESSION_ID] = {}
        self.card = card

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данных.
        """
        product_ids = self.card.keys()
        # получаем товары и добавляем их в корзину
        products = Product.objects.filter(id__in=product_ids)

        card = self.card.copy()
        for product in products:
            card[str(product.id)]['product'] = product

        for item in card.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * int(item['quantity'])
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(int(item['quantity']) for item in self.card.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        product_id = str(product.id)
        if product_id not in self.card:
            self.card[product_id] = {'quantity': quantity,
                                     'price': str(product.price)}
            print('quantity_card'+str(quantity))
        elif update_quantity:
            self.card[product_id]['quantity'] = quantity
        else:
            k = self.card[product_id]['quantity']
            self.card[product_id]['quantity'] = int(k)+int(quantity)
        print(self.card)
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, product):
        """
        Удаляем товар
        """
        product_id = str(product.id)
        if product_id in self.card:
            del self.card[product_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(int(item['price']) * int(item['quantity']) for item in self.card.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CARD_SESSION_ID]
        self.save()