---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Annihilation Plane
  icon: annihilation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:annihilation_plane
---

# The Annihilation Plane

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/annihilation_plane.snbt" />
</GameScene>

Annihilation Plane ทุบบล็อกและเก็บไอเทม ทำงานคล้าย <ItemLink id="import_bus" /> โดยส่งสิ่งของ
เข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ไอเทมที่จะถูกเก็บต้องชนกับ
ด้านหน้าของ Plane มันไม่ได้เก็บเป็นบริเวณกว้าง

ลงเอนชานต์ Pickaxe ชนิดใดก็ได้บน Annihilation Plane ดังนั้นคุณลง Fortune สูง ๆ สักสองสามเครื่อง
แล้ว [แปรรูปแร่อัตโนมัติ](../example-setups/ore-fortuner.md) ได้หากม็อดแพ็กอนุญาต นอกจากนี้ Silk Touch ทำงานตามที่คาด
Efficiency ลดพลังงานที่ใช้ทุบบล็อก และ Unbreaking ให้โอกาสไม่ใช้พลังงานเลย

เป็น [ชิ้นส่วนย่อยของสาย](../ae2-mechanics/cable-subparts.md)

อย่าลืมอนุญาต FAKE PLAYER ในพื้นที่เคลมชังก์ของคุณ

## Filtering

การกรอง

Annihilation Plane จะทุบบล็อกหรือเก็บไอเทมก็ต่อเมื่อเก็บของที่ดรอปได้
ในเครือข่ายของมัน ดังนั้นหากต้องการกรอง คุณต้องจำกัดชนิดที่เก็บในเครือข่ายนั้นได้ ซึ่งมักทำโดยวางมัน
บน [เครือข่ายย่อย](../ae2-mechanics/subnetworks.md) แล้วใช้ <ItemLink id="storage_bus" /> หรือ [เซลล์](../items-blocks-machines/storage_cells.md)
ที่ [กำหนดชนิด](cell_workbench.md) ไว้เพื่อให้ได้ผลนี้

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        กรองให้ตรงกับของที่ดรอปจากสิ่งที่ต้องการทุบ
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
        กำหนดให้เก็บเฉพาะของที่ดรอปจากสิ่งที่ต้องการทุบ
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ย้ำว่ามันกรอง ตามไอเทมที่ดรอป เช่น หากต้องการกรองการทุบ <ItemLink id="minecraft:amethyst_cluster" />
ต้องใช้ Plane ที่มี Silk Touch มิฉะนั้นผลึกทุกช่วงก่อนโตเต็มที่จะไม่ดรอปอะไร และ Plane จะทุบเสมอ
ไม่ว่าตั้งตัวกรองอย่างไร เพราะเครือข่ายเก็บ "ความว่างเปล่า" ได้เสมอ

## Recipe

สูตรคราฟต์

<RecipeFor id="annihilation_plane" />
