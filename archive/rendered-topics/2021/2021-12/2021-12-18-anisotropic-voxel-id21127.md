---
topic_id: 21127
title: "Anisotropic Voxel"
date: 2021-12-18
url: https://discourse.slicer.org/t/21127
---

# Anisotropic voxel

**Topic ID**: 21127
**Date**: 2021-12-18
**URL**: https://discourse.slicer.org/t/anisotropic-voxel/21127

---

## Post #1 by @Valentina_Nepi (2021-12-18 10:19 UTC)

<p>Hi everyone. I am studying a MRI dataset. All the images have the same spacing (0,80x0,46x0,46) cause everything is reported in FLAIR space. Also a given ground truth segmentation for lesions has this spacing condition. To analyze this segmentation features I’ve loaded Flair image as volume and this consensus as label map. Now I have two questions:</p>
<ol>
<li>
<p>this consensus can be considered anisotropic cause z is almost twice x and y? An import in segmentation module is required to have an isotropic voxel imposing the isotropic geometry flag for segmentation geometry (passing trough the “white cube” in segment editor)? My goal is to extract features, so this condition, in my opinion, is important. Any suggestions about this?</p>
</li>
<li>
<p>using islands effects splitting islands to segment and imposing minimum voxel size (for the initial consensus segmentation) all the generated segments are isotropic (1mm)? again: is necessary to impose space isotropy before applying this effect? I’ve tried both these two operations (with or without imposition) but in the subject hierarchy I always see the segmentation node with islands that seems containing only one segment… how can I resolve?</p>
</li>
</ol>
<p>Thanks everyone in advantage for a request.</p>

---

## Post #2 by @pieper (2021-12-18 17:08 UTC)

<p>In general isotropic voxels are not required for segmentation or radiomics.</p>
<p>I’m not really following the rest of your questions.  Perhaps some screenshots would help.</p>

---

## Post #3 by @Valentina_Nepi (2021-12-27 08:05 UTC)

<p>Thank you for the answer, Pieper!<br>
Yes, I’ll take some screen as soon as possible.</p>
<p>Meanwhile I’ve forgot a question. Since my voxel are isotropic only in plane xy, a force 2d setting in parameter file is required (setting it true) or not(leaving default false)?<br>
Thank you if you’ll answer me again.</p>
<p>Have a nice day</p>

---

## Post #4 by @pieper (2021-12-28 02:57 UTC)

<aside class="quote no-group" data-username="Valentina_Nepi" data-post="3" data-topic="21127">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/valentina_nepi/48/13474_2.png" class="avatar"> Valentina_Nepi:</div>
<blockquote>
<p>Since my voxel are isotropic only in plane xy, a force 2d setting in parameter file is required (setting it true) or not(leaving default false)?</p>
</blockquote>
</aside>
<p>You could use the force 2d option if your slices really have no relation to each other and should be treated independently.  Otherwise it’s okay to have anisotropic voxels, but you should look at the metrics to use and decide if they make sense when the data sampling is not uniform (meaning it doesn’t capture tissue variations the same way in all directions). <a class="mention" href="/u/joostjm">@JoostJM</a> or <a class="mention" href="/u/fedorov">@fedorov</a> may have further suggestions.</p>

---

## Post #5 by @Valentina_Nepi (2022-01-01 23:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f42f3f041f6bec7a19ce90f6f27d9f0ff8f35d.jpeg" data-download-href="/uploads/short-url/goVARKwSRGsHcpB1fn371hQyTE1.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72f42f3f041f6bec7a19ce90f6f27d9f0ff8f35d_2_559x500.jpeg" alt="1" data-base62-sha1="goVARKwSRGsHcpB1fn371hQyTE1" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72f42f3f041f6bec7a19ce90f6f27d9f0ff8f35d_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f42f3f041f6bec7a19ce90f6f27d9f0ff8f35d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72f42f3f041f6bec7a19ce90f6f27d9f0ff8f35d.jpeg 2x" data-dominant-color="3D3D3D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">637×569 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
after importing a labelmap I’ve used “effect: islands” to create and remove islands<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/038255d382c7c9336f2cc8454ca49d1136d20cc9.jpeg" alt="2" data-base62-sha1="v2FOs0UERVctRhflt4P5BXz689" width="644" height="468"><br>
going back to see segmentation property it seems that there is only one segment instead of 9 (created 2 seconds ago with segment editor).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a932d73ff8047ba35f485a88b7ebbe492639d37.jpeg" alt="3" data-base62-sha1="fcNWaTbd4I5KIMkhe9RiyIq4ZYX" width="638" height="442"><br>
could you tell me why? I don’t understand… thank you</p>

---

## Post #6 by @pieper (2022-01-03 13:27 UTC)

<aside class="quote no-group" data-username="Valentina_Nepi" data-post="5" data-topic="21127">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/valentina_nepi/48/13474_2.png" class="avatar"> Valentina_Nepi:</div>
<blockquote>
<p>one segment instead</p>
</blockquote>
</aside>
<p>In that image you have one Segmentation with several Segments (a Segmentation is a set of Segments).</p>

---

## Post #7 by @Valentina_Nepi (2022-01-03 13:44 UTC)

<p>“numbers of segment:1”, this let me confused</p>

---

## Post #8 by @JoostJM (2022-01-11 11:57 UTC)

<p>Texture features such as GLCM, GLRLM assume spacing isotropy. If this is not the case (as in the dataset), there are 4 options of dealing with this:</p>
<ul>
<li>Ignore the error: not advised, this introduces rotational dependency in your feature values</li>
<li>Use matrix weighting: this corrects the anisotropy by weighting the matrix as a function of the distance to the neighbor</li>
<li>Resample the dataset: ensures your voxels are isotropic. Be aware that heavy oversampling can introduce bias (though resampling in your dataset to .5 x .5 x .5 should be fine)</li>
<li>Use force2D: this ensures the out-of-plane angles are ignored and the isotropy assumption holds true (as voxels are isotropic in-plane).</li>
</ul>

---

## Post #9 by @Valentina_Nepi (2022-01-12 12:21 UTC)

<p>Thank you for these advices! They are precious!<br>
Can I resample directly in radiomics module or should I do this operation with resample volume module before feature extraction?</p>

---

## Post #10 by @JoostJM (2022-01-18 12:35 UTC)

<p>You can do so directly in the radiomics module. For this to work, enable it in the parameter file you pass to the module.</p>

---
