---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Pattern Provider
  icon: pattern_provider
  position: 210
categories:
- devices
item_ids:
- ae2:pattern_provider
- ae2:cable_pattern_provider
---

# The Pattern Provider

<Row gap="20">
<BlockImage id="pattern_provider" scale="8" />
<BlockImage id="pattern_provider" p:push_direction="up" scale="8" />
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_pattern_provider.snbt" />
</GameScene>
</Row>

Pattern Provider เป็นช่องทางหลักที่ระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md) โต้ตอบกับโลก โดยส่งวัตถุดิบใน
[แพตเทิร์น](patterns.md) เข้าช่องเก็บของข้างเคียง และรับไอเทมเพื่อใส่กลับเข้าเครือข่ายได้ จึงมัก
ประหยัดช่องสัญญาณโดยต่อท่อผลผลิตเครื่องจักรกลับเข้า Pattern Provider ใกล้ ๆ (มักเป็นเครื่องที่ส่งวัตถุดิบไป)
แทนการใช้ <ItemLink id="import_bus" /> ดึงผลผลิตเข้าเครือข่าย

โปรดทราบว่าเพราะมันส่งวัตถุดิบตรงจาก [Crafting Storage](crafting_cpu_multiblock.md#crafting-storage) ใน Crafting CPU
ตัวมันจึงไม่เคยมีวัตถุดิบอยู่ในช่องเก็บของจริง และต่อท่อดึงออกไม่ได้ ต้องให้ Provider ส่ง
เข้าช่องเก็บของอื่น (เช่น Barrel) แล้วจึงต่อท่อจากจุดนั้น

อีกข้อคือ Provider ต้องส่งวัตถุดิบทั้งชุดพร้อมกัน ส่งเพียงครึ่งชุดไม่ได้
คุณนำคุณสมบัตินี้ไปใช้ประโยชน์ได้

Pattern Provider ทำงานพิเศษกับ Interface บน [เครือข่ายย่อย](../ae2-mechanics/subnetworks.md): หาก Interface ยังไม่ปรับแต่ง (ไม่มีอะไรในช่องร้องขอ)
Provider จะข้าม Interface แล้วส่งตรงเข้า [ที่เก็บ](../ae2-mechanics/import-export-storage.md) ของเครือข่ายย่อย
จึงไม่เติม Interface จนเต็มด้วยชุดวัตถุดิบ และที่สำคัญจะไม่ใส่ชุดถัดไปจนกว่าเครื่องจักรจะมีพื้นที่
ใช้กับ Blocking Mode ได้ถูกต้อง โดย Provider จะตรวจวัตถุดิบในช่องเครื่องจักรแทนช่อง Interface

เช่น ระบบนี้ส่งทั้งของที่จะหลอมและเชื้อเพลิงตรงเข้าช่องที่เหมาะสมของ Furnace
คุณใช้วิธีนี้ส่งแพตเทิร์นเข้าหลายด้านของเครื่องเดียว หรือหลายเครื่องได้

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/furnace_automation.snbt" />

<BoxAnnotation color="#dddddd" min="1 0 0" max="2 1 1">
        (1) Pattern Provider: รุ่นกำหนดทิศทางด้วย Certus Quartz Wrench พร้อม Processing Pattern ที่เกี่ยวข้อง

        ![แพตเทิร์น Iron](../assets/diagrams/furnace_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="2 1.3 1">
        (2) Interface: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 1 0" max="1.3 2 1">
        (3) Storage Bus #1: กรองให้รับ Coal
        <ItemImage id="minecraft:coal" scale="2" />
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 2 0" max="1 2.3 1">
        (4) Storage Bus #2: ตั้งรายการปฏิเสธ Coal ด้วย Inverter Card
        <Row><ItemImage id="minecraft:coal" scale="2" /><ItemImage id="inverter_card" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="4 0.5 0.5" color="#00ff00">
        ไปเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ภาพนี้แสดงหลักการส่งวัตถุดิบให้หลายเครื่องโดยทั่วไป

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        Interface (ต้องเป็นแบบแบน ไม่ใช่บล็อกเต็ม)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        Storage Bus
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        จุดที่ต้องการส่งวัตถุดิบตามแพตเทิร์น
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

รองรับ Pattern Provider หลายเครื่องที่มีแพตเทิร์นเหมือนกัน และทำงานขนานกันได้

Pattern Provider พยายามส่งชุดวัตถุดิบวนไปทุกด้าน ทำให้เครื่องจักรที่ติดอยู่ทั้งหมดทำงานขนานกัน

## Variants

รูปแบบต่าง ๆ

Pattern Provider มี 3 รูปแบบ: ปกติ กำหนดทิศทาง และแบน/[ชิ้นส่วนย่อย](../ae2-mechanics/cable-subparts.md) ซึ่งมีผลต่อด้านที่มันส่ง
วัตถุดิบ รับไอเทม และเชื่อมต่อเครือข่าย

*   แบบปกติส่งวัตถุดิบและรับไอเทมทุกด้าน และทำงานเหมือนสาย
    ที่ให้การเชื่อมต่อเครือข่ายทุกด้าน เช่นเดียวกับเครื่องจักร AE2 ส่วนใหญ่

*   แบบกำหนดทิศทางทำโดยใช้ <ItemLink id="certus_quartz_wrench" /> กับ Pattern Provider ปกติเพื่อเปลี่ยน
    ทิศทาง ส่งวัตถุดิบเฉพาะด้านที่เลือก รับไอเทมทุกด้าน และไม่เชื่อม
    เครือข่ายด้านที่เลือก จึงส่งให้เครื่องจักร AE2 โดยไม่รวมเครือข่ายได้หากต้องการสร้างเครือข่ายย่อย

*   แบบแบนเป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md) จึงติดหลายตัวบนสายเดียวให้ระบบกะทัดรัดได้
    ทำงานคล้ายด้านที่เลือกของแบบกำหนดทิศทาง โดยส่งแพตเทิร์น รับไอเทม และ ไม่
    ให้การเชื่อมต่อเครือข่ายที่ด้านหน้า

สลับ Pattern Provider ระหว่างปกติกับแบนได้ในตารางคราฟต์

## Settings

การตั้งค่า

Pattern Provider มีหลายโหมด:

*   โหมดป้องกันของค้าง หยุดไม่ให้ Provider ส่งชุดวัตถุดิบใหม่หากมี
    วัตถุดิบอยู่ในเครื่องแล้ว
*   ล็อกการคราฟต์ ล็อก Provider ตามเงื่อนไขเรดสโตนหลายแบบ หรือจนกว่าจะใส่ผลผลิต
    จากการคราฟต์ครั้งก่อนกลับเข้า Pattern Provider เครื่องนั้น
*   แสดงหรือซ่อน Provider ใน <ItemLink id="pattern_access_terminal" /> ได้

## Priority

ลำดับความสำคัญ

ตั้งลำดับความสำคัญโดยคลิกประแจมุมขวาบนของหน้าจอ หากมี [แพตเทิร์น](patterns.md) หลายสูตร
สำหรับไอเทมเดียวกัน จะเลือกแพตเทิร์นใน Provider ที่ลำดับสูงกว่าก่อน
ยกเว้นเครือข่ายไม่มีวัตถุดิบสำหรับสูตรลำดับสูงนั้น

## A Common Misconception

ความเข้าใจผิดที่พบบ่อย

ไม่รู้ทำไมผู้คนยังทำแบบนี้กัน ผู้เขียนไม่เข้าใจแต่ขอใส่ไว้เผื่อช่วยได้ (บางที
ผู้เล่นอาจเข้าใจผิดว่า <ItemLink id="export_bus" /> เป็นทางเดียวที่สิ่งของออกจากเครือข่ายได้ โดยไม่รู้
ว่า Pattern Provider ส่งออกสิ่งของได้ด้วย)

แบบนี้จะไม่ได้ผลตามที่ต้องการ ดังที่กล่าวในหน้า [สาย](cables.md) สายไม่ใช่ท่อไอเทม และไม่มี
ช่องเก็บของภายใน Provider จึงไม่ส่งของเข้าไป

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_1.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        ไม่ใช่ Blast Furnace
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

เพราะ Provider ไม่มีปลายทางให้ส่งของ
จึงทำงานไม่ได้ ในภาพนี้มันเพียงทำหน้าที่เหมือนสาย เชื่อม <ItemLink id="export_bus" /> เข้ากับ
เครือข่าย

Provider ไม่ได้บอก <ItemLink id="export_bus" /> ว่าต้องส่งออกอะไรด้วย Export Bus จะส่งออก
ทุกอย่างที่คุณใส่ไว้ในตัวกรองของมันเท่านั้น

สิ่งที่ทำอยู่จริง ๆ จึงเทียบได้กับแบบนี้:

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_2.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        ไม่ใช่ Blast Furnace
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

สิ่งที่คุณน่าจะต้องการจริงคือแบบนี้ ซึ่ง Pattern Provider ส่งเนื้อหาของแพตเทิร์นเข้า
เครื่องจักรที่อยู่ติดกันได้:

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/assemblies/provider_misconception_3.snbt" />

  <BoxAnnotation color="#dddddd" min="1 0 3" max="2 1 4">
        ไม่ใช่ Blast Furnace
  </BoxAnnotation>

  <IsometricCamera yaw="95" pitch="5" />
</GameScene>

## Recipes

สูตรคราฟต์

<RecipeFor id="pattern_provider" />

<RecipeFor id="cable_pattern_provider" />
