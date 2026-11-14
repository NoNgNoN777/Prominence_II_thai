---
navigation:
  parent: example-setups/example-setups-index.md
  title: Charger อัตโนมัติ
  icon: charger
---

# Charger Automation

Charger อัตโนมัติ

โปรดทราบว่าระบบนี้ใช้ <ItemLink id="pattern_provider" /> จึงออกแบบให้รวมเข้ากับระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
ของคุณ หากต้องการให้ <ItemLink id="charger" /> ทำงานอัตโนมัติแยกเดี่ยว ใช้ Hopper หีบ หรืออุปกรณ์ทั่วไปได้

ทำให้ <ItemLink id="charger" /> อัตโนมัติได้ค่อนข้างง่าย <ItemLink id="pattern_provider" /> ส่งวัตถุดิบเข้าเครื่อง แล้ว [เครือข่ายย่อยแบบท่อ](pipe-subnet.md)
หรือท่อไอเทมอื่นส่งผลผลิตกลับเข้า Provider

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/charger_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Pattern Provider: ใช้การตั้งค่าเริ่มต้น พร้อมแพตเทิร์นแปรรูปที่เกี่ยวข้อง และจ่ายพลังงานให้ Charger ด้วย

        ![Charger Pattern](../assets/diagrams/charger_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="1 1.3 1">
        (2) Import Bus: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (3) Storage Bus: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="pattern_provider" /> (1) ใช้การตั้งค่าเริ่มต้น พร้อม <ItemLink id="processing_pattern" /> ที่เกี่ยวข้อง
  และจ่าย [พลังงาน](../ae2-mechanics/energy.md) ให้ <ItemLink id="charger" /> ด้วย เพราะทำงานเหมือน [สายเคเบิล](../items-blocks-machines/cables.md)
  
    ![Charger Pattern](../assets/diagrams/charger_pattern.png)

* <ItemLink id="import_bus" /> (2) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="storage_bus" /> (3) ใช้การตั้งค่าเริ่มต้น

## How It Works

หลักการทำงาน

1. <ItemLink id="pattern_provider" /> ส่งวัตถุดิบเข้า <ItemLink id="charger" />
2. Charger ทำหน้าที่ชาร์จ
3. <ItemLink id="import_bus" /> บนเครือข่ายย่อยสีเขียวดึงผลผลิตจาก Charger และพยายามเก็บไว้ใน
   [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
4. ที่เก็บเดียวบนเครือข่ายย่อยสีเขียวคือ <ItemLink id="storage_bus" /> ซึ่งเก็บผลผลิตลง Pattern Provider ส่งกลับเข้าเครือข่ายหลัก
