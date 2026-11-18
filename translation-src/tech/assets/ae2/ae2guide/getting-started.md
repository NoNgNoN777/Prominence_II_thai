---
navigation:
  title: เริ่มต้นใช้งาน (1.20+)
  position: 10
---

<div class="notification is-info">
  ข้อมูลต่อไปนี้ใช้กับ Applied Energistics 2 ใน Minecraft 1.20 ขึ้นไปเท่านั้น
</div>

# Getting Started

เริ่มต้นใช้งาน

## Getting The Initial Materials)

หาวัตถุดิบเริ่มต้น

<GameScene zoom="4" background="transparent">
  <ImportStructure src="assets/assemblies/meteor_interior.snbt" />
</GameScene>

เริ่มใช้ Applied Energistics 2 ด้วยการหา[อุกกาบาต](ae2-mechanics/meteorites.md) ซึ่งพบค่อนข้างบ่อยและมักทิ้งหลุมขนาดใหญ่ไว้ คุณอาจเคยเจอระหว่างเดินทางแล้ว
หากยังไม่พบ ให้คราฟต์ <ItemLink id="meteorite_compass" /> ซึ่งจะชี้ไปยัง <ItemLink id="mysterious_cube" /> ที่ใกล้ที่สุด

เมื่อพบอุกกาบาต ให้ขุดเข้าไปตรงกลาง จะพบกลุ่มผลึก Certus Quartz, หน่อ Certus Quartz, [Budding Certus Quartz](items-blocks-machines/budding_certus.md) หลายระดับ และ Mysterious Cube อยู่ตรงกลาง

ขุดกลุ่มผลึกและบล็อก Certus Quartz ที่พบ จะเก็บ Budding Certus Quartz ไปด้วยก็ได้ แต่หากไม่มี Silk Touch บล็อกจะเสื่อมลง 1 ระดับ

อย่าทุบ Flawless Budding Certus Quartz เพราะแม้ใช้ Silk Touch ก็จะลดเป็น Flawed Budding Certus Quartz และซ่อมกลับเป็น Flawless ไม่ได้

ขุด Mysterious Cube ตรงกลางอุกกาบาตด้วย เพื่อรับ Inscriber Press ครบทั้ง 4 แบบ

## Growing Certus Quartz

เพาะ Certus Quartz

<GameScene zoom="4" background="transparent">
<ImportStructure src="assets/assemblies/budding_certus_1.snbt" />
</GameScene>

หน่อ Certus Quartz จะงอกจาก [Budding Certus Quartz](items-blocks-machines/budding_certus.md) คล้าย Amethyst หากทุบหน่อที่ยังโต
ไม่เต็มที่จะได้ <ItemLink id="certus_quartz_dust" /> หนึ่งชิ้น โดย Fortune ไม่มีผล หากทุบผลึกที่โตเต็มที่จะได้
<ItemLink id="certus_quartz_crystal" /> สี่ชิ้น และ Fortune เพิ่มจำนวนนี้ได้

Budding Certus Quartz มี 4 ระดับ ได้แก่ Flawless, Flawed, Chipped และ Damaged

<GameScene zoom="4" background="transparent">
<ImportStructure src="assets/assemblies/budding_blocks.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

ทุกครั้งที่หน่อโตขึ้นหนึ่งขั้น บล็อกต้นกำเนิดมีโอกาสเสื่อมลงหนึ่งระดับ จนท้ายที่สุดกลายเป็น
Certus Quartz Block ธรรมดา ซ่อมบล็อกหรือสร้างบล็อกต้นกำเนิดใหม่ได้โดยโยน Budding Certus Quartz หรือ
Certus Quartz Block ลงน้ำพร้อม <ItemLink id="charged_certus_quartz_crystal" /> หนึ่งชิ้นขึ้นไป

<RecipeFor id="damaged_budding_quartz" />

Flawless Budding Certus Quartz จะไม่เสื่อมและผลิต Certus ได้ไม่จำกัด แต่คราฟต์หรือย้าย
ด้วย Pickaxe ไม่ได้ แม้จะมี Silk Touch (อย่างไรก็ตาม ย้ายได้ ด้วย[ระบบจัดเก็บเชิงมิติ](ae2-mechanics/spatial-io.md))

หน่อ Certus Quartz โตช้ามากตามธรรมชาติ แต่ <ItemLink id="growth_accelerator" /> จะเร่ง
การเติบโตได้อย่างมากเมื่อวางติดบล็อกต้นกำเนิด ควรสร้างไว้หลายเครื่องเป็นลำดับแรก

<GameScene zoom="4" background="transparent">
<ImportStructure src="assets/assemblies/budding_certus_2.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

หากมี Quartz ไม่พอทำ <ItemLink id="energy_acceptor" /> หรือ <ItemLink id="vibration_chamber" /> เพิ่ม
ให้สร้าง <ItemLink id="crank" /> แล้วติดที่ปลายเครื่องเร่งการเติบโตแทน

ดูวิธีเก็บ Certus อัตโนมัติได้[ที่นี่](example-setups/simple-certus-farm.md)

## A Quick Aside on Fluix

เรื่องน่ารู้เกี่ยวกับ Fluix

วัตถุดิบอีกอย่างที่ต้องใช้คือ Fluix ซึ่งคุณเคยใช้สร้าง Growth Accelerator ไปแล้ว ทำได้โดยโยน Charged Certus Quartz, Redstone และ Nether Quartz ลงน้ำ ส่วนวิธีทำอัตโนมัติขอ "ฝากเป็นแบบฝึกหัดให้ผู้อ่าน"

ต้องใช้ <ItemLink id="charger" /> ผลิต <ItemLink id="charged_certus_quartz_crystal" /> หากยังไม่มี ให้สร้างไว้ด้วย

## Inscribing Some Processors

จารึก Processor

เมื่อขุด Mysterious Cube ในอุกกาบาต คุณจะได้แม่พิมพ์ "Press" สี่แบบ ใช้ใน <ItemLink id="inscriber" /> เพื่อผลิต Processor สามชนิด

<ItemGrid>
  <ItemIcon id="silicon_press" />

  <ItemIcon id="logic_processor_press" />

  <ItemIcon id="calculation_processor_press" />

  <ItemIcon id="engineering_processor_press" />
</ItemGrid>

Inscriber เป็นเครื่องจักรที่แต่ละด้านทำงานต่างกัน คล้าย Furnace ปกติ ใส่ของจากด้านบนหรือล่างเพื่อเข้าช่องบนหรือล่าง ใส่จากด้านข้างหรือด้านหลังเพื่อเข้าช่องกลาง และดึงผลผลิตออกทางด้านข้างหรือด้านหลังได้

ใช้ <ItemLink id="certus_quartz_wrench" /> หมุน Inscriber ได้ เพื่อให้ทำอัตโนมัติด้วย Hopper สะดวกขึ้นและอาจช่วยลดท่อพันกัน

ผลิต Processor แต่ละชนิดไว้เล็กน้อยสำหรับขั้นต่อไป คือสร้างระบบ ME พื้นฐาน ส่วนการผลิต Processor อัตโนมัติขอ "ฝากเป็นแบบฝึกหัดให้ผู้อ่าน"

## Matter Energy Tech: ME Networks and Storage

เทคโนโลยี Matter Energy: เครือข่ายและคลัง ME

### What is ME Storage?

คลัง ME คืออะไร?

อ่านว่า เอ็ม-อี ย่อมาจาก Matter Energy

Matter Energy เป็นส่วนหลักของ Applied Energistics 2 คล้ายหีบมัลติบล็อกฉบับนักวิทยาศาสตร์สติเฟื่อง
ที่จะเปลี่ยนวิธีเก็บของของคุณไปเลย ME ต่างจากระบบเก็บของอื่นใน Minecraft มาก
จึงอาจต้องคิดนอกกรอบเล็กน้อย แต่เมื่อเริ่มใช้ได้ ความจุมหาศาลในพื้นที่เล็ก
และจุดเข้าถึงคลังหลายแห่งเป็นเพียงจุดเริ่มต้นของสิ่งที่ทำได้

### What do I need to know to get started?

ต้องรู้อะไรก่อนเริ่ม?

ME เก็บไอเทมไว้ภายในไอเทมอีกชนิดที่เรียกว่า [Storage Cell](items-blocks-machines/storage_cells.md) มี 5 ระดับที่ความจุ
เพิ่มขึ้นเรื่อย ๆ การใช้ Storage Cell ต้องใส่ไว้ใน <ItemLink id="chest" />
หรือ <ItemLink id="drive" />

<ItemLink id="chest" /> แสดงของในเซลล์ทันทีที่ใส่เข้าไป คุณ
ฝากหรือถอนของได้เหมือน <ItemLink id="minecraft:chest" /> แต่ไอเทมจะ
เก็บอยู่ใน Storage Cell ไม่ได้อยู่ในตัว <ItemLink id="chest" />

<ItemLink id="chest" /> เหมาะสำหรับเริ่มทำความเข้าใจ ME แต่หากต้องการ
ใช้ประโยชน์เต็มที่ ต้องสร้าง[เครือข่าย ME](ae2-mechanics/me-network-connections.md)

## Your Very First ME System

ระบบ ME ชุดแรกของคุณ

เมื่อมีวัตถุดิบและเครื่องจักรพื้นฐานของ Applied Energistics 2 ครบแล้ว ก็สร้างระบบ ME หรือ Matter Energy ชุดแรกได้ เป็นระบบง่าย ๆ ไม่มีคราฟต์อัตโนมัติหรือระบบขนส่ง มีเพียงคลังที่ใช้ง่ายและค้นหาได้

<GameScene zoom="6" interactive={true}>
<ImportStructure src="assets/assemblies/tiny_me_system.snbt" />

</GameScene>

*   สิ่งที่ต้องใช้:
    * 1x <ItemLink id="drive" />
    * 1x <ItemLink id="terminal" /> หรือ <ItemLink id="crafting_terminal" />
    * 1x <ItemLink id="energy_acceptor" />
    * [สายเคเบิล](items-blocks-machines/cables.md) เล็กน้อย ใช้ Glass, Covered หรือ Smart แต่ไม่ใช้ Dense
    * [Storage Cell](items-blocks-machines/storage_cells.md) เล็กน้อย แนะนำขนาด 4k ซึ่งสมดุลดีระหว่าง
    ความจุกับจำนวนชนิด (การ[แบ่งรายการเก็บ](items-blocks-machines/cell_workbench.md)ด้วยเซลล์ 4k ร่วมกับ 1k จะมีประสิทธิภาพกว่า แต่
    ขอข้ามรายละเอียดที่ซับซ้อนนั้นไปก่อน)
---
1. วาง Drive
2. Energy Acceptor และ[อุปกรณ์](ae2-mechanics/devices.md) AE2 อีกหลายชนิดมี 2 รูปแบบ คือเต็มบล็อกและแบบแบน สลับได้ในช่องคราฟต์ ถ้าเป็นเต็มบล็อกให้วางข้าง Drive หากเป็นแผ่นแบน ให้วางสายเคเบิลบน Drive แล้วติด Acceptor กับสายนั้น
3. ต่อพลังงานเข้า Energy Acceptor ด้วยสาย ท่อ หรือ Conduit จากม็อดผลิตพลังงานที่คุณใช้
4. วางสายเคเบิลบน Drive หรือที่ระดับสายตา แล้วติด Terminal หรือ Crafting Terminal บนสาย
5. ใส่ Storage Cell ใน Drive
6. ได้คลังพร้อมใช้แล้ว!
7. ลองปรับการตั้งค่าของ Terminal
8. ดื่มด่ำกับความสามารถอันยิ่งใหญ่ของคุณ
9. แล้วตระหนักว่าเมื่อมองภาพใหญ่ เครือข่ายนี้ยังเล็กมาก

### Expanding your Network

ขยายเครือข่าย

ตอนนี้คุณมีคลังพื้นฐานและจุดเข้าถึงแล้ว ถือเป็นจุดเริ่มต้นที่ดี แต่คงอยากเริ่ม
ทำขั้นตอนแปรรูปบางอย่างอัตโนมัติ

ตัวอย่างง่าย ๆ คือวาง <ItemLink id="export_bus" /> บน Furnace เพื่อ
ส่งแร่เข้าไป แล้วติด <ItemLink id="import_bus" />
ด้านล่างเพื่อดึงแร่ที่หลอมแล้วออก

<ItemLink id="export_bus" /> ส่งไอเทมจากเครือข่ายไปยัง
ช่องเก็บของที่ติดอยู่ ส่วน <ItemLink id="import_bus" /> นำของจากช่องเก็บของนั้นเข้า
เครือข่าย

### Overcoming Limits

ก้าวข้ามข้อจำกัด

ตอนนี้คุณอาจมี[อุปกรณ์](ae2-mechanics/devices.md)ใกล้ครบ 8 ชิ้น เมื่อถึง 9 ชิ้นต้องเริ่ม
จัดการ[ช่องสัญญาณ](ae2-mechanics/channels.md) อุปกรณ์หลายชนิดแต่ไม่ใช่ทุกชนิดต้องใช้ช่องสัญญาณ
ในการทำงาน

โดยปกติเครือข่ายรองรับ 8 ช่องสัญญาณ หากเกินขีดจำกัด ต้องเพิ่ม
<ItemLink id="controller" /> เพื่อขยายเครือข่ายได้มากขึ้น
[Smart Cable](items-blocks-machines/cables.md) แสดงเส้นทางช่องสัญญาณในเครือข่าย ควรใช้บ่อย ๆ ตอนเริ่มต้นเพื่อเรียนรู้การทำงาน หรือเมื่อมี Redstone และ Glowstone มากพอ
