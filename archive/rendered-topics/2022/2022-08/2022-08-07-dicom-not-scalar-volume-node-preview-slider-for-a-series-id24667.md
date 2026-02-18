# Dicom (not-scalar-volume-node) preview slider for a Series

**Topic ID**: 24667
**Date**: 2022-08-07
**URL**: https://discourse.slicer.org/t/dicom-not-scalar-volume-node-preview-slider-for-a-series/24667

---

## Post #1 by @mau_igna_06 (2022-08-07 09:30 UTC)

<p>Hi. I would like to know if there exists some kind of preview-widget (opensource) you know for Slicer that achieves the following:</p>
<ul>
<li>Has a pixmap where the preview current dicom image of the Series is loaded</li>
<li>Has a slider to move through the series in a way that the offset of the slices goes on positive direction and allows to preview all dicom images of Series using all the slider range</li>
</ul>
<p>Dear <a class="mention" href="/u/pieper">@pieper</a> have you worked on anything similar that you could share?</p>
<p>Thanks for your attention and to everyone answering<br>
Have a great day</p>

---

## Post #2 by @pieper (2022-08-07 16:11 UTC)

<p>Hi <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> - yes we used to have something like this as part of the <a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM/Widgets"><code>ctkDICOM</code></a> infrastructure but it wasn’t every quite finished so it was disabled (thumbnail jpg images were generated when the dicom files were imported).  But these days I would suggest just reading and rendering the images on the fly from disk would typically be efficient enough for what you are describing.  An image rendering feature could be added to the metadata browser dialog.  All the code for generating the dicom images in qt format is still around in the code so it would be pretty easy to hook it up to display images along side the metadata in the metadata browser dialog (or somewhere else).</p>
<p>Here’s what the original prototype looked like from <a href="http://www.commontk.org/index.php/CTK-Hackfest-Feb-2011">the 2011 hackfest</a> (good times!).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a058a9cecbbc2a692cb45236319c493e3919e3c.jpeg" data-download-href="/uploads/short-url/8hhz4WFlV8WWSnkMZTckTTbdL9G.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a058a9cecbbc2a692cb45236319c493e3919e3c_2_345x199.jpeg" alt="image" data-base62-sha1="8hhz4WFlV8WWSnkMZTckTTbdL9G" width="345" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a058a9cecbbc2a692cb45236319c493e3919e3c_2_345x199.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a058a9cecbbc2a692cb45236319c493e3919e3c_2_517x298.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a058a9cecbbc2a692cb45236319c493e3919e3c_2_690x398.jpeg 2x" data-dominant-color="BCBAB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1720×993 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
