---
topic_id: 9912
title: "Loaded Files But With Blank Browser"
date: 2020-01-23
url: https://discourse.slicer.org/t/9912
---

# Loaded Files but with blank browser

**Topic ID**: 9912
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/loaded-files-but-with-blank-browser/9912

---

## Post #1 by @ravi_nataraj (2020-01-23 00:25 UTC)

<p>Hey fellow slicers,</p>
<p>I’m pretty new at 3D slicer but I can’t seem to figure something out. I’m able to manipulate and play with the preloaded data that software offers when downloaded but I can’t seem see the files that I’ve uploaded. Whenever I try uploading a DICOM directory, everything will work properly but nothing will show in the browser. What’s even weirder is that when select the show zoomed slice option on the data probe option on left pulldown menu, I can see the image bright and clear. How can I get it to show on my main browser? Is there something wrong with my slicer app?</p>
<p>Thanks, <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0708e4dacd16c3dbe7f61e48a775a8e3a7b40948.png" data-download-href="/uploads/short-url/10eoE4HYfmkluTuSCeqln1mYBkY.png?dl=1" title="3d Slicer Problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0708e4dacd16c3dbe7f61e48a775a8e3a7b40948_2_690x361.png" alt="3d Slicer Problem" data-base62-sha1="10eoE4HYfmkluTuSCeqln1mYBkY" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0708e4dacd16c3dbe7f61e48a775a8e3a7b40948_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0708e4dacd16c3dbe7f61e48a775a8e3a7b40948_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0708e4dacd16c3dbe7f61e48a775a8e3a7b40948_2_1380x722.png 2x" data-dominant-color="585858"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d Slicer Problem</span><span class="informations">1920×1005 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-01-23 00:27 UTC)

<p>It seems like that the default brightness/contrast value is not optimal (maybe there is an outlier voxel value). Could you please try the latest Slicer Preview release? If you have problem with that, too, then check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM FAQ page</a>.</p>

---
