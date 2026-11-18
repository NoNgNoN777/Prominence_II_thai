---
navigation:
  parent: example-setups/example-setups-index.md
  title: ตัวอย่างเครือข่ายหลัก
  icon: controller
---

# An Example "Main Network"

ตัวอย่างเครือข่ายหลัก

ระบบอื่นหลายแบบอ้างถึง "เครือข่ายหลัก" คุณอาจสงสัยว่า [อุปกรณ์](../ae2-mechanics/devices.md) เหล่านี้ทำงาน
ร่วมกันเป็นระบบที่ใช้งานได้อย่างไร นี่คือตัวอย่าง:

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="3.9 0 1.9" max="9.1 5 7.1" thickness="0.05">
        กลุ่ม Pattern Provider และ Assembler ขนาดใหญ่ให้พื้นที่มากสำหรับแพตเทิร์นคราฟต์ ตัดหิน และตีเหล็ก
        รูปแบบตารางหมากรุกให้ Provider ใช้ Assembler หลายตัวขนานกันโดยยังมีขนาดกะทัดรัด
        แบ่งเป็นกลุ่มละ 8 เพื่อไม่ให้ช่องสัญญาณหาเส้นทางผิด
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="3.9 0 9.9" max="5.1 3 12.1" thickness="0.05">
        เครื่องจักรบางชนิด พร้อมเครือข่ายย่อยแบบท่อเพื่อส่งผลผลิตเข้า Provider
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="-0.1 0 8.9" max="1.1 3 13.1" thickness="0.05">
      Terminal และอุปกรณ์อรรถประโยชน์ต่าง ๆ (ปกติน่าจะใช้แค่ Crafting Terminal ไม่จำเป็นต้องมีทั้ง Terminal ธรรมดา และ Crafting Terminal)
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="-0.1 0 -0.1" max="2.1 3 8.1" thickness="0.05">
      ชุด Crafting CPU โดยบางตัวมีพื้นที่เก็บมาก และอีกจำนวนหนึ่งมีพื้นที่เก็บน้อยกว่า
      ในการใช้งานจริงน่าจะต้องการ Co-processor มากกว่านี้ แต่จะใหญ่เกินฉากตัวอย่างนี้
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5.9 0 13.9" max="7.1 1 15.1" thickness="0.05">
      Controller ควรอยู่กลางฐาน และน่าจะใหญ่กว่าตัวอย่างนี้เล็กน้อย รูปทรงแท่งเป็นตัวเลือกที่ดี
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="11.9 0 7.9" max="13.1 4 13.1" thickness="0.05">
        วิธีจัดเก็บหลายแบบด้วย Drive หรือ Storage Bus สังเกตว่าทุกอย่างแบ่งเป็นกลุ่มละ 8
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="10.9 0 0.9" max="13.1 2 7.1" thickness="0.05">
        วิธีจัดเก็บหลายแบบด้วย Drive หรือ Storage Bus สังเกตว่าทุกอย่างแบ่งเป็นกลุ่มละ 8
    </BoxAnnotation>

  <IsometricCamera yaw="315" pitch="30" />
</GameScene>
