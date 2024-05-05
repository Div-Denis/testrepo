planets = ["Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptue"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# 修改数组
planets[3] = "red Planet"
print("Mars is also known as ", planets[3])

# 确定数组列表的长度 len()
planets = ["Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptue"]
number_of_planets = len(planets)
print("there are", number_of_planets, "planets in the solar system")

# 向数组列表中添加值: 可以在创建后添加和删除项。.append(value)
planets = ["Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptue"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There  are actually", number_of_planets , "planets in the solar system.")

# 从数组中删除值.pop()，可以删除列表中的最后一项
planets.pop()
number_of_planets = len(planets)
print("No,there are definitely", number_of_planets , "planets in the solar system.")

# 使用负索引，如何使用索引来提取列表中的单个项
print("The first planet is", planets[0])
# 索引从0开始增加，负索引从列表末尾开始，并向后执行
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# 在数组中查找值
# 若在确定某值在列表中的存储位置，请使用列表的index方法。此方法在列表中搜索值并返回该项的索引。如果未找到匹配项，则返回-1
planets = ["Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptue"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# 使用min() max()
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weiht = 12650 # 地球上的巴士的牛顿力
print("On Earth, a double-decker bus weighs", bus_weiht, "N")
print("The lightest a bus would be in the solar system is ", bus_weiht * min(gravity_on_planets), "N")
print("The heaveiest a bus would be in the solar system is ", bus_weiht * max(gravity_on_planets), "N")

# 操作列表数据
# 切片数组
planets = ["Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptue"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
planets_after_earth = planets[3:]
print(planets_after_earth)

# 连接列表
amalthea_group = ["Metis", "Adrastea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# 对列表进行排序，请对列表使用.sort()方法，Python 按字母顺序对字符串列表排序，按数字循序对数字列表排序
amalthea_group = ["Metis", "Adrastea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)