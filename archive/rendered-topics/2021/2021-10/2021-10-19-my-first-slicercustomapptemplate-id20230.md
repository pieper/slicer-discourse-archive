---
topic_id: 20230
title: "My First Slicercustomapptemplate"
date: 2021-10-19
url: https://discourse.slicer.org/t/20230
---

# My first SlicerCustomAppTemplate

**Topic ID**: 20230
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/my-first-slicercustomapptemplate/20230

---

## Post #1 by @fghazouani (2021-10-19 11:49 UTC)

<p>Hello,</p>
<p>I am following the tutorial of <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> and I have created a directory contains the CMakeLists for my custom slicer build by using the Custom app template generation procedure :</p>
<pre><code class="lang-auto">pip install cookiecutter jinja2-github
cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
</code></pre>
<p>Now I have this folder:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69ff56f08b13ac19a55caa350c773fe75d21ca8e.png" alt="image" data-base62-sha1="f7HcdcOuhWVpDIPuurw2e9K9nOu" width="520" height="496"></p>
<p>My question is what I must do after those steps.<br>
I tried to follow build instruction for Mac OS:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c99093a166271af510563fb8e40d694a03d65a0.png" data-download-href="/uploads/short-url/8E4wDCrQGoZpNrklV2nIIvV1kYw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c99093a166271af510563fb8e40d694a03d65a0_2_690x237.png" alt="image" data-base62-sha1="8E4wDCrQGoZpNrklV2nIIvV1kYw" width="690" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c99093a166271af510563fb8e40d694a03d65a0_2_690x237.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c99093a166271af510563fb8e40d694a03d65a0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c99093a166271af510563fb8e40d694a03d65a0.png 2x" data-dominant-color="DFEABC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×290 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I don’t know what path source I must use in the cmake command: the path source of Slicer or the path source of the directory of the generated template.</p>
<p>Please I need your help!!</p>

---

## Post #2 by @cpinter (2021-10-19 14:33 UTC)

<p>You don’t need to checkout and edit the cookie cutter code. All you need to do is call it: <code>cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate</code></p>

---

## Post #4 by @jcfr (2021-10-19 20:49 UTC)

<aside class="quote no-group quote-post-not-found" data-username="fghazouani" data-post="3" data-topic="20230">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f07891/48.png" class="avatar"> fghazouani:</div>
<blockquote>
<p>So, when I have used the directory of the generated template “/…/ SlicerCustomAppTemplate” it works very well now.</p>
</blockquote>
</aside>
<p>Great. Thanks for reporting back.</p>
<p>Let us know if you have additional questions.</p>

---

## Post #6 by @lassoan (2021-10-22 17:52 UTC)

<p>You can make changes anytime and then need to build the application again to make the changes have an effect. You don’t need to rebuild from scratch, so these builds will take just a few minutes and not hours.</p>

---
