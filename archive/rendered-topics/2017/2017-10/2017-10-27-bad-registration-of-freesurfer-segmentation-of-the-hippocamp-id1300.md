# Bad registration of Freesurfer segmentation of the hippocampus

**Topic ID**: 1300
**Date**: 2017-10-27
**URL**: https://discourse.slicer.org/t/bad-registration-of-freesurfer-segmentation-of-the-hippocampus/1300

---

## Post #1 by @Olof (2017-10-27 08:11 UTC)

<p>Hi,<br>
was wondering if anyone have experience with freesurfer segmentation of the hippocampus in SPHARM.</p>
<p>I tried various tricks but the registration really does not work. It is obvious that there are several irregularities of the shape from FS but I find it a bit strange that I cannot get the registration to work … as the overall shape is relatively similar between subjects.</p>
<p>So far i tried to increase or decreas spherical complexity 10 - 15 - 20 - did not work for any of these.</p>
<p>I also tried to use different subjects as reference for the registration (choosing one that seem to have a relatively regular shape).</p>
<p>Is there anything else that I can try?</p>
<p>best<br>
Olof</p>

---

## Post #2 by @bpaniagua (2017-10-27 12:48 UTC)

<p>Hi Olof,</p>
<p>Sorry this is being a challenge. Do you have an example snapshot on how the segmentation looks like?</p>
<p>Thank you,<br>
Bea</p>

---

## Post #3 by @Olof (2017-11-01 12:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/997ef17122b4dafc05dbf0929a7845c252384ba7.png" data-download-href="/uploads/short-url/lTT1HgP3zNWC7I1eZZOfqYkVXw3.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/997ef17122b4dafc05dbf0929a7845c252384ba7_2_690x194.png" alt="1" data-base62-sha1="lTT1HgP3zNWC7I1eZZOfqYkVXw3" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/997ef17122b4dafc05dbf0929a7845c252384ba7_2_690x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/997ef17122b4dafc05dbf0929a7845c252384ba7_2_1035x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/997ef17122b4dafc05dbf0929a7845c252384ba7_2_1380x388.png 2x" data-dominant-color="BABCBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">3840×1080 751 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6e6f470b56cb3b4e1591449572f6d4e337d9620.png" data-download-href="/uploads/short-url/q61Iwm3wnF0oVfLietcp5XLxxq8.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b6e6f470b56cb3b4e1591449572f6d4e337d9620_2_690x194.png" alt="2" data-base62-sha1="q61Iwm3wnF0oVfLietcp5XLxxq8" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b6e6f470b56cb3b4e1591449572f6d4e337d9620_2_690x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b6e6f470b56cb3b4e1591449572f6d4e337d9620_2_1035x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b6e6f470b56cb3b4e1591449572f6d4e337d9620_2_1380x388.png 2x" data-dominant-color="A9AAAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">3840×1080 694 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80fae44b919c02fdc93bbdfc61cd2f89f8287829.jpeg" data-download-href="/uploads/short-url/ip0EgbKZy9PfUaRPBPfkwI38ez7.jpg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80fae44b919c02fdc93bbdfc61cd2f89f8287829_2_690x194.jpg" alt="3" data-base62-sha1="ip0EgbKZy9PfUaRPBPfkwI38ez7" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80fae44b919c02fdc93bbdfc61cd2f89f8287829_2_690x194.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80fae44b919c02fdc93bbdfc61cd2f89f8287829_2_1035x291.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/80fae44b919c02fdc93bbdfc61cd2f89f8287829_2_1380x388.jpg 2x" data-dominant-color="969698"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">3840×1080 692 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So attached are some images … Highly irregular I admint - but I had hoped that the overall shape and curvature of the structure would make it possible to make an ok registration.</p>

---
