# [qSlicerScalarVolumeDisplayWidget] Adding user-defined histogram to this

**Topic ID**: 21448
**Date**: 2022-01-13
**URL**: https://discourse.slicer.org/t/qslicerscalarvolumedisplaywidget-adding-user-defined-histogram-to-this/21448

---

## Post #1 by @strider_hunter (2022-01-13 16:29 UTC)

<p>Hi,<br>
I wish to add a <strong>user-defined histogram</strong> in ScalarVolumeDisplayWidget. Is it possible to do so? I have seen solutions that display histograms using slicer.util.plot(), but I have a very specific user-defined layout that I do not wish to disturb.</p>
<p>The reason why I need a custom histogram, is that I am unable to interpret the widgets default histogram. The images below might help illustrate my issue.</p>
<p>This is a histogram made using slicer.util.plot() for a particular volume<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/766dd1741b56b22fb1997591ad8173b44d9aad09.png" alt="image" data-base62-sha1="gTFCNRiLLBQpJdA9R5QoaLoH84F" width="499" height="270"></p>
<p>But the histogram in the ScalarVolumeDisplayWidget looks like this. I am unable to interpret this.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3229d1fe99c8377ccca9dcbffef16d76aa05afea.png" alt="image" data-base62-sha1="79LtkwVvq5OHT8vIyud0c88FuxY" width="663" height="211"></p>
<p>For e.g, another volumes histogram plot that does offer insight into its properties is this:-<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c525775feb3b9b19b2461527315572679f1d5ad6.jpeg" data-download-href="/uploads/short-url/s82kDyF4lbHqwEANRyTbIoKNRBQ.jpeg?dl=1" title="MicrosoftTeams-image (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c525775feb3b9b19b2461527315572679f1d5ad6_2_690x280.jpeg" alt="MicrosoftTeams-image (1)" data-base62-sha1="s82kDyF4lbHqwEANRyTbIoKNRBQ" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c525775feb3b9b19b2461527315572679f1d5ad6_2_690x280.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c525775feb3b9b19b2461527315572679f1d5ad6_2_1035x420.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c525775feb3b9b19b2461527315572679f1d5ad6_2_1380x560.jpeg 2x" data-dominant-color="898988"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MicrosoftTeams-image (1)</span><span class="informations">1680×684 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The grey’ish parts in the widget histogram can be seen in the slicer.util.plot() histogram.</p>

---
