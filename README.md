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

### 1. ✅ Instalação Automática via Ulauncher

1. Abra o Ulauncher e digite `ext`, depois pressione Enter.
2. A página de extensões será aberta no navegador.
3. Clique em **"Add Extension"**.
4. Cole o link abaixo e clique em **Add**:

   👉 [https://github.com/silvan-batistella/doc-util-ulauncher-ext](https://github.com/silvan-batistella/doc-util-ulauncher-ext)

---

### 2. 📦 Instale as dependências Python (necessário)

O Ulauncher **não instala automaticamente** as bibliotecas Python usadas pela extensão. Você precisa fazer isso uma vez após a instalação:

#### 2.1. Encontre o caminho da extensão:

```bash
find ~/.local/share/ulauncher/extensions/ -name requirements.txt
```

O caminho retornado será algo como:

```bash
~/.local/share/ulauncher/extensions/com.github.silvan-batistella.doc-util-ulauncher-ext/requirements.txt
```

#### 2.2. Instale os pacotes Python:

```bash
pip install --user -r /CAMINHO/requirements.txt
```

Substitua `/CAMINHO/requirements.txt` pelo caminho exato encontrado acima.

Ou, se estiver usando `pip3`:

```bash
pip3 install --user -r /CAMINHO/requirements.txt
```

#### 2.3. Instale dependências do sistema (para Ubuntu/Debian):

```bash
sudo apt install libxml2-dev libxslt1-dev python3-dev
```

---

## 🧪 Como usar

Abra o Ulauncher (`Ctrl + Space`) e digite `doc`, seguido de uma das opções:

- `beautify`
- `minify`
- `check`

Cole seu JSON ou XML após o comando e veja o resultado diretamente no launcher.

---

## ⚙️ Configurações personalizadas

A extensão permite configurar **apelidos (aliases)** para os comandos diretamente pela interface do Ulauncher:

| Configuração          | Função              | Padrão    |
|-----------------------|---------------------|-----------|
| Alias for Beautify    | Atalho para beautify| beautify  |
| Alias for Minify      | Atalho para minify  | minify    |
| Alias for Check       | Atalho para check   | check     |

Você pode usar comandos como:

```bash
doc beautify {"name": "exemplo"}
doc minify {"foo": "bar"}
doc check <xml><tag/></xml>
```

---

## 📄 Licença

MIT © 2025  
[Silvan S. Batistella](https://github.com/silvan-batistella)
