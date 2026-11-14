---
navigation:
  parent: example-setups/example-setups-index.md
  title: เครื่องผลิต Cobblestone แบบควบคุมอัตโนมัติ
  icon: minecraft:cobblestone
---

# Auto-Regulated Cobblestone Generator

เครื่องผลิต Cobblestone แบบควบคุมอัตโนมัติ

ทำเครื่องผลิต Cobblestone อัตโนมัติได้ง่าย เพียงหัน <ItemLink id="annihilation_plane" /> เข้าหาเครื่องผลิต Cobblestone
แบบขุดด้วยมือของเกมหลัก แต่หากทำเช่นนี้ ในที่สุดเครือข่ายจะเต็มไปด้วย Cobblestone จึงควรมีระบบ
ควบคุมปริมาณ

เพราะ Annihilation Plane ทำงานเหมือน <ItemLink id="import_bus" /> เราจึงไม่สามารถวาง <ItemLink id="level_emitter" />
หันเข้า <ItemLink id="export_bus" /> ที่มี <ItemLink id="redstone_card" /> ได้ตรง ๆ (เพราะนำเข้าแล้วส่งออกโดยตรงไม่ได้
หากไม่มีที่เก็บคั่นกลาง) จึงต้องอ้อมเล็กน้อย

<ItemLink id="toggle_bus" /> ให้เชื่อมและตัดส่วนของเครือข่ายด้วยสัญญาณเรดสโตนได้ แต่จะทำให้
เครือข่ายเริ่มใหม่ทุกครั้งที่สลับ มีวิธีเลี่ยงง่าย ๆ คือวาง Toggle Bus บน [เครือข่ายย่อย](../ae2-mechanics/subnetworks.md)
เพื่อให้เริ่มใหม่เฉพาะเครือข่ายย่อย

ใช้ [เครือข่ายย่อย](../ae2-mechanics/subnetworks.md) แยกอิสระที่มี <ItemLink id="annihilation_plane" /> กับ <ItemLink id="storage_bus" />
ส่งของเข้า <ItemLink id="interface" /> บนเครือข่ายหลัก Toggle Bus จะเชื่อมและตัดเครือข่ายย่อยกับ
<ItemLink id="quartz_fiber" /> เพื่อตัดพลังงานที่จ่ายให้ Plane

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/regulated_cobble_gen.snbt" />

<BoxAnnotation color="#dddddd" min="3 2 2" max="7 2.3 3">
        (1) Annihilation Plane: ไม่มีหน้าจอตั้งค่า แต่เสริม Efficiency และ Unbreaking เพื่อลดการใช้พลังงานได้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 2" max="2.3 3 3">
        (2) Storage Bus: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 2.3 2" max="2.7 2.7 2.3">
        (3) Toggle Bus: สำคัญมากที่ต้องวาง Toggle Bus บน
        เครือข่ายย่อย ไม่ใช่เครือข่ายหลัก
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 2.3" max="2.7 3.3 2.7">
        (4) Level Emitter: ตั้ง Cobblestone กับจำนวนที่ต้องการ และเลือก "ส่งสัญญาณเมื่อระดับต่ำกว่าเกณฑ์"
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 3" max="2 3 2">
        (5) Interface: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<DiamondAnnotation pos="0 2.5 1.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

<DiamondAnnotation pos="5 1.5 3.5" color="#00ff00">
        บันไดที่มีน้ำขังป้องกันน้ำไหลไปเปลี่ยนลาวาเป็น Obsidian
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="annihilation_plane" /> (1) ไม่มีหน้าจอตั้งค่า แต่เสริม Efficiency และ Unbreaking เพื่อลดการใช้พลังงานได้
* <ItemLink id="storage_bus" /> (2) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="toggle_bus" /> (3) ต้องอยู่ฝั่งเครือข่ายย่อยของ Quartz Fiber ไม่ใช่เครือข่ายหลัก มิฉะนั้นเครือข่ายหลัก
  จะเริ่มใหม่ทุกครั้งที่สลับ
* <ItemLink id="level_emitter" /> (4) ตั้งไอเทมและจำนวนที่ต้องการ และเลือก "ส่งสัญญาณเมื่อระดับต่ำกว่าเกณฑ์"
* <ItemLink id="interface" /> (5) ใช้การตั้งค่าเริ่มต้น

## How It Works

หลักการทำงาน

1. เครื่องผลิต Cobblestone สร้าง Cobblestone ขึ้นมา
2. <ItemLink id="annihilation_plane" /> ทุบ Cobblestone
3. <ItemLink id="storage_bus" /> เก็บ Cobblestone ใน <ItemLink id="interface" /> ส่งเข้าเครือข่ายหลัก
4. เมื่อจำนวน Cobblestone ในเครือข่ายหลักเกินค่าที่ตั้งไว้ <ItemLink id="level_emitter" /> จะหยุด
   ส่งสัญญาณ ทำให้ <ItemLink id="toggle_bus" /> ปิด
5. การทำเช่นนี้ตัดไฟเครือข่ายย่อยและหยุด Annihilation Plane
