---
navigation:
  parent: example-setups/example-setups-index.md
  title: เติมสต็อกอัตโนมัติด้วย Interface
  icon: interface
---

# Interface Autostocking

เติมสต็อกอัตโนมัติด้วย Interface

คุณอาจสงสัยว่า "จะเก็บไอเทมหลายชนิดตามจำนวนที่กำหนด และคราฟต์เพิ่มเมื่อจำเป็นได้อย่างไร?"

วิธีหนึ่งคือใช้ <ItemLink id="interface" /> กับ <ItemLink id="crafting_card" /> เพื่อขอไอเทมใหม่โดยอัตโนมัติ
จากระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) ของเครือข่าย ระบบนี้เหมาะกับการรักษาสต็อกปริมาณน้อยของ
ไอเทมหลากหลายชนิด

ตัวอย่างนี้ตัดให้สั้นเพื่อไม่ให้กว้างเกินไป แบบที่คุ้มที่สุดน่าจะใช้ <ItemLink id="interface" /> 4 ตัวกับ <ItemLink id="storage_bus" /> 4 ตัว
เพื่อใช้ [ช่องสัญญาณ](../ae2-mechanics/channels.md) ทั้ง 8 ช่องใน [สายเคเบิล](../items-blocks-machines/cables.md) ปกติ

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_autostocking.snbt" />

<BoxAnnotation color="#dddddd" min="0 0 0" max="2 1 1">
        (1) Interface: ตั้งให้เก็บไอเทมที่ต้องการไว้ภายใน และมี Crafting Card
        <ItemImage id="crafting_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 0" max="2 1.3 1">
        (2) Storage Bus: ตั้ง "โหมดขาเข้า/ขาออก" เป็น "ดึงออกเท่านั้น"
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="interface" /> (1) ตั้งให้เก็บไอเทมที่ต้องการไว้ภายใน โดยคลิกไอเทมที่ต้องการลงใน
   ช่องด้านบน หรือลากจาก JEI ลงช่องด้านบน จากนั้นคลิกไอคอน Wrench เหนือช่องเพื่อตั้งจำนวน และใส่ <ItemLink id="crafting_card" />
* <ItemLink id="storage_bus" /> (2) ตั้ง "โหมดขาเข้า/ขาออก" เป็น "ดึงออกเท่านั้น"

## How It Works

หลักการทำงาน

1. หาก <ItemLink id="interface" /> ดึงไอเทมที่ตั้งไว้จาก [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ได้ไม่พอ
   (และมี <ItemLink id="crafting_card" />) จะขอให้ระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) ของเครือข่ายคราฟต์ไอเทมนั้นเพิ่ม
2. <ItemLink id="storage_bus" /> เปิดให้เครือข่ายเข้าถึงของภายใน Interface