# Python viewing two volumes side by side (four over four)

**Topic ID**: 19638
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/python-viewing-two-volumes-side-by-side-four-over-four/19638

---

## Post #1 by @S_Arbabi (2021-09-13 07:48 UTC)

<p>I wanted to have two volumes that I load from dicom series to be viewed side by side separately. something like this view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e64cadff1111f93682da9e9edcbbb78fb84a0ecb.jpeg" data-download-href="/uploads/short-url/wRk6qpDEJuy1SLKR2gRrLp72R1V.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e64cadff1111f93682da9e9edcbbb78fb84a0ecb_2_690x445.jpeg" alt="Capture" data-base62-sha1="wRk6qpDEJuy1SLKR2gRrLp72R1V" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e64cadff1111f93682da9e9edcbbb78fb84a0ecb_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e64cadff1111f93682da9e9edcbbb78fb84a0ecb_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e64cadff1111f93682da9e9edcbbb78fb84a0ecb.jpeg 2x" data-dominant-color="282834"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1318×851 40 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
how is the good approach to that?</p>

---

## Post #2 by @pieper (2021-09-13 14:37 UTC)

<p>Did you try the CompareVolumes module?  It doesn’t currently do 3D but does allow you to easily create layouts with axi/sag/cor views.  We’ve discussed generalizing it to a CompareData module but that’s not on any current roadmap.</p>

---

## Post #3 by @lassoan (2021-09-13 14:55 UTC)

<p>You can also <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">drag-and-drop the volumes from the Data module into the views</a> where you want to see them.</p>
<p><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/drag_to_view.gif" alt="" width="690" height="269"></p>

---
