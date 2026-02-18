# Modelling the Anterior Muscle Compartment

**Topic ID**: 20554
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/modelling-the-anterior-muscle-compartment/20554

---

## Post #1 by @ejdr33s (2021-11-09 21:02 UTC)

<p>Hi there. I’m completely new to 3D slicer, let me preface that. My objective is to create a model of the anterior muscle compartment of the leg. I have found an MRI scan of the lower leg, shown in the attached image.</p>
<p>My question: how would I go about isolating the anterior muscle from the leg so that I can model it. Any general tips or advice is very much appreciated!</p>
<p>Ed<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33d5291abf94bb1070fe27940fc1c2ee6b27cc5.png" data-download-href="/uploads/short-url/yHNpjidvqTV8zxL6RCO5f799hfT.png?dl=1" title="Screenshot 2021-11-09 at 20.49.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f33d5291abf94bb1070fe27940fc1c2ee6b27cc5_2_656x500.png" alt="Screenshot 2021-11-09 at 20.49.08" data-base62-sha1="yHNpjidvqTV8zxL6RCO5f799hfT" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f33d5291abf94bb1070fe27940fc1c2ee6b27cc5_2_656x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33d5291abf94bb1070fe27940fc1c2ee6b27cc5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33d5291abf94bb1070fe27940fc1c2ee6b27cc5.png 2x" data-dominant-color="34353E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-11-09 at 20.49.08</span><span class="informations">864×658 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-11-09 21:09 UTC)

<p>The most commonly used tool for segmenting an individual muscle is “<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#fill-between-slices">Fill between slices</a>” effect in Segment Editor module. One reason is that there is no contrast difference between adjacent muscles, therefore automatic separation would be challenging. The other reason is that muscles tend to be long structures with a cross-section shape that changes slowly along the long axis, therefore, it is often enough to just segment 6-8 cross sections to get a complete reconstruction of the entire muscle shape in 3D.</p>
<p>I would recommend to get started with <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html">this page</a>, then learn about segmentation in general on <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a>. If you have any questions or run into any problems you can post follow-up questions here.</p>

---

## Post #3 by @ejdr33s (2021-11-15 20:15 UTC)

<p>Thank you so much for your helpful reply, I was able to create an approximate model of the compartment. The problem is, it’s very approximate, and I’m trying to get it a bit more accurate. To do this I had the idea of either highlighting the compartment itself somehow, or find a way to highlight the membrane that surrounds the compartment - that being the interosseous membrane and the anterior intermuscular septum. If I could do either of these things I could then accurately use the draw tool to create a model of the anterior compartment. Do you have any suggestions?</p>
<p>Thanks in advance!<br>
Ed</p>

---

## Post #4 by @lassoan (2021-11-16 00:11 UTC)

<aside class="quote no-group" data-username="ejdr33s" data-post="3" data-topic="20554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/f14d63/48.png" class="avatar"> ejdr33s:</div>
<blockquote>
<p>To do this I had the idea of either highlighting the compartment itself somehow</p>
</blockquote>
</aside>
<p>In Segment Editor, the current segment is shown in all the views (with filled contour). Do you have some other highlighting in mind?</p>
<aside class="quote no-group" data-username="ejdr33s" data-post="3" data-topic="20554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/f14d63/48.png" class="avatar"> ejdr33s:</div>
<blockquote>
<p>I was able to create an approximate model of the compartment. The problem is, it’s very approximate</p>
</blockquote>
</aside>
<p>You can be as accurate as needed. After you click “Preview” in “Fill between slices” effect, you can browse the slices and if you find that the interpolated segmentation is not accurate enough on any of the slices then you can modify the segmentation using Paint or Draw effects and the interpolated slices are immediately recomputed.</p>
<aside class="quote no-group" data-username="ejdr33s" data-post="3" data-topic="20554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/f14d63/48.png" class="avatar"> ejdr33s:</div>
<blockquote>
<p>find a way to highlight the membrane that surrounds the compartment - that being the interosseous membrane and the anterior intermuscular septum.</p>
</blockquote>
</aside>
<p>Yes, it sometimes it is worth segmenting adjacent structures, just to get some more context for segmenting a challenging object. For this, I would recommend to paint multiple compartments on each frame, for example, anterior, lateral, deep posterior, each using a different segment. Paint on those frames where you are confident that you can identify them, and then use “Fill between slices” effect to simultaneously interpolate all of them on all frames.</p>
<p>If you find a frame where interpolation did not provide sufficient accuracy, you can segment the compartments manually (using the existing estimation). Tips:</p>
<ol>
<li>If you segment multiple compartments, then you need to segment all compartments that are visible on a slice.</li>
<li>You can temporarily disable automatic update in “Fill between slices” effect to keep the preview result unchanged while you are painting the accurate boundaries.</li>
</ol>

---

## Post #5 by @ejdr33s (2021-11-16 11:00 UTC)

<p>Thanks for getting back to me, much appreciated!</p>
<p>When I say I want to highlight the compartment or the membrane that surrounds it, it is because I want to have a ‘template’ of the anterior compartment to draw around using the draw tool. I find it difficult to identify the specific compartments when looking at some slices such as the attached image.</p>
<p>I will have a go with painting multiple compartments and see if that makes a difference, and in the meantime, any suggestions you have for creating this ‘template’ would be greatly received.</p>
<p>Thanks again!</p>
<p>Ed</p>

---

## Post #6 by @lassoan (2021-11-16 13:23 UTC)

<p>You can use any single case at template. You can align and warp the template to a patient image using either point-based semi-automatic registration or automatic intensity based image registration - <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---

## Post #7 by @ejdr33s (2021-11-16 21:44 UTC)

<p>That sounds like it could be helpful, could you explain that a little further though please as the linked document has only left me with more questions!</p>
<p>Thanks,</p>
<p>Ed</p>

---

## Post #8 by @lassoan (2021-11-16 22:47 UTC)

<p>This video tutorial may help:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u93kI1MG6Ic" data-video-title="Quick manual segmentation with contour interpolation" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u93kI1MG6Ic" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u93kI1MG6Ic/maxresdefault.jpg" title="Quick manual segmentation with contour interpolation" width="" height="">
  </a>
</div>


---
