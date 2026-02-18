# Skeletal representation

**Topic ID**: 10478
**Date**: 2020-02-29
**URL**: https://discourse.slicer.org/t/skeletal-representation/10478

---

## Post #1 by @Dyatsen (2020-02-29 13:15 UTC)

<p>Hello.<br>
i am following the tutorial of skeletal representation (<a href="https://docs.google.com/presentation/d/1BF5Y4wAXOAS2yfdrmJeujrZFiKsnh9GwOs-XgQg8RZE/present?slide=id.p1" class="inline-onebox" rel="noopener nofollow ugc">SrepModule-Tutorial_v5.0 - Google Slides</a>). But there is SkeletalRepresentationRefiner in the tutorial:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b39501bc85257ae13dbac877ec9806fd8fbf3e7f.png" alt="image" data-base62-sha1="pCEIbT6XsiobCJzPRc4Bm1Y0m6j" width="445" height="153"><br>
and i just can find Initializer and Visualizer in the modules list.<br>
Also, the tutorial said<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07454f8975eced53851964239c8ff0639314f1b9.png" alt="image" data-base62-sha1="12jQ43kFUyRsGL1ESVq28RNkHtT" width="554" height="177"> . While I can not find the S-rep<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4410a06280488b0ad42fee651b04b7bd37bdf6e9.png" data-download-href="/uploads/short-url/9I85Anu0brQR1XP5Whlv3lKspg5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4410a06280488b0ad42fee651b04b7bd37bdf6e9_2_690x437.png" alt="image" data-base62-sha1="9I85Anu0brQR1XP5Whlv3lKspg5" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4410a06280488b0ad42fee651b04b7bd37bdf6e9_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4410a06280488b0ad42fee651b04b7bd37bdf6e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4410a06280488b0ad42fee651b04b7bd37bdf6e9.png 2x" data-dominant-color="E2E6E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">827×524 85.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> .<br>
Can someone help me see where the problem is?<br>
Thanks in advance!</p>

---

## Post #2 by @Dyatsen (2020-02-29 13:26 UTC)

<p>I’ve tried another way to install the SkeletalRepresentationRefiner module via github. But when i built the s-rep extension using command cmake, the error occurred.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ec0537d4946a585253d85c700d4a4d80c94df7.png" data-download-href="/uploads/short-url/89FCCPkB2LXgJ4gUG4B81fUl0j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ec0537d4946a585253d85c700d4a4d80c94df7.png" alt="image" data-base62-sha1="89FCCPkB2LXgJ4gUG4B81fUl0j" width="690" height="499" data-dominant-color="3D1932"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">830×601 89.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
So i can not install the extension via souce code.<br>
Can someone help me please?</p>

---

## Post #3 by @Zhiy (2020-03-02 20:37 UTC)

<p>Hi Dyatsen,</p>
<p>The s-rep extension is not yet shipped in Slicer binary. I suggest you build it from its source.</p>

---

## Post #4 by @Zhiy (2020-03-02 20:44 UTC)

<aside class="quote no-group" data-username="Dyatsen" data-post="2" data-topic="10478">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e56c9b/48.png" class="avatar"> Dyatsen:</div>
<blockquote>
<p>So i can not install the extension via souce code.</p>
</blockquote>
</aside>
<p>I assume there is no Slicer built in your machine. This page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a> will help you in building Slicer. Note the versions of software required.</p>
<p>After building Slicer, you need to configure the Slicer_DIR for the extension. Overall, the extension relies on Slicer. Building it with CMAKE is analogous to building your projects in windows with Visual studio: for example, if project A uses libraries provided by project B, you need compile and bulid project B first and then add it into your build configurations for project A.</p>
<p>Hope this helps.</p>
<p>Zhiyuan</p>

---
