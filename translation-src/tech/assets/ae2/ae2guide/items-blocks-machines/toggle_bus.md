---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Toggle Bus
  icon: toggle_bus
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:toggle_bus
- ae2:inverted_toggle_bus
---

# The Toggle Bus

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/assemblies/toggle_bus.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

บัสที่ทำงานคล้าย <ItemLink id="fluix_glass_cable" /> หรือสายชนิดอื่น แต่สลับสถานะการเชื่อมต่อด้วยเรดสโตนได้
จึงใช้ตัดการเชื่อมต่อส่วนหนึ่งของ [เครือข่าย ME](../ae2-mechanics/me-network-connections.md) ได้

เมื่อได้รับสัญญาณเรดสโตน ชิ้นส่วนนี้จะเปิดการเชื่อมต่อ ส่วน <ItemLink id="inverted_toggle_bus" /> ทำงานกลับกัน
โดยปิดการเชื่อมต่อแทน

โปรดทราบว่าการสลับสถานะอาจทำให้เครือข่ายเริ่มทำงานใหม่และคำนวณอุปกรณ์ที่เชื่อมต่อใหม่

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

## Recipes

สูตรคราฟต์

<RecipeFor id="toggle_bus" />

<RecipeFor id="inverted_toggle_bus" />
