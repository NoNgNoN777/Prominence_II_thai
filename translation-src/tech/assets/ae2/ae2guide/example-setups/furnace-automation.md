---
navigation:
  parent: example-setups/example-setups-index.md
  title: Furnace อัตโนมัติ
  icon: minecraft:furnace
---

# Furnace Automation

Furnace อัตโนมัติ

โปรดทราบว่าระบบนี้ใช้ <ItemLink id="pattern_provider" /> จึงออกแบบให้รวมเข้ากับระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
ของคุณ หากต้องการให้ Furnace ทำงานอัตโนมัติแยกเดี่ยว ใช้ Hopper หีบ หรืออุปกรณ์ทั่วไปได้

ทำให้ <ItemLink id="minecraft:furnace" /> อัตโนมัติซับซ้อนกว่าเครื่องง่าย ๆ อย่าง [Charger](../example-setups/charger-automation.md) เล็กน้อย
Furnace ต้องรับของจากสองด้านและดึงผลผลิตออกด้านที่สาม ต้องส่งไอเทมที่จะเผาเข้าด้านบน
ส่งเชื้อเพลิงเข้าด้านข้าง และดึงผลผลิตออกด้านล่าง

ทำได้โดยใช้ <ItemLink id="pattern_provider" />
ด้านบน <ItemLink id="export_bus" /> ด้านข้างสำหรับเติมเชื้อเพลิงต่อเนื่อง และ <ItemLink id="import_bus" />
ด้านล่างสำหรับนำผลผลิตเข้าเครือข่าย แต่แบบนี้ใช้ 3 [ช่องสัญญาณ](../ae2-mechanics/channels.md)

วิธีต่อไปนี้ใช้เพียง 1 ช่องสัญญาณ:

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/furnace_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Pattern Provider: รุ่นกำหนดทิศทางด้วย Certus Quartz Wrench พร้อมแพตเทิร์นแปรรูปที่เกี่ยวข้อง

        ![Iron Pattern](../assets/diagrams/furnace_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (2) Interface: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
        (3) Storage Bus #1: กรองเฉพาะ Coal
        <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
        (4) Storage Bus #2: ใช้ Inverter Card ตั้งตัวกรองให้ปฏิเสธ Coal
        <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="pattern_provider" /> (1) ใช้การตั้งค่าเริ่มต้น พร้อม <ItemLink id="processing_pattern" /> ที่เกี่ยวข้อง
    กำหนดทิศทางได้โดยใช้ <ItemLink id="certus_quartz_wrench" /> กับเครื่อง

  ![Iron Pattern](../assets/diagrams/furnace_pattern.png)

* <ItemLink id="interface" /> (2) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="storage_bus" /> ตัวแรก (3) กรองเฉพาะ Coal หรือเชื้อเพลิงที่ต้องการใช้
* <ItemLink id="storage_bus" /> ตัวที่สอง (4) ใช้ <ItemLink id="inverter_card" /> ตั้งตัวกรองให้ปฏิเสธเชื้อเพลิงที่คุณใช้

## How It Works

หลักการทำงาน

1. <ItemLink id="pattern_provider" /> ส่งวัตถุดิบเข้า <ItemLink id="interface" />
   (จริง ๆ แล้ว เพื่อเพิ่มประสิทธิภาพ มันส่งผ่าน Storage Bus โดยตรงเหมือนเป็นส่วนต่อขยายของด้าน Provider ไอเทมไม่ได้เข้า Interface เลย)
2. Interface ถูกตั้งไม่ให้เก็บอะไร จึงพยายามส่งวัตถุดิบเข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
3. ที่เก็บเดียวบนเครือข่ายย่อยสีเขียวคือ <ItemLink id="storage_bus" /> ตัวที่กรอง Coal จะใส่ Coal เข้าช่องเชื้อเพลิงของ Furnace ผ่านด้านข้าง
    ตัวที่กรองให้ไม่รับ Coal จะใส่ไอเทมที่จะเผาเข้าช่องด้านบน ผ่านด้านบน
4. Furnace ทำหน้าที่เผา
5. Hopper ดึงผลผลิตออกด้านล่าง Furnace แล้วใส่ช่องรับคืนของ Provider เพื่อส่งกลับเครือข่ายหลัก
