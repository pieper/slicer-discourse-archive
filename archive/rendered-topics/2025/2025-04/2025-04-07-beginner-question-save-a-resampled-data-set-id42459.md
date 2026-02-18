# Beginner Question: Save a resampled data set

**Topic ID**: 42459
**Date**: 2025-04-07
**URL**: https://discourse.slicer.org/t/beginner-question-save-a-resampled-data-set/42459

---

## Post #1 by @Chamini (2025-04-07 01:05 UTC)

<p>Hi Everyone, I’m new to 3D slicer. I wanted to resample a scanned data set which is in png format. After resampling, when I tried to save the data set in my folder in png format, only the first slice is saved there. What has gone wrong there? I want to get the full data set. Here I attach how my data appear in the data tree and the settings I gave while saving.<br>
TIA.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5bcb89aa97e07c843babc2987e06488f5788efa.png" data-download-href="/uploads/short-url/nEb7aTsRpxEtKS2gcJkFh8scFC2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bcb89aa97e07c843babc2987e06488f5788efa_2_690x476.png" alt="image" data-base62-sha1="nEb7aTsRpxEtKS2gcJkFh8scFC2" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bcb89aa97e07c843babc2987e06488f5788efa_2_690x476.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bcb89aa97e07c843babc2987e06488f5788efa_2_1035x714.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5bcb89aa97e07c843babc2987e06488f5788efa_2_1380x952.png 2x" data-dominant-color="ABABAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1802×1244 370 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da6baf3b6d529313140a5d0a8ce7461aadd42af2.png" data-download-href="/uploads/short-url/vaeNH6wYJ4W3f66YqtlimXtWM0i.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6baf3b6d529313140a5d0a8ce7461aadd42af2_2_690x192.png" alt="image" data-base62-sha1="vaeNH6wYJ4W3f66YqtlimXtWM0i" width="690" height="192" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6baf3b6d529313140a5d0a8ce7461aadd42af2_2_690x192.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6baf3b6d529313140a5d0a8ce7461aadd42af2_2_1035x288.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6baf3b6d529313140a5d0a8ce7461aadd42af2_2_1380x384.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×630 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-04-07 11:26 UTC)

<p>If you really need it as a stack of PNGs you can use the Screen Capture module.</p>

---

## Post #3 by @muratmaga (2025-04-07 18:36 UTC)

<aside class="quote no-group" data-username="Chamini" data-post="1" data-topic="42459">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecb155/48.png" class="avatar"> Chamini:</div>
<blockquote>
<p>my folder in png format, o</p>
</blockquote>
</aside>
<p>Slicer does not save volume objects in 2D formats. Is there a reason you want your data in 2D format? If you want to do that Screen Capture is the only option but then you will loose the resolution information you had before since the screen capture is at the resolution of your screen, particularly given that you resampled your data.</p>
<p>Tell us what you want to do more?</p>

---

## Post #4 by @Chamini (2025-04-08 00:09 UTC)

<p>Hi, Thanks again. Later I tried with a python script and got it solved, but the images were in tif format. Anyway, I will try the screen capture module next time. Actually my requirement is, to resample the data to change the resolution. Then I’m going to evaluate the porosity of the volume, using CTAN.<br>
Thanks</p>

---

## Post #5 by @Chamini (2025-04-08 00:55 UTC)

<p>Thank you. I will try this.</p>

---

## Post #6 by @muratmaga (2025-04-08 01:39 UTC)

<p>If you are using the Bruker’s platform to this, you should probably use their tools for your convenience. Bruker hsa a tool called <code>Dataviewer</code> to allow you to reorient and resample your samples. It <strong>should</strong> preserve all the metadata…</p>

---

## Post #7 by @Chamini (2025-04-08 01:49 UTC)

<p>Yes, I work with Bruker’s platform and have used Dataviewer for orientation registration. However, I couldn’t locate any resolution adjustment options there. That’s why I’m looking into 3D Slicer specifically to modify resolution. My samples were originally scanned at different resolutions, and I need to standardize them to a single resolution for proper comparison. Thanks.</p>

---

## Post #8 by @muratmaga (2025-04-08 02:49 UTC)

<p>If you are trying to rescale (and reorient) your data a fixed resolution, then you should probably use automated registration, or a few landmarks (if the sample positions are too different for automated registration to work).</p>
<p>here is how you can do:</p>
<ol>
<li>Use the interaction widget to orient one sample to the position for all your samples to be.</li>
<li>Use the Crop Volume to resample to the resolution you want this to be in.</li>
<li>Use the automated image registration modules in Slicer (e.g., Brainsfit, or Elastix, or ANTs) to rigidly register every volume against this reference (including the original data of the reference).</li>
</ol>
<p>The outputs will be in the same orientation, and will have the exact image resolution as your reference.</p>
<p>It is possible that your scan orientations are too different for automated registration algorithms to do it for you. This is where landmarks come in. If you annotate 4 landmarks in every sample such that they mark top/bottom, right/left axis approximately, you can then use that transformation to initialize the automatic registration and will get very good results.</p>
<p>We are actually just finished prototyping an extension to do all of this in a very streamlined way. it is functional (as far as we tested) but it is not in the extension catalogue. If you are OK with some elbow grease I am happy to walk you through the process.</p>
<p><a href="https://github.com/SlicerMorph/SlicerANTsPy" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerANTsPy: module and GUI for antspy</a> is the extension.</p>

---

## Post #9 by @Chamini (2025-04-08 04:18 UTC)

<p>Many Thanks. I’ll try it out.</p>

---
