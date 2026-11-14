---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: เครือข่ายย่อย
---

# Subnetworks

เครือข่ายย่อย

<GameScene zoom="4" interactive={true}>
<ImportStructure src="../assets/assemblies/subnet_demonstration.snbt" />

<DiamondAnnotation pos="6.5 2.5 0.5" color="#00ff00">
        เครือข่ายย่อยขนส่งไอเทม
    </DiamondAnnotation>

<DiamondAnnotation pos="5.5 2.5 0.5" color="#00ff00">
        เครือข่ายย่อยขนส่งของเหลว
    </DiamondAnnotation>

<DiamondAnnotation pos="4.5 2.5 0.5" color="#00ff00">
        Annihilation Plane พร้อมตัวกรอง
    </DiamondAnnotation>

<DiamondAnnotation pos="3.5 2.5 0.5" color="#00ff00">
        เครือข่ายย่อยของ Formation Plane
    </DiamondAnnotation>

<DiamondAnnotation pos="2.5 2.5 0.5" color="#00ff00">
        เครือข่ายย่อยที่ใช้การทำงานร่วมกันของ Interface กับ Storage Bus เป็นคลังย่อย
ให้เครือข่ายหลักเข้าถึงได้
    </DiamondAnnotation>

<DiamondAnnotation pos="1.5 1.5 0.5" color="#00ff00">
        เครือข่ายย่อยขนส่งไอเทมอีกชุด เพื่อส่งไอเทมที่ชาร์จแล้วกลับไปยัง Pattern Provider
    </DiamondAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

"เครือข่ายย่อย" ไม่มีนิยามตายตัว แต่โดยทั่วไปหมายถึงเครือข่ายที่ช่วยสนับสนุน
เครือข่ายหลักหรือทำหน้าที่ย่อยบางอย่าง มักมีขนาดเล็กจนไม่ต้องใช้ Controller โดยมีการใช้งานหลัก 2 อย่าง:

*   จำกัดว่า[อุปกรณ์](../ae2-mechanics/devices.md)ใดเข้าถึงคลังใดได้ เช่น ไม่ควรให้ Import Bus ของเครือข่ายย่อยที่ใช้แทนท่อเข้าถึง
    คลังหลัก ไม่เช่นนั้นจะส่งไอเทมเข้า Storage Cell แทนภาชนะปลายทาง
*   ประหยัดช่องสัญญาณของเครือข่ายหลัก เช่น ให้ Pattern Provider ส่งของเข้า Interface ที่เชื่อมกับ Storage Bus
    หลายตัวบนเครื่องจักรหลายเครื่อง ใช้เพียง 1 ช่องสัญญาณ แทนการติด Pattern Provider ทุกเครื่องซึ่งใช้หลายช่อง

สายเคเบิลต่างสีไม่ได้สร้างเครือข่ายย่อยด้วยตัวมันเอง เพียงแต่จะไม่เชื่อมต่อถึงกัน

ตัวอย่างเครือข่ายย่อย ได้แก่

*   Import Bus กับ Storage Bus ที่ขนไอเทมหรือของเหลวจากภาชนะหนึ่งไปอีกภาชนะเหมือนท่อ
*   Annihilation Plane กับ Storage Bus เพื่อบังคับให้ของที่ทุบได้ไปที่ Storage Bus เท่านั้น จึงใช้ตัวกรองควบคุม Plane ได้
*   Interface กับ Formation Plane เพื่อส่งสิ่งที่ใส่ใน Interface ไปยัง Formation Plane ให้วางหรือปล่อยออกมาในโลก
*   ระบบผลิต Certus Quartz อัตโนมัติที่ควบคุมปริมาณด้วย <ItemLink id="level_emitter" /> บนเครือข่ายหลัก
*   คลังเฉพาะทางที่เครือข่ายหลักเข้าถึงผ่าน Storage Bus บน Interface เพื่อเก็บผลผลิตฟาร์มโดยไม่ทำให้คลังหลักล้นไม่สิ้นสุด
*   และรูปแบบอื่น ๆ

<ItemLink id="quartz_fiber" /> มีประโยชน์มากในการสร้างเครือข่ายย่อย เพราะส่งพลังงานระหว่างเครือข่ายโดยไม่
รวมเครือข่ายเข้าด้วยกัน จึงจ่ายพลังงานให้เครือข่ายย่อยได้โดยไม่ต้องติด Energy Acceptor และสายพลังงานทุกจุด
