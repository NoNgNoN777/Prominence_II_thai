---
navigation:
  parent: example-setups/example-setups-index.md
  title: เครือข่ายย่อยแบบท่อไอเทม/ของเหลว
  icon: storage_bus
---

# Item/Fluid "Pipe" Subnet

เครือข่ายย่อยแบบท่อไอเทม/ของเหลว

วิธีง่าย ๆ ในการจำลองท่อไอเทมหรือของเหลวด้วย [อุปกรณ์](../ae2-mechanics/devices.md) AE2 ใช้ได้กับทุกอย่างที่ต้องใช้ท่อไอเทมหรือของเหลว
รวมถึงการส่งผลผลิตจากการคราฟต์กลับเข้า <ItemLink id="pattern_provider" />

โดยทั่วไปทำได้สองวิธี:

## Import Bus -> Storage Bus

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_storage_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        (1) Import Bus: ตั้งตัวกรองได้
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        (2) Storage Bus: ตั้งตัวกรองได้ ตัวนี้ (และ Storage Bus อื่นที่ต้องการใช้เป็นปลายทาง)
        ต้องเป็นที่เก็บเพียงอย่างเดียวบนเครือข่าย
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
        ต้นทาง
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
        ปลายทาง
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="import_bus" /> (1) บนช่องเก็บของต้นทางนำไอเทมหรือของเหลวเข้า และพยายามเก็บไว้ใน [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
เนื่องจากที่เก็บเดียวบนเครือข่ายคือ <ItemLink id="storage_bus" /> (2) (จึงต้องเป็นเครือข่ายย่อย ไม่ใช่เครือข่ายหลัก) ไอเทมหรือของเหลว
จึงถูกวางลงช่องเก็บของปลายทาง เกิดเป็นการถ่ายโอน รับพลังงานผ่าน <ItemLink id="quartz_fiber" />
ตั้งตัวกรองทั้ง Import Bus และ Storage Bus ได้ แต่ถ้าไม่ตั้ง ระบบจะถ่ายโอนทุกสิ่งที่เข้าถึงได้
ระบบนี้ใช้กับ Import Bus และ Storage Bus หลายตัวได้ด้วย

## Storage Bus -> Export Bus

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/storage_export_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        (1) Storage Bus: ตั้งตัวกรองได้ ตัวนี้ (และ Storage Bus อื่นที่ต้องการใช้เป็นต้นทาง)
        ต้องเป็นที่เก็บเพียงอย่างเดียวบนเครือข่าย
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        (2) Export Bus: ต้องตั้งตัวกรอง
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#00ff00">
        ต้นทาง
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#00ff00">
        ปลายทาง
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<ItemLink id="export_bus" /> บนช่องเก็บของปลายทางพยายามดึงไอเทมที่อยู่ในตัวกรองจาก [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md)
เนื่องจากที่เก็บเดียวบนเครือข่ายคือ <ItemLink id="storage_bus" /> (จึงต้องเป็นเครือข่ายย่อย ไม่ใช่เครือข่ายหลัก) ไอเทมหรือของเหลว
จึงถูกดึงจากช่องเก็บของต้นทาง เกิดเป็นการถ่ายโอน รับพลังงานผ่าน <ItemLink id="quartz_fiber" />
Export Bus ต้องตั้งตัวกรองจึงจะทำงาน ระบบนี้จึงทำงานเฉพาะเมื่อตั้งตัวกรองให้ Export Bus แล้ว
ระบบนี้ใช้กับ Storage Bus และ Export Bus หลายตัวได้ด้วย

## A Setup That Does Not Work (Import Bus -> Export Bus)

ระบบที่ใช้ไม่ได้ (Import Bus -> Export Bus)

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_export_pipe.snbt" />

<BoxAnnotation color="#dd3333" min="3.7 0 0" max="4 1 1">
        Import Bus: เนื่องจากเครือข่ายไม่มีที่เก็บ จึงไม่มีที่ให้นำของเข้า
  </BoxAnnotation>

<BoxAnnotation color="#dd3333" min="1 0 0" max="1.3 1 1">
        (2) Export Bus: เนื่องจากเครือข่ายไม่มีที่เก็บ จึงไม่มีของให้ส่งออก
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 0.5" color="#ff0000">
        ต้นทาง
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 0.5" color="#ff0000">
        ปลายทาง
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

ระบบที่มีเพียง Import Bus และ Export Bus ใช้ไม่ได้ Import Bus จะพยายามดึงของจากช่องเก็บต้นทาง
มาเก็บไอเทมหรือของเหลวในที่เก็บของเครือข่าย ส่วน Export Bus จะพยายามดึงจากที่เก็บของเครือข่ายแล้วใส่
ไอเทมหรือของเหลวลงช่องเก็บปลายทาง แต่เนื่องจากเครือข่ายนี้ **ไม่มีที่เก็บ** Import Bus จึงนำเข้าไม่ได้
และ Export Bus ส่งออกไม่ได้ จึงไม่เกิดอะไรขึ้น

## Inputting And Outputting Through 1 Face

ป้อนเข้าและส่งออกผ่านด้านเดียว

สมมติคุณมีเครื่องที่รับวัตถุดิบและดึงผลผลิตออกผ่านด้านเดียวได้ (เช่น <ItemLink id="charger" />)
คุณส่งวัตถุดิบเข้าและดึงผลผลิตออกพร้อมกันได้ โดยรวมเครือข่ายย่อยแบบท่อสองวิธี:

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/import_storage_export_pipe.snbt" />

<BoxAnnotation color="#dddddd" min="4 1 1" max="5 1.3 2">
        (1) Import Bus: ตั้งตัวกรองได้
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 1 1" max="3 1.3 2">
        (2) Storage Bus: ตั้งตัวกรองได้ ตัวนี้ (และ Storage Bus อื่นที่ต้องการใช้ส่งและดึงไอเทม)
        ต้องเป็นที่เก็บเพียงอย่างเดียวบนเครือข่าย
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="2 0 1" max="3 1 2">
        (3) สิ่งที่ต้องการส่งเข้าและดึงออก: ในตัวอย่างนี้คือ Charger
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 1" max="1 1.3 2">
        (4) Export Bus: ต้องตั้งตัวกรอง
  </BoxAnnotation>

<DiamondAnnotation pos="4.5 0.5 1.5" color="#00ff00">
        ต้นทาง
    </DiamondAnnotation>

<DiamondAnnotation pos="0.5 0.5 1.5" color="#00ff00">
        ปลายทาง
    </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Interfaces

Interface

ปรากฏว่ายังมี [อุปกรณ์](../ae2-mechanics/devices.md) อื่นนอกจาก Import Bus และ Export Bus ที่ส่งไอเทมเข้า
และดึงไอเทมออกจาก [ที่เก็บของเครือข่าย](../ae2-mechanics/import-export-storage.md) ได้!
ตัวที่เกี่ยวข้องคือ <ItemLink id="interface" /> หากใส่ไอเทมที่ไม่ได้ตั้งให้ Interface สำรองไว้ มันจะ
ส่งเข้าไปในที่เก็บของเครือข่าย ซึ่งนำมาใช้คล้ายท่อ Import Bus -> Storage Bus ได้ การตั้ง Interface ให้
สำรองไอเทมจะดึงไอเทมนั้นจากที่เก็บของเครือข่าย คล้ายท่อ Storage Bus -> Export Bus ตั้งให้ Interface
สำรองของบางชนิดแต่ไม่สำรองชนิดอื่นได้ จึงส่งและดึงของระยะไกลผ่าน Storage Bus ได้หากต้องการ

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/interface_pipes.snbt" />

<BoxAnnotation color="#dddddd" min="3.7 0 0" max="4 1 1">
        Interface
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 1">
        Storage Bus
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="3.7 0 2" max="4 1 3">
        Storage Bus
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 1 2" max="1 1.3 3">
        Storage Bus
  </BoxAnnotation>

<IsometricCamera yaw="195" pitch="30" />
</GameScene>

## One-To-Many and Many-To One (and many-to-many)

หนึ่งต่อหลาย และหลายต่อหนึ่ง (รวมหลายต่อหลาย)

แน่นอนว่าไม่จำเป็นต้องใช้ <ItemLink id="import_bus" /> หรือ <ItemLink id="export_bus" /> หรือ <ItemLink id="storage_bus" /> เพียงตัวเดียว

<GameScene zoom="3" background="transparent">
<ImportStructure src="../assets/assemblies/many_to_many_pipe.snbt" />

<IsometricCamera yaw="185" pitch="30" />
</GameScene>

## Providing To Multiple Places

จ่ายวัตถุดิบให้หลายจุด

จากทั้งหมดนี้ เราสร้างวิธีส่งวัตถุดิบจากด้านหนึ่งของ <ItemLink id="pattern_provider" /> ไปยังหลาย
ตำแหน่ง เช่น เครื่องจักรเป็นแถว หรือหลายด้านของเครื่องเดียว

เราไม่ต้องการท่อ Import -> Storage หรือ Storage -> Export เพราะ <ItemLink id="pattern_provider" /> ไม่ได้
เก็บวัตถุดิบอยู่ภายในจริง ๆ แต่ Provider จะ *ส่ง* วัตถุดิบเข้าช่องเก็บของข้างเคียง จึงต้องมี
ช่องเก็บของข้างเคียงที่นำไอเทมเข้าได้ด้วย

ฟังดูเหมือน... <ItemLink id="interface" />!
ตรวจให้ Provider อยู่ในโหมดกำหนดทิศทางหรือแบบแผ่นย่อย และ/หรือ Interface เป็นแบบแผ่นย่อย เพื่อไม่ให้ทั้งสองเชื่อม
เป็นเครือข่ายเดียวกัน

<GameScene zoom="6" background="transparent">
<ImportStructure src="../assets/assemblies/provider_interface_storage.snbt" />

<BoxAnnotation color="#dddddd" min="2.7 0 1" max="3 1 2">
        Interface (ต้องเป็นแบบแผ่น ไม่ใช่บล็อกเต็ม)
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="1 0 0" max="1.3 1 4">
        Storage Bus
  </BoxAnnotation>

<BoxAnnotation color="#dddddd" min="0 0 0" max="1 1 4">
        จุดที่ต้องการให้ Pattern Provider จ่ายวัตถุดิบ (หลายเครื่อง หรือหลายด้านของเครื่องเดียว)
  </BoxAnnotation>

<IsometricCamera yaw="185" pitch="30" />
</GameScene>