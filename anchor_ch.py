import re
import os
from typing import List, Tuple

def fix_markdown_anchors_with_newlines(file_path: str) -> None:
    """
    Исправляет HTML-якоря в Markdown файле с сохранением переносов строк.
    
    Преобразует якоря вида <a id="3.1"></a> в <a id="Activate"></a>
    с сохранением структуры документа.
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Паттерн для поиска HTML-якорей и следующих за ними заголовков
    # Учитываем возможные пробелы и переносы строк
    pattern = r'(<a id="([^"]+)"></a>)\s*(\n\s*#{1,6}\s*([^\n]+))'
    
    def create_camelcase_anchor(match):
        full_anchor_tag = match.group(1)  # Полный тег <a id="..."></a>
        old_anchor = match.group(2)       # Старый якорь (например "3.1")
        heading_part = match.group(3)     # Часть с заголовком включая переносы
        heading_text = match.group(4)     # Текст заголовка (например "3.1 activate")
        
        # Извлекаем ключевое слово из заголовка (часть после номера)
        keyword_match = re.match(r'^[\d\.]+\s+(.+)', heading_text)
        if keyword_match:
            keyword = keyword_match.group(1)
            
            # Преобразуем в CamelCase (горбатая нотация)
            camelcase = ''.join(word.capitalize() for word in keyword.split())
            
            # Создаем новый якорь с сохранением структуры
            new_anchor_tag = f'<a id="{camelcase}"></a>'
            
            # Возвращаем с сохранением переносов строк
            return new_anchor_tag + heading_part
        
        return match.group(0)  # Если не удалось извлечь ключевое слово
    
    new_content = re.sub(pattern, create_camelcase_anchor, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Якоря исправлены в файле: {file_path}")
        
        # Показываем изменения
        print("Внесенные изменения:")
        old_matches = re.findall(r'<a id="([^"]+)"></a>', content)
        new_matches = re.findall(r'<a id="([^"]+)"></a>', new_content)
        
        for old, new in zip(old_matches, new_matches):
            if old != new:
                print(f"  {old} -> {new}")
    else:
        print(f"Изменений не требуется в файле: {file_path}")

def comprehensive_anchor_fix_preserve_formatting(file_path: str) -> None:
    """
    Комплексное исправление якорей с полным сохранением форматирования.
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Более точный паттерн, который сохраняет все пробелы и переносы
    pattern = r'(<a id="([\d\.]+)"></a>)(\s*?\n?\s*?#{1,6}\s*([^\n]+))'
    
    def convert_anchor(match):
        anchor_tag = match.group(1)      # <a id="3.1"></a>
        old_anchor = match.group(2)      # 3.1
        spacing = match.group(3)         # пробелы и переносы + заголовок
        heading_text = match.group(4)    # текст заголовка
        
        # Извлекаем ключевые слова после номера
        keyword_match = re.match(r'^[\d\.]+\s+(.+)', heading_text)
        if keyword_match:
            keyword_text = keyword_match.group(1)
            
            # Преобразуем в CamelCase
            clean_keyword = re.sub(r'[^\w\s]', '', keyword_text)
            camelcase = ''.join(word.capitalize() for word in clean_keyword.split())
            
            # Сохраняем оригинальное форматирование
            return f'<a id="{camelcase}"></a>{spacing}'
        
        return match.group(0)
    
    new_content = re.sub(pattern, convert_anchor, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Якоря исправлены с сохранением форматирования в файле: {file_path}")
    else:
        print(f"Якоря уже в правильном формате в файле: {file_path}")

# Упрощенная версия для быстрого использования
def quick_fix_anchors(file_path: str):
    """Быстрое исправление якорей с сохранением переносов строк"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Замена с сохранением всей структуры после якоря
    def fix_match(match):
        old_id = match.group(1)
        rest_of_content = match.group(2)  # ВСЁ что после якоря до следующего якоря
        
        # Находим следующий заголовок после якоря
        heading_match = re.search(r'#+\s*([^\n]+)', rest_of_content)
        if heading_match:
            heading_text = heading_match.group(1).strip()
            
            # Извлекаем ключевое слово
            words = heading_text.split()
            if len(words) > 1:
                keyword = ' '.join(words[1:])
                camelcase = ''.join(word.capitalize() for word in keyword.split())
                
                # Заменяем только якорь, сохраняя всё остальное
                return f'<a id="{camelcase}"></a>{rest_of_content}'
        
        return match.group(0)
    
    # Ищем каждый якорь и следующий за ним контент
    new_content = re.sub(r'<a id="([\d\.]+)"></a>([^<]+)', fix_match, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Якоря исправлены в {file_path}")

# Демонстрация работы
def demo_fix():
    """Демонстрация исправления"""
    test_content = '''
<a id="3.1"></a>
### 3.1 activate

Some text here.

<a id="3.2"></a>
### 3.2 ancestor

More text.

<a id="3.14"></a>
### 3.14 children node

Final text.
'''
    
    # Применяем исправление
    pattern = r'(<a id="([\d\.]+)"></a>)(\s*?\n\s*?#{1,6}\s*([^\n]+))'
    
    def convert(match):
        anchor_tag = match.group(1)
        old_id = match.group(2)
        spacing = match.group(3)
        heading = match.group(4)
        
        words = heading.split()
        if len(words) > 1:
            keyword = ' '.join(words[1:])
            camelcase = ''.join(word.capitalize() for word in keyword.split())
            return f'<a id="{camelcase}"></a>{spacing}'
        
        return match.group(0)
    
    result = re.sub(pattern, convert, test_content)
    print("ДО:")
    print(test_content)
    print("\nПОСЛЕ:")
    print(result)

if __name__ == "__main__":
    # Использование
    file_path = r"C:\REPO\VrmlMDRUS\part1\glossary.md"
    
    # Вариант 1: Сохранение форматирования
    comprehensive_anchor_fix_preserve_formatting(file_path)
    
    # Вариант 2: Быстрое исправление
    # quick_fix_anchors(file_path)
    
    # Демонстрация
    # demo_fix()
