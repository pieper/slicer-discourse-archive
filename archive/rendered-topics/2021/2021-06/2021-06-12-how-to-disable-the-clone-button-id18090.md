# How to disable the clone button?

**Topic ID**: 18090
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/how-to-disable-the-clone-button/18090

---

## Post #1 by @OpenSource_Contri (2021-06-12 08:56 UTC)

<p><a class="mention" href="/u/simonoxen">@simonoxen</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
I have explored these options but I wanted to <strong>disable clone button</strong>. How to go ahead with this?</p>

---

## Post #2 by @lassoan (2021-06-12 12:02 UTC)

<p>Which clone button do you mean? The Clone action in the right-click menu in Data module that duplicates the selected node? Why would you like to disable this option? What is your overall goal?</p>

---

## Post #3 by @OpenSource_Contri (2021-06-12 14:09 UTC)

<p><strong>Clone Button screenshot has been attached.</strong></p>
<p>I wanted to make a clone button there with same functionalities.</p>
<p>Now, It is by right clicking but I want to create a separate button for the same.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/403e0c0967f93410716580ded7d2ea13e98b2e66.png" data-download-href="/uploads/short-url/9ajuzZccmCne23SKSVSJs3Xvldk.png?dl=1" title="Screenshot (218)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/403e0c0967f93410716580ded7d2ea13e98b2e66_2_320x500.png" alt="Screenshot (218)" data-base62-sha1="9ajuzZccmCne23SKSVSJs3Xvldk" width="320" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/403e0c0967f93410716580ded7d2ea13e98b2e66_2_320x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/403e0c0967f93410716580ded7d2ea13e98b2e66_2_480x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/403e0c0967f93410716580ded7d2ea13e98b2e66.png 2x" data-dominant-color="2D3033"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (218)</span><span class="informations">504×787 27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-06-12 14:37 UTC)

<p>Adding a Clone button is a completely different question. That is discussed in <a href="https://discourse.slicer.org/t/is-there-an-option-to-duplicate-a-segment/18074/6">another topic</a>.</p>
<p>You wrote above that “I wanted to disable clone button”. Would you like to remove (or disable) the “Clone” action in the right-click menu in DICOM module? What is the reason for that? What is your end goal?</p>

---

## Post #5 by @OpenSource_Contri (2021-06-12 15:12 UTC)

<p>I wanted to disable clone button because I want to add a clone button with same functionalities so that It is visible there. Currently It is there but we have to “Right Click.”.</p>

---

## Post #6 by @lassoan (2021-06-12 17:14 UTC)

<p>Why do you need to hide the “Clone” action from the right-click menu? What harm does its presence cause in your workflow?</p>

---

## Post #7 by @OpenSource_Contri (2021-06-12 17:58 UTC)

<p>It doesn’t harm anything but if we put this button just beside the particular segment (whom we want to clone)  then, I think it would be better option.</p>

---

## Post #8 by @OpenSource_Contri (2021-06-12 18:08 UTC)

<p>This is the reason I want to disable right click clone button and create same clone button just besides particular segment.</p>

---

## Post #9 by @lassoan (2021-06-12 19:19 UTC)

<p>Do you mean that you would like to make it easy to clone a selected segment instead of a complete segmentation?</p>
<p>Can you describe your complete workflow? There are so many different solutions for this that it would be very important to know what your end goal is, so that we can give advice or implement improve Slicer core in a way that best serves your end goal and can be generalized to other workflows.</p>

---

## Post #10 by @OpenSource_Contri (2021-06-14 07:12 UTC)

<p>Yes, I want to make it easy for the other to clone particular segment. As there is button to add segment and remove segment, I think it is very much helpful when there will be button for clone particular segment. Other will not have to explore “how to clone” because of separate button for clone.<br>
My workflow is to make easily accessible user interface for other.</p>

---

## Post #11 by @lassoan (2021-06-25 21:11 UTC)

<p>I’ve updated the “Clone” action to clone a segment if you right-click on a segment, and clone the entire segmentation if you right-click on the segmentation.</p>

---
