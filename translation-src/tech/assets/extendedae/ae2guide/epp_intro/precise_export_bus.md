---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: ME Precise Export Bus
    icon: extendedae:precise_export_bus
categories:
- extended devices
item_ids:
- extendedae:precise_export_bus
---

# ME Precise Export Bus

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_precise_export_bus.snbt"></ImportStructure>
</GameScene>

ME Precise Export Bus ส่งไอเทมหรือของเหลวออกตามจำนวนที่กำหนด โดยจะส่งเมื่อภาชนะปลายทางรับผลผลิตทั้งชุดได้เท่านั้น

## Example

ตัวอย่าง

![GUI](../pic/pre_bus_gui1.png)

การตั้งค่านี้ส่ง Cobblestone ออกครั้งละ 3 ชิ้น และจะหยุดส่งหากในเครือข่ายเหลือน้อยกว่า 3 ชิ้น

![GUI](../pic/pre_bus_gui2.png)

เครื่องจะหยุดส่งเช่นกันเมื่อภาชนะปลายทางรับทั้งชุดไม่ได้ ในภาพ หีบรับ Cobblestone ได้อีกเพียง 2 ชิ้น จึงหยุดส่ง
