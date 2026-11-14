---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME Drive
  icon: drive
  position: 210
categories:
- devices
item_ids:
- ae2:drive
---

# The ME Drive

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/drive.snbt" />
</GameScene>

Drive เป็น [อุปกรณ์](../ae2-mechanics/devices.md) สำหรับใส่ [Storage Cell](storage_cells.md) เพื่อใช้เป็น
[ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) มี 10 ช่อง แต่ละช่องรับหนึ่งเซลล์

หากต้องการ คุณส่งเซลล์เข้าและดึงออกจากช่องเก็บของได้ด้วยระบบขนส่งไอเทมใดก็ได้ เช่น Hopper หรือบัส AE2

หมุนได้ด้วย <ItemLink id="certus_quartz_wrench" />

## Cell Status LEDs

ไฟ LED แสดงสถานะเซลล์

เซลล์ใน Drive มีไฟ LED แสดงสถานะ:

| สี  | สถานะ                                                                           |
| :----- | :------------------------------------------------------------------------------- |
| เขียว  | ว่างเปล่า                                                                            |
| น้ำเงิน   | มีของอยู่บางส่วน                                                                |
| ส้ม | [จำนวนชนิด](../ae2-mechanics/bytes-and-types.md) เต็ม เพิ่มชนิดใหม่ไม่ได้     |
| แดง    | [Bytes](../ae2-mechanics/bytes-and-types.md) เต็ม ใส่ไอเทมเพิ่มไม่ได้ |
| ดำ  | ไม่มีพลังงาน หรือ Drive ไม่มี [ช่องสัญญาณ](../ae2-mechanics/channels.md)                 |

## Priority

ลำดับความสำคัญ

ตั้งลำดับความสำคัญโดยคลิกประแจมุมขวาบนของหน้าจอ
ไอเทมที่เข้าสู่เครือข่ายจะเลือกที่เก็บที่มีลำดับความสำคัญสูงสุดก่อน
หากที่เก็บหรือเซลล์สองแห่งมีลำดับเท่ากัน จะเลือกแห่งที่มีไอเทมชนิดนั้นอยู่แล้ว
ก่อนที่เก็บอื่น เซลล์ที่ [กำหนดชนิดไว้](cell_workbench.md) จะถือว่ามีไอเทมนั้นอยู่แล้ว
เมื่ออยู่ในกลุ่มลำดับเดียวกัน ส่วนการดึงไอเทมออกจะเริ่มจากที่เก็บที่มีลำดับต่ำสุด
ระบบนี้ทำให้เมื่อมีการใส่และดึงของจากเครือข่าย ที่เก็บลำดับสูงจะค่อย ๆ เต็ม
และที่เก็บลำดับต่ำจะค่อย ๆ ว่าง

## Recipe

สูตรคราฟต์

<RecipeFor id="drive" />
