# N4ITK MRI Bias correction

**Topic ID**: 1200
**Date**: 2017-10-09
**URL**: https://discourse.slicer.org/t/n4itk-mri-bias-correction/1200

---

## Post #1 by @annapbarnes (2017-10-09 14:06 UTC)

<p>Operating system: MacOSX Sierra<br>
Slicer version: 4.6.2 r25516<br>
Expected behavior: N4ITK bias correction output<br>
Actual behavior: nothing</p>
<p>Hi<br>
I’m a bit of a newbie to this GUI but I have used N3 bias correction before in linux and bash scripts etc.  so I know what I want to do and what output I want to get it from it but…</p>
<p>So I’ve loaded my data in to the 3D slicer viewer, I’ve selected N4ITK MRI Bias correction in drop down.</p>
<p>I would like to apply this to the image I have loaded in the GUI but it just says “output volume” as does the next 3 drop down menus.</p>
<p>What I was then expecting would be an output of the corrected image and the bias field.</p>
<p>Feeling a bit of “numpty” can someone send me a “dummies guide” on how to get this module to work in this rather snazzy GUI</p>
<p>thanks<br>
Anna</p>

---

## Post #2 by @pieper (2017-10-09 17:45 UTC)

<p>Hi Anna -</p>
<p>The panel should look something like below.</p>
<p>I just tested like this:</p>
<ul>
<li>download MRHead from the SampleData</li>
<li>go to the N4ITK MRI Bias Correction module</li>
<li>for the Output volumes, pick Create New from the menu</li>
<li>select MRHead as the input</li>
<li>click Apply</li>
</ul>
<p>(Note that in 4.6 there is a bug that resets the input volume after creating a new volume , which is why the input is selected last in the sequence above.  In the recent nightly builds this issue is fixed).</p>
<p>HTH,<br>
Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66fd14fe84a909cae9944f1e2c374caad8f82eb0.png" data-download-href="/uploads/short-url/eH4Vw2aojsXKCoPGyBoEnb7ePPG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66fd14fe84a909cae9944f1e2c374caad8f82eb0_2_496x500.png" alt="image" data-base62-sha1="eH4Vw2aojsXKCoPGyBoEnb7ePPG" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66fd14fe84a909cae9944f1e2c374caad8f82eb0_2_496x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66fd14fe84a909cae9944f1e2c374caad8f82eb0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66fd14fe84a909cae9944f1e2c374caad8f82eb0.png 2x" data-dominant-color="EBECEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">583×587 64.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
