shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
	menus.sort()
	for order in orders:
		start = 0
		end = len(menus) - 1
		is_available = False
		while start <= end:
			mid = (start + end) // 2
			if menus[mid] == order:
				is_available = True
				break
			elif menus[mid] < order:
				start = mid + 1
			else:
				end = mid - 1
		return is_available
	return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
