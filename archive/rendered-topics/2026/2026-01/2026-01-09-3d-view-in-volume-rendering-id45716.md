# 3d view in volume rendering

**Topic ID**: 45716
**Date**: 2026-01-09
**URL**: https://discourse.slicer.org/t/3d-view-in-volume-rendering/45716

---

## Post #1 by @alex_He (2026-01-09 09:15 UTC)

<p>I wander is all dicom volume series can have a 3d view display in volume rendering? I find a few volumes cannot display in 3d view</p>

---

## Post #2 by @ebrahim (2026-01-09 13:22 UTC)

<p>Once you’ve got your DICOM volume loaded into Slicer as a <em>scalar volume node</em>, it should always be displayable in the 3D view.</p>

---

## Post #3 by @chir.set (2026-01-09 17:05 UTC)

<p>This <a href="https://discourse.slicer.org/t/gpu-based-volume-rendering-fails-if-one-dimension-is-more-than-2000px/6546">post</a> may be helpful.</p>

---

## Post #4 by @alex_He (2026-01-10 02:12 UTC)

<p>hi</p>
<p>I try some dicom files , yes it did , but when I try my dicom files from my hospital, it does NOT , I search the Internet and also seek help from chatgpt, still donot get is displayed, is there some criteria that the dicom series must satisfied inorder to display the 3d view in volume rendering?</p>

---

## Post #5 by @muratmaga (2026-01-10 02:14 UTC)

<p>if these are regular clinical exams (like CT or MR), they should work perfectly fine. What have you tried and what have failed?</p>

---

## Post #6 by @alex_He (2026-01-10 02:21 UTC)

<p>I goto volume rendering module and select my dicom volume, the axial coronarl and sagittal 2d view appear, I can scroll and see the images, but my 3d view is blank, I try all combinations of the preset values and try to modify them. They all failed. My dicom series is ct scan, and I check the properly of the volume, it seams everything is in order.</p>

---

## Post #7 by @muratmaga (2026-01-10 02:38 UTC)

<p>Did you turn on the 3D visibility on from the volume rendering? What happens if you simply drag the dicom object in the scene (from the data module) on to the 3D viewer?</p>
<p>can you provide a screenshot with the volume information visible (from volumes module)?</p>

---

## Post #8 by @alex_He (2026-01-10 02:44 UTC)

<p>there is no 3d view option button . When I dragon the object to the 3d view as you suggest, nothing happen.</p>

---

## Post #9 by @alex_He (2026-01-10 02:47 UTC)

<p>I am not with the computer, will get a screen shot and get back to you ASAP.</p>

---

## Post #10 by @muratmaga (2026-01-10 04:13 UTC)

<p>There is a visibility button. You might want to review the Volume Rendering module documentation.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" target="_blank" rel="noopener nofollow ugc">Volume rendering — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @alex_He (2026-01-10 04:53 UTC)

<p>OK I will try and get back to you</p>

---

## Post #12 by @cpinter (2026-01-13 10:43 UTC)

<p>Maybe your 3D view is not centered on the volume, and it is displayed but simply it is not in front of the camera. Please try clicking this button</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/272ddf39821d6e56f417f1ece40e854af18cb906.png" alt="image" data-base62-sha1="5AATTIMaJ3VFx7aWRJhpwNI9RKS" width="162" height="64"></p>

---

## Post #13 by @alex_He (2026-01-17 03:23 UTC)

<p>I drag  volume to the 3d view, some show out but some show nothing.</p>

---

## Post #14 by @alex_He (2026-01-17 03:25 UTC)

<p>Ok I found the visibility icon. Thanks</p>

---

## Post #15 by @alex_He (2026-01-17 03:28 UTC)

<p>Yes, I know the center button, thanks for your suggestion.  But if the 3d shows nothing, center button zoom in out pan fit screen all down not help</p>

---

## Post #16 by @pieper (2026-01-17 15:15 UTC)

<p>That probably means there’s something different about your image data that makes it incompatible with the volume rendering module.  You can look in the Volumes module (Volume Information) and see how it’s different from any sample data that works.</p>

---

## Post #17 by @alex_He (2026-01-28 02:53 UTC)

<p>Thanks for your advise . I checked the volume information but I did not see significant differences from the sample data</p>

---

## Post #18 by @muratmaga (2026-01-28 05:10 UTC)

<p>I think they only way we can help you if you share your dataset, or at the minimum provide the full detail on the Volumes module about the volume.</p>

---
