---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME Chest
  icon: chest
  position: 210
categories:
- devices
item_ids:
- ae2:chest
---

# The ME Chest

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/chest.snbt" />
</GameScene>

ME Chest ทำงานเหมือนเครือข่ายขนาดจิ๋วที่มี <ItemLink id="terminal" />, <ItemLink id="drive" /> และ <ItemLink id="energy_acceptor" />
แม้ใช้เป็นเครือข่ายจัดเก็บเล็ก ๆ ได้ แต่การใส่ [Storage Cell](../items-blocks-machines/storage_cells.md)
ได้เพียงเซลล์เดียวทำให้มีประโยชน์ด้านนี้จำกัด

มันจึงเหมาะกับการใช้งาน Storage Cell ที่ใส่ไว้โดยเฉพาะ เทอร์มินัลในตัวเห็นและเข้าถึง
ได้เฉพาะของในเซลล์นั้น ขณะที่ [อุปกรณ์](../ae2-mechanics/devices.md) ในเครือข่ายทั่วไปเข้าถึงของใน [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ใดก็ได้
รวมถึง ME Chest

มีหน้าจอ 2 แบบและแยกด้านขนส่งไอเทม คลิกที่เทอร์มินัลด้านบนเพื่อเปิดเทอร์มินัลในตัว ใส่ไอเทมเข้า
Storage Cell ผ่านด้านนี้ได้ แต่ดึงออกไม่ได้ คลิกด้านอื่นเพื่อเปิดหน้าจอช่อง Storage Cell
และการตั้งค่าลำดับความสำคัญ ระบบขนส่งใส่และนำเซลล์ออกได้เฉพาะด้านที่มีช่องเซลล์

หมุนได้ด้วย <ItemLink id="certus_quartz_wrench" />

มีบัฟเฟอร์พลังงาน AE ขนาดเล็ก หากไม่ได้ต่อกับเครือข่ายที่มี [Energy Cell](../items-blocks-machines/energy_cells.md)
การใส่หรือดึงของมากเกินไปในครั้งเดียวอาจทำให้ไฟตก

เปลี่ยนสีเทอร์มินัลได้ด้วย <ItemLink id="color_applicator" />

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/chest_color.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Settings

การตั้งค่า

ME Chest มีการตั้งค่าเหมือน <ItemLink id="terminal" /> หรือ <ItemLink id="crafting_terminal" /> ทุกอย่าง
แต่ไม่รองรับ <ItemLink id="view_cell" />

## Cell Status LEDs

ไฟ LED แสดงสถานะเซลล์

เซลล์ในหีบมีไฟ LED แสดงสถานะ:

| สี  | สถานะ                                                                           |
| :----- | :------------------------------------------------------------------------------- |
| เขียว  | ว่างเปล่า                                                                            |
| น้ำเงิน   | มีของอยู่บางส่วน                                                                |
| ส้ม | [จำนวนชนิด](../ae2-mechanics/bytes-and-types.md) เต็ม เพิ่มชนิดใหม่ไม่ได้     |
| แดง    | [Bytes](../ae2-mechanics/bytes-and-types.md) เต็ม ใส่ไอเทมเพิ่มไม่ได้ |
| ดำ  | ไม่มีพลังงาน หรือ Drive ไม่มี [ช่องสัญญาณ](../ae2-mechanics/channels.md)                 |

## Priority

ลำดับความสำคัญ

ตั้งลำดับความสำคัญโดยคลิกประแจมุมขวาบนของหน้าจอช่องเซลล์
ไอเทมที่เข้าสู่เครือข่ายจะเลือกที่เก็บที่มีลำดับความสำคัญสูงสุดก่อน
หากที่เก็บหรือเซลล์สองแห่งมีลำดับเท่ากัน จะเลือกแห่งที่มีไอเทมชนิดนั้นอยู่แล้ว
ก่อนที่เก็บอื่น เซลล์ที่ [กำหนดชนิดไว้](cell_workbench.md) จะถือว่ามีไอเทมนั้นอยู่แล้ว
เมื่ออยู่ในกลุ่มลำดับเดียวกัน ส่วนการดึงไอเทมออกจะเริ่มจากที่เก็บที่มีลำดับต่ำสุด
ระบบนี้ทำให้เมื่อมีการใส่และดึงของจากเครือข่าย ที่เก็บลำดับสูงจะค่อย ๆ เต็ม
และที่เก็บลำดับต่ำจะค่อย ๆ ว่าง

## Recipe

สูตรคราฟต์

<RecipeFor id="chest" />
