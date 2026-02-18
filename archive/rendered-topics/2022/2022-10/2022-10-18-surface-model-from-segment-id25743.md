# Surface model from segment

**Topic ID**: 25743
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/surface-model-from-segment/25743

---

## Post #1 by @A_B (2022-10-18 02:19 UTC)

<p>Hello,</p>
<p>I am trying to create a model of the outer surface of a segment. I have tried wrap solidify extension, surface model module &gt; model maker and hollow. The only one that worked in making a surface model without internal structures is wrap solidify. However, it also creates an abnormal surface attached to the segment as shown in the images (The green mandible is the segment and the yellow mandible is created after using wrap solidify extension). Please let me know which tool to use to create a surface model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/817efbc10be7cee45d5bbc7192990535e6a8af6e.png" data-download-href="/uploads/short-url/itzEzvv1OOinVqNH2xLXmaGR7HM.png?dl=1" title="mandible" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/817efbc10be7cee45d5bbc7192990535e6a8af6e_2_506x500.png" alt="mandible" data-base62-sha1="itzEzvv1OOinVqNH2xLXmaGR7HM" width="506" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/817efbc10be7cee45d5bbc7192990535e6a8af6e_2_506x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/817efbc10be7cee45d5bbc7192990535e6a8af6e_2_759x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/817efbc10be7cee45d5bbc7192990535e6a8af6e.png 2x" data-dominant-color="9599C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mandible</span><span class="informations">837×827 63.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562bea8850c71c8492805b6e9f69630c83fa5bd6.png" data-download-href="/uploads/short-url/cij9rFEFVBrnnhkrdSKHeIiBeh8.png?dl=1" title="mandible wrap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562bea8850c71c8492805b6e9f69630c83fa5bd6_2_532x500.png" alt="mandible wrap" data-base62-sha1="cij9rFEFVBrnnhkrdSKHeIiBeh8" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562bea8850c71c8492805b6e9f69630c83fa5bd6_2_532x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562bea8850c71c8492805b6e9f69630c83fa5bd6_2_798x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562bea8850c71c8492805b6e9f69630c83fa5bd6.png 2x" data-dominant-color="9895B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mandible wrap</span><span class="informations">828×777 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-10-18 03:02 UTC)

<p>That peak at the top may have been caused by a small speckle that you did not notice. You can use Island effect / Keep largest island to ensure that these small pieces are removed.</p>

---

## Post #3 by @mau_igna_06 (2022-10-18 16:25 UTC)

<p>After you do what Andras suggested, I think you should use the WrapSolidify option “carve holes” with 30mm value and click apply</p>

---

## Post #4 by @A_B (2022-10-18 22:42 UTC)

<p>Thank you very much. it worked with both suggestions but carve holes was set at 0.1000mm. There was a slight difference between the original segment and created model.</p>

---
