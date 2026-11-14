---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Quantum Bridge
  icon: quantum_ring
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:quantum_link
- ae2:quantum_ring
---

# The Quantum Network Bridge

![Quantum Network Bridge ที่ประกอบเสร็จ](../assets/diagrams/quantum_bridge_demonstration.png)

Quantum Network Bridge ขยาย [เครือข่าย](../ae2-mechanics/me-network-connections.md) ได้ไกลไม่จำกัดและข้ามมิติได้
ส่งช่องสัญญาณได้รวม 32 ช่อง (ไม่ว่าสายจะต่อเข้าด้านต่าง ๆ อย่างไร)
จึงทำงานเหมือน [Dense Cable](cables.md#dense-cable) แบบไร้สาย

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_2.snbt" />

  <BoxAnnotation color="#33dd33" min="1 1 1" max="6 2 3">
        สายในจินตนาการระหว่างปลายทั้งสอง
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

โปรดทราบว่า **ต้องโหลดชังก์ทั้งสองฝั่ง** จึงต้องใช้ <ItemLink id="spatial_anchor" /> หรือเครื่องโหลดชังก์อื่น
หากปลายทั้งสองอยู่ห่างกัน

# Quantum Ring

<BlockImage id="quantum_ring" scale="8" />

วางบล็อกนี้แปดชิ้นรอบ <ItemLink id="quantum_link" /> เพื่อสร้าง
Quantum Network Bridge มีเพียงบล็อก <ItemLink id="quantum_ring" /> 4 ชิ้นที่ติดกับ
<ItemLink id="quantum_link" /> เท่านั้นที่รับการเชื่อมต่อเครือข่าย
บล็อกมุมทั้ง 4 ต่อสายไม่ได้

## Recipe

สูตรคราฟต์

<RecipeFor id="quantum_ring" />

# Quantum Link Chamber

<BlockImage id="quantum_link" scale="8" />

วางบล็อกนี้หนึ่งชิ้นให้ <ItemLink id="quantum_ring" /> ล้อมรอบ
เพื่อสร้าง Quantum Network Bridge บล็อกนี้ไม่ต่อกับสายใด และจะถูกนับ
เป็นส่วนหนึ่งของเครือข่ายเมื่อประกอบสะพานสมบูรณ์แล้วเท่านั้น

ช่องเก็บของของบล็อกนี้ใส่ <ItemLink id="quantum_entangled_singularity" /> ได้เพียงชิ้นเดียว
และระบบอัตโนมัติเข้าถึงได้

## Recipe

สูตรคราฟต์

<RecipeFor id="quantum_link" />
