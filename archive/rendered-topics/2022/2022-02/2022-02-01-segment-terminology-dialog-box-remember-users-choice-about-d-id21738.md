---
topic_id: 21738
title: "Segment Terminology Dialog Box Remember Users Choice About D"
date: 2022-02-01
url: https://discourse.slicer.org/t/21738
---

# Segment terminology dialog box: remember user's choice about displaying advanced terminology

**Topic ID**: 21738
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/segment-terminology-dialog-box-remember-users-choice-about-displaying-advanced-terminology/21738

---

## Post #1 by @chribaue (2022-02-01 19:32 UTC)

<p>I have a request regarding the dialog box used to edit “color and terminology codes” of segments.</p>
<p>In modules “Segmentations” and “Segment Editor” a double click on the color opens the following dialog:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88fee3cf39c8c88730a279ef2373e37ea1709442.png" alt="image" data-base62-sha1="jxV2aF6YxXVAtFBIbmRjeCyN0Xw" width="224" height="290"><br>
with the left and right arrows opening more details for terminology:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c4fb3598ab3ac19578fcb014d0034623557efe7.png" alt="image" data-base62-sha1="hJHXLOuJnKK3C7ZGUOeW0rTbA6H" width="228" height="294"></p>
<p>Per default, in older Slicer versions it used to look like this right after double clicking the color button.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ab7d9017f765d72e71e36110d6403a84d65322f.png" data-download-href="/uploads/short-url/1wOFkbeoWptP2u7V0qrBOQuyV43.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab7d9017f765d72e71e36110d6403a84d65322f_2_517x252.png" alt="image" data-base62-sha1="1wOFkbeoWptP2u7V0qrBOQuyV43" width="517" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab7d9017f765d72e71e36110d6403a84d65322f_2_517x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab7d9017f765d72e71e36110d6403a84d65322f_2_775x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ab7d9017f765d72e71e36110d6403a84d65322f.png 2x" data-dominant-color="D2DADE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">895×437 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In addition, even after switching to the expanded view, every time a user double clicks the color button to edit terminology, it opens the dialog box again without displaying the more detailed terminology areas.</p>
<p>I guess the advanced options are hidden now by default, because it might confuse novice users. But for use cases, where users need to use the more advanced options several times, these additional clicks and resizing the window becomes very tedious.</p>
<p>It would be great if Slicer would remember the user’s choice about having the “Segmentation Category” and “Anatomic region” area open or not and open the window with proper width right away.</p>

---

## Post #2 by @lassoan (2022-02-02 04:43 UTC)

<p>Indeed, we hide these sections to avoid overwhelming users. Restore the last state would not interfere with this much and would save the user a click, so it makes sense. I’ve pushed a commit with this change, it’ll be available in the Slicer Preview Release from the day after tomorrow.</p>

---

## Post #3 by @cpinter (2022-02-02 11:23 UTC)

<p>This is great <a class="mention" href="/u/lassoan">@lassoan</a> ! I just thought about this the other day that it would be nice, when I was setting terms from a context different from the default in many segments.</p>

---

## Post #4 by @chribaue (2022-02-02 13:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Good that you agree. And great that you even implemented it so quickly!</p>
<p>Thank you!</p>

---

## Post #5 by @lassoan (2023-03-21 01:57 UTC)



---
