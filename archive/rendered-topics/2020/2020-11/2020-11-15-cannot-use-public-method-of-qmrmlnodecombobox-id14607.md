# Cannot use public method of qMRMLNodeComboBox

**Topic ID**: 14607
**Date**: 2020-11-15
**URL**: https://discourse.slicer.org/t/cannot-use-public-method-of-qmrmlnodecombobox/14607

---

## Post #1 by @mau_igna_06 (2020-11-15 00:31 UTC)

<p>Here there is a method called setShowHidden<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a724b4b712d2ce76ee2164085e08bd67f" target="_blank" rel="noopener nofollow ugc">apidocs.slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a724b4b712d2ce76ee2164085e08bd67f" target="_blank" rel="noopener nofollow ugc">Slicer: qMRMLNodeComboBox Class Reference</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
I try the following code in the python interactor and it doesn’t work and it should:
<pre><code class="lang-auto">inputComboBox = slicer.qMRMLNodeComboBox()
inputComboBox.setShowHidden(False)
</code></pre>
<p>It gives the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: qMRMLNodeComboBox has no attribute named 'setShowHidden'
</code></pre>

---
