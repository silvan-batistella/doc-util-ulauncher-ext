# 📦 DocUtils for Ulauncher

Uma extensão para o [Ulauncher](https://ulauncher.io/) que permite **minificar**, **embelezar (beautify)** e **validar (check)** conteúdos JSON e XML diretamente pelo launcher.

<br>

## ✨ Funcionalidades

- ✅ **Check**: Valida arquivos JSON ou XML.
- 🧹 **Beautify**: Formata JSON ou XML com indentação.
- 📉 **Minify**: Remove espaços e quebras de linha para compactação.

- ⚙️ **Aliases personalizados** para comandos.
- 🧠 Destaque da linha com erro (caso haja).

<br>

## 🚀 Instalação

### 1. Clone o repositório na pasta de extensões do Ulauncher

```bash
cd ~/.local/share/ulauncher/extensions/
git clone https://github.com/seu-usuario/ulauncher-docutils.git com.github.silvan-batistella.docutils
cd com.github.silvan-batistella.docutils
```

> 📁 Certifique-se de que a pasta esteja com o nome exato:
**com.github.silvan-batistella.docutils**

<br>

### 2. Instale as dependências
Instale o pacote necessário diretamente com o **pip**, dentro do repositório que foi clonado do github:

```bash
pip install --user -r requirements.txt
```

ou **a depender do SO**

```bash
pip3 install --user -r requirements.txt
```

> ⚠️ Dependência do sistema (no Ubuntu/Debian):

```bash
 sudo apt install libxml2-dev libxslt1-dev python3-dev
```

<br>

## 🧪 Como usar
Abra o Ulauncher (Ctrl + Space ou atalho definido).

Digite doc e selecione uma das opções:
- beautify

- minify

- check


Cole seu JSON ou XML após o comando e veja o resultado!

<br>

## ⚙️ Configurações personalizadas
A extensão permite configurar apelidos (aliases) para cada comando via interface do Ulauncher:
| Configuração | Função | Padrão |
|---|---|---|
| Alias for Beautify | Atalho para beautify | beautify |
| Alias for Minify | Atalho para minify | minify |
| Alias for Check | Atalho para check | check |
||||		

Você pode usar apelidos curtos como:

```bash
doc beautify {"name": "exemplo"}
doc minify { "foo": "bar" }
doc check <xml><tag/></xml>

```

<br>

## 📄 License

MIT © 2025 
<br>
[Silvan S. Batistella](https://github.com/silvan-batistella)


