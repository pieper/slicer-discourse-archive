# AttributeError: 'vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsROI' object has no attribute 'SetAndObserveObjectToNodeMatrix'

**Topic ID**: 27280
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/attributeerror-vtkslicermarkupsmodulemrmlpython-vtkmrmlmarkupsroi-object-has-no-attribute-setandobserveobjecttonodematrix/27280

---

## Post #1 by @spodamon (2023-01-16 21:59 UTC)

<p>I was trying to create a bounding box as shown in the documentation <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>. But I keep running into the error<br>
AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsROI’ object has no attribute ‘SetAndObserveObjectToNodeMatrix’<br>
Using Slicer 4.11.202210226</p>

---

## Post #2 by @lassoan (2023-01-16 22:01 UTC)

<p>This is a new API. I would recommend to use the current Slicer Stable Release or Slicer Preview Release. If you are forced to use an older Slicer version then make sure you use examples from the corresponding documentation version (you can select the documentation version in ReadTheDocs in the lower-left corner).</p>

---

## Post #3 by @spodamon (2023-01-16 22:12 UTC)

<p>Thank you for the quick response. Appreciate it. Could you link me to the page with the appropriate documentation? When I follow the link in the bottom left corner it says page not found. Thank You again.</p>

---

## Post #4 by @jamesobutler (2023-01-16 22:28 UTC)

<p>Slicer readthedocs only contains the Script Repository page for version 5.0 and newer. I would suggest that you upgrade from 4.11.20210226 to Slicer 5.2.1 which you can get at <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>
<p>The last version of the Script Repository on the old Slicer wiki can be found at:</p>
<p><a href="https://www.slicer.org/w/index.php?title=Documentation/Nightly/ScriptRepository&amp;oldid=63561" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/w/index.php?title=Documentation/Nightly/ScriptRepository&amp;oldid=63561</a></p>

---
