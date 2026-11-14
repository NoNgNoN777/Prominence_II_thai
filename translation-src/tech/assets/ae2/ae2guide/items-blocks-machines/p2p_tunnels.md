---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: P2P Tunnels
  icon: me_p2p_tunnel
  position: 210
categories:
- devices
item_ids:
- ae2:me_p2p_tunnel
- ae2:redstone_p2p_tunnel
- ae2:item_p2p_tunnel
- ae2:fluid_p2p_tunnel
- ae2:fe_p2p_tunnel
- ae2:light_p2p_tunnel
---

# Point To Point Tunnels

อุโมงค์เชื่อมจุดต่อจุด

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_tunnels.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

P2P Tunnel ใช้ขนส่งไอเทม ของเหลว สัญญาณเรดสโตน พลังงาน แสง และ [ช่องสัญญาณ](../ae2-mechanics/channels.md)
ไปรอบเครือข่ายโดยไม่โต้ตอบกับเครือข่ายโดยตรง มีหลายรุ่น แต่ละรุ่น
ส่งได้เฉพาะสิ่งของประเภทของมัน คล้ายประตูที่เชื่อมด้านของบล็อกสองด้าน
ในระยะไกล ไม่ได้ทำงานสองทิศทาง แต่กำหนดขาเข้าและขาออกชัดเจน

![ประตู](../assets/assemblies/p2p_portal.png)

ตัวอย่างเช่น Hopper ที่หันเข้า Item P2P จะทำงานเหมือนต่อกับ Barrel โดยตรง และไอเทมจะไหลผ่าน

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_hopper_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

แต่ Barrel สองใบที่วางติดกันจะไม่ส่งไอเทมให้กัน

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_barrel_barrel.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

มีรุ่นอื่นด้วย เช่น Redstone P2P

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_redstone.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Types Of P2P Tunnel And Attunement

ชนิดของ P2P Tunnel และการปรับชนิด

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_tunnels.snbt" />
  <IsometricCamera yaw="180" pitch="90" />
</GameScene>

P2P Tunnel มีหลายชนิด คราฟต์ได้โดยตรงเฉพาะ ME P2P Tunnel ส่วนชนิดอื่นทำโดยคลิกขวาที่
P2P Tunnel ด้วยไอเทมบางชนิด:
- เลือก ME P2P Tunnel โดยคลิกขวาด้วย [สาย](../items-blocks-machines/cables.md) ชนิดใดก็ได้
- เลือก Redstone P2P Tunnel โดยคลิกขวาด้วยส่วนประกอบเรดสโตนหลายชนิด
- เลือก Item P2P Tunnel โดยคลิกขวาด้วย Chest หรือ Hopper
- เลือก Fluid P2P Tunnel โดยคลิกขวาด้วย Bucket หรือ Bottle
- เลือก Energy P2P Tunnel โดยคลิกขวาด้วยไอเทมที่บรรจุพลังงานได้แทบทุกชนิด
- เลือก Light P2P Tunnel โดยคลิกขวาด้วย Torch หรือ Glowstone

บางชนิดมีกฎเฉพาะ เช่น ช่องสัญญาณของ ME P2P Tunnel ผ่าน ME P2P Tunnel อื่นไม่ได้ และ
Energy P2P Tunnel เก็บค่าผ่านทางทางอ้อม 5% ของ FE หรือ E ที่ไหลผ่าน โดยเพิ่ม
[พลังงาน](../ae2-mechanics/energy.md) ที่มันใช้

## The Most-Used Form of P2P

รูปแบบ P2P ที่ใช้บ่อยที่สุด

การใช้งาน P2P Tunnel ที่พบบ่อยที่สุดคือใช้ ME P2P Tunnel เพิ่มความหนาแน่นการส่ง [ช่องสัญญาณ](../ae2-mechanics/channels.md)
แทนที่จะลาก Dense Cable หลายเส้น ก็ใช้ Dense Cable เส้นเดียวส่งช่องสัญญาณจำนวนมากได้

ในตัวอย่างนี้ ME P2P ขาเข้า 8 ตัวรับ 256 ช่องสัญญาณ (8*32) จาก <ItemLink id="controller" /> ของเครือข่ายหลัก และ ME P2P ขาออก 8 ตัว
ส่งออกที่อื่น สังเกตว่าปลายขาเข้าหรือขาออกแต่ละตัวใช้ 1 ช่องสัญญาณ เราจึงส่งหลายช่อง
ผ่านสายเล็กได้ และเพราะ P2P Tunnel อยู่ใน [เครือข่ายย่อย](../ae2-mechanics/subnetworks.md) เฉพาะ จึงไม่
ใช้ช่องสัญญาณของเครือข่ายหลักเลย! แม้ติด P2P Tunnel ตรงกับ Controller ได้ แต่แทรก
[Dense Smart Cable](../items-blocks-machines/cables.md#smart-cable) เพื่อเห็นช่องสัญญาณได้ง่ายขึ้นก็ได้

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/p2p_compact_channels.snbt" />

  <BoxAnnotation color="#dddddd" min="1.3 1.3 6.3" max="2 2.7 6.7">
        Quartz Fiber แบ่งพลังงานระหว่างเครือข่ายหลักกับเครือข่ายย่อย P2P
  </BoxAnnotation>

  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

อีกตัวอย่าง (รวมการใช้กับ [Quantum Bridge](quantum_bridge.md)) ดูภาพ MS Paint นี้ที่ผู้เขียนขี้เกียจ
ปรับแต่งให้สวย:

![P2P และ Quantum Bridge](../assets/diagrams/p2p_quantum_network.png)

## Nesting

การซ้อนกัน

แต่ใช้วิธีนี้ส่งช่องสัญญาณไม่จำกัดผ่านสายเส้นเดียวไม่ได้ ช่องสัญญาณของ ME P2P Tunnel จะไม่
ผ่าน ME P2P Tunnel อีกตัว จึงซ้อนวนซ้ำไม่ได้ สังเกตว่า ME P2P ชั้นนอก
บนสายสีแดงออฟไลน์ กฎนี้ใช้เฉพาะ ME P2P ส่วนชนิดอื่นผ่าน ME P2P ได้
ดังที่ Redstone P2P ยังทำงานปกติ

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_nesting.snbt" />
  <IsometricCamera yaw="225" pitch="30" />
</GameScene>

## Linking

การเชื่อมโยง

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/p2p_linking_frequency.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

เชื่อมปลาย P2P Tunnel เข้าคู่กันด้วย <ItemLink id="memory_card" /> ความถี่จะแสดง
เป็นตารางสี 2x2 ด้านหลัง Tunnel
- Shift+คลิกขวาเพื่อสร้างความถี่เชื่อมโยง P2P ใหม่
- คลิกขวาเพื่อวางการตั้งค่า การ์ดอัปเกรด หรือความถี่เชื่อมโยง

Tunnel ที่ Shift+คลิกขวาจะเป็นขาเข้า ส่วนตัวที่คลิกขวาจะเป็นขาออก มีขาออกหลายตัวได้
แต่สำหรับ ME P2P ช่องสัญญาณที่เข้าจะถูกแบ่งระหว่างขาออก จึงทำสำเนาช่องสัญญาณไม่ได้

## Recipe

สูตรคราฟต์

<RecipeFor id="me_p2p_tunnel" />