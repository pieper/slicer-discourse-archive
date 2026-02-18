# Plus remote > 'scan scout' error (Plus server)

**Topic ID**: 19019
**Date**: 2021-08-02
**URL**: https://discourse.slicer.org/t/plus-remote-scan-scout-error-plus-server/19019

---

## Post #1 by @sujin (2021-08-02 05:23 UTC)

<p>Hello. I’m sujin</p>
<ol>
<li>
<p>I am currently sending ‘images’ and ‘image’s location information’ from visual studio to 3D slicer and plus server using openigtlink.</p>
</li>
<li>
<p>The images and location information is transmitted well in real time(of course, it takes little time for these information to be transmitted.), and I can see the image moving on the slicer.</p>
</li>
<li>
<p>I want to perform 3D reconstruction using [Plus remote &gt; scan scout], but I am having trouble with the following two errors in ‘plus server’. How can I solve this?</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31e17eb6ca75ff2ce30b7747233326616b11c310.png" data-download-href="/uploads/short-url/77gw2CCEUg8i3P6M1bBh8D9yw5W.png?dl=1" title="error1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e17eb6ca75ff2ce30b7747233326616b11c310_2_690x122.png" alt="error1" data-base62-sha1="77gw2CCEUg8i3P6M1bBh8D9yw5W" width="690" height="122" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e17eb6ca75ff2ce30b7747233326616b11c310_2_690x122.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e17eb6ca75ff2ce30b7747233326616b11c310_2_1035x183.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31e17eb6ca75ff2ce30b7747233326616b11c310_2_1380x244.png 2x" data-dominant-color="EAE2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error1</span><span class="informations">1465×260 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c670ffeda2211940330bfc6701992a1e51a51253.png" data-download-href="/uploads/short-url/sjuDFTGXCNbQLc2QFBmRfHssz07.png?dl=1" title="error2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c670ffeda2211940330bfc6701992a1e51a51253_2_690x244.png" alt="error2" data-base62-sha1="sjuDFTGXCNbQLc2QFBmRfHssz07" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c670ffeda2211940330bfc6701992a1e51a51253_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c670ffeda2211940330bfc6701992a1e51a51253_2_1035x366.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c670ffeda2211940330bfc6701992a1e51a51253_2_1380x488.png 2x" data-dominant-color="F7D8D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error2</span><span class="informations">1677×594 682 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-08-03 16:23 UTC)

<p>It seems that you haven’t specified hole filling parameters. You either need to disable hole filling or add these missing parameters (see other Plus configuration files for examples).</p>

---
