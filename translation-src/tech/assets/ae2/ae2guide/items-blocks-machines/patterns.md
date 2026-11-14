---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: แพตเทิร์น
  icon: crafting_pattern
  position: 410
categories:
- tools
item_ids:
- ae2:blank_pattern
- ae2:crafting_pattern
- ae2:processing_pattern
- ae2:smithing_table_pattern
- ae2:stonecutting_pattern
---

# Patterns

แพตเทิร์น

<ItemImage id="crafting_pattern" scale="4" />

สร้าง Pattern จาก Blank Pattern ใน <ItemLink id="pattern_encoding_terminal" /> แล้วใส่ใน <ItemLink id="pattern_provider" />
หรือ <ItemLink id="molecular_assembler" />

มีแพตเทิร์นหลายชนิดสำหรับงานต่าง ๆ:

*   <ItemLink id="crafting_pattern" /> เข้ารหัสสูตรของ Crafting Table ใส่โดยตรงใน <ItemLink id="molecular_assembler" /> เพื่อให้
    คราฟต์เมื่อได้รับวัตถุดิบได้ แต่การใช้งานหลักคือใส่ใน <ItemLink id="pattern_provider" /> ข้าง Molecular Assembler
    Pattern Provider จะทำงานพิเศษในกรณีนี้ โดยส่งแพตเทิร์นที่เกี่ยวข้องพร้อมวัตถุดิบให้ Assembler ข้างเคียง
    เนื่องจาก Assembler ส่งผลผลิตเข้าช่องเก็บของข้างเคียงอัตโนมัติ แค่ติด Assembler ข้าง Pattern Provider ก็ทำให้แพตเทิร์นคราฟต์ทำงานอัตโนมัติได้

***

*   <ItemLink id="smithing_table_pattern" /> คล้าย Crafting Pattern มาก แต่เข้ารหัสสูตร Smithing Table ทำงานอัตโนมัติด้วย Pattern
    Provider และ Molecular Assembler แบบเดียวกันทุกประการ ที่จริงแล้วแพตเทิร์นคราฟต์ ตีเหล็ก และตัดหิน
    ใช้ร่วมกันในระบบเดียวได้

***

*   <ItemLink id="stonecutting_pattern" /> คล้าย Crafting Pattern มาก แต่เข้ารหัสสูตร Stonecutter ทำงานอัตโนมัติด้วย Pattern
    Provider และ Molecular Assembler แบบเดียวกันทุกประการ ที่จริงแล้วแพตเทิร์นคราฟต์ ตีเหล็ก และตัดหิน
    ใช้ร่วมกันในระบบเดียวได้

***

*   <ItemLink id="processing_pattern" /> เป็นที่มาของความยืดหยุ่นส่วนใหญ่ในการคราฟต์อัตโนมัติ เป็นชนิดที่ทั่วไปที่สุด โดยเพียง
    บอกว่า "ถ้า Pattern Provider ส่งวัตถุดิบเหล่านี้เข้าช่องเก็บของข้างเคียง ระบบ ME จะได้รับไอเทมเหล่านี้ในอนาคต
    อันใกล้หรือไกล" ใช้กับเครื่องจักรจากม็อดแทบทุกชนิด รวมถึง Furnace และสิ่งคล้ายกันได้ เพราะมันใช้งานได้
    กว้างและไม่สนใจว่าเกิดอะไรระหว่างส่งวัตถุดิบกับรับผลผลิต คุณจึงทำอะไรพิสดารได้ เช่น ป้อนวัตถุดิบเข้า
    สายการผลิตโรงงานซับซ้อนทั้งสาย ที่จัดเรียงสิ่งของ รับวัตถุดิบอื่นจากฟาร์มที่ผลิตได้ไม่จำกัด
    หรือพิมพ์บท Bee Movie ทั้งเรื่อง ระบบ ME ก็ไม่สนใจ ตราบใดที่ได้ผลผลิตตามแพตเทิร์น ที่จริงแล้ว
    มันไม่สนใจด้วยซ้ำว่าวัตถุดิบเกี่ยวข้องกับผลผลิตหรือไม่ คุณบอกว่า "Cherry Planks 1 = Nether Star 1"
    แล้วให้ฟาร์ม Wither ฆ่า Wither เมื่อได้รับ Cherry Planks หนึ่งชิ้น ก็ทำงานได้

รองรับ <ItemLink id="pattern_provider" /> หลายเครื่องที่มีแพตเทิร์นเหมือนกัน และทำงานขนานกันได้ อีกทั้งกำหนดแพตเทิร์น
เช่น Cobblestone 8 = Stone 8 แทน Cobblestone 1 = Stone 1 เพื่อให้ Pattern Provider ใส่ Cobblestone 8 ชิ้น
เข้าระบบหลอมต่อครั้ง แทนที่จะใส่ทีละชิ้นได้

## Recipe

สูตรคราฟต์

<RecipeFor id="blank_pattern" />
