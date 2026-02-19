---
topic_id: 22583
title: "Export Rt Structure"
date: 2022-03-18
url: https://discourse.slicer.org/t/22583
---

# Export RT Structure

**Topic ID**: 22583
**Date**: 2022-03-18
**URL**: https://discourse.slicer.org/t/export-rt-structure/22583

---

## Post #1 by @lharzee (2022-03-18 14:10 UTC)

<p>I have imported some dicom data ( CT and RT structure) from an other TPS.<br>
I would like to use 3d slicer to create new segment and export this to the TPS.<br>
When i use the module “export to dicom” and export the RT structure, 3d slicer changes some metadata in the file. I don’t more have the possibilitie to import directly the new file in my TPS.<br>
If i can do this, It 's necesseray to export also the new CT created into 3d slicer when i export the RT Structure, to import this CT into my TPS and do a registration to have the possibilitie to copy the new segmentation.<br>
Do you have a solution to solve this problem.<br>
Thanks</p>

---

## Post #2 by @cpinter (2022-03-21 14:29 UTC)

<p>RTStruct export currently creates a whole new study, and you need to export the CT as well.</p>
<p>Hwever, I don’t understand why yo need to do registration. The exported CT is exactly in the same coordinate frame as the CT you imported.</p>

---
