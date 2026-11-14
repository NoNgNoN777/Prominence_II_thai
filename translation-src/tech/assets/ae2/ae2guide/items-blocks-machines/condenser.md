---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Matter Condenser
  icon: condenser
  position: 310
categories:
- machines
item_ids:
- ae2:condenser
---

# The Matter Condenser

<BlockImage id="condenser" scale="8" />

Matter Condenser ใช้เป็นถังขยะหรือผลิต <ItemLink id="matter_ball" /> และ
[Singularity](singularities.md) ได้ รับไอเทม ของเหลว และสิ่งอื่น ๆ ที่ Storage Cell เก็บได้

## Settings/Recipes

การตั้งค่า/สูตรคราฟต์

*   โหมดถังขยะจะทำลายทุกอย่างที่ใส่เข้ามา
*   โหมด Matter Ball ผลิต <ItemLink id="matter_ball" /> จากสิ่งที่ใส่เข้าไป
    ต้องใส่ Storage Component ในช่องบนของเครื่อง แต่ละชิ้นใช้ไอเทมหรือของเหลว 256 ถังตัก
    ดังนั้น <ItemLink id="cell_component_1k" /> (ความจุ 8192 bits) ก็เพียงพอแล้ว
*   โหมด Matter Singularity ผลิต [Singularity](singularities.md) จากสิ่งที่ใส่เข้าไป
    ต้องใส่ Storage Component ในช่องบนของเครื่อง แต่ละชิ้นใช้ไอเทมหรือของเหลว 256,000 ถังตัก
    ดังนั้น <ItemLink id="cell_component_64k" /> (ความจุ 524,288 bits) ก็เพียงพอแล้ว

โปรดทราบว่าในสองโหมดหลังที่มีการผลิตทรัพยากร Matter Condenser *อาจ* ตันได้
และจะไม่รับสิ่งใดเพิ่มหากบัฟเฟอร์พลังงานและผลผลิตเต็มทั้งคู่

## Recipe

สูตรคราฟต์

<RecipeFor id="condenser" />
