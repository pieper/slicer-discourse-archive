# Segmentations/Segment Editor - toggle visibility for all segments

**Topic ID**: 4706
**Date**: 2018-11-09
**URL**: https://discourse.slicer.org/t/segmentations-segment-editor-toggle-visibility-for-all-segments/4706

---

## Post #1 by @fedorov (2018-11-09 19:32 UTC)

<p>When I load a reasonably large number of segments, I find it useful to visualize one segment at a time.</p>
<p>It would be very helpful if it was possible to toggle visibility of all segments at once, since otherwise they need to be toggled one at a time, and I encountered segmentations that contain hundreds of segments.</p>
<p>Perhaps a button could be added to the table header to do that.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c1fc685007438808cadfa46764e233744b4dddb.png" alt="image" data-base62-sha1="aRqmIm9GdtcLURZpcwGcsoEg0MX" width="109" height="157"></p>

---

## Post #2 by @lassoan (2018-11-09 20:13 UTC)

<p>You can right-click on a segment and choose “Show only selected segments”. In lists where multiple selection is allowed (e.g., in Segments module) you can show all selected segments at once, while hiding all the others.</p>

---

## Post #3 by @NoobForSlicer (2021-05-21 07:56 UTC)

<p>thank you Lassoan, I am going through your replies and learning about all the features &lt;3 thank you so much</p>
<p>we remain thankful<br>
students</p>

---

## Post #4 by @mrrezaie (2022-10-25 08:48 UTC)

<p>Hi,</p>
<p>It would be great if there are buttons for turning the visibility on/off for all, in Segment Editor, Segmentations, Markups, and Data modules, the same as Models:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8776d3a44639c5f3a2594113a69f34c55a033ddf.png" alt="image" data-base62-sha1="jkn2HA3mG9iwsbFfRMmW9Y21S0L" width="440" height="191"></p>
<p>It will come in handy.</p>

---

## Post #5 by @pieper (2022-10-25 12:22 UTC)

<p>In the Data module you can select a set of segments and toggle visibility with the context menu (right click).</p>

---

## Post #6 by @SummerZ2020 (2025-02-18 05:15 UTC)

<p>Hi Pieper,<br>
Is it still in the version 5.6.2. I did not find any option can toggle visibility of the set of segment. Here is my right click menu in the Data Module.<br>
Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc0117caf786e00730f864641c870a3ff642d444.png" data-download-href="/uploads/short-url/zXkFb3PfyyWKRLudUgTbZHTyMfy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc0117caf786e00730f864641c870a3ff642d444.png" alt="image" data-base62-sha1="zXkFb3PfyyWKRLudUgTbZHTyMfy" width="265" height="235"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">265×235 2.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2025-02-18 05:24 UTC)

<p>You don’t need the right-click, visibility is shown as an icon (eye). Click on it to toggle from visible to invisible.</p>

---

## Post #8 by @pieper (2025-02-18 12:32 UTC)

<p>You can toggle selected segments with the context menu like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f99faa0ecece9812a0ab35787f6225b0667618a8.png" data-download-href="/uploads/short-url/zCgY5ZQtWpMoiAsU078TsxURQne.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f99faa0ecece9812a0ab35787f6225b0667618a8_2_690x329.png" alt="image" data-base62-sha1="zCgY5ZQtWpMoiAsU078TsxURQne" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f99faa0ecece9812a0ab35787f6225b0667618a8_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f99faa0ecece9812a0ab35787f6225b0667618a8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f99faa0ecece9812a0ab35787f6225b0667618a8.png 2x" data-dominant-color="BDD2ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">826×394 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @fedorov (2025-02-18 15:12 UTC)

<p>Related open issue here: <a href="https://github.com/Slicer/Slicer/issues/8190" class="inline-onebox">Segment visibility toggle in Data and Segmentations modules · Issue #8190 · Slicer/Slicer · GitHub</a>.</p>
<p>If you are a user not happy with the current behavior, please add your voice to that issue!</p>

---
