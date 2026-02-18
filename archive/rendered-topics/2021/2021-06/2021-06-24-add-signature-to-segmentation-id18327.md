# Add signature to segmentation

**Topic ID**: 18327
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/add-signature-to-segmentation/18327

---

## Post #1 by @ni5h (2021-06-24 10:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - an unrelated question and I am unsure if you can answer this (it may require our IT); once we have annotated and segmented an area, are we able to configure and add a medical signature on to the annotation with a time stamp before we export the files (we export into NIFTI format)?</p>

---

## Post #2 by @lassoan (2021-06-24 15:59 UTC)

<p>If you use nrrd format then you can assign arbitrary metadata to each segment. You could save some kind of signature there.</p>
<p>I would not recommend using nifti format for anything except for maybe storing brain images, because nifti is used widely by the brain imaging community. Nifti has many serious issues, including inability to add arbitrary metadata to the file (you need to use additional files, linked to the nifti file based on similar filename or other unreliable mechanisms).</p>

---

## Post #3 by @ni5h (2021-06-25 08:32 UTC)

<p>we use nifti as it is preferential for our binary analyses, though it is not a brain/neurological study we are completing.</p>
<p>Could you offer a link or method in how we would add a dicom tag/signature in 3d slicer? This is all experimental we just want to see if we can build upon our segmentations.</p>
<p>Thanks again!</p>

---

## Post #4 by @lassoan (2021-06-25 18:06 UTC)

<p>You can save the signature into custom key:value pairs in your segmentation using <a href="http://apidocs.slicer.org/master/classvtkSegment.html#a75d0c23fc90fc1252acd14278f64c386"><code>vtkSegment.SetTag</code></a>. For example:</p>
<pre><code class="lang-python">segmentation = getNode('Segmentation').GetSegmentation()
segment = segmentation.GetSegment(segmentation.GetSegmentIdBySegmentName('Segment_1'))
segment.SetTag("Signature", "abcd")
</code></pre>
<p>Of course, nifti cannot store such custom metadata, so you need to use seg.nrrd.</p>
<p>You can use <a href="https://github.com/lassoan/slicerio">slicerio</a> Python package (pip-installable in any Python environment) to get segmentation metadata from .seg.nrrd files.</p>

---

## Post #5 by @ni5h (2021-07-06 16:59 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>1/a. I am trying to complete this on one of our data sets but I am unsure how to write the vtk.segment.settag onto one of the nrrd exports, how is this completed within 3d slicer<br>
1/b. would I need to write this into the code for each segmentation or could we enable this for the whole data set?<br>
2. i have downloaded the preview release (4.13) and still cannot find mono ai label, do I have to wait for this to be released fully?</p>

---

## Post #6 by @lassoan (2021-07-09 04:44 UTC)

<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="18327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>I am trying to complete this on one of our data sets but I am unsure how to write the vtk.segment.settag onto one of the nrrd exports, how is this completed within 3d slicer</p>
</blockquote>
</aside>
<p>I gave a complete example above. If you encounter any errors then describe what you did exactly, what you expected to happen, and what happened instead (including any error message that is displayed).</p>
<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="18327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>would I need to write this into the code for each segmentation or could we enable this for the whole data set?</p>
</blockquote>
</aside>
<p>You can store custom metadata for each segment.</p>
<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="18327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>i have downloaded the preview release (4.13) and still cannot find mono ai label, do I have to wait for this to be released fully?</p>
</blockquote>
</aside>
<p>MONAILabel is already available. Check the Extensions Manager again and if you still cannot find it then tell us what exact Slicer version and operating system do you use.</p>

---

## Post #7 by @ni5h (2021-07-09 12:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="18327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>MONAILabel is already available. Check the Extensions Manager again and if you still cannot find it then tell us what exact Slicer version and operating system do you use.</p>
</blockquote>
</aside>
<p>i am using the latest version 4.11.20210226 I believe, I have also installed the preview release also, 4.13 and cannot find this here either. Windows.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="18327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I gave a complete example above. If you encounter any errors then describe what you did exactly, what you expected to happen, and what happened instead (including any error message that is displayed).</p>
</blockquote>
</aside>
<p>We (for the time being) do not require the signature, so I can put this to the side for the time being. I was initially unsure where to input the code, if it was the python interactor or a higher skillset was required to input this, something I do not possess. Thanks for your help!</p>

---

## Post #8 by @lassoan (2021-07-14 03:43 UTC)

<p>MONAILabel is available for recent Slicer Preview Releases. If you are in Europe then some extension will only appear in the afternoon. So, after downloading and installing the latest Slicer Preview Release, wait until at least the evening before you install the extension. You can also download and install Slicer Preview Release from the day before using <a href="https://download.slicer.org/?offset=-1">this</a> link and for that all the extensions should be available immediately.</p>

---

## Post #9 by @ni5h (2021-07-15 15:54 UTC)

<p>hi, I have downloaded this, is there a help/how-to guide into using it? I cannot find anything on youtube to perform an annotation…</p>

---

## Post #10 by @lassoan (2021-07-15 15:56 UTC)

<p>Everything is explained in detail on the extension’s website: <a href="https://github.com/Project-MONAI/MONAILabel" class="inline-onebox">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>

---
