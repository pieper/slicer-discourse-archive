# How to generate a "mean model" between few amount of surface mesh?

**Topic ID**: 24793
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/how-to-generate-a-mean-model-between-few-amount-of-surface-mesh/24793

---

## Post #1 by @joanne40226 (2022-08-17 05:30 UTC)

<p>Hi community, i want to generate a “mean model” between few amount (i will show the schematic diagram with 2 data sets) of surface mesh as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd1d1ca013ef4a668006305123913fdb3db6db2f.jpeg" data-download-href="/uploads/short-url/A79aEpYDsIvK6A6yPdkebTRj4iH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd1d1ca013ef4a668006305123913fdb3db6db2f_2_690x423.jpeg" alt="image" data-base62-sha1="A79aEpYDsIvK6A6yPdkebTRj4iH" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd1d1ca013ef4a668006305123913fdb3db6db2f_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd1d1ca013ef4a668006305123913fdb3db6db2f_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd1d1ca013ef4a668006305123913fdb3db6db2f.jpeg 2x" data-dominant-color="858AAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1216×747 91.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ee44d5c57831ce53d3b1c380a54d8b41833d67.jpeg" data-download-href="/uploads/short-url/wwmSdGrUJAqTtHJiitR7TuFiD9t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ee44d5c57831ce53d3b1c380a54d8b41833d67_2_690x431.jpeg" alt="image" data-base62-sha1="wwmSdGrUJAqTtHJiitR7TuFiD9t" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ee44d5c57831ce53d3b1c380a54d8b41833d67_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ee44d5c57831ce53d3b1c380a54d8b41833d67_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ee44d5c57831ce53d3b1c380a54d8b41833d67.jpeg 2x" data-dominant-color="979CAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1187×743 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Besides, the suface mesh are already aligned.<br>
Is there any module that i can generate a “mean model” between them? Thank you for your time.</p>

---

## Post #2 by @lassoan (2022-08-17 10:30 UTC)

<p>You can use modules in <a href="https://slicermorph.github.io/">SlicerMorph</a> and <a href="https://salt.slicer.org/">SlicerSALT</a> extensions for this. A simple PCA (that can be computed by the GPA module of SlicerMorph) can provide you a mean shape, but there are many more tools in these extensions for shape modeling and analysis.</p>

---

## Post #4 by @joanne40226 (2022-08-18 09:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Hi, now i finished generating landmarks from the surface mesh i got.<br>
However, when building mean shape by them, i follow up your suggestion by using GPA<br>
im not sure if i did it right but i only get one slice() and the 3D visualization seem to be weird<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ec549f7e65e80ca192880413a15583737044604.png" data-download-href="/uploads/short-url/mEy83sHv8ih36hry2uHanqRlh2s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec549f7e65e80ca192880413a15583737044604_2_690x432.png" alt="image" data-base62-sha1="mEy83sHv8ih36hry2uHanqRlh2s" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec549f7e65e80ca192880413a15583737044604_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec549f7e65e80ca192880413a15583737044604_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ec549f7e65e80ca192880413a15583737044604.png 2x" data-dominant-color="A198AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1220×764 86.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>where red and green LMs are my two data sets and pink is the mean shape it generated.<br>
The mean shape it generated seem to be extremely close</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/738dc44ca541addc6b1f9a4beb07f17c499d8bb2.png" data-download-href="/uploads/short-url/gueDRUKp6XMsslk8BEIdZV1JNzI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/738dc44ca541addc6b1f9a4beb07f17c499d8bb2.png" alt="image" data-base62-sha1="gueDRUKp6XMsslk8BEIdZV1JNzI" width="326" height="500" data-dominant-color="E9EAE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">421×644 8.84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Am i wrong when doing that? thank you for your help!</p>

---

## Post #5 by @lassoan (2022-08-18 09:52 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/bpaniagua">@bpaniagua</a> can you recommend modules that can compute mean shape of already aligned models?</p>

---

## Post #6 by @muratmaga (2022-08-18 17:04 UTC)

<p><a class="mention" href="/u/joanne40226">@joanne40226</a> please follow this tutorial to assign one of your models as a reference model.</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_2#3d-interactive-visualization-and-exporting-animations">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_2#3d-interactive-visualization-and-exporting-animations" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_2#3d-interactive-visualization-and-exporting-animations" target="_blank" rel="noopener nofollow ugc">Tutorials/GPA_2 at main · SlicerMorph/Tutorials - 3D interactive visualization and exporting animations</a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GPA_2#3d-interactive-visualization-and-exporting-animations" target="_blank" rel="noopener nofollow ugc">main/GPA_2</a></p>

  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The blue model you will see in the right-hand viewer (<span class="hashtag">#2</span>) will be mean model .</p>
<p>You can then go to the Data module, and right click on the object that says <strong>PCA Warped Volume</strong> and you can export it as a model. Make sure you do not touch the PC sliders (or that they are at 0,0).</p>
<p>If you do want to explore variation, you can use the sliders.</p>

---

## Post #7 by @joanne40226 (2022-08-19 07:04 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you both a lot!<br>
i just figure it out it is bcuz i did not choose the option<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37000b5eabb1603de99c891d3d2193bcf5174e09.png" alt="image" data-base62-sha1="7Qym4zRAs16APBAD2aNRnWzZxpL" width="202" height="21"></p>
<p>so it would be scaled into unit.<br>
after i clicked it, it seems to be good.</p>
<p>Thank you for your time!</p>

---
