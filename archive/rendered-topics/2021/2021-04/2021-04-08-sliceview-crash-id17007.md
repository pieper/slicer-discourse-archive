# Sliceview crash?

**Topic ID**: 17007
**Date**: 2021-04-08
**URL**: https://discourse.slicer.org/t/sliceview-crash/17007

---

## Post #1 by @roozbehshams (2021-04-08 20:35 UTC)

<p>Hi,</p>
<p>In our setup we have a live EM-tracked US showing in the red sliceview (through PlusServer). There are times when this happens to the sliceview:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37d000d956713141761349c2c9b7502cd9483e7d.jpeg" data-download-href="/uploads/short-url/7XJUancfN7cBcKgTVr180ceILw1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37d000d956713141761349c2c9b7502cd9483e7d_2_690x368.jpeg" alt="image" data-base62-sha1="7XJUancfN7cBcKgTVr180ceILw1" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37d000d956713141761349c2c9b7502cd9483e7d_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37d000d956713141761349c2c9b7502cd9483e7d_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37d000d956713141761349c2c9b7502cd9483e7d_2_1380x736.jpeg 2x" data-dominant-color="AC756D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1411×753 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There is a corresponding error message in slicer’s log:<br>
[WARNING][Qt] 08.04.2021 10:36:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ctkSliderWidget::setSingleStep() 0.0745971 is out of bounds. 4.78081 4.85541 4.81811</p>
<p>The slicer version running here is 4.11.0-2020-02-12 but it happened in previous versions as well.</p>
<p>It’s been difficult to reliably reproduce it (it doesn’t happen that often), but it seems to happen when one of EM sensors stays out of the tracking field for a while.</p>
<p>Any ideas or suggestions on how to avoid it or deal with it?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2021-04-08 20:44 UTC)

<p>The first step towards addressing the issue will be to try and replicate the issue using latest Slicer stable and Slicer preview. See <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a></p>
<p>You state it fails like that using Slicer 4.11.0-2020-02-12 which is well over a year old now.</p>
<p>Try with the current Slicer stable (Slicer 4.11.20210226).</p>
<p>Then try using latest Slicer preview. Not sure if Plus is going to complain about mismatched VTK and ITK versions since I don’t think Plus has updated to VTK9 or ITK 5.2, but you can try.</p>
<p>Once you’ve tested with those versions, post your results here.</p>

---

## Post #3 by @roozbehshams (2021-04-08 21:31 UTC)

<p>That was indeed the plan. I asked to see if anyone here has had dealings with a similar issue while I work on reproducing it.</p>

---

## Post #4 by @jamesobutler (2021-04-08 22:13 UTC)

<p>I have not seen a slice view lose its view area like that as shown in your included image.</p>
<p>The setSingleStep logged message is just a warning and not an error. I’ve seen that one before with the slice view staying normal. It’s usually indicative of a single slice volume.</p>

---
