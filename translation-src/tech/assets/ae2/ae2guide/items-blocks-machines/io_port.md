---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME IO Port
  icon: io_port
  position: 210
categories:
- devices
item_ids:
- ae2:io_port
---

# The ME I/O Port

<BlockImage id="io_port" p:powered="true" scale="8" />

IO Port ใช้เติมหรือระบาย [Storage Cell](../items-blocks-machines/storage_cells.md) ระหว่างเซลล์กับ
[ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ได้อย่างรวดเร็ว

หมุนได้ด้วย <ItemLink id="certus_quartz_wrench" />

## Settings

การตั้งค่า

*   ตั้งให้ IO Port ย้ายเซลล์ไปยังช่องขาออกเมื่อเซลล์ว่าง เต็ม หรือทำงานเสร็จได้
*   เมื่อใส่ <ItemLink id="redstone_card" /> จะมีตัวเลือกเงื่อนไขเรดสโตนหลายแบบ
*   ลูกศรกลางหน้าจอใช้กำหนดทิศทางย้ายไอเทม จากเซลล์เข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
    หรือจากที่เก็บเข้าเซลล์

## Upgrades

อัปเกรด

IO Port รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="speed_card" /> เพิ่มจำนวนสิ่งของที่ย้ายต่อการทำงานหนึ่งครั้ง
*   <ItemLink id="redstone_card" /> เพิ่มการควบคุมด้วยเรดสโตน ให้ทำงานเมื่อสัญญาณสูง ต่ำ หรือหนึ่งครั้งต่อพัลส์

## Recipe

สูตรคราฟต์

<RecipeFor id="io_port" />
