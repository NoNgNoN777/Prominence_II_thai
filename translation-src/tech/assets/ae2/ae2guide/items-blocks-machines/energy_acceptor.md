---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Energy Acceptor
  icon: energy_acceptor
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_acceptor
---

# The Energy Acceptor

<Row gap="20">
<BlockImage id="energy_acceptor" scale="8" /> 

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_energy_acceptor.snbt" />
</GameScene>
</Row>

Energy Acceptor แปลงพลังงานทั่วไปจากม็อดเทคอื่นเป็น [พลังงาน](../ae2-mechanics/energy.md) ภายในของ AE2
ที่เรียกว่า AE แม้ <ItemLink id="controller" /> จะทำเช่นนี้ได้เหมือนกัน แต่พื้นที่แต่ละด้านของ Controller มีค่า
จึงมักใช้ Energy Acceptor แทนจะดีกว่า

อัตราแปลง Forge Energy และ Techreborn Energy คือ

*   2 FE = 1 AE (Forge)
*   1 E  = 2 AE (Fabric)

ความเร็วในการแปลงขึ้นอยู่กับปริมาณ AE ที่เครือข่ายเก็บได้ทั้งหมด ด้วยเหตุผลที่อธิบายใน
[หน้านี้](../ae2-mechanics/energy.md)

## Variants

รูปแบบต่าง ๆ

Energy Acceptor มี 2 รูปแบบ คือแบบปกติและแบบแบน/[ชิ้นส่วนย่อย](../ae2-mechanics/cable-subparts.md) ทำให้จัดบางระบบได้กะทัดรัดขึ้น

สลับ Energy Acceptor ระหว่างแบบปกติกับแบบแบนได้ในตารางคราฟต์

## Recipe

สูตรคราฟต์

<RecipeFor id="energy_acceptor" />

<RecipeFor id="cable_energy_acceptor" />