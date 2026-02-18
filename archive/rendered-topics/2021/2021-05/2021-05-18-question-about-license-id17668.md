# Question about license

**Topic ID**: 17668
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/question-about-license/17668

---

## Post #1 by @GRChoi (2021-05-18 04:51 UTC)

<p>Hi everyone,<br>
I am interested in building Slicer in Windows.<br>
I read build instruction and I found something weird.<br>
Slicer build requires QT 5, and QT is (L)GPL license.<br>
As I know, (L)GPL is infectious which makes referencing projects (L)GPL license projects, but Slicer is BSD license.<br>
How is it possible?</p>
<p>Thanks for your help. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2021-05-18 04:56 UTC)

<p>GPL is viral, but LGPL is not.</p>
<p>The only restrictions of using Qt with LGPL license are that:</p>
<ol>
<li>you are not allowed to link Qt to Slicer statically</li>
<li>if you modify Qt’s source code then you need to contribute back your changes to Qt</li>
</ol>
<p>None of these are an issue.</p>

---

## Post #3 by @GRChoi (2021-05-18 05:03 UTC)

<p>Thanks for your reply!</p>

---
