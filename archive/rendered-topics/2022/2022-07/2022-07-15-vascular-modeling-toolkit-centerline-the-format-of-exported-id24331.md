# Vascular Modeling Toolkit: Centerline. The format of exported centerline.

**Topic ID**: 24331
**Date**: 2022-07-15
**URL**: https://discourse.slicer.org/t/vascular-modeling-toolkit-centerline-the-format-of-exported-centerline/24331

---

## Post #1 by @NwahsHou (2022-07-15 15:48 UTC)

<p>Hi,<br>
The centerline curve was successfully obtained, but how can I define the format of exported file.<br>
3D silcer gives 3 types of format: .mrk.json, .json and .fcsv.<br>
As I want to preserve the structure and the metadata, I need to use .vtp or .vtk format.<br>
Could someone help me to do next?<br>
Thanks so much.</p>

---

## Post #2 by @mau_igna_06 (2022-07-15 17:32 UTC)

<p>You should select the create model option on centerline module. That would give you a 3D model that contains polydata and the pointdata you want to save. After you create it, just click the save dialog and select the format you want</p>
<p>Hope it helps</p>

---
