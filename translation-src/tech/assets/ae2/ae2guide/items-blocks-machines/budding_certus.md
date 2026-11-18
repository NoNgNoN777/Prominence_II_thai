---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Budding Certus Quartz
  icon: flawless_budding_quartz
  position: 010
categories:
- misc ingredients blocks
item_ids:
- ae2:flawless_budding_quartz
- ae2:flawed_budding_quartz
- ae2:chipped_budding_quartz
- ae2:damaged_budding_quartz
- ae2:small_quartz_bud
- ae2:medium_quartz_bud
- ae2:large_quartz_bud
- ae2:quartz_cluster
---

# Budding Certus Quartz

(ดู [การเติบโตของ Certus](../ae2-mechanics/certus-growth.md) ด้วย)

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ตา Certus Quartz แตกหน่อจาก Budding Certus Block คล้าย Amethyst พบได้ใน [อุกกาบาต](../ae2-mechanics/meteorites.md)
มี 4 ระดับ: Flawless, Flawed, Chipped และ Damaged แยกชนิดได้ง่ายที่สุด
ด้วยม็อดอย่าง HWYLA, Jade, The One Probe เป็นต้น (หรือหน้าจอ F3)

สำหรับ Flawed, Chipped และ Damaged Budding Certus ทุกครั้งที่ตาคริสตัลโตขึ้นหนึ่งขั้น บล็อกต้นกำเนิดมีโอกาส
เสื่อมลงหนึ่งระดับ จนกลายเป็น <ItemLink id="quartz_block" /> ปกติในที่สุด

Flawless Budding Certus ไม่เสื่อมสภาพจากการเติบโตของตาคริสตัล จึงเป็นแหล่งทรัพยากรไม่สิ้นสุด

เมื่อทุบด้วย Pickaxe ปกติ Budding Certus Block จะลดลง 1 ระดับ หากทุบด้วย Pickaxe
ที่มี Silk Touch จะไม่เสื่อมสภาพ ยกเว้น Flawless จึงเก็บและย้าย Flawless Budding Certus Block
ด้วย Pickaxe ไม่ได้ แต่ใช้ [Spatial Storage](../ae2-mechanics/spatial-io.md)
ตัดและวางบล็อก Flawless ย้ายที่ได้

## Recipes

สูตรคราฟต์

คราฟต์ Flawed, Chipped และ Damaged Budding Certus ได้โดยโยนบล็อกต้นกำเนิดระดับก่อนหน้า (หรือ <ItemLink id="quartz_block" />)
ลงน้ำพร้อม <ItemLink id="charged_certus_quartz_crystal" /> อย่างน้อยหนึ่งชิ้น

Flawless Budding Certus คราฟต์ไม่ได้ ต้องหาในโลกเท่านั้น

<Row>
  <RecipeFor id="damaged_budding_quartz" />

  <RecipeFor id="chipped_budding_quartz" />

  <RecipeFor id="flawed_budding_quartz" />
</Row>
