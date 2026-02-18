# Saving a VTK model in a certain directory using Python

**Topic ID**: 3946
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/saving-a-vtk-model-in-a-certain-directory-using-python/3946

---

## Post #1 by @chaddy1004 (2018-08-30 13:33 UTC)

<p>Hi</p>
<p>Is there a way to save a .vtk file in a specific directory using Python? I would like to include this functionality in my script but could not find a good way to do it.</p>
<p>Thank you!</p>
<p>Chad Paik</p>

---

## Post #2 by @Sam_Horvath (2018-08-30 14:14 UTC)

<p>slicer.util.saveNode will work for saving model nodes to .vtk files.  Is that what you are trying to do?</p>
<p>slicer.util.saveNode(modelNode, ‘/path/of/file.vtk’)</p>
<p>You will need to specify the full path in order to put it in an arbitrary location.</p>

---

## Post #3 by @chaddy1004 (2018-08-30 14:59 UTC)

<p>Yes! This is exactly what I was looking for!</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
