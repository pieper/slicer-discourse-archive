# Linear transformation problem

**Topic ID**: 13298
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/linear-transformation-problem/13298

---

## Post #1 by @CHRIS_HUYNH (2020-09-02 14:13 UTC)

<p>Hi,</p>
<p>I’m trying to apply linear transformations to my robot links, but whenever I save the entire scene and reopen it, the area that specifies which links are transformed disappears shown in the image.</p>
<p>I’m current in the base_link transformation, but the base_link doesn’t appear in the “Transformed” box. I can still translate and rotate the base_link, but it just doesn’t appear in the transformed box. Is this an issue or can I neglect it.</p>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96dba56ea9df6bebeffaecb9138e5424d67bf306.png" data-download-href="/uploads/short-url/lwyd2RHquAzYhBmogjVR9biXVmC.png?dl=1" title="issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96dba56ea9df6bebeffaecb9138e5424d67bf306_2_690x460.png" alt="issue" data-base62-sha1="lwyd2RHquAzYhBmogjVR9biXVmC" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96dba56ea9df6bebeffaecb9138e5424d67bf306_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96dba56ea9df6bebeffaecb9138e5424d67bf306_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/96dba56ea9df6bebeffaecb9138e5424d67bf306_2_1380x920.png 2x" data-dominant-color="5C5B63"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">issue</span><span class="informations">3000×2000 560 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-09-02 15:01 UTC)

<p>Thanks for reporting this. Could you share a saved scene (.mrb) file that reproduces this problem?</p>

---

## Post #3 by @CHRIS_HUYNH (2020-09-03 09:32 UTC)

<p>Hi Andras,</p>
<p>This is the link to abb scene. I’ve uploaded it to onedrive.</p>
<p>I open the scene up using the (.mrml) file, I’m unsure of where the (.mrb) file is.</p>
<p><a href="https://1drv.ms/u/s!AsyU2pv-0QIdjRdA5cQ7mhii2QwW?e=drR5Ii" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/u/s!AsyU2pv-0QIdjRdA5cQ7mhii2QwW?e=drR5Ii</a></p>

---

## Post #4 by @CHRIS_HUYNH (2020-09-03 09:37 UTC)

<p>I think I’ve fixed the issue by just restarting the 3D slicer software each time I load up a new scene, but unsure how long this method will last.</p>

---
