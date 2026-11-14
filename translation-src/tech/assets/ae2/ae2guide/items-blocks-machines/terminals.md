---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: เทอร์มินัล
  icon: crafting_terminal
  position: 210
categories:
- devices
item_ids:
- ae2:terminal
- ae2:crafting_terminal
- ae2:pattern_encoding_terminal
- ae2:pattern_access_terminal
---

# Terminals

เทอร์มินัล

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/terminals.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

แม้ <ItemLink id="pattern_provider" />, <ItemLink id="import_bus" />, <ItemLink id="storage_bus" /> และอุปกรณ์อื่น
จะเป็นช่องทางหลักที่เครือข่าย AE2 โต้ตอบกับโลก แต่เทอร์มินัลเป็นช่องทางหลักที่เครือข่าย AE2
โต้ตอบกับ *คุณ* มีหลายรุ่นที่ทำหน้าที่ต่างกัน

เทอร์มินัลใช้สีเดียวกับ [สาย](cables.md) ที่ติดตั้งอยู่

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

## Terminal Placement

การวางเทอร์มินัล

เพราะเทอร์มินัลมักเป็น [ชิ้นส่วนย่อย](../ae2-mechanics/cable-subparts.md) ชิ้นแรกที่ผู้เล่นวาง
จึงมักเกิดความผิดพลาดโดยวางกลับด้าน ตัวอย่างต่อไปนี้แสดงวิธีที่ถูกและผิด:

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/terminal_placement.snbt" />
  <IsometricCamera yaw="195" pitch="30" />

  <LineAnnotation color="#ff3333" from="2.5 .5 .5" to="4.5 2.5 .5" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="2.5 2.5 .5" to="4.5 .5 .5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="-.5 2.5 .5" to="1 .5 .5" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1 .5 .5" to="1.5 1 .5" alwaysOnTop={true} thickness="0.05"/>
</GameScene>

คุณยังมีเทอร์มินัลกับ Energy Acceptor เหมือนเดิม แต่ตอนนี้เทอร์มินัลหันถูกด้าน
และเชื่อมต่อเครือข่ายจริง อีกทั้งทั้งหมดใช้พื้นที่น้อยลง

<a name="terminal-ui"></a>

# Terminal

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

เทอร์มินัลพื้นฐาน ให้คุณดูและเข้าถึงของใน [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
และส่งคำขอไปยังระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)

## The UI

หน้าจอควบคุม

หน้าจอเทอร์มินัลพื้นฐานแบ่งเป็นหลายส่วน

ส่วนกลางให้เข้าถึงที่เก็บของเครือข่าย ใส่และนำสิ่งของออกได้ มีปุ่มลัด
เมาส์และคีย์บอร์ดหลายแบบ:

*   คลิกซ้ายหยิบหนึ่งกอง คลิกขวาหยิบครึ่งกอง
*   หากไอเทม ของเหลว หรือสิ่งอื่น [คราฟต์อัตโนมัติได้](../ae2-mechanics/autocrafting.md)
    กดปุ่มที่ตั้งเป็น "เลือกบล็อก" (ปกติคือเมาส์กลาง) เพื่อเปิดหน้าจอระบุจำนวนที่จะคราฟต์ ใส่สูตรอย่าง `3*64/2` ได้
    หรือพิมพ์ `=32` เพื่อคราฟต์เฉพาะจำนวนที่ขาดให้ในที่เก็บครบ 32 ชิ้น
*   กด Shift ค้างเพื่อตรึงรายการที่แสดง ไม่ให้เรียงใหม่เมื่อจำนวนเปลี่ยนหรือมีไอเทมใหม่เข้าระบบ
*   คลิกขวาด้วย Bucket หรือภาชนะของเหลวอื่นเพื่อฝากของเหลว คลิกซ้ายที่ของเหลวในเทอร์มินัลด้วย
    ภาชนะเปล่าเพื่อถอนของเหลว

ด้านซ้ายมีปุ่มตั้งค่าสำหรับ:

*   เรียงตามข้อมูลต่าง ๆ เช่น ชื่อ ม็อด และจำนวน
*   แสดงของที่เก็บอยู่ ของที่คราฟต์ได้ หรือทั้งสอง
*   แสดงไอเทม ของเหลว หรือทั้งสอง
*   เปลี่ยนลำดับการเรียง
*   เปิดหน้าต่างตั้งค่าเทอร์มินัลโดยละเอียด
*   เปลี่ยนความสูงหน้าจอเทอร์มินัล

ด้านขวามีช่องสำหรับ <ItemLink id="view_cell" />

มุมขวาบนของส่วนกลาง (ปุ่มค้อน) เปิดหน้าจอสถานะ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
เพื่อดูความคืบหน้างาน และดูว่า [Crafting CPU](crafting_cpu_multiblock.md) แต่ละชุดทำอะไรอยู่

## Recipe

สูตรคราฟต์

<RecipeFor id="terminal" />

<a name="crafting-terminal-ui"></a>

# Crafting Terminal

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/crafting_terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

Crafting Terminal คล้ายเทอร์มินัลปกติ มีการตั้งค่าและส่วนต่าง ๆ เหมือนกัน แต่เพิ่มตารางคราฟต์ที่เติมวัตถุดิบอัตโนมัติ
จาก [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ระวังเมื่อ Shift+คลิกที่ผลผลิต!

ควรอัปเกรดเทอร์มินัลเป็น Crafting Terminal ให้เร็วที่สุด

## The UI

หน้าจอควบคุม

Crafting Terminal มีหน้าจอเหมือนเทอร์มินัลปกติ แต่เพิ่มตารางคราฟต์ตรงกลาง

มีปุ่มเพิ่ม 2 ปุ่มสำหรับย้ายของออกจากตารางคราฟต์เข้าเครือข่ายหรือช่องเก็บของของคุณ

## Recipe

สูตรคราฟต์

<RecipeFor id="crafting_terminal" />

<a name="pattern-encoding-terminal-ui"></a>

# Pattern Encoding Terminal

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/pattern_encoding_terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

Pattern Encoding Terminal คล้ายเทอร์มินัลปกติ มีการตั้งค่าและส่วนต่าง ๆ เหมือนกัน แต่เพิ่ม
ส่วนเข้ารหัส [แพตเทิร์น](patterns.md) รูปร่างคล้ายหน้าจอ Crafting Terminal แต่ตารางนี้
ไม่ได้คราฟต์จริง

ควรมีเครื่องนี้เพิ่มจาก Crafting Terminal

## The UI

หน้าจอควบคุม

Crafting Terminal มีหน้าจอเหมือนเทอร์มินัลปกติ พร้อมส่วนเข้ารหัส [แพตเทิร์น](patterns.md) เพิ่มเติม

ส่วนเข้ารหัสแพตเทิร์นแบ่งเป็นหลายส่วน:

ช่องสำหรับใส่ <ItemLink id="blank_pattern" />

ลูกศรใหญ่สำหรับเข้ารหัสแพตเทิร์น

ช่องแพตเทิร์นที่เข้ารหัสแล้ว ใส่แพตเทิร์นที่มีข้อมูลแล้วในช่องนี้เพื่อแก้ไข จากนั้นคลิกลูกศร "เข้ารหัส"

มี 4 แท็บทางขวาเพื่อเปลี่ยนชนิดแพตเทิร์นระหว่าง

*   คราฟต์
*   แปรรูป
*   ตีเหล็ก
*   ตัดหิน

หน้าจอส่วนกลางเปลี่ยนตามชนิดแพตเทิร์นที่จะเข้ารหัส:

*   โหมดคราฟต์:
    *   คลิกซ้ายใส่หรือลากวัตถุดิบจาก JEI/REI เพื่อจัดสูตร คลิกขวาเพื่อนำวัตถุดิบออก
    *   เปิดการใช้วัตถุดิบทดแทนเพื่อทำสิ่งอย่างคราฟต์ Stick จาก Planks ชนิดใดก็ได้
        ควรใช้เมื่อจำเป็นจริง ๆ เท่านั้น
    *   การใช้ของเหลวทดแทนให้ใช้ของเหลวที่เก็บไว้แทน Bucket ของเหลว
    *   เข้ารหัสแพตเทิร์นโดยตรงจากหน้าสูตร JEI/REI ได้ด้วย

*   โหมดแปรรูป:
    * คลิกซ้าย คลิกขวา หรือลากวัตถุดิบจาก JEI/REI เพื่อระบุวัตถุดิบและผลผลิตของสูตร
    * คลิกขวาด้วยภาชนะของเหลว (เช่น Bucket หรือถังของเหลว) เพื่อกำหนดของเหลวเป็นวัตถุดิบแทนไอเทมภาชนะ
    * เมื่อถือไอเทมเป็นกอง คลิกซ้ายวางทั้งกอง คลิกขวาวางหนึ่งชิ้น คลิกซ้ายกองวัตถุดิบที่มีอยู่
        เพื่อนำออกทั้งกอง คลิกขวาเพื่อลดหนึ่งชิ้น ปุ่ม "เลือกบล็อก" (ปกติคือเมาส์กลาง)
        ให้กำหนดจำนวนไอเทมหรือของเหลวที่แน่นอนได้
    * ช่องผลผลิตมีผลผลิตหลักและที่สำหรับผลผลิตรองที่อยากให้ระบบคราฟต์อัตโนมัติรับรู้
    * ทั้งช่องวัตถุดิบและผลผลิตเลื่อนได้ จึงใส่วัตถุดิบต่างชนิดได้ 81 ชนิด และผลผลิตรอง 26 ชนิด
    * เข้ารหัสแพตเทิร์นโดยตรงจากหน้าสูตร JEI/REI ได้ด้วย

*   หน้าจอโหมดตีเหล็กและตัดหินทำงานคล้าย Smithing Table และ Stonecutter ตามลำดับ

## Recipe

สูตรคราฟต์

<RecipeFor id="pattern_encoding_terminal" />

<a name="pattern-access-terminal-ui"></a>

# Pattern Access Terminal

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/blocks/pattern_access_terminal.snbt" />
  <IsometricCamera yaw="180" />
</GameScene>

Pattern Access Terminal แก้ปัญหาเฉพาะอย่าง: เมื่อสร้างหอ <ItemLink id="pattern_provider" />
กับ <ItemLink id="molecular_assembler" /> แน่น ๆ คุณจะเข้าไปใส่แพตเทิร์นใหม่ใน Provider โดยตรงไม่ได้
หรือบางทีคุณอาจขี้เกียจเดินข้ามฐานไปใส่ [แพตเทิร์น](patterns.md) Pattern Access Terminal
ทำให้เข้าถึง Pattern Provider ทุกเครื่องในเครือข่ายได้

## The UI

หน้าจอควบคุม

เทอร์มินัลนี้มีหน้าจอต่างจากรุ่นอื่นทั้งหมด

มีการตั้งค่าความสูงหน้าจอและรายการ Pattern Provider ที่จะแสดง

แต่ละแถวในเทอร์มินัลตรงกับ Pattern Provider หนึ่งเครื่อง

เรียง Pattern Provider ในเทอร์มินัลตามบล็อกที่เชื่อมติดอยู่ หรือชื่อที่ตั้งให้ (ใน Anvil หรือ
ด้วย <ItemLink id="name_press" />)

## Recipe

สูตรคราฟต์

<RecipeFor id="pattern_access_terminal" />
