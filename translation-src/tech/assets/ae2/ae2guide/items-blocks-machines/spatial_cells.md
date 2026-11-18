---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Spatial Cells
  icon: spatial_storage_cell_128
  position: 410
categories:
- tools
item_ids:
- ae2:spatial_storage_cell_2
- ae2:spatial_storage_cell_16
- ae2:spatial_storage_cell_128
- ae2:spatial_cell_component_2
- ae2:spatial_cell_component_16
- ae2:spatial_cell_component_128
---

# Spatial Storage Cells

เซลล์เก็บพื้นที่มิติ

  <Row>
    <ItemImage id="spatial_storage_cell_2" scale="4" />

    <ItemImage id="spatial_storage_cell_16" scale="4" />

    <ItemImage id="spatial_storage_cell_128" scale="4" />
  </Row>

Spatial Storage Cell ใช้ [เก็บปริมาตรพื้นที่จริง](../ae2-mechanics/spatial-io.md)
โดยใส่ใน <ItemLink id="spatial_io_port" />

ต่างจาก [Storage Cell](../items-blocks-machines/storage_cells.md) ตรงที่ Spatial Cell ฟอร์แมตใหม่ไม่ได้

ย้ำอีกครั้ง เมื่อใช้แล้ว คุณรีเซ็ต ฟอร์แมตใหม่ หรือเปลี่ยนขนาด Spatial Cell ไม่ได้ หากต้องการใช้ขนาดอื่น ให้สร้างเซลล์ใหม่


## Recipes

สูตรคราฟต์

  <Row>
    <Recipe id="network/cells/spatial_storage_cell_2_cubed_storage" />

    <Recipe id="network/cells/spatial_storage_cell_16_cubed_storage" />

    <Recipe id="network/cells/spatial_storage_cell_128_cubed_storage" />
  </Row>

# Housings

ตัวเรือน

สร้างเซลล์โดยประกอบ Spatial Component กับ Housing หรือใช้สูตร Housing ล้อมรอบ Spatial Component:

<Row>
  <Recipe id="network/cells/spatial_storage_cell_2_cubed" />

  <Recipe id="network/cells/spatial_storage_cell_2_cubed_storage" />
</Row>

คราฟต์ Housing แยกได้ดังนี้:

  <RecipeFor id="item_cell_housing" />

# Spatial Components

ส่วนประกอบมิติ

Spatial Component เป็นแกนกลางของ Spatial Storage Cell แต่ละระดับเพิ่มขนาดปริมาตรที่เก็บได้
เป็น 8 เท่า

  <Row>
    <RecipeFor id="spatial_cell_component_2" />

    <RecipeFor id="spatial_cell_component_16" />

    <RecipeFor id="spatial_cell_component_128" />
  </Row>