# SPHARM flip option

**Topic ID**: 16681
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/spharm-flip-option/16681

---

## Post #1 by @ikhsannk (2021-03-22 03:24 UTC)

<p>Hello Bea <a class="mention" href="/u/bpaniagua">@bpaniagua</a>  , Martin <a class="mention" href="/u/styner">@styner</a>  and everyone.</p>
<p>I have a simple question regarding SPHARM, is there a way to manually flip the output SPHARM file within SlicerSALT?</p>
<p>I am aware that there are ‘flip template’ and ‘manual flip option’ when we create the SPHARM file, but I haven’t found the answer to do such flipping after it has been created.</p>
<p>Below I attached the screenshot of my dentate nucleus SPHARM result. I actually prefer manual flipping if I can do that for these SPHARM files.</p>
<p>Many thanks in advance.<br>
Best, Ikhsan</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e8a38753f9bc2fc6985f2f5dff106d9ace6dd51.png" data-download-href="/uploads/short-url/bcNnueNGIgTirIhRk0XOgx6mGtj.png?dl=1" title="SPHARM_right_dentate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8a38753f9bc2fc6985f2f5dff106d9ace6dd51_2_690x356.png" alt="SPHARM_right_dentate" data-base62-sha1="bcNnueNGIgTirIhRk0XOgx6mGtj" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8a38753f9bc2fc6985f2f5dff106d9ace6dd51_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8a38753f9bc2fc6985f2f5dff106d9ace6dd51_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e8a38753f9bc2fc6985f2f5dff106d9ace6dd51_2_1380x712.png 2x" data-dominant-color="3C3440"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SPHARM_right_dentate</span><span class="informations">2553×1319 996 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Khalid_Saifullah (2022-07-16 22:11 UTC)

<p>Hi <a class="mention" href="/u/ikhsannk">@ikhsannk</a>,</p>
<p>Were you able to solve this issue finally? I am currently stuck with this problem actually!</p>
<p>Regards,<br>
Khalid</p>

---

## Post #3 by @styner (2022-08-22 16:05 UTC)

<p>Still catching up, sorry Ikhsan for not answering earlier.</p>
<p>In order to flip the data, you will have to use the ParaToSPHARMMesh module (this is usually the last module that is called by the SPHARM-PDM generator module) and apply it to individual objects.<br>
You have to use the manual flip option (called additional flipping in this module), and it uses number coding, same order as the generator module. Try out each option until it your object has the correct correspondence encoding.</p>
<p>Before you do that, look at the phi/theta coloring (see khalid’s earlier message) and check the correspondence, whether this is indeed a flip issue.</p>
<p>Martin</p>

---
