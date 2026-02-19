---
topic_id: 25137
title: "Registration Transform As Sequence Bundle Format"
date: 2022-09-07
url: https://discourse.slicer.org/t/25137
---

# Registration transform as sequence bundle format

**Topic ID**: 25137
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/registration-transform-as-sequence-bundle-format/25137

---

## Post #1 by @Boris33 (2022-09-07 08:13 UTC)

<p>Hello 3DSlicer Community,</p>
<p>I have successfully performed registration of my 4D data thanks to the <a href="https://github.com/moselhy/SlicerSequenceRegistration" rel="noopener nofollow ugc">sequence registration module tutorial</a>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5de738b49d14c24eea0c8cb09e79f2833d12649.png" data-download-href="/uploads/short-url/z53zXM96BPu1IyWC0I33t31QzEZ.png?dl=1" title="Skärmbild 2022-09-07 095603" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5de738b49d14c24eea0c8cb09e79f2833d12649_2_669x500.png" alt="Skärmbild 2022-09-07 095603" data-base62-sha1="z53zXM96BPu1IyWC0I33t31QzEZ" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5de738b49d14c24eea0c8cb09e79f2833d12649_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5de738b49d14c24eea0c8cb09e79f2833d12649_2_1003x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5de738b49d14c24eea0c8cb09e79f2833d12649.png 2x" data-dominant-color="312222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmbild 2022-09-07 095603</span><span class="informations">1032×771 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I now need to export the volumes and transformation sequences to MatLab to further process them. Usually when performing registration of 3D data I could save the transform as a displacement field in .nrrd format which is convenient.</p>
<p>However the output transform I get from the sequence registration module can only be saved in .mrb or .seq.mrb formats which cannot be opened in MatLab. Is there any way to convert this format to .nrrd, is there something I’m doing wrong in 3DSlicer? There is no problem to save the sequence volumes directly in .nrrd by the way.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/824de69313355b8147e871676cead0f374dd2f01.png" data-download-href="/uploads/short-url/iAIYiFBPzUFdwsud5KsJRM2JEg9.png?dl=1" title="Skärmbild 2022-09-07 095448" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824de69313355b8147e871676cead0f374dd2f01_2_690x351.png" alt="Skärmbild 2022-09-07 095448" data-base62-sha1="iAIYiFBPzUFdwsud5KsJRM2JEg9" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824de69313355b8147e871676cead0f374dd2f01_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824de69313355b8147e871676cead0f374dd2f01_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/824de69313355b8147e871676cead0f374dd2f01.png 2x" data-dominant-color="EDEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skärmbild 2022-09-07 095448</span><span class="informations">1261×642 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you in advance for your help!</p>
<p>/Boris</p>

---
