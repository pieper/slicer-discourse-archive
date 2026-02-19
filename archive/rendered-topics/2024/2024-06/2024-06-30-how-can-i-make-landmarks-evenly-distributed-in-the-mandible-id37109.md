---
topic_id: 37109
title: "How Can I Make Landmarks Evenly Distributed In The Mandible"
date: 2024-06-30
url: https://discourse.slicer.org/t/37109
---

# How can i make landmarks evenly distributed in the mandible?

**Topic ID**: 37109
**Date**: 2024-06-30
**URL**: https://discourse.slicer.org/t/how-can-i-make-landmarks-evenly-distributed-in-the-mandible/37109

---

## Post #1 by @yijie3091 (2024-06-30 15:16 UTC)

<p>Operating system:win11<br>
Slicer version:5.6.2<br>
Expected behavior:i want to use the “PseudoLandmarks”  where i use "Original Geometry"to make the landmarks evenly distributed in the mandible.<br>
Actual behavior:it has some blank regions in the right jaw,and the left has a relatively better result than the left.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9205e9d15871caf844342327a0f5a638df544be4.png" data-download-href="/uploads/short-url/kPMnyE482MWLXywczmom3a80AGE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9205e9d15871caf844342327a0f5a638df544be4_2_690x416.png" alt="image" data-base62-sha1="kPMnyE482MWLXywczmom3a80AGE" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9205e9d15871caf844342327a0f5a638df544be4_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9205e9d15871caf844342327a0f5a638df544be4_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9205e9d15871caf844342327a0f5a638df544be4.png 2x" data-dominant-color="A694AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1101×664 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f76200c1a602c59af48eeb72a2387579f611fbc4.png" data-download-href="/uploads/short-url/zirU8Z5s0gh7vZgekye5tKDSBik.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f76200c1a602c59af48eeb72a2387579f611fbc4_2_690x495.png" alt="image" data-base62-sha1="zirU8Z5s0gh7vZgekye5tKDSBik" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f76200c1a602c59af48eeb72a2387579f611fbc4_2_690x495.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f76200c1a602c59af48eeb72a2387579f611fbc4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f76200c1a602c59af48eeb72a2387579f611fbc4.png 2x" data-dominant-color="A39C74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">832×597 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-06-30 17:11 UTC)

<p>Are you using a plane? If you are not trying to make symmetrical template (with landmarks designated as left and right), I wouldn’t use a plane.</p>
<p>There are a few things to consider. If you are using “Model Geometry” make sure your model’s triangulation is fairly uniform (you can check that by enabling the surface with edges option in Models module for visualization). If they are not, try using the Surface Toolbox, Uniform Remesh option and run it something like 50K option.</p>
<p>Finally, make the Maximum project factor small, and then if points are not ending on the surface, incrementally increase that.</p>

---

## Post #3 by @yijie3091 (2024-08-31 17:37 UTC)

<p>we all know that pseudo-landmarks are semi-landmarks,so when i perform geometric<br>
morphological analysis,it is necessary to have landmarks.thus,i have a problem “how can i make landmarks and semi-landmarks exist at the same time.”<br>
the red are landmarks manually,green are pseudo-landmarks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/611154fd08ec76be9471207b693d4230577e935b.png" data-download-href="/uploads/short-url/dQHrN2H4VFh6WjWPmNq9s6wA0jx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/611154fd08ec76be9471207b693d4230577e935b_2_690x393.png" alt="image" data-base62-sha1="dQHrN2H4VFh6WjWPmNq9s6wA0jx" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/611154fd08ec76be9471207b693d4230577e935b_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/611154fd08ec76be9471207b693d4230577e935b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/611154fd08ec76be9471207b693d4230577e935b.png 2x" data-dominant-color="95A09D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">954×544 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a054a9380774845061e6763c6e539fc4095f8c8.png" data-download-href="/uploads/short-url/hprAsclg3I9GsmGewSWqP2iC2dG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a054a9380774845061e6763c6e539fc4095f8c8_2_676x500.png" alt="image" data-base62-sha1="hprAsclg3I9GsmGewSWqP2iC2dG" width="676" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a054a9380774845061e6763c6e539fc4095f8c8_2_676x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a054a9380774845061e6763c6e539fc4095f8c8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a054a9380774845061e6763c6e539fc4095f8c8.png 2x" data-dominant-color="9BA39C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×655 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-08-31 21:38 UTC)

<p>Not sure what you are asking? You clearly got  both semi and anatomical landmarks together.</p>
<p>If you are asking how to save them in a single json file, you can use the MergeMarkups module to save them into a single file.</p>

---

## Post #5 by @yijie3091 (2024-09-01 15:37 UTC)

<p>yes,thank you very much,what you say solves my problem;and i have other questions which really need your help;one is that how to make a "mandible template"from many mandibles in slicermorph ;and the other is how to segment crestal area precisely apart from mandible.</p>

---

## Post #6 by @muratmaga (2024-09-02 05:54 UTC)

<p>Since your original question is answered, please post separate questions for these two. That allows finding answers easier on the forum.</p>

---

## Post #7 by @yijie3091 (2024-09-04 07:56 UTC)

<p>OK,thank you very much!</p>

---
