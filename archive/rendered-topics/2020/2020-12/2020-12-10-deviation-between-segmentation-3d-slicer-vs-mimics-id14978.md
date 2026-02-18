# Deviation between segmentation - 3D Slicer vs Mimics

**Topic ID**: 14978
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/deviation-between-segmentation-3d-slicer-vs-mimics/14978

---

## Post #1 by @LLacombe (2020-12-10 06:24 UTC)

<p>Hi,</p>
<p>I really like to work with 3D Slicer and i was curious about making a comparison between the segmentation made in 3D Slicer and Mimics. When comparing the same DICOM file segmented in both softwares, i get a dimensional deviation :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eb6c6a26fd22fbf670cc6473198dfca4e39ad41.jpeg" data-download-href="/uploads/short-url/i4XKVpuYAYYd5aAvzaNAf3LoUfL.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eb6c6a26fd22fbf670cc6473198dfca4e39ad41_2_690x336.jpeg" alt="Capture" data-base62-sha1="i4XKVpuYAYYd5aAvzaNAf3LoUfL" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eb6c6a26fd22fbf670cc6473198dfca4e39ad41_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eb6c6a26fd22fbf670cc6473198dfca4e39ad41_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eb6c6a26fd22fbf670cc6473198dfca4e39ad41.jpeg 2x" data-dominant-color="99B690"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1327×648 69.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What you see in the snippet above is the comparison between the radius segmented in Mimics and 3D Slicer. The reference surface is the radius segmented in Mimics. The surface of the radius segmented in 3D Slicer is nearly 0.8 to 1 mm smaller than the one segmented in Mimics. I tried to modify the lower threshold HU in 3D Slicer to see is there’s a difference, unfortunately without significant changes.</p>
<p>I used Mimics in the past for several custom implant design and i’m pretty confident with it, but i was wondering if there’s a way i can use 3D Slicer instead of Mimics. Is there adjustment i can make while making the segmentation in 3D Slicer so i can get closer to the Mimics results?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2020-12-10 06:37 UTC)

<p>Dimensional accuracy of segmentations created in 3D Slicer has been verified independently by many groups, so you can generally rely on measurements or segmentations done in Slicer, but of course in the end it is always the user’s responsibility to verify correctness of a particular processing workflow.</p>
<p>If you can provide us an image and example segmentations that you created in Mimics and Slicer then we can have a look. Make sure the data image is anonymized or get a sample data set from a public data repository (e.g., TCIA).</p>

---

## Post #3 by @LLacombe (2020-12-10 14:47 UTC)

<p>Hello,</p>
<p>Thank you for your answer. I came back to slicer and played with the different smoothing tools and realized that this is what is making a big difference in dimensional accuracy. Would you recommend smoothing with the tools in the segmentation palette and leave the 3D model smoothing factor to 0 in order to yield the best accuracy?</p>
<p>Best regards</p>

---

## Post #4 by @hherhold (2020-12-10 14:54 UTC)

<p>Just as a quick workflow comment, I tend to almost never use Segment Editor’s smoothing. I tend to favor the smoothing options in the Surface Toolbox as it gives me more fine-grained control - sometimes Segment Editor’s smoothing is a bit too much of a “black box” to me. This is entirely on me, of course - I should probably have a better understanding of what the smoothing parameter does in Segment Editor. I’m sure it’s documented somewhere.</p>

---

## Post #5 by @lassoan (2020-12-10 17:52 UTC)

<p>In labelmaps 3D shape is represented by discrete point samples. You can reconstruct the true physical object shape with smoothing. Many methods have been proposed over the years, providing slightly different results, each of them being optimal in some way. What is common in all of them that the error is smaller than the labelmap’s spacing.</p>
<p>Therefore, in practice, you need to reduce the segmentation labelmap’s spacing to be 2-5x smaller than your maximum acceptable surface error.</p>
<p>That’s why we often start segmentation with cropping and resampling the input volume using Crop volume module (make spacing smaller and isotropic and crop the volume to keep the data size under control), or use “Specify geometry” button in Segment Editor to specify an oversampling factor.</p>

---

## Post #6 by @LLacombe (2020-12-10 18:04 UTC)

<p>Thank you very much.</p>

---

## Post #7 by @tsehrhardt (2020-12-12 13:19 UTC)

<p>I have found that in Mimics, the “Optimal” 3d setting (Contour interpolation) produces a slightly larger model than using a Custom setting with Gray Value Interpolation selected–the difference also depends on scan resolution.</p>

---
