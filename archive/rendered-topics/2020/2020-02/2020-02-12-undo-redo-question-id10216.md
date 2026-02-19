---
topic_id: 10216
title: "Undo Redo Question"
date: 2020-02-12
url: https://discourse.slicer.org/t/10216
---

# Undo/Redo question

**Topic ID**: 10216
**Date**: 2020-02-12
**URL**: https://discourse.slicer.org/t/undo-redo-question/10216

---

## Post #1 by @Davide_Punzo (2020-02-12 13:18 UTC)

<p>Hi all,</p>
<p>I just wanted to ask if there are plans/news regarding the Undo/Redo mechanism respect to <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Undo.2FRedo" rel="nofollow noopener">Roadmap</a>.<br>
Is there also a wiki page that explain/summarize the current mechanism (I could not find in the developer manual)?</p>

---

## Post #2 by @pieper (2020-02-12 14:32 UTC)

<p>Hi <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> - there are some very old slides that describe the original undo/redo design in MRML (e.g. the last two slides of <a href="https://www.slideserve.com/awena/slicer3-architecture">this deck</a>).  I think a lot of the issue that caused us to turn it off have long since been addressed, since they also caused problems loading scenes.  Hopefully in current Slicer any state changes in the scene are handled well by the gui and views.  I guess <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> have looked at it more recently and can probably tell us if they are able to use the old design or have something new in mind.</p>

---

## Post #3 by @Davide_Punzo (2020-02-20 07:35 UTC)

<p>For reference, I think this is the git commit where Kyle and Andras fixed undo/redo: <a href="https://github.com/Slicer/Slicer/commit/8352f2e13764e422ddaf722bfb05317db4f38eb1" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/8352f2e13764e422ddaf722bfb05317db4f38eb1</a></p>

---
