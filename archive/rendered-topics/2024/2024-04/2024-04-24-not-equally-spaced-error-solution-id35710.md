# Not equally spaced error... solution?

**Topic ID**: 35710
**Date**: 2024-04-24
**URL**: https://discourse.slicer.org/t/not-equally-spaced-error-solution/35710

---

## Post #1 by @Gonzalo_Rojas_Costa (2024-04-24 16:05 UTC)

<p>Hi:</p>
<p>I am currently trying to load CT images (3D Slicer 5.7.0-2024-04-22 r32818 / 6884806), and I got the following error:</p>
<p>“Image slices are not equally spaced (1.5 spacing was expected, 4.5 spacing was found between files D:/cerro_el_plomo/Esmeralda/Dicom/ST00001/SE00003/IM00244 and D:/cerro_el_plomo/Esmeralda/Dicom/ST00001/SE00003/IM00248).  Slicer will apply a transform to this series trying to regularize the volume. Please use caution.”</p>
<p>How do I solve the problem?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @pieper (2024-04-24 16:45 UTC)

<p>That may not be a “problem”, just a description of the data with a message about how Slicer addressed it.  Have a look at the thread below and get back if there’s something else going on.</p>
<aside class="quote quote-modified" data-post="1" data-topic="19001">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/understanding-ct-image-spacing-and-acquisition-geometry-regularization/19001">Understanding CT Image spacing and Acquisition geometry regularization</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Dear all, 
"Images are not equally spaced (a difference of 0.6 vs 0.3 was detected)’ 
Why does this error occur? What causes the acquisition of acquired irregular geometry? is it something to do with CT machine, protocol, technique or just a problem with exporting the data? 
with Acquisition geometry regularization correction transform applied,  I tried to harden the transformation and I expected the corrected version of the image to persist but it changed to the original? is this the expected b…
  </blockquote>
</aside>


---
