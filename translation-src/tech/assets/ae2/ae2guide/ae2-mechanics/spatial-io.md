---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: Spatial IO
  icon: spatial_storage_cell_2
---

# Spatial IO

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/spatial_storage_1x1x1.snbt" />

  <BoxAnnotation color="#33dd33" min="1 1 1" max="2 2 2">
        ปริมาตรพื้นที่ที่จะย้าย
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />

</GameScene>

Spatial IO ใช้ตัดและวางปริมาตรพื้นที่จริงในโลกได้ ใช้ย้าย <ItemLink id="flawless_budding_quartz" />
สร้างห้องในฐานที่สลับภายในเพื่อใช้งานหลายแบบ หรือแม้แต่ย้าย
End Portal ก็ได้!

ระบบทำงานโดย *สลับ* พื้นที่ที่กำหนดกับพื้นที่ขนาดเท่ากันในมิติจัดเก็บเชิงมิติ ส่งสิ่งที่อยู่
ในแนว Pylon ไปยังมิตินั้น และส่งสิ่งที่อยู่ในมิตินั้นกลับมายังแนว Pylon

หากมีวิธีเดินทางข้ามมิติ ก็ใช้พื้นที่นี้เป็นเครื่องจักรขนาดกะทัดรัดหรือมิติย่อยที่กำหนดขนาดเองได้
(Spatial IO *ใช้* สร้างเครื่องวาร์ปได้ แต่ซับซ้อน ค่อนข้างติดขัด และอยู่นอกขอบเขตคู่มือนี้)

# The Multiblock Setup

การจัดวางมัลติบล็อก

Spatial IO ต้องจัดส่วนประกอบตามรูปแบบที่กำหนด เพื่อให้ทำงานและระบุพื้นที่ที่จะตัดวางได้

ส่วนประกอบทั้งหมดต้องอยู่ใน[เครือข่าย](me-network-connections.md)เดียวกัน และหนึ่งเครือข่ายมีระบบ
Spatial IO ได้เพียงชุดเดียว จึงแนะนำให้ใช้[เครือข่ายย่อย](subnetworks.md)

## The Spatial IO Port

Spatial IO Port

<BlockImage id="spatial_io_port" p:powered="true" scale="4" />

<ItemLink id="spatial_io_port" /> ควบคุมการทำงานของ Spatial IO แสดงสถิติของมัลติบล็อก และใช้ใส่
[Spatial Cell](../items-blocks-machines/spatial_cells.md)

หน้าจอแสดง
- [พลังงาน](energy.md)ที่เก็บอยู่และความจุสูงสุดของเครือข่าย
- พลังงานที่ต้องใช้ต่อครั้ง ซึ่งอาจสูงมากและใช้ทั้งหมดในทันที จึงต้องมี
  [Energy Cell](../items-blocks-machines/energy_cells.md) มากพอเก็บพลังงานให้ครบ
- ประสิทธิภาพของแนว Pylon
- ขนาดพื้นที่ที่กำหนด

ใส่ Spatial Storage Cell ในช่องรับ แล้วส่งพัลส์เรดสโตนให้ Spatial IO Port เพื่อเริ่มทำงาน
ระบบจะ *สลับ* พื้นที่ภายใน Pylon กับพื้นที่ในมิติจัดเก็บ หากส่งบล็อกชุดหนึ่ง
ไปมิติจัดเก็บ แล้ว *วางบล็อกอีกชุดในแนว Pylon* จากนั้นใส่เซลล์กลับช่องรับ
และสั่ง IO Port อีกครั้ง บล็อกชุดที่ 2 จะหายไป และชุดที่ 1 จะกลับมา

**ระวัง! เอนทิตีทุกตัวในพื้นที่ รวมถึงคุณ จะถูกย้ายไปด้วย หากไม่มีทางออก คุณจะติดอยู่
ในกล่องมืดที่ว่างเปล่าในมิติจัดเก็บเชิงมิติ** จะใช้แกล้งเพื่อนก็ได้นะ!

## Pylons

Pylon

<BlockImage id="spatial_pylon" p:powered_on="true" scale="4" />

<ItemLink id="spatial_pylon" /> เป็นส่วนหลักของระบบ Spatial IO ใช้กำหนดพื้นที่ที่จะย้าย

พื้นที่ถูกกำหนดจากกรอบนอกของแนว Pylon แล้วย่อเข้ามา 1 บล็อกในทุกทิศทาง

กฎมีดังนี้:
- ขนาดขั้นต่ำ 3x3x3 ซึ่งกำหนดพื้นที่ภายใน 1x1x1
- Spatial Pylon ทุกชิ้นต้องอยู่ในกรอบชั้นนอก
- Spatial Pylon ทุกชิ้นต้องอยู่เครือข่ายเดียวกัน
- Pylon แต่ละแนวต้องยาวอย่างน้อย 2 บล็อก

ตัวอย่าง หากต้องการพื้นที่ 3x3x3 ตามกฎข้อ 2 ต้องวาง Pylon ทุกชิ้นในเปลือกขนาด 5x5x5 รอบ
พื้นที่ที่กำหนด จัดรูปแบบได้แทบอิสระ ตราบใดที่อยู่ในเปลือกหนา 1 บล็อก
ขนาด 5x5x5 นี้

<GameScene zoom="4" interactive={true}>
<ImportStructure src="../assets/assemblies/spatial_storage_3x3x3_pylon_demonstration.snbt" />

<BoxAnnotation color="#33dd33" min="1 1 1" max="4 4 4">
        ปริมาตรพื้นที่ที่จะย้าย
  </BoxAnnotation>

<BoxAnnotation color="#3333ff" min="5 5 0" max="0 0 5">
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

ตัวอย่างที่จัดวางเหมาะสมกว่า:

<GameScene zoom="4" interactive={true}>
<ImportStructure src="../assets/assemblies/better_spatial_storage_3x3x3.snbt" />

<BoxAnnotation color="#33dd33" min="1 1 1" max="4 4 4">
        ปริมาตรพื้นที่ที่จะย้าย
  </BoxAnnotation>

<BoxAnnotation color="#3333ff" min="5 5 0" max="0 0 5">
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Efficiency

ประสิทธิภาพ

ประสิทธิภาพขึ้นกับสัดส่วนเปลือกที่เติม Pylon หากวางน้อยมากรอบพื้นที่ขนาดใหญ่
ประสิทธิภาพจะต่ำมาก และอาจต้องใช้พลังงาน AE *หลายพันล้าน* หน่วย

## Cell Dimensions

ขนาดมิติของเซลล์

เมื่อใช้ [Spatial Cell](../items-blocks-machines/spatial_cells.md) แล้ว จะกำหนดขนาดแกน XYZ ถาวร เช่น 3x4x2
และเชื่อมกับพื้นที่หนึ่งในมิติจัดเก็บ **หลังใช้แล้วจะรีเซ็ต ล้างรูปแบบ หรือปรับขนาด Spatial Cell
ไม่ได้** หากต้องการขนาดอื่น ให้สร้างเซลล์ใหม่

ขนาดนี้ต่างจากตัวเลขในชื่อเซลล์ เช่นเซลล์ 16^3 รองรับขนาดใดก็ได้ *ไม่เกิน* 16x16x16

พื้นที่มีทิศทางและหมุนไม่ได้ ดังนั้น 2x2x3 ไม่เหมือน 3x2x2 แม้จะมี
ปริมาตรเท่ากัน

หากขนาดแกน XYZ ของเซลล์ไม่ตรงกับพื้นที่ที่กำหนด ซึ่งดูได้ใน IO Port เครื่องจะไม่ทำงาน