# How can I register a 3D view in segmentation?

**Topic ID**: 19347
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/how-can-i-register-a-3d-view-in-segmentation/19347

---

## Post #1 by @Antoine (2021-08-24 19:03 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @rbumm (2021-08-24 20:39 UTC)

<p>Welcome Antoine,</p>
<p>try</p>
<pre><code class="lang-auto">yourSegmentation.CreateClosedSurfaceRepresentation()
</code></pre>
<p>Regards<br>
rudolf</p>

---

## Post #3 by @Antoine (2021-08-25 07:52 UTC)

<p>Thank you for your answer!<br>
I did it but i don’t think i was clear.<br>
I already have the 3D And now i want to get rid of Green red and yellow in order to record (using a graphic table) the 3D model.<br>
We want to make disappear some of the structures and to move around.<br>
Is it possible to do so?</p>
<p>Thank you for your help<br>
Antoine</p>
<p>Envoyé de mon iPhone</p>

---

## Post #4 by @rbumm (2021-08-25 11:20 UTC)

<aside class="quote no-group" data-username="Antoine" data-post="3" data-topic="19347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7ab992/48.png" class="avatar"> Antoine:</div>
<blockquote>
<p>I already have the 3D And now i want to get rid of Green red and yellow in order to record (using a graphic table) the 3D model.</p>
</blockquote>
</aside>
<p>You want to switch to 3D view only from a python script ? Or do you want to do that manually within slicer ?</p>

---

## Post #5 by @Antoine (2021-08-25 12:01 UTC)

<p>We thought doing it with slicer.<br>
We want to record it with Two screens : one for the segmentations and the other with only the 3D model</p>
<p>Envoyé de mon iPhone</p>

---

## Post #6 by @rbumm (2021-08-25 13:07 UTC)

<p>For showing 3D only within Slicer please go:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03628d2a9106dc89905c46ca159c96926fcf5100.png" data-download-href="/uploads/short-url/tWzPmuYVlQqcMvM3271utei3u0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03628d2a9106dc89905c46ca159c96926fcf5100.png" alt="image" data-base62-sha1="tWzPmuYVlQqcMvM3271utei3u0" width="270" height="500" data-dominant-color="BDBFC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">340×629 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @rbumm (2021-08-25 13:10 UTC)

<p>In oder to show / hide individual segmentations or change opacities go to “Segmentations”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f3abc42690b40d1fc369508c70aeaa913afa876.png" data-download-href="/uploads/short-url/91lV4Tir2ZTKe9P0JLAl9XIFQAm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3abc42690b40d1fc369508c70aeaa913afa876_2_646x500.png" alt="image" data-base62-sha1="91lV4Tir2ZTKe9P0JLAl9XIFQAm" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3abc42690b40d1fc369508c70aeaa913afa876_2_646x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3abc42690b40d1fc369508c70aeaa913afa876_2_969x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f3abc42690b40d1fc369508c70aeaa913afa876_2_1292x1000.png 2x" data-dominant-color="BBBEDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1292×999 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Antoine (2021-08-25 13:12 UTC)

<p>I don’t have on my screen. When i load my .mrb the icon disappear.</p>
<p>Envoyé de mon iPhone</p>

---

## Post #9 by @Antoine (2021-08-25 13:33 UTC)

<p>Thanks a lot it works!</p>
<p>Envoyé de mon iPhone</p>

---

## Post #10 by @Antoine (2021-08-25 13:41 UTC)

<p>Sorry to bother you again.<br>
We don’t manage to create à rotation point.<br>
We marked a fiducial node but then when i go to transform i can’t get the application to work…</p>
<p>Envoyé de mon iPhone</p>

---

## Post #11 by @rbumm (2021-08-25 19:53 UTC)

<p>Find details on that procedure in the script repository</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point</a></p>

---

## Post #12 by @Antoine (2021-08-25 20:20 UTC)

<p>Thank you we managed to do it with transforms!<br>
Antoine</p>
<p>Envoyé de mon iPhone</p>

---
