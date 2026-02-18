# How to get current volume and model selection using Python

**Topic ID**: 11325
**Date**: 2020-04-28
**URL**: https://discourse.slicer.org/t/how-to-get-current-volume-and-model-selection-using-python/11325

---

## Post #1 by @Shicong (2020-04-28 06:14 UTC)

<p>It’s the default not on the volumeclipwithmodel “, the display is “select a volume” , without the mouse select. I want to get the active volume object of the volumes module from the python code, and the current model object of the module. Note that I am going to get volume and model objects in the python code, can you provide the code? Thanks so much! !!!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a2fa87d951ad8d680f5ac843d580206b4c45855.png" alt="图片" data-base62-sha1="hqUmefjRtBbHhnPZuJKth63sGm9" width="640" height="341"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94.png" data-download-href="/uploads/short-url/uj7BpIFRTNAA4V3oM1UX2ByM3qY.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94_2_557x500.png" alt="图片" data-base62-sha1="uj7BpIFRTNAA4V3oM1UX2ByM3qY" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94_2_557x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46a987061d0f74dc1ad9925dd4befcc70d06c94.png 2x" data-dominant-color="F3F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">644×578 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/914416c9071e59484c7f11d88716492b12dea189.png" data-download-href="/uploads/short-url/kJ571haqciAOiV2WSG3IOTAO1C1.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/914416c9071e59484c7f11d88716492b12dea189_2_453x500.png" alt="图片" data-base62-sha1="kJ571haqciAOiV2WSG3IOTAO1C1" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/914416c9071e59484c7f11d88716492b12dea189_2_453x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/914416c9071e59484c7f11d88716492b12dea189.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/914416c9071e59484c7f11d88716492b12dea189.png 2x" data-dominant-color="F1F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">662×730 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-28 14:00 UTC)

<p>You can access every widget of every module using <code>slicer.util.findChild()</code> function, but this should only be used for testing or diagnostics, not for implementing end-user workflows.</p>
<p>Your module should not depend on what nodes are selected to be edited in other module’s GUI. Doing this would severely restrict what you can do in Slicer (modules would keep interfering with each other and ultimately many things would be just impossible to do).</p>
<p>Instead, you put node selectors and various editing widgets into the GUI of your module. Module user interfaces are typically built from reusable widgets, so you can easily put together a GUI that is a combination of several other modules.</p>

---

## Post #3 by @Shicong (2020-04-29 06:50 UTC)

<p>Thank you for your answer <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
