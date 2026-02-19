---
topic_id: 16717
title: "Mapping Electromagnetic Tracking Error"
date: 2021-03-23
url: https://discourse.slicer.org/t/16717
---

# Mapping electromagnetic tracking error

**Topic ID**: 16717
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/mapping-electromagnetic-tracking-error/16717

---

## Post #1 by @marco.cavaliere (2021-03-23 12:04 UTC)

<p>Hi,</p>
<p>I’m trying to visualize the position error between 2 tracking systems (electromagnetic and optical) in Slicer, as it is done in this paper <a href="https://doi.org/10.1117/12.2082330" rel="noopener nofollow ugc">https://doi.org/10.1117/12.2082330</a></p>
<p>I’m following this tutorial<br>
<a href="https://onedrive.live.com/view.aspx?cid=7230d4dec6058018&amp;page=view&amp;resid=7230D4DEC6058018!5624&amp;parId=7230D4DEC6058018!2937&amp;authkey=!AGQkSCZOwjVYXw8&amp;app=PowerPoint" rel="noopener nofollow ugc">SlicerIGT-U19_EmFieldDistorition.pptx - Microsoft PowerPoint Online (live.com)</a></p>
<p>but the module required is not loaded correctly.</p>
<p>Thank you,<br>
Marco</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: Position Error Tracking module<br>
Actual behavior: module failed to load</p>

---

## Post #2 by @lassoan (2021-03-24 17:21 UTC)

<p>We have not tested this module with latest Slicer versions, but if there are failures then it is most likely due to slight Python2/3 syntax and Slicer API changes, which should be easy to address. Have a look at the Python console (Ctrl-3) for errors and try to fix them. If you get stuck with any specific errors then let us know.</p>

---
