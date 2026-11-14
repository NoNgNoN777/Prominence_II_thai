---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Inscriber
  icon: inscriber
  position: 310
categories:
- machines
item_ids:
- ae2:inscriber
---

# The Inscriber

<BlockImage id="inscriber" scale="8" />

Inscriber ใช้จารึกวงจรและ [Processor](processors.md) ด้วย [แม่พิมพ์](presses.md) และบดไอเทมหลายชนิดเป็นฝุ่น
รับได้ทั้งพลังงาน AE2 (AE) หรือ Fabric/Forge Energy (E/FE) ตั้งให้การใส่จากแต่ละด้าน
เข้าไปคนละช่องได้ และหมุนด้วย <ItemLink id="certus_quartz_wrench" /> เพื่อช่วยจัดระบบแบบนี้
อีกทั้งตั้งให้ส่งผลผลิตเข้าช่องเก็บของข้างเคียงได้

ปรับขนาดบัฟเฟอร์ขาเข้าได้ เช่น หากป้อนจากช่องเก็บของเดียวเข้า Inscriber หลายเครื่อง
ควรใช้บัฟเฟอร์เล็กเพื่อกระจายวัตถุดิบระหว่างเครื่องได้เหมาะสม
แทนที่จะเติมเครื่องแรกจนเต็ม 64 ขณะที่เครื่องอื่นว่าง

แม่พิมพ์วงจร 4 ชนิดใช้คราฟต์ [Processor](processors.md)

<Row>
  <ItemImage id="silicon_press" scale="4" />

  <ItemImage id="logic_processor_press" scale="4" />

  <ItemImage id="calculation_processor_press" scale="4" />

  <ItemImage id="engineering_processor_press" scale="4" />
</Row>

ส่วน Name Press ใช้ตั้งชื่อบล็อกได้คล้าย Anvil มีประโยชน์ในการติดป้ายสิ่งต่าง ๆ ใน <ItemLink id="pattern_access_terminal" />

<ItemImage id="name_press" scale="4" />

## Settings

การตั้งค่า

* ตั้งให้ Inscriber แยกด้าน (ตามที่อธิบายด้านล่าง) หรือรับเข้าทุกช่องจากทุกด้านโดยใช้ตัวกรองภายใน
    เลือกช่องปลายทางได้ ในโหมดไม่แยกด้าน จะดึงไอเทมจากช่องบนและช่องล่างไม่ได้
* ตั้งให้ Inscriber ส่งไอเทมเข้าช่องเก็บของข้างเคียงได้
* ปรับขนาดบัฟเฟอร์ขาเข้าได้ แบบใหญ่เหมาะกับเครื่องเดี่ยวที่ป้อนด้วยมือ
แบบเล็กช่วยให้จัดระบบเครื่องหลายตัวทำงานขนานกันได้ดีขึ้น

## The GUI And Sidedness

หน้าจอและการแยกด้าน

ในโหมดแยกด้าน Inscriber จะเลือกช่องตามด้านที่ใส่หรือดึงไอเทม

![หน้าจอ Inscriber](../assets/diagrams/inscriber_gui.png) ![ด้านต่าง ๆ ของ Inscriber](../assets/diagrams/inscriber_sides.png)

A. **ช่องเข้าบน** เข้าถึงจากด้านบนของ Inscriber (ใส่และดึงไอเทมจากช่องนี้ได้)

B. **ช่องเข้ากลาง** ใส่จากด้านซ้าย ขวา หน้า และหลังของ Inscriber (ใส่ได้อย่างเดียว ดึงออกไม่ได้)

C. **ช่องเข้าล่าง** เข้าถึงจากด้านล่างของ Inscriber (ใส่และดึงไอเทมจากช่องนี้ได้)

D. **ช่องออก** ดึงจากด้านซ้าย ขวา หน้า และหลังของ Inscriber (ดึงได้อย่างเดียว ใส่เข้าไม่ได้)

## Simple Automation

ระบบอัตโนมัติอย่างง่าย

ตัวอย่างเช่น การแยกด้านและการหมุนทำให้จัด Inscriber แบบกึ่งอัตโนมัติได้ดังนี้:

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/inscriber_hopper_automation.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

หรือเพียงต่อท่อเข้าและออกจาก Inscriber เมื่อใช้โหมดไม่แยกด้าน

## Upgrades

อัปเกรด

Inscriber รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้:

*   <ItemLink id="speed_card" />

## Recipe

สูตรคราฟต์

<RecipeFor id="inscriber" />
