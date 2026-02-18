# Quality of registration

**Topic ID**: 7421
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/quality-of-registration/7421

---

## Post #1 by @Sibi_Thirunavukarasu (2019-07-04 22:24 UTC)

<p>Hi,</p>
<p>I am registering CT perfusion maps with the MRI DWI sequence using elastix module. Is there a way to check the quality of the registration other than visual assessment?<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2019-07-05 16:48 UTC)

<p>These posts should help:</p>
<aside class="quote quote-modified" data-post="8" data-topic="514">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/ct-to-optical-image-registration/514/8">CT to optical image registration</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Saving should be no problem, but maybe if it’s a color image there may be issues. Could you try if saving works if you convert the image to scalar (grayscale) volume (using Vector to scalar volume module)? 

Mutual information minimizes the entropy of the joint histogram. You can find the final value in the application log (the metric value should decrease in each iteration), but it’s not a metric of registration quality. 
Registration is typically assessed using spatial error metrics. If you h…
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="4" data-topic="3091">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/evaluating-registration-error/3091/4">Evaluating registration error</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You only need to do segmentation if you want to get quantitative results using Hausdorff or Dice metrics. 
It is also useful to do a very simple, threshold-based segmentation if you want to compare two images in a slice view, as it is difficult to see misalignment on two images that are blended together (especially when you want to see small differences), while misalignment is very clearly visible if you overlay extracted contours on an image. 
Example 1: perfectly aligned images (left: blending…
  </blockquote>
</aside>

<p>If you have any specific questions then let us know.</p>

---
