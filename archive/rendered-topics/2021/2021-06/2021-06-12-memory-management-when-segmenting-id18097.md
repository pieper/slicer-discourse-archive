# Memory management when segmenting

**Topic ID**: 18097
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/memory-management-when-segmenting/18097

---

## Post #1 by @bcolbert (2021-06-12 23:36 UTC)

<p>I am a new user and not terribly technically proficient. I am segmenting a ~3.5gb data set and am am having issues. While just running in the background (not doing any segmenting) Slicer is using nearly 8gb of my 16gb RAM. When I just use the paint tool it immediately begins lagging severely (takes 15-30 seconds just to add a tiny bit) and  memory usage jumps to 100%. This seemed to start when I began the 7th segment. Previously I have done 2-3 segments and used the grow from seeds tool and had no issues.</p>
<p>I could use any advice. If it matters, I am trying to segment 15 structures and will eventually export them as models for geometric morphometric analysis.</p>

---

## Post #2 by @muratmaga (2021-06-14 07:28 UTC)

<p>The rule of thumb is 6-8X more memory than your dataset size to be available during segmentation. So if your dataset is 3.5GB, that corresponds to 20-30GB of RAM to be available (not just the physical RAM installed, which is also being used by other applications, your OS etc)… SO in that respect your computer doesn’t have sufficient memory, and probably using the virtual memory causing things too slow down</p>
<p>If you can’t install more RAM into your computer (and bring it up to about 32GB), you can try either of these approaches:</p>
<ol>
<li>If you have a large volume, but only segmenting out a small portion (for example a tooth in a skull), then use the CropVolume with an ROI so that your new volume is only that region (plus a small buffer). And then go ahead and segment the structure(s) using this new volume as the master volume. And keep doing this for every segment you need to generate.</li>
<li>If you do need to use the entire volume for your segmentation, then consider downsampling this volume to a lower resolution. Again, you can use the CropVolume for this purpose. A downsamping factor of 2 will create a reduction factor of 1/8, so instead of 3.5GB volume you will have something about 450MBs, which is you should be able to work without any problem. However, downsampling comes at the expense of detail, particularly for regions where you try to segment thin structures (e.g., orbital wall). So you have to experiment and see if this is acceptable to you.</li>
</ol>

---

## Post #3 by @rbumm (2021-06-14 20:34 UTC)

<p>Very good and helpful answer, thanks</p>

---
