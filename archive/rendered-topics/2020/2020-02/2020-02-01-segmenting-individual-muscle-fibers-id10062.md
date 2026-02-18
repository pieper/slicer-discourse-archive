# Segmenting individual muscle fibers

**Topic ID**: 10062
**Date**: 2020-02-01
**URL**: https://discourse.slicer.org/t/segmenting-individual-muscle-fibers/10062

---

## Post #1 by @Yordano_Jimenez (2020-02-01 15:57 UTC)

<p>Hey folks,</p>
<p>I am vertebrate morphologist using Slicer to segment bones and muscles (from contrast-stained specimens). I am comfortable with segmenting bone and muscle (i.e., the whole muscle body), but the next step of my research requires segmenting out individual muscle fibers. I envision being able to manually draw a straight line in one plane, and then adjust the angle of that line in another plane. Then these lines would have a 3D vector of some sort where I can measure their lengths and angles (see first image). I am aware that I can literally segment the individual muscle fibers separately, but this would be too difficult with the scan quality I have.</p>
<p>Any help would be greatly appreciated!!</p>
<p>–Yordano</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62ec9a2b426d42d4592c65c16447942d652b3550.jpeg" data-download-href="/uploads/short-url/e77I1lyANDHygR4IXna376lnX9u.jpeg?dl=1" title="slicer_question-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ec9a2b426d42d4592c65c16447942d652b3550_2_690x384.jpeg" alt="slicer_question-01" data-base62-sha1="e77I1lyANDHygR4IXna376lnX9u" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ec9a2b426d42d4592c65c16447942d652b3550_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ec9a2b426d42d4592c65c16447942d652b3550_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62ec9a2b426d42d4592c65c16447942d652b3550_2_1380x768.jpeg 2x" data-dominant-color="4A4A51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_question-01</span><span class="informations">3508×1954 787 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system:Windows<br>
Slicer version:4.10.2</p>

---

## Post #2 by @lassoan (2020-02-01 23:49 UTC)

<p>This sounds like an interesting project. Would you like to analyse those separating lines on their own (their distances, angles, etc.) or create volumetric segmentation of individual bundles (subdivide the muscle segments to smaller segments)?</p>

---

## Post #3 by @Yordano_Jimenez (2020-02-02 04:17 UTC)

<p>Thanks for such a quick reply!</p>
<p>I think the latter option is what I would like to do (volumetric segmentation). Attached is an example from a scientific publication by Dickinson et al. (2019).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af604d089891727d47608a8e60b521041d51bee7.jpeg" alt="dicect2" data-base62-sha1="p1rSCStQJ9puzdEJLLT4oxClSab" width="606" height="304"></p>

---

## Post #4 by @Yordano_Jimenez (2020-02-02 16:39 UTC)

<p>After some thought, I think the best way to describe what I’d like to do is I’d like to have volumetric models of the individual muscle fibers (as shown in the photo above under “fascicular econstruction”) while also being able to analyze the lengths and angles of those individual fibers.</p>
<p>It’s not completely necessary for me to measure the lengths and angles of those individual fibers with Slicer. But it would be great if I could “segment” each individual muscle fibers as a straight line and export those fibers as a vector field which I could analyze elsewhere–unless there’s already a way to do that in Slicer!</p>
<p>Hope that clarification helps.</p>

---

## Post #5 by @lassoan (2020-02-02 17:23 UTC)

<p>You can segment volume or you can manually segment maybe a few hundred lines, but those lines in the “fascicular reconstruction” image seem to be thousands of lines - probably streamlines generated from a vector or tensor field.</p>
<p>I see two options:</p>
<p>A. Manual tracing: Use curve tool in recent recent Slicer preview release to track fibers manually. This may be a lot of work if you want to segment many segments (and not feasible but to segment thousands of them) but very robust and does not require any custom algorithm development.</p>
<p>B. Automatic tracing: You could apply some processing to convert the texture of the CT images to tensor images and use Slicer’s diffusion tractography modules to generate fiber tracts. Such processing may not be easy (you probably need to get funding to get this developed if there are no readily available solutions) and the algorithm may be sensitive to image quality, but this would be very nice way to leverage tools that are originally developed for MRI diffusion tractography in a completely new domain.</p>

---
