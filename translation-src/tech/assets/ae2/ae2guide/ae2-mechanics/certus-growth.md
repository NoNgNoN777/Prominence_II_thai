---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: การเติบโตของ Certus
  icon: quartz_cluster
---

# Certus Growth

การเติบโตของ Certus

## Basically just copy-pasted from the getting started page

เนื้อหาหลักยกมาจากหน้าเริ่มต้นใช้งาน

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/budding_certus_1.snbt" />
</GameScene>

หน่อ Certus Quartz จะงอกจาก [Budding Certus Quartz](../items-blocks-machines/budding_certus.md) คล้าย Amethyst หากทุบหน่อที่ยังโต
ไม่เต็มที่จะได้ <ItemLink id="certus_quartz_dust" /> หนึ่งชิ้น โดย Fortune ไม่มีผล หากทุบผลึกที่โตเต็มที่จะได้
<ItemLink id="certus_quartz_crystal" /> สี่ชิ้น และ Fortune เพิ่มจำนวนนี้ได้

Budding Certus Quartz มี 4 ระดับ ได้แก่ Flawless, Flawed, Chipped และ Damaged

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ทุกครั้งที่หน่อโตขึ้นหนึ่งขั้น บล็อกต้นกำเนิดมีโอกาสเสื่อมลงหนึ่งระดับ จนท้ายที่สุดกลายเป็น
Certus Quartz Block ธรรมดา ซ่อมบล็อกหรือสร้างบล็อกต้นกำเนิดใหม่ได้โดยโยน Budding Certus Quartz หรือ
Certus Quartz Block ลงน้ำพร้อม <ItemLink id="charged_certus_quartz_crystal" /> หนึ่งชิ้นขึ้นไป

<RecipeFor id="damaged_budding_quartz" />

Flawless Budding Certus Quartz จะไม่เสื่อมและผลิต Certus ได้ไม่จำกัด แต่คราฟต์หรือย้าย
ด้วย Pickaxe ไม่ได้ แม้จะมี Silk Touch (อย่างไรก็ตาม *ย้ายได้* ด้วย[ระบบจัดเก็บเชิงมิติ](../ae2-mechanics/spatial-io.md))

หน่อ Certus Quartz โตช้ามากตามธรรมชาติ แต่ <ItemLink id="growth_accelerator" /> จะเร่ง
การเติบโตได้อย่างมากเมื่อวางติดบล็อกต้นกำเนิด ควรสร้างไว้หลายเครื่องเป็นลำดับแรก

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_certus_2.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

หากมี Quartz ไม่พอทำ <ItemLink id="energy_acceptor" /> หรือ <ItemLink id="vibration_chamber" /> เพิ่ม
ให้สร้าง <ItemLink id="crank" /> แล้วติดที่ปลายเครื่องเร่งการเติบโตแทน

ดูวิธีเก็บ Certus อัตโนมัติได้[ที่นี่](../example-setups/simple-certus-farm.md)