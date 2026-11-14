---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Matter Cannon
  icon: matter_cannon
  position: 410
categories:
- tools
item_ids:
- ae2:matter_cannon
---

# The Matter Cannon

<ItemImage id="matter_cannon" scale="4" />

Matter Cannon เป็นปืนรางแม่เหล็กแบบพกพาที่ใช้ไอเทมเล็ก ๆ เป็นกระสุนได้ เช่น <ItemLink id="matter_ball" /> และ Nugget โลหะ
ความเสียหายขึ้นกับไอเทมที่ยิง โดยของที่ "หนัก" อย่าง Gold Nugget (ความเสียหาย 10) แรงกว่าของเบาอย่าง Matter Ball (ความเสียหาย 2)
ใช้พลังงานพื้นฐาน 1600 AE ต่อนัด

เมื่อตัวเลือกตั้งค่า "matterCannonBlockDamage" เป็น true ปืนจะทำลายบล็อกตามความแข็งของบล็อก
และความเสียหายของกระสุน

ชาร์จพลังงานกลับได้ใน <ItemLink id="charger" />

Matter Cannon ทำงานเหมือน [Storage Cell](storage_cells.md) วิธีเติมกระสุนที่ง่ายที่สุดคือใส่
ปืนในช่อง Storage Cell ของ <ItemLink id="chest" />

## Upgrades

อัปเกรด

Matter Cannon รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้ โดยใส่ผ่าน <ItemLink id="cell_workbench" />:

*   <ItemLink id="fuzzy_card" /> ให้กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="inverter_card" /> เปลี่ยนตัวกรองจากรายการอนุญาตเป็นรายการปฏิเสธ
*   <ItemLink id="speed_card" /> เพิ่มพลังงานที่ใช้ต่อนัด เพื่อให้ยิงได้แรงขึ้น
*   <ItemLink id="void_card" /> ทำลายไอเทมที่ใส่เข้าเมื่อเซลล์เต็ม ควรกำหนดชนิดที่อนุญาตให้เก็บอย่างระมัดระวัง!
*   <ItemLink id="energy_card" /> เพิ่มความจุแบตเตอรี่

## Recipe

สูตรคราฟต์

<RecipeFor id="matter_cannon" />
