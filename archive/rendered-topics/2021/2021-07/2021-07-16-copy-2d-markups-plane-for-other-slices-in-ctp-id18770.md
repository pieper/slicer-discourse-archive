# Copy 2D Markups Plane for other slices in CTP

**Topic ID**: 18770
**Date**: 2021-07-16
**URL**: https://discourse.slicer.org/t/copy-2d-markups-plane-for-other-slices-in-ctp/18770

---

## Post #1 by @Dhruba (2021-07-16 18:01 UTC)

<p>Hello, I am trying to annotate my CTP data using Markups Plane. There are a total of 158 slices in my CT data. I want to create Markup Plane in only 1 slice and copy the markup for 3 slices above and 3 slices below of that slice. Is there a way to do that automatically? In that way, I don’t have to draw markup plane 7 times for 7 slices. I can draw just one markup plane and it will be automatically copied to 6 other slices (3 top and 3 below).<br>
I know that I can use 3D ROI to cover multiple slices together. But I need the 2D markup plane for this project.<br>
Please let me know if there is such option in slicer. Also, can I write a code in Python Interactor window to do this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67094291a908b97202ca7ad9247ef415d34c4a46.png" data-download-href="/uploads/short-url/eHv1aZPWKMhQD7tcF2yXyhM3ZLE.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67094291a908b97202ca7ad9247ef415d34c4a46_2_690x382.png" alt="Capture1" data-base62-sha1="eHv1aZPWKMhQD7tcF2yXyhM3ZLE" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67094291a908b97202ca7ad9247ef415d34c4a46_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67094291a908b97202ca7ad9247ef415d34c4a46_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67094291a908b97202ca7ad9247ef415d34c4a46.png 2x" data-dominant-color="80807F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1046×580 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-16 20:42 UTC)

<p>Normally you would use a 3D ROI for this.</p>
<p>If you really want to have 7 duplicate planes then you can write a short Python code snippet that this. The simplest is to add a keyboard shortcut for this, which calls your function that adds the 6 extra planes.</p>
<p>You can find all the examples that you will need in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>. You can get an <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">introduction to Python scripting in 3D Slicer in the PerkLab Slicer Programming tutorial</a>.</p>
<p>You can ask us here if you get stuck at any point.</p>

---

## Post #3 by @Dhruba (2021-07-18 17:04 UTC)

<p>I tried to copy the markup plane control points using “GetNthControlPoint”, but it gives an error saying ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsPla’ object has no attribute ‘GetNthControlPoint’.<br>
Also i tried using “GetNthFiducialPosition” which gives the same type of error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64902c3e1a7c17eadf45da88074f4ff2a508595b.png" data-download-href="/uploads/short-url/elCDqn3CauftcRDyAtswIjmLOt5.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64902c3e1a7c17eadf45da88074f4ff2a508595b_2_652x499.png" alt="1" data-base62-sha1="elCDqn3CauftcRDyAtswIjmLOt5" width="652" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64902c3e1a7c17eadf45da88074f4ff2a508595b_2_652x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64902c3e1a7c17eadf45da88074f4ff2a508595b_2_978x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64902c3e1a7c17eadf45da88074f4ff2a508595b_2_1304x998.png 2x" data-dominant-color="C7C7CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2136×1637 475 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can you kindly help me to copy the control points of markup plane?</p>

---

## Post #4 by @Dhruba (2021-07-18 17:27 UTC)

<p>FYI, I am using slicer 4.11.20210226 version.</p>

---

## Post #5 by @Dhruba (2021-07-18 17:57 UTC)

<p>I was able to copy the control points using</p>
<p>p1=[0,0,0]  <span class="hashtag">#np</span>.zeros(3)<br>
p2=[0,0,0]<br>
p3=[0,0,0]</p>
<p>f = getNode(‘F’)  <span class="hashtag">#F</span> is the name of markups plane</p>
<p>f.GetNthControlPointPositionWorld(0, p1)<br>
f.GetNthControlPointPositionWorld(1, p2)<br>
f.GetNthControlPointPositionWorld(2, p3)</p>
<p>But trying to figure out, how to paste the control points using a new markup plane name.</p>

---

## Post #6 by @lassoan (2021-07-18 18:56 UTC)

<p><code>[0,0,0]</code> is an integer array. You must create a vector of floating-point values for example using <code>np.zeros(3)</code> as it is done in all the examples. <code>[0.0, 0.0, 0.0]</code> would work, too, but it is longer and you cannot do numerical array operations on it directly.</p>
<p>You can create a new node using the scene’s <code>AddNewNodeByClass</code> method. See the script repository for examples.</p>

---

## Post #7 by @Dhruba (2021-07-18 20:45 UTC)

<p>Thanks a lot, Lasso. I was able to do what I wanted. But when I use the python interactor window, after closing the slicer app; I have to write the code again to work. Is there a way to save this change?</p>

---

## Post #8 by @lassoan (2021-07-19 11:55 UTC)

<p>You can create a Python scripted module from this. See step-by-step instructions in the Slicer Programming tutorials.</p>

---

## Post #9 by @Dhruba (2021-07-19 18:33 UTC)

<p>I did that using JupyterKernel. Thanks.</p>

---
