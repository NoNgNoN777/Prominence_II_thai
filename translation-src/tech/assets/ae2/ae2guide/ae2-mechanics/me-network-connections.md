---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: การเชื่อมต่อเครือข่าย
  icon: fluix_glass_cable
---

# Network Connections

การเชื่อมต่อเครือข่าย

## What Does "Network" Mean?

"เครือข่าย" หมายถึงอะไร?

"เครือข่าย" คือกลุ่ม[อุปกรณ์](../ae2-mechanics/devices.md)ที่เชื่อมกันด้วยบล็อกซึ่งส่งผ่าน[ช่องสัญญาณ](../ae2-mechanics/channels.md)ได้
เช่น [สายเคเบิล](../items-blocks-machines/cables.md) หรือเครื่องจักรและ[อุปกรณ์](../ae2-mechanics/devices.md)แบบเต็มบล็อก
(<ItemLink id="charger" />, <ItemLink id="interface" />, <ItemLink id="drive" /> เป็นต้น)
ตามหลักแล้ว สายเคเบิลเพียงเส้นเดียวก็นับเป็นเครือข่าย

## An Aside On Device Positioning

เรื่องตำแหน่งการวางอุปกรณ์

สำหรับ[อุปกรณ์](../ae2-mechanics/devices.md)ที่ทำหน้าที่เฉพาะในเครือข่าย เช่น <ItemLink id="interface" />
ซึ่งส่งของเข้าออก[คลังเครือข่าย](../ae2-mechanics/import-export-storage.md), <ItemLink id="level_emitter" />
ซึ่งอ่านของในคลัง หรือ <ItemLink id="drive" /> ซึ่งเป็นคลังของเครือข่าย
ตำแหน่งทางกายภาพของอุปกรณ์ไม่มีผลต่อหน้าที่นั้น

ย้ำว่า ตำแหน่งทางกายภาพของอุปกรณ์ไม่มีผล สิ่งสำคัญคืออุปกรณ์เชื่อมกับเครือข่ายอยู่
และแน่นอนว่าเชื่อมอยู่กับเครือข่ายใด

## Network Connections

การเชื่อมต่อเครือข่าย

วิธีง่าย ๆ ในการดูว่าสิ่งใดเชื่อมอยู่คือใช้ <ItemLink id="network_tool" /> ซึ่งแสดง
ส่วนประกอบทั้งหมดในเครือข่าย หากเห็นสิ่งที่ไม่ควรมี หรือไม่เห็นสิ่งที่ควรมี แสดงว่ามีปัญหา

ตัวอย่างนี้เป็น 2 เครือข่ายแยกจากกัน

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        เครือข่าย 1
  </BoxAnnotation>

<BoxAnnotation color="#915dcd" min="2 0 0" max="3 2 2">
        เครือข่าย 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ตัวอย่างนี้ก็เป็น 2 เครือข่าย เพราะ <ItemLink id="quartz_fiber" /> แบ่งปัน[พลังงาน](../ae2-mechanics/energy.md)
แต่ไม่เชื่อมเครือข่ายเข้าด้วยกัน

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        เครือข่าย 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="1.3 0 0" max="3 2 2">
        เครือข่าย 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

แต่ตัวอย่างนี้มีเพียง 1 เครือข่าย ไม่ใช่ 2 เครือข่ายแยกกัน [Quantum Bridge](../items-blocks-machines/quantum_bridge.md) ทำงานเหมือน
[Dense Cable](../items-blocks-machines/cables.md#dense-cable) แบบไร้สาย ปลายทั้งสองจึงอยู่เครือข่ายเดียวกัน

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="7 3 3">
        ทั้งหมดคือ 1 เครือข่าย
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ตัวอย่างนี้ก็มีเพียง 1 เครือข่าย สีของ[สายเคเบิล](../items-blocks-machines/cables.md)ไม่ได้กำหนดเครือข่าย มีเพียงสายต่างสีกันที่ไม่เชื่อม
ถึงกัน แต่ทุกสีเชื่อมกับสาย Fluix หรือสายไม่มีสีได้

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        ทั้งหมดคือ 1 เครือข่าย
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Less Intuitive Connections

การเชื่อมต่อที่อาจคาดไม่ถึง

ตัวอย่างนี้มีเพียง 1 เครือข่าย เพราะ <ItemLink id="pattern_provider" /> เป็นอุปกรณ์เต็มบล็อกจึงส่งผ่านสัญญาณเหมือน
สายเคเบิล และ <ItemLink id="inscriber" /> ก็ทำเช่นเดียวกัน การเชื่อมต่อจึงผ่าน
Provider และ Inscriber ไปถึงกัน

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        ทั้งหมดคือ 1 เครือข่าย
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

เพื่อป้องกันการเชื่อมแบบนี้ ซึ่งมีประโยชน์กับระบบคราฟต์อัตโนมัติที่ใช้[เครือข่ายย่อย](../ae2-mechanics/subnetworks.md)
ให้ใช้ <ItemLink id="certus_quartz_wrench" /> คลิกขวาที่ Provider เพื่อเปลี่ยนเป็นแบบกำหนดทิศทาง
ทำให้ไม่ส่งช่องสัญญาณผ่านด้านหนึ่งของบล็อก

<Row gap="40">
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="2 2 2">
        เครือข่าย 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="2 0 0" max="4 2 2">
        เครือข่าย 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_directional_connection.snbt" />

  <BoxAnnotation color="#ee3333" min="1 .3 .3" max="1.3 .7 .7">
        สังเกตว่าสายเคเบิลไม่เชื่อมต่อกัน
  </BoxAnnotation>

  <IsometricCamera yaw="255" pitch="30" />
</GameScene>
</Row>

ส่วนประกอบอื่นที่ไม่เชื่อมเครือข่ายผ่านด้านทำงาน ได้แก่[อุปกรณ์แบบชิ้นส่วน](../ae2-mechanics/cable-subparts.md)
[ต่าง ๆ](../ae2-mechanics/devices.md) ส่วนใหญ่ เช่น <ItemLink id="import_bus" />, <ItemLink id="storage_bus" /> และ
<ItemLink id="cable_interface" />

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/subpart_no_connection.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>