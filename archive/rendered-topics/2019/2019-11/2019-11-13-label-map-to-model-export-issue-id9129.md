---
topic_id: 9129
title: "Label Map To Model Export Issue"
date: 2019-11-13
url: https://discourse.slicer.org/t/9129
---

# Label Map to Model-Export issue

**Topic ID**: 9129
**Date**: 2019-11-13
**URL**: https://discourse.slicer.org/t/label-map-to-model-export-issue/9129

---

## Post #1 by @Melodicpinpon (2019-11-13 12:50 UTC)

<p>Goodafternoon from Montpellier, gentlemen,</p>
<p>I downloaded a dicom from Open anatomy (the one about the inner ear) saved it and opened it on my computer. The temporal bone model (it contains a bunch of models) is a bit rough/fat sothat I made a new ‘Structure’ (or is it a ‘Labelmap’?) through the ‘Editor’ module with the ‘Treshold’ tool and applied it.</p>
<p>As I would like to export an .stl from it, I chose the ‘MakeModelEffect’ tool and applied it but do not find any new model; I can only show the result of my ‘Ear-CT-bone-label’ in the ‘Volume Rendering’ module.</p>
<p>When I look within the ‘Surface Model’&gt;‘Model Maker’ module an error message tells me that:<br>
ERROR: cannot open input volume file C:/Users/GAUTHI~1/AppData/Local/Temp/Slicer/DIGEI_vtkMRMLLabelMapVolumeNodeE.nrrd</p>
<p>It is weird since the dicom is not saved in this folder, and that there is no ‘Slicer’ folder within C:/Users/GAUTHI~1/AppData/Local/Temp/</p>
<p>Thank you if you can help me with this one.</p>

---

## Post #2 by @rkikinis (2019-11-13 13:30 UTC)

<p>Hi,</p>
<p>3D Slicer does not work with special characters in the path.try to put software and data in a location without the ~ character in the path.<br>
I would recommend to use the segment editor, not the older interactive editor. There are tutorials on how to perform segmentations and output .stl files.</p>
<p>Best</p>
<p>Ron</p>

---

## Post #3 by @Melodicpinpon (2019-11-13 16:13 UTC)

<p>Thank you so much; I will do that. (I was wondering why there were two similar modules but followed an old tutorial).</p>
<p>The problem has been resolved through a change within<br>
‘Welcome to 3D Slicer’ &gt;‘Customise 3D slicer’&gt;Modules&gt;Temporary directory.<br>
It was pointing to a protected(unwritable) folder.</p>
<p>There was also a change to do in<br>
‘Welcome to 3D Slicer’ &gt;‘Customise 3D slicer’&gt;Cache&gt;Cache size has been raised to 2000Mb<br>
and CacheFreeBuffer lowered to 10Mb.</p>

---
