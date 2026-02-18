# Black layers on z-axis

**Topic ID**: 26264
**Date**: 2022-11-16
**URL**: https://discourse.slicer.org/t/black-layers-on-z-axis/26264

---

## Post #1 by @hpok (2022-11-16 19:16 UTC)

<p>Hello everyone, I would like to ask about importing data into Slicer. I have a sequence of tiffs of cells. I have converted them to nrrd data to use within the Slicer. When I load them in, their almost correct measurements load by themselves<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab455073aaf1682e5aa25ff1acabf7540e578531.jpeg" data-download-href="/uploads/short-url/or89suMJARouy6NglgCwAjBewhj.jpeg?dl=1" title="image (3)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab455073aaf1682e5aa25ff1acabf7540e578531_2_643x500.jpeg" alt="image (3)" data-base62-sha1="or89suMJARouy6NglgCwAjBewhj" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab455073aaf1682e5aa25ff1acabf7540e578531_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab455073aaf1682e5aa25ff1acabf7540e578531_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab455073aaf1682e5aa25ff1acabf7540e578531.jpeg 2x" data-dominant-color="424255"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (3)</span><span class="informations">1166×906 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26fcf07e47ddd471f7e299250f2de94d90c778ae.jpeg" data-download-href="/uploads/short-url/5yU3YoNcgR9KbiC0JwEAqi9o4r4.jpeg?dl=1" title="MicrosoftTeams-image (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26fcf07e47ddd471f7e299250f2de94d90c778ae_2_631x500.jpeg" alt="MicrosoftTeams-image (2)" data-base62-sha1="5yU3YoNcgR9KbiC0JwEAqi9o4r4" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26fcf07e47ddd471f7e299250f2de94d90c778ae_2_631x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26fcf07e47ddd471f7e299250f2de94d90c778ae_2_946x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26fcf07e47ddd471f7e299250f2de94d90c778ae.jpeg 2x" data-dominant-color="4C4D62"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MicrosoftTeams-image (2)</span><span class="informations">1171×927 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(Volumes → More Information-&gt; Slice Spacing) at values 1.242 x 1.242 x 1.242. The Slices, however, have a black layering on the z-axis (see photo 1). I change the layer spacing to be correct: 1.242 x 1.242 x 6, at which point the z axis elongates but the black layers stay (picture 2). How can I make the slices sit closer together so there are no black division line spaces between the slices with the data? I have another dataset with a larger single cell where this ‘layering’ isn’t an issue (also tiffs converted to nrrd dataset). Thank you in advance.</p>

---

## Post #2 by @lassoan (2022-12-01 07:14 UTC)

<p>It seems that the conversion to NRRD file had some errors. You can load the TIFF stack directly, using ImageStacks module of SlicerMorph extension.</p>

---

## Post #3 by @hpok (2022-12-04 11:31 UTC)

<p>Hi Andras, thank you so much for your response.<br>
I have tried the Slicer Morph and when I adjust the slice thickness, it becomes all distorted…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fbc10a1dbbc724c2f45d9624ae4b5b629f6c7c8.png" data-download-href="/uploads/short-url/mN4QoIIVVlqOtZMGW1pb6JiPACs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fbc10a1dbbc724c2f45d9624ae4b5b629f6c7c8_2_553x500.png" alt="image" data-base62-sha1="mN4QoIIVVlqOtZMGW1pb6JiPACs" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fbc10a1dbbc724c2f45d9624ae4b5b629f6c7c8_2_553x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fbc10a1dbbc724c2f45d9624ae4b5b629f6c7c8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fbc10a1dbbc724c2f45d9624ae4b5b629f6c7c8.png 2x" data-dominant-color="5D5D7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">804×726 99.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
