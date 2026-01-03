class Dict:
	def __init__(self):
		self.items = [None] * 8

	def get_key(self, key):
		return hash(key) % len(self.items)

	def put(self, key, value):
		self.items[self.get_key(key)] = value

	def get(self, key):
		return self.items[self.get_key(key)]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!
