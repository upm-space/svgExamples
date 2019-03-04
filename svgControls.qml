import QtQuick 2.9
import QtQuick.Window 2.3
import QtQuick.Controls 2.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Image {
        id: myCircle2
        source: "svg/horizon_back.svg"

    }
    Image {
        id: horizonCircle
        source: "svg/horizon_circle.svg"

    }
    Image {
        id: mechanism
        source: "svg/horizon_mechanics.svg"

    }
    Image {
        id: myCircle
        source: "svg/fi_circle.svg"
    }

    Slider{
       onValueChanged : function(){
           texto.text = value;
           myCircle2.rotation = value
           horizonCircle.rotation = value
           //mechanism.x = (value + 90) * 2
           //mechanism.y = (value + 90) * 2
       }
       from: -90
       to: 90
       value: 0
       stepSize: 1
       x: 400
    }
    TextField {
        id:texto
        x:400
        y:40
    }
}
