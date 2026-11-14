---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME Import Bus
  icon: import_bus
  position: 220
categories:
- devices
item_ids:
- ae2:import_bus
---

# The Import Bus

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/import_bus.snbt" />
</GameScene>

Import Bus ดึงไอเทมและของเหลว (รวมถึงสิ่งอื่นตามม็อดเสริม) จากช่องเก็บของที่สัมผัสอยู่ แล้วส่งเข้า
[ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)

เพื่อลดอาการแลค หาก Import Bus ไม่ได้นำเข้าสิ่งใดมาระยะหนึ่ง จะเข้าสู่
"โหมดพัก" ที่ทำงานช้าลง และจะตื่นขึ้นเร่งสู่ความเร็วเต็ม (4 ครั้งต่อวินาที) เมื่อนำเข้าสำเร็จ

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

## Filtering

การกรอง

ค่าเริ่มต้นบัสจะนำเข้าทุกอย่างที่เข้าถึงได้ ไอเทมในช่องกรองทำหน้าที่เป็นรายการอนุญาต
ให้นำเข้าเฉพาะไอเทมที่ระบุไว้เท่านั้น

ลากไอเทมและของเหลวจาก JEI/REI มาใส่ช่องได้ แม้คุณจะไม่มีไอเทมนั้นอยู่จริง

คลิกขวาด้วยภาชนะของเหลว (เช่น Bucket หรือถังของเหลว) เพื่อกำหนดของเหลวนั้นเป็นตัวกรอง แทนที่จะกรองตัวไอเทมภาชนะ

## Upgrades

อัปเกรด

Import Bus รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="capacity_card" /> เพิ่มจำนวนช่องกรอง
*   <ItemLink id="speed_card" /> เพิ่มจำนวนสิ่งของที่ย้ายต่อการทำงานหนึ่งครั้ง
*   <ItemLink id="fuzzy_card" /> ให้กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="inverter_card" /> เปลี่ยนจากรายการอนุญาตเป็นรายการปฏิเสธ
*   <ItemLink id="redstone_card" /> เพิ่มการควบคุมด้วยเรดสโตน ให้ทำงานเมื่อสัญญาณสูง ต่ำ หรือหนึ่งครั้งต่อพัลส์

## Speeds

ความเร็ว

| Acceleration Card | ไอเทมที่ย้ายต่อครั้ง |
|:-------------------|:--------------------------|
| 0                  | 1                         |
| 1                  | 8                         |
| 2                  | 32                        |
| 3                  | 64                        |
| 4                  | 96                        |

## Recipe

สูตรคราฟต์

<RecipeFor id="import_bus" />
