---
topic_id: 20032
title: "Tool To Create Or Remove Surface"
date: 2021-10-06
url: https://discourse.slicer.org/t/20032
---

# Tool to create or remove surface

**Topic ID**: 20032
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/tool-to-create-or-remove-surface/20032

---

## Post #1 by @Felipe_Pinzon (2021-10-06 02:54 UTC)

<p>Slicer version:4.11.20210226</p>
<p>Good evening, I am carrying out a project where the deformation of the periodontal ligament is studied when doing a rapid expansion of the maxilla. For this I need to perform the reconstruction of the tooth tomography and design the ligament, but I cannot find a tool that allows me to create or erase surfaces for this task. That is why I use this forum to find out if anyone knows of any 3D Slicer tool that will allow me to achieve my goal. Thanks.</p>

---

## Post #2 by @manjula (2021-10-06 05:51 UTC)

<p>You can use segment editor to segment the parts of the tooth ( or any other structure).</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>
<aside class="quote quote-modified" data-post="9" data-topic="9775">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/teeth-segmentaion/9775/9">Teeth Segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve checked this and found that all teeth can be quite quickly and accurately segmented  at once by the following steps: 

Set editable intensity range from about 1880 to maximum using Threshold effect, “Use for masking”

 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abe1ef3a4fba2bd6e1fb12fb93e2a6240cd88b9f.jpeg" data-download-href="/uploads/short-url/owxI0DZMnPEQGISQGHiaT4vgpY3.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 

Using “Paint” effect, painta few strokes in the mandible and each tooth with different segment. You need to experiment to find what is the minimum amount that you need to paint and where, but probably it is enough to paint one stroke that goes down to the tip of th…
  </blockquote>
</aside>


---
