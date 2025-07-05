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
        print(f"Total package weight {total_weight / 1000:.1f}kg")