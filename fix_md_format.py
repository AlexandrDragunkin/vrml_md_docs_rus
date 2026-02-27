import re
import os


# Самый надежный метод - построчная обработка
def line_by_line_fix(file_path: str) -> None:
    """
    Построчная обработка - самый надежный способ
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    fixed_lines = []
    current_paragraph = []
    
    for i, line in enumerate(lines):
        line = line.rstrip('\n')  # Убираем символ переноса
        
        # Если это заголовок с якорем
        if re.match(r'^<a id="[^"]+"></a>\s*#{1,6}', line):
            # Если есть накопленный абзац - обрабатываем его
            if current_paragraph:
                # Объединяем строки абзаца
                paragraph_text = ' '.join(current_paragraph)
                fixed_lines.append(paragraph_text)
                fixed_lines.append('')  # Пустая строка перед заголовком
                current_paragraph = []
            
            # Добавляем заголовок
            fixed_lines.append(line)
        
        # Если пустая строка - конец абзаца
        elif line.strip() == '':
            if current_paragraph:
                paragraph_text = ' '.join(current_paragraph)
                fixed_lines.append(paragraph_text)
                current_paragraph = []
            fixed_lines.append('')
        
        # Обычная текстовая строка
        else:
            # Убираем обратные слеши из строки
            clean_line = line.replace('\\', '')
            current_paragraph.append(clean_line.strip())
    
    # Обрабатываем последний абзац
    if current_paragraph:
        paragraph_text = ' '.join(current_paragraph)
        fixed_lines.append(paragraph_text)
    
    # Записываем обратно
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(fixed_lines))
    
    print(f"Построчное форматирование применено к файлу: {file_path}")

def robust_markdown_fix(file_path: str) -> None:
    """
    Надежный метод обработки всех случаев
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Убираем обратные слеши
    content = content.replace('\\', '')
    
    # Разделяем на строки для точной обработки
    lines = content.split('\n')
    processed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Пропускаем полностью пустые строки
        if not line:
            processed_lines.append('')
            i += 1
            continue
        
        # Если это якорь
        if line.startswith('<a id="') and line.endswith('</a>'):
            processed_lines.append(line)
            
            # Следующая строка должна быть заголовком
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('#'):
                    processed_lines.append(next_line)
                    processed_lines.append('')  # Пустая строка после заголовка
                    i += 1  # Пропускаем уже обработанный заголовок
                else:
                    processed_lines.append('')  # Пустая строка если нет заголовка
            else:
                processed_lines.append('')  # Пустая строка в конце файла
        
        # Если это заголовок без якоря (на всякий случай)
        elif line.startswith('#'):
            processed_lines.append(line)
            processed_lines.append('')  # Пустая строка после заголовка
        
        # Обычный текст - начинаем собирать абзац
        else:
            paragraph_lines = [line]
            i += 1
            
            # Собираем все последующие непустые строки до якоря или заголовка
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line or next_line.startswith('<a id="') or next_line.startswith('#'):
                    break
                paragraph_lines.append(next_line)
                i += 1
            
            # Объединяем строки абзаца
            paragraph_text = ' '.join(paragraph_lines)
            processed_lines.append(paragraph_text)
            continue  # Не увеличиваем i, так как уже переместились вперед
        
        i += 1
    
    # Объединяем обратно
    fixed_content = '\n'.join(processed_lines)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(fixed_content)
    
    print(f"Надежное форматирование применено к файлу: {file_path}")

# Демонстрация
def demo_fix():
    """Демонстрация исправления"""
    test_content = '''computer-based file system.<a id="Frame"></a>
### 3.34 frame

A single rendering of a [_world_](#World) on a [_display device_](#DisplayDevice) or a single time-step in a simulation.<a id="Generator"></a>
### 3.35 generator

Компьютерная программа, которая создает[_VRML files_](#VRMLFile). Генератор может использоваться человеком или работать автоматически.<a id="GeometricPropertyNode"></a>
### 3.36 geometric property node'''

    print("ДО:")
    print(test_content)
    print("\n" + "="*50 + "\n")
    
    # Используем построчную обработку
    lines = test_content.split('\n')
    fixed_lines = []
    current_paragraph = []
    
    for line in lines:
        if re.match(r'^<a id="[^"]+"></a>\s*#{1,6}', line):
            if current_paragraph:
                paragraph_text = ' '.join(current_paragraph)
                fixed_lines.append(paragraph_text)
                fixed_lines.append('')
                current_paragraph = []
            fixed_lines.append(line)
        elif line.strip() == '':
            if current_paragraph:
                paragraph_text = ' '.join(current_paragraph)
                fixed_lines.append(paragraph_text)
                current_paragraph = []
            fixed_lines.append('')
        else:
            clean_line = line.replace('\\', '')
            current_paragraph.append(clean_line.strip())
    
    if current_paragraph:
        paragraph_text = ' '.join(current_paragraph)
        fixed_lines.append(paragraph_text)
    
    result = '\n'.join(fixed_lines)
    
    print("ПОСЛЕ:")
    print(result)

if __name__ == "__main__":
    file_path = r"C:\REPO\VrmlMDRUS\part1\concepts.md"
    
    # Самый надежный метод
    # line_by_line_fix(file_path)
    robust_markdown_fix(file_path)

    
    # Или демонстрацию
    # demo_fix()



