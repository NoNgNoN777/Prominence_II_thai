---
navigation:
  parent: example-setups/example-setups-index.md
  title: ฟาร์ม Certus กึ่งอัตโนมัติ
  icon: certus_quartz_crystal
  position: 115
---

# Semi-Auto Certus Farm

ฟาร์ม Certus กึ่งอัตโนมัติ

น่าเสียดายที่ [ฟาร์ม Certus แบบง่าย](simple-certus-farm.md) ต้องใช้ <ItemLink id="flawless_budding_quartz" /> จึงจะทำงาน
อัตโนมัติเต็มรูปแบบได้ ซึ่งต้องใช้ [Spatial IO](../ae2-mechanics/spatial-io.md) หรือสร้างฟาร์มที่ [อุกกาบาต](../ae2-mechanics/meteorites.md)

แต่ AE2 วางและทุบบล็อกได้ จึงอาจ
ทำให้ฟาร์ม เปลี่ยน Budding Certus ให้คุณได้ (คุณต้องคอยใส่
<ItemLink id="flawed_budding_quartz" /> ในถังขาเข้า และดึง <ItemLink id="quartz_block" /> ออกจากถังบล็อก
Budding Certus ที่ใช้หมดเป็นระยะ)

หากต้องการอัตโนมัติเต็มรูปแบบ ดู [ฟาร์ม Certus ขั้นสูง](advanced-certus-farm.md)

ฟาร์มนี้ซับซ้อนกว่า [ฟาร์ม Certus แบบง่าย](simple-certus-farm.md) เล็กน้อย เพราะจริง ๆ คือ
ระบบแยกกัน 3 ชุดที่ยัดรวมไว้ด้วยกัน

โครงสร้างนี้ซับซ้อนและมีบางส่วนถูกบังอยู่ ให้หมุนมุมมองเพื่อตรวจดูจากทุกด้าน

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/semiauto_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) Annihilation Plane #1: ไม่มีหน้าจอตั้งค่า แต่เสริม Fortune ได้
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1" max="2.3 3 2">
        (2) Storage Bus #1: กรองเฉพาะ Certus Quartz Crystal
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    เครือข่ายย่อยทุบกลุ่มผลึก
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) Annihilation Plane #2: ไม่มีหน้าจอตั้งค่า แต่เสริม Silk Touch ไว้
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1" max="2.3 2 2">
        (4) Storage Bus #2: กรองเฉพาะ Certus Quartz Block
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    เครือข่ายย่อยทุบบล็อก Certus
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) Formation Plane: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0 1" max="2.3 1 2">
        (6) Import Bus: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    เครือข่ายย่อยวางบล็อกเพาะผลึก
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="0.7 2 1" max="1 3 2">
        (7) Storage Bus #3: กรองเฉพาะ Certus Quartz Crystal ตั้งลำดับความสำคัญสูงกว่าที่เก็บหลัก
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

    <DiamondAnnotation pos="1.5 0.5 1.5" color="#00ff00">
        ใส่ Flawed Budding Certus Quartz ด้วยมือ
        <BlockImage id="flawed_budding_quartz" scale="2" />
    </DiamondAnnotation>

    <DiamondAnnotation pos="1.5 1.5 1.5" color="#00ff00">
        ดึง Certus Quartz Block ออกด้วยมือ
        <BlockImage id="quartz_block" scale="2" />
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="165" pitch="5" />
</GameScene>

## Configurations

การตั้งค่า

### Cluster Breaker:

ระบบทุบกลุ่มผลึก:

* <ItemLink id="annihilation_plane" /> ตัวแรก (1) ไม่มีหน้าจอและตั้งค่าไม่ได้ แต่เสริม Fortune ได้
* <ItemLink id="storage_bus" /> ตัวแรก (2) กรองเฉพาะ <ItemLink id="certus_quartz_crystal" />

### Certus Block Breaker:

ระบบทุบบล็อก Certus:

* <ItemLink id="annihilation_plane" /> ตัวที่สอง (3) ไม่มีหน้าจอและตั้งค่าไม่ได้ แต่ต้องเสริม Silk Touch
* <ItemLink id="storage_bus" /> ตัวที่สอง (4) กรองเฉพาะ <ItemLink id="quartz_block" />

### Budding Block Placer:

ระบบวางบล็อกเพาะผลึก:

* <ItemLink id="formation_plane" /> (5) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="import_bus" /> (6) ใช้การตั้งค่าเริ่มต้น

### On Main Network:

บนเครือข่ายหลัก:

* <ItemLink id="storage_bus" /> ตัวที่สาม (7) กรองเฉพาะ <ItemLink id="certus_quartz_crystal" /> และตั้ง
  [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงกว่าที่เก็บหลัก

## How It Works

หลักการทำงาน

### Cluster Breaker:

ระบบทุบกลุ่มผลึก:

เครือข่ายย่อยทุบกลุ่มผลึกทำงานคล้ายกับเครือข่ายย่อยใน [ฟาร์ม Certus แบบง่าย](simple-certus-farm.md) มาก

1. <ItemLink id="annihilation_plane" /> พยายามทุบสิ่งที่อยู่ด้านหน้า แต่ทุบได้เฉพาะ <ItemLink id="quartz_cluster" />
   เพราะที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="storage_bus" /> ที่กรองเฉพาะ <ItemLink id="certus_quartz_crystal" />
2. <ItemLink id="storage_bus" /> เก็บ Certus Quartz Crystal ลงถัง

### Certus Block Breaker

ระบบทุบบล็อก Certus

เครือข่ายย่อยทุบบล็อก Certus มีหน้าที่ทุบบล็อกเพาะผลึกที่ใช้หมดแล้ว เมื่อกลายเป็น <ItemLink id="quartz_block" /> ธรรมดา
ทำงานคล้ายระบบทุบกลุ่มผลึก

1. <ItemLink id="annihilation_plane" /> พยายามทุบสิ่งที่อยู่ด้านหน้า แต่ทุบได้เฉพาะ <ItemLink id="quartz_block" />
   เพราะที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="storage_bus" /> ที่กรองเฉพาะ <ItemLink id="quartz_block" />
   Plane ต้องมี Silk Touch เพื่อไม่ให้บล็อกเพาะผลึกเสื่อมสภาพเมื่อถูกทุบ และจะได้ไม่ทุบบล็อกก่อนเวลา
2. <ItemLink id="storage_bus" /> เก็บ Certus Quartz Block ในถังบล็อก
   Budding Certus ที่ใช้หมดแล้ว คุณต้องนำไปโยนลงน้ำพร้อม <ItemLink id="charged_certus_quartz_crystal" /> เพื่อฟื้นสภาพเอง

### Budding Block Placer

ระบบวางบล็อกเพาะผลึก

เครือข่ายย่อยวางบล็อกเพาะผลึกมีหน้าที่วาง <ItemLink id="flawed_budding_quartz" /> ใหม่เมื่อเครือข่ายทุบทำลายบล็อกเก่าที่ใช้หมดแล้ว

1. <ItemLink id="import_bus" /> นำบล็อกเพาะผลึกเข้าจากถังขาเข้า
2. ที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="formation_plane" /> ซึ่งวางบล็อกเพาะผลึก

### On the Main Network

บนเครือข่ายหลัก

* <ItemLink id="storage_bus" /> เปิดให้เครือข่ายหลัก (รวมทั้ง [Charger อัตโนมัติ](charger-automation.md)) เข้าถึง Certus Quartz Crystal ทั้งหมดในถัง โดยตั้ง
  [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงเพื่อให้ Certus Quartz Crystal ถูกนำ
  กลับไปเก็บในถังก่อนที่เก็บหลัก