---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Formation Plane
  icon: formation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:formation_plane
---

# The Formation Plane

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/formation_plane.snbt" />
</GameScene>

Formation Plane วางบล็อกและปล่อยไอเทม ทำงานคล้าย <ItemLink id="storage_bus" /> ที่รับเข้าได้อย่างเดียว
โดยวางหรือปล่อยเมื่อสิ่งของถูก "เก็บ" เข้าไปผ่าน [อุปกรณ์](../ae2-mechanics/devices.md) ที่ใส่ของเข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
เช่น <ItemLink id="import_bus" /> และ <ItemLink id="interface" />

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/formation_plane_demonstration.snbt" />
  <IsometricCamera yaw="255" pitch="30" />
</GameScene>

[อุปกรณ์](../ae2-mechanics/devices.md) นี้ใช้กลไกเดียวกับ Storage Bus ในระบบอย่าง [เครือข่ายย่อยแบบท่อ](../example-setups/pipe-subnet.md)
และแทน Storage Bus ในระบบเหล่านั้นได้ หากต้องการปล่อยไอเทมหรือวางบล็อกแทนการขนส่งไอเทม

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

**อย่าลืมอนุญาต FAKE PLAYER ในพื้นที่เคลมชังก์ของคุณ**

## Filtering

การกรอง

ค่าเริ่มต้น Plane จะวางหรือปล่อยทุกอย่าง ไอเทมในช่องกรองจะเป็นรายการอนุญาต
ให้วางได้เฉพาะไอเทมที่กำหนดไว้

ลากไอเทมและของเหลวจาก JEI/REI มาใส่ช่องได้ แม้คุณจะไม่มีไอเทมนั้นอยู่จริง

คลิกขวาด้วยภาชนะของเหลว (เช่น Bucket หรือถังของเหลว) เพื่อกำหนดของเหลวนั้นเป็นตัวกรอง แทนที่จะกรองตัวไอเทมภาชนะ

## Priority

ลำดับความสำคัญ

ตั้งลำดับความสำคัญได้โดยคลิกประแจมุมขวาบนของหน้าจอ
ไอเทมที่เข้าสู่เครือข่ายจะเริ่มจากที่เก็บลำดับสูงสุด

## Settings

การตั้งค่า

*   ตั้ง Plane ให้วางบล็อกในโลกหรือปล่อยไอเทมได้

## Upgrades

อัปเกรด

Formation Plane รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="capacity_card" /> เพิ่มจำนวนช่องกรอง
*   <ItemLink id="fuzzy_card" /> ให้ Plane กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="inverter_card" /> เปลี่ยนจากรายการอนุญาตเป็นรายการปฏิเสธ

## Recipe

สูตรคราฟต์

<RecipeFor id="formation_plane" />
