# Slicer SALT attribute to measure bone resorption

**Topic ID**: 33699
**Date**: 2024-01-09
**URL**: https://discourse.slicer.org/t/slicer-salt-attribute-to-measure-bone-resorption/33699

---

## Post #1 by @anasmh101 (2024-01-09 17:21 UTC)

<p>Hello everyone, may I ask which attribute in Shape population viewer represents  bone resorption/deposition in mandible condyle for (pre/post treatment condyle ), I have done model to model distance ( corresponding point to point) analysis to measure bone resorption/deposition between pre / post operative condyles, is this correct method to achieve this purpose?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdfd6e72730a167c025a8d4951287aff2c9e0679.png" data-download-href="/uploads/short-url/AeTM0FdkhBlcSTF3gfU9DLNqy9z.png?dl=1" title="attribute" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdfd6e72730a167c025a8d4951287aff2c9e0679.png" alt="attribute" data-base62-sha1="AeTM0FdkhBlcSTF3gfU9DLNqy9z" width="690" height="275" data-dominant-color="DCE3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">attribute</span><span class="informations">806×322 20.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @SAO (2024-04-21 14:55 UTC)

<p>Hello,</p>
<p>Since the correspondence has already been established between the two mean models [i.e. source model (the post-operative Model) &amp; target model (the pre-operative model)], you can then use “singed point-to-point distance” to visualize and quantify the resorption (-) and deposition (+) between the mean models for pre / post operative condyles.</p>
<p>Regards,<br>
Sultan</p>

---

## Post #3 by @lili-yu22 (2024-04-22 05:22 UTC)

<p>hi，after choose the signedpointtopointDistance ，there is no true value ，because when i set the range，the value chang。thank you for your reply</p>

---

## Post #4 by @anasmh101 (2024-04-22 14:19 UTC)

<p>thank you for your reply</p>

---

## Post #5 by @SAO (2024-04-25 08:55 UTC)

<p>Hi,</p>
<p>Yes; the value has changed because you switched to, and chose, different variable within the ‘population viewer’ module. The value will also change when ever you modify range as well.</p>
<p>In general:</p>
<ul>
<li>
<p>For  quantifying the amount of deviation between the two models, you need to run the “Model to Model Distance” module in [SlicerSALT or 3D slicer].</p>
</li>
<li>
<p>Since you have already establish correspondence between the mean models for, you need to chose “corresponding point-to-point distance” in the module. This will allow you to quantify the amount of deviation between each corresponding points between the two models.</p>
</li>
<li>
<p>After running the module successfully, you will obtain a ‘vtk file’ that has all value you need for creating the color map (using population viewer module) and quantifying the deviation with specific values for each corresponding (which will be shown to you clearly in spread sheet when using Paraview software).</p>
</li>
</ul>
<p>Regards,<br>
Sultan</p>

---

## Post #6 by @lili-yu22 (2024-04-29 02:41 UTC)

<p>thank you very much for your reply</p>

---
