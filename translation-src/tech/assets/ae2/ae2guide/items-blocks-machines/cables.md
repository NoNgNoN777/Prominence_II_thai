---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: สาย
  icon: fluix_glass_cable
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:white_glass_cable
- ae2:orange_glass_cable
- ae2:magenta_glass_cable
- ae2:light_blue_glass_cable
- ae2:yellow_glass_cable
- ae2:lime_glass_cable
- ae2:pink_glass_cable
- ae2:gray_glass_cable
- ae2:light_gray_glass_cable
- ae2:cyan_glass_cable
- ae2:purple_glass_cable
- ae2:blue_glass_cable
- ae2:brown_glass_cable
- ae2:green_glass_cable
- ae2:red_glass_cable
- ae2:black_glass_cable
- ae2:fluix_glass_cable
- ae2:white_covered_cable
- ae2:orange_covered_cable
- ae2:magenta_covered_cable
- ae2:light_blue_covered_cable
- ae2:yellow_covered_cable
- ae2:lime_covered_cable
- ae2:pink_covered_cable
- ae2:gray_covered_cable
- ae2:light_gray_covered_cable
- ae2:cyan_covered_cable
- ae2:purple_covered_cable
- ae2:blue_covered_cable
- ae2:brown_covered_cable
- ae2:green_covered_cable
- ae2:red_covered_cable
- ae2:black_covered_cable
- ae2:fluix_covered_cable
- ae2:white_covered_dense_cable
- ae2:orange_covered_dense_cable
- ae2:magenta_covered_dense_cable
- ae2:light_blue_covered_dense_cable
- ae2:yellow_covered_dense_cable
- ae2:lime_covered_dense_cable
- ae2:pink_covered_dense_cable
- ae2:gray_covered_dense_cable
- ae2:light_gray_covered_dense_cable
- ae2:cyan_covered_dense_cable
- ae2:purple_covered_dense_cable
- ae2:blue_covered_dense_cable
- ae2:brown_covered_dense_cable
- ae2:green_covered_dense_cable
- ae2:red_covered_dense_cable
- ae2:black_covered_dense_cable
- ae2:fluix_covered_dense_cable
- ae2:white_smart_cable
- ae2:orange_smart_cable
- ae2:magenta_smart_cable
- ae2:light_blue_smart_cable
- ae2:yellow_smart_cable
- ae2:lime_smart_cable
- ae2:pink_smart_cable
- ae2:gray_smart_cable
- ae2:light_gray_smart_cable
- ae2:cyan_smart_cable
- ae2:purple_smart_cable
- ae2:blue_smart_cable
- ae2:brown_smart_cable
- ae2:green_smart_cable
- ae2:red_smart_cable
- ae2:black_smart_cable
- ae2:fluix_smart_cable
- ae2:white_smart_dense_cable
- ae2:orange_smart_dense_cable
- ae2:magenta_smart_dense_cable
- ae2:light_blue_smart_dense_cable
- ae2:yellow_smart_dense_cable
- ae2:lime_smart_dense_cable
- ae2:pink_smart_dense_cable
- ae2:gray_smart_dense_cable
- ae2:light_gray_smart_dense_cable
- ae2:cyan_smart_dense_cable
- ae2:purple_smart_dense_cable
- ae2:blue_smart_dense_cable
- ae2:brown_smart_dense_cable
- ae2:green_smart_dense_cable
- ae2:red_smart_dense_cable
- ae2:black_smart_dense_cable
- ae2:fluix_smart_dense_cable
---

# Cables

สาย

<GameScene zoom="3" background="transparent">
  <ImportStructure src="../assets/assemblies/cables.snbt" />
  <IsometricCamera yaw="180" pitch="30" />
</GameScene>

แม้เครื่องจักรที่รองรับ ME ซึ่งวางติดกันจะสร้างเครือข่าย ME ได้ แต่สายคือวิธีหลัก
ในการขยายเครือข่าย ME ไปยังพื้นที่กว้าง

ใช้สายคนละสีเพื่อไม่ให้สายที่อยู่ติดกันเชื่อมกันได้
ช่วยกระจาย [ช่องสัญญาณ](../ae2-mechanics/channels.md) ได้มีประสิทธิภาพขึ้น อีกทั้งกำหนดสีเทอร์มินัลที่ต่ออยู่
จึงไม่ต้องมีแต่เทอร์มินัลสีม่วง สาย Fluix เชื่อมกับสายทุกสี

โปรดทราบว่า **ช่องสัญญาณไม่เกี่ยวข้องกับสีของสาย**

## An Important Note

ข้อควรทราบที่สำคัญ

**หากเพิ่งเริ่ม AE2 และยังไม่คุ้นกับช่องสัญญาณ ให้ใช้ Smart Cable และ Dense Smart Cable ทุกจุดที่ทำได้
มันแสดงเส้นทางช่องสัญญาณผ่านเครือข่าย ทำให้เข้าใจพฤติกรรมได้ง่ายขึ้น**

## Another Note

ข้อควรทราบเพิ่มเติม

**สายเหล่านี้ไม่ใช่ท่อไอเทม ของเหลว พลังงาน หรือสิ่งอื่น** ไม่มีช่องเก็บของภายใน Pattern Provider และเครื่องจักรไม่ได้ "ส่ง"
ของเข้าไป หน้าที่ของมันมีเพียงเชื่อม [อุปกรณ์](../ae2-mechanics/devices.md) AE2 เข้าด้วยกันเป็นเครือข่าย

## Glass Cable

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/fluix_glass_cable.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="fluix_glass_cable" /> เป็นสายที่สร้างง่ายที่สุด ส่งพลังงาน
และ [ช่องสัญญาณ](../ae2-mechanics/channels.md) ได้สูงสุด 8 ช่อง มี 17 สี โดยค่าเริ่มต้น
คือ Fluix และย้อมได้ด้วยสีย้อมทั้ง 16 สี

คราฟต์สายสีโดยวางสายชนิดเดียวกัน 8 ชิ้นล้อมสีย้อมชนิดใดก็ได้
(สีสายไม่สำคัญ แต่ต้องเป็นชนิดเดียวกัน
เช่น Glass หรือ Smart) ทาสีสายที่ติดตั้งในโลกได้ด้วยแปรงทาสีที่เข้ากันกับ Forge

คราฟต์สายสีใดก็ได้ร่วมกับ Water Bucket เพื่อล้างสี

หุ้มสายด้วย Wool เพื่อสร้าง <ItemLink id="fluix_covered_cable" /> และคราฟต์ <ItemLink id="fluix_smart_cable" /> เพื่อให้เห็นการใช้งาน
[ช่องสัญญาณ](../ae2-mechanics/channels.md) ชัดเจนขึ้น

<RecipeFor id="fluix_glass_cable" />

<RecipeFor id="blue_glass_cable" />

## Covered Cable

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

รุ่น Covered ไม่มีข้อได้เปรียบด้านการเล่นเหนือ <ItemLink id="fluix_glass_cable" />
แต่เป็นตัวเลือกด้านความสวยงามหากชอบแบบหุ้ม

เปลี่ยนสีได้แบบเดียวกับ <ItemLink id="fluix_glass_cable" /> คราฟต์ <ItemLink id="fluix_covered_cable" /> 4 ชิ้นร่วมกับ
Redstone และ Glowstone เพื่อสร้าง <ItemLink id="fluix_covered_dense_cable" />

<Recipe id="network/cables/covered_fluix" />

<RecipeFor id="blue_covered_cable" />

## Dense Cable

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_covered_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

สายความจุสูง ส่งได้ 32 ช่องสัญญาณ ต่างจากสายมาตรฐานที่ส่งได้ 8 ช่อง
แต่ไม่รองรับบัส จึงต้องแยกจาก Dense เป็นสาย
เล็กกว่า (เช่น <ItemLink id="fluix_glass_cable" /> หรือ <ItemLink id="fluix_smart_cable" />) ก่อนติดบัส
หรือแผงต่าง ๆ

Dense Cable เปลี่ยนพฤติกรรม "เส้นทางสั้นที่สุด" ของช่องสัญญาณเล็กน้อย ช่องสัญญาณจะเลือกเส้นทางสั้นที่สุดไปยัง
Dense Cable แล้วเลือกเส้นทางสั้นที่สุดผ่านสาย Dense นั้นไปยัง Controller

<Recipe id="network/cables/dense_covered_fluix" />

<RecipeFor id="blue_covered_dense_cable" />

## Smart Cable

<Row>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/fluix_smart_dense_cable.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>
</Row>

แม้รูปร่างคล้าย <ItemLink id="fluix_covered_cable" /> อยู่บ้าง
แต่มีความสามารถวินิจฉัยโดยแสดงการใช้ช่องสัญญาณบนสาย
ช่องสัญญาณปรากฏเป็นเส้นสีเรืองแสงตามแถบดำ
ช่วยให้เข้าใจว่าช่องสัญญาณในเครือข่ายถูกใช้อย่างไร
สำหรับ Smart Cable ปกติ สี่ช่องแรกเป็นเส้นสีเดียวกับสาย
สี่ช่องถัดไปเป็นเส้นสีขาว ส่วน Dense Smart Cable แต่ละเส้นแทน 4 ช่องสัญญาณ

ในเครือข่ายที่มี <ItemLink id="controller" /> เส้นบนสายแสดงเส้นทางจริงที่ช่องสัญญาณใช้

Smart Cable ในเครือข่ายเฉพาะกิจจะแสดงจำนวนช่องสัญญาณที่ใช้ทั้งเครือข่าย แทนจำนวนที่ผ่านสายเส้นนั้น

เปลี่ยนสีได้แบบเดียวกับ <ItemLink id="fluix_glass_cable" />

<Recipe id="network/cables/smart_fluix" />

<Recipe id="network/cables/dense_smart_fluix" />

<RecipeFor id="blue_smart_cable" />
