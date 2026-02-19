---
topic_id: 24923
title: "How To Do Online Real Time Annotation When Recording A New S"
date: 2022-08-25
url: https://discourse.slicer.org/t/24923
---

# How to do online (real-time) annotation when recording a new sequence of ultrasound stream using the module "Sequences"?

**Topic ID**: 24923
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/how-to-do-online-real-time-annotation-when-recording-a-new-sequence-of-ultrasound-stream-using-the-module-sequences/24923

---

## Post #1 by @sunshine (2022-08-25 19:24 UTC)

<p>Hi everyone,</p>
<p>This topic is to continue a question from</p><aside class="quote quote-modified" data-post="3" data-topic="24895">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3ec8ea/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-dynamically-update-the-stringname-of-parameternode/24895/3">How to dynamically update the StringName of ParameterNode?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Andras, 
Thank you so much for your help! 
I found the attribute “selectedItemNumber” from vtkMRMLSequenceBrowserNode in the scene file, which solved my problem. 
As you can see in the screenshot below, I am now able to retrieve SequenceBrowser and show the FrameIndex in my own module, and I should also be able to do offline annotation now. 
[image] 
However, it might be impossible for me to complete a new “Sequences” module for the new sequence recording, and it seems that the existing “Sequ…
  </blockquote>
</aside>

<p>I am trying to design my first extension module, similar to the module “Sequences” but with real-time frame annotations from AI image processing for live ultrasound sequence collection.</p>
<p>As you can see in the screenshot below, I am now able to retrieve SequenceBrowser and show the FrameIndex in my own module, and I should also be able to do <strong>offline</strong> annotation now.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b.png" data-download-href="/uploads/short-url/7UTKB1ankRruXMSJv5BISQYs3Uf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b_2_690x298.png" alt="image" data-base62-sha1="7UTKB1ankRruXMSJv5BISQYs3Uf" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/377dc8ab7965659ecc9efe1fbd99745a6898e18b.png 2x" data-dominant-color="A09F9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">998×432 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, it might be impossible for me to complete a new “Sequences” module for the new sequence recording, and it seems that the existing “Sequences” module does not support PyQt5 script source code.</p>
<p>What should I do to make the annotation <strong>online</strong>?<br>
E.g., after I click the recording button in the “Sequences” module to record a sequence of ultrasound data, as the real-time raw image shown in the red widget, how should I annotate a “Yes” notation in the center of the raw image and show the annotated image in the yellow widget simultaneously?</p>
<p>Assume this problem can be solved in three steps:</p>
<ol>
<li>How can I add a new shortcut button in the toolbar to trigger the annotation?</li>
<li>How should I retrieve the real-time raw image?</li>
<li>How should I display the annotated image in the yellow widget?</li>
</ol>
<p>Thank you again for your valuable time!</p>

---
