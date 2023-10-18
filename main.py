import webbrowser, time

url = input("Введите ссылку: ")

while True:
 try:
  dur = int(input("Время просмотра: "))
  break
 except:
  print("\nВведите цифру!\n")

while True:
 try:
  wtc = int(input("Сколько просмотров: "))
  break
 except:
  print("\nВведите цифру!\n")

for i in range(wtc):
 webbrowser.open_new(url)
 time.sleep(dur)
