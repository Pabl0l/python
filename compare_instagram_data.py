# compare_instagram_data.py
# Analiza followers y followees desde los archivos JSON descargados de Instagram.

import json

# Cargar lista de seguidores (followers)
with open("followers_and_following/followers_1.json", encoding="utf-8") as f:
    followers_data = json.load(f)
    followers = {item["string_list_data"][0]["value"] for item in followers_data}

# Cargar lista de seguidos (followees)
with open("followers_and_following/following.json", encoding="utf-8") as f:
    followees_data = json.load(f)
    followees = {item["string_list_data"][0]["value"] for item in followees_data}

# Comparaciones
mutuals = followers & followees
you_follow_but_not_back = followees - followers
they_follow_but_not_back = followers - followees

# Resultados en consola
print(f"Total seguidores: {len(followers)}")
print(f"Total seguidos: {len(followees)}")
print(f"Mutuos: {len(mutuals)}")
print(f"No te siguen: {len(you_follow_but_not_back)}")
print(f"No sigues: {len(they_follow_but_not_back)}")

# Guardar en archivos de texto
with open("mutuos.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(mutuals)))

with open("no_te_siguen.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(you_follow_but_not_back)))

with open("no_sigues.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(they_follow_but_not_back)))

print("\nListas guardadas: mutuos.txt, no_te_siguen.txt, no_sigues.txt")
