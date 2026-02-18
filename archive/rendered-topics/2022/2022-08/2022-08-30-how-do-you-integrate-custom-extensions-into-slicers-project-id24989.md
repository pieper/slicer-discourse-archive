# How do you integrate custom extensions into Slicer's project

**Topic ID**: 24989
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/how-do-you-integrate-custom-extensions-into-slicers-project/24989

---

## Post #1 by @miniminic (2022-08-30 02:45 UTC)

<p>I created an extension and now I want to integrate it into Slicer’s project, like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5a5d280ac463dfeaf7b8f992c4545e57e178bb2.png" data-download-href="/uploads/short-url/z36fFWFo3uDtF6vjYvduxz8cbHs.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a5d280ac463dfeaf7b8f992c4545e57e178bb2_2_390x500.png" alt="捕获" data-base62-sha1="z36fFWFo3uDtF6vjYvduxz8cbHs" width="390" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a5d280ac463dfeaf7b8f992c4545e57e178bb2_2_390x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a5d280ac463dfeaf7b8f992c4545e57e178bb2_2_585x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5a5d280ac463dfeaf7b8f992c4545e57e178bb2_2_780x1000.png 2x" data-dominant-color="2A2929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">839×1073 44.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jay1987 (2022-08-31 02:09 UTC)

<p>i don’t known how to add it in cmake way ,it’s hard to learn slicer cmakelist<br>
but i have a alternative way<br>
right click the project -&gt;add -&gt;custom project<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce3e7ebe75c7e19e651e2ac936f6035ca97efa47.png" data-download-href="/uploads/short-url/tqwfKvebRTjmDA14sWLWPDyQ53p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce3e7ebe75c7e19e651e2ac936f6035ca97efa47.png" alt="image" data-base62-sha1="tqwfKvebRTjmDA14sWLWPDyQ53p" width="690" height="152" data-dominant-color="DDE3F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">757×167 5.98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
add your project debug or release into the slicer project<br>
if you have more project,you can create a folder to manager them<br>
but the bad news is that when out enviroment has changed,you have to do it again</p>

---

## Post #3 by @miniminic (2022-08-31 03:54 UTC)

<p>This is also a good solution, thanks</p>

---
