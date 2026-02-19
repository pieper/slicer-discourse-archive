---
topic_id: 25043
title: "Slicer Crash Without Error Message When Calling Vtkmrmlseque"
date: 2022-09-01
url: https://discourse.slicer.org/t/25043
---

# Slicer crash without Error message when calling vtkMRMLSequenceNode.GetNthDataNode(-1)

**Topic ID**: 25043
**Date**: 2022-09-01
**URL**: https://discourse.slicer.org/t/slicer-crash-without-error-message-when-calling-vtkmrmlsequencenode-getnthdatanode-1/25043

---

## Post #1 by @sunshine (2022-09-01 14:50 UTC)

<p>Operating system: Win10<br>
Slicer version: 5.1.0-2022-08-16<br>
Expected behavior: Generate an Error message, instead of crashing without any warning or error<br>
Actual behavior: Crash directly with no error message</p>
<p>This happens when the input argument 	of function .GetNthDataNode( int 	itemNumber &lt; 0 ).<br>
The crashing without a hint gives the programmer a hard time debugging.</p>

---
