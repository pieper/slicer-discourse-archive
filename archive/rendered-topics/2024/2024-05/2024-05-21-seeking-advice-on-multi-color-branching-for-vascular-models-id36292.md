# Seeking Advice on Multi-Color Branching for Vascular Models

**Topic ID**: 36292
**Date**: 2024-05-21
**URL**: https://discourse.slicer.org/t/seeking-advice-on-multi-color-branching-for-vascular-models/36292

---

## Post #1 by @petit223 (2024-05-21 09:44 UTC)

<p>Hello everyone,</p>
<p>I am currently working on a project where I aim to color different branches of a vascular model with distinct colors. I start by selecting a main vessel and use the first branching point as an anchor. From there, I want to apply different colors to three (or possibly more) branches. For this, I’ve been using the extract and centerline plugin, which has been incredibly helpful in identifying the necessary anchor points.</p>
<p>However, I’m at a bit of a standstill as I’m unsure how to apply colors to the surface of the vessels effectively. I would appreciate any suggestions or guidance from those who have tackled similar challenges. Any advice on techniques or tools that could be used for this purpose would be greatly appreciated.</p>
<p>Thank you for your help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/597285afb8f169edffa8b20787eb0f32efc1744c.png" data-download-href="/uploads/short-url/cLhRax2aH12JFeY1qLu5WhyXJ5W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/597285afb8f169edffa8b20787eb0f32efc1744c_2_690x442.png" alt="image" data-base62-sha1="cLhRax2aH12JFeY1qLu5WhyXJ5W" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/597285afb8f169edffa8b20787eb0f32efc1744c_2_690x442.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/597285afb8f169edffa8b20787eb0f32efc1744c_2_1035x663.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/597285afb8f169edffa8b20787eb0f32efc1744c_2_1380x884.png 2x" data-dominant-color="FBF7F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1489×954 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
（I drew a diagram to ensure that my above expression is clear）</p>

---

## Post #2 by @chir.set (2024-05-21 10:24 UTC)

<p>You may consider the ‘Branch clipper’ module in SlicerVMTK.</p>

---

## Post #3 by @petit223 (2024-05-21 12:27 UTC)

<p>Thank you very much, I’m certain this is what I need. However, I have a small issue. For more fragmented models, the original anchor points are missing due to the model being divided into several segments (maybe calculi or space-occupying), making it impossible to extract the centerline. Do you have any suggestions on how to handle this?</p>

---

## Post #4 by @chir.set (2024-05-21 13:18 UTC)

<aside class="quote no-group" data-username="petit223" data-post="3" data-topic="36292">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e5b9ba/48.png" class="avatar"> petit223:</div>
<blockquote>
<p>extract the centerline</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="petit223" data-post="3" data-topic="36292">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e5b9ba/48.png" class="avatar"> petit223:</div>
<blockquote>
<p>how to handle this</p>
</blockquote>
</aside>
<p>This question is quite different from the original.</p>
<p>I don’t really understand what you mean by ‘calculi, space-occupying’. The VMTK libraries called by the ‘Extract centerline’ module require good quality input. So your segmentation result is important, itself depending much on the quality of the original volume, in particular, the level of contrast available. I found that holes in the segmentation are very detrimental to centerline extraction. Fortunately, the ‘Smoothing’ effect of the ‘Segment editor’ has a ‘Fill holes’ functionality. Try that while looking for the most adequate settings of smoothing.</p>
<p>In general, providing pertinent images is helpful. At best, share your segmentation and your anonymized input volume as an MRB file. Guess work is not funny for the guys at the other end of the line.</p>

---

## Post #5 by @petit223 (2024-05-21 14:56 UTC)

<p>I’m sorry for the inconvenience caused. In fact, this plugin aligns very well with my goals, but when I applied it to other segments, I encountered new problems. For this reason, I have divided the segment files I need to handle into two categories: Case A and Case B. Case A can be resolved very well, but Case B is where I encountered the new problems (That’s what I mentioned earlier, a missing section).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e13dce14970b04d9e884a204e615d8c40fbf772.png" data-download-href="/uploads/short-url/20xeUlMOsF0dY1e2USts8ZrhuuK.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e13dce14970b04d9e884a204e615d8c40fbf772_2_690x439.png" alt="无标题" data-base62-sha1="20xeUlMOsF0dY1e2USts8ZrhuuK" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e13dce14970b04d9e884a204e615d8c40fbf772_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e13dce14970b04d9e884a204e615d8c40fbf772_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e13dce14970b04d9e884a204e615d8c40fbf772_2_1380x878.png 2x" data-dominant-color="FDFBF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">2043×1300 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I understand what you mean. Indeed, my model after segmentation is not high-quality input for the ‘extract centerline’ plugin, but it is realistic. I agree that ‘Fill holes’ is one method.</p>

---

## Post #6 by @chir.set (2024-05-21 15:08 UTC)

<p>In case B, ‘Fill holes’ won’t fill in the gap, that’s not what it’s meant to do. You should extract 3 distinct centerlines on 3 distinct segments. Why do you invest time in case B while case A is perfect?</p>

---

## Post #7 by @petit223 (2024-05-29 14:13 UTC)

<p>Sorry I just came back from a team equipment update. Actually, I deal with 3D reconstruction of magnetic resonance cholangiopancreatography. I will encounter the following situation:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1G5_FOrOo_GbXJCx21v0VVYkOteBXnBJ5/view?usp=drive_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1G5_FOrOo_GbXJCx21v0VVYkOteBXnBJ5/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1G5_FOrOo_GbXJCx21v0VVYkOteBXnBJ5/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1G5_FOrOo_GbXJCx21v0VVYkOteBXnBJ5/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">Pathological_case.stl</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
