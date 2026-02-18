# How do I add Ultrasonic probe STL into a scene?

**Topic ID**: 15895
**Date**: 2021-02-08
**URL**: https://discourse.slicer.org/t/how-do-i-add-ultrasonic-probe-stl-into-a-scene/15895

---

## Post #1 by @Carl098 (2021-02-08 05:43 UTC)

<p>Hi, I’m writing a module.<br>
I’d like to implement a function that will load a probe in the upper right after pressing the Apply button.<br>
Like this,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b78d2427e9c4c3842eddc4d8b6359869b18e084.jpeg" data-download-href="/uploads/short-url/fkJWLuetN6LpCUKf659QxnjJD7e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b78d2427e9c4c3842eddc4d8b6359869b18e084_2_690x411.jpeg" alt="image" data-base62-sha1="fkJWLuetN6LpCUKf659QxnjJD7e" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b78d2427e9c4c3842eddc4d8b6359869b18e084_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b78d2427e9c4c3842eddc4d8b6359869b18e084_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b78d2427e9c4c3842eddc4d8b6359869b18e084.jpeg 2x" data-dominant-color="42424C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1343×800 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
How do I write this part of my Python program.<br>
Thanks!</p>

---

## Post #2 by @lassoan (2021-02-08 05:53 UTC)

<p>You can use <code>slicer.util.loadModel()</code> function. See many examples in the <a href="https://slicer.util.loadModel">script repository</a>. You can find Python scripting tutorials and documentation <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">here</a>.</p>

---

## Post #3 by @Carl098 (2021-02-08 08:06 UTC)

<p>Thank you very much.<br>
How can I add interaction to the model so that I can resize and position it.</p>

---

## Post #4 by @ungi (2021-02-08 22:34 UTC)

<p>You can create a transform node in the Transforms module, and use that to transform (rotate, shift, etc.) any model, including your ultrasound model. I’m not sure what exactly you are trying to achieve, but maybe some of these tutorial will help too: <a href="http://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a></p>

---
