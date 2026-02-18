# Modul "Export Tractography to PLY (mesh)" doesn't work in Slicer 5.7.0

**Topic ID**: 40805
**Date**: 2024-12-19
**URL**: https://discourse.slicer.org/t/modul-export-tractography-to-ply-mesh-doesnt-work-in-slicer-5-7-0/40805

---

## Post #1 by @Elisabeth (2024-12-19 16:06 UTC)

<p>Problem report for Slicer 5.7.0-2024-12-13 win-amd64: [please describe expected and actual behavior]</p>
<p>Dear community,<br>
I’ve done tractography in the 3D Slicer 5.7.0 software and now I planned to export my fiber bundle as a ply in order to continue processing and make a 3D print. With the 5.6.2 software I had no problem and the export went well. Then my 5.6.2 software crashed sometimes during my work and I decided to go for the newer version. Now my question: Is it a generell bug, that the export modul doesn’t work in the 5.7.0 version or maybe, did I do something wrong?<br>
Any help and advise is much welcome!<br>
Best regards, Elisabeth</p>

---

## Post #2 by @pieper (2024-12-19 20:26 UTC)

<p>Are you using this script?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-tract-fiberbundle-to-blender-including-color">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-tract-fiberbundle-to-blender-including-color</a></p>
<p>As far as I know any recent version should work.</p>
<p>If you are getting a crash, please report the exact steps how to reproduce, ideally using public data (there are DTI scans in the SampleData).</p>

---
