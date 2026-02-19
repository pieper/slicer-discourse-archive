---
topic_id: 38048
title: "I Need Help Please If Anyone Know Can You Please Help Me"
date: 2024-08-27
url: https://discourse.slicer.org/t/38048
---

# I need help please if anyone know, can you please help me

**Topic ID**: 38048
**Date**: 2024-08-27
**URL**: https://discourse.slicer.org/t/i-need-help-please-if-anyone-know-can-you-please-help-me/38048

---

## Post #1 by @Vikram (2024-08-27 03:19 UTC)

<p>Hi i have 3D stl file of cubic , in stl file there is two density one is air and other is solid part , i want to calculate the volume of solid part and air , but the file is in stl format , can anyone please help me first how to segment both solid and air from cubic<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/627b590abadabd3118f541a8f0e6697cb941eeda.png" data-download-href="/uploads/short-url/e3d3Wr9Mas0MnnZK5oy1q2powEq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/627b590abadabd3118f541a8f0e6697cb941eeda.png" alt="image" data-base62-sha1="e3d3Wr9Mas0MnnZK5oy1q2powEq" width="620" height="500" data-dominant-color="9EA3B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×517 2.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-08-27 03:39 UTC)

<p>Hi,</p>
<p>You asked this a few times and I think we tried to help as much as we can with the information provided. It is still the same workflow</p>
<p>You can import this STL as a segmentation. Then you can use the threshold tool to assign the lattice (solid) voxels into Segment_1, then you can assign the remaining (air) voxels to Segment_2. Please see the relevant sections of Segmentation tutorial on how to achieve these tasks:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>
<p>Then you you can use the Segment Statistics module to calculate volumes of them.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>
<p>However, for that to be correct your STL should correct physical sizes. For example if you know the length of the lattice, measure it in 3D slicer and compare it to known size to assess whether the STL is providing you the correct physical dimensions.</p>

---

## Post #3 by @Vikram (2024-08-27 03:48 UTC)

<p>Sorry from my side<br>
But now I work on stl file<br>
Before it was Dicom file , i used these step on Dicom file , it was success.<br>
But now I use these steps on stl file but it is not working<br>
Thank you <img src="https://emoji.discourse-cdn.com/twitter/heart.png?v=12" title=":heart:" class="emoji" alt=":heart:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Vikram (2024-08-27 03:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba274ec5704960af0c6b65ad47d1a5f048f8d514.png" data-download-href="/uploads/short-url/qyN1BpOCgfajWToYesfiYvjabNa.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba274ec5704960af0c6b65ad47d1a5f048f8d514_2_472x198.png" data-base62-sha1="qyN1BpOCgfajWToYesfiYvjabNa" alt="image.png" width="472" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba274ec5704960af0c6b65ad47d1a5f048f8d514_2_472x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba274ec5704960af0c6b65ad47d1a5f048f8d514_2_708x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba274ec5704960af0c6b65ad47d1a5f048f8d514_2_944x396.png 2x" data-dominant-color="939294"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1902×799 69.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when i upload stl file, stl file also show in output box , and tool for segment editor we can’t use</p>

---

## Post #5 by @muratmaga (2024-08-27 03:53 UTC)

<p>I gave you</p>
<aside class="quote no-group" data-username="Vikram" data-post="3" data-topic="38048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/e47774/48.png" class="avatar"> Vikram:</div>
<blockquote>
<p>But now I use these steps on stl file but it is not working</p>
</blockquote>
</aside>
<p>The proper way of doing this is with DICOMs, and once you convert your stl it is the same set of instructions for segmentation. but it is of course your call whichever way you want to do this.</p>
<p>Anyways, if you follow my instructions above carefully, you should be able to do what you want to do.</p>

---

## Post #6 by @Vikram (2024-08-27 10:24 UTC)

<p>I tried, but it only calculates the volume of the wall( solid) not air (hole) from the stl file.<br>
Maybe I did not understand.<br>
someone simply explain to me</p>

---
