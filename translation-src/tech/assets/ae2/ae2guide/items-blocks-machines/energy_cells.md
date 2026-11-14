---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: เซลล์พลังงาน
  icon: energy_cell
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_cell
- ae2:dense_energy_cell
- ae2:creative_energy_cell
---

# Energy Cells

เซลล์พลังงาน

<Row gap="20">
  <BlockImage id="energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="dense_energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="creative_energy_cell" scale="8" />
</Row>

Energy Cell เพิ่มที่เก็บ [พลังงาน](../ae2-mechanics/energy.md) ให้เครือข่าย บัฟเฟอร์พลังงานช่วยรองรับ
การใช้พลังงานพุ่งสูงเมื่อใส่หรือดึงไอเทมปริมาณมาก ส่วนที่เก็บขนาดใหญ่ช่วยให้เครือข่ายทำงานต่อได้
ขณะที่ไม่มีการผลิตพลังงาน (เช่น Solar Panel ในตอนกลางคืน) หรือรองรับการใช้พลังงานมหาศาลทันทีของ
[Spatial Storage](../ae2-mechanics/spatial-io.md)

## Fill Bars

ขีดแสดงปริมาณพลังงาน

<Row>
<BlockImage id="energy_cell" scale="4" p:fullness="0" />
<BlockImage id="energy_cell" scale="4" p:fullness="1" />
<BlockImage id="energy_cell" scale="4" p:fullness="2" />
<BlockImage id="energy_cell" scale="4" p:fullness="3" />
<BlockImage id="energy_cell" scale="4" p:fullness="4" />
</Row>

ขีดด้านข้างเซลล์แสดงปริมาณพลังงานที่มี

*   0 ขีดเมื่อชาร์จน้อยกว่า 25%
*   1 ขีดเมื่อชาร์จระหว่าง 25% ถึง 50%
*   2 ขีดเมื่อชาร์จระหว่าง 50% ถึง 75%
*   3 ขีดเมื่อชาร์จระหว่าง 75% ถึง 99%
*   4 ขีดเมื่อชาร์จมากกว่า 99%

## Types Of Cell

ชนิดของเซลล์

*   <ItemLink id="energy_cell" /> เก็บได้ 200k AE เพียงหนึ่งเซลล์ก็น่าจะเพียงพอกับการใช้งานส่วนใหญ่
    และรับมือการใช้พลังงานพุ่งสูงของเครือข่ายปกติได้สบาย
*   <ItemLink id="dense_energy_cell" /> เก็บได้ 1.6M AE เหมาะกับการเดินเครือข่ายด้วยพลังงานสะสม หรือ
    รองรับการใช้พลังงานมหาศาลทันทีของระบบ [Spatial Storage](../ae2-mechanics/spatial-io.md) ขนาดใหญ่
*   <ItemLink id="creative_energy_cell" /> เป็นไอเทมโหมดสร้างสรรค์สำหรับทดสอบ ให้พลังงงงงานไม่มีวันหมด อะไรทำนองนั้น

## Recipes

สูตรคราฟต์

<Row>
  <RecipeFor id="energy_cell" />

  <RecipeFor id="dense_energy_cell" />
</Row>
