---
topic_id: 8609
title: "Capture Scene Layout Is Broken In Later Nightlies"
date: 2019-09-29
url: https://discourse.slicer.org/t/8609
---

# Capture scene layout is broken in later nightlies

**Topic ID**: 8609
**Date**: 2019-09-29
**URL**: https://discourse.slicer.org/t/capture-scene-layout-is-broken-in-later-nightlies/8609

---

## Post #1 by @muratmaga (2019-09-29 06:03 UTC)

<p>It take a blank screen captuure, and also saves it as a model node in the subject hierarchy. There is also this error message:</p>
<p>“class QColor __cdecl qSlicerSubjectHierarchyModelsPlugin::getDisplayColor(__int64,class QMap&lt;int,class QVariant&gt; &amp;) const : No display node for model”</p>
<p>This going back at least a week.</p>

---

## Post #2 by @pieper (2019-09-30 12:36 UTC)

<p>Do you mean the SceneViews?  Something is screwed up there.  For me the image is upside down and the colors are wrong, but I don’t get that error message.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeb59a916d5d112f99f6e81969146525f6cbb676.png" alt="image" data-base62-sha1="y3IIMqd7165VUY7R5EoB5mS2Z4W" width="272" height="206"></p>

---

## Post #3 by @muratmaga (2019-09-30 17:09 UTC)

<p>Yes, on linux I got wrong colors, and cut/flipped images. On windows I get the error message, and captured images are blank (or rather full black) and I get the error message.</p>
<p>also captured images shows as models in the subject hierarchy, which is confusing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b8d0c91f1aedef41e41fe2072668400168c29b6.png" data-download-href="/uploads/short-url/3VJ5sj4UptRZ9BpuxSsSFPoTZxs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b8d0c91f1aedef41e41fe2072668400168c29b6_2_690x228.png" alt="image" data-base62-sha1="3VJ5sj4UptRZ9BpuxSsSFPoTZxs" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b8d0c91f1aedef41e41fe2072668400168c29b6_2_690x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b8d0c91f1aedef41e41fe2072668400168c29b6_2_1035x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b8d0c91f1aedef41e41fe2072668400168c29b6.png 2x" data-dominant-color="E7EFF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×364 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2019-09-30 18:48 UTC)

<p>Thanks for reporting this! Looks like something to do with the latest SH hiccups. See for example <a href="https://github.com/Slicer/Slicer/pull/1215" rel="nofollow noopener">this PR</a>.</p>

---

## Post #5 by @Fernando (2019-10-06 18:44 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="8609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For me the image is upside down and the colors are wrong, but I don’t get that error message.</p>
</blockquote>
</aside>
<p>I’ve been having this issue too. Until it’s solved, it should work if you click on the radio buttons a couple of times.</p>

---

## Post #6 by @pieper (2019-10-07 00:20 UTC)

<p>Should be fixed now: <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28535" rel="nofollow noopener">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28535</a></p>

---
