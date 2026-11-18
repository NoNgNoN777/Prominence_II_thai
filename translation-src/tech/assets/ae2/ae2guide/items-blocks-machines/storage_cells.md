---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: เซลล์จัดเก็บ
  icon: item_storage_cell_1k
  position: 410
categories:
- tools
item_ids:
- ae2:item_cell_housing
- ae2:fluid_cell_housing
- ae2:cell_component_1k
- ae2:cell_component_4k
- ae2:cell_component_16k
- ae2:cell_component_64k
- ae2:cell_component_256k
- ae2:item_storage_cell_1k
- ae2:item_storage_cell_4k
- ae2:item_storage_cell_16k
- ae2:item_storage_cell_64k
- ae2:item_storage_cell_256k
- ae2:fluid_storage_cell_1k
- ae2:fluid_storage_cell_4k
- ae2:fluid_storage_cell_16k
- ae2:fluid_storage_cell_64k
- ae2:fluid_storage_cell_256k
---

# Storage Cells

เซลล์จัดเก็บ

<Column>
  <Row>
    <ItemImage id="item_storage_cell_1k" scale="4" />

    <ItemImage id="item_storage_cell_4k" scale="4" />

    <ItemImage id="item_storage_cell_16k" scale="4" />

    <ItemImage id="item_storage_cell_64k" scale="4" />

    <ItemImage id="item_storage_cell_256k" scale="4" />
  </Row>

  <Row>
    <ItemImage id="fluid_storage_cell_1k" scale="4" />

    <ItemImage id="fluid_storage_cell_4k" scale="4" />

    <ItemImage id="fluid_storage_cell_16k" scale="4" />

    <ItemImage id="fluid_storage_cell_64k" scale="4" />

    <ItemImage id="fluid_storage_cell_256k" scale="4" />
  </Row>
</Column>

Storage Cell เป็นวิธีจัดเก็บหลักอย่างหนึ่งใน Applied Energistics โดยใส่ใน <ItemLink id="drive" />
หรือ <ItemLink id="chest" />

ดู [Bytes และชนิด](../ae2-mechanics/bytes-and-types.md) สำหรับคำอธิบายความจุด้านไบต์และจำนวนชนิด

หากเซลล์ว่าง ถอด Storage Component ออกจาก Housing ได้โดยถือเซลล์แล้ว Shift+คลิกขวา

## Storage Capacity with Varying Type Count

ความจุเมื่อจำนวนชนิดต่างกัน

เนื่องจาก [พื้นที่ตั้งต้นต่อชนิด](../ae2-mechanics/bytes-and-types.md) เซลล์ที่เก็บเพียง 1 ชนิดจึงเก็บจำนวนได้ 2 เท่าของเซลล์ที่ใช้ครบ 63 ชนิด

| เซลล์                                     | ความจุรวมเมื่อใช้ 1 ชนิด | ความจุรวมเมื่อใช้ 63 ชนิด |
| ---------------------------------------- | ----------------------------------------: | ------------------------------------------: |
| <ItemLink id="item_storage_cell_1k" />   |                                     8,128 |                                       4,160 |
| <ItemLink id="item_storage_cell_4k" />   |                                    32,512 |                                      16,640 |
| <ItemLink id="item_storage_cell_16k" />  |                                   130,048 |                                      66,560 |
| <ItemLink id="item_storage_cell_64k" />  |                                   520,192 |                                     266,240 |
| <ItemLink id="item_storage_cell_256k" /> |                                 2,080,768 |                                   1,064,960 |


## Partitioning

การกำหนดชนิดที่อนุญาต

กรองเซลล์ให้รับเฉพาะไอเทมบางชนิดได้ คล้ายการกรอง <ItemLink id="storage_bus" />
โดยตั้งค่าใน <ItemLink id="cell_workbench" />

ลากไอเทมจาก JEI/REI มาใส่ช่องได้ แม้คุณจะไม่มีไอเทมนั้นอยู่จริง

## Upgrades

อัปเกรด

Storage Cell รองรับ [อัปเกรด](upgrade_cards.md) ต่อไปนี้ โดยใส่ผ่าน <ItemLink id="cell_workbench" />:

*   <ItemLink id="fuzzy_card" /> (ใช้กับเซลล์ของเหลวไม่ได้) ให้กรองตามระดับความเสียหายและ/หรือไม่สนใจ NBT ของไอเทม
*   <ItemLink id="inverter_card" /> เปลี่ยนจากรายการอนุญาตเป็นรายการปฏิเสธ
*   <ItemLink id="equal_distribution_card" /> แบ่งพื้นที่ไบต์ให้แต่ละชนิดเท่ากัน ป้องกันชนิดเดียวกินทั้งเซลล์
*   <ItemLink id="void_card" /> ทำลายไอเทมที่ใส่เข้าเมื่อเซลล์เต็ม (หรือเมื่อพื้นที่ของชนิดนั้นเต็ม
    หากใช้ Equal Distribution Card) ช่วยป้องกันฟาร์มตัน ควรกำหนดชนิดที่อนุญาตอย่างระมัดระวัง!
*   เซลล์พกพารับ <ItemLink id="energy_card" /> เพื่อเพิ่มความจุแบตเตอรี่ได้

## Coloring

การเปลี่ยนสี

ย้อมสีเซลล์ไอเทมและของเหลวพกพาได้คล้ายชุดเกราะ Leather โดยคราฟต์ร่วมกับสีย้อม

# Housings

ตัวเรือน

สร้างเซลล์โดยประกอบ Storage Component กับ Housing หรือใช้สูตร Housing ล้อมรอบ Storage Component:

<Row>
  <Recipe id="network/cells/item_storage_cell_1k" />

  <Recipe id="network/cells/item_storage_cell_1k_storage" />
</Row>

คราฟต์ Housing แยกได้ดังนี้:

<Row>
  <RecipeFor id="item_cell_housing" />

  <RecipeFor id="fluid_cell_housing" />
</Row>

# Storage Components

ส่วนประกอบจัดเก็บ

Storage Component เป็นแกนกลางของเซลล์ AE2 ทุกชนิด กำหนดความจุเซลล์ แต่ละระดับเพิ่มความจุ
เป็น 4 เท่า และใช้ชิ้นส่วนระดับก่อนหน้า 3 ชิ้น

<Column>
  <Row>
    <RecipeFor id="cell_component_1k" />

    <RecipeFor id="cell_component_4k" />

    <RecipeFor id="cell_component_16k" />
  </Row>

  <Row>
    <RecipeFor id="cell_component_64k" />

    <RecipeFor id="cell_component_256k" />
  </Row>
</Column>

# Item Storage Cells

เซลล์เก็บไอเทม

เซลล์ไอเทมเก็บไอเทมต่างชนิดได้สูงสุด 63 ชนิด และมีความจุมาตรฐานทุกขนาด

<Column>
  <Row>
    <Recipe id="network/cells/item_storage_cell_1k_storage" />

    <Recipe id="network/cells/item_storage_cell_4k_storage" />

    <Recipe id="network/cells/item_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/item_storage_cell_64k_storage" />

    <Recipe id="network/cells/item_storage_cell_256k_storage" />
  </Row>
</Column>

## Portable Item Storage

ที่เก็บไอเทมแบบพกพา

ทำงานเหมือน <ItemLink id="chest" /> ขนาดจิ๋วในกระเป๋า หรือเหมือนกระเป๋าสะพาย ชาร์จได้ใน <ItemLink id="charger" />

ต่างจาก Storage Cell มาตรฐาน ตรงที่จำนวนชนิดที่เก็บได้จะ ลดลง เมื่อความจุไบต์เพิ่มขึ้น และมี
ความจุไบต์รวมเพียงครึ่งเดียว

นอกจากการ์ดอัปเกรดที่ทุกเซลล์รับได้แล้ว ยังใส่ <ItemLink id="energy_card" /> เพื่อเพิ่มแบตเตอรี่ภายในได้

<Column>
  <Row>
    <RecipeFor id="portable_item_cell_1k" />

    <RecipeFor id="portable_item_cell_4k" />

    <RecipeFor id="portable_item_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_item_cell_64k" />

    <RecipeFor id="portable_item_cell_256k" />
  </Row>
</Column>

# Fluid Storage Cells

เซลล์เก็บของเหลว

เซลล์ของเหลวเก็บของเหลวต่างชนิดได้สูงสุด 5 ชนิด และมีความจุมาตรฐานทุกขนาด

<Column>
  <Row>
    <Recipe id="network/cells/fluid_storage_cell_1k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_4k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/fluid_storage_cell_64k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_256k_storage" />
  </Row>
</Column>

## Portable Fluid Storage

ที่เก็บของเหลวแบบพกพา

ทำงานเหมือน <ItemLink id="chest" /> ขนาดจิ๋วในกระเป๋า หรือเหมือนกระเป๋าสะพาย ชาร์จได้ใน <ItemLink id="charger" />

ต่างจาก Storage Cell มาตรฐาน ตรงที่จำนวนชนิดที่เก็บได้จะ ลดลง เมื่อความจุไบต์เพิ่มขึ้น และมี
ความจุไบต์รวมเพียงครึ่งเดียว

นอกจากการ์ดอัปเกรดที่ทุกเซลล์รับได้แล้ว ยังใส่ <ItemLink id="energy_card" /> เพื่อเพิ่มแบตเตอรี่ภายในได้

<Column>
  <Row>
    <RecipeFor id="portable_fluid_cell_1k" />

    <RecipeFor id="portable_fluid_cell_4k" />

    <RecipeFor id="portable_fluid_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_fluid_cell_64k" />

    <RecipeFor id="portable_fluid_cell_256k" />
  </Row>
</Column>

# Creative Item and Fluid Cells

เซลล์ไอเทมและของเหลวแบบ Creative

<Row>
  <ItemImage id="creative_item_cell" scale="2" />

  <ItemImage id="creative_fluid_cell" scale="2" />
</Row>

เซลล์ไอเทมและของเหลว Creative ไม่ได้ให้พื้นที่เก็บไม่จำกัด แต่เป็นทั้งแหล่งผลิตและที่รับทิ้งไม่จำกัด
ของไอเทมหรือของเหลวที่คุณ [กำหนดชนิด](cell_workbench.md) ไว้
