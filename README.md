# 📄 PDF Toolbox

Egyszerű, ingyenes és nyílt forráskódú PDF eszköz Pythonban. Azokat az alapfunkciókat tartalmazza, amikért az online szolgáltatások általában fizetést kérnek, mindezt helyben, a saját gépeden futtatva. Nincs feltöltés, nincs fiók, nincs limit.

## ✨ Funkciók

| Funkció | Leírás |
|---|---|
| **Összefűzés (Merge)** | Több PDF egyesítése egyetlen fájlba, a megadott sorrendben |
| **Szétvágás (Split)** | PDF darabolása oldalak, oldaltartományok vagy fix oldalszám szerint |
| **Oldalak forgatása** | Egyes oldalak vagy a teljes dokumentum elforgatása 90°, 180° vagy 270°-kal |
| **Oldalak törlése és átrendezése** | Felesleges oldalak eltávolítása, oldalsorrend módosítása |
| **Szövegkinyerés** | A PDF szöveges tartalmának mentése `.txt` fájlba |
| **Képek → PDF** | JPG és PNG képek egyesítése egyetlen PDF-be |
| **Vízjel** | Szöveges vízjel elhelyezése az oldalakon |
| **Jelszavas védelem** | Jelszó hozzáadása és eltávolítása PDF-ről |
| **Tömörítés** | A fájlméret csökkentése a képek és a tartalom optimalizálásával |

## 🛠️ Használt technológiák

- [Python](https://www.python.org/) 3.10+
- [pypdf](https://pypi.org/project/pypdf/): PDF-műveletek
- [Pillow](https://pypi.org/project/pillow/): képkezelés
- [ReportLab](https://pypi.org/project/reportlab/): vízjel generálása


## 📁 Projektstruktúra

```
pdf-toolbox/
├── pdf-app.py              # belépési pont
├── tools/
│   ├── merge.py
│   ├── split.py
│   ├── rotate.py
│   ├── delete.py
│   ├── extract_text.py
│   ├── images_to_pdf.py
│   ├── watermark.py
│   ├── security.py
│   └── compress.py
├── requirements.txt
└── README.md
```

## 🗺️ Tervek

- Grafikus felület (Tkinter / PyQt)
- Drag & drop támogatás
- Kötegelt feldolgozás több fájlra
- Futtatható `.exe` készítése (PyInstaller)

## 🤝 Közreműködés

Ez egy személyes hobbiprojekt, de ötleteket, hibajelentéseket és pull requesteket szívesen fogadok. Nyiss egy issue-t, vagy készíts egy fork-ot.

## 📜 Licenc

MIT License: szabadon felhasználható, módosítható és terjeszthető. Részletek a `LICENSE` fájlban.

## 👤 Szerző

**Dénes** – [GitHub](https://github.com/Dns18)
