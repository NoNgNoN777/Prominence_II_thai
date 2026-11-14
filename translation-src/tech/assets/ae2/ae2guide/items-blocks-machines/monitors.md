---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: จอแสดงผล
  icon: storage_monitor
  position: 210
categories:
- devices
item_ids:
- ae2:storage_monitor
- ae2:conversion_monitor
---

# Monitors

จอแสดงผล

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/assemblies/monitors.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

Monitor แสดงและให้โต้ตอบกับไอเทมหรือของเหลวชนิดเดียวได้โดยไม่ต้องเปิดหน้าจอ

Monitor จะใช้สีเดียวกับ [สาย](cables.md) ที่ติดตั้งอยู่

หากติดตั้ง Monitor บนพื้นหรือเพดาน หมุนได้ด้วย <ItemLink id="certus_quartz_wrench" />

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

# Storage Monitor

แสดงไอเทมหรือของเหลวพร้อมจำนวน ลองติดไว้ข้างฟาร์มหรือที่อื่น ๆ ดู...

*ไม่* ต้องใช้ [ช่องสัญญาณ](../ae2-mechanics/channels.md)

ปุ่มควบคุม:

*   คลิกขวาด้วยไอเทม หรือคลิกขวาสองครั้งด้วยภาชนะของเหลว เพื่อตั้ง Monitor ให้แสดงไอเทมหรือของเหลวนั้น
*   คลิกขวาด้วยมือเปล่าเพื่อล้าง Monitor
*   Shift+คลิกขวาด้วยมือเปล่าเพื่อล็อก Monitor

## Recipe

สูตรคราฟต์

<RecipeFor id="storage_monitor" />

# Conversion Monitor

Conversion Monitor คล้าย Storage Monitor แต่ใส่หรือดึงไอเทมที่กำหนดไว้ออกได้

หากไอเทมที่กำหนด [คราฟต์อัตโนมัติได้](../ae2-mechanics/autocrafting.md) แต่ไม่มีในที่เก็บ การพยายามดึงไอเทม
จะเปิดหน้าจอให้ระบุจำนวนที่ต้องการคราฟต์แทน

*ต้อง* ใช้ [ช่องสัญญาณ](../ae2-mechanics/channels.md)

ปุ่มควบคุมเพิ่มเติม:

*   คลิกซ้ายเพื่อดึงไอเทมที่กำหนดไว้หนึ่งกอง หรือขอคราฟต์หากไม่มีในที่เก็บ
*   คลิกขวาด้วยไอเทมใดก็ได้เพื่อใส่ไอเทมนั้น
*   คลิกขวาด้วยมือเปล่าเพื่อใส่ไอเทมที่กำหนดไว้ทั้งหมดจากช่องเก็บของของคุณ

## Recipe

สูตรคราฟต์

<RecipeFor id="conversion_monitor" />
