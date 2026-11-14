---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Growth Accelerator
  icon: growth_accelerator
  position: 310
categories:
- machines
item_ids:
- ae2:growth_accelerator
---

# The Growth Accelerator

<BlockImage id="growth_accelerator" p:powered="true" scale="8"/>

Growth Accelerator เร่ง [การเติบโต](../ae2-mechanics/certus-growth.md) ของ Certus หรือ Amethyst อย่างมาก เมื่อติดตั้งข้างบล็อกต้นกำเนิดผลึก

น่าสนใจที่มันเร่งการเติบโตของพืชหลายชนิดได้ *ด้วย*

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/growth_accelerator.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

หากต้องการจ่ายพลังงานด้วยมือ ให้วาง <ItemLink id="crank" /> ด้านบนหรือด้านล่าง แล้วคลิกขวา

เชื่อมต่อกับสายได้เฉพาะปลายทั้งสองด้านที่มีส่วน Fluix สีชมพู

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/accelerator_connections.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Recipe

สูตรคราฟต์

<RecipeFor id="growth_accelerator" />
