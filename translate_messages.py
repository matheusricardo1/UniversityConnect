from googletrans import Translator
import polib

def translate_messages():
    # Caminho do arquivo PO para o idioma inglês (en)
    caminho_po_en = 'locale/en/LC_MESSAGES/django.po'

    # Traduzir as mensagens para o idioma inglês
    traduzir_mensagens(caminho_po_en, 'en')

def traduzir_mensagens(caminho_po, idioma_destino):
    translator = Translator()
    po = polib.pofile(caminho_po)

    for entry in po:
        if entry.msgstr == "":
            # Apenas traduz mensagens que não possuem tradução
            traducao = translator.translate(entry.msgid, dest=idioma_destino)
            entry.msgstr = traducao.text

    # Salva as alterações no arquivo PO
    po.save()

if __name__ == "__main__":
    translate_messages()
