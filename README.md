# Doc Utils - Ulauncher Extension

📄 **Doc Utils** é uma extensão para o [Ulauncher](https://ulauncher.io) que permite **formatar, minificar e validar** arquivos ou trechos de texto em **JSON** ou **XML**, diretamente da launcher.

---

## 🚀 Funcionalidades

- 🔍 **Autodetecção** do tipo (JSON ou XML)
- 🎨 `prettier` — Formata com indentação e quebras de linha
- 📦 `minifier` — Compacta o conteúdo removendo espaços
- ✅ `validate` — Verifica se o conteúdo é válido e indica o tipo
- 📂 Suporte a arquivos locais com prefixo `file:///`
- 🧠 Autocomplete de caminhos de arquivos/pastas
- 📋 Copia o resultado direto para a área de transferência
- 🐧 Compatível com qualquer distribuição Linux

---

## ✨ Exemplos de uso

### ✅ Formatar JSON
```bash
doc beautify {"nome":"Silvan","idade":33}
```

### ✅ Minificar XML
```bash
doc minify <pessoa><nome>Silvan</nome></pessoa>
```

### ✅ Validar arquivo XML
```bash
doc check file:///home/seuusuario/nota.xml
```

<!-- ### ✅ Autocompletar caminhos
Digite:
```bash
doc prettier file:///
```
Use as setas para navegar pelas sugestões.

--- -->

## 🛠 Instalação

Para facilitar a instalação, geramos um script para instalar a extensão, para isto basta dar permissão de execução ao arquivo e executar

### 1. Conceder permissão ao arquivos install.sh
Executar o seguinte comando dentro da pasta clonada
```bash
sudo chmod +x install.sh
```

### 2. Executar a instalação
```bash
./install.sh
```

---

## 🐞 Logs e Debug

Todos os eventos e erros são registrados em:
```
~/.local/share/ulauncher/extensions/com.github.seunome.docutils/logs.txt
```

## 📤 Contribuições

Sinta-se livre para abrir *issues* ou fazer *pull requests*! Vamos deixar essa extensão insana juntos 😄

---

## 📜 Licença

MIT — Use livremente, sem moderação.
