---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: การ์ดอัปเกรด
  icon: speed_card
  position: 410
categories:
- tools
item_ids:
- ae2:basic_card
- ae2:advanced_card
- ae2:redstone_card
- ae2:capacity_card
- ae2:void_card
- ae2:fuzzy_card
- ae2:speed_card
- ae2:inverter_card
- ae2:crafting_card
- ae2:equal_distribution_card
- ae2:energy_card
---

# Upgrade Cards

การ์ดอัปเกรด

<Row>
  <ItemImage id="redstone_card" scale="2" />

  <ItemImage id="capacity_card" scale="2" />

  <ItemImage id="void_card" scale="2" />

  <ItemImage id="fuzzy_card" scale="2" />

  <ItemImage id="speed_card" scale="2" />

  <ItemImage id="inverter_card" scale="2" />

  <ItemImage id="crafting_card" scale="2" />

  <ItemImage id="equal_distribution_card" scale="2" />

  <ItemImage id="energy_card" scale="2" />
</Row>

การ์ดอัปเกรดเปลี่ยนพฤติกรรมของ [อุปกรณ์](../ae2-mechanics/devices.md) และเครื่องจักร AE2 เช่น เพิ่มความเร็ว เพิ่มความจุ
ตัวกรอง เปิดการควบคุมด้วยเรดสโตน และอื่น ๆ

## Card Components

ส่วนประกอบการ์ด

<Row>
  <ItemImage id="basic_card" scale="2" />

  <ItemImage id="advanced_card" scale="2" />
</Row>

คราฟต์การ์ดจาก Basic Card หรือ Advanced Card

<Row>
  <RecipeFor id="basic_card" />

  <RecipeFor id="advanced_card" />
</Row>

## Redstone Card

<ItemImage id="redstone_card" scale="2" />

Redstone Card เพิ่มการควบคุมด้วยเรดสโตน พร้อมปุ่มในหน้าจออุปกรณ์สำหรับสลับเงื่อนไขสัญญาณหลายแบบ

<RecipeFor id="redstone_card" />

## Capacity Card

<ItemImage id="capacity_card" scale="2" />

Capacity Card เพิ่มช่องกรองของ Import Bus, Export Bus, Storage Bus และ Formation Plane

<RecipeFor id="capacity_card" />

## Overflow Destruction Card

<ItemImage id="void_card" scale="2" />

ใส่ Overflow Destruction Card ใน [Storage Cell](storage_cells.md) ผ่าน <ItemLink id="cell_workbench" /> ได้
มันจะลบไอเทมที่ใส่เข้ามาเมื่อเซลล์เต็ม (อย่าลืม [กำหนดชนิด](cell_workbench.md) ให้เซลล์!) หากใช้ร่วมกับ Equal Distribution Card
จะทำลายไอเทมเมื่อพื้นที่ที่แบ่งให้ไอเทมชนิดนั้นเต็ม แม้ส่วนของชนิดอื่นยังว่าง

<RecipeFor id="void_card" />

## Fuzzy Card

<ItemImage id="fuzzy_card" scale="2" />

Fuzzy Card ให้อุปกรณ์และเครื่องมือที่มีตัวกรองกรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม จึงส่งออก
Iron Axe ทุกเล่มโดยไม่สนความเสียหายและเอนชานต์ หรือส่งเฉพาะ Diamond Sword ที่เสียหายโดยไม่ส่งเล่มที่ซ่อมเต็มได้

ด้านล่างเป็นตัวอย่างโหมดเปรียบเทียบความเสียหายแบบ Fuzzy ด้านซ้ายคือ
การตั้งค่าบัส ด้านบนคือไอเทมที่นำมาเปรียบเทียบ

| 25%                    | Pickaxe เสียหาย 10% | Pickaxe เสียหาย 30% | Pickaxe เสียหาย 80% | Pickaxe ซ่อมเต็ม |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Pickaxe ใกล้พัง  | ✅                   | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            |
| Pickaxe ซ่อมเต็ม | \*\*\*\*            | ✅                   | ✅                   | ✅                   |

| 50%                    | Pickaxe เสียหาย 10% | Pickaxe เสียหาย 30% | Pickaxe เสียหาย 80% | Pickaxe ซ่อมเต็ม |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Pickaxe ใกล้พัง  | ✅                   | ✅                   | \*\*\*\*            | \*\*\*\*            |
| Pickaxe ซ่อมเต็ม | \*\*\*\*            | \*\*\*\*            | ✅                   | ✅                   |

| 75%                    | Pickaxe เสียหาย 10% | Pickaxe เสียหาย 30% | Pickaxe เสียหาย 80% | Pickaxe ซ่อมเต็ม |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Pickaxe ใกล้พัง  | ✅                   | ✅                   | \*\*\*\*            | \*\*\*\*            |
| Pickaxe ซ่อมเต็ม | \*\*\*\*            |                     | ✅                   | ✅                   |

| 99%                    | Pickaxe เสียหาย 10% | Pickaxe เสียหาย 30% | Pickaxe เสียหาย 80% | Pickaxe ซ่อมเต็ม |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Pickaxe ใกล้พัง  | ✅                   | ✅                   | ✅                   | \*\*\*\*            |
| Pickaxe ซ่อมเต็ม | \*\*\*\*            | \*\*\*\*            | \*\*\*\*            | ✅                   |

| ไม่สนใจ                 | Pickaxe เสียหาย 10% | Pickaxe เสียหาย 30% | Pickaxe เสียหาย 80% | Pickaxe ซ่อมเต็ม |
| ---------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Pickaxe ใกล้พัง  | ✅                   | ✅                   | ✅                   | **✅**               |
| Pickaxe ซ่อมเต็ม | **✅**               | **✅**               | **✅**               | ✅                   |

<RecipeFor id="fuzzy_card" />

## Acceleration Card

<ItemImage id="speed_card" scale="2" />

Acceleration Card ทำให้สิ่งต่าง ๆ เร็วขึ้น เช่น เพิ่มจำนวนไอเทมที่ Import Bus และ Export Bus ย้ายต่อครั้ง และทำให้ Inscriber
กับ Assembler ทำงานเร็วขึ้น

<RecipeFor id="speed_card" />

## Inverter Card

<ItemImage id="inverter_card" scale="2" />

Inverter Card เปลี่ยนตัวกรองในอุปกรณ์และเครื่องมือจากรายการอนุญาตเป็นรายการปฏิเสธ

<RecipeFor id="inverter_card" />

## Crafting Card

<ItemImage id="crafting_card" scale="2" />

Crafting Card ให้อุปกรณ์ส่งคำขอไปยังระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
เพื่อรับไอเทมที่ต้องการ

<RecipeFor id="crafting_card" />

## Equal Distribution Card

<ItemImage id="equal_distribution_card" scale="2" />

ใส่ Equal Distribution Card ใน [Storage Cell](storage_cells.md) ผ่าน <ItemLink id="cell_workbench" /> เพื่อ
แบ่งเซลล์เป็นส่วนเท่า ๆ กันตามรายการที่ [กำหนดชนิด](cell_workbench.md) ไว้ ป้องกันไม่ให้ไอเทมชนิดเดียว
กินพื้นที่ทั้งเซลล์

<RecipeFor id="equal_distribution_card" />

## Energy Card

<ItemImage id="energy_card" scale="2" />

Energy Card เพิ่มที่เก็บพลังงานให้เครื่องมือบางชนิด เช่น เทอร์มินัลพกพา และทำให้ <ItemLink id="vibration_chamber" />
มีประสิทธิภาพมากขึ้น

<RecipeFor id="energy_card" />
