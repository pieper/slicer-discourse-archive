---
topic_id: 22095
title: "Adc Histogram Of Segmented Brain Lesion"
date: 2022-02-21
url: https://discourse.slicer.org/t/22095
---

# ADC histogram of segmented brain lesion

**Topic ID**: 22095
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/adc-histogram-of-segmented-brain-lesion/22095

---

## Post #1 by @dszimatore (2022-02-21 20:44 UTC)

<p>Good evening! Could you suggest me the easiest way to calculate the ADC histogram of a segmented brain lesion? I am able to segment a lesion and have its volume but still I don’t find the way to have ADC values.<br>
Thanks</p>

---

## Post #2 by @pieper (2022-02-21 21:02 UTC)

<p>I believe you will need to do a little scripting for that.  Mask the ADC volume with the segmentation and then make a histogram like this:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>

---

## Post #3 by @dszimatore (2022-02-23 06:18 UTC)

<p>Is it necessary to do it with Python? or there is an easiest workflow?<br>
Is it possible to find some screenshots or a tutorial?<br>
thanks</p>

---

## Post #4 by @lassoan (2022-02-23 07:07 UTC)

<p>You can use the Mask Volume effect in Segment Editor to create a volume that only contain the voxels in the segmented region and you can see its histogram in Volumes module. but it will require about 10 clicks and all you get is a visual representation of the histogram.</p>
<p>Since in most cases you need to further process the histogram (e.g., compute a percentile) and might also want to analyze data in batch mode (instead of manually clicking through the GUI), it is usually more convenient to copy-paste a few lines of Python script into the Python console. You don’t need any Python scripting experience, just to be able to copy and paste code the code below into the Python console (hit Ctrl + 3 to show the console).</p>
<pre><code class="lang-python"># Get input data (use the first volume, segmentation, and segment that are found in the scene)
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)

# Get voxel values of the volume in the segmented region
import numpy as np
volumeArray = slicer.util.arrayFromVolume(volumeNode)
segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
segmentVoxels = volumeArray[segmentArray != 0]

# Compute and plot histogram
import numpy as np
histogram = np.histogram(segmentVoxels, bins=50)
slicer.util.plot(histogram, xColumnIndex = 1)
</code></pre>
<p><em>(adapted from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">this code snippet</a> in the script repository)</em></p>

---

## Post #5 by @dszimatore (2022-02-27 16:52 UTC)

<p>Thank you very muche for the answer. Unfortunatelly I find an error I can’t solve during the procedure, it’s like we give 3 arguments instead of 2?</p>
<blockquote>
<blockquote>
<blockquote>
<p>volumeNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLScalarVolumeNode”)</p>
<p>volumeNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLScalarVolumeNode”)</p>
<p>segmentationNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)<br>
import numpy as np<br>
volumeArray = slicer.util.arrayFromVolume(volumeNode)<br>
segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: arrayFromSegmentBinaryLabelmap() takes 2 positional arguments but 3 were given</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #6 by @KatS (2022-03-14 12:24 UTC)

<p>Hello,<br>
I’m running into a similar error when pasting the above mentioned code into the python interactor.<br>
What I would like to do is to obtain a histogram from a segmented area from a T2 relaxometry map. So I figured I could use the code in a comparable way. I use Slicer 4.11.0 on Windows 10 Pro.<br>
Any help with this is highly appreciated, unfortunately I’m not very strong in coding…<br>
Thank you a lot!<br>
Please find a screenshot from my scene with the error message attached.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63c465baafdad60f92187d74c28816f407ad599a.png" data-download-href="/uploads/short-url/eeA32qT2q1pGcyt5fA4xZiOu0AO.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63c465baafdad60f92187d74c28816f407ad599a_2_688x500.png" alt="grafik" data-base62-sha1="eeA32qT2q1pGcyt5fA4xZiOu0AO" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63c465baafdad60f92187d74c28816f407ad599a_2_688x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63c465baafdad60f92187d74c28816f407ad599a_2_1032x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/63c465baafdad60f92187d74c28816f407ad599a_2_1376x1000.png 2x" data-dominant-color="A8A4A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1780×1293 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2022-03-14 12:44 UTC)

<p>You need to use a recent Slicer Preview Release (Slicer-4.13).</p>

---

## Post #8 by @KatS (2022-03-14 15:09 UTC)

<p>Thanks a lot, it worked!</p>

---

## Post #9 by @dszimatore (2022-03-24 19:40 UTC)

<p>Thank you! now it works!<br>
Is it possible to download the entire dataset of the histogram to export them in excel?</p>
<p>Thanks a lot</p>

---

## Post #10 by @lassoan (2022-03-24 19:46 UTC)

<p>The histogram is already in a table that is saved as a <code>.csv</code> or <code>.tsv</code> file.</p>
<p>You can hit Ctrl-S to save all nodes, including the table. Or you can go to Data module and right-click on the table node and choose <code>Export to file...</code>.</p>

---

## Post #11 by @dszimatore (2022-03-25 12:17 UTC)

<p>Great! it works!<br>
thank you very much</p>

---

## Post #12 by @KatS (2023-04-03 15:17 UTC)

<p>Hello,</p>
<p>I have a further question related to histograms.<br>
In a current project, I am looking into qMRI parameters of tumor subregions, which I segmented in Segment Editor (one Segmentation-files contains several sub-segments created with the “add segment”-button). I am able to obtain a reasonable histogram using the code posted above, if there is only one segment. However, if I try the same with my current segmentation, I’m not able to get histograms for each sub-segment. This it how it looks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90bf8978426f4ea5a439ff7eacdc5dbd6652cdfb.jpeg" data-download-href="/uploads/short-url/kEv7ypF7MhfDqaEz8lyLZ84fjSj.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90bf8978426f4ea5a439ff7eacdc5dbd6652cdfb_2_690x195.jpeg" alt="grafik" data-base62-sha1="kEv7ypF7MhfDqaEz8lyLZ84fjSj" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90bf8978426f4ea5a439ff7eacdc5dbd6652cdfb_2_690x195.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90bf8978426f4ea5a439ff7eacdc5dbd6652cdfb_2_1035x292.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90bf8978426f4ea5a439ff7eacdc5dbd6652cdfb_2_1380x390.jpeg 2x" data-dominant-color="AEAEAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">2560×727 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried by making only one segment visible at a time, which didn’t work.</p>
<p>Is there a way to plot histograms for sub-segments or do I need to create separate segmentations for every sub-region I’m interested in?</p>
<p>Thanks a lot in advance!</p>

---

## Post #13 by @lassoan (2023-04-03 15:41 UTC)

<p><code>segmentId</code> variable selects the segment that you want to compute the histogram for. In the code snippet above, the first segment is used:</p>
<pre><code class="lang-python">segmentId = segmentationNode.GetSegmentation().GetNthSegmentID(0)
</code></pre>
<p>You can change <code>0</code> to <code>1</code>, <code>2</code>, … to select a different segment, or use <code>GetSegmentIdBySegmentName</code>:</p>
<pre><code class="lang-python">segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Some segment name")
</code></pre>

---

## Post #14 by @KatS (2023-04-06 11:06 UTC)

<p>Thanks a lot, it worked!</p>
<p>I’m sorry, but I have another question related to this topic. I was able to obtain histograms and .csv-files for all regions I was interested in. What I ultimately want to do is to compare frequency distributions of a given MRI parameter in histologically defined tumor subregions of five samples. I plotted a frequency distribution of all samples using the information from the individual csv-files. However, I think, this is not correct, because I realized that the mean/median derived from this “pooled” frequency distribution are different from mean/median derived from segmentation statistics (I used “Segment Statistics” for that). I believe that this may have something to do with binning of the individual histograms. Could that be the case? If so, would it be better to get the value for each voxel in each segment of all samples separately and then plot a frequency distribution with individual voxel values? Is there a way to export the values for each voxel in a segmented region?</p>

---

## Post #15 by @Man (2023-09-04 20:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22095">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>slicer.util.plot(histogram, xColumnIndex = 1)</code></p>
</blockquote>
</aside>
<p>Hi this is really helpful, Thank you so much. Please can you add a code for exporting the data of the histogram for the segment as text or csv files?</p>

---
