---
topic_id: 22665
title: "Fiducial Markers Hidden When Cropping Roi Disabled And Shown"
date: 2022-03-24
url: https://discourse.slicer.org/t/22665
---

# Fiducial markers hidden when cropping ROI disabled, and shown when cropping ROI enabled

**Topic ID**: 22665
**Date**: 2022-03-24
**URL**: https://discourse.slicer.org/t/fiducial-markers-hidden-when-cropping-roi-disabled-and-shown-when-cropping-roi-enabled/22665

---

## Post #1 by @DIV (2022-03-24 05:13 UTC)

<p>I created a fiducial maker that was located just outside a cropping ROI.</p>
<ul>
<li>When cropping ROI is enabled and displayed, the external fiducial marker isn’t shown (<em>this is logical</em>).</li>
<li>When cropping ROI is enabled but not displayed, the external fiducial marker is shown (<em>this is <strong>not</strong> logical</em>).</li>
<li>When cropping ROI is not enabled and not displayed, the external fiducial marker is shown (<em>this is logical</em>).</li>
<li>When cropping ROI is not enabled but is displayed, the external fiducial marker isn’t shown (<em>this is <strong>not</strong> logical</em>).</li>
</ul>
<p>This occurs in version 4.13.0-2022-01-19 of Slicer.<br>
Display of the 3D volume is tied to enabling of the cropping ROI, not display of the cropping ROI (<em>that is logical</em>).</p>
<p>—DIV</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb8b719135e2467f50b6e58058b5bbc5727fa334.png" data-download-href="/uploads/short-url/t2DGlLU1a1NKHHasIH8Uqnnp5Zi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb8b719135e2467f50b6e58058b5bbc5727fa334_2_690x367.png" alt="image" data-base62-sha1="t2DGlLU1a1NKHHasIH8Uqnnp5Zi" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb8b719135e2467f50b6e58058b5bbc5727fa334_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb8b719135e2467f50b6e58058b5bbc5727fa334_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb8b719135e2467f50b6e58058b5bbc5727fa334.png 2x" data-dominant-color="C0C2E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/759c251945c71a15684491392c019a67484f944c.png" data-download-href="/uploads/short-url/gMqoZ4o5Rz7Z3xe8Vx2kaeXrREM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/759c251945c71a15684491392c019a67484f944c_2_690x367.png" alt="image" data-base62-sha1="gMqoZ4o5Rz7Z3xe8Vx2kaeXrREM" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/759c251945c71a15684491392c019a67484f944c_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/759c251945c71a15684491392c019a67484f944c_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/759c251945c71a15684491392c019a67484f944c.png 2x" data-dominant-color="C1C3E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68d08ca841ce4af0828f795709d5ae46f5c83e17.png" data-download-href="/uploads/short-url/eXetgxRvdjbEOYkNY7l9Cre4d6f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d08ca841ce4af0828f795709d5ae46f5c83e17_2_690x367.png" alt="image" data-base62-sha1="eXetgxRvdjbEOYkNY7l9Cre4d6f" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d08ca841ce4af0828f795709d5ae46f5c83e17_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68d08ca841ce4af0828f795709d5ae46f5c83e17_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68d08ca841ce4af0828f795709d5ae46f5c83e17.png 2x" data-dominant-color="C0C2E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd00b1eb09575dcb7c88bad546a218ce884a792b.png" data-download-href="/uploads/short-url/qXZJjH0N8GfgOJNAUEHMJ5Cb3uP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd00b1eb09575dcb7c88bad546a218ce884a792b_2_690x367.png" alt="image" data-base62-sha1="qXZJjH0N8GfgOJNAUEHMJ5Cb3uP" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd00b1eb09575dcb7c88bad546a218ce884a792b_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd00b1eb09575dcb7c88bad546a218ce884a792b_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd00b1eb09575dcb7c88bad546a218ce884a792b.png 2x" data-dominant-color="C1C3E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @DIV (2022-03-24 05:19 UTC)

<p>Sorry, I have mischaracterised the problem.<br>
It is not due to external location of the marker.  When the marker is far outside, it can be seen always.<br>
Rather, it seems to be due to unfortunate conflict between the marker and the light-grey handles at the corners of the cropping ROI, or (similarly) the coloured handles in the centre of the faces of the cropping ROI.<br>
So, it’s still unexpected/undesirable behaviour, although the actual behaviour/mechanism is different to how I initially interpreted it.<br>
—DIV</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81fa48f774c4971ae5128de02c11adf295108664.png" data-download-href="/uploads/short-url/ixPPgxk25v9E5qOP5ONvcLoDZHu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81fa48f774c4971ae5128de02c11adf295108664_2_690x367.png" alt="image" data-base62-sha1="ixPPgxk25v9E5qOP5ONvcLoDZHu" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81fa48f774c4971ae5128de02c11adf295108664_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81fa48f774c4971ae5128de02c11adf295108664_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81fa48f774c4971ae5128de02c11adf295108664.png 2x" data-dominant-color="C0C2E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2022-03-24 13:03 UTC)

<p>Markups control point labels are only displayed for visible points. Visibility is determined only for the centerpoint position, not for the entire point glyph, therefore, as you noted, a line can occlude a point. It would be computationally too expensive to check visibility of all (or many) points of a glyph, so it is not likely that we will change this behavior.</p>
<p>If you must always see the labels then you can enable <code>Occluded visibility</code> (in Markups module → Display → Advanced → 3D display section).</p>

---

## Post #4 by @DIV (2022-03-24 13:20 UTC)

<p>Thanks.  Actually, I didn’t notice the ROI box line occluding the markups, only the ‘handles’ on the ROI box.</p>
<p>As you guessed, retaining the label would be sufficient to avoid the main cause of confusion for me.</p>

---
