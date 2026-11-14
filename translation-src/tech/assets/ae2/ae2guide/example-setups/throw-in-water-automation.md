---
navigation:
  parent: example-setups/example-setups-index.md
  title: การโยนลงน้ำอัตโนมัติ
  icon: fluix_crystal
---

# Automation of Throwing In Water recipes

ทำสูตรโยนลงน้ำอัตโนมัติ

โปรดทราบว่าระบบนี้ใช้ <ItemLink id="pattern_provider" /> จึงออกแบบให้รวมเข้ากับระบบ [คราฟต์อัตโนมัติ](../ae2-mechanics/autocrafting.md)
ของคุณ

บางสูตรต้องโยนไอเทมลงน้ำ (แต่ใช้ระบบคล้ายกันเพื่อโยนไอเทมไปที่อื่นได้)
ทำอัตโนมัติได้ด้วย <ItemLink id="formation_plane" />, <ItemLink id="annihilation_plane" /> และระบบ
สนับสนุนบางส่วน (โดยพื้นฐานคือ [เครือข่ายย่อยแบบท่อ](pipe-subnet.md) ดัดแปลง 2 ชุด)

ระบบนี้ออกแบบให้ใช้ร่วมกับ [Charger อัตโนมัติ](charger-automation.md) เพื่อจ่าย <ItemLink id="charged_certus_quartz_crystal" />

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/throw_in_water.snbt" />

<BoxAnnotation color="#dddddd" min="2 0 1" max="3 1 2">
        (1) Pattern Provider: ใช้การตั้งค่าเริ่มต้น พร้อมแพตเทิร์นแปรรูปที่เกี่ยวข้อง

        ![Fluix Pattern](../assets/diagrams/fluix_pattern_small.png) ![Flawed Budding Pattern](../assets/diagrams/flawed_budding_pattern_small.png)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1.7 0 1" max="2 1 2">
        (2) Interface: ใช้การตั้งค่าเริ่มต้น
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 .7 1" max="2 1 2">
        (3) Formation Plane: ตั้งให้ปล่อยของขาเข้าเป็นไอเทม
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 2 1" max="2 2.3 2">
        (4) Annihilation Plane: ไม่มีหน้าจอตั้งค่า
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 1 1" max="3 1.3 2">
        (5) Storage Bus: กรองเฉพาะผลผลิตของแพตเทิร์น
        <Row><ItemImage id="fluix_crystal" scale="2" /><BlockImage id="flawless_budding_quartz" scale="2" /></Row>
  </BoxAnnotation>

<DiamondAnnotation pos="3.9 0.5 1.5" color="#00ff00">
        ไปยังเครือข่ายหลักและ Charger อัตโนมัติ
        <GameScene zoom="3" background="transparent">
          <ImportStructure src="../assets/assemblies/charger_automation.snbt" />
          <IsometricCamera yaw="195" pitch="30" />
        </GameScene>
    </DiamondAnnotation>

  <IsometricCamera yaw="180" pitch="0" />
</GameScene>

## Configurations and Patterns

การตั้งค่าและแพตเทิร์น

* <ItemLink id="pattern_provider" /> (1) ใช้การตั้งค่าเริ่มต้น พร้อม <ItemLink id="processing_pattern" /> ที่เกี่ยวข้อง
  * สำหรับ <ItemLink id="fluix_crystal" /> ใช้สูตรเริ่มต้นจาก JEI/REI ได้เลย:

    ![Fluix Pattern](../assets/diagrams/fluix_pattern.png)

  * สำหรับ <ItemLink id="flawed_budding_quartz" /> น่าจะดีที่สุดหากสร้างโดยตรงจาก <ItemLink id="quartz_block" />
    เพื่อเลี่ยงปัญหาวัตถุดิบของสูตรหนึ่งเป็นผลผลิตของอีกสูตร ทำให้ Storage Bus กรองแยกไม่ได้:

    ![Flawed Budding Pattern](../assets/diagrams/flawed_budding_pattern.png)

* <ItemLink id="interface" /> (2) ใช้การตั้งค่าเริ่มต้น
* <ItemLink id="formation_plane" /> (3) ตั้งให้ปล่อยของขาเข้าเป็นไอเทม
* <ItemLink id="annihilation_plane" /> (4) ไม่มีหน้าจอและตั้งค่าไม่ได้
* <ItemLink id="storage_bus" /> (5) กรองเฉพาะผลผลิตของแพตเทิร์น

## How It Works

หลักการทำงาน

1.  <ItemLink id="pattern_provider" /> ส่งวัตถุดิบเข้า <ItemLink id="interface" /> ด้านข้าง บนเครือข่ายย่อยสีเขียว
2.  Interface (ซึ่งตั้งไม่ให้เก็บอะไรตามค่าเริ่มต้น) พยายามส่งของภายในเข้า [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
3.  ที่เก็บเดียวบนเครือข่ายย่อยสีเขียวคือ <ItemLink id="formation_plane" /> ซึ่งโยนไอเทมที่ได้รับลงน้ำ
4.  <ItemLink id="annihilation_plane" /> บนเครือข่ายย่อยสีส้มพยายามเก็บไอเทมที่เพิ่งโยนลงไป แต่ทำไม่ได้ เพราะ
    <ItemLink id="storage_bus" /> บน Pattern Provider (ที่เก็บเดียวของเครือข่ายย่อยสีส้ม) กรองให้รับเฉพาะผลผลิตของสูตรที่คราฟต์ได้
5.  ไอเทมเกิดปฏิกิริยาแปรสภาพในโลก
6.  ตอนนี้ Annihilation Plane เก็บไอเทมด้านหน้าได้ เพราะ Storage Bus อนุญาตให้เก็บไอเทมเหล่านั้น
7.  Storage Bus เก็บผลผลิตลง Pattern Provider ส่งกลับเข้าเครือข่าย
