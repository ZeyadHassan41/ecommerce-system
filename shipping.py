import math

class ShippingService:
    @staticmethod
    def ship(items):
        print("** Shipment notice **")
        total_weight = 0
        item_counts = {}

        for item in items:
            name = item.name
            weight = item.weight
            item_counts[name] = item_counts.get(name, 0) + 1
            total_weight += weight

        for name, count in item_counts.items():
            print(f"{count}x {name}")
        for item in items:
            print(f"{item.weight}g")

        total_weight_kg = total_weight / 1000
        rounded_kg = math.ceil(total_weight_kg)
        print(f"Total package weight {total_weight_kg:.1f}kg")

        shipping_fee = 30 * rounded_kg
        return shipping_fee
