---
topic_id: 41743
title: "What Smoothing Is Applied To Segmentations Before Stl Export"
date: 2025-02-17
url: https://discourse.slicer.org/t/41743
---

# What smoothing is applied to segmentations before STL export?

**Topic ID**: 41743
**Date**: 2025-02-17
**URL**: https://discourse.slicer.org/t/what-smoothing-is-applied-to-segmentations-before-stl-export/41743

---

## Post #1 by @ramen (2025-02-17 14:41 UTC)

<p>Hi everyone,</p>
<p>I would like to understand the smoothing process applied to segmentations when exporting them as .stl files in 3D Slicer.</p>
<p>I assume that after applying the Marching Cubes algorithm, the software performs some form of surface smoothing to refine the final result. Could someone clarify what specific smoothing steps are applied by default?</p>
<ul>
<li>Does 3D Slicer use a particular smoothing filter after mesh generation?</li>
<li>Is it possible to disable the smoothing process?</li>
</ul>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @cpinter (2025-02-18 12:46 UTC)

<p>I don’t have any time right now to find the information, but I am completely sure that this question has been answered several times here in the forum (by me as well more than once). I know that the search function on discourse is really bad, but please give it a try!</p>
<p>Let us know if you cannot find it. And if you can please paste the links here for future reference.</p>
<p>Again, sorry for the non-answer, but this is an FAQ by now and I’m super swamped today.</p>

---

## Post #3 by @ramen (2025-02-19 09:08 UTC)

<p>Thank you for your reply!</p>
<p>I’ve spent several hours searching through the forum, but unfortunately, I couldn’t find the answer. I understand that this is a frequently asked question, but the search function made it quite challenging to locate the relevant threads.</p>
<p>If you have any hints on specific keywords or topics to look for, I’d really appreciate it. Otherwise, if you happen to find a moment later on, any guidance would be super helpful.</p>
<p>Thanks again for your time and understanding!</p>

---

## Post #4 by @cpinter (2025-02-19 10:01 UTC)

<p>I understand, sorry that you spent so much time searching, with no avail. I found this topic which talks about this:</p><aside class="quote" data-post="1" data-topic="1933">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/35a633/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/turn-off-all-smoothing-in-segmentation/1933">Turn off all smoothing in segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    O.S. Win 10 - 64bit 
Version: 4.8.1 
Hi there, 
We are willing to apply this software to segment the thalamus and need to correct segmentation errors on a pixel-by-pixel basis. For this reason, we need to abolish any possible type of smoothing on the source image. Is that by any means possible? 
With very best wishes and many thanks in advance, 
Leonardo
  </blockquote>
</aside>

<p>Also either the paper or the thesis will have detailed information about the smoothing applied during conversion:</p>
<p>Pinter, C., Lasso, A., &amp; Fichtinger, G. (2019). Polymorph segmentation representation for medical image computing. Computer Methods and Programs in Biomedicine, 171, 19–26. <a href="https://doi.org/10.1016/j.cmpb.2019.02.011" class="inline-onebox">Redirecting</a><br>
(<a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf">https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf</a>)</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://qspace.library.queensu.ca/handle/1974/26422">
  <header class="source">
      <img src="https://qspace.library.queensu.ca/handle/1974/assets/atmire/images/favicon.png" class="site-icon" width="" height="">

      <a href="https://qspace.library.queensu.ca/handle/1974/26422" target="_blank" rel="noopener">qspace.library.queensu.ca</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://qspace.library.queensu.ca/handle/1974/26422" target="_blank" rel="noopener">Dynamic Representation of Anatomical Structures in Radiation Therapy...</a></h3>

  <p>Segmentation is a ubiquitous operation in radiation therapy (RT) and in medical image computing (MIC) in general. Various data representations can describe segmentation results, such as binary volumes or surface models. Conversions between them are...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let us know if you still haven’t found the answer you’re looking for.</p>

---
