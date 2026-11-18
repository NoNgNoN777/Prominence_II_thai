---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: พลังงาน
  icon: energy_cell
---

# Energy

พลังงาน

เครือข่ายต้องใช้พลังงานในการทำงาน โดยมีแหล่งพลังงานส่วนกลางให้[อุปกรณ์](../ae2-mechanics/devices.md)ดึงไปใช้โดยตรง และ
<ItemLink id="vibration_chamber" />, <ItemLink id="energy_acceptor" /> (รวมถึง <ItemLink id="controller" />) ใช้เติมพลังงานเข้าสู่ระบบ ดู
สถิติพลังงานของเครือข่ายได้โดยถือ <ItemLink id="network_tool" /> แล้วคลิกขวาที่ส่วนใดก็ได้ของระบบ หรือ
คลิกขวาที่ Controller หากมี การเก็บและจ่ายพลังงานร่วมกันทั้งเครือข่ายทำให้
ไม่มีข้อจำกัดอัตราถ่ายโอนพลังงาน อุปกรณ์จึงดึงพลังงานได้มากเท่าที่ต้องการ และ
Energy Acceptor รับพลังงานได้ด้วยความเร็วแทบไม่จำกัด โดยมีเพียงความจุพลังงานของระบบเป็นข้อจำกัด

## Energy Accepting

การรับพลังงาน

<Row>
  <BlockImage id="energy_acceptor" scale="4" />

  <GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/blocks/cable_energy_acceptor.snbt" />
  </GameScene>

  <BlockImage id="controller" p:state="online" scale="4" />

  <BlockImage id="vibration_chamber" p:active="true" scale="4" />
  
  <BlockImage id="crystal_resonance_generator" scale="4" />
</Row>

ภายในระบบ AE2 ไม่ได้ใช้ Forge Energy (บน Forge) หรือ TechReborn Energy (บน Fabric) โดยตรง แต่แปลงเป็น
หน่วยของตัวเองคือ AE และแปลงกลับไม่ได้ ใช้ <ItemLink id="energy_acceptor" /> และ
<ItemLink id="controller" /> แปลงพลังงานได้ แต่ควรเก็บด้านต่าง ๆ ของ Controller ไว้เพิ่ม[ช่องสัญญาณ](../ae2-mechanics/channels.md)มากกว่า
ผลิตพลังงานด้วย <ItemLink id="vibration_chamber" /> หรือผลิตแบบต่อเนื่องด้วย <ItemLink id="crystal_resonance_generator" /> ก็ได้ แต่ AE2 ออกแบบ
มาให้ใช้ร่วมกับม็อดเทคอื่นที่ผลิตพลังงานได้ดีกว่า

ดังนั้น เมื่อวางระบบจ่ายพลังงานของฐาน ควรมองเครือข่าย AE2 เป็นเครื่องจักรมัลติบล็อกขนาดใหญ่เครื่องเดียว

อัตราแปลง Forge Energy และ Techreborn Energy คือ

*   2 FE = 1 AE (Forge)
*   1 E  = 2 AE (Fabric)

## Energy Storage

การเก็บพลังงาน

<Row>
  <BlockImage id="energy_cell" scale="4" p:fullness="4" />

  <BlockImage id="dense_energy_cell" scale="4" p:fullness="4" />

  <BlockImage id="creative_energy_cell" scale="4" />
</Row>

เครือข่ายรับหรือใช้พลังงานในหนึ่งทิกได้ไม่เกินความจุที่เก็บได้ หากระบบ
เก็บได้เพียง 800 AE เมื่อ[อุปกรณ์](../ae2-mechanics/devices.md)เรียกใช้พลังงาน จะใช้ได้สูงสุด 800 AE หากพลังงานเต็ม
และ Energy Acceptor จะเติมเข้าสู่เครือข่ายได้สูงสุด 800 AE หากพลังงานหมด

นี่เป็นสาเหตุที่พบบ่อยของอาการแปลก ๆ ในเครือข่ายเล็กที่มีแค่ Energy Acceptor, Drive, Terminal และ
อุปกรณ์ไม่กี่ชิ้น เมื่อเท Cobblestone เต็มช่องเก็บของเข้าสู่ระบบพร้อมกันใน
ทิกเดียว อาจใช้พลังงานมากกว่าที่เก็บอยู่ จึงใส่ Cobblestone ได้ไม่ครบ เครือข่าย
พลังงานหมดและเริ่มทำงานใหม่

แก้ได้ด้วยการเพิ่ม Energy Cell

เครือข่ายมีบัฟเฟอร์พลังงานในตัว 25 AE ต่อสายเคเบิล เครื่องจักร หรือชิ้นส่วนแต่ละชิ้น

<ItemLink id="controller" /> มีความจุพลังงานภายในเล็กน้อยที่ 8,000 AE

<ItemLink id="energy_cell" /> เก็บได้ 200k AE โดยปกติเพียงชิ้นเดียวก็เพียงพอ และรองรับการใช้พลังงานสูงชั่วขณะ
ของเครือข่ายทั่วไปได้สบาย

<ItemLink id="dense_energy_cell" /> เก็บได้ 1.6M AE เหมาะสำหรับใช้พลังงานสำรองเลี้ยงเครือข่าย หรือ
รองรับการดึงพลังงานมหาศาลในทันทีของระบบ[จัดเก็บเชิงมิติ](spatial-io.md)ขนาดใหญ่

<ItemLink id="creative_energy_cell" /> เป็นไอเทมโหมดสร้างสรรค์สำหรับทดสอบ ให้พลังงานไม่จำกัดแบบจัดเต็ม!
