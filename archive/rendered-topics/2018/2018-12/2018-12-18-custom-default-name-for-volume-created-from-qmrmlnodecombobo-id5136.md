# Custom default name for volume created from qMRMLNodeComboBox

**Topic ID**: 5136
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/custom-default-name-for-volume-created-from-qmrmlnodecombobox/5136

---

## Post #1 by @emckenzi123 (2018-12-18 22:24 UTC)

<p>Hello,</p>
<p>I am writing my own python scripted loadable module, and I have a qMRMLNodeComboBox where the user is able to optionally choose to “Create a New Volume As…”.  However, currently the default New Name is “Volume_”.  I would like to customize this new name that is initially presented to the user.  I have searched through the sourcecode and found that I can possibly set this default name using qMRMLNodeFactory.setBaseName (maybe?).  Am I on the right track here?  If so, how do I connect this to my combobox?</p>
<p>much appreciated,<br>
E</p>

---

## Post #2 by @lassoan (2018-12-18 22:42 UTC)

<p>The syntax is <code>myCombobox.baseName='something'</code></p>
<p>(<a href="https://apidocs.slicer.org/v4.8/classqMRMLNodeComboBox.html#a122b3eae788ad580c0dc73976ccd1bb1" rel="nofollow noopener">https://apidocs.slicer.org/v4.8/classqMRMLNodeComboBox.html#a122b3eae788ad580c0dc73976ccd1bb1</a>)</p>

---

## Post #3 by @emckenzi123 (2018-12-19 00:48 UTC)

<p>Thank you very much!</p>

---
