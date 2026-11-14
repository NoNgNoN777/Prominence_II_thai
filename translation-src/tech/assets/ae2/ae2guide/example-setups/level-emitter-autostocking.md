---
navigation:
  parent: example-setups/example-setups-index.md
  title: เติมสต็อกอัตโนมัติด้วย Level Emitter
  icon: level_emitter
---

# Level Emitter Autostocking

เติมสต็อกอัตโนมัติด้วย Level Emitter

คุณอาจสงสัยว่า "จะเก็บไอเทมชนิดหนึ่งตามจำนวนที่กำหนด และคราฟต์เพิ่มเมื่อจำเป็นได้อย่างไร?"

วิธีหนึ่งคือใช้ <ItemLink id="export_bus" />, <ItemLink id="level_emitter" /> และ <ItemLink id="crafting_card" /> เพื่อขอไอเทมใหม่โดยอัตโนมัติ
จากระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) ของเครือข่าย ระบบนี้เหมาะกับการรักษาสต็อกไอเทมชนิดเดียวปริมาณมาก

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/level_emitter_autostocking.snbt" />

  <BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (1) Export Bus: กรองเฉพาะไอเทมที่ต้องการ มี Redstone Card และ Crafting Card ตั้งโหมดเรดสโตนเป็น
        "ทำงานเมื่อมีสัญญาณ" และพฤติกรรมการคราฟต์เป็น "ไม่ใช้ไอเทมในสต็อก"
        <Row><ItemImage id="redstone_card" scale="2" /> <ItemImage id="crafting_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0.7 1 0" max="1 2 1">
        (2) Level Emitter: ตั้งไอเทมและจำนวนที่ต้องการ และเลือก "ส่งสัญญาณเมื่อระดับต่ำกว่าเกณฑ์"
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (3) Interface: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="export_bus" /> (1) กรองเฉพาะไอเทมที่ต้องการ มี <ItemLink id="redstone_card" /> และ <ItemLink id="crafting_card" />
  ตั้ง "โหมดเรดสโตน" เป็น "ทำงานเมื่อมีสัญญาณ" และ "พฤติกรรมการคราฟต์" เป็น "ไม่ใช้ไอเทมในสต็อก"
* <ItemLink id="level_emitter" /> (2) ตั้งไอเทมและจำนวนที่ต้องการ และเลือก "ส่งสัญญาณเมื่อระดับต่ำกว่าเกณฑ์"
* <ItemLink id="interface" /> (3) ใช้การตั้งค่าเริ่มต้น

## How It Works

หลักการทำงาน

1. หากจำนวนไอเทมที่ต้องการใน [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ต่ำกว่าค่าที่ระบุใน
   <ItemLink id="level_emitter" /> เครื่องจะส่งสัญญาณเรดสโตน
2. เมื่อได้รับสัญญาณเรดสโตน (ประกอบกับมี <ItemLink id="crafting_card" /> และตั้งไม่ให้ใช้ของในสต็อก)
   <ItemLink id="export_bus" /> จะขอให้ระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) ของเครือข่ายคราฟต์
   ไอเทมที่ต้องการเพิ่ม แล้วส่งออก
3. เมื่อมีไอเทมถูกส่งเข้ามา (และไม่ได้ตั้งให้เก็บของใดในช่องภายใน) <ItemLink id="interface" /> จะส่งไอเทมนั้นเข้าที่เก็บของเครือข่าย