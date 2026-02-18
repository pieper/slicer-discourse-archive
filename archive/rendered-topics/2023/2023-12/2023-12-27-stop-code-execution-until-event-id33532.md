# Stop code execution until Event

**Topic ID**: 33532
**Date**: 2023-12-27
**URL**: https://discourse.slicer.org/t/stop-code-execution-until-event/33532

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-12-27 11:54 UTC)

<p>Hi all <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>On this time I’m interested in automatize some process, related with centerline quantification and data related with it.</p>
<p>In my code I have to put some fiducial (that can not be set before), and with this fiducial node info, made some operations. The problem becomes when the code doesn’t wait for the fiducial selection and keeps running (The code finally fail, because it don’t have the fiducial Info)</p>
<p>Is there a way to keep  waiting the code until some event occurs, and then runs the other part of the code?</p>
<p>Thanks a lot for your help.</p>

---

## Post #2 by @pieper (2023-12-27 18:30 UTC)

<p>Hi -</p>
<p>For this issue and probably <a href="https://discourse.slicer.org/t/extract-ras-coordinates-by-clicking/33531">your other question</a> you could study how the event observers work in Slicer to make everything asynchronous.  E.g. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-notification-if-a-markup-control-point-position-is-modified">this example</a> has callbacks for markup interactions.  Your code shouldn’t block, but should instead be driven by callbacks when events occur.</p>

---
