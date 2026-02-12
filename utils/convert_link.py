import re

def get_direct_drive_link(share_link):
    """
    Извлекает ID файла из ссылки Google Диска и формирует прямую ссылку для встраивания.
    Поддерживает ссылки вида:
    - https://drive.google.com/file/d/ID_ФАЙЛА/view?usp=share_link
    - https://drive.google.com/open?id=ID_ФАЙЛА
    """
    match = re.search(r'(?:id=|/d/)([a-zA-Z0-9_-]+)', share_link)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?id={file_id}"
    else:
        return "Не удалось извлечь ID файла из ссылки."