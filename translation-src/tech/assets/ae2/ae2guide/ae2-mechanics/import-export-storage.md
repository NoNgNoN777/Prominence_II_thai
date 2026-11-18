---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: นำเข้า ส่งออก และจัดเก็บ
---

# Import, Export, and Storage

นำเข้า ส่งออก และจัดเก็บ

ระบบ ME ของคุณกับโลกภายนอก

แนวคิดสำคัญของ AE2 คือคลังเครือข่าย ซึ่งเป็นที่เก็บสิ่งต่าง ๆ ของระบบ
โดยทั่วไปคือ [Storage Cell](../items-blocks-machines/storage_cells.md) หรือช่องเก็บของที่ <ItemLink id="storage_bus" />
เชื่อมต่ออยู่ [อุปกรณ์](../ae2-mechanics/devices.md)ส่วนใหญ่ของ AE2 จะทำงานกับคลังนี้ในรูปแบบใดรูปแบบหนึ่ง

ตัวอย่างเช่น

*   <ItemLink id="import_bus" /> ส่งของเข้าคลังเครือข่าย
*   <ItemLink id="export_bus" /> ดึงของจากคลังเครือข่าย
*   <ItemLink id="interface" /> ทั้งดึงของออกและส่งของเข้าคลังเครือข่าย
*   [Terminal](../items-blocks-machines/terminals.md) ทั้งส่งของเข้าและดึงของออกเมื่อคุณฝากหรือถอนของ รวมถึงเติมวัตถุดิบในช่องคราฟต์
*   <ItemLink id="storage_bus" /> ไม่ได้ส่งของเข้าออกคลังโดยตรง แต่ส่งเข้าออกช่องเก็บของที่เชื่อมต่อ
    เพื่อใช้ช่องเก็บของนั้นเป็นคลังเครือข่าย กล่าวคืออุปกรณ์อื่นส่งของเข้าหรือดึงของออกผ่าน *Storage Bus*

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/import_export_storage.snbt" />

  <BoxAnnotation color="#dddddd" min="8 1 1" max="9 1.3 2">
        Import Bus นำของจากช่องเก็บของที่หันเข้าหาเข้าสู่คลังเครือข่าย
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="8 2 1" max="9 3 1.3">
        การใส่ของจากช่องเก็บของผู้เล่นลง Terminal ถือเป็นการนำของเข้าเครือข่าย
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="7 0 1" max="8 1 2">
        Interface นำของจากช่องภายในเข้าเครือข่ายหากไม่ได้ตั้งให้สำรองของในช่องนั้น หรือมีจำนวน
        เกินที่ตั้งสำรองไว้ จึงส่งของเข้า Interface เพื่อฝากเข้าสู่เครือข่ายได้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="6 0 1" max="7 1 2">
        Pattern Provider นำของจากช่องรับคืนเข้าเครือข่าย จึงส่งของเข้าช่องนั้นเพื่อฝากเข้าสู่ระบบได้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 1" max="5 2 2">
        Drive ใช้เซลล์ที่ใส่อยู่เป็นคลังเครือข่าย
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="3 1 1" max="4 1.3 2">
        Storage Bus ใช้ช่องเก็บของที่หันเข้าหาเป็นคลังเครือข่าย
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 1 1" max="2 1.3 2">
        Export Bus ส่งของจากคลังเครือข่ายไปยังช่องเก็บของที่หันเข้าหา
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 1" max="2 3 1.3">
        การดึงของออกจาก Terminal ถือเป็นการส่งของออกจากเครือข่าย
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 1 1" max="1 2 2">
        Interface ส่งของจากเครือข่ายมายังช่องภายในที่ตั้งให้สำรองของไว้
        จึงดึงของจากช่องนั้นเพื่อถอนออกจากเครือข่ายได้
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

การส่งของเข้าหรือดึงของออกจากคลังเครือข่ายเป็นสิ่งสำคัญที่ต้องคำนึงถึงเมื่อออกแบบ
ระบบอัตโนมัติและระบบขนส่ง

## Storage Priority

ลำดับความสำคัญของคลัง

คลิกไอคอนประแจมุมขวาบนของหน้าจอบางชนิดเพื่อตั้งลำดับความสำคัญ
ของที่เข้าสู่เครือข่ายจะไปยังคลังที่มีลำดับความสำคัญสูงสุดก่อน
หากสองคลังมีลำดับเท่ากัน ระบบจะเลือกคลังที่มีไอเทมชนิดนั้นอยู่แล้ว
ก่อนคลังอื่น เซลล์ที่กำหนดรายการอนุญาตไว้จะถือว่ามีไอเทมนั้นอยู่แล้ว
เมื่อเปรียบเทียบกับคลังในกลุ่มลำดับเดียวกัน ส่วนการถอนของจะ
ดึงจากคลังที่มีลำดับความสำคัญต่ำสุดก่อน ดังนั้นเมื่อฝากและถอนของ
คลังที่สำคัญกว่าจะค่อย ๆ เต็ม ส่วนคลังที่สำคัญน้อยกว่าจะค่อย ๆ ว่าง
