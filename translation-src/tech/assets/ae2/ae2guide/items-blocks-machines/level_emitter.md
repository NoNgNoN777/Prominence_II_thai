---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Level Emitter
  icon: level_emitter
  position: 220
categories:
- devices
item_ids:
- ae2:level_emitter
- ae2:energy_level_emitter
---

# The Level Emitter

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/level_emitter.snbt" />
</GameScene>

Level Emitter ส่งสัญญาณเรดสโตนตามจำนวนไอเทมใน
[ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)

มีอีกรุ่นที่ส่งสัญญาณเรดสโตนตาม [พลังงาน](../ae2-mechanics/energy.md) ที่เก็บ
ในเครือข่ายของคุณ

ลากไอเทมและของเหลวจาก JEI/REI มาใส่ช่องได้ แม้คุณจะไม่มีไอเทมนั้นอยู่จริง

คลิกขวาด้วยภาชนะของเหลว (เช่น Bucket หรือถังของเหลว) เพื่อกำหนดของเหลวนั้นเป็นตัวกรอง แทนที่จะกรองตัวไอเทมภาชนะ

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

ต่างจาก [อุปกรณ์](../ae2-mechanics/devices.md) อื่น Level Emitter ไม่ต้อง ใช้ [ช่องสัญญาณ](../ae2-mechanics/channels.md)

## Settings

การตั้งค่า

*   ตั้ง Level Emitter เป็นโหมด "มากกว่าหรือเท่ากับ" หรือ "น้อยกว่า" ได้
*   เมื่อใส่ <ItemLink id="crafting_card" /> จะตั้งเป็น "ส่งเรดสโตนขณะคราฟต์ไอเทม" หรือ
    "ส่งเรดสโตนเพื่อคราฟต์ไอเทม" ได้

## Upgrades

อัปเกรด

Level Emitter รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="fuzzy_card" /> ให้กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="crafting_card" /> เปิดใช้ความสามารถด้านการคราฟต์

## Crafting Functionality

ความสามารถด้านการคราฟต์

เมื่อใส่ <ItemLink id="crafting_card" /> ตัวส่งสัญญาณจะเปลี่ยนเป็นโหมดคราฟต์

โหมดนี้เปิดให้เลือกได้สองแบบ:

แบบแรก "ส่งเรดสโตนขณะคราฟต์ไอเทม" ทำให้ตัวส่งสัญญาณปล่อยเรดสโตนขณะที่ระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
กำลังคราฟต์ไอเทมที่ระบุผ่าน <ItemLink id="pattern_provider" /> เหมาะสำหรับเปิดระบบอัตโนมัติ
ที่กินพลังงานสูงเฉพาะตอนที่ใช้งานจริง

แบบที่สอง "ส่งเรดสโตนเพื่อคราฟต์ไอเทม" มีประโยชน์มากกับงานเฉพาะ เช่น ฟาร์มไม่สิ้นสุด
และระบบอัตโนมัติที่มีเพียงโอกาสได้ผลผลิต แทนที่จะได้แน่นอนทุกครั้ง
การตั้งค่านี้สร้าง [แพตเทิร์น](patterns.md) เสมือนสำหรับให้ระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) ใช้ โดยอ้างอิงไอเทม
ในช่องกรองของตัวส่งสัญญาณ
(เพื่อให้ทำงานถูกต้อง ไม่ควรมี แพตเทิร์นจริงสำหรับไอเทมเดียวกันใน <ItemLink id="pattern_provider" />)

"แพตเทิร์น" นี้ไม่กำหนดหรือสนใจวัตถุดิบเลย
มันเพียงบอกว่า "หากส่งเรดสโตนจาก Level Emitter นี้ ระบบ ME จะได้รับไอเทมนี้ในอนาคต
อันใกล้หรือไกล" มักใช้เปิดและปิดฟาร์มไม่สิ้นสุดที่ไม่ต้องใช้วัตถุดิบ
หรือเปิดระบบจัดการสูตรวนซ้ำ (ที่การคราฟต์อัตโนมัติปกติไม่เข้าใจ) เช่น "Cobblestone 1 = Cobblestone 2"
หากคุณมีเครื่องจักรที่เพิ่มจำนวน Cobblestone ได้

## Recipe

สูตรคราฟต์

<RecipeFor id="level_emitter" />

<RecipeFor id="energy_level_emitter" />
