---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Controller
  icon: controller
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:controller
---

# The Controller

<BlockImage id="controller" p:state="online" scale="8" />

Controller เป็นศูนย์กลางกำหนดเส้นทางของ [เครือข่าย ME](../ae2-mechanics/me-network-connections.md)
หากไม่มี เครือข่ายจะเป็นแบบ "เฉพาะกิจ" และมี [อุปกรณ์](../ae2-mechanics/devices.md) ที่ใช้ช่องสัญญาณได้รวมสูงสุดเพียง 8 ชิ้น

มี Controller 2 ชุดใน [เครือข่าย ME](../ae2-mechanics/me-network-connections.md) เดียวกันไม่ได้

Controller ให้ 32 [ช่องสัญญาณ](../ae2-mechanics/channels.md) ต่อด้าน

Controller ต้องใช้ 6 AE/t ต่อบล็อกเพื่อทำงาน
แต่ละบล็อกเก็บได้ 8000 AE เครือข่ายขนาดใหญ่จึงอาจต้องเพิ่มที่เก็บพลังงาน
ดูรายละเอียดที่ [พลังงาน](../ae2-mechanics/energy.md)

สร้าง Controller หลายบล็อกเป็นรูปทรงได้ค่อนข้างอิสระ

<GameScene zoom="2" background="transparent">
  <ImportStructure src="../assets/assemblies/controllers.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

แต่ต้องทำตามกฎดังนี้:

1.  บล็อก Controller ทุกบล็อกใน [เครือข่าย ME](../ae2-mechanics/me-network-connections.md) ต้องเชื่อมติดกัน มิฉะนั้นจะเปลี่ยนเป็นสีแดง
2.  ขนาด Controller ต้องอยู่ภายใน 7x7x7 มิฉะนั้นจะเปลี่ยนเป็นสีแดง
3.  Controller หนึ่งบล็อกมีบล็อกติดกันสองฝั่งได้ไม่เกิน 1 แกน หากละเมิดกฎนี้ บล็อกจะหยุดทำงานและเป็นสีแดง

<GameScene zoom="2" background="transparent">
  <ImportStructure src="../assets/assemblies/controller_rules.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

หากทำตามกฎทั้งหมดและได้รับพลังงาน Controller จะเรืองแสง
และสลับสีไปมา

คลิกขวาที่ Controller เพื่อเปิดหน้าจอเดียวกับ <ItemLink id="network_tool" /> ได้

## Recipe

สูตรคราฟต์

<RecipeFor id="controller" />
