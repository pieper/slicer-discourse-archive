---
topic_id: 21742
title: "Process Module Logics Event Within Displayable Node"
date: 2022-02-01
url: https://discourse.slicer.org/t/21742
---

# Process module logic's event within displayable node

**Topic ID**: 21742
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/process-module-logics-event-within-displayable-node/21742

---

## Post #1 by @keri (2022-02-01 22:13 UTC)

<p>Hi,</p>
<p>I have a module that invokes custom event <code>MyEvent</code>. I’m looking for a way to catch this event within displayable node.<br>
I can see an option here:</p>
<ol>
<li>I can invoke the event from the module’s logic but set scene as a caller;</li>
<li>invoke the event from the logic and set the logic as a caller</li>
</ol>
<p>If I choose the first option than <code>MyEvent</code> enum will be defined in <code>MyLogic.h</code> and the caller will be the scene. I think this is not a good idea.</p>
<p>If I choose the second option then it seems that I will be unable to get module instance from the displayable node and thus I will be unable to <code>addObserver</code> from the node to the logic.</p>
<p>Also there is a third option: from the module logic iterate through all displayable nodes and call the common method (probably <code>ProcessMRMLEvents</code>) and within this method I should process the chosen event. But I think this is also not a best choice.</p>
<p>Is there any recommendation?</p>

---

## Post #2 by @pieper (2022-02-02 00:31 UTC)

<p>In your own custom app you can do it, but in Slicer we don’t let the MRML nodes know about the Logic and the Logic doesn’t know about the GUI.  So if you want the displayable node to be notified the Logic would invoke the event on the node or set a value that caused the event to be invoked.</p>

---

## Post #3 by @keri (2022-02-03 18:04 UTC)

<p>Thank you, I will take that into account!</p>

---
