---
topic_id: 33841
title: "Vmtk Automatic Centerline And Export Control Points As Xyz C"
date: 2024-01-17
url: https://discourse.slicer.org/t/33841
---

# VMTK automatic centerline and export control points as XYZ coordinates

**Topic ID**: 33841
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/vmtk-automatic-centerline-and-export-control-points-as-xyz-coordinates/33841

---

## Post #1 by @RD_morph (2024-01-17 19:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.6.1<br>
Expected behavior: Use the ExtractCenterline.py code to automatically generate centerlines for existing models and export XYZ control points of centerlines<br>
Actual behavior: Trying to run the .py code in slicer python console results in nothing happening</p>
<p>Hi all - I have a few thousand models (meshes created in a different software) for which I need to generate centerlines and then obtain the XYZ coordinates of the control points of each centerline. I can execute this manually but was hoping to streamline to process due to the large volume of models.</p>
<p>I have attempted to automate the process by running the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L378" rel="noopener nofollow ugc">VMTK extract centerline code</a> with no success. I have gone through many topics here to solve my problem but nothing has worked. I’m a fairly novice coder (mostly Python) and the existing code is well beyond my understanding. I had a ton of errors initially but seemed to resolve them by downloading/fixing some .py files that were not included in the imported packages. Now, when I try to run code in the console literally nothing happens - the code just turns grey. I also attempted <a href="https://discourse.slicer.org/t/automatic-centerline/14829/23">this code</a> but have yet to successfully debug it on my end.</p>
<p>How do I get the extract centerline code to actually run in the console? And is this process even any faster than the manual process? It seems like I will have to manually export the control point coordinates regardless of automation. I apologize if this is a very basic question - I’m not sure what I’m missing here.</p>

---
