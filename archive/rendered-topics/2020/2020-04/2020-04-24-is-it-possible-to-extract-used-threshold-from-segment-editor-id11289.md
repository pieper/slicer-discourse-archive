# Is it possible to extract used threshold from segment editor?

**Topic ID**: 11289
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/is-it-possible-to-extract-used-threshold-from-segment-editor/11289

---

## Post #1 by @ASR225 (2020-04-24 13:05 UTC)

<p>Hi,</p>
<p>I have a simple question. I could not find the answer that’s why I made a new topic.<br>
So I use 3d Slicer to calculate volumes with segment editor. first, I create a new segment and  I use a threshold to select the parts I’m interested in, I cut away the rest of the image with the scissors tool. If that’s finished I use the segment statistics to calculate the volume and save the data.</p>
<p>After saving I get the following files:<br>
1 scene.mrml<br>
2  scene.png<br>
3. unamed series.nrrd<br>
4. segmentation.seg.nrrd<br>
5. table.schema.tsv<br>
6. table.tsv</p>
<p>During the procedure, I use a threshold to select the parts of interest. Is It possible to find out what threshold was used?<br>
I opened the files in notepad and tried to find the threshold value but I didn’t found it. I Also reloaded the data and went back to segment editor en clicked on the threshold but on all the data i reloaded it’s giving a threshold of ± 1400. And I know for sure that’s not correct.</p>
<p>Could someone please let me know if it is possible to find this value.</p>
<p>Thanks in advance!</p>
<p>Kind regards,</p>
<p>ASR225</p>

---
