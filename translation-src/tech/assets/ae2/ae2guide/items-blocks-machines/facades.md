---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Facades
  icon: facade
  icon_nbt: '{item: "minecraft:stone"}'
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:facade
---

# Facades

Facade ช่วยให้ฐานของคุณดูเรียบร้อยขึ้น ปิดสายได้ทั้งสองขนาด และทำจากบล็อกได้หลายชนิด

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/facades_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ปิดได้ทุกด้านของสาย แต่ [ชิ้นส่วนย่อย](../ae2-mechanics/cable-subparts.md) และส่วนเชื่อมต่อสาย
จะยื่นทะลุออกมาได้

<GameScene zoom="6"  interactive={true}>
  <ImportStructure src="../assets/assemblies/facades_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ใช้ให้สร้างสรรค์เพื่อเพิ่มความสวยงามให้ฐาน หรือทำให้แต่ละด้านของบล็อกมีพื้นผิวต่างกัน

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/facades_3.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Hiding Facades

การซ่อน Facade

Facade จะซ่อนเมื่อถือ <a href="network_tool.md">Network Tool</a> ในมือข้างใดก็ได้

คุณโต้ตอบกับบล็อกหลัง Facade ที่ซ่อนอยู่ได้โดยไม่ต้องถอด Facade ก่อน

## Recipe

สูตรคราฟต์

วางบล็อกที่ต้องการนำพื้นผิวมาใช้ไว้ตรงกลาง <ItemLink id="cable_anchor" /> 4 ชิ้น

![สูตร Facade](../assets/diagrams/facade_recipe.png)
