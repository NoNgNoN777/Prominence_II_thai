---
navigation:
  parent: example-setups/example-setups-index.md
  title: ฟาร์ม Amethyst
  icon: minecraft:amethyst_shard
---

# Farming of Amethyst

การฟาร์ม Amethyst

แม้ <ItemLink id="growth_accelerator" /> จะใช้กับ Amethyst ได้ แต่วิธีกรอง [หน่อ Certus](../items-blocks-machines/budding_certus.md) ตามปกติ
ด้วย <ItemLink id="annihilation_plane" /> ใช้กับหน่อ Amethyst ไม่ได้ เพราะต่างจากหน่อ Certus ที่ยังไม่โตซึ่งดรอป
<ItemLink id="certus_quartz_dust" /> หน่อ Amethyst ที่ยังไม่โตไม่ดรอปอะไรเลย Annihilation Plane จึงทุบมันเสมอ
เพราะเครือข่ายเก็บ "ความว่างเปล่า" ได้เสมอ

แก้ได้โดยเสริม Silk Touch ให้ Annihilation Plane แล้วหน่อ Amethyst ที่ยังไม่โต *จะ* ดรอปของ
(บล็อกหน่อในระยะเติบโตต่าง ๆ) จึงกรองแยกได้

จากนั้นต้องนำ <ItemLink id="minecraft:amethyst_cluster" /> ไปวางอีกครั้งด้วย <ItemLink id="formation_plane" /> แล้ว
ทุบซ้ำด้วย <ItemLink id="annihilation_plane" /> ที่ไม่มี Silk Touch เพื่อรับ <ItemLink id="minecraft:amethyst_shard" />

โปรดทราบว่ากลุ่มผลึกมีทิศทาง จึงต้องมีหน้าบล็อกทึบอยู่ตรงข้าม Formation Plane โดยตรง

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/amethyst_farm.snbt" />

  <BoxAnnotation color="#dddddd" min="2.7 1 1" max="3 2 2">
        (1) Annihilation Plane #1: ไม่มีหน้าจอตั้งค่า แต่เสริม Silk Touch ไว้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="2 1 1" max="2.3 2 2">
        (2) Formation Plane: กรองเฉพาะ Amethyst Cluster
        <ItemImage id="minecraft:amethyst_cluster" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1.3 0.7 1" max="2 1 2">
        (3) Annihilation Plane #2: ไม่มีหน้าจอตั้งค่า แต่เสริม Fortune ได้
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="1 0 1" max="1.3 1 2">
        (4) Storage Bus #1: กรองเฉพาะ Amethyst Shard
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

  <BoxAnnotation color="#dddddd" min="0 0 .7" max="1 1 1">
        (5) Storage Bus #2: กรองเฉพาะ Amethyst Shard ตั้งลำดับความสำคัญสูงกว่าที่เก็บหลัก
        <ItemImage id="minecraft:amethyst_shard" scale="2" />
  </BoxAnnotation>

<DiamondAnnotation pos="0 0.5 0.5" color="#00ff00">
        ไปยังเครือข่ายหลัก
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Configurations

การตั้งค่า

* <ItemLink id="annihilation_plane" /> ตัวแรก (1) ไม่มีหน้าจอและตั้งค่าไม่ได้ แต่ต้องเสริม Silk Touch
* <ItemLink id="formation_plane" /> (2) กรองเฉพาะ <ItemLink id="minecraft:amethyst_cluster" />
* <ItemLink id="annihilation_plane" /> ตัวที่สอง (3) ไม่มีหน้าจอและตั้งค่าไม่ได้ แต่เสริม Fortune ได้
* <ItemLink id="storage_bus" /> ตัวแรก (4) กรองเฉพาะ <ItemLink id="minecraft:amethyst_shard" />
* <ItemLink id="storage_bus" /> ตัวที่สอง (5) กรองเฉพาะ <ItemLink id="minecraft:amethyst_shard" /> และตั้ง
  [ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงกว่าที่เก็บหลัก

## How It Works

หลักการทำงาน

1. <ItemLink id="annihilation_plane" /> ตัวแรกพยายามทุบสิ่งที่อยู่ด้านหน้า แต่ทุบได้เฉพาะ <ItemLink id="minecraft:amethyst_cluster" />
    เพราะที่เก็บเดียวบนเครือข่ายย่อยคือ <ItemLink id="formation_plane" /> ที่กรองเฉพาะ Amethyst Cluster ทั้งนี้ได้ผลเพราะ
Plane เสริม Silk Touch ไว้เท่านั้น มิฉะนั้นจะทุบหน่อที่ยังไม่โตได้ด้วยเพราะมันไม่ดรอปอะไร
2. <ItemLink id="formation_plane" /> วางกลุ่มผลึกบนบล็อกฝั่งตรงข้าม
3. <ItemLink id="annihilation_plane" /> ตัวที่สองทุบกลุ่มผลึกและได้ <ItemLink id="minecraft:amethyst_shard" />
4. <ItemLink id="storage_bus" /> ตัวแรกเก็บเศษผลึกลงถัง จริง ๆ ไม่ต้องกรอง เพราะสิ่งเดียว
ที่ Annihilation Plane ตัวที่สองควรพบคือกลุ่มผลึกที่โตเต็มที่แล้ว
5. <ItemLink id="storage_bus" /> ตัวที่สองเปิดให้เครือข่ายหลักเข้าถึง Amethyst Shard ทั้งหมดในถัง โดยตั้ง
[ลำดับความสำคัญ](../ae2-mechanics/import-export-storage.md#storage-priority) สูงเพื่อให้ Amethyst Shard ถูกนำ
กลับไปเก็บในถังก่อนที่เก็บหลัก
