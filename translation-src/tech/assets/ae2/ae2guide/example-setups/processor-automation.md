---
navigation:
  parent: example-setups/example-setups-index.md
  title: การผลิต Processor อัตโนมัติ
  icon: inscriber
---

# Automation of Processor Production

การผลิต Processor อัตโนมัติ

มีหลายวิธีทำ [Processor](../items-blocks-machines/processors.md) อัตโนมัติ และนี่คือวิธีหนึ่ง

รูปแบบทั่วไปนี้ใช้ท่อขนส่งไอเทมชนิดใดก็ได้ ไม่ว่าม็อดจะเรียก Pipe, Conduit, Duct หรือชื่ออื่น
ตราบใดที่ตั้งตัวกรองได้

![The Process FLow Diagram](../assets/diagrams/processor_flow_diagram.png)

ต่อไปนี้อธิบายวิธีทำด้วย AE2 ล้วน โดยใช้ [เครือข่ายย่อยแบบท่อ](pipe-subnet.md)

โปรดทราบว่าระบบนี้ใช้ <ItemLink id="pattern_provider" /> จึงออกแบบให้รวมเข้ากับระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
ของคุณ หากต้องการทำ Processor อัตโนมัติแยกเดี่ยว ให้แทน Pattern Provider ด้วยถังอีกใบ และใส่วัตถุดิบลงถังด้านบนโดยตรง

ระบบนี้ยังรองรับย้อนหลัง
กับ AE2 รุ่นก่อน เพราะแม้ <ItemLink id="inscriber" /> จะจำกัดด้านรับส่ง เครือข่ายย่อยแบบท่อก็ยังส่งเข้า
และดึงออกจากด้านที่ถูกต้อง

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/processor_automation.snbt" />

  <BoxAnnotation color="#dddddd" min="5 1 0" max="6 2 1" thickness=".05">
        (1) Pattern Provider: ใช้การตั้งค่าเริ่มต้น พร้อมแพตเทิร์นแปรรูปที่เกี่ยวข้อง

        <Row>
            ![Logic Pattern](../assets/diagrams/logic_pattern_small.png)
            ![Calculation Pattern](../assets/diagrams/calculation_pattern_small.png)
            ![Engineering Pattern](../assets/diagrams/engineering_pattern_small.png)
        </Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4.7 2 0" max="5 3 1" thickness=".05">
        (2) Storage Bus #1: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="4.3 2 1" thickness=".05">
        (3) Export Bus #1: กรองเฉพาะ Silicon มี Acceleration Card 2 ใบ
        <Row><ItemImage id="silicon" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="4.3 3 1" thickness=".05">
        (4) Export Bus #2: กรองเฉพาะ Gold Ingot มี Acceleration Card 2 ใบ
        <Row><ItemImage id="minecraft:gold_ingot" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="4.3 4 1" thickness=".05">
        (5) Export Bus #3: กรองเฉพาะ Certus Quartz Crystal มี Acceleration Card 2 ใบ
        <Row><ItemImage id="certus_quartz_crystal" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 6 0" max="4.3 5 1" thickness=".05">
        (6) Export Bus #4: กรองเฉพาะ Diamond มี Acceleration Card 2 ใบ
        <Row><ItemImage id="minecraft:diamond" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.3 3 0" max="2 2 1" thickness=".05">
        (7) Export Bus #5: กรองเฉพาะ Redstone Dust มี Acceleration Card 2 ใบ
        <Row><ItemImage id="minecraft:redstone" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 1 0" max="3 2 1" thickness=".05">
        (8) Inscriber #1: ใช้การตั้งค่าเริ่มต้น มี Silicon Press และ Acceleration Card 4 ใบ
        <Row><ItemImage id="silicon_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 3 0" max="3 4 1" thickness=".05">
        (9) Inscriber #2: ใช้การตั้งค่าเริ่มต้น มี Logic Press และ Acceleration Card 4 ใบ
        <Row><ItemImage id="logic_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 4 0" max="3 5 1" thickness=".05">
        (10) Inscriber #3: ใช้การตั้งค่าเริ่มต้น มี Calculation Press และ Acceleration Card 4 ใบ
        <Row><ItemImage id="calculation_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="4 5 0" max="3 6 1" thickness=".05">
        (11) Inscriber #4: ใช้การตั้งค่าเริ่มต้น มี Engineering Press และ Acceleration Card 4 ใบ
        <Row><ItemImage id="engineering_processor_press" scale="2" /> <ItemImage id="speed_card" scale="2" /></Row>
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 2 0" max="1 3 1" thickness=".05">
        (12) Inscriber #5: ใช้การตั้งค่าเริ่มต้น มี Acceleration Card 4 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 2 0" max="3 1 1" thickness=".05">
        (13) Import Bus #1: ใช้การตั้งค่าเริ่มต้น มี Acceleration Card 2 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 4 0" max="3 3 1" thickness=".05">
        (14) Import Bus #2: ใช้การตั้งค่าเริ่มต้น มี Acceleration Card 2 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 5 0" max="3 4 1" thickness=".05">
        (15) Import Bus #3: ใช้การตั้งค่าเริ่มต้น มี Acceleration Card 2 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2.7 6 0" max="3 5 1" thickness=".05">
        (16) Import Bus #4: ใช้การตั้งค่าเริ่มต้น มี Acceleration Card 2 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 3 0" max="1 3.3 1" thickness=".05">
        (17) Storage Bus #2: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1.7 0" max="1 2 1" thickness=".05">
        (18) Storage Bus #3: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 2 0" max="0.7 3 1" thickness=".05">
        (19) Import Bus #5: ใช้การตั้งค่าเริ่มต้น มี Acceleration Card 2 ใบ
        <ItemImage id="speed_card" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="5 0.7 0" max="6 1 1" thickness=".05">
        (20) Storage Bus #4: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.3 2.7 0.3" max="3.7 3 0.7" thickness=".05">
        Quartz Fiber จ่ายพลังงานให้ Inscriber ทั้ง 3 เพราะ Inscriber ทำงานเหมือนสายเคเบิลและส่งต่อพลังงานได้
  </BoxAnnotation>

<DiamondAnnotation pos="7 1.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="185" pitch="5" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="pattern_provider" /> (1) ใช้การตั้งค่าเริ่มต้น พร้อม <ItemLink id="processing_pattern" /> ที่เกี่ยวข้อง

  ![Logic Pattern](../assets/diagrams/logic_pattern.png)
  ![Calculation Pattern](../assets/diagrams/calculation_pattern.png)
  ![Engineering Pattern](../assets/diagrams/engineering_pattern.png)

* <ItemLink id="storage_bus" /> (2, 17, 18, 20) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="export_bus" /> (3-7) กรองเฉพาะวัตถุดิบที่เกี่ยวข้อง และมี <ItemLink id="speed_card" /> 2 ใบ
    <Row>
      <ItemImage id="silicon" scale="2" />
      <ItemImage id="minecraft:gold_ingot" scale="2" />
      <ItemImage id="certus_quartz_crystal" scale="2" />
      <ItemImage id="minecraft:diamond" scale="2" />
      <ItemImage id="minecraft:redstone" scale="2" />
    </Row>
* <ItemLink id="import_bus" /> (13-16, 19) ใช้การตั้งค่าเริ่มต้น และมี <ItemLink id="speed_card" /> 2 ใบ
* <ItemLink id="inscriber" /> ใช้การตั้งค่าเริ่มต้น มี [Press](../items-blocks-machines/presses.md) ที่เกี่ยวข้อง
   และ <ItemLink id="speed_card" /> 4 ใบ
   <Row>
     <ItemImage id="silicon_press" scale="2" />
     <ItemImage id="logic_processor_press" scale="2" />
     <ItemImage id="calculation_processor_press" scale="2" />
     <ItemImage id="engineering_processor_press" scale="2" />
   </Row>

## How It Works

หลักการทำงาน

1. <ItemLink id="pattern_provider" /> ส่งวัตถุดิบลงถัง
2. [เครือข่ายย่อยแบบท่อ](pipe-subnet.md) ชุดแรก (สีส้ม) ดึง Silicon, Redstone Dust และวัตถุดิบของ Processor ชนิดนั้น
   (Gold Ingot, Certus Quartz Crystal หรือ Diamond) จากถัง แล้วใส่ <ItemLink id="inscriber" /> ที่เกี่ยวข้อง
3. <ItemLink id="inscriber" /> สี่เครื่องแรกสร้าง <ItemLink id="printed_silicon" /> และ <ItemLink id="printed_logic_processor" />,
   <ItemLink id="printed_calculation_processor" /> หรือ <ItemLink id="printed_engineering_processor" />
4. [เครือข่ายย่อยแบบท่อ](pipe-subnet.md) ชุดที่สองและสาม (สีเขียว) นำวงจรที่พิมพ์แล้วจาก <ItemLink id="inscriber" /> สี่เครื่องแรก
    ไปใส่ <ItemLink id="inscriber" /> เครื่องที่ห้าซึ่งทำขั้นตอนประกอบสุดท้าย
5. <ItemLink id="inscriber" /> เครื่องที่ห้าประกอบ [Processor](../items-blocks-machines/processors.md)
6. [เครือข่ายย่อยแบบท่อ](pipe-subnet.md) ชุดที่สี่ (สีม่วง) ใส่ Processor กลับใน Pattern Provider เพื่อส่งคืนเครือข่ายหลัก