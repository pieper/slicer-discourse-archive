---
topic_id: 19360
title: "Is There Any Way To Programmatically Change Scissor Operatio"
date: 2021-08-25
url: https://discourse.slicer.org/t/19360
---

# Is there any way to programmatically change scissor operation in segment editor?

**Topic ID**: 19360
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-programmatically-change-scissor-operation-in-segment-editor/19360

---

## Post #1 by @akshay_pillai (2021-08-25 16:46 UTC)

<p>Is there any way to programmatically change the scissor operation in segment editor? As of right now the scissor operation removes everything in the enclosed area if it is selected in the segments list of the segment editor. I want to change this to also delete or remove another segment attached to the current  selected segment if it is enclosed in the area of the scissor. How can I do this? I hope its clear what I am asking.</p>

---

## Post #2 by @jamesobutler (2021-08-25 17:01 UTC)

<p>I was using latest Slicer Preview and there is a “Apply to all segments” option to erase inside for any segments inside the region.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e1c94ab1a1e23e4bfd76dc6cfebd9d92dfb14e7.png" alt="image" data-base62-sha1="myIFNUCaIjCNfm3UYvcFtAcBkUL" width="252" height="166"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70bdb9650c6177c67f4cbf4c43402790c9f23725.png" alt="image" data-base62-sha1="g5lXs37RANTIi9HXVMotGo4mvtj" width="215" height="209"></p>

---

## Post #3 by @akshay_pillai (2021-08-25 17:11 UTC)

<p>Ok, sounds good, ill try using the latest preview then.</p>

---

## Post #4 by @akshay_pillai (2021-08-25 17:44 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>  can you confirm the slicer version that you are using. I just downloaded the latest preview and I don’t see the “Apply to all segments” option. I was previously using 4.11.20200930 and the preview I just now downloaded is 4.13.0-2021-02-24/</p>

---

## Post #5 by @jamesobutler (2021-08-25 18:08 UTC)

<p>The latest preview build I tried is 4.13.0-2021-08-24 corresponding to today’s date. It looks like the version you are using is exactly 6 months old?</p>

---

## Post #6 by @rbumm (2021-08-31 20:30 UTC)

<p>I have 4.13.0-2021-08-24.exe here and<br>
“Apply to all segments” is - as previously implemented - in several segment editor functions.<br>
I can find it in “scissors” too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f62145771024f013df1960ca9a18c7d2ac1b864.png" data-download-href="/uploads/short-url/92Idk7djOtn7CgPQPDqfgEPjRD6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f62145771024f013df1960ca9a18c7d2ac1b864_2_449x500.png" alt="image" data-base62-sha1="92Idk7djOtn7CgPQPDqfgEPjRD6" width="449" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f62145771024f013df1960ca9a18c7d2ac1b864_2_449x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f62145771024f013df1960ca9a18c7d2ac1b864_2_673x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f62145771024f013df1960ca9a18c7d2ac1b864.png 2x" data-dominant-color="EDF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">719×800 53.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
