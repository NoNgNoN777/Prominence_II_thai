---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: คราฟต์อัตโนมัติ
  icon: pattern_provider
---

# Autocrafting

คราฟต์อัตโนมัติ

### The Big One

หัวใจสำคัญของระบบ

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/autocraft_setup_greebles.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

การคราฟต์อัตโนมัติเป็นหนึ่งในหน้าที่หลักของ AE2 แทนที่จะคราฟต์วัตถุดิบย่อยแต่ละอย่างให้ได้จำนวนที่ถูกต้อง
ด้วยตัวเองอย่างเหนื่อยยาก คุณสั่งให้ระบบ ME ทำแทนได้ หรือจะให้คราฟต์แล้วส่งของออกอัตโนมัติ
รวมถึงใช้การทำงานร่วมกันของอุปกรณ์เพื่อสำรองไอเทมตามจำนวนที่ต้องการก็ได้ ระบบรองรับของเหลวด้วย และหากติดตั้ง
ส่วนเสริมที่รองรับทรัพยากรม็อดอื่น เช่นก๊าซ Mekanism ก็ใช้กับทรัพยากรนั้นได้เช่นกัน สะดวกมากเลยทีเดียว

หัวข้อนี้ค่อนข้างซับซ้อน เตรียมตัวให้พร้อมแล้วไปกันเลย

ระบบคราฟต์อัตโนมัติมี 3 ส่วน:
- สิ่งที่ส่งคำขอคราฟต์
- Crafting CPU
- <ItemLink id="pattern_provider" />

ลำดับการทำงานมีดังนี้:

1. มีสิ่งหนึ่งสร้างคำขอคราฟต์ อาจเป็นคุณคลิกไอเทมที่คราฟต์อัตโนมัติได้ใน Terminal
    หรือ Export Bus/Interface ที่ใส่ Crafting Card ส่งคำขอไอเทมที่ตั้งให้ส่งออกหรือสำรองไว้

*   (สำคัญ: ใช้ปุ่มที่กำหนดให้ "เลือกบล็อก" ซึ่งปกติคือปุ่มเมาส์กลาง เพื่อสั่งคราฟต์ไอเทมที่มีอยู่ในคลังแล้ว ปุ่มนี้อาจชนกับม็อดจัดช่องเก็บของ)

2. ระบบ ME คำนวณวัตถุดิบและขั้นตอนย่อยที่จำเป็นต่อคำขอ แล้วเก็บไว้ใน Crafting CPU ที่เลือก

3. <ItemLink id="pattern_provider" /> ที่มี[แพตเทิร์น](../items-blocks-machines/patterns.md)ตรงกับงาน จะส่งวัตถุดิบตามแพตเทิร์นไปยังช่องเก็บของข้างเคียง
    สำหรับสูตรจาก Crafting Table หรือ "แพตเทิร์นคราฟต์" ปลายทางคือ <ItemLink id="molecular_assembler" />
    สำหรับสูตรชนิดอื่นหรือ "แพตเทิร์นแปรรูป" ปลายทางคือบล็อก เครื่องจักร หรือระบบซับซ้อนที่ควบคุมด้วยเรดสโตน

4. ผลผลิตต้องถูกส่งกลับเข้าระบบด้วยวิธีใดวิธีหนึ่ง เช่น Import Bus, Interface หรือส่งกลับเข้า Pattern Provider
    ต้องเกิดเหตุการณ์ "นำไอเทมเข้าเครือข่าย" จึงไม่สามารถ
    ส่งผลผลิตผ่านท่อเข้าหีบที่ติด <ItemLink id="storage_bus" /> แล้วถือว่าเสร็จได้

5. หากผลผลิตนั้นเป็นวัตถุดิบของขั้นตอนถัดไปในคำขอ ระบบจะเก็บไว้ใน Crafting CPU แล้วนำไปใช้คราฟต์ต่อ

# Patterns

แพตเทิร์น

<ItemImage id="crafting_pattern" scale="4" />

สร้างแพตเทิร์นจาก Blank Pattern ใน <ItemLink id="pattern_encoding_terminal" />

แพตเทิร์นมีหลายชนิดสำหรับงานต่างกัน:

*   <ItemLink id="crafting_pattern" /> บันทึกสูตร Crafting Table ใส่ลง <ItemLink id="molecular_assembler" /> โดยตรงเพื่อให้
    คราฟต์เมื่อได้รับวัตถุดิบก็ได้ แต่การใช้งานหลักคือใส่ใน <ItemLink id="pattern_provider" /> ที่อยู่ข้าง Molecular Assembler
    Provider จะส่งข้อมูลแพตเทิร์นพร้อมวัตถุดิบให้ Assembler ข้างเคียง
    เนื่องจาก Assembler ส่งผลผลิตไปช่องเก็บของข้างเคียงอัตโนมัติ เพียงวางติด Provider ก็ทำแพตเทิร์นคราฟต์อัตโนมัติได้แล้ว

***

*   <ItemLink id="smithing_table_pattern" /> คล้ายแพตเทิร์นคราฟต์ แต่บันทึกสูตร Smithing Table ใช้ Pattern
    Provider กับ Molecular Assembler ทำอัตโนมัติได้ด้วยวิธีเดียวกัน แพตเทิร์นคราฟต์ ตีเหล็ก และตัดหิน
    ใช้ร่วมกันในระบบเดียวได้

***

*   <ItemLink id="stonecutting_pattern" /> คล้ายแพตเทิร์นคราฟต์ แต่บันทึกสูตร Stonecutter ใช้ Pattern
    Provider กับ Molecular Assembler ทำอัตโนมัติได้ด้วยวิธีเดียวกัน แพตเทิร์นคราฟต์ ตีเหล็ก และตัดหิน
    ใช้ร่วมกันในระบบเดียวได้

***

*   <ItemLink id="processing_pattern" /> ทำให้การคราฟต์อัตโนมัติยืดหยุ่นมากที่สุด โดยบอกเพียงว่า
    "เมื่อ Pattern Provider ส่งวัตถุดิบเหล่านี้ไปช่องเก็บของข้างเคียง ระบบ ME จะได้รับผลผลิตตามนี้ในอนาคต
    ไม่ว่าจะใกล้หรือไกล" ใช้กับเครื่องจักรจากม็อดแทบทุกชนิด รวมถึง Furnace และอุปกรณ์คล้ายกัน เพราะ
    ไม่จำกัดขั้นตอนระหว่างส่งวัตถุดิบกับรับผลผลิต คุณจึงสร้างระบบแปลก ๆ ได้ เช่น ส่งวัตถุดิบ
    เข้าสายการผลิตทั้งโรงงานที่จัดเรียงของ รับวัตถุดิบอื่นจากฟาร์มที่ผลิตไม่จำกัด
    หรือแม้แต่พิมพ์บท Bee Movie ทั้งเรื่อง ระบบ ME ก็ไม่สนใจตราบใดที่ได้ผลผลิตตามแพตเทิร์น
    ที่จริง วัตถุดิบไม่จำเป็นต้องเกี่ยวกับผลผลิตเลย คุณตั้งว่า "1 Cherry Planks = 1 Nether Star" แล้วให้
    ฟาร์ม Wither ฆ่า Wither เมื่อได้รับ Cherry Planks ก็ยังทำงานได้

รองรับ <ItemLink id="pattern_provider" /> หลายตัวที่มีแพตเทิร์นเหมือนกันเพื่อทำงานขนานกัน นอกจากนี้คุณอาจตั้ง
แพตเทิร์นเป็น Cobblestone 8 ชิ้น = Stone 8 ชิ้น แทน Cobblestone 1 ชิ้น = Stone 1 ชิ้น เพื่อให้ส่ง Cobblestone ครั้งละ 8 ชิ้น
เข้าสู่ระบบหลอม แทนการส่งทีละชิ้น

## The Most General Form of "Pattern"

"แพตเทิร์น" แบบทั่วไปที่สุด

ยังมี "แพตเทิร์น" ที่ทั่วไปกว่าแพตเทิร์นแปรรูปอีก คือ <ItemLink id="level_emitter" /> ที่ใส่ Crafting Card แล้วตั้ง
ให้ส่งสัญญาณเรดสโตนเพื่อคราฟต์ของ "แพตเทิร์น" แบบนี้ไม่กำหนดและไม่สนใจวัตถุดิบเลย
เพียงบอกว่า "หาก Level Emitter นี้ส่งสัญญาณเรดสโตน ระบบ ME จะได้รับไอเทมนี้ในอนาคต
ไม่ว่าจะใกล้หรือไกล" ปกติใช้เปิดปิดฟาร์มผลิตไม่จำกัดที่ไม่ใช้วัตถุดิบ
หรือควบคุมระบบสูตรวนซ้ำที่การคราฟต์อัตโนมัติทั่วไปไม่เข้าใจ เช่น "Cobblestone 1 ชิ้น = Cobblestone 2 ชิ้น"
เมื่อมีเครื่องเพิ่มจำนวน Cobblestone

# The Crafting CPU

Crafting CPU

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/crafting_cpus.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Crafting CPU จัดการคำขอและงานคราฟต์ เก็บวัตถุดิบระหว่างทางขณะทำงานหลายขั้นตอน
กำหนดขนาดงานสูงสุดและมีผลต่อความเร็วบางส่วน เป็นโครงสร้างมัลติบล็อก
รูปทรงสี่เหลี่ยมมุมฉากที่ต้องมี Crafting Storage อย่างน้อย 1 ชิ้น

Crafting CPU ประกอบด้วย:

*   (จำเป็น) [Crafting Storage](../items-blocks-machines/crafting_cpu_multiblock.md) มีขนาดตามเซลล์มาตรฐานคือ 1k, 4k, 16k, 64k และ 256k เก็บวัตถุดิบ
    และวัตถุดิบระหว่างทางของงานคราฟต์ งานที่ใช้วัตถุดิบมากจึงต้องมีพื้นที่ขนาดใหญ่ขึ้น
    หรือเพิ่มจำนวน Storage
*   (ทางเลือก) <ItemLink id="crafting_accelerator" /> ทำให้ระบบส่งวัตถุดิบจาก Pattern Provider ได้หลายชุดขึ้น
    เช่น Provider ที่ล้อมด้วย Molecular Assembler 6 เครื่องจะส่งวัตถุดิบไปใช้พร้อมกันทั้ง 6 เครื่อง แทนเพียงเครื่องเดียว
*   (ทางเลือก) <ItemLink id="crafting_monitor" /> แสดงงานที่ CPU กำลังทำ และย้อมสีได้ด้วย <ItemLink id="color_applicator" />
*   (ทางเลือก) <ItemLink id="crafting_unit" /> ใช้เติมพื้นที่ให้ CPU เป็นทรงสี่เหลี่ยมมุมฉากเท่านั้น

Crafting CPU แต่ละชุดรับได้ 1 คำขอหรืองาน หากต้องการสั่ง Calculation Processor และ Smooth Stone 256 ชิ้นพร้อมกัน ต้องมี CPU มัลติบล็อก 2 ชุด

ตั้งให้รับคำขอจากผู้เล่น ระบบอัตโนมัติ (Export Bus และ Interface) หรือทั้งสองแบบได้

# Pattern Providers

Pattern Provider

<Row>
<BlockImage id="pattern_provider" scale="4" />

<BlockImage id="pattern_provider" p:push_direction="up" scale="4" />

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/blocks/cable_pattern_provider.snbt" />
</GameScene>
</Row>

<ItemLink id="pattern_provider" /> เป็นช่องทางหลักที่ระบบคราฟต์อัตโนมัติทำงานกับโลกภายนอก ส่งวัตถุดิบตาม
[แพตเทิร์น](../items-blocks-machines/patterns.md)ไปยังช่องเก็บของข้างเคียง และรับของเพื่อส่งเข้าเครือข่ายได้ มัก
ประหยัดช่องสัญญาณได้ด้วยการต่อท่อผลผลิตกลับเข้า Pattern Provider ใกล้ ๆ ซึ่งมักเป็นตัวที่ส่งวัตถุดิบออก
แทนการใช้ <ItemLink id="import_bus" /> ดึงผลผลิตจากเครื่องเข้าเครือข่าย

เนื่องจากส่งวัตถุดิบตรงจาก [Crafting Storage](../items-blocks-machines/crafting_cpu_multiblock.md#crafting-storage) ใน Crafting CPU
จึงไม่เก็บวัตถุดิบในช่องภายในของตัวเอง และต่อท่อดึงของจาก Provider ไม่ได้ ต้องให้ Provider ส่งของ
ไปช่องเก็บของอื่น เช่น Barrel ก่อน แล้วจึงต่อท่อจากที่นั่น

อีกจุดสำคัญคือ Provider ต้องส่งวัตถุดิบทั้งหมดของชุดพร้อมกัน ส่งเพียงครึ่งชุดไม่ได้ สามารถใช้คุณสมบัตินี้
ช่วยออกแบบระบบได้

Pattern Provider ทำงานพิเศษร่วมกับ Interface บน[เครือข่ายย่อย](../ae2-mechanics/subnetworks.md): หากไม่ได้กำหนดของในช่องร้องขอของ Interface
Provider จะข้ามตัว Interface แล้วส่งตรงเข้า[คลัง](../ae2-mechanics/import-export-storage.md)ของเครือข่ายย่อย
จึงไม่อัดชุดวัตถุดิบไว้ใน Interface และที่สำคัญจะไม่ส่งชุดถัดไปจนกว่าคลังจะมีพื้นที่

รองรับ Pattern Provider หลายตัวที่มีแพตเทิร์นเหมือนกันเพื่อทำงานขนานกัน

Pattern Provider พยายามวนส่งวัตถุดิบไปทุกด้าน จึงใช้เครื่องจักรที่ติดอยู่ทั้งหมดทำงานขนานกัน

## Variants

รูปแบบ

Pattern Provider มี 3 รูปแบบ คือปกติ กำหนดทิศทาง และแบบแบน แต่ละแบบกำหนดด้านที่ใช้ส่ง
วัตถุดิบ รับไอเทม และเชื่อมเครือข่ายต่างกัน

*   แบบปกติส่งวัตถุดิบและรับของได้ทุกด้าน และทำงานเหมือน
    สายเคเบิลที่เชื่อมเครือข่ายทุกด้านเช่นเดียวกับเครื่องจักร AE2 ส่วนใหญ่

*   แบบกำหนดทิศทางสร้างโดยใช้ <ItemLink id="certus_quartz_wrench" /> กับ Provider ปกติเพื่อเปลี่ยน
    ทิศทาง ส่งวัตถุดิบเฉพาะด้านที่เลือก รับของได้ทุกด้าน แต่ไม่เชื่อม
    เครือข่ายผ่านด้านที่เลือก จึงส่งของให้เครื่อง AE2 โดยไม่รวมเครือข่าย เหมาะกับการสร้างเครือข่ายย่อย

*   แบบแบนเป็น[ชิ้นส่วนบนสายเคเบิล](../ae2-mechanics/cable-subparts.md) วางหลายตัวบนสายเดียวได้ จึงจัดระบบกะทัดรัด
    ทำงานคล้ายด้านที่เลือกของแบบกำหนดทิศทาง โดยส่งแพตเทิร์น รับของ และไม่
    เชื่อมเครือข่ายผ่านด้านหน้าของตัวเอง

สลับ Pattern Provider ระหว่างแบบปกติกับแบบแบนได้ในช่องคราฟต์

## Settings

การตั้งค่า

Pattern Provider มีหลายโหมด:

*   โหมดป้องกันการแทรกชุด หยุดส่งวัตถุดิบชุดใหม่หากยังมี
    วัตถุดิบอยู่ในเครื่อง
*   ล็อกการคราฟต์ ล็อก Provider ตามเงื่อนไขเรดสโตนหลายแบบ หรือจนกว่าผลผลิตจาก
    งานก่อนหน้าจะกลับเข้า Provider ตัวนั้นโดยเฉพาะ
*   เลือกแสดงหรือซ่อน Provider ใน <ItemLink id="pattern_access_terminal" /> ได้

## Priority

ลำดับความสำคัญ

คลิกประแจมุมขวาบนของหน้าจอเพื่อตั้งลำดับความสำคัญ หากมี[แพตเทิร์น](../items-blocks-machines/patterns.md)
หลายสูตรสำหรับไอเทมเดียวกัน ระบบจะใช้แพตเทิร์นใน Provider ที่มีลำดับสูงกว่าก่อน
เว้นแต่เครือข่ายจะมีวัตถุดิบสำหรับแพตเทิร์นนั้นไม่พอ

# Molecular Assemblers

Molecular Assembler

<BlockImage id="molecular_assembler" scale="4" />

<ItemLink id="molecular_assembler" /> รับไอเทมแล้วทำงานตามที่ <ItemLink id="pattern_provider" /> ข้างเคียงกำหนด
หรือตาม <ItemLink id="crafting_pattern" />, <ItemLink id="smithing_table_pattern" /> หรือ <ItemLink id="stonecutting_pattern" /> ที่ใส่ไว้
จากนั้นส่งผลผลิตออกไปช่องเก็บของข้างเคียง

การใช้งานหลักคือวางข้าง <ItemLink id="pattern_provider" /> โดย Provider จะทำงานพิเศษ
ส่งข้อมูลแพตเทิร์นพร้อมวัตถุดิบไปยัง Assembler ข้างเคียง เนื่องจาก Assembler ส่งผลผลิต
ไปช่องเก็บของข้างเคียงอัตโนมัติ ซึ่งรวมถึงช่องรับคืนของ Provider เพียงติด Assembler กับ Pattern Provider
ก็ทำแพตเทิร์นคราฟต์อัตโนมัติได้แล้ว

<GameScene zoom="4" background="transparent">
<ImportStructure src="../assets/assemblies/assembler_tower.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>