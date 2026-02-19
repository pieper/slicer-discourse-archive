---
topic_id: 10848
title: "How To Export All Structures To Stl File"
date: 2020-03-26
url: https://discourse.slicer.org/t/10848
---

# How to export all structures to STL file?

**Topic ID**: 10848
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/how-to-export-all-structures-to-stl-file/10848

---

## Post #1 by @taehyeong_kim (2020-03-26 13:21 UTC)

<p>Hi everyone</p>
<p>I’ll ask you to how to export the dicom slice.</p>
<p>I implemented as follows.</p>
<ol>
<li>A Dicom file containing the structure(OAR, spinal cord, eye… etc) was imported into the 3D slicer from Varian Eclipse.</li>
<li>The segment editor confirmed that the structure was normally recalled.</li>
<li>Export to save the STL file and import the autodesk Netfabb</li>
<li>But In the loaded Dicom files, only the surface of the bones and body is visible, but no other structures are visible.!<br>
I’d like to print 3D like the attached picture (section), is there anything wrong with what I did? I’d like to hear your explanation in detail.</li>
</ol>
<p>I think it would be better to reply by e-mail. <a href="mailto:dnssll1009@naver.com">dnssll1009@naver.com</a><br>
<a href="/uploads/short-url/vQiCadvyjGiotTl7eCgAgpiMfMq.jpeg">2020-03-26_16-13-41|538x350</a></p>

---

## Post #2 by @lassoan (2020-03-26 13:42 UTC)

<p>For everyone’s benefit, please keep the discussion on the forum (not in private emails).</p>
<p>To improve the contrast of the loaded CT volume, adjust window/level by click-and-dragging with the left mouse in slice views. In recent Slicer Preview Releases, you need to to activate the window/level mouse mode first - see details here: <a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284" class="inline-onebox">Recent improvements in window/level management</a></p>

---
