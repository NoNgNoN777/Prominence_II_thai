---
navigation:
  parent: example-setups/example-setups-index.md
  title: ที่เก็บเฉพาะของแต่ละพื้นที่
  icon: drive
---

# Specialized Local Storage

ที่เก็บเฉพาะของแต่ละพื้นที่

ใช้หนึ่งใน [พฤติกรรมพิเศษของ Interface](../items-blocks-machines/interface.md#special-interactions) เพื่อให้
[เครือข่ายย่อย](../ae2-mechanics/subnetworks.md) แสดงของในที่เก็บให้เครือข่ายหลักเข้าถึง โดยไม่สามารถ
มองเห็นที่เก็บของเครือข่ายหลัก และใช้เพียง 1 [ช่องสัญญาณ](../ae2-mechanics/channels.md)

มีประโยชน์สำหรับที่เก็บประจำฟาร์ม เพื่อไม่ให้ไอเทมล้นเข้าไปยังที่เก็บหลัก

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/local_storage.snbt" />

<BoxAnnotation color="#dddddd" min="4 0 0" max="5 2 1">
        (1) วิธีนำไอเทมเข้าระบบชนิดใดก็ได้ (ในตัวอย่างนี้ใช้ Interface)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 0 0" max="4 1 1">
        (2) Drive: มี Cell อยู่ภายใน ควรตั้งตัวกรอง Cell ให้ตรงกับผลผลิตของฟาร์ม
        Cell มี Equal Distribution Card และ Overflow Destruction Card ได้
        <Row><ItemImage id="item_storage_cell_4k" scale="2" /> <ItemImage id="equal_distribution_card" scale="2" /> <ItemImage id="void_card" scale="2" /></Row>
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3 1 0" max="4 2 0.3">
        (3) Crafting Terminal: มองเห็นของใน Drive บนเครือข่ายย่อย แต่ไม่เห็นของในที่เก็บของเครือข่ายหลัก
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 0" max="2.3 1 1">
        (4) Interface #2: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 0" max="2 1 1">
        (5) Storage Bus: ตั้งลำดับความสำคัญสูงกว่าที่เก็บหลัก กรองให้ตรงกับผลผลิตของฟาร์มได้
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 2 0.3">
        Crafting Terminal: มองเห็นทั้งของในที่เก็บของเครือข่ายหลัก และ เครือข่ายย่อย
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="interface" /> ตัวแรก (1) รับไอเทมจากฟาร์มที่คุณมี แล้วส่งเข้าเครือข่ายย่อย
* <ItemLink id="drive" /> (2) มี [Cell](../items-blocks-machines/storage_cells.md) อยู่ภายใน ควรตั้ง
  [การแบ่งประเภท](../items-blocks-machines/cell_workbench.md) ให้ตรงกับผลผลิตของฟาร์ม
  Cell มี <ItemLink id="equal_distribution_card" /> และ <ItemLink id="void_card" /> ได้
* <ItemLink id="interface" /> ตัวที่สอง (4) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="storage_bus" /> ตั้ง [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority)
  สูงกว่าที่เก็บหลัก และตั้งตัวกรองให้ตรงกับผลผลิตของฟาร์มได้

## How It Works

หลักการทำงาน

* <ItemLink id="interface" /> บนเครือข่ายย่อยแสดงเนื้อหาของ
<ItemLink id="drive" /> ให้ <ItemLink id="storage_bus" /> บนเครือข่ายหลักเห็น จึงดึงไอเทมออกจากและส่งเข้า Cell ใน Drive ได้โดยตรง
* Storage Bus ตั้ง [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงเพื่อให้ไอเทมถูกนำ
  กลับไปเก็บในเครือข่ายย่อยก่อนที่เก็บหลัก
* ที่สำคัญ หาก Cell ในเครือข่ายย่อยเต็ม ไอเทมจะไม่ล้นเข้าเครือข่ายหลัก หากเป็นฟาร์มชนิดที่
เสียหายเมื่อของค้างสะสม ใช้ <ItemLink id="void_card" /> ลบไอเทมส่วนเกินแทนได้
* หากฟาร์มมีผลผลิตหลายชนิด <ItemLink id="equal_distribution_card" /> ป้องกันไม่ให้ไอเทมชนิดเดียวเติมจน Cell ทุกใบเต็ม
และไม่มีที่เก็บไอเทมชนิดอื่นได้