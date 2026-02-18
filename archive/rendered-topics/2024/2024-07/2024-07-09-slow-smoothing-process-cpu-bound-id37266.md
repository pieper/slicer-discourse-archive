# Slow smoothing process, CPU bound

**Topic ID**: 37266
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/slow-smoothing-process-cpu-bound/37266

---

## Post #1 by @Mark_Ryan (2024-07-09 01:44 UTC)

<p>Have a 46 slice chest CT  that I’ve upsampled to 196 slices using “crop volume” tool. Have performed segmentation on this using Totalsegmentator tool. Main issues are that the “apply to visible segments” checkbox in the smoothing tool doesn’t work when I click on apply, but does work if I uncheck the box and do each segment individually. Which takes a while but normally not a big deal.</p>
<p>Other issue I’m having is that the new model is more complex and smoothing each segment takes 30-45 seconds and looks like it’s running entirely through the CPU at 100% load. I’ve got to be doing this incorrectly somehow. The reason I upsampled was that the scan didn’t have enough slices and I was getting stairstepping even with the smoothing tool.</p>

---

## Post #2 by @muratmaga (2024-07-09 02:17 UTC)

<p>By going from 46 to 196 slices, you have quadrupled your data volume. So things will work out a bit slower. However, if you enable the new experimental smoothing options, I things will work out much faster.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51832e2159a14ae08736a09958563f71d892ad4a.png" data-download-href="/uploads/short-url/bD5J63eViQCptS1hLtzbRdmBX4e.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51832e2159a14ae08736a09958563f71d892ad4a_2_690x168.png" alt="image" data-base62-sha1="bD5J63eViQCptS1hLtzbRdmBX4e" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51832e2159a14ae08736a09958563f71d892ad4a_2_690x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51832e2159a14ae08736a09958563f71d892ad4a_2_1035x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51832e2159a14ae08736a09958563f71d892ad4a_2_1380x336.png 2x" data-dominant-color="C0C8DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1710×418 95.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
