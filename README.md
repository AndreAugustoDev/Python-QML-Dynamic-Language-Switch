# Python QtQuick Dynamic Language Switch

This is a basic example of implementing dynamic language switching when running an application in PySide and QML.
It was only tested with PySide6, but I believe it can be adapted to PyQt5/6 and PySide2 without complications.

[[English](README.md) | [Portuguese](README-pt-BR.md)]

## Requirements

-   [Qt Linguist][qtlinguist] (see: [qtlinguist-installers][] | [thurask/Qt-Linguist][]) or other translation software (eg [OmegaT][omegat])
-   Code editor

## Tips

Here are tips on how to get the texts and compile them

**Extract translatable texts:**

```
lupdate .\main.qml -ts .\locale\en-US.ts .\locale\fr-FR.ts .\locale\zh-CN.ts
```

In this example, the texts are extracted from the **main.qml** file and exported in **.ts** format in the **locale** folder according to the specified names.

At this point translate these files using the translation software.

**Compiling translated texts:**
If you want to compile all languages ​​at once

```
lrelease .\locale\*.ts
```

Or if you just want a specific one:

```
lrelease .\locale\fr-FR.ts
```

# License

[MIT](LICENSE)

[qt]: https://qt.io
[qtlinguist]: https://doc.qt.io/qt-5/qtlinguist-index.html
[qtlinguist-installers]: https://github.com/lelegard/qtlinguist-installers
[thurask/qt-linguist]: https://github.com/thurask/Qt-Linguist/
[omegat]: omegat.sourceforge.io/
