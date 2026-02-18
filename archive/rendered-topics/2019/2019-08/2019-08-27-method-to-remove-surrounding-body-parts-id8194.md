# Method to remove surrounding body parts

**Topic ID**: 8194
**Date**: 2019-08-27
**URL**: https://discourse.slicer.org/t/method-to-remove-surrounding-body-parts/8194

---

## Post #1 by @prorai (2019-08-27 13:21 UTC)

<p>How can i set a ROI which only selects the particular organ or body part.<br>
for example in abdomen there are organs and other body part , how can i choose only one while doing segmentation using threshold.</p>

---

## Post #2 by @lassoan (2019-08-27 13:29 UTC)

<p>In most imaging modalities, abdominal organs look quite similar to each other, so you cannot separate them by simple thresholding. You may try segmenting them using “Grow from seeds” effect or use other manual/semi-automatic methods. See some pointers for further help here:</p>
<aside class="quote" data-post="6" data-topic="5348">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/tutorial-for-doing-segmentation/5348/6">Tutorial for doing Segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There are 3 step-by-step tutorials and several segmentation recipes on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">training page of the latest Slicer version</a>. 
You can also find lots of questions and answers about segmentation on this forum (see <a href="https://discourse.slicer.org/tags/segmentation">segmentation tag</a> or use the search function). 
You may get help at any of the <a href="https://discourse.slicer.org/c/community/hangout">Slicer weekly hangouts</a> or if you attend a <a href="https://na-mic.github.io/ProjectWeek/" rel="nofollow noopener">Slicer project week</a>. 
If any of your questions are not answered, feel free to post it as a new topic in this forum.
  </blockquote>
</aside>


---
