# "Liver vessel" task

**Topic ID**: 33203
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/liver-vessel-task/33203

---

## Post #1 by @Matteboo (2023-12-04 14:49 UTC)

<p>Hello,<br>
One month ago (13th of november) I used totalsegmentator to segment the blood vessel of a liver<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f44c43b4146a39397ecae59599733b92439e382.jpeg" data-download-href="/uploads/short-url/i9RYa34fkvwZXu5Jr1XSirGrWIa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f44c43b4146a39397ecae59599733b92439e382_2_690x400.jpeg" alt="image" data-base62-sha1="i9RYa34fkvwZXu5Jr1XSirGrWIa" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f44c43b4146a39397ecae59599733b92439e382_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f44c43b4146a39397ecae59599733b92439e382_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f44c43b4146a39397ecae59599733b92439e382_2_1380x800.jpeg 2x" data-dominant-color="585762"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1478×857 78.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
From memory, the task was called “liver vessel” on the slicer interface<br>
However, I can’t find that task anymore. I have updated totalsegmentator since and maybe the task was removed/fused with another task.<br>
If somebody know how to get resuls similar to the picture it would be very helpful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @Matteboo (2023-12-07 13:35 UTC)

<p>Hello again,</p>
<p>I found the cause of the issue.<br>
I have the “liver vessel” task on SLicer 5.4 but not on slicer 5.6<br>
I don’t know if this is because I messed up something with my installation or if this is normal</p>

---

## Post #4 by @rbumm (2023-12-07 14:24 UTC)

<p>5.6 uses Totalsegmentator V2, where liver vessels seem to no longer be supported. Maybe <a class="mention" href="/u/wasserth">@wasserth</a> can comment on the latest status.</p>

---

## Post #5 by @wasserth (2023-12-07 15:29 UTC)

<p>I did not have time yet to retrain the liver vessels on nnunet v2. Therefore they are missing in TotalSegmentator v2 so far.</p>

---
