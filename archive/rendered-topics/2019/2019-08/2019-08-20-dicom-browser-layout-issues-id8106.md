---
topic_id: 8106
title: "Dicom Browser Layout Issues"
date: 2019-08-20
url: https://discourse.slicer.org/t/8106
---

# DICOM browser layout issues

**Topic ID**: 8106
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/dicom-browser-layout-issues/8106

---

## Post #1 by @cpinter (2019-08-20 18:26 UTC)

<p>I found an issue with the new DICOM browser, and thought that we need a place to discuss these (from my experience there are always a few issues after major changes). Since the PR is closed, we can track the issues on Mantis, but I think we could use discourse for related discussions.</p>
<p>So the one I found is about the browser disappearing after a successful load (<a href="https://issues.slicer.org/view.php?id=4705" rel="nofollow noopener">here’s the issue</a>). The DICOM browser itself disappears from the layout, which becomes white and the “DICOM database” label shifts to the middle. The “Show DICOM database browser” button remains toggled, but does not have any effect. To make it reappear, need to switch to another layout then press the show button.</p>
<p>I also have a question: if I remember correctly we wanted to keep the popup style browser as an option but I can’t find it in Application Settings. Is it there programmatically just not exposed?</p>

---

## Post #2 by @Sunderlandkyl (2019-08-20 18:43 UTC)

<p>It doesn’t seem to happen with all datasets.<br>
Behavior is fine when loading CT/RTDose volumes, but the issue occurs when loading RTStruct.</p>
<p>I’ll compile SlicerRT and debug the problem.</p>

---

## Post #3 by @cpinter (2019-08-20 18:45 UTC)

<p>Thanks, Kyle! There are no errors (only the usual warnings about geometry and empty structures), so I did not assume it was due to RTSS. I wonder what it can be…</p>

---

## Post #4 by @JanWitowski (2019-08-20 18:58 UTC)

<p>I have encountered different DICOM Browser issue recently, not sure if I should report it here or on an issue tracker?</p>
<p>After importing one dataset, series description got multiplied in some series, resulting in destroying the layout of whole browser:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98a796c6a3ca220f388ea7411a79f6217cc20b37.png" data-download-href="/uploads/short-url/lMrDg5pPUrgHcwf9xDdZUu24g0T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98a796c6a3ca220f388ea7411a79f6217cc20b37_2_690x114.png" alt="image" data-base62-sha1="lMrDg5pPUrgHcwf9xDdZUu24g0T" width="690" height="114" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98a796c6a3ca220f388ea7411a79f6217cc20b37_2_690x114.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98a796c6a3ca220f388ea7411a79f6217cc20b37_2_1035x171.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98a796c6a3ca220f388ea7411a79f6217cc20b37_2_1380x228.png 2x" data-dominant-color="E8ECF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2334×388 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Even though the metadata series description seems fine:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c660d3f24f32630149d067e1963d9a0c62b89e48.png" data-download-href="/uploads/short-url/siVZvfWBX2GTaadPDxCMRjfjTOo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c660d3f24f32630149d067e1963d9a0c62b89e48.png" alt="image" data-base62-sha1="siVZvfWBX2GTaadPDxCMRjfjTOo" width="690" height="57" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">786×66 3.12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can try to upload an anonymized dataset if that helps</p>

---

## Post #5 by @cpinter (2019-08-20 19:00 UTC)

<p><a class="mention" href="/u/janwitowski">@JanWitowski</a> I fixed this last week. If you download a recent nightly, then this issue will not occur. You will need to re-import the dataset (or re-update the database if it was from an old one).</p>

---

## Post #6 by @JanWitowski (2019-08-20 19:11 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>, reloaded the study and it’s fixed!</p>

---

## Post #7 by @Sunderlandkyl (2019-08-20 19:54 UTC)

<p>The issue with the DICOM browser layout dissapearing should be fixed in this PR: <a href="https://github.com/Slicer/Slicer/pull/1200" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1200</a></p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> To answer your previous question about the option for the popup style, we decided to only allow the DICOM browser layout rather than complicate things by maintaining both options.</p>

---

## Post #8 by @cpinter (2019-08-21 14:54 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="7" data-topic="8106">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>only allow the DICOM browser layout rather than complicate things by maintaining both options</p>
</blockquote>
</aside>
<p>Interesting. We usually decide to “complicate things” when we introduce a big change like this. Many users will want their popups I’m sure. But I guess we’ll see.</p>

---

## Post #9 by @lassoan (2019-08-21 15:21 UTC)

<p>In your own module you can still show the widget in a popup. Also, it will be possible to show the DICOM browser view on a secondary screen or floating panel when we implement multi-display layouts.</p>

---

## Post #10 by @cpinter (2019-08-21 15:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="8106">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>when we implement multi-display layouts</p>
</blockquote>
</aside>
<p>Yes, that will be the proper solution, but realistically that may be a year from now.<br>
I personally like the browser in the layout.</p>

---
