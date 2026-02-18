# Incorrect method signature for addAttribute of qMRMLNodeComboBox?

**Topic ID**: 43015
**Date**: 2025-05-20
**URL**: https://discourse.slicer.org/t/incorrect-method-signature-for-addattribute-of-qmrmlnodecombobox/43015

---

## Post #1 by @jamesobutler (2025-05-20 23:10 UTC)

<p>Using Slicer Preview 5.9.0-2025-05-16</p>
<p>When calling a qMRMLNodeComboBox <code>addAttribute</code> with 2 input arguments I observe no error however the help method indicates there should be 3 input arguments:</p>
<pre data-code-wrap="python"><code class="lang-python">node_combobox = slicer.qMRMLNodeComboBox()
node_combobox.setMRMLScene(slicer.mrmlScene)
node_combobox.nodeTypes = ["vtkMRMLMarkupsLineNode"]
print(help(node_combobox.addAttribute))
</code></pre>
<p>Output:</p>
<pre><code class="lang-auto">Help on builtin_qt_slot:

addAttribute(...)
    X.addAttribute(nodeType, attributeName, attributeValue)

None
</code></pre>
<p>The <code>help()</code> output appears to show 1 signature with 3 input arguments, but when I only give 1 input argument it warns that it has 2 signatures that accept either 2 or 3 input arguments.Is it getting confused that qMRMLNodeFactory has an <code>addAttribute</code> with 2 input arguments while qMRMLNodeComboBox has an <code>addAttribute</code> with 3 input arguments?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; node_combobox.addAttribute("MyAttributeName")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ValueError: Could not find matching overload for given arguments:
('MyAttributeName',)
 The following slots are available:
addAttribute(QString nodeType, QString attributeName, QVariant attributeValue) -&gt; void
addAttribute(QString nodeType, QString attributeName) -&gt; void
</code></pre>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L144-L146">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L144-L146" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L144-L146" target="_blank" rel="noopener nofollow ugc">Libs/MRML/Widgets/qMRMLNodeComboBox.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/673ddca536801eedfdc3287dbc6ab110c494382c/Libs/MRML/Widgets/qMRMLNodeComboBox.h#L144-L146" rel="noopener nofollow ugc"><code>673ddca53</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="144" style="counter-reset: li-counter 143 ;">
          <li>Q_INVOKABLE void addAttribute(const QString&amp; nodeType,</li>
          <li>                              const QString&amp; attributeName,</li>
          <li>                              const QVariant&amp; attributeValue = QVariant());</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @cpinter (2025-05-21 09:04 UTC)

<p>This seems correct to me.</p>
<ul>
<li>There is one function for adding attribute in the node combobox, which has three arguments</li>
<li>The <code>help</code> call shows you that</li>
<li>The last argument in the function has a default value, so theorically you can call it with giving two arguments</li>
<li>The error message listing the available variants finds this option</li>
</ul>
<p>The only thing that I find strange is that <code>help</code> output and the error message are different.<br>
Is this your problem?</p>

---

## Post #3 by @jamesobutler (2025-05-21 10:48 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="43015">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The only thing that I find strange is that <code>help</code> output and the error message are different.<br>
Is this your problem?</p>
</blockquote>
</aside>
<p>Yes these outputs were producing two things.</p>

---
