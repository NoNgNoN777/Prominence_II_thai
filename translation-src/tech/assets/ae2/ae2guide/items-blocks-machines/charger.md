---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Charger
  icon: charger
  position: 310
categories:
- machines
item_ids:
- ae2:charger
---

# The Charger

<BlockImage id="charger" scale="8" />

Charger ใช้ชาร์จเครื่องมือที่รองรับ
และ <ItemLink id="certus_quartz_crystal" />

รับพลังงานทางด้านบนหรือด้านล่างได้ ทั้งจาก [สาย](cables.md) ของ AE2 หรือสายพลังงานของม็อดอื่น
รับได้ทั้งพลังงาน AE2 (AE) และ Forge Energy (FE) ใส่หรือนำไอเทมออกได้ทุกด้าน
แต่ดึงออกได้เฉพาะผลผลิต จึงไม่ต้องใช้ตัวกรองป้องกันการดึง Certus Crystal ที่ยังไม่ชาร์จออกมา หมุนได้ด้วย
<ItemLink id="certus_quartz_wrench" /> เพื่อช่วยจัดระบบอัตโนมัติ

ใช้สร้าง <ItemLink id="charged_certus_quartz_crystal" />
จาก <ItemLink id="certus_quartz_crystal" /> และสร้าง <ItemLink id="meteorite_compass" /> จาก <ItemLink id="minecraft:compass" />

หากต้องการจ่ายพลังงานด้วยมือ ให้วาง <ItemLink id="crank" /> ด้านบนหรือด้านล่าง แล้วคลิกขวาจนกว่าไอเทมจะชาร์จเสร็จ

เป็นบล็อกอาชีพของชาวบ้าน AE2 ด้วย

## Simple Automation

ระบบอัตโนมัติอย่างง่าย

ตัวอย่างเช่น ความสามารถในการหมุนทำให้จัด Charger แบบกึ่งอัตโนมัติได้ดังนี้:

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/charger_hopper.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Recipe

สูตรคราฟต์

<RecipeFor id="charger" />
