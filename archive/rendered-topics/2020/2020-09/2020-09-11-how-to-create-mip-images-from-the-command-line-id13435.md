---
topic_id: 13435
title: "How To Create Mip Images From The Command Line"
date: 2020-09-11
url: https://discourse.slicer.org/t/13435
---

# How to create MIP images from the command line?

**Topic ID**: 13435
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/how-to-create-mip-images-from-the-command-line/13435

---

## Post #1 by @shahrokh (2020-09-11 08:22 UTC)

<p>Hello Dear Developers and Users</p>
<p>Can the <strong>MIP viewer</strong> module be run from the command line?<br>
In other words, how can I generate axial MIP images from <em>the command line</em> by setting <strong>Slice Size MIP</strong> in any way possible?</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-09-11 13:37 UTC)

<p>Hello <a class="mention" href="/u/shahrokh">@shahrokh</a></p>
<p>One option is to write a python script to generate the MIP and write out the resliced image output to a file.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections</a></p>
<p>You can then run your python script using --python-script command line option in  Slicer.</p>
<p>-Andinet</p>

---

## Post #3 by @shahrokh (2020-09-13 12:58 UTC)

<p>Hello Andinet</p>
<p>Thank you very much for your guidance. I have some questions about the concept of <strong>MIP</strong> that I hope you will guide me, perhaps I should not ask my question in here.</p>
<p>Thanks a lot for your help. To create the MIP images, I used the Python code provided on github:<br>
Title: GitHub - ljpadam/maximum_intensity_projection: Maximum intensity projection for medical image<br>
Address: <a href="https://github.com/ljpadam/maximum_intensity_projection" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ljpadam/maximum_intensity_projection: Maximum intensity projection for medical image</a></p>
<p>I think that the <strong>slices_num</strong> parameter in the <em>maximum_intensity_projection.py</em> code (in the above link) is similar to the <strong>Slice size MIP</strong>  in the module of <strong>MIP Viewer</strong>. Is it true?</p>
<p>As you can see in the following image, if I increase <strong>slices_num</strong> in the code of <em>maximum_intensity_projection.py</em> or <strong>Slice Size MIP</strong> in 3DSlicer, more arteries will be projected in the axial slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94213b37a164b0d2740496aa1a712334eba5d483.png" data-download-href="/uploads/short-url/l8pRwTsljoy7valbQJofLaoHw7F.png?dl=1" title="new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94213b37a164b0d2740496aa1a712334eba5d483_2_690x388.png" alt="new" data-base62-sha1="l8pRwTsljoy7valbQJofLaoHw7F" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94213b37a164b0d2740496aa1a712334eba5d483_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94213b37a164b0d2740496aa1a712334eba5d483_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94213b37a164b0d2740496aa1a712334eba5d483_2_1380x776.png 2x" data-dominant-color="A09E9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new</span><span class="informations">1920×1080 448 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This destroys the vascular view in the coronal slice as you can see in the following image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5b6bb38270f6b2b55227f4b1e6ca63e0c2994a2.png" data-download-href="/uploads/short-url/pVvVaYDFAAXPbwh8NRxXOpMp0PM.png?dl=1" title="new2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b6bb38270f6b2b55227f4b1e6ca63e0c2994a2_2_690x388.png" alt="new2" data-base62-sha1="pVvVaYDFAAXPbwh8NRxXOpMp0PM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b6bb38270f6b2b55227f4b1e6ca63e0c2994a2_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b6bb38270f6b2b55227f4b1e6ca63e0c2994a2_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b6bb38270f6b2b55227f4b1e6ca63e0c2994a2_2_1380x776.png 2x" data-dominant-color="A19F9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new2</span><span class="informations">1920×1080 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this situation unavoidable in a MIP view?</p>
<p>How can I have good quality of MIPs in the three directions (AP, IS and LR)?</p>
<p>Please guide me.<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #4 by @lassoan (2020-09-13 13:44 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="3" data-topic="13435">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>To create the MIP images, I used the Python code provided on github:<br>
Title: GitHub - ljpadam/maximum_intensity_projection: Maximum intensity projection for medical image<br>
Address: <a href="https://github.com/ljpadam/maximum_intensity_projection" class="inline-onebox">GitHub - ljpadam/maximum_intensity_projection: Maximum intensity projection for medical image</a></p>
</blockquote>
</aside>
<p>This code, as is, does not make a lot of sense, as it does thick slice reformat for every slice of a volume. However, you could easily change it to compute the maximum intensity for all slices and along any of the 3 images axes.</p>
<p>If you need arbitrarily oriented views then I would recommend to use the script that <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> linked above. If you need perspective projection (to simulate fluoroscopy images) or you need fast MIP generation (50-100 images per second) and 8 bit precision is enough then you can use the volume renderer.</p>

---
