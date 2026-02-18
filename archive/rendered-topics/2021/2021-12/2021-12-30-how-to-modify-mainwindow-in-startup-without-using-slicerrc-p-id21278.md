# How to modify mainwindow in startup without using .slicerrc.py file

**Topic ID**: 21278
**Date**: 2021-12-30
**URL**: https://discourse.slicer.org/t/how-to-modify-mainwindow-in-startup-without-using-slicerrc-py-file/21278

---

## Post #1 by @Dwij_Mistry (2021-12-30 13:58 UTC)

<p>We are having <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">script repository</a> in Slicer which we have to keep in executable folder. (So while loading it will do the changes)</p>
<p>But I dont want to use rc file.<br>
Is there any method to call .py file in startup in the EXE. (Hard coded)</p>

---

## Post #2 by @jcfr (2021-12-30 14:04 UTC)

<p>You could manually edit the <code>NameOfYouAppLauncherSettings.ini</code> file and append <code>--python-script script.py</code></p>

---

## Post #3 by @Dwij_Mistry (2021-12-30 14:33 UTC)

<pre><code class="lang-auto">viewNode = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()
viewNode.SetBackgroundColor(0,0,0)
viewNode.SetBackgroundColor2(0,0,0)
viewNode.SetBoxVisible(0)
viewNode.SetAxisLabelsVisible(0)
</code></pre>
<p>Is there any way to directly use those functions?</p>

---
