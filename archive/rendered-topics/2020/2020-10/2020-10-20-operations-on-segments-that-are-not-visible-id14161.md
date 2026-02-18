# Operations on segments that are not visible

**Topic ID**: 14161
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/operations-on-segments-that-are-not-visible/14161

---

## Post #1 by @hherhold (2020-10-20 14:05 UTC)

<p>I will sometimes inadvertently hit “apply” on an editing operation with a segment that is not visible. This results in a rather long delay, followed by “undo”, to get back to where I was.</p>
<p>Has there been any discussion about a warning box when you hit “apply” and the selected segment is not visible? I realize it’s my own dumb fault, but over the years this would probably have saved me a fair amount of time.</p>
<p>Thanks!!</p>

---

## Post #2 by @lassoan (2020-10-20 14:54 UTC)

<p>This has come up a few times before. I agree that applying operation on a non-visible segment often happens by mistake, so a warning box for could be helpful. If we add a “Do not show again” checkbox then it would not be very annoying for those people who do this intentionally. Could you submit a feature request to <a href="https://github.com/Slicer/Slicer/issues">https://github.com/Slicer/Slicer/issues</a>?</p>
<p>Would you be interested in implementing it? It would be a helper function in C++ that could be called using a single line from both C++ and Python scripted effects.</p>

---

## Post #3 by @hherhold (2020-10-22 12:25 UTC)

<p>Feature request submitted.</p>
<p>Sure, I’d be willing to try implementing it. As long as nobody needs it urgently - I have two separate conference talks to prep and give in the next month or so.</p>

---
