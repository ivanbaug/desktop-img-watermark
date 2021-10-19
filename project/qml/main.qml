import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

ApplicationWindow{
  id: window
  width: 400
  height: 580
  visible: true
  title: qsTr("Watermark My Image")

  // Set flags
  flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizedWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint
  
  // Set Material Style
  Material.theme: Material.Dark
  Material.accent: Material.LightBlue

  // Create top button
  Rectangle{
    id: topThing
    height: 40
    color: Material.color(Material.Blue)
    anchors{
      left: parent.left
      right: parent.right
      top: parent.top
      margins: 10
    }
    radius: 10
    Button {
        text: "press me"
        onClicked: msg.visible = true
    }
  }

  // Button {
  //   id: controlBt
  //   text: qsTr("Test")
  //   font.pixelSize: 32

  //   contentItem: Text {
  //       text: controlBt.text
  //       font: controlBt.font
  //       opacity: enabled ? 1.0 : 0.3
  //       color: controlBt.down ? "#17a81a" : "#21be2b"
  //       horizontalAlignment: Text.AlignHCenter
  //       verticalAlignment: Text.AlignVCenter
  //       elide: Text.ElideRight
  //   }

  //   background: Rectangle {
  //       height: 40
  //       color: Material.color(Material.Blue)
  //       anchors{
  //         left: parent.left
  //         right: parent.right
  //         top: topButton.bottom
  //         margins: 10
  //       }
  //       radius: 5
  //   }
  // }
}