import QtQuick 6
import QtQuick.Controls 2.15

ApplicationWindow {
    id : window
    width : 400
    height : 200
    visible : true
    title : qsTr("Dinamic Language Switcher")

    // Language ComboBox
    ComboBox {
        id : combo
        x : 50
        y : 50
        anchors.horizontalCenter : parent.horizontalCenter
        textRole : "text"
        valueRole : "value"
        onActivated : backend.switchLanguage(currentValue)

        model : [
            {
                value: "en-US",
                text: qsTr("English")
            }, {
                value: "fr-FR",
                text: qsTr("Français")
            }, {
                value: "zh-CN",
                text: qsTr("Chinese")
            }
        ]
    }

    Text {
        anchors.bottom : combo.top
        anchors.margins : 20
        anchors.horizontalCenter : parent.horizontalCenter
        text : qsTr("Sample Text")
    }

    Connections {
        target : backend
    }
}
