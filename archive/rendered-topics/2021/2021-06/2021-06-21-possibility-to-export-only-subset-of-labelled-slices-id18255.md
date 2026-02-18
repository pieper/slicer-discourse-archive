# Possibility to export only subset of labelled slices?

**Topic ID**: 18255
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/possibility-to-export-only-subset-of-labelled-slices/18255

---

## Post #1 by @mluerig (2021-06-21 15:54 UTC)

<p>I am trying to get started with biomedisa (<a href="https://biomedisa.org/" rel="noopener nofollow ugc">https://biomedisa.org/</a>), a deep learning based automatic segmentation tool which uses a subset of labels (e.g., only every 10th label from a stack of slices) to segment all remaining slices in between.</p>
<p>Using 3D slicers amazing segmentation editor, someone has already segmented a bunch of images. Now I would like to do some benchmarking with biomedisa, and for that I need to export only a subset of these labelled slices - i.e., only every 10th, to compare labelling expert performance with biomedisa performance.</p>
<p><strong>Question:</strong> When saving segmentation labels as tif, is it possible to only save every nth labelled slice instead of all labelled slices? The slices in between should just be black / zeros.</p>
<p>That’s a bit of special case, and I know I could do it in Python - I just figured I’d ask before I get busy.</p>

---

## Post #2 by @pieper (2021-06-21 16:18 UTC)

<p>biomedisa looks pretty cool - it looks like you should be able to get it to work, but yes, you will need a few lines of python, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">something like these examples</a> and then some <a href="https://numpy.org/doc/stable/reference/arrays.indexing.html#basic-slicing-and-indexing">numpy indexing</a>.  Follow up if you need more specifics.  Let us know how it goes!</p>

---

## Post #3 by @hherhold (2021-06-21 16:28 UTC)

<p>You can feed biomedisa an NRRD file. You just need to make a segmentation with labels, one segment per “thing” you want Biomedisa to segment out, and then your source volume data, which can also be an NRRD file.</p>
<p>I’ve been experimenting with a local installation of it (requires an NVIDIA card) and it’s promising.</p>

---

## Post #4 by @hherhold (2021-06-21 23:33 UTC)

<p>Sorry for short post earlier, in-between zoom calls.</p>
<p>So what I did to test it with an existing segmentation was to make new segments, paint individual slices in those segments, then move them to a new segmentation. The result is a segmentation the same dimensions as the original one, but each segment is single slices of a given organ/limb/etc. Save this as a regular .seg.nrrd, which is readable by Biomedisa.</p>
<p>You then send Biomedisa your volume as an NRRD file and your .seg.nrrd file that is your “labels”. Biomedisa returns an NRRD file where the values in the volume correspond to your labels. I’d convert that to a segmentation by importing the NRRD as a volume, make a new segmentation, and threshold by 1 to 1 for the first segment, 2 to 2 for the second, and so on. A little tedious but it would not be a ton of work to script this up in python to semi-automate it.</p>
<p>Getting Biomedisa running locally was quite doable, and you basically run it from the command line rather than set up a web interface and such.</p>
<p>Hope this helps.</p>
<p>-Hollister</p>

---

## Post #5 by @lassoan (2021-06-21 23:35 UTC)

<p>The renderings in biomedisa demo videos look amazing… but they are all manually colored and textured, several of them are rigged and animated. The models look so awesome because a very talented artistic 3D modeler spent tens (hundreds?) of hours with each model after segmentation.</p>
<p>It is also interesting to note that you might not need deep learning for interpolation. In <a href="https://www.nature.com/articles/s41467-020-19303-w">one of their papers</a> they show that you can get almost identical results with simple geometric interpolation. They could only find differences in extreme very few, special cases, in special circumstances.</p>
<p>Anyway, if it turns out that this slice interpolation tool is useful then it could be added to Slicer as a new Segment Editor effect. However, most likely developers will not invest time into this due to the restrictive (GPL-like copyleft license that essentially prevents commercial applications) and extreme hardware requirements.</p>
<p>Hopefully we’ll see more open and more diverse set of GPU-accelerated segmentation algorithms in Slicer via <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a>.</p>

---

## Post #6 by @hherhold (2021-06-21 23:42 UTC)

<p>All good points by <a class="mention" href="/u/lassoan">@lassoan</a>. The deep learning is only necessary (and beneficial) if you’re doing the same type of operation on many many similar scans.</p>
<p>As far as this type of interpolation, I think of it as a “smart fill-between-slices”, where it looks at the volume data in addition to geometric interpolation. This is likely an oversimplification - it’s been a little while since I read the paper.</p>
<p>I also don’t necessarily think that it’s necessary to do this (where “this” is the interpolation) on a GPU. It’s not taxing mine terribly heavily, and I’m not sure it’s really exploiting the parallelism that the paper says warrants a GPU. That being said, I have not delved deeply into the code, and I am not doing any machine learning on it - I’m only doing the Biomedisa interpolation. It is highly likely that the machine learning stuff exercises the GPU much more heavily.</p>
<p>At any rate, an “intelligent” fill between slices would be quite awesome, actually. My 2 cents.</p>

---

## Post #7 by @lassoan (2021-06-21 23:48 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="6" data-topic="18255">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>At any rate, an “intelligent” fill between slices would be quite awesome, actually. My 2 cents.</p>
</blockquote>
</aside>
<p>This kind of “intelligent” segmentation (that takes into account the underlying image content) is already available in Slicer as a post-processing step:</p>
<ul>
<li>shrink every segment by a small margin</li>
<li>apply Grow from seeds</li>
</ul>
<p>It reproduces fine details of the surface texture, hairs, etc. that a geometric interpolation would miss.</p>

---

## Post #8 by @hherhold (2021-06-21 23:51 UTC)

<p>Oh wow, I will have to try this.</p>
<p>I must admit I have not used grow from seeds hardly at all. My volumes tend to be large (usually &gt; 1GB) and when I first tried it, I was on a system with only 16GB memory. I’ve since upgraded and need to give it another try.</p>
<p>Thanks!!</p>

---

## Post #9 by @mluerig (2021-06-22 08:33 UTC)

<p>thanks for these interesting points - and good to know that geometric interpolation and smater interpolation is already available in 3D slicer. if I’ll have time I’ll include it in my benchmark.</p>
<p>the biomedisa approach is still useful because we have hundreds of images, of which a bunch are already labelled, so I am hoping to get going on the deep learning feature for many images (<a href="https://github.com/biomedisa/biomedisa#run-example" rel="noopener nofollow ugc">https://github.com/biomedisa/biomedisa#run-example</a>)</p>
<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="18255">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>So what I did to test it with an existing segmentation was to make new segments, paint individual slices in those segments, then move them to a new segmentation. The result is a segmentation the same dimensions as the original one, but each segment is single slices of a given organ/limb/etc. Save this as a regular .seg.nrrd, which is readable by Biomedisa.</p>
</blockquote>
</aside>
<p>but then you still have every consecutive slice labelled, no? to try biomedisa on single images I would want completely black slices between the labels. i.e., emulate the benchmark exercise in figure 3 of the corresponding publication (<a href="https://paperpile.com/shared/Hw0ehS" class="inline-onebox" rel="noopener nofollow ugc">1 shared paper | Paperpile</a>) and compare it to my manual measurements</p>
<p>I know it’s a no-brainer in Python, but I still wanted to ask whether 3Dslicer has a similar feature</p>

---

## Post #10 by @lassoan (2021-06-22 13:28 UTC)

<p>Yes, it is so trivial to do in Python (by copy-pasting a few line into Slicer’s Python console), that it is probably not worth clicking around in modules or writing a dedicated Python scripted module for this. If you have a label volume called <code>MRHead-label</code> in the scene:</p>
<pre><code class="lang-python">volumeNode = slicer.util.getNode('MRHead-label')
K=10

volumeArray=slicer.util.arrayFromVolume(volumeNode)
for slice in range(volumeArray.shape[0]):
  if slice % K:
    volumeArray[slice,:,:]=0

slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>
<p>You can easily automate iterating through all files in a folder, reading the volume, blanking out, and writing back.</p>
<p>Note that in Biomedisa they did not just randomly kept every 10th slice, but carefully choose which slices they segmented. In Slicer a good workflow can be:</p>
<ul>
<li>Segment slices that you think are important using Segment Editor.</li>
<li>Go to “Fill between slices” and click Initialize to do geometric interpolation (it is quick and there is no need for pre-training and no need for GPU).</li>
<li>Browse through the slices and see where segmentation was not accurate enough and if there is any slice that needs improvement then segment that slice. If your volume is not too big (or you just make slight changes) then you can keep auto-update of “Fill between slices” enabled to see segmentation update as you go; for larger, more complex volumes you would just cancel “Fill between slices” and then later initialize it again.</li>
<li>Finalize segmentation:
<ul>
<li>Option A: If result of geometric segmentation is sufficiently good, then just click “Apply” in “Fill between slices” effect.</li>
<li>Option B: Use image content to finalize segmentation in Slicer (by slightly eroding each segment and then use Grow from seeds effect).</li>
<li>Option C: Export the segmentation and use biomedisa to interpolate the segmentation, then load back results into Slicer for verification.</li>
</ul>
</li>
</ul>
<p>If the biomedisa interpolation turns out to be practically useful then you can write an NVidia Clara or MONAILabel interface (a simple REST API) to run biomedisa directly from Slicer (and all other compatible software, such as OHIF viewer or MITK).</p>

---

## Post #11 by @mluerig (2021-06-30 15:17 UTC)

<p>excellent! love the built-in python console…</p>

---
