---
topic_id: 18365
title: "Attributeerror Qmrmlnodecombobox Has No Attribute Named Setn"
date: 2021-06-28
url: https://discourse.slicer.org/t/18365
---

# AttributeError: qMRMLNodeComboBox has no attribute named 'setNoneEnabled'

**Topic ID**: 18365
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/attributeerror-qmrmlnodecombobox-has-no-attribute-named-setnoneenabled/18365

---

## Post #1 by @Yihao_Liu (2021-06-28 05:59 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version: 4.11.20210226<br>
Expected behavior: setNoneEnabled() to disable qMRMLNodeComboBox “none” option<br>
Actual behavior: reported error</p>
<p>My code:<br>
…<br>
self.ui.fid1MRMLNodeComboBox.nodeTypes = [‘vtkMRMLMarkupsFiducialNode’]<br>
self.ui.fid1MRMLNodeComboBox.setNoneEnabled(False)<br>
…<br>
Bug:<br>
Traceback (most recent call last):<br>
File “/home/yl/se/TMSKuka/TMSKukaGUI/TMSKukaGUI.py”, line 92, in setup<br>
self.ui.fid1MRMLNodeComboBox.setNoneEnabled(False)<br>
AttributeError: qMRMLNodeComboBox has no attribute named ‘setNoneEnabled’<br>
Slicer Docs:<br>
<a href="https://apidocs.slicer.org/master/qMRMLNodeComboBox_8h_source.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/qMRMLNodeComboBox_8h_source.html</a><br>
<a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a60aadef87aa219043a0177780f22d855" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a60aadef87aa219043a0177780f22d855</a></p>

---

## Post #2 by @jamesobutler (2021-06-28 11:18 UTC)

<p>From Python this property “noneEnabled” is set directly. You can find examples of its usage in python by searching the Slicer GitHub repo.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/Slicer/search?l=Python&amp;q=noneEnabled&amp;type=">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">

      <a href="https://github.com/Slicer/Slicer/search?l=Python&amp;q=noneEnabled&amp;type=" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/3b0adef3fc47ab0d8d17660819fc3d5a78b497abbd640d879a399717a7768cb8/Slicer/Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/Slicer/search?l=Python&amp;q=noneEnabled&amp;type=" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer</a></h3>

  <p>Multi-platform, free open source software for visualization and image computing. - Slicer/Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-python">self.ui.fid1MRMLNodeComboBox.noneEnabled = False
</code></pre>

---

## Post #3 by @lassoan (2021-06-28 15:13 UTC)

<p>You may find useful this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">documentation page</a>, which describes how to read doxygen-generated documentation in Python.</p>

---

## Post #4 by @Yihao_Liu (2021-06-28 15:26 UTC)

<p>Thank you for your reply. Yes I tried it and it worked.</p>

---

## Post #5 by @Yihao_Liu (2021-06-28 15:27 UTC)

<p>Thank you very much! This is very helpful. I should have seen this earlier.</p>

---
