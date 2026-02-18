# Issue on Slicer UI in Windows10 - green stripes

**Topic ID**: 17232
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/issue-on-slicer-ui-in-windows10-green-stripes/17232

---

## Post #1 by @om-ganesh (2021-04-21 16:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bcf72b0a0c8f17a236dda56593284bdb3c6080b.png" data-download-href="/uploads/short-url/d6bU7gOUweAMUAXrIHTv6QyFNwL.png?dl=1" title="slicer-4112" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bcf72b0a0c8f17a236dda56593284bdb3c6080b_2_690x428.png" alt="slicer-4112" data-base62-sha1="d6bU7gOUweAMUAXrIHTv6QyFNwL" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bcf72b0a0c8f17a236dda56593284bdb3c6080b_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bcf72b0a0c8f17a236dda56593284bdb3c6080b_2_1035x642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bcf72b0a0c8f17a236dda56593284bdb3c6080b_2_1380x856.png 2x" data-dominant-color="80B892"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer-4112</span><span class="informations">1549×962 80.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not able to load the Slicer3D in Windows10. I am having the weird UI issues as shown in snapshot. I tried fresh installation with both versions 4.10.2 and the latest stable 4.11.2. Any community members have this issue observed? If not, what could be the possible reason?</p>

---

## Post #2 by @pieper (2021-04-21 16:51 UTC)

<p>This is a driver issue - see this thread for example:</p>
<aside class="quote quote-modified" data-post="9" data-topic="12543">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-opening-screen-error-green-stripes/12543/9">Slicer opening screen error - Green Stripes</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Note that seems to happen with other software, too, such as Adobe After Effects: 
 <a class="lightbox" href="https://community.adobe.com/t5/image/serverpage/image-id/109601i940D191F3057EA10/image-size/large?v=1.0&amp;px=999" title="">[image]</a> 
(source: <a href="https://community.adobe.com/t5/after-effects/a-bunch-of-horizontal-green-lines-won-t-go-away-on-my-composition-screen-when-i-open-up-any-video/td-p/11223965?page=1">https://community.adobe.com/t5/after-effects/a-bunch-of-horizontal-green-lines-won-t-go-away-on-my-composition-screen-when-i-open-up-any-video/td-p/11223965?page=1</a>) 
There are lots of complaints for this latest Intel graphics driver causing these green horizontal lines appear in various software  - see these: <a href="https://www.reddit.com/r/premiere/comments/gzk1r8/how_can_i_solve_this_problem_black_and_green/">1</a>, <a href="https://adobe-video.uservoice.com/forums/911311-after-effects/suggestions/40712056-green-horizontal-lines-in-preview-of-ae-and-premie">2</a>, <a href="https://community.adobe.com/t5/premiere-pro/green-horizontal-lines-amp-distorted-colors/td-p/11188074?page=1">3</a>, <a href="https://community.adobe.com/t5/premiere-pro/green-horizontal-lines-in-my-source-monitor-please-help/td-p/11214905?page=1">4</a>, <a href="https://community.adobe.com/t5/after-effects/a-bunch-of-horizontal-green-lines-won-t-go-away-on-my-composition-screen-when-i-open-up-any-video/td-p/11223965?page=1">5</a>. 
Recommended solution there is to either upgrade or downgrade your graphi…
  </blockquote>
</aside>


---
