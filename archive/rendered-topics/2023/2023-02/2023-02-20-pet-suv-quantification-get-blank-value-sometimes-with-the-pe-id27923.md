# PET SUV quantification get blank value sometimes. (with the PET Standard Value Computation module)

**Topic ID**: 27923
**Date**: 2023-02-20
**URL**: https://discourse.slicer.org/t/pet-suv-quantification-get-blank-value-sometimes-with-the-pet-standard-value-computation-module/27923

---

## Post #1 by @zhang_ming (2023-02-20 10:52 UTC)

<p>Aim：SUVmax/SUVmean and other relevant parameters were obtained by mapping the 3D ROI (not cross-sectional) of intestinal cross-section through the target area</p>
<p>For some reason, the correct SUV value rarely appeared, and sometimes the value was blank.</p>
<ol>
<li>
<p>We do not know whether the method is wrong, but have we have got the correct value according to the same method? The next day we’re going to do the same procedure with the same patient, and we can’t get the correct numbers.</p>
</li>
<li>
<p>I wonder whether there is air in the intestine, which leads to the failure to output the correct value?</p>
</li>
<li>
<p>Due to the winding and shape of the intestine, which is different from other solid organs, there is no good continuity between the cross sections of the intestine. After drawing each truncated surface to generate 3D ROI region, there is an obvious error: the synthetic 3D ROI region is not in the correct position of the intestine.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a381aaa875c96b44a8e2615305cdc1c8b8409a86.jpeg" data-download-href="/uploads/short-url/nkrDvfOLJ8rkEGkmPXJuxcbU6rQ.jpeg?dl=1" title="a6bc4f8b62c8295dd4efbf1f61d3eeb" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a381aaa875c96b44a8e2615305cdc1c8b8409a86_2_690x347.jpeg" alt="a6bc4f8b62c8295dd4efbf1f61d3eeb" data-base62-sha1="nkrDvfOLJ8rkEGkmPXJuxcbU6rQ" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a381aaa875c96b44a8e2615305cdc1c8b8409a86_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a381aaa875c96b44a8e2615305cdc1c8b8409a86_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a381aaa875c96b44a8e2615305cdc1c8b8409a86_2_1380x694.jpeg 2x" data-dominant-color="6A6A6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a6bc4f8b62c8295dd4efbf1f61d3eeb</span><span class="informations">1596×804 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @3sa5c64x (2023-04-20 06:39 UTC)

<p>Ni hao,<br>
make a long story short，</p>
<ol>
<li>import DICOM files and add segmentation</li>
<li>go to quantification -  segment statistics (<strong>important</strong>) module</li>
<li>select segmentation and volume</li>
<li>select PET volume statistics Options (SUVbw Maximum …)</li>
<li>click Apply</li>
</ol>

---

## Post #3 by @mikbuch (2023-04-20 08:20 UTC)

<p><a class="mention" href="/u/zhang_ming">@zhang_ming</a>, what do you mean by the “correct” SUV value? Did you validate the result with some other software, and you expected to see the same SUV in Slicer?</p>
<p>What was the console output for the cases in which you got blank values?</p>
<p>To open a console, click the double down arrow next to the “Status: Completed” label:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98c5a7cd16630b51dc0eb0e497dfaaf69da21783.jpeg" data-download-href="/uploads/short-url/lNu37LfYtovzUChNoV9ZYhWKWcz.jpeg?dl=1" title="a381aaa875c96b44a8e2615305cdc1c8b8409a86" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98c5a7cd16630b51dc0eb0e497dfaaf69da21783_2_690x347.jpeg" alt="a381aaa875c96b44a8e2615305cdc1c8b8409a86" data-base62-sha1="lNu37LfYtovzUChNoV9ZYhWKWcz" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98c5a7cd16630b51dc0eb0e497dfaaf69da21783_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98c5a7cd16630b51dc0eb0e497dfaaf69da21783_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98c5a7cd16630b51dc0eb0e497dfaaf69da21783_2_1380x694.jpeg 2x" data-dominant-color="6A6A6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a381aaa875c96b44a8e2615305cdc1c8b8409a86</span><span class="informations">1596×804 93.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @zhang_ming (2023-07-14 12:01 UTC)

<p>sorry too late to apply your answer, thank you</p>

---

## Post #5 by @mikbuch (2023-07-29 08:40 UTC)

<p>No problem, maybe my answer/question will help someone else who will be reading this post in the future.<br>
Btw. we managed to get the same SUV results in Slicer as from the GE Workstation. We also successfully implemented the functionality of calculating SUVs in an external Python script. If someone will need help that regard, feel free to contact me.</p>

---

## Post #6 by @akmal871026 (2025-02-09 07:41 UTC)

<p>In my experiences, you have to uninstall some extension about PET. I forgot what type I uninstall, then SUV will compute as usual.</p>

---
