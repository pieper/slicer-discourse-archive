---
topic_id: 16792
title: "Changing The Name Of The Fiducial And Getting The Updated Na"
date: 2021-03-28
url: https://discourse.slicer.org/t/16792
---

# Changing the name of the fiducial and getting the updated names of the fiducial

**Topic ID**: 16792
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/changing-the-name-of-the-fiducial-and-getting-the-updated-names-of-the-fiducial/16792

---

## Post #1 by @will_kim (2021-03-28 04:46 UTC)

<p>Hi is there a way to print out the updated fiducials list even if I rename it from (‘F’) to something else? Right now I have to hardcode the names of my fiducials into .getNode() but was wondering if there is a better alternative way.</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2021-03-29 09:12 UTC)

<p>Based on your description it’s hard to know what you want to do with the fiducials and whether you want to use a certain fiducial node or all of them. Some more information would be quite useful.</p>
<p>Normally one creates a fiducial node from the module and then you can have control over it, for example you can add observers.</p>
<p>As you mention getNode by name, maybe it is useful to mention that you can get nodes by type. For example<br>
<code>collection = slicer.mrmlScene.GetNodesByClass('vtkMRMLMarkupsFiducialNode')</code><br>
or<br>
<code>fiducialNodes = getNodes('vtkMRMLMarkupsFiducialNode*')</code></p>

---

## Post #3 by @will_kim (2021-03-29 22:28 UTC)

<p>Ok, that works. Thanks!</p>

---
