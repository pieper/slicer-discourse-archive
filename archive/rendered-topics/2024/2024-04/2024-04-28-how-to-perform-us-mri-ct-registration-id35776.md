# How to perform US MRI/CT registration?

**Topic ID**: 35776
**Date**: 2024-04-28
**URL**: https://discourse.slicer.org/t/how-to-perform-us-mri-ct-registration/35776

---

## Post #1 by @jay1987 (2024-04-28 01:59 UTC)

<p>I want to perform registration from US to CT or MRI. The ants, elastix, and brains algorithms can perform registration from 3D to 3D. But if I want to perform registration from 2D US to 3D CT/MRI, is there any way in Slicer? Or can it be achieved through code?</p>

---

## Post #2 by @pieper (2024-04-29 15:56 UTC)

<p>I don’t have a good solution for this registration task.</p>
<p>But I used your question as a test for the AI plugin to discourse.  It would be interesting to know if people think the result is helpful.</p>
<aside class="quote quote-modified" data-post="6" data-topic="34811">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/semantic-search-for-this-forum/34811/6">Semantic search for this forum</a> <a class="badge-category__wrapper " href="/c/forum-feedback/10"><span data-category-id="10" style="--category-badge-color: #B3B5B4; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Discussion about this site, its organization, how it works, and how we can improve it."><span class="badge-category__name">Forum and website feedback</span></span></a>
  </div>
  <blockquote>
    I also tried posting <a href="https://discourse.slicer.org/t/how-to-perform-us-mri-ct-registration/35776">this question</a> and here’s what I got.  These results are encouraging I think.  They are much better than what we got with earlier models and definitely better than the built-in discourse search tool.  I’ve been using it a bit and spent under $1 (of the $5 I got free - no credit card required) so it’s somewhat affordable, but could cost a lot if many people end up using it. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b61b1dc125e6da01094029f0649451f06fee6026.png" data-download-href="/uploads/short-url/pYYZK8tQBFhxU4BecNjULxAKhmu.png?dl=1" title="image">[image]</a> 
<a href="https://discourse.slicer.org/u/claude_3_opus_bot">claude_3_opus_bot</a>Forum Helper 
<a href="https://discourse.slicer.org/t/untitled-ai-bot-pm/35806/2">10m</a> 
Search 
Found 1 <a href="https://discourse.slicer.org/search?q=registration+2d+ultrasound+3d+ct+mri">result</a> for ‘registration 2d ultrasound 3d…
  </blockquote>
</aside>


---

## Post #3 by @cpinter (2024-04-30 12:07 UTC)

<p>I think the AI answer is pretty good. I’m not an expert in 2D-3D segmentation, but would have answered something similar if I had considered myself the best person to answer (which I didn’t so passed the opportunity to other, smarter people).</p>
<p>Unfortunately there is no clear solution, or any finished project I’m aware of. Making a 3D volume from the slice is an idea that did crossed my mind, but I don’t think it would work. However, it’s just a hunch, based on my knowledge about the BRAINS and Elastix extensions, so it’s worth a try. What I think that means is making a “thicker” slice, maybe 3 or 5 adjacent slices of that US image, make sure the area out of the fan is masked out, and run the registration in the two modules I mention above.</p>

---

## Post #4 by @LeidyMoraV (2024-04-30 15:40 UTC)

<p>Maybe this article with help you with some ideas:<br>
Behnami, D., Sedghi, A., Anas, E.M.A. <em>et al.</em> Model-based registration of preprocedure MR and intraprocedure US of the lumbar spine. <em>Int J CARS</em> <strong>12</strong> , 973–982 (2017). <a href="https://doi.org/10.1007/s11548-017-1552-2" class="inline-onebox" rel="noopener nofollow ugc">Model-based registration of preprocedure MR and intraprocedure US of the lumbar spine | International Journal of Computer Assisted Radiology and Surgery</a></p>

---

## Post #5 by @Ontheroad123 (2024-12-04 12:20 UTC)

<p>I meet the same problem, US is arbitrarily section without pose information， do you have resolve this problem?</p>

---
