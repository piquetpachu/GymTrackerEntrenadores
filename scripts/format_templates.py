"""Formatea plantillas HTML Django en templates/ preservando tags {% %} y {{ }}.

Estrategia:
- Reemplazar temporalmente los bloques Django por marcadores únicos.
- Usar BeautifulSoup con el parser html5lib para prettify.
- Restaurar los bloques Django y escribir el archivo.

Uso: ejecutar desde la raíz del repo con el venv activado.
"""
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

TEMPLATES_DIR = Path(".") / "templates"
PATTERN_BLOCK = re.compile(r"({%.*?%})", re.DOTALL)
PATTERN_VAR = re.compile(r"({{.*?}})", re.DOTALL)


def escape_django_tags(text: str):
    replacements = {}
    i = 0

    def _swap(match):
        nonlocal i
        token = match.group(0)
        key = f"__DJANGO_TAG_{i}__"
        replacements[key] = token
        i += 1
        return key

    text = PATTERN_BLOCK.sub(_swap, text)
    text = PATTERN_VAR.sub(_swap, text)
    return text, replacements


def restore_django_tags(text: str, replacements: dict):
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def format_html_file(path: Path):
    original = path.read_text(encoding="utf-8")
    escaped, replacements = escape_django_tags(original)

    soup = BeautifulSoup(escaped, "html5lib")
    pretty = soup.prettify()

    restored = restore_django_tags(pretty, replacements)

    # Quick cleanup: remove extra blank lines
    restored = "\n".join([line.rstrip() for line in restored.splitlines()])

    if restored != original:
        path.write_text(restored, encoding="utf-8")
        return True
    return False


def main():
    if not TEMPLATES_DIR.exists():
        print("No directory 'templates' found.")
        sys.exit(1)

    changed = []
    for p in TEMPLATES_DIR.rglob("*.html"):
        try:
            if format_html_file(p):
                changed.append(str(p))
        except Exception as e:
            print(f"Error formateando {p}: {e}")

    if changed:
        print("Archivos modificados:")
        for c in changed:
            print(" - ", c)
    else:
        print("No se modificó ningún archivo.")


if __name__ == "__main__":
    main()
