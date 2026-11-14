---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: ตัวประมวลผล
  icon: logic_processor
  position: 010
categories:
- misc ingredients blocks
item_ids:
- ae2:logic_processor
- ae2:calculation_processor
- ae2:engineering_processor
- ae2:printed_silicon
- ae2:printed_logic_processor
- ae2:printed_calculation_processor
- ae2:printed_engineering_processor
- ae2:silicon
---

# Processors

ตัวประมวลผล

<Row>
  <ItemImage id="logic_processor" scale="4" />

  <ItemImage id="calculation_processor" scale="4" />

  <ItemImage id="engineering_processor" scale="4" />
</Row>

Processor เป็นวัตถุดิบหลักอย่างหนึ่งของ [อุปกรณ์](../ae2-mechanics/devices.md) และเครื่องจักร AE2 อีกทั้งเป็นหนึ่งในความท้าทาย
ด้านระบบอัตโนมัติครั้งใหญ่ช่วงแรก มี 3 ชนิด ซึ่งใช้ Gold, <ItemLink id="certus_quartz_crystal" />
และ Diamond ตามลำดับ ผลิตโดยใช้ [แม่พิมพ์](presses.md) ใน <ItemLink id="inscriber" /> ผ่านกระบวนการหลายขั้น
(มักทำด้วย Inscriber หลายเครื่องต่อกันและระบบท่อที่กรองไอเทม)

## Production Steps

ขั้นตอนการผลิต

<Column gap="5">
  1.  รวบรวมหรือผลิตวัตถุดิบที่ต้องใช้: Silicon, Redstone, Gold, <ItemLink id="certus_quartz_crystal" />, Diamond

  <RecipeFor id="silicon" />

  <br />

  2.  ปั๊มชิ้นส่วนวงจรพิมพ์ที่ต้องใช้ก่อน

  <Row>
    <RecipeFor id="printed_silicon" />

    <RecipeFor id="printed_logic_processor" />
  </Row>

  <Row>
    <RecipeFor id="printed_calculation_processor" />

    <RecipeFor id="printed_engineering_processor" />
  </Row>

  <br />

  3.  ประกอบขั้นสุดท้าย

  <Row>
    <RecipeFor id="logic_processor" />

    <RecipeFor id="calculation_processor" />
  </Row>

  <RecipeFor id="engineering_processor" />
</Column>
