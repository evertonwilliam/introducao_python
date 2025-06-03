import re

# Lê a versão atual
with open("version.txt", "r") as f:
    version = f.read().strip()

# Incrementa o patch
major, minor, patch = map(int, version.split("."))
patch += 1
new_version = f"{major}.{minor}.{patch}"

# Salva a nova versão
with open("version.txt", "w") as f:
    f.write(new_version)

# Atualiza o README.md
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Substitui o texto entre os marcadores
new_readme = re.sub(
    r"(<!--version-start-->).*?(<!--version-end-->)",
    f"\\1 {new_version} \\2",
    readme,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print(f"Versão atualizada para {new_version}")