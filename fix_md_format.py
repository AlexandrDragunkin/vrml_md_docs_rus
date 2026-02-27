import re
import os

def fix_markdown_paragraphs(file_path: str) -> None:
    """
    Исправляет переносы строк в абзацах Markdown файла:
    - Сохраняет пустую строку после заголовка
    - Убирает переносы внутри абзаца
    - Сохраняет переносы между разными абзацами
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Разделяем содержимое на строки для более точной обработки
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        fixed_lines.append(line)
        
        # Если это заголовок с якорем
        if re.match(r'^<a id="[^"]+"></a>\s*#{1,6}', line):
            # Пропускаем пустую строку после заголовка
            if i + 1 < len(lines) and lines[i + 1].strip() == '':
                fixed_lines.append('')
                i += 1
            
            # Обрабатываем следующий абзац (все строки до следующего заголовка или пустой строки)
            paragraph_lines = []
            i += 1
            while i < len(lines):
                current_line = lines[i]
                # Если встречаем новый заголовок или пустую строку (конец абзаца) - останавливаемся
                if (re.match(r'^<a id="[^"]+"></a>\s*#{1,6}', current_line) or 
                    current_line.strip() == ''):
                    break
                paragraph_lines.append(current_line)
                i += 1
            
            if paragraph_lines:
                # Объединяем строки абзаца в одну
                paragraph_text = ' '.join(line.strip() for line in paragraph_lines if line.strip())
                fixed_lines.append(paragraph_text)
        
        i += 1
    
    # Объединяем обратно в текст
    fixed_content = '\n'.join(fixed_lines)
    
    # Убираем обратные слеши в ссылках (вторая задача)
    fixed_content = re.sub(r'\\', '', fixed_content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"Абзацы исправлены в файле: {file_path}")

def fix_markdown_smart(file_path: str) -> None:
    """
    Умное исправление форматирования Markdown:
    - Сохраняет структуру заголовков
    - Объединяет перенесенные строки в абзацах
    - Убирает обратные слеши
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Разделяем на параграфы (двойной перенос строки)
    paragraphs = content.split('\n\n')
    fixed_paragraphs = []
    
    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        
        # Если первый элемент - заголовок с якорем
        if len(lines) > 0 and re.match(r'^<a id="[^"]+"></a>\s*#{1,6}', lines[0]):
            # Заголовок оставляем как есть
            header_line = lines[0]
            
            # Остальные строки абзаца объединяем
            if len(lines) > 1:
                paragraph_text = ' '.join(line.strip() for line in lines[1:] if line.strip())
                fixed_paragraph = header_line + '\n\n' + paragraph_text
            else:
                fixed_paragraph = header_line
        else:
            # Обычный абзац - просто объединяем строки
            paragraph_text = ' '.join(line.strip() for line in lines if line.strip())
            fixed_paragraph = paragraph_text
        
        fixed_paragraphs.append(fixed_paragraph)
    
    fixed_content = '\n\n'.join(fixed_paragraphs)
    
    # Убираем обратные слеши
    fixed_content = re.sub(r'\\', '', fixed_content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"Умное форматирование применено к файлу: {file_path}")

# Самый простой и надежный способ
def fix_markdown_simple(file_path: str) -> None:
    """
    Простой и надежный способ исправления:
    1. Найти все блоки "заголовок + абзац"
    2. В каждом абзаце заменить переносы на пробелы
    3. Сохранить пустую строку между заголовком и абзацем
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Паттерн для поиска блоков: заголовок + абзац (до следующего заголовка)
    pattern = r'(<a id="[^"]+"></a>\s*#{1,6}[^\n]+)\n\n([^<]*)'
    
    def fix_paragraph(match):
        header = match.group(1)  # Заголовок
        paragraph = match.group(2)  # Текст абзаца
        
        # Убираем переносы строк внутри абзаца, сохраняя структуру
        # Заменяем одиночные переносы на пробелы
        fixed_paragraph = re.sub(r'\n', ' ', paragraph)
        # Убираем лишние пробелы
        fixed_paragraph = re.sub(r'\s+', ' ', fixed_paragraph).strip()
        
        return f"{header}\n\n{fixed_paragraph}"
    
    # Применяем замену
    fixed_content = re.sub(pattern, fix_paragraph, content)
    
    # Убираем обратные слеши во всем документе
    fixed_content = re.sub(r'\\', '', fixed_content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"Простое форматирование применено к файлу: {file_path}")

# Демонстрация
def demo_fix():
    """Демонстрация исправления"""
    test_content = '''<a id="EnvironmentalSensor"></a>
### 3.23 environmental sensor

Environmental sensor [_nodes_](#Node) generate [_events_](#Event) based on the location of the viewpoint
in the world or in relation to [_objects_](#Object) in
the world. The TimeSensor node generates events at regular intervals in [_time_](#Time). A node of type Collision,
ProximitySensor, TimeSensor, or VisibilitySensor. See " [4.6.7.2 Environmental sensors](concepts.md#4.6.7.2)"
for details.

<a id="Element"></a>
### 3.22 element

The smallest unit into which an [_object_](#Object) may
be divided. For example, the header record of a [_VRML_\
_file_](#VRMLFile) or a single value of a multi-valued [_field_](#Field).'''

    print("ДО:")
    print(test_content)
    print("\n" + "="*50 + "\n")
    
    # Применяем исправление
    pattern = r'(<a id="[^"]+"></a>\s*#{1,6}[^\n]+)\n\n([^<]*)'
    
    def fix_para(match):
        header = match.group(1)
        para = match.group(2)
        fixed_para = re.sub(r'\n', ' ', para)
        fixed_para = re.sub(r'\s+', ' ', fixed_para).strip()
        return f"{header}\n\n{fixed_para}"
    
    result = re.sub(pattern, fix_para, test_content)
    result = re.sub(r'\\', '', result)
    
    print("ПОСЛЕ:")
    print(result)

if __name__ == "__main__":
    file_path = r"C:\REPO\VrmlMDRUS\part1\glossary.md"
    
    # Используйте самый простой способ - он самый надежный
    fix_markdown_simple(file_path)
    
    # Или демонстрацию
    # demo_fix()

