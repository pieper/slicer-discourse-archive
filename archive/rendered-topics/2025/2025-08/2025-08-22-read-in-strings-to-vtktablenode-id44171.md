---
topic_id: 44171
title: "Read In Strings To Vtktablenode"
date: 2025-08-22
url: https://discourse.slicer.org/t/44171
---

# Read in Strings to vtkTableNode?

**Topic ID**: 44171
**Date**: 2025-08-22
**URL**: https://discourse.slicer.org/t/read-in-strings-to-vtktablenode/44171

---

## Post #1 by @mrsh0r3s (2025-08-22 17:29 UTC)

<p>Hello,</p>
<p>Whenever I try to use the slicer.util.updateTableFromArray() function to import an array with a string value - say “DeviceID” - I get the error “ValueError: could not convert string to float: ‘DeviceID’”</p>
<p>Numerical arrays work just fine but string arrays, object arrays, or anything that isn’t exclusively numbers fails. If I pass an array of strings that are numbers - for instance np.array([[‘0’, ‘0’, ‘0’]])which could be seen as the equivalent of np.zeros((1,3)).astype(str) - the table reads it in but still has columns with Data type set to float when examined in Slicer’s Table module.</p>
<p>Is there a better way to import string or mixed tables through code?</p>

---

## Post #2 by @lassoan (2025-08-23 02:57 UTC)

<p><code>slicer.util.updateTableFromArray()</code> only works for numeric types (as VTK only offers array mapping for these types). You can set string elements one by one:</p>
<pre data-code-wrap="python"><code class="lang-python">column = tableNode.GetTable().GetColumn(0)

column.InsertNextValue("asdf")
column.InsertNextValue("zxcv")
column.InsertNextValue("qwerty")

tableNode.GetTable().Modified()
</code></pre>

---
