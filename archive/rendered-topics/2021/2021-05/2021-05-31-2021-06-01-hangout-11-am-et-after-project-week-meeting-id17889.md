---
topic_id: 17889
title: "2021 06 01 Hangout 11 Am Et After Project Week Meeting"
date: 2021-05-31
url: https://discourse.slicer.org/t/17889
---

# 2021.06.01 Hangout - 11 AM ET after Project Week Meeting

**Topic ID**: 17889
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/2021-06-01-hangout-11-am-et-after-project-week-meeting/17889

---

## Post #1 by @Sam_Horvath (2021-05-31 22:54 UTC)

<p>Tomorrow, we will be having our next weekly hangout at 11:00 AM ET, after the <a href="https://discourse.slicer.org/t/reminder-project-week-prep-meeting-tomorrow-june-1-2021/17888">Project Week meeting </a>. We will be remaining on the Project Week Zoom call for the hangout.</p>
<p>Anyone is welcome to join to ask questions!</p>
<p>Agenda:</p>
<ul>
<li>Slicer 5</li>
<li>Extension manager</li>
</ul>
<p>Feel free to post to this thread to request/suggest a topic!</p>
<p>Thanks<br>
Sam and J-Christophe</p>

---

## Post #2 by @smrolfe (2021-06-01 17:07 UTC)

<p>Following up on our conversation, I’m sharing a <a href="https://drive.google.com/file/d/19lnpVCG8elu4QBDEVpfy7lPhht0gR4Of/view?usp=sharing" rel="noopener nofollow ugc">short screen recording</a> showing showing node creation and placement node selection from the in-progress Markups toolbar. Following advice from <a class="mention" href="/u/lassoan">@lassoan</a>, this will be updated to use the existing Simple Markups widget, with modified persistence options.</p>

---

## Post #3 by @lassoan (2021-06-01 17:27 UTC)

<p>The <code>qSlicerSimpleMarkupsWidget</code> contains a node selector and a control point list. The node selector could be fine, but probably we don’t want a control point list in the toolbar. So, probably the <code>qSlicerMarkupsPlaceWidget()</code> would be a more suitable choice (which does not contain a node selector and control point list).</p>

---
