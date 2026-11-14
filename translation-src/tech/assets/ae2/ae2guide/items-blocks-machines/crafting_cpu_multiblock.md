---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Crafting CPU Multiblock (Storage, Coprocessor, Monitor, Unit)
  icon: 1k_crafting_storage
  position: 210
categories:
- devices
item_ids:
- ae2:1k_crafting_storage
- ae2:4k_crafting_storage
- ae2:16k_crafting_storage
- ae2:64k_crafting_storage
- ae2:256k_crafting_storage
- ae2:crafting_accelerator
- ae2:crafting_monitor
- ae2:crafting_unit
---

# The Crafting CPU

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<Row>
  <BlockImage id="1k_crafting_storage" scale="4" />

  <BlockImage id="crafting_accelerator" scale="4" />

  <BlockImage id="crafting_monitor" scale="4" />

  <BlockImage id="crafting_unit" scale="4" />
</Row>

Crafting CPU จัดการคำขอหรืองานคราฟต์ เก็บวัตถุดิบระหว่างทางขณะดำเนินงานหลายขั้น
และกำหนดขนาดงานสูงสุด รวมถึงมีผลบางส่วนต่อความเร็วที่งานเสร็จ ดู [การคราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
สำหรับรายละเอียด

Crafting CPU แต่ละชุดจัดการได้ 1 คำขอหรืองาน หากต้องการสั่ง Calculation Processor และ Smooth Stone 256 ชิ้นพร้อมกัน ต้องมีโครง CPU 2 ชุด

ตั้งให้รับคำขอจากผู้เล่น ระบบอัตโนมัติ (Export Bus และ Interface) หรือทั้งสองได้

คลิกขวาเพื่อเปิดหน้าจอสถานะการคราฟต์และดูความคืบหน้างานที่ CPU รับผิดชอบ

## Settings

การตั้งค่า

*   ตั้ง CPU ให้รับคำขอเฉพาะผู้เล่น เฉพาะระบบอัตโนมัติ (เช่น <ItemLink id="export_bus" /> ที่ใส่
    <ItemLink id="crafting_card" />) หรือทั้งสองได้

## Construction

การประกอบ

Crafting CPU เป็นโครงสร้างหลายบล็อก ต้องเป็นทรงสี่เหลี่ยมมุมฉากตันไม่มีช่องว่าง ประกอบจากส่วนประกอบหลายชนิด

แต่ละ CPU ต้องมี Crafting Storage อย่างน้อย 1 บล็อก (CPU ที่เล็กที่สุดที่ใช้งานได้คือ 1k Crafting Storage เพียงบล็อกเดียว)

# Crafting Unit

<BlockImage id="crafting_unit" scale="4" />

(ไม่บังคับ) Crafting Unit ใช้เติมพื้นที่ให้ CPU เป็นทรงสี่เหลี่ยมตันเมื่อมีส่วนประกอบอื่นไม่พอ
และเป็นวัตถุดิบพื้นฐานของส่วนประกอบอื่นด้วย

<RecipeFor id="crafting_unit" />

# Crafting Storage

<Row>
  <BlockImage id="1k_crafting_storage" scale="4" />

  <BlockImage id="4k_crafting_storage" scale="4" />

  <BlockImage id="16k_crafting_storage" scale="4" />

  <BlockImage id="64k_crafting_storage" scale="4" />

  <BlockImage id="256k_crafting_storage" scale="4" />
</Row>

(จำเป็น) Crafting Storage มีขนาดมาตรฐานเหมือนเซลล์ (1k, 4k, 16k, 64k, 256k) ใช้เก็บวัตถุดิบ
และวัตถุดิบระหว่างทางในการคราฟต์ งานที่ใช้วัตถุดิบมากจึงต้องใช้ Storage ขนาดใหญ่ขึ้น
หรือเพิ่มจำนวน

<Column>
  <Row>
    <RecipeFor id="1k_crafting_storage" />

    <RecipeFor id="4k_crafting_storage" />

    <RecipeFor id="16k_crafting_storage" />
  </Row>

  <Row>
    <RecipeFor id="64k_crafting_storage" />

    <RecipeFor id="256k_crafting_storage" />
  </Row>
</Column>

# Crafting Co-Processing Unit

<BlockImage id="crafting_accelerator" scale="4" />

(ไม่บังคับ) Crafting Co-Processor ทำให้ระบบส่งชุดวัตถุดิบจาก <ItemLink id="pattern_provider" /> ได้ถี่ขึ้น
จึงตามทันเครื่องจักรที่แปรรูปเร็ว เช่น Pattern Provider ที่ล้อมด้วย
<ItemLink id="molecular_assembler" /> ส่งวัตถุดิบได้เร็วกว่า Assembler เดียวจะทำทัน จึง
กระจายชุดวัตถุดิบระหว่าง Assembler รอบข้าง

<RecipeFor id="crafting_accelerator" />

# Crafting Monitor

<BlockImage id="crafting_monitor" scale="4" />

(ไม่บังคับ) Crafting Monitor แสดงงานที่ CPU กำลังจัดการ
เปลี่ยนสีหน้าจอได้ด้วย <ItemLink id="color_applicator" />

<RecipeFor id="crafting_monitor" />
