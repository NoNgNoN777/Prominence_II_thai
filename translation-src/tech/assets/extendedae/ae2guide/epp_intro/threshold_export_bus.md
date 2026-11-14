---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: ME Threshold Export Bus
    icon: extendedae:threshold_export_bus
categories:
- extended devices
item_ids:
- extendedae:threshold_export_bus
---

# ME Threshold Export Bus

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_threshold_export_bus.snbt"></ImportStructure>
</GameScene>

ME Threshold Export Bus ทำงานเมื่อจำนวนไอเทมที่เก็บในเครือข่าย ME สูงกว่าหรือต่ำกว่าเกณฑ์ที่กำหนด

## Example

ตัวอย่าง

![GUI](../pic/thr_bus_gui1.png)

ตั้งเกณฑ์ Copper ไว้ที่ 128 จึงส่ง Copper ออกเมื่อจำนวนที่เก็บในเครือข่ายมากกว่า 128

![GUI](../pic/thr_bus_gui2.png)

ใช้เกณฑ์เดิม แต่ตั้งโหมดเป็นต่ำกว่า จึงส่ง Copper ออกเมื่อจำนวนที่เก็บต่ำกว่า 128