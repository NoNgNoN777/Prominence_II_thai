---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Vibration Chamber
  icon: vibration_chamber
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:vibration_chamber
---

# The Vibration Chamber

<BlockImage id="vibration_chamber" p:active="true" scale="8" />

แม้วิธีหลักที่ตั้งใจให้ใช้จ่าย [พลังงาน](../ae2-mechanics/energy.md) แก่เครือข่ายคือ
<ItemLink id="energy_acceptor" /> แต่ Vibration Chamber ผลิต AE ปริมาณน้อยถึงปานกลางได้โดยตรง

ค่าเริ่มต้น (ไม่มี [อัปเกรด](upgrade_cards.md) และใช้การตั้งค่าปกติ) ผลิตได้ 40 AE/t

เมื่อที่เก็บ [พลังงาน](../ae2-mechanics/energy.md) ของเครือข่ายเต็ม Vibration Chamber จะลดกำลังลงเพื่อประหยัด
เชื้อเพลิง แต่หยุดทำงานทั้งหมดไม่ได้

## Settings

การตั้งค่า

*   Vibration Chamber ให้เข้าถึงการตั้งค่าหน่วยพลังงานส่วนกลางเพื่อเลือก AE หรือ E/FE

## Upgrades

อัปเกรด

Vibration Chamber รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="energy_card" /> เพิ่มประสิทธิภาพเครื่อง +50% ต่อชิ้น สูงสุด +150% หรือ 250% ของประสิทธิภาพพื้นฐาน
*   <ItemLink id="speed_card" /> เพิ่มอัตราเผาไหม้ +50% ต่อชิ้น สูงสุด +150% หรือกำลังผลิต 250% ของค่าพื้นฐาน

## Config

การตั้งค่า

แก้คุณสมบัติ Vibration Chamber ได้ใน common.json ภายในโฟลเดอร์ ae2 ใน config ของไดเรกทอรี .minecraft\
ของคุณ

*   baseEnergyPerFuelTick กำหนดประสิทธิภาพพื้นฐานที่ยังไม่อัปเกรดของ Vibration Chamber
*   minEnergyPerGameTick กำหนดกำลังผลิตต่ำสุด (เครื่องยังค่อย ๆ ใช้เชื้อเพลิงเสมอ แม้เครือข่าย
    ไม่ต้องการพลังงาน)
*   maxEnergyPerGameTick กำหนดกำลังผลิตสูงสุด (และความเร็ว) ของเครื่องก่อนอัปเกรด

## Recipe

สูตรคราฟต์

<RecipeFor id="vibration_chamber" />
