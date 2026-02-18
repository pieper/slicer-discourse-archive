# Unable to paint under rhe segmentation module

**Topic ID**: 33526
**Date**: 2023-12-27
**URL**: https://discourse.slicer.org/t/unable-to-paint-under-rhe-segmentation-module/33526

---

## Post #1 by @Michelle_Cataldo (2023-12-27 01:03 UTC)

<p>Hello guys, 'im trying to paint the area on the ROI I determined but, it wont segment the area. it “erase” itself whenever I stop holding and dragging the mouse. I cant draw anything too. I could segment without problems before.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b791ce48c8471e6031c6631ed6a84fcbe2e2c1c.mp4">
  </div><p></p>
<p>Can someone guide me so i can start my segmentation?<br>
Thanks in advance.</p>

---

## Post #2 by @muratmaga (2023-12-27 01:37 UTC)

<p>Please read these two threads:</p><aside class="quote quote-modified" data-post="5" data-topic="33166">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/could-someone-help-me-about-segmentation/33166/5">Could someone help me about segmentation?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It looks like you may be working with data in a Sequence (judging by the Sequence Browser toolbar in your screenshots).  This can be confusing until you understand how the Sequence system is set up and the relationships between Sequences, Sequence Browsers, and Proxy Nodes work.  I am guessing that you may want to perform a segmentation on each frame of a sequence of images; if so, it might be helpful to follow the sequence of steps here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#create-a-segmentation-node-sequence">https://slicer.readthedocs.io/en/latest/user_guide/module…</a>
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="5" data-topic="28642">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-using-paint-the-bulb-of-paint-disappears-instead-of-remaining/28642/5">Segmentation, using paint, the bulb of paint disappears instead of remaining</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    To understand what’s going on and why it is happening try these steps: 

Download MRHead and CT Chest sample datasets
Right click on MRHead and choose “segment this”
Create a single segment, and paint somewhere with a paint brush.
While in segment editor, switch Source Volume from MRHead to CTChest
Try to paint any region using Segment_1 and notice that everything you paint immediately disappears.

 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/858120d3908e2f53ef0d2579f8adbd6b13fce352.png" data-download-href="/uploads/short-url/j329TcJWRjMValevdrS0QeffJJ0.png?dl=1" title="image">[image]</a> 
That’s because segmentation geometry is determined by the physical extends of the first …
  </blockquote>
</aside>


---

## Post #3 by @Michelle_Cataldo (2023-12-27 01:59 UTC)

<p>Thank you!<br>
The second post was the solution to my problem <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
