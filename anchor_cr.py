import re
import os

def add_anchors_to_headings_improved(file_path):
    """
    Улучшенная версия: добавляет якоря ко всем заголовкам с номерами
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    new_lines = []
    changes_made = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Ищем строку с заголовком, содержащим номер версии
        match = re.match(r'^(#+)\s*((\d+\.)+\d+\s+.*)$', line.strip())
        
        if match:
            heading_level = match.group(1)
            heading_text = match.group(2)
            
            # Извлекаем номер для якоря
            numbers_match = re.match(r'^((\d+\.)+\d+)', heading_text)
            if numbers_match:
                anchor_id = numbers_match.group(1)
                
                # Проверяем следующую строку на наличие якоря
                has_anchor = False
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if f'<a id="{anchor_id}">' in next_line or f'id="{anchor_id}"' in next_line:
                        has_anchor = True
                
                # Если якоря нет, добавляем его
                if not has_anchor:
                    new_lines.append(f'<a id="{anchor_id}"></a>\n')
                    changes_made = True
                
                new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
        
        i += 1
    
    # Записываем изменения, если они были
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)
        print(f"Якоря успешно добавлены в: {file_path}")
    else:
        print(f"Якоря уже присутствуют или не требуются в: {file_path}")

# Использование
if __name__ == "__main__":
    file_path = r"C:\REPO\VrmlMDRUS\part1\concepts.md"
    add_anchors_to_headings_improved(file_path)
