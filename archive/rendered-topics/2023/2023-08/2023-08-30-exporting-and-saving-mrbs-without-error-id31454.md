---
topic_id: 31454
title: "Exporting And Saving Mrbs Without Error"
date: 2023-08-30
url: https://discourse.slicer.org/t/31454
---

# Exporting and saving mrbs without error

**Topic ID**: 31454
**Date**: 2023-08-30
**URL**: https://discourse.slicer.org/t/exporting-and-saving-mrbs-without-error/31454

---

## Post #1 by @trish (2023-08-30 21:59 UTC)

<p>Hi there,</p>
<p>I am running a Slicer 5.2 kernel in Jupyter notebook and looking to create Medical Reality Bundles (.mrbs) for radiotherapy patients for which I have their CTs, RTStructs, and RTDose files. Slicer is able to bundle the inputs and create the scene, and I can visually confirm the mrb creation as the patient mrbs load into Slicer. However, for some of the patients, it is not able to export and save the mrb correctly, currently executed at the end of my code like this:</p>
<pre><code>#Exporting
#p is the patient number
sceneSaveFilename = saveDir + p + ".mrb"
if slicer.util.saveScene(sceneSaveFilename):
    logging.info("Scene saved to: {0}".format(sceneSaveFilename))
else:
    logging.error("Scene saving failed")
</code></pre>
<p>It exports an mrb that gives this error when you try to open it in a different Slicer window:</p>
<ul>
<li>Error: Loading E:/TestORATOR/ORAT2-235-5.mrb - ERROR: In D:\D\S\S-0-build\VTK\IO\XMLParser\vtkXMLParser.cxx, line 379<br>
vtkMRMLParser (0000021D783653B0): Error parsing XML in stream at line 127, column 162, byte index 53698: not well-formed (invalid token)</li>
<li>Error: Loading E:/TestORATOR/ORAT2-235-5.mrb - Syntax error in scene file.</li>
</ul>
<p>I should note that if I manually save the mrb after the scene has loaded, I can open up those mrbs without error. However, I’d like to be able to loop through the patients and have Slicer save non-corrupt mrbs so that I wouldn’t have to manually save mrbs for each patient. Thanks!</p>

---

## Post #2 by @lassoan (2023-08-30 22:03 UTC)

<p>Could you have a look at the .mrml scene file to see what’s in line 127 at column 162?<br>
You can get the .mrml file by renaming the .mrb file to .zip and unzip it.</p>
<p>You can also try if the problem is fixed in Slicer-4.2.</p>

---

## Post #3 by @pieper (2023-08-30 22:57 UTC)

<p>My guess would be a bad character in a node name extracted from a dicom series description.  You might need to clean those up before saving.</p>

---
