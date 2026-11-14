---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: ME Threshold Level Emitter
    icon: extendedae:threshold_level_emitter
categories:
- extended devices
item_ids:
- extendedae:threshold_level_emitter
---

# ME Threshold Level Emitter

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_threshold_level_emitter.snbt"></ImportStructure>
</GameScene>

ทำงานคล้ายวงจร Reset-Set Latch โดยปิดสัญญาณเรดสโตนเมื่อจำนวนไอเทมในเครือข่ายต่ำกว่า
เกณฑ์ล่าง และเปิดสัญญาณเมื่อจำนวนสูงกว่าเกณฑ์บน

ตัวอย่างเช่น ตั้งเกณฑ์ล่างไว้ที่ 100 และเกณฑ์บนไว้ที่ 150

ช่วงแรกเครือข่ายยังว่าง จึงยังไม่ส่งสัญญาณ

เมื่อจำนวนไอเทมเพิ่มขึ้นจนมากกว่า 150 เครื่องจะเริ่มส่งสัญญาณเรดสโตน

เมื่อจำนวนลดลงต่ำกว่า 150 เครื่องจะยังคงส่งสัญญาณ

สัญญาณจะปิดเมื่อจำนวนลดลงต่ำกว่า 100 เท่านั้น
