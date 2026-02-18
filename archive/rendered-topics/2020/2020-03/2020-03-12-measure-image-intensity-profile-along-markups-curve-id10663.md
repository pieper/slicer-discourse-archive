# Measure image intensity profile along markups curve

**Topic ID**: 10663
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/measure-image-intensity-profile-along-markups-curve/10663

---

## Post #1 by @kmalexander (2020-03-12 17:14 UTC)

<p>I’m looking to get a curved line profile from a volume, however it seems that the Line Profile tool does not work when using a MarkupsCurve input line - only the MarkupsLine works.  When a MarkupsCurve input line is selected, only the data between points 1 and 2 of the MarkupsCurve is plotted.  Any thoughts on how to get an entire curved line plotted?  Thanks!</p>

---

## Post #2 by @lassoan (2020-03-12 18:53 UTC)

<p>I’ve updated the LineProfile module now to be able to measure profile along a curve, too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1c3cfa548603f71e90e12e7d248fcaeea4492c8.jpeg" data-download-href="/uploads/short-url/pmA2d2r7OX6aEvF2xGLNNL8eYJ2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1c3cfa548603f71e90e12e7d248fcaeea4492c8_2_690x410.jpeg" alt="image" data-base62-sha1="pmA2d2r7OX6aEvF2xGLNNL8eYJ2" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1c3cfa548603f71e90e12e7d248fcaeea4492c8_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1c3cfa548603f71e90e12e7d248fcaeea4492c8_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1c3cfa548603f71e90e12e7d248fcaeea4492c8_2_1380x820.jpeg 2x" data-dominant-color="C3C4C6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1391×828 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can update your local LineProfile.py file with <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/LineProfile/LineProfile.py">this one</a> or wait for the next Slicer Preview Release (we are migrating our Slicer repository, so you may need to wait a few days).</p>

---

## Post #3 by @kmalexander (2020-03-12 19:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Awesome!  Thanks so much, Andras!</p>

---

## Post #4 by @Justus_Muller-Goebel (2023-07-12 16:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi there, is that tool still available on the most recent version?</p>

---

## Post #5 by @lassoan (2023-07-12 20:42 UTC)

<p>Yes, <code>Line Profile</code> module is still available, it is in the <code>Sandbox</code> extension.</p>

---

## Post #6 by @Justus_Muller-Goebel (2023-07-13 06:01 UTC)

<p>Amazing, thanks for the fast response. Is there, to your knowledge, any other add on for measuring a profile curve along a line with FWHM like mentioned in the paper:<br>
<a href="https://www.tandfonline.com/doi/epdf/10.1080/00016489.2020.1788225?needAccess=true&amp;role=button" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.tandfonline.com/doi/epdf/10.1080/00016489.2020.1788225?needAccess=true&amp;role=button</a></p>

---

## Post #7 by @lassoan (2023-07-20 22:22 UTC)

<p>I’ve added automatic peak detection and peak width measurement (FWHM by default) to the Line Profile module. It’ll be available in the extensions manager from tomorrow.</p>

---
