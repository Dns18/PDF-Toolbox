# 📄 PDF Toolbox

A simple, free and open-source PDF tool written in Python. No uploads, no accounts, no limits.

## ✨ Features

| Feature | Description |
|---|---|
| **Merge** | Combine multiple PDFs into a single file in the order you choose |
| **Split** | Break a PDF apart by pages, page ranges or a fixed number of pages |
| **Rotate pages** | Rotate individual pages or the whole document by 90°, 180° or 270° |
| **Delete and reorder pages** | Remove unwanted pages and change the page order |
| **Text extraction** | Save the text content of a PDF to a `.txt` file |
| **Images → PDF** | Combine JPG and PNG images into a single PDF |
| **Watermark** | Add a text watermark to the pages |
| **Password protection** | Add or remove a password on a PDF |
| **Compression** | Reduce file size by optimizing images and content |

## 🛠️ Built With

- [Python](https://www.python.org/) 3.10+
- [pypdf](https://pypi.org/project/pypdf/): PDF operations
- [Pillow](https://pypi.org/project/pillow/): image handling
- [ReportLab](https://pypi.org/project/reportlab/): watermark generation

## 📁 Project Structure

```
pdf-toolbox/
├── pdf-app.py              # entry point
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

## 🗺️ Roadmap

- Graphical user interface (Tkinter / PyQt)
- Drag & drop support
- Batch processing for multiple files
- Standalone `.exe` build (PyInstaller)

## 🤝 Contributing

This is a personal hobby project, but ideas, bug reports and pull requests are welcome. Open an issue or create a fork.

## 📜 License

MIT License: free to use, modify and distribute. See the `LICENSE` file for details.

## 👤 Author

**Dénes** – [GitHub](https://github.com/Dns18)


# 📄 PDF Toolbox

Egyszerű, ingyenes és nyílt forráskódú PDF eszköz Pythonban. Nincs feltöltés, nincs fiók, nincs limit.

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
