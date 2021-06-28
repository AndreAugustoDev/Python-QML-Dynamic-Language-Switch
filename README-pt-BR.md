# Python QtQuick Alternador de Linguagem Dinâmico

Este é um exemplo básico de implementação de mudança dinâmica de idioma durante a execução de um aplicativo em PySide e QML.
Foi testado apenas com PySide6, mas creio que pode ser adaptado para PyQt5/6 e PySide2 sem complicações.

[[English](README.md) | [Portuguese](README-pt-BR.md)]

## Requisitos

-   [Qt Linguist][qtlinguist] (veja: [qtlinguist-installers][] | [thurask/Qt-Linguist][]) ou outro software de tradução (ex.: [OmegaT][omegat])
-   Editor de código

## Dicas

Aqui estão dicas de como obter os textos e compilá-los

**Extrair textos traduzíveis:**

```
lupdate .\main.qml -ts .\locale\en-US.ts .\locale\fr-FR.ts .\locale\zh-CN.ts
```

Neste exemplo, os textos são extraídos do arquivo **main.qml** e exportados no formato **.ts** na pasta **locale** conforme os nomes especificados.

Neste momento traduza estes arquivos usando o software de tradução.

**Compilando textos traduzidos:**
Se desejar compilar todos os idiomas de uma vez

```
lrelease .\locale\*.ts
```

Ou se desejar apenas um específico:

```
lrelease .\locale\fr-FR.ts
```

# Licença

[MIT](LICENSE)

[qt]: https://qt.io
[qtlinguist]: https://doc.qt.io/qt-5/qtlinguist-index.html
[qtlinguist-installers]: https://github.com/lelegard/qtlinguist-installers
[thurask/qt-linguist]: https://github.com/thurask/Qt-Linguist/
[omegat]: omegat.sourceforge.io/
