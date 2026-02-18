# Orientation Marker incorrect?

**Topic ID**: 14399
**Date**: 2020-11-03
**URL**: https://discourse.slicer.org/t/orientation-marker-incorrect/14399

---

## Post #1 by @Tommaso_Di_Noto (2020-11-03 08:59 UTC)

<p>Hi All!</p>
<p>I have a dataset of MR angiography patients. Through <code>sitk</code>, I checked with <code>GetDirections()</code> the direction of every volume.</p>
<p>It turns out they all have direction (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0), except one who has instead (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, <strong>-1.0</strong>).</p>
<p>So I investigated this outlier sub with Slicer and I noticed a potential bug in the Orientation (image below).</p>
<p>I have 2 questions:</p>
<ol>
<li>
<p>any idea of why only one sub has different Directions? Why could this be?</p>
</li>
<li>
<p>is it really a bug or am I missing something? The human in the coronal and sagittal planes doesn’t seem correctly oriented</p>
</li>
</ol>
<p>In case you want to try it out, you can find the nifti file at this GDrive [link]<br>
(<a href="https://drive.google.com/file/d/1VRDupP7VFHN1cLwFjzuU7t7ZnqSvL9PI/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1VRDupP7VFHN1cLwFjzuU7t7ZnqSvL9PI/view?usp=sharing</a>)</p>
<p>Thanks a lot in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d0b9b18891dff7456a18cb1f91bdb98b5d318a.jpeg" data-download-href="/uploads/short-url/zdqEhGHZjnq8VikeuF1176JKP3A.jpeg?dl=1" title="bug_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6d0b9b18891dff7456a18cb1f91bdb98b5d318a_2_690x430.jpeg" alt="bug_slicer" data-base62-sha1="zdqEhGHZjnq8VikeuF1176JKP3A" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6d0b9b18891dff7456a18cb1f91bdb98b5d318a_2_690x430.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6d0b9b18891dff7456a18cb1f91bdb98b5d318a_2_1035x645.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d0b9b18891dff7456a18cb1f91bdb98b5d318a.jpeg 2x" data-dominant-color="4C4D58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bug_slicer</span><span class="informations">1378×859 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @issakomi (2020-11-03 18:44 UTC)

<p>IMHO, Slicer is not guilty. Other programs show the same - wrong - orientation. Something went wrong with the file somwhere.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e931a07b57ad2be448e8b9936898b53ce60940.jpeg" data-download-href="/uploads/short-url/wF2tGtFoyJGOsiknC1fmJWOdWHS.jpeg?dl=1" title="20201103-193630" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e931a07b57ad2be448e8b9936898b53ce60940_2_333x375.jpeg" alt="20201103-193630" data-base62-sha1="wF2tGtFoyJGOsiknC1fmJWOdWHS" width="333" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e931a07b57ad2be448e8b9936898b53ce60940_2_333x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e931a07b57ad2be448e8b9936898b53ce60940.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e931a07b57ad2be448e8b9936898b53ce60940.jpeg 2x" data-dominant-color="85352F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20201103-193630</span><span class="informations">466×523 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ebf16e7f3dbfa4c7ca6acc2b43ea5b8b8e14716.jpeg" data-download-href="/uploads/short-url/i5fzfFvHpUOmdBGofIzlkc6z5fo.jpeg?dl=1" title="snap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ebf16e7f3dbfa4c7ca6acc2b43ea5b8b8e14716_2_420x375.jpeg" alt="snap" data-base62-sha1="i5fzfFvHpUOmdBGofIzlkc6z5fo" width="420" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ebf16e7f3dbfa4c7ca6acc2b43ea5b8b8e14716_2_420x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ebf16e7f3dbfa4c7ca6acc2b43ea5b8b8e14716_2_630x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ebf16e7f3dbfa4c7ca6acc2b43ea5b8b8e14716.jpeg 2x" data-dominant-color="1A1B1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">snap</span><span class="informations">719×640 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-11-03 20:17 UTC)

<p>Yes, image direction is specified incorrectly in this file.</p>
<p>(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,  <strong>-1.0</strong> ) would mean a left-handed coordinate system, which is not used in medical image computing, so most likely this is just a bug somewhere in the processing pipeline.</p>
<p>You can fix the file easily by inverting the third image axis direction:</p>
<pre><code class="lang-python">import numpy as np
volumeNode = getNodesByClass("vtkMRMLVolumeNode")[0]
volumeNode.ApplyTransformMatrix(vtkMatrixFromArray(np.diag([1,1,-1,1])))
</code></pre>

---
