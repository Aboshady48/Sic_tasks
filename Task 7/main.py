class SicStore ():
    def __init__ (self,clothes_type,model_year,brand,price):
        self.clothes_type=clothes_type
        self.model_year=model_year
        self.brand=brand
        self.price=price
        
    def calc(self):
        if self.clothes_type == "shirt":
            discount = 0.4
        elif self.clothes_type == "shose":
            discount = 0.5
        elif self.clothes_type == "pants":
            discount = 0.3
        else:
            discount = 0

        disc_price = self.price * (1 - discount)# this make the all oprations take the price and discont and clc all of them
        return disc_price


def main():
    clothes_type = input("Enter the type of clothes [shirt, pants, shoes]: ")
    model_year = int(input("Enter the model year: "))
    brand = input("Enter the brand: ")
    price = float(input("Enter the price: "))

    clothes_item = SicStore(clothes_type, model_year, brand, price)
    discounted_price = clothes_item.calc()
    print(f"The discounted price is: {discounted_price}")

if __name__ == "__main__":
    main()