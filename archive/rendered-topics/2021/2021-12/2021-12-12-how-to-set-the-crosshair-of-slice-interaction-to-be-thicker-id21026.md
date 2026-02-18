# How to set the crosshair of slice interaction to be thicker?

**Topic ID**: 21026
**Date**: 2021-12-12
**URL**: https://discourse.slicer.org/t/how-to-set-the-crosshair-of-slice-interaction-to-be-thicker/21026

---

## Post #1 by @jumbojing (2021-12-12 10:25 UTC)

<p>The crosshair of slice interaction is too thin to see clearly,How to set it to be thicker in slices?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6845f24ce862be41a22667f7ffaaaa33caf445.jpeg" data-download-href="/uploads/short-url/AiAGh3j28dzO2TH23pGNtvTJbdb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6845f24ce862be41a22667f7ffaaaa33caf445_2_559x500.jpeg" alt="image" data-base62-sha1="AiAGh3j28dzO2TH23pGNtvTJbdb" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6845f24ce862be41a22667f7ffaaaa33caf445_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6845f24ce862be41a22667f7ffaaaa33caf445_2_838x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe6845f24ce862be41a22667f7ffaaaa33caf445_2_1118x1000.jpeg 2x" data-dominant-color="8C8C88"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1794×1602 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @jamesobutler (2021-12-12 18:38 UTC)

<p>See the following thread which covered this topic</p>
<aside class="quote" data-post="3" data-topic="18932">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-intersection-thickness/18932/3">Slice Intersection Thickness</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You need to dig into how to get the slice display nodes, but in most cases this for example will set the red slice intersection thickness to 5 points: 
getNode('vtkMRMLModelDisplayNode1').SetLineWidth(5)
  </blockquote>
</aside>


---

## Post #3 by @jumbojing (2021-12-12 19:55 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thanks<br>
谢谢老师</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d67ce6140be4dcea36991895644d2ed65a121e1.png" data-download-href="/uploads/short-url/dkiO7FTfmBwtleo6IawYnXxC8qR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d67ce6140be4dcea36991895644d2ed65a121e1_2_560x500.png" alt="image" data-base62-sha1="dkiO7FTfmBwtleo6IawYnXxC8qR" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d67ce6140be4dcea36991895644d2ed65a121e1_2_560x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d67ce6140be4dcea36991895644d2ed65a121e1_2_840x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d67ce6140be4dcea36991895644d2ed65a121e1_2_1120x1000.png 2x" data-dominant-color="2B3137"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1796×1602 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
