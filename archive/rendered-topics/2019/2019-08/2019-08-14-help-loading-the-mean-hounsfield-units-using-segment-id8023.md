# Help Loading The Mean Hounsfield Units Using Segment

**Topic ID**: 8023
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/help-loading-the-mean-hounsfield-units-using-segment/8023

---

## Post #1 by @daleblack109 (2019-08-14 03:47 UTC)

<p>Hello</p>
<p>I cannot figure out how to display the average hounsfield units of my segmentation using segmentation statistics. Could anyone share screenshots of how it is done? I have shared screenshots of what I am trying to do, please point out what I am missing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e827720660b2bdb12cf5a0a1da8a13f9642f818.jpeg" data-download-href="/uploads/short-url/8UZ7G8DVDbsgNZqyDvABAepQBEA.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e827720660b2bdb12cf5a0a1da8a13f9642f818_2_690x302.jpeg" alt="Capture" data-base62-sha1="8UZ7G8DVDbsgNZqyDvABAepQBEA" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e827720660b2bdb12cf5a0a1da8a13f9642f818_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e827720660b2bdb12cf5a0a1da8a13f9642f818_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e827720660b2bdb12cf5a0a1da8a13f9642f818_2_1380x604.jpeg 2x" data-dominant-color="858589"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1914×838 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c13a64c82bc7e0bd223ba2218545204a23c7543.jpeg" data-download-href="/uploads/short-url/40nt1YLokvidzGt3fKpRdemEKH1.jpeg?dl=1" title="Segmentation%20Table" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c13a64c82bc7e0bd223ba2218545204a23c7543_2_690x296.jpeg" alt="Segmentation%20Table" data-base62-sha1="40nt1YLokvidzGt3fKpRdemEKH1" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c13a64c82bc7e0bd223ba2218545204a23c7543_2_690x296.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c13a64c82bc7e0bd223ba2218545204a23c7543_2_1035x444.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c13a64c82bc7e0bd223ba2218545204a23c7543_2_1380x592.jpeg 2x" data-dominant-color="848487"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segmentation%20Table</span><span class="informations">1910×821 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-08-15 16:34 UTC)

<p>To get average intensity (HU) of your CT in each segment’s region, then in in Segment statistics module choose your CT volume as “Scalar volume”.</p>

---

## Post #3 by @daleblack109 (2019-08-16 23:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a425de9ff3fc583e2c06e9b96020bdf160f1d9bd.png" data-download-href="/uploads/short-url/nq7rj7rbxivMxv5D3VpBxbzIBoF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a425de9ff3fc583e2c06e9b96020bdf160f1d9bd_2_690x332.png" alt="image" data-base62-sha1="nq7rj7rbxivMxv5D3VpBxbzIBoF" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a425de9ff3fc583e2c06e9b96020bdf160f1d9bd_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a425de9ff3fc583e2c06e9b96020bdf160f1d9bd_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a425de9ff3fc583e2c06e9b96020bdf160f1d9bd_2_1380x664.png 2x" data-dominant-color="9A999C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1907×920 64.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you! It worked</p>

---
