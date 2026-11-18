---
navigation:
  parent: example-setups/example-setups-index.md
  title: ฟาร์ม Certus ขั้นสูง
  icon: certus_quartz_crystal
  position: 120
---

# Advanced Certus Farm

ฟาร์ม Certus ขั้นสูง

โดยพื้นฐานนี่คือ [ฟาร์ม Certus กึ่งอัตโนมัติ](semiauto-certus-farm.md) ที่รวมเข้ากับ
ระบบ ME ของคุณอย่างเต็มรูปแบบ

แทนที่จะสะสมบล็อกเพาะผลึกจำนวนมากและคอยฟื้นสภาพด้วยมือเป็นระยะ
ระบบนี้ใช้ [Charger อัตโนมัติ](charger-automation.md) และ [การโยนลงน้ำอัตโนมัติ](throw-in-water-automation.md)
เพื่อทำขั้นตอนนั้นอัตโนมัติ

โครงสร้างนี้ซับซ้อนและมีบางส่วนถูกบังอยู่ ให้หมุนมุมมองเพื่อตรวจดูจากทุกด้าน

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/advanced_certus_farm.snbt" />

  <BoxAnnotation color="#ddaaaa" min="3.7 2 1" max="4 3 2">
        (1) Annihilation Plane #1: ไม่มีหน้าจอตั้งค่า แต่เสริม Fortune ได้
  </BoxAnnotation>

  <BoxAnnotation color="#ddaaaa" min="2 2 1.7" max="3 3 2">
        (2) Storage Bus #1: กรองเฉพาะ Certus Quartz Crystal
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 2.5 1.5" color="#ff0000">
    เครือข่ายย่อยทุบกลุ่มผลึก
  </DiamondAnnotation>

  <BoxAnnotation color="#aaddaa" min="3.7 1 1" max="4 2 2">
        (3) Annihilation Plane #2: ไม่มีหน้าจอตั้งค่า แต่เสริม Silk Touch ไว้
  </BoxAnnotation>

  <BoxAnnotation color="#aaddaa" min="2 1 1.7" max="3 2 2">
        (4) Storage Bus #2: กรองเฉพาะ Certus Quartz Block
        <BlockImage id="quartz_block" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 1.5 1.5" color="#00ff00">
    เครือข่ายย่อยทุบบล็อก Certus
  </DiamondAnnotation>

  <BoxAnnotation color="#ffddaa" min="4 0.7 1" max="5 1 2">
        (5) Formation Plane: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#ffddaa" min="2 0.7 2" max="3 1 3">
        (6) Import Bus: กรองเฉพาะ Flawed Budding Certus Quartz
        <BlockImage id="flawed_budding_quartz" scale="2" />
  </BoxAnnotation>

  <DiamondAnnotation pos="3 0.5 1.5" color="#ddcc00">
    เครือข่ายย่อยวางบล็อกเพาะผลึก
  </DiamondAnnotation>

  <BoxAnnotation color="#aaaadd" min="1.7 2 2" max="2 3 3">
        (7) Storage Bus #3: กรองเฉพาะ Certus Quartz Crystal ตั้งลำดับความสำคัญสูงกว่าที่เก็บหลัก
        <ItemImage id="certus_quartz_crystal" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#aaaadd" min="2 1 2" max="3 2 3">
        (8) Interface: ตั้งให้เก็บ Flawed Budding Certus Quartz 1 บล็อกไว้ภายใน และมี Crafting Card
        <Row><BlockImage id="flawed_budding_quartz" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="1.5 0.5 0" color="#00ff00">
        ไปยังเครือข่ายหลัก Charger อัตโนมัติ และระบบโยนลงน้ำอัตโนมัติ
        <Row>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
        </Row>
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
* <ItemLink id="import_bus" /> (6) กรองเฉพาะ <ItemLink id="flawed_budding_quartz" />

### On Main Network:

บนเครือข่ายหลัก:

* <ItemLink id="storage_bus" /> ตัวที่สาม (7) กรองเฉพาะ <ItemLink id="certus_quartz_crystal" /> และตั้ง
  [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงกว่าที่เก็บหลัก
* <ItemLink id="interface" /> (8) ตั้งให้เก็บ Flawed Budding Certus Quartz 1 บล็อกไว้ภายใน และมี <ItemLink id="crafting_card" />

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
2. <ItemLink id="storage_bus" /> เก็บ Certus Quartz Block ใน <ItemLink id="interface" /> เพื่อให้
   [ระบบโยนลงน้ำอัตโนมัติ](throw-in-water-automation.md) นำไปสร้าง <ItemLink id="flawed_budding_quartz" /> บล็อกใหม่

### Budding Block Placer

ระบบวางบล็อกเพาะผลึก

เครือข่ายย่อยวางบล็อกเพาะผลึกมีหน้าที่วาง <ItemLink id="flawed_budding_quartz" /> ใหม่เมื่อเครือข่ายทุบทำลายบล็อกเก่าที่ใช้หมดแล้ว

1. <ItemLink id="import_bus" /> นำบล็อกเพาะผลึกจาก <ItemLink id="interface" /> เข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
2. ที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="formation_plane" /> ซึ่งวางบล็อกเพาะผลึก

### On the Main Network

บนเครือข่ายหลัก

* <ItemLink id="storage_bus" /> เปิดให้เครือข่ายหลัก (รวมทั้ง [Charger อัตโนมัติ](charger-automation.md)) เข้าถึง Certus Quartz Crystal ทั้งหมดในถัง โดยตั้ง
  [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงเพื่อให้ Certus Quartz Crystal ถูกนำ
  กลับไปเก็บในถังก่อนที่เก็บหลัก
* <ItemLink id="interface" /> เปิดให้เครือข่ายย่อยวางบล็อกเข้าถึง <ItemLink id="flawed_budding_quartz" /> และ
    เป็นทางให้เครือข่ายย่อยทุบบล็อกส่งบล็อกที่ใช้หมดกลับเข้าเครือข่ายหลัก ส่วน
    <ItemLink id="crafting_card" /> ให้ Interface ขอสร้างบล็อกเพาะผลึกใหม่ผ่าน [การคราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) ของเครือข่ายหลัก