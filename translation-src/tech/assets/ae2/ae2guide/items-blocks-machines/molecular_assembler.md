---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Molecular Assembler
  icon: molecular_assembler
  position: 310
categories:
- machines
item_ids:
- ae2:molecular_assembler
---

# The Molecular Assembler

<BlockImage id="molecular_assembler" scale="8" />

Molecular Assembler รับไอเทมเข้ามาแล้วทำงานตามที่ <ItemLink id="pattern_provider" /> ที่อยู่ติดกันกำหนด
หรือทำตาม <ItemLink id="crafting_pattern" />, <ItemLink id="smithing_table_pattern" /> หรือ <ItemLink id="stonecutting_pattern" /> ที่ใส่ไว้
จากนั้นส่งผลผลิตเข้าสู่ช่องเก็บของที่อยู่ติดกัน

Assembler นี้มีแพตเทิร์นคราฟต์สูตร Oak Log 1 ชิ้น = Oak Planks 4 ชิ้น เมื่อป้อน Oak Log ลง Hopper ด้านบน
เครื่องจะคราฟต์แล้วส่ง Oak Planks ลง Hopper ด้านล่าง

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/standalone_assembler.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## The Main Use Of The Molecular Assembler

การใช้งานหลักของ Molecular Assembler

อย่างไรก็ตาม การใช้งานหลักคือวางข้าง <ItemLink id="pattern_provider" /> ซึ่งจะทำงานแบบพิเศษในกรณีนี้
โดยส่งข้อมูลแพตเทิร์นพร้อมวัตถุดิบให้ Assembler ที่อยู่ติดกัน เนื่องจาก Assembler ส่งผลผลิตจากการคราฟต์
เข้าช่องเก็บของข้างเคียงอัตโนมัติ (จึงเข้าช่องรับกลับของ Pattern Provider ได้) เพียงติด Assembler ข้าง Pattern Provider
ก็ทำให้แพตเทิร์นคราฟต์ทำงานอัตโนมัติได้แล้ว

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Upgrades

อัปเกรด

Molecular Assembler รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="speed_card" />

## Recipe

สูตรคราฟต์

<RecipeFor id="molecular_assembler" />

## Note

ข้อควรทราบ

Optifine ทำให้ฟังก์ชัน "ส่งเข้าช่องเก็บของข้างเคียง" เสีย ระบบคราฟต์ส่วนใหญ่ที่ใช้ Assembler จึงทำงานไม่ได้