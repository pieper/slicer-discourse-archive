# 4D straightened volume rendering

**Topic ID**: 19269
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/4d-straightened-volume-rendering/19269

---

## Post #1 by @xiaolin (2021-08-19 07:49 UTC)

<p>Hi everyone.<br>
Warm Greetings.<br>
This is Xiaolin Sun, a doctoral student in Berlin.<br>
I am writing this message to ask for your kind help with 4D straightened volume rendering.<br>
I used the animal cardiac CT to reconstruct the right heart. The CT was reconstructed in every 10% of the cardiac cycle(from 0 to 100%), with this I get the 4D cardiac CT directly. Then I applied segmentation(right heart)-&gt; Add centerline-&gt; Curved Planar reformat-&gt;volume rendering, to get the straightened right heart model. As in the screenshot (right ventricle-pulmonary artery, top-&gt;down).<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a5fe34f9939cdf6993c4f2a7fa325f8b9a105be.jpeg" data-download-href="/uploads/short-url/fb239lbbNRXMKqLJff7mBGogOwS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a5fe34f9939cdf6993c4f2a7fa325f8b9a105be_2_690x393.jpeg" alt="image" data-base62-sha1="fb239lbbNRXMKqLJff7mBGogOwS" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a5fe34f9939cdf6993c4f2a7fa325f8b9a105be_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a5fe34f9939cdf6993c4f2a7fa325f8b9a105be_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a5fe34f9939cdf6993c4f2a7fa325f8b9a105be_2_1380x786.jpeg 2x" data-dominant-color="A1A2A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1094 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Furthermore, 4D dynamic heart can be achieved by volume rendering.<br>
Now, I am wondering how can I get the 4D straightened volume rendering, a beating straightened model. Should I segment every 10% of the cardiac cycle, export the Dicom file, register the 10 frames ( from 0-100 % of the cardiac cycle), or use other extensions? Could you please offer me some detailed guidance to achieve this?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-08-20 18:19 UTC)

<p>Volume rendering requires the transform to be hardened on the volume. If you load the 4D cardiac CT as a volume sequence (not as a multivolume) then you can apply and harden the transform on each frame.</p>

---
