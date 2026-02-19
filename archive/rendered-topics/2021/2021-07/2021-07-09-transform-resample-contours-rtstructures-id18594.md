---
topic_id: 18594
title: "Transform Resample Contours Rtstructures"
date: 2021-07-09
url: https://discourse.slicer.org/t/18594
---

# Transform & Resample Contours/RTStructures?

**Topic ID**: 18594
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/transform-resample-contours-rtstructures/18594

---

## Post #1 by @MichaelCHL (2021-07-09 00:25 UTC)

<p>Hi all, I am new to 3D Slicer <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">. For a project I am working on, I need to transform some CT scans alongside with the contours from Eclipse and reimport them back into Eclipse afterwards.</p>
<p>To read the contours (RTStructures), I installed the SlicerRT plugin. I did manage to apply transformations via the Transforms Module to both the scan, contours and fiducials, but when I try to resample them, it only works for the CT scans. (there are only options for 3:RTP Brain but not for 7:RTStructure under the Resample Module)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5684421bdbe21309207fab24d1655d24011a31bb.jpeg" data-download-href="/uploads/short-url/clmqjuyo9RRcrsQeGsyRTff1woz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5684421bdbe21309207fab24d1655d24011a31bb_2_690x402.jpeg" alt="image" data-base62-sha1="clmqjuyo9RRcrsQeGsyRTff1woz" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5684421bdbe21309207fab24d1655d24011a31bb_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5684421bdbe21309207fab24d1655d24011a31bb_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5684421bdbe21309207fab24d1655d24011a31bb_2_1380x804.jpeg 2x" data-dominant-color="788C7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1439×840 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f003620db53b6f871f785eb2f302912254b56851.jpeg" data-download-href="/uploads/short-url/yffQ8NqWARIUNQbeUCNGC9MhflD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f003620db53b6f871f785eb2f302912254b56851_2_690x402.jpeg" alt="image" data-base62-sha1="yffQ8NqWARIUNQbeUCNGC9MhflD" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f003620db53b6f871f785eb2f302912254b56851_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f003620db53b6f871f785eb2f302912254b56851_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f003620db53b6f871f785eb2f302912254b56851_2_1380x804.jpeg 2x" data-dominant-color="778B79"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1439×839 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any way to rotate+translate the scans together with the contours and/or fiducials and output them all togther as DICOＭ files? This have been bothering me for a while so any help will be appreciated!</p>
<p>Thank you for your help in advance!</p>
<p>BW<br>
Michael</p>

---

## Post #2 by @cpinter (2021-07-09 13:48 UTC)

<p>What Slicer version do you use? That part is just cropped from both screenshots <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #3 by @MichaelCHL (2021-07-09 14:04 UTC)

<p>Hi Csaba, the version is 4.11.20210226 for Windows. Many thanks! <img src="https://emoji.discourse-cdn.com/twitter/grinning_face_with_smiling_eyes.png?v=9" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:"></p>

---

## Post #4 by @cpinter (2021-07-09 14:08 UTC)

<p>You use the wrong method for applying the registration. There is no need to go so complex, you can do it much simpler. As far as I remember the IGRT tutorial shows just this:<br>
<a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/SlicerRT#Tutorials" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/SlicerRT#Tutorials</a></p>

---

## Post #5 by @MichaelCHL (2021-07-09 15:38 UTC)

<p>Hi, Thanks for the reply! I’ve tried to transformed the data, harden it and then export to DICOM (without trying to resample it), which works well for translations, but for any transformation involving rotations, half the the body contour is lost and the red target is also missing when I reopen the exported data:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bbcdad5963392239c606fb0fc3fe60eaaa583ef.jpeg" data-download-href="/uploads/short-url/fn5HX7cjAGAUVGnbKGqrRsqYxXx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbcdad5963392239c606fb0fc3fe60eaaa583ef_2_690x450.jpeg" alt="image" data-base62-sha1="fn5HX7cjAGAUVGnbKGqrRsqYxXx" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbcdad5963392239c606fb0fc3fe60eaaa583ef_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbcdad5963392239c606fb0fc3fe60eaaa583ef_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bbcdad5963392239c606fb0fc3fe60eaaa583ef_2_1380x900.jpeg 2x" data-dominant-color="374A43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1420×927 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What I was trying to do is to rotate the phantom about the red target, where I first translate the target to the origin (which works fine), and then I applied a 10 degree rotation along one of the axis, and this happens.</p>
<p>It is weird as it works well for the CT scans, and only affecting the contours.</p>
<p>Any thought? Thanks again!</p>

---

## Post #6 by @MichaelCHL (2021-07-09 16:00 UTC)

<p>Here the some more images to illustrate the problem:</p>
<p>Original Image set in Eclipse:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8af964af0997507e3b8ca338871ec56191f759bb.jpeg" data-download-href="/uploads/short-url/jPqdf3rSAKBfeeUH9lggiCbOzSX.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af964af0997507e3b8ca338871ec56191f759bb_2_690x339.jpeg" alt="Capture" data-base62-sha1="jPqdf3rSAKBfeeUH9lggiCbOzSX" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af964af0997507e3b8ca338871ec56191f759bb_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af964af0997507e3b8ca338871ec56191f759bb_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8af964af0997507e3b8ca338871ec56191f759bb_2_1380x678.jpeg 2x" data-dominant-color="111212"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1618×796 72.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I then import it into 3D slicer to transform it, first translating the target to the origin (I’ve checked that this step is fine). I then rotate the whole structure about the origin, now some of the contours are missing on both 3D Slicer and Eclipse:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d89ad6a1760b5edab394ce808f35cfde44bec1c.jpeg" data-download-href="/uploads/short-url/dltno2kBiemdXWOCN19kQhPNXDS.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d89ad6a1760b5edab394ce808f35cfde44bec1c_2_690x340.jpeg" alt="Capture2" data-base62-sha1="dltno2kBiemdXWOCN19kQhPNXDS" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d89ad6a1760b5edab394ce808f35cfde44bec1c_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d89ad6a1760b5edab394ce808f35cfde44bec1c_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d89ad6a1760b5edab394ce808f35cfde44bec1c_2_1380x680.jpeg 2x" data-dominant-color="121212"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1617×797 68.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-07-11 15:27 UTC)

<p>Can you share the scene (saved as .mrb file) that you have trouble exporting? Use an anonymized data set or - even better - a publicly available sample data set.</p>

---

## Post #8 by @MichaelCHL (2021-07-12 15:31 UTC)

<p>Hi Andras, thanks for the reply, I am now using Eclipse to register the contours to the rotated CT scans so this problem has been solved.</p>

---
