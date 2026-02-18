# How to extract brain to STL when I have 3 different files with one HD resolution in one direction each?

**Topic ID**: 10294
**Date**: 2020-02-16
**URL**: https://discourse.slicer.org/t/how-to-extract-brain-to-stl-when-i-have-3-different-files-with-one-hd-resolution-in-one-direction-each/10294

---

## Post #1 by @meee (2020-02-16 18:02 UTC)

<p>Hello,</p>
<p>I am trying to do it for such a long time and find no answer anywhere.</p>
<p>I have few files from my brain MRI and I am trying to extract it to STL file so I can 3D print it.<br>
I have been trying to do it with FreeSurfer (I successfully have done it with other, good volume) an Slicer, and even combinign the images with <a href="https://github.com/gift-surg/NiftyMIC" rel="noopener nofollow ugc">NiftyMIC</a> but results are bad.</p>
<p>The problem is that scan was taken multiple times in one direction only (in T1 and T2 variants, and one with flare (but only one direction).</p>
<p>So I have multiple overlapping imagings and I would like to have stl model.</p>
<p>I can add nii.gz files if you are interested, but just give me some anonymization metod.</p>
<p>What I have (form my scan, best result):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/893360d52b41ccb9a3ca7d6a783ba52f3176a22a.jpeg" data-download-href="/uploads/short-url/jzJuqPmm9s4pQs7IuSREcRNbqb0.jpeg?dl=1" title="b1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/893360d52b41ccb9a3ca7d6a783ba52f3176a22a_2_582x500.jpeg" alt="b1" data-base62-sha1="jzJuqPmm9s4pQs7IuSREcRNbqb0" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/893360d52b41ccb9a3ca7d6a783ba52f3176a22a_2_582x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/893360d52b41ccb9a3ca7d6a783ba52f3176a22a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/893360d52b41ccb9a3ca7d6a783ba52f3176a22a.jpeg 2x" data-dominant-color="D6D5D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b1</span><span class="informations">872×748 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I want (done using great MRI scan and freesurfer):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac9e047f7b2ef710b4202bc9b919e9f180963b0d.png" data-download-href="/uploads/short-url/oD2FUxJy5kCMhPad6QGLO57MNFb.png?dl=1" title="b2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9e047f7b2ef710b4202bc9b919e9f180963b0d_2_690x458.png" alt="b2" data-base62-sha1="oD2FUxJy5kCMhPad6QGLO57MNFb" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9e047f7b2ef710b4202bc9b919e9f180963b0d_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9e047f7b2ef710b4202bc9b919e9f180963b0d_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac9e047f7b2ef710b4202bc9b919e9f180963b0d.png 2x" data-dominant-color="D2D0D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b2</span><span class="informations">1144×760 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-02-16 18:16 UTC)

<p>Unfortunately, you cannot combine 3 anisotropic images into one high-resolution image because lots of information is missing between the slices. See this topic for more details: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing?</a></p>

---
