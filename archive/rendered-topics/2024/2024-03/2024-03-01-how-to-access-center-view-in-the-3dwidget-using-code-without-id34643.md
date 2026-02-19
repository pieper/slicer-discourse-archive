---
topic_id: 34643
title: "How To Access Center View In The 3Dwidget Using Code Without"
date: 2024-03-01
url: https://discourse.slicer.org/t/34643
---

# How to access center view in the 3dwidget using code without pressing the center view option?

**Topic ID**: 34643
**Date**: 2024-03-01
**URL**: https://discourse.slicer.org/t/how-to-access-center-view-in-the-3dwidget-using-code-without-pressing-the-center-view-option/34643

---

## Post #1 by @ebin1234 (2024-03-01 11:53 UTC)

<p>How to access center view in the 3dwidget using code without pressing the center view option?.</p>

---

## Post #2 by @cpinter (2024-03-01 12:07 UTC)

<p>This is the simplest way I think</p>
<pre><code class="lang-auto">slicer.app.layoutManager().threeDWidget(0).threeDController().resetFocalPoint()
</code></pre>
<p>I checked and this can also be found in the script repository<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#center-the-3d-view-on-the-scene" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#center-the-3d-view-on-the-scene</a><br>
I encourage everyone to check there first for pieces of code.</p>

---

## Post #3 by @ebin1234 (2024-03-01 12:15 UTC)

<p>Thank You . It is working. I have a doubt in positioning the 3D view. If I want to place 3D view in anterior or posterior position . What I have to do using code?.</p>

---

## Post #4 by @jamesobutler (2024-03-01 12:29 UTC)

<p>You can review the API documentation associated with the 3D view the find all the various methods involved with that functionality. I’d suggest using that along with the script repository examples to help you learn how you would find how to do X functionality with the 3D view through Python.</p>
<p><a href="https://apidocs.slicer.org/main/classqMRMLThreeDView.html#a771517a8f8d6be954eab97e453b987e6" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/main/classqMRMLThreeDView.html#a771517a8f8d6be954eab97e453b987e6</a></p>

---

## Post #5 by @cpinter (2024-03-01 12:59 UTC)

<p>A relevant example:<br>
<code>threeDWidget.threeDController().lookFromAxis(ctk.ctkAxesWidget.Superior)</code></p>
<p>But I also suggest looking at the available functions instead of asking about them individually.</p>

---
