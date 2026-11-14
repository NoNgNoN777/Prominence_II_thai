---
navigation:
  parent: example-setups/example-setups-index.md
  title: ทุบแร่ด้วย Fortune อัตโนมัติ
  icon: minecraft:raw_iron
---

# Automation of Ore Fortuning

ทุบแร่ด้วย Fortune อัตโนมัติ

<ItemLink id="annihilation_plane" /> เสริมเอนชานต์ของ Pickaxe ได้ทุกชนิด รวม Fortune จึงใช้ได้ชัดเจนโดย
เสริม Fortune ให้หลายตัว แล้วให้ <ItemLink id="formation_plane" /> และ <ItemLink id="annihilation_plane" /> วางและ
ทุบแร่อย่างรวดเร็ว

โปรดทราบว่า <ItemLink id="import_bus" /> ต้อง "เร่งจนได้ความเร็ว" ระบบจึงเริ่มช้าแล้วถึงความเร็วเต็มในไม่กี่วินาที

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/ore_fortuner.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 0 2" max="3 1 3">
        (1) Import Bus: มี Acceleration Card หลายใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 2" max="2 1 2.3">
        (2) Formation Plane: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 0.7" max="2 1 1">
        (3) Annihilation Plane: ไม่มีหน้าจอตั้งค่า แต่เสริม Fortune ไว้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 0 0" max="3 1 1">
        (4) Storage Bus: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<DiamondAnnotation pos="3.5 0.5 2.5" color="#00ff00">
        ขาเข้า
    </DiamondAnnotation>

<DiamondAnnotation pos="3.5 0.5 0.5" color="#00ff00">
        ขาออก
    </DiamondAnnotation>

<DiamondAnnotation pos="4 0.5 1.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

*   <ItemLink id="import_bus" /> (1) มี <ItemLink id="speed_card" /> หลายใบ ยิ่งมี Formation Plane
    ในชุดมากก็ยิ่งต้องใช้การ์ดเพิ่ม เพราะทำให้ Import Bus ดึงไอเทมได้ครั้งละมากขึ้น
*   <ItemLink id="formation_plane" /> (2) ใช้การตั้งค่าเริ่มต้น
*   <ItemLink id="annihilation_plane" /> (3) ไม่มีหน้าจอและตั้งค่าไม่ได้ แต่เสริม Fortune ไว้
*   <ItemLink id="storage_bus" /> (4) ใช้การตั้งค่าเริ่มต้น

## How It Works

หลักการทำงาน

1.  <ItemLink id="import_bus" /> บนเครือข่ายย่อยสีเขียวนำบล็อกจากถังแรกเข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
2.  ที่เก็บเดียวบนเครือข่ายย่อยสีเขียวคือ <ItemLink id="formation_plane" /> ซึ่งวางบล็อก
3.  <ItemLink id="annihilation_plane" /> บนเครือข่ายย่อยสีส้มทุบบล็อกพร้อมใช้ Fortune
4.  <ItemLink id="storage_bus" /> บนเครือข่ายย่อยสีส้มเก็บผลผลิตจากการทุบลงถังที่สอง
