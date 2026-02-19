---
topic_id: 15927
title: "How Would People Extract Center Line On A Hollow Model"
date: 2021-02-09
url: https://discourse.slicer.org/t/15927
---

# How would people extract center line on a hollow model?

**Topic ID**: 15927
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/how-would-people-extract-center-line-on-a-hollow-model/15927

---

## Post #1 by @Jezza (2021-02-09 23:16 UTC)

<p>Operating system: macOS Catalina 10.15.7<br>
Slicer version: 4.11 20200930</p>
<p>I need to 3D print a hollow model of the aorta and I need to extract the center lines to modify it before 3D printing.</p>
<p>Center line extraction only seems to work in solid models. The empty space inside my hollow model does not “count” as being part of my model, and thus the Extract Centerline tool will mess-up and put the center lines on the perimeter of my model.</p>
<p>How would experienced people solve this? I cannot “fill” my model and then use the “hollow” tool because my MRI images are too low resolution so the “hollow” tool does a very very bad job.</p>
<p>Is there a way for me to keep my hollow model and still apply center line extraction to it somehow?</p>

---

## Post #2 by @lassoan (2021-02-10 00:02 UTC)

<p>You would normally use the vessel wall (hollow) for 3D printing and visualization, and use the blood pool (solid) for quantitative analysis. If you want to do both then keep both segments. You can use “Logical operators” effect to clone contents of a segment (“Copy” operation).</p>

---

## Post #3 by @Jezza (2021-02-10 14:17 UTC)

<p>Thank you very much that was very helpful. I came across your advice on how to switch from vessel wall to blood pool:</p>
<ul>
<li>Logical operators effect, Invert operation =&gt; Apply</li>
<li>Islands effect, Keep largest island =&gt; Apply</li>
<li>Logical operators effect, Invert operation =&gt; Apply</li>
</ul>
<p>This method worked wonders the first time, but ever since then it has failed at all of my attempts and I cannot figure out why. It seems that now the “keep largest island” does not work anymore once I’ve inverted my vessel wall… This must mean that the big fat inversion block is somehow still connected to my inverted vessel wall (the new solid version of my model).</p>
<p>Do you have any idea as to why this might have happened? Why are they connected to each other after inversion? Would this have something to do with my ROI volume?? I’ve posted a transparent version of the inverted model in case this is helpful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/582a3ec5024f3d916318e517c7adc581abf8cdbf.jpeg" data-download-href="/uploads/short-url/czWwGYB8MnFGhzqdfFIehVf3QsL.jpeg?dl=1" title="Screenshot 2021-02-10 at 14.15.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/582a3ec5024f3d916318e517c7adc581abf8cdbf_2_690x285.jpeg" alt="Screenshot 2021-02-10 at 14.15.36" data-base62-sha1="czWwGYB8MnFGhzqdfFIehVf3QsL" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/582a3ec5024f3d916318e517c7adc581abf8cdbf_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/582a3ec5024f3d916318e517c7adc581abf8cdbf_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/582a3ec5024f3d916318e517c7adc581abf8cdbf_2_1380x570.jpeg 2x" data-dominant-color="969D9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-10 at 14.15.36</span><span class="informations">2876×1188 393 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Jezza (2021-02-11 00:23 UTC)

<p>This particular issue was solved. The inversion block has a rectangular shape which does not isotropically fit my model. Only one of the branches in my model reaches the height of this rectangle (the branches have different length). Thus some of my branches were trapped inside the inversion block and I had to manually use the erasor tool to create empty space above them so that they are <strong>not</strong> connected to the block and so that they <strong>can</strong> be removed using the “keep largest island” tool.</p>
<p>After that I applied the inversion tool again and voila, I obtained a solid (blood pool) version of my hollow model.</p>
<p>PS: Note that the empty space I created <strong>also</strong> became a part of the solid model after applying the 2nd inversion. I got rid of it by painting a new colour in its place (to use as a reference point) and erasing it after.</p>

---
