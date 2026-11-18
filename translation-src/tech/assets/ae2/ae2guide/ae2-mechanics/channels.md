---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: ช่องสัญญาณ
  icon: controller
---

# Channels

ช่องสัญญาณ

[เครือข่าย ME](me-network-connections.md) ของ Applied Energistics 2 ต้องใช้
ช่องสัญญาณเพื่อรองรับ[อุปกรณ์](../ae2-mechanics/devices.md)ที่ใช้คลังหรือบริการต่าง ๆ
ในเครือข่าย ลองคิดว่าช่องสัญญาณเหมือนสาย USB ที่ต่ออุปกรณ์ คอมพิวเตอร์มีพอร์ต USB จำกัดจึงรองรับ
อุปกรณ์ได้จำกัด เครื่องจักร อุปกรณ์เต็มบล็อก และสายเคเบิลทั่วไปส่วนใหญ่ส่งผ่านได้
สูงสุด 8 ช่องสัญญาณ มองได้ว่าเป็นมัดสายสัญญาณ 8 เส้น แต่ [Dense Cable](../items-blocks-machines/cables.md#dense-cable) รองรับได้สูงสุด
32 ช่อง อุปกรณ์อื่นที่ส่งผ่านได้ 32 ช่องมีเพียง <ItemLink id="me_p2p_tunnel" />
และ [Quantum Network Bridge](../items-blocks-machines/quantum_bridge.md) ทุกครั้งที่อุปกรณ์ใช้ช่องสัญญาณ ให้นึกว่าดึงสาย USB หนึ่งเส้นออก
จากมัด สายนั้นจึงใช้ต่อไปตามแนวเดิมไม่ได้

<GameScene zoom="7" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_demonstration_1.snbt" />

  <LineAnnotation color="#33ff33" from="1 .4 .7" to="2.4 .4 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .7" to="2.4 .6 .7" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .6" to="2.6 .4 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .6 .6" to="2.6 .6 .6" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.4 .6 .7" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .4 .7" to="2.4 .4 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .6 .6" to="2.6 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 .6" to="2.6 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.1 .6 1.5" to="2.4 .6 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.6 .4 1.5" to="2.9 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="2.6 .6 1.5" to="2.6 .9 1.5" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="2.4 .1 1.5" to="2.4 .4 1.5" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .4" to="3.5 .6 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="3.5 .6 .4" to="3.5 .9 .4" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="3.5 .1 .4" to="3.5 .4 .4" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1 .6 .3" to="1.5 .6 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1 .4 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#33ff33" from="1.5 .6 .3" to="1.5 .9 .3" alwaysOnTop={true}/>
  <LineAnnotation color="#33ff33" from="1.5 .1 .3" to="1.5 .4 .3" alwaysOnTop={true}/>

  <LineAnnotation color="#ff3333" from="3.5 .5 .5" to="5.5 .5 .5" alwaysOnTop={true}>
  ใช้ครบทั้ง 8 ช่องในสายเคเบิลแล้ว Drive จึงไม่ได้รับช่องสัญญาณ
  </LineAnnotation>

  <LineAnnotation color="#993333" from="1 .5 .5" to="1.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="1.5 .5 .5" to="1.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2 .5 .5" to="2.25 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="2.5 .5 .5" to="2.75 .5 .5" alwaysOnTop={true}/>
  <LineAnnotation color="#993333" from="3 .5 .5" to="3.25 .5 .5" alwaysOnTop={true}/>

  <DiamondAnnotation pos="3.6 0.5 0.5" color="#ff0000">
        ใช้ครบทั้ง 8 ช่องในสายเคเบิลแล้ว Drive จึงไม่ได้รับช่องสัญญาณ
    </DiamondAnnotation>

  <IsometricCamera yaw="15" pitch="30" />
</GameScene>

ใช้ [Smart Cable](../items-blocks-machines/cables.md) เพื่อดูเส้นทางและจำนวนช่องสัญญาณที่ใช้ในเครือข่ายได้ง่าย ๆ โดยข้อมูลจะแสดงบนสาย

ช่องสัญญาณใช้พลังงาน 1⁄128 ae/t ต่อจุดที่ผ่าน ดังนั้น
การเพิ่ม <ItemLink id="controller" /> ให้
เครือข่ายที่มีอุปกรณ์ 8 ชิ้นและมากกว่า 96 จุด อาจ
ลดการใช้พลังงานได้จริง เพราะเปลี่ยนวิธีจัดสรรช่องสัญญาณ

จำไว้ว่า ช่องสัญญาณไม่เกี่ยวกับสีสายเคเบิล สีมีหน้าที่เพียงป้องกันสายต่างสีเชื่อมกัน

## Channel Routing

เส้นทางช่องสัญญาณ

เมื่อใช้ <ItemLink id="controller" />
ช่องสัญญาณจะหาเส้นทาง 3 ขั้น เริ่มจากเส้นทางสั้นที่สุดผ่านเครื่องข้างเคียงไปยัง[สายปกติ](../items-blocks-machines/cables.md)ที่ใกล้ที่สุด
คือ Glass, Covered หรือ Smart แล้วหาเส้นทางสั้นที่สุดตามสายปกติไปยัง [Dense Cable](../items-blocks-machines/cables.md) ที่ใกล้ที่สุด
คือ Dense หรือ Dense Smart จากนั้นตาม Dense Cable ด้วยเส้นทางสั้นที่สุดไปยัง <ItemLink id="controller" />
หากเส้นทางที่สั้นที่สุดเต็มแล้ว [อุปกรณ์](devices.md)บางชิ้นอาจไม่ได้รับช่องสัญญาณที่ต้องใช้ ควรใช้
สายสี Cable Anchor และ Tunnel ช่วยบังคับเส้นทางให้เป็นไปตามต้องการ

ตัวอย่างนี้ Drive บางเครื่องไม่ได้รับช่องสัญญาณ แม้สายทั้งหมดมีความจุพอ เพราะ
ช่องสัญญาณเลือกเส้นทางสั้นที่สุด ทำให้สายบางเส้นเกินความจุ ขณะที่บางเส้นว่าง

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 3.6" to="1.4 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.4 0.5 3.6" to="1.4 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 1.6" to="0.6 .5 1.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 1.6" to="0.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#ff3333" from="0.6 .5 3.4" to="1.4 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#ff3333" from="3 .5 3.4" to="1.6 .5 3.4" alwaysOnTop={true} thickness="0.05"/>

  <BoxAnnotation color="#dddddd" min="1.2 0.2 3.2" max="1.8 0.8 3.8" alwaysOnTop={true} thickness="0.05">
        มีช่องสัญญาณพยายามผ่านจุดนี้มากกว่า 8 ช่อง บางส่วนจึงถูกตัดออก
  </BoxAnnotation>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

แก้ได้ด้วยการกำหนดเส้นทางให้ชัดเจนขึ้น ควรจัดเครือข่ายเป็นรูปต้นไม้หรือพุ่มไม้
ลดวงวนและเส้นทางที่กำกวมให้เหลือน้อยที่สุด

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/channel_path_length_issue_fix.snbt" />

  <LineAnnotation color="#33ff33" from="3 .5 1.4" to="0.4 0.5 1.4" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 .5 1.4" to="0.4 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="0.4 0.5 5.6" to="1 0.5 5.6" alwaysOnTop={true} thickness="0.05"/>

  <LineAnnotation color="#33ff33" from="3 0.5 3.6" to="1.6 0.5 3.6" alwaysOnTop={true} thickness="0.05"/>
  <LineAnnotation color="#33ff33" from="1.6 0.5 3.6" to="1.6 0.5 5" alwaysOnTop={true} thickness="0.05"/>

  <IsometricCamera yaw="90" pitch="90" />

</GameScene>

## Ad-Hoc Networks

เครือข่าย Ad-Hoc

เครือข่ายที่ไม่มี <ItemLink id="controller" />
ถือเป็นแบบ Ad-Hoc รองรับอุปกรณ์ที่ใช้ช่องสัญญาณได้สูงสุด 8 ชิ้น
หากเกิน 8 ชิ้น อุปกรณ์ที่ต้องใช้ช่องสัญญาณในเครือข่ายจะหยุดทำงาน
แก้โดยถอดอุปกรณ์บางชิ้นออก หรือเพิ่ม <ItemLink id="controller" />

ต่างจากเครือข่ายที่มี Controller โดย [Smart Cable](../items-blocks-machines/cables.md) ในเครือข่าย Ad-Hoc จะแสดงจำนวน
ช่องสัญญาณที่ใช้ทั้งเครือข่าย แทนจำนวนที่ผ่านสายเส้นนั้น

ในเครือข่าย Ad-Hoc อุปกรณ์แต่ละชิ้น
ใช้ 1 ช่องจากทั้งเครือข่าย ซึ่งต่างจากการที่ <ItemLink id="controller" /> จัดสรรช่อง
ตามเส้นทางสั้นที่สุด

## Design

ออกแบบเครือข่าย

ตามหัวข้อ[เส้นทางช่องสัญญาณ](channels.md#channel-routing) ควรจัดเครือข่ายเป็นรูปต้นไม้ ให้ Dense Cable แตกแขนงจาก Controller แล้วให้สายปกติ
แตกแขนงจาก Dense Cable โดยจัด[อุปกรณ์](../ae2-mechanics/devices.md)เป็นกลุ่มละไม่เกิน 8 ชิ้นบนสายปกติ

ตัวอย่างที่ไม่ควรทำ:

เมื่อตามเส้นทางช่องสัญญาณ:

1. ออกจาก Controller ทางขวาก็เกิดคอขวดเหลือ 8 ช่อง เพราะ Drive ทำงานเหมือนสายปกติ
แต่ไม่ได้ใช้ Smart Cable จึงมองไม่เห็นจำนวนช่องที่ใช้ เหลือ 8 ช่อง
2. Drive ใช้ไปหนึ่งช่อง
เหลือ 7 ช่อง
3. ส่งขึ้นไปยัง Terminal 2 ช่อง
เหลือ 5 ช่อง
4. ไปทางขวาต่อ Interface ใช้อีกหนึ่งช่อง
เหลือ 4 ช่อง
5. ส่งขึ้นไปยัง Pattern Provider 1 ช่อง
เหลือ 3 ช่อง
6. ไปทางขวาต่อ ส่งขึ้นไปยัง Import Bus 1 ช่อง
เหลือ 2 ช่อง
7. กลุ่ม Pattern Provider ที่ป้อน Assembler ได้รับเพียง 2 ช่อง จึงมี Provider 2 ตัวไม่ได้รับช่องสัญญาณ

สรุปว่าปัญหาเกิดจากคอขวดและการไม่ได้วางแผนกระจายช่องสัญญาณให้ทั่วถึง

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="../assets/assemblies/bad_network_structure.snbt" />

<LineAnnotation color="#33ff33" from="6.5 .5 1.5" to="6 .5 1.5" alwaysOnTop={true} thickness="0.4">
  32 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="6 .5 1.5" to="5.5 .5 1.5" alwaysOnTop={true} thickness="0.2">
  8 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 1.5 1.5" alwaysOnTop={true} thickness="0.1">
  2 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="5.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 1.5 1.5" to="5.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 2.5 1.5" to="5.5 2.5 1.1" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="5.5 .5 1.5" to="4.5 .5 1.5" alwaysOnTop={true} thickness="0.158">
  5 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 .3 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="4.5 1.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="4.5 .5 1.5" to="3.5 .5 1.5" alwaysOnTop={true} thickness="0.122">
  3 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="3.5 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 2.5 1.5" to="3.7 2.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="3.5 .5 1.5" to="1.5 .5 1.5" alwaysOnTop={true} thickness="0.1">
  2 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="1.5 0.3 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="1.5 0.5 1.5" to="0.5 0.5 1.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#33ff33" from="0.5 0.5 1.5" to="0.5 0.5 0.5" alwaysOnTop={true} thickness="0.071">
  1 ช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#ff3333" from="0.5 1.5 1.5" to="0.5 1.3 1.5" alwaysOnTop={true} thickness="0.071">
  ไม่มีช่องสัญญาณ
</LineAnnotation>

<LineAnnotation color="#ff3333" from="1.5 1.5 0.5" to="1.5 1.3 0.5" alwaysOnTop={true} thickness="0.071">
  ไม่มีช่องสัญญาณ
</LineAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

---

ตัวอย่างโครงสร้างที่ดี:

<GameScene zoom="2.5" interactive={true}>
  <ImportStructure src="../assets/assemblies/treelike_network_structure.snbt" />

    <BoxAnnotation color="#dddddd" min="6.9 0 4.9" max="9.1 4 7.1" thickness="0.05">
        สังเกตว่า Pattern Provider แยกเป็นกลุ่มละ 8 ตัว
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 4 4" max="8 5 5" thickness="0.05">
        เมื่อสายปกติสองเส้นที่ใช้ช่องเต็มมารวมกัน ต้องเปลี่ยนเป็น Dense Cable
    </BoxAnnotation>

    <BoxAnnotation color="#dddddd" min="5 0 13" max="8 1 14" thickness="0.05">
        ใช้สายเคเบิลต่างสีเพื่อไม่ให้สายที่ติดกันเชื่อมเข้าหากัน
    </BoxAnnotation>


  <IsometricCamera yaw="315" pitch="30" />
</GameScene>

## Channel Modes

โหมดช่องสัญญาณ

AE2 10.0.0 สำหรับ Minecraft 1.18 เพิ่มตัวเลือกเปลี่ยนการทำงานของช่องสัญญาณในโลก
มีตัวเลือกใหม่ในหมวดทั่วไปชื่อ `channels` และมีคำสั่งในเกมให้ผู้ดูแลเปลี่ยนโหมด
พร้อมค่าตั้งจากในเกม ใช้ `/ae2 channelmode <mode>`
เพื่อเปลี่ยน และ `/ae2 channelmode` เพื่อดูโหมดปัจจุบัน เมื่อเปลี่ยนโหมดในเกม เครือข่ายทั้งหมดจะ
เริ่มทำงานใหม่และใช้โหมดใหม่ทันที

ตัวเลือกนี้นำความสามารถจาก Minecraft 1.12 กลับมาและปรับปรุงให้มีทางเลือกที่ดีขึ้นสำหรับ
ผู้เล่นที่อยากเล่นสบายขึ้นเล็กน้อย แต่ยังต้องการระบบช่องสัญญาณอยู่

ตารางต่อไปนี้แสดงโหมดที่ใช้ได้ทั้งในไฟล์ตั้งค่าและคำสั่ง

| การตั้งค่า    | คำอธิบาย                                                                                                                                                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default`  | โหมดมาตรฐาน ใช้ความจุของสายและเครือข่าย Ad-Hoc ตามที่อธิบายในคู่มือนี้                                                                                                                           |
| `x2`       | เพิ่มความจุทุกแบบเป็นสองเท่า (สายปกติ 16 ช่อง, Dense Cable 64 ช่อง และ Ad-Hoc รองรับ 16 ช่อง)                                                                                                                           |
| `x3`       | เพิ่มความจุทุกแบบเป็นสามเท่า (สายปกติ 24 ช่อง, Dense Cable 92 ช่อง และ Ad-Hoc รองรับ 24 ช่อง)                                                                                                                           |
| `x4`       | เพิ่มความจุทุกแบบเป็นสี่เท่า (สายปกติ 32 ช่อง, Dense Cable 128 ช่อง และ Ad-Hoc รองรับ 32 ช่อง)                                                                                                                       |
| `infinite` | ยกเลิกข้อจำกัดช่องสัญญาณทั้งหมด Controller ยังลดการใช้พลังงานของเครือข่ายได้มาก ส่วน Smart Cable จะแสดงเพียงดับทั้งหมดเมื่อไม่มีช่องสัญญาณ หรือสว่างเต็มเมื่อมีอย่างน้อย 1 ช่อง |