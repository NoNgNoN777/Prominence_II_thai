---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ME Export Bus
  icon: export_bus
  position: 220
categories:
- devices
item_ids:
- ae2:export_bus
---

# The Export Bus

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/export_bus.snbt" />
</GameScene>

Export Bus ดึงไอเทมและของเหลว (รวมถึงสิ่งอื่นตามม็อดเสริม) จาก [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
แล้วส่งเข้าช่องเก็บของที่สัมผัสอยู่

เพื่อลดอาการแลค หาก Export Bus ไม่ได้ส่งออกสิ่งใดมาระยะหนึ่ง จะเข้าสู่
"โหมดพัก" ที่ทำงานช้าลง และจะตื่นขึ้นเร่งสู่ความเร็วเต็ม (4 ครั้งต่อวินาที) เมื่อส่งออกสำเร็จ

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

## Filtering

การกรอง

ค่าเริ่มต้นบัสจะไม่ส่งออกอะไร ไอเทมในช่องกรองทำหน้าที่เป็นรายการอนุญาต
ให้ส่งออกไอเทมที่ระบุไว้เท่านั้น

ลากไอเทมและของเหลวจาก JEI/REI มาใส่ช่องได้ แม้คุณจะไม่มีไอเทมนั้นอยู่จริง

คลิกขวาด้วยภาชนะของเหลว (เช่น Bucket หรือถังของเหลว) เพื่อกำหนดของเหลวนั้นเป็นตัวกรอง แทนที่จะกรองตัวไอเทมภาชนะ

## Upgrades

อัปเกรด

Import Bus รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="capacity_card" /> เพิ่มช่องกรอง และเพิ่มตัวเลือกว่าควรส่งออกสิ่งที่กรองไว้ตามลำดับใด
*   <ItemLink id="speed_card" /> เพิ่มจำนวนสิ่งของที่ย้ายต่อการทำงานหนึ่งครั้ง
*   <ItemLink id="fuzzy_card" /> ให้กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="crafting_card" /> ให้บัสส่งคำขอคราฟต์ไปยังระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
    เพื่อรับไอเทมที่ต้องการ ตั้งให้ดึงจากที่เก็บก่อนหากมี หรือส่งคำขอ
    คราฟต์ไอเทมใหม่ทุกครั้งก็ได้
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
