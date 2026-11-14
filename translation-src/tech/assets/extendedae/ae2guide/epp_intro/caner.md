---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: ME Caner
    icon: extendedae:caner
categories:
- extended devices
item_ids:
- extendedae:caner
---

# ME Caner

<BlockImage id="extendedae:caner" scale="8"></BlockImage>

ME Caner เป็นเครื่องบรรจุสิ่งต่าง ๆ ลงภาชนะ ทั้งของเหลว ก๊าซจาก Mekanism มานาจาก Botania และแม้แต่พลังงาน!

ช่องแรกใช้ใส่สิ่งที่จะบรรจุ ส่วนช่องที่สองใช้ใส่ภาชนะที่จะรับสิ่งนั้น

ต้องใช้พลังงานในการทำงาน โดยแต่ละครั้งใช้ 80 AE

![GUI](../pic/caner_gui.png)

โดยปกติจะบรรจุได้เฉพาะของเหลว หากต้องการบรรจุสิ่งอื่น ต้องติดตั้งส่วนเสริมที่รองรับ

### Support addons:

ส่วนเสริมที่รองรับ:
- Applied Flux
- Applied Mekanistics
- Applied Botanics Addon

## Autocrafting with ME Caner

คราฟต์อัตโนมัติด้วย ME Caner

รับพลังงานและเชื่อมต่อเครือข่ายได้เฉพาะด้านบนและด้านล่าง

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../structure/caner_example.snbt"></ImportStructure>
</GameScene>

ตัวอย่างการติดตั้ง ME Caner แบบง่าย เมื่อรับวัตถุดิบจาก <ItemLink id="ae2:pattern_provider" /> แล้ว เครื่องจะส่งไอเทมที่บรรจุเสร็จออกโดยอัตโนมัติ

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../structure/caner_auto.snbt"></ImportStructure>
</GameScene>

แพตเทิร์นต้องมีเฉพาะสิ่งที่จะบรรจุและภาชนะที่ใช้รับเท่านั้น ตัวอย่างเช่น:

เติมน้ำใส่ Bucket:

![P1](../pic/fill_water.png)

ชาร์จ Energy Tablet (ต้องติดตั้ง Applied Flux):

![P1](../pic/fill_energy.png)


## Uncaning

ถ่ายสิ่งที่บรรจุออก

ME Caner ถ่ายสิ่งที่บรรจุออกจากภาชนะได้ในโหมดถ่ายออก โดยต้องสลับวัตถุดิบกับผลผลิตในแพตเทิร์น
