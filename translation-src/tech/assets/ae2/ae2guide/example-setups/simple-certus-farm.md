---
navigation:
  parent: example-setups/example-setups-index.md
  title: ฟาร์ม Certus แบบง่าย
  icon: certus_quartz_crystal
  position: 110
---

# Simple Certus Farm

ฟาร์ม Certus แบบง่าย

ดังที่กล่าวใน [การเติบโตของ Certus](../ae2-mechanics/certus-growth.md) การเก็บเกี่ยว <ItemLink id="certus_quartz_crystal" />
อัตโนมัติใช้ <ItemLink id="annihilation_plane" /> และ <ItemLink id="storage_bus" />
ใช้ <ItemLink id="growth_accelerator" /> เร่งการเติบโตของหน่อ Certus Quartz อย่างมาก จากนั้น Plane
ทุบ <ItemLink id="quartz_cluster" /> ที่โตเต็มที่ อาศัยคุณสมบัติที่บังเอิญเป็นประโยชน์คือหน่อ Certus
ที่ยังไม่โตดรอป <ItemLink id="certus_quartz_dust" /> แทนที่จะไม่ดรอปอะไร จึงกรองแยกได้

ฟาร์มนี้ทำงานอัตโนมัติเต็มรูปแบบด้วย <ItemLink id="flawless_budding_quartz" /> แต่หากใช้ Budding Certus Quartz แบบ Flawed, Chipped และ Damaged
คุณต้องเปลี่ยนบล็อกเพาะผลึกเอง หรือทำแบบอัตโนมัติตามที่อธิบายใน [ฟาร์ม Certus กึ่งอัตโนมัติ](semiauto-certus-farm.md)
และ [ฟาร์ม Certus ขั้นสูง](advanced-certus-farm.md)

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/simple_certus_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="3.7 1 1" max="4 2 2">
        (1) Annihilation Plane: ไม่มีหน้าจอตั้งค่า แต่เสริม Fortune ได้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="3.3 2 2">
        (2) Storage Bus #1: กรองเฉพาะ Certus Quartz Crystal
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 .7" max="2 2 1">
        (3) Storage Bus #2: กรองเฉพาะ Certus Quartz Crystal ตั้งลำดับความสำคัญสูงกว่าที่เก็บหลัก
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="annihilation_plane" /> ตัวแรก (1) ไม่มีหน้าจอและตั้งค่าไม่ได้ แต่เสริม Fortune ได้
* <ItemLink id="storage_bus" /> ตัวแรก (2) กรองเฉพาะ <ItemLink id="certus_quartz_crystal" />
* <ItemLink id="storage_bus" /> ตัวที่สอง (3) กรองเฉพาะ <ItemLink id="certus_quartz_crystal" /> และตั้ง
  [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงกว่าที่เก็บหลัก

## How It Works

หลักการทำงาน

1. <ItemLink id="annihilation_plane" /> พยายามทุบสิ่งที่อยู่ด้านหน้า แต่ทุบได้เฉพาะ <ItemLink id="quartz_cluster" />
   เพราะที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="storage_bus" /> ที่กรองเฉพาะ <ItemLink id="certus_quartz_crystal" />
4. <ItemLink id="storage_bus" /> ตัวแรกเก็บ Certus Quartz Crystal ลงถัง
5. <ItemLink id="storage_bus" /> ตัวที่สองเปิดให้เครือข่ายหลักเข้าถึง Certus Quartz Crystal ทั้งหมดในถัง โดยตั้ง
   [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงเพื่อให้ Certus Quartz Crystal ถูกนำ
   กลับไปเก็บในถังก่อนที่เก็บหลัก
