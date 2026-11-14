---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: ME Wireless Connector
    icon: extendedae:wireless_connect
categories:
- extended devices
item_ids:
- extendedae:wireless_connect
- extendedae:wireless_tool
---

# ME Wireless Connector

<Row gap="20">
<BlockImage id="extendedae:wireless_connect" scale="6"></BlockImage>
<ItemImage id="extendedae:wireless_tool" scale="6"></ItemImage>
</Row>

ME Wireless Connector เชื่อมสองเครือข่ายได้คล้าย <ItemLink id="ae2:quantum_link" /> แต่มีระยะจำกัดและเชื่อมข้ามมิติไม่ได้

## Link the Wireless Connectors

เชื่อม Wireless Connector เข้าด้วยกัน

ใช้ ME Wireless Setup Kit คลิก Wireless Connector ทั้งสองเครื่องที่ต้องการ เพื่อเชื่อมเข้าด้วยกัน

กดย่อพร้อมคลิกเพื่อล้างการตั้งค่าปัจจุบันของ ME Wireless Setup Kit

ME Wireless Connector จะเปลี่ยนลวดลายเมื่อเชื่อมต่อสำเร็จ

ME Wireless Connector ที่ยังไม่เชื่อมต่อ

<GameScene zoom="5" background="transparent">
  <ImportStructure src="../structure/wireless_connector_off.snbt"></ImportStructure>
</GameScene>

ME Wireless Connector ที่เชื่อมต่อแล้ว

<GameScene zoom="5" background="transparent">
  <ImportStructure src="../structure/wireless_connector_on.snbt"></ImportStructure>
</GameScene>

## Color

สี

ย้อมสี Wireless Connector ได้เหมือนสายเคเบิล โดยจะเชื่อมต่อเฉพาะสายเคเบิลหรือตัวเชื่อมต่อที่มีสีเดียวกัน

ต้องใช้ <ItemLink id="ae2:color_applicator" /> เพื่อย้อมสีตัวเชื่อมต่อ

จึงจัดวางตัวเชื่อมต่อไร้สายได้ดังตัวอย่างนี้:

<GameScene zoom="3" background="transparent" interactive={true}>
  <ImportStructure src="../structure/wireless_connector_setup.snbt"></ImportStructure>
</GameScene>


## Power Usage

การใช้พลังงาน

ME Wireless Connector ใช้พลังงานมากขึ้นเมื่ออยู่ห่างกัน ความสัมพันธ์ระหว่างระยะกับการใช้พลังงานไม่เป็นเส้นตรง
หากอยู่ไกลกันมากจึงอาจใช้พลังงานสูงมาก

ใช้ <ItemLink id="ae2:energy_card" /> เพื่อประหยัดพลังงานได้ แต่ละใบลดการใช้พลังงานลง 10%

