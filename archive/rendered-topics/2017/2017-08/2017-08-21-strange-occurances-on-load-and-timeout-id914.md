# Strange occurances on load and Timeout

**Topic ID**: 914
**Date**: 2017-08-21
**URL**: https://discourse.slicer.org/t/strange-occurances-on-load-and-timeout/914

---

## Post #1 by @stevenagl12 (2017-08-21 20:35 UTC)

<p>I have todays nightly build downloaded onto my computer and the command window for the system keeps saying:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/salewis/AppData/Roaming/NA-MIC/Extensions-26293/Chest_Imaging_Platform/lib/Slicer-4.7/qt-scripted-modules/CIP_LesionModel.py”, line 17, in <br>
from FeatureWidgetHelperLib import FeatureExtractionLogic<br>
ImportError: cannot import name FeatureExtractionLogic<br>
loadSourceAsModule - Failed to load file “C:/Users/salewis/AppData/Roaming/NA-MIC/Extensions-26293/Chest_Imaging_Platform/lib/Slicer-4.7/qt-scripted-modules/CIP_LesionModel.py”  as module “CIP_LesionModel” !<br>
Fail to instantiate module  "CIP_LesionModel"<br>
Failed to obtain reference to ‘qSlicerAppMainWindow’</p>
<p>Also causing a window to show up saying:<br>
There are other DICOM listeners running.<br>
Do you want to end them?</p>
<p>Not sure if the second is a big deal or not, but this is upon startup and it’s never done it before. Finally, I have been running the module openCAD and using the heterogeneityCAD, but every time it is causing the program to become unresponsive.</p>

---

## Post #2 by @pieper (2017-08-21 20:54 UTC)

<p>Looks like SlicerCIP will need to be updated to account for this change (it just requires a small change)</p>
<p><a href="https://github.com/Slicer/Slicer/commit/b420669b0f8bd93fc925aca592300d9cab43add9" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/b420669b0f8bd93fc925aca592300d9cab43add9</a></p>

---
