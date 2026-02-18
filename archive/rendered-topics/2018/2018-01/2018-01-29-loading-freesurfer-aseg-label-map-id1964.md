# Loading FreeSurfer aseg label map

**Topic ID**: 1964
**Date**: 2018-01-29
**URL**: https://discourse.slicer.org/t/loading-freesurfer-aseg-label-map/1964

---

## Post #1 by @Vinny (2018-01-29 01:17 UTC)

<p>Hi,</p>
<p>I’ve been following Dr. Pujol’s tutorial on 3d visualization of FreeSurfer data.  I am using Slicer version 4.9.0 whereas the tutorial is based on Slicer version 3.4.  However, the names of the label do not appear in any of the views whereas they appear in the tutorial session when hovering the mouse over a specific delineated region; however, numbers associated with the labeled regions do appear in the Data Probe window.  Is there a way to access the label names?  Please note that I converted the aseg.mgz file into a label map in the Volumes module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3189d0e3d6397ff5d002c8cf5d2731042ea9e3d5.png" data-download-href="/uploads/short-url/74eFfScgWEystY57Gf8ugBBN3Q9.png?dl=1" title="SlicerApp-real_2018-01-28_20-06-57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3189d0e3d6397ff5d002c8cf5d2731042ea9e3d5_2_690x388.png" alt="SlicerApp-real_2018-01-28_20-06-57" data-base62-sha1="74eFfScgWEystY57Gf8ugBBN3Q9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3189d0e3d6397ff5d002c8cf5d2731042ea9e3d5_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3189d0e3d6397ff5d002c8cf5d2731042ea9e3d5_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3189d0e3d6397ff5d002c8cf5d2731042ea9e3d5_2_1380x776.png 2x" data-dominant-color="9D9FB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerApp-real_2018-01-28_20-06-57</span><span class="informations">1920×1080 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-01-29 15:35 UTC)

<p>You can see the label mapping in the Colors module (in Informatics category). Make sure you select the same color node (in your case GenericColors, but be careful because there is one called GenericAnatomyColors as well, which is different).</p>

---

## Post #3 by @Fernando (2018-01-29 16:22 UTC)

<p>Also try this:</p>
<ol>
<li>Go to Volumes module</li>
<li>Set the Active Volume to your label map</li>
<li>Open the Display button</li>
<li>Lookup Table -&gt; FreeSurferLabels</li>
</ol>

---

## Post #4 by @Vinny (2018-01-30 02:15 UTC)

<p>Great thanks!  Was able to get the label text from the LUT.</p>

---

## Post #5 by @MVallejoAzar (2023-08-03 16:59 UTC)

<p>Hi! In my Slicer not appears the FreeSurferLabels in the lookup Table, do you have any idea? Thanks</p>

---
