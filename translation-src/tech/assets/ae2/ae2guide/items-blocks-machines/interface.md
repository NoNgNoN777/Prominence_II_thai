---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Interface
  icon: interface
  position: 210
categories:
- devices
item_ids:
- ae2:interface
- ae2:cable_interface
---

# The Interface

<Row gap="20">
<BlockImage id="interface" scale="8" />
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_interface.snbt" />
</GameScene>
</Row>

Interface ทำงานเหมือนหีบเล็กและถังของเหลวที่เติมตัวเองจากและระบายเข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
ตามรายการที่ตั้งให้เก็บสต็อกในแต่ละช่อง พยายามทำให้เสร็จภายในหนึ่ง game tick จึงเติมหรือระบายได้
สูงสุด 9 กองต่อ game tick เป็นวิธีนำเข้าหรือส่งออกที่เร็วหากมีท่อไอเทมที่เร็ว

อีกคุณสมบัติที่มีประโยชน์คือ แม้ถังของเหลวส่วนใหญ่เก็บได้เพียงชนิดเดียว แต่ Interface เก็บได้สูงสุด 9 ชนิดพร้อมไอเทม
โดยพื้นฐานคือหีบหรือถังหลายของเหลวที่มีความสามารถเสริม ซึ่งปิดความสามารถเสริมได้โดยไม่เชื่อม
กับเครือข่ายใด
จึงเหมาะกับกรณีเฉพาะที่ต้องการเก็บของหลายชนิดอย่างละเล็กน้อย

## How An Interface Works Internally

Interface ทำงานภายในอย่างไร

ดังที่กล่าวไป Interface เปรียบเหมือนหีบหรือถังที่ติด <ItemLink id="import_bus" /> และ
<ItemLink id="export_bus" /> รุ่นสุดยอด พร้อม <ItemLink id="level_emitter" /> อีกหลายตัว

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_internals.snbt" />

  <BoxAnnotation color="#dddddd" min="1.3 0.3 1.3" max="9.7 1 1.7">
        Level Emitter หลายตัวสำหรับควบคุมจำนวนสต็อกที่ต้องการ
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/level_emitter.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 4 1.3" max="9.7 4.7 1.7">
        Level Emitter หลายตัวสำหรับควบคุมจำนวนสต็อกที่ต้องการ
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/level_emitter.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 1.3 1.3" max="9.7 2 1.7">
        Import Bus รุ่นสุดยอดหลายตัวที่ย้ายได้ 1 กองต่อ game tick
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/import_bus.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 3 1.3" max="9.7 3.7 1.7">
        Export Bus รุ่นสุดยอดหลายตัวที่ย้ายได้ 1 กองต่อ game tick
        <GameScene zoom="4" background="transparent">
        <ImportStructure src="../assets/blocks/export_bus.snbt" />
        </GameScene>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 1" max="10 3 2">
        ช่องภายในแยกกัน 9 ช่อง
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="15" />
</GameScene>

## Special Interactions

การทำงานร่วมกันแบบพิเศษ

Interface ยังมีการทำงานพิเศษกับ [อุปกรณ์](../ae2-mechanics/devices.md) AE2 อื่น ๆ:

<ItemLink id="storage_bus" /> ที่ติดกับ Interface ซึ่งยังไม่ตั้งค่า จะเปิด [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
ทั้งหมดของฝั่ง Interface ให้เครือข่ายฝั่ง Storage Bus เห็น ราวกับเครือข่ายของ Interface เป็นหีบใหญ่ใบเดียว
ที่ติด Storage Bus อยู่ การตั้งไอเทมให้เก็บสต็อกในช่องกรอง Interface จะปิดความสามารถนี้

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/interface_storage.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Pattern Provider ทำงานพิเศษกับ Interface บน [เครือข่ายย่อย](../ae2-mechanics/subnetworks.md): หาก Interface ยังไม่ตั้งค่า
Provider จะข้าม Interface แล้วส่งตรงเข้า [ที่เก็บ](../ae2-mechanics/import-export-storage.md) ของเครือข่ายย่อย
จึงไม่เติม Interface จนเต็มด้วยชุดวัตถุดิบ และที่สำคัญจะไม่ใส่ชุดถัดไปจนกว่าที่เก็บจะมีพื้นที่

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        Interface (ต้องเป็นแบบแบน ไม่ใช่บล็อกเต็ม)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        Storage Bus
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        จุดที่ต้องการส่งวัตถุดิบตามแพตเทิร์น (หลายเครื่อง หรือหลายด้านของเครื่องเดียว)
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Variants

รูปแบบต่าง ๆ

Interface มี 2 รูปแบบ คือปกติและแบน/[ชิ้นส่วนย่อย](../ae2-mechanics/cable-subparts.md) ซึ่งกำหนดด้านที่เข้าถึง
ช่องเก็บของได้ และด้านที่มีการเชื่อมต่อเครือข่าย

*   แบบปกติให้ใส่ ดึง และเข้าถึงช่องเก็บของได้ทุกด้าน และทำงานเหมือนสาย
    ที่เชื่อมเครือข่ายทุกด้าน เช่นเดียวกับเครื่องจักร AE2 ส่วนใหญ่

*   แบบแบนเป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md) จึงติดหลายตัวบนสายเดียวให้ระบบกะทัดรัดได้
    ใส่ ดึง และเข้าถึงช่องเก็บของผ่านด้านหน้าของมัน แต่ไม่ให้การเชื่อมต่อเครือข่ายด้านนั้น

สลับ Interface ระหว่างแบบปกติกับแบบแบนได้ในตารางคราฟต์

## Settings

การตั้งค่า

ช่องบนของ Interface กำหนดรายการที่จะเก็บสต็อกไว้ภายใน เมื่อใส่ไอเทมหรือ
ลากจาก JEI/REI จะมีประแจให้กำหนดจำนวน

คลิกขวาด้วยภาชนะของเหลว (เช่น Bucket หรือถังของเหลว) เพื่อกำหนดของเหลวนั้นเป็นตัวกรอง แทนที่จะกรองตัวไอเทมภาชนะ

## Upgrades

อัปเกรด

Interface รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="fuzzy_card" /> ให้กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="crafting_card" /> ให้ Interface ส่งคำขอไปยังระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
    เพื่อรับไอเทมที่ต้องการ โดยจะดึงจากที่เก็บก่อนหากมี แล้วจึงส่งคำขอ
    คราฟต์ชิ้นใหม่

## Priority

ลำดับความสำคัญ

ตั้งลำดับความสำคัญโดยคลิกประแจมุมขวาบนของหน้าจอ Interface ที่มีลำดับสูงกว่าจะได้รับไอเทม
ก่อนตัวที่มีลำดับต่ำกว่า

## Recipes

สูตรคราฟต์

<Recipe id="network/blocks/interfaces_interface" />

<RecipeFor id="cable_interface" />
