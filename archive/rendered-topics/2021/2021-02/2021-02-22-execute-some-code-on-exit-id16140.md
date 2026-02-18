# Execute some code on exit

**Topic ID**: 16140
**Date**: 2021-02-22
**URL**: https://discourse.slicer.org/t/execute-some-code-on-exit/16140

---

## Post #1 by @giovform (2021-02-22 18:36 UTC)

<p>Is there a way to execute some code on Slicer exit?</p>

---

## Post #2 by @lassoan (2021-02-22 18:54 UTC)

<p>You can detect and intercept application exit request, scene saving, shutdown, etc. at multiple levels. What exactly you would like to do and when?</p>

---

## Post #3 by @giovform (2021-02-22 19:01 UTC)

<p>I would like to cancel a runnig CLI at the application shutdown… I saw there is a signal emitted for startup “startupCompleted()” but none for the shutdown. Does it has to be done directly from Qt?</p>

---
