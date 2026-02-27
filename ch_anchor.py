import re
import os

def convert_html_anchors_to_markdown(file_path: str) -> None:
    """
    Конвертирует HTML якоря в Markdown синтаксис
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Паттерн для поиска HTML якорей перед заголовками
    pattern = r'<a id="([^"]+)"></a>\s*\n\s*(#{1,6}\s*[^\n]+)'
    
    def replace_with_markdown(match):
        anchor_id = match.group(1)
        heading = match.group(2)
        return f"{heading} {{#{anchor_id}}}"
    
    fixed_content = re.sub(pattern, replace_with_markdown, content)
    
    # Также заменяем HTML ссылки в тексте
    fixed_content = re.sub(r'<a id="([^"]+)"></a>', '', fixed_content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"HTML якоря конвертированы в Markdown в файле: {file_path}")

def remove_html_anchors_keep_links(file_path: str) -> None:
    """
    Удаляет HTML якоря, но сохраняет ссылки в тексте
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Удаляем только HTML якоря, но оставляем текст и заголовки
    # Паттерн: якорь + заголовок -> заголовок
    content = re.sub(r'<a id="[^"]+"></a>\s*\n\s*', '', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"HTML якоря удалены из файла: {file_path}")

# Альтернатива: использовать комментарии для якорей
def convert_to_markdown_with_comments(file_path: str) -> None:
    """
    Заменяет HTML якоря на Markdown-совместимые комментарии
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Заменяем HTML якоря на комментарии
    pattern = r'<a id="([^"]+)"></a>\s*\n\s*(#{1,6}\s*[^\n]+)'
    
    def replace_with_comment(match):
        anchor_id = match.group(1)
        heading = match.group(2)
        return f"<!-- {anchor_id} -->\n{heading}"
    
    fixed_content = re.sub(pattern, replace_with_comment, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"HTML якоря заменены на комментарии в файле: {file_path}")

def fix_markdown_anchors_final(file_path: str) -> None:
    """
    Финальное исправление: чистый Markdown синтаксис
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Заменяем HTML якоря на Markdown синтаксис
    # Был: <a id="PointingDeviceSensor"></a>\n### 3.77 pointing device sensor
    # Стал: ### 3.77 pointing device sensor {#PointingDeviceSensor}
    pattern = r'<a id="([^"]+)"></a>\s*\n\s*(#{1,6}\s*[\d\.]+\s*[^\n]+)'
    
    def markdown_anchor(match):
        anchor_id = match.group(1)
        heading = match.group(2)
        return f"{heading} {{#{anchor_id}}}"
    
    fixed_content = re.sub(pattern, markdown_anchor, content)
    
    # Обновляем ссылки в тексте (заменяем HTML якоря на чистые)
    fixed_content = re.sub(r'\[_([^_]+)_\]\(#([^)]+)\)', r'[_\1_](#\2)', fixed_content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"Файл конвертирован в чистый Markdown: {file_path}")

# Использование
if __name__ == "__main__":
    file_path = r"C:/REPO/VrmlMDRUS/part1/glossary.md"
    fix_markdown_anchors_final(file_path)
