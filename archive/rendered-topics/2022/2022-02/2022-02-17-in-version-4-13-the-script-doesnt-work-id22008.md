---
topic_id: 22008
title: "In Version 4 13 The Script Doesnt Work"
date: 2022-02-17
url: https://discourse.slicer.org/t/22008
---

# In version 4.13 ，the script doesn't work

**Topic ID**: 22008
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/in-version-4-13-the-script-doesnt-work/22008

---

## Post #1 by @slicer365 (2022-02-17 01:15 UTC)

<p>Hello,everyone！<br>
version 4.13 0215<br>
win 10<br>
Problem as is shown in the picture<br>
and I can’t find the module SlicerElastix in the new version extention manager<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b31402da2a13a314be85a24f5db61e1c4dc44575.png" data-download-href="/uploads/short-url/pycl8lZXFDcFq0o7bbF6UCLvzMh.png?dl=1" title="1645060374(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31402da2a13a314be85a24f5db61e1c4dc44575_2_517x284.png" alt="1645060374(1)" data-base62-sha1="pycl8lZXFDcFq0o7bbF6UCLvzMh" width="517" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31402da2a13a314be85a24f5db61e1c4dc44575_2_517x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31402da2a13a314be85a24f5db61e1c4dc44575_2_775x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b31402da2a13a314be85a24f5db61e1c4dc44575.png 2x" data-dominant-color="AFA8A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1645060374(1)</span><span class="informations">976×537 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-02-18 04:47 UTC)

<p><code>vtkMRMLDIsplayNode1</code>, <code>vtkMRMLDIsplayNode2</code>, <code>vtkMRMLDIsplayNode3</code> were never guaranteed to correspond to slice display nodes. They happened to get those node IDs in a range of Slicer versions, but not in older and very recent Slicer versions.</p>
<p>You can access slice display nodes via slice logic object, for example as it is shown in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-views-renderers-and-cameras">example</a>.</p>
<hr>
<p>Thank you for reporting the missing SlicerElastix extension. It is because of the recent update of ITK library. We expect to resolve the problem soon. Until then you can use a Slicer version from 2 weeks ago that you can download using this link: <a href="https://download.slicer.org/?offset=-14">https://download.slicer.org/?offset=-14</a></p>

---
