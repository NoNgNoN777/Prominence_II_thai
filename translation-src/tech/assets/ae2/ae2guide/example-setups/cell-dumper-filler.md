---
navigation:
  parent: example-setups/example-setups-index.md
  title: ระบบถ่ายของเข้าออก Cell
  icon: io_port
---

# Cell Dumper Or Filler

ระบบถ่ายของเข้าออก Cell

คุณอาจสงสัยว่า "จะถ่ายของใน Cell ลงหีบ ชุดลิ้นชัก หรือกระเป๋าอย่างรวดเร็ว หรือเติมของจากที่เหล่านั้นเข้า Cell ได้อย่างไร?"

คำตอบคือใช้ <ItemLink id="io_port" /> และเครือข่ายย่อยเพื่อจำกัดว่าจะให้วางไอเทมที่ใด หรือดึงไอเทมจากที่ใด

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/cell_dumper_filler.snbt" />

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 1">
        (1) IO Port: ตั้งเป็น "ถ่ายข้อมูลเข้าเครือข่าย" หรือ "ถ่ายข้อมูลเข้า Storage Cell" ได้ด้วยปุ่มลูกศร
        กลางหน้าจอ มี Acceleration Card 3 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0.7 0" max="1 1 1">
        (2) Storage Bus: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#33dd33" min="0 1 0" max="1 2 1">
        วางสิ่งที่ต้องการเติมหรือถ่ายของออกที่นี่
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0.35 0.35" max="2.3 0.65 0.65">
        Quartz Fiber: จำเป็นเฉพาะเมื่อใช้เครือข่ายอื่นเป็นแหล่งพลังงาน
  </BoxAnnotation>

<DiamondAnnotation pos="3 0.5 0.5" color="#00ff00">
        ไปยังแหล่งพลังงาน เช่น เครือข่ายอื่น หรือ Energy Acceptor
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="io_port" /> (1) ตั้งเป็น "ถ่ายข้อมูลเข้าเครือข่าย" หรือ "ถ่ายข้อมูลเข้า Storage Cell" ได้ด้วยปุ่มลูกศร
  กลางหน้าจอ มี Acceleration Card 3 ใบเพื่อให้เร็วที่สุด
* <ItemLink id="storage_bus" /> (2) ใช้การตั้งค่าเริ่มต้น

## How It Works

หลักการทำงาน

### In "Transfer To Network" Mode

ในโหมด "ถ่ายเข้าเครือข่าย"

1. <ItemLink id="io_port" /> พยายามถ่ายของใน [Storage Cell](../items-blocks-machines/storage_cells.md) ที่ใส่ไว้
    เข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
2. ที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="storage_bus" /> ซึ่งเก็บไอเทม ของเหลว หรือสิ่งอื่นลงในภาชนะ
    ที่คุณวางไว้ด้านหน้า
* <ItemLink id="energy_cell" /> เป็นที่พัก [พลังงาน](../ae2-mechanics/energy.md) ที่มากพอให้เครือข่าย
    ไม่หมดพลังงานจากการถ่ายโอนไอเทมปริมาณมากต่อหนึ่ง tick ของเกม

### In "Transfer To Storage Cell" Mode

ในโหมด "ถ่ายเข้า Storage Cell"

1. <ItemLink id="io_port" /> พยายามถ่ายของใน [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
   เข้า [Storage Cell](../items-blocks-machines/storage_cells.md) ที่ใส่ไว้
2. ที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="storage_bus" /> ซึ่งดึงไอเทม ของเหลว หรือสิ่งอื่นออกจากภาชนะ
   ที่คุณวางไว้ด้านหน้า
* <ItemLink id="energy_cell" /> เป็นที่พัก [พลังงาน](../ae2-mechanics/energy.md) ที่มากพอให้เครือข่าย
  ไม่หมดพลังงานจากการถ่ายโอนไอเทมปริมาณมากต่อหนึ่ง tick ของเกม