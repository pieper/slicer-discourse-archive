---
topic_id: 16596
title: "Apply Button For Scissor Tool Missing"
date: 2021-03-17
url: https://discourse.slicer.org/t/16596
---

# apply button for scissor tool missing?

**Topic ID**: 16596
**Date**: 2021-03-17
**URL**: https://discourse.slicer.org/t/apply-button-for-scissor-tool-missing/16596

---

## Post #1 by @rebecca-green (2021-03-17 14:33 UTC)

<p>Hi, I am on 4.11.20210226 and it seems the apply button for the scissors tool is now missing? I can set my area, but then I can’t do anything with it. All the tutorials seem to show an apply button. Am I missing something?</p>

---

## Post #2 by @lassoan (2021-03-17 14:37 UTC)

<p>Scissors effect does not have an Apply button, it is applied immediately when you release the mouse button. “Surface cut” effect is somewhat similar and it has an Apply button, maybe you saw that in tutorials.</p>

---

## Post #3 by @muratmaga (2021-03-17 19:29 UTC)

<p><a class="mention" href="/u/rebecca-green">@rebecca-green</a> just to make sure your active tools  is scissor, this is what you should be seeing:<br>
There is no Apply button.</p>
<p>                    <a href="https://raw.githubusercontent.com/SlicerMorph/Spr_2021/main/Day_2/Segmentation/images/Slide16.PNG" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/SlicerMorph/Spr_2021/main/Day_2/Segmentation/images/Slide16.PNG" width="666" height="500">
          </a>

</p>

---

## Post #4 by @rebecca-green (2021-03-17 19:31 UTC)

<p>Figured out the problem! I hadn’t properly created a mask of the surface first!</p>

---

## Post #5 by @muratmaga (2021-03-17 19:32 UTC)

<aside class="quote no-group" data-username="rebecca-green" data-post="4" data-topic="16596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rebecca-green/48/10329_2.png" class="avatar"> rebecca-green:</div>
<blockquote>
<p>! I hadn’t properly created a mask of the surface first!</p>
</blockquote>
</aside>
<p>Yes, you have to have an initial segment for scissors to cut from.</p>

---
