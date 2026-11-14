---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Spatial Anchor
  icon: spatial_anchor
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:spatial_anchor
---

# The Spatial Anchor

<BlockImage id="spatial_anchor" p:powered="true" scale="8"/>

เครือข่าย AE2 ต้องมีการโหลดชังก์เพื่อให้ [อุปกรณ์](../ae2-mechanics/devices.md) ทำงานได้ และหากโหลดเพียงบางส่วน
อาจทำงานผิดปกติ Spatial Anchor แก้ปัญหานี้โดยบังคับโหลดชังก์ที่เครือข่ายของมันอยู่
เพียงมีสายหนึ่งเส้นข้ามขอบชังก์ ก็เพียงพอที่จะโหลดชังก์ใหม่นั้น

การโหลดส่งผ่าน [Quantum Bridge](quantum_bridge.md) ได้ แต่ไม่ข้ามมิติ ดังนั้นหากคุณเชื่อม Quantum Bridge ไป The Nether
ต้องติดตั้ง Spatial Anchor ทั้งในเครือข่ายฐานและเครือข่ายใน The Nether

ค่าเริ่มต้นจะเปิด random tick ในชังก์ที่โหลดด้วย ปิดได้ในไฟล์ตั้งค่า AE2

หมุนได้ด้วย <ItemLink id="certus_quartz_wrench" /> หากมีเหตุผลอะไรที่ทำให้คุณอยากหมุน

## Settings

การตั้งค่า

*   Spatial Anchor ให้เข้าถึงการตั้งค่าหน่วยพลังงานส่วนกลางเพื่อเลือก AE หรือ E/FE
*   แสดงโฮโลแกรมในโลกเพื่อบอกชังก์ที่กำลังโหลดได้

## Energy

พลังงาน

Spatial Anchor ใช้ [พลังงาน](../ae2-mechanics/energy.md) ตามสมการนี้:

e = 80 + (x\*(x+1))/2

โดย x คือจำนวนชังก์ที่กำลังโหลด

## Recipe

สูตรคราฟต์

<RecipeFor id="spatial_anchor" />
