import json
import logging
from lxml import etree
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.ActionList import ActionList

logger = logging.getLogger(__name__)

def minify(text):
    text = text.strip()
    if not text:
        return "Entrada vazia. Por favor, forneça um JSON ou XML válido para minificar."

    fmt = detect_format(text)
    if fmt == 'json':
        try:
            obj = json.loads(text)
            return json.dumps(obj, separators=(',', ':'))
        except Exception as e:
            return f"Invalid JSON: {str(e)}"
    elif fmt == 'xml':
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.fromstring(text.encode(), parser)
            return etree.tostring(tree, encoding='unicode', method='xml')
        except Exception as e:
            return f"Invalid XML: {str(e)}"
    else:
        return "Formato desconhecido para minificar. Use JSON ou XML."


def beautify(text):
    try:
        obj = json.loads(text)
        return json.dumps(obj, indent=4)
    except Exception as e:
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.fromstring(text.encode(), parser)
            return etree.tostring(tree, pretty_print=True, encoding='unicode')
        except Exception as e2:
            return f"Invalid format for beautify: {str(e2)}"

def get_line_content(text, line_number):
    lines = text.splitlines()
    if 1 <= line_number <= len(lines):
        return lines[line_number - 1].strip()
    return ""

def detect_format(text):
    text = text.strip()
    if not text:
        return None

    open_braces = text.count('{')
    open_angles = text.count('<')

    if open_braces == 0 and open_angles == 0:
        return None

    if open_braces >= open_angles:
        try:
            json.loads(text)
            return 'json'
        except:
            return 'json'
    else:
        return 'xml'

def check(text):
    items = []
    fmt = detect_format(text)

    if fmt == 'json':
        try:
            json.loads(text)
            items.append(ExtensionResultItem(
                icon='images/json.png',
                name='✅ JSON válido',
                description='Nenhum erro encontrado.',
                on_enter=HideWindowAction()
            ))
        except json.JSONDecodeError as e:
            items.append(ExtensionResultItem(
                icon='images/json.png',
                name='❌ Erro no JSON',
                description=f'{e.msg} (linha {e.lineno}, coluna {e.colno})',
                on_enter=HideWindowAction()
            ))
            items.append(ExtensionResultItem(
                icon='images/json.png',
                name='🧠 Linha com erro',
                description=get_line_content(text, e.lineno),
                on_enter=HideWindowAction()
            ))
    elif fmt == 'xml':
        parser = etree.XMLParser(recover=True)
        try:
            etree.fromstring(text.encode(), parser)
            items.append(ExtensionResultItem(
                icon='images/xml.png',
                name='✅ XML válido',
                description='Nenhum erro encontrado.',
                on_enter=HideWindowAction()
            ))
        except etree.XMLSyntaxError as e:
            first_error = e.error_log[0] if e.error_log else None
            if first_error:
                items.append(ExtensionResultItem(
                    icon='images/xml.png',
                    name=f'❌ {first_error.level_name} em XML',
                    description=f'{first_error.message} (linha {first_error.line}, coluna {first_error.column})',
                    on_enter=HideWindowAction()
                ))
                items.append(ExtensionResultItem(
                    icon='images/xml.png',
                    name='🧠 Linha com erro',
                    description=get_line_content(text, first_error.line),
                    on_enter=HideWindowAction()
                ))
            else:
                items.append(ExtensionResultItem(
                    icon='images/xml.png',
                    name='❌ Erro desconhecido em XML',
                    description=str(e),
                    on_enter=HideWindowAction()
                ))
    else:
        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name='Formato desconhecido ❓',
            description='Não foi possível determinar se é JSON ou XML.',
            on_enter=HideWindowAction()
        ))

    return items

def has_error(items):
    for item in items:
        try:
            name = item.get_name()
        except AttributeError:
            name = getattr(item, '_name', '')
        if '❌' in name:
            return True
    return False

def copiarMessagem(text):
    return ActionList([
        CopyToClipboardAction(text),
        HideWindowAction()
    ])

class DocUtilsExtension(Extension):
    def __init__(self):
        super(DocUtilsExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = (event.get_argument() or "").strip()

        # Lê aliases personalizados
        alias_beautify = extension.preferences.get('alias_beautify', 'beautify').lower()
        alias_check = extension.preferences.get('alias_check', 'check').lower()
        alias_minify = extension.preferences.get('alias_minify', 'minify').lower()

        alias_map = {
            alias_beautify: 'beautify',
            alias_check: 'check',
            alias_minify: 'minify'
        }

        parts = query.split(' ', 1)
        user_action = parts[0].lower() if parts else ''
        normalized_action = alias_map.get(user_action)
        content = parts[1] if len(parts) > 1 else ''

        # Sugestão se o comando estiver incompleto ou errado
        if not query or user_action not in alias_map:
            valid_actions = {
                alias_beautify: {
                    'action': 'beautify',
                    'icon': 'images/beautify.png',
                    'description': 'Beautify content input'
                },
                alias_check: {
                    'action': 'check',
                    'icon': 'images/check.png',
                    'description': 'Validate content syntax'
                },
                alias_minify: {
                    'action': 'minify',
                    'icon': 'images/minify.png',
                    'description': 'Minify content input'
                }
            }

            filtered_items = []
            for alias, data in valid_actions.items():
                if alias.startswith(user_action):
                    filtered_items.append(
                        ExtensionResultItem(
                            icon=data['icon'],
                            name=data['action'].capitalize(),
                            description=data['description'],
                            on_enter=SetUserQueryAction(f'doc {alias} ')
                        )
                    )

            return RenderResultListAction(filtered_items or [
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Ação inválida',
                    description='Use: minify, beautify ou check',
                    on_enter=HideWindowAction()
                )
            ])

        # Se não há conteúdo, aguarda entrada
        if not content:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Aguardando entrada',
                    description=f'Digite ou cole o conteúdo para \"{normalized_action}\"',
                    on_enter=ExtensionCustomAction({'action': normalized_action, 'text': ''}, keep_app_open=True)
                )
            ])

        # Execução da ação
        if normalized_action == 'check':
            return RenderResultListAction(check(content))

        if normalized_action == 'beautify':
            items = check(content)
            if has_error(items):
                return RenderResultListAction(items)
            result = beautify(content)
            fmt = detect_format(content)
            icon = 'images/json.png' if fmt == 'json' else 'images/xml.png'
            preview = result.replace('\n', ' ')[:50] + ('...' if len(result) > 50 else '')
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=icon,
                    name='✅ Resultado Beautify - Clique para Copiar',
                    description=preview,
                    on_enter=copiarMessagem(result)
                )
            ])

        if normalized_action == 'minify':
            items = check(content)
            if has_error(items):
                return RenderResultListAction(items)
            result = minify(content)
            fmt = detect_format(content)
            icon = 'images/json.png' if fmt == 'json' else 'images/xml.png'
            preview = result.replace('\n', ' ')[:50] + ('...' if len(result) > 50 else '')
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=icon,
                    name='✅ Resultado Minify - Clique para Copiar',
                    description=preview,
                    on_enter=copiarMessagem(result)
                )
            ])

class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        action = data.get('action')
        text = data.get('text', '')

        if action == 'minify':
            result = minify(text)
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/json.png',
                    name='Minificado',
                    description=result,
                    on_enter=HideWindowAction()
                )
            ])
        elif action == 'beautify':
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/json.png',
                    name='Beautify executado',
                    description='',
                    on_enter=HideWindowAction()
                )
            ])
        elif action == 'copy_beautify':
            return copiarMessagem(text)
        elif action == 'check':
            return RenderResultListAction(check(text))
        else:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Ação desconhecida',
                    description='Erro interno ao processar ação.',
                    on_enter=HideWindowAction()
                )
            ])

if __name__ == '__main__':
    DocUtilsExtension().run()
