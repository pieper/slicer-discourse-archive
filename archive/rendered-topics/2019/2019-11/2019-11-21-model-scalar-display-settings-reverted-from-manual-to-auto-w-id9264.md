# Model scalar display settings reverted from "manual" to "auto" when saving/loading scene

**Topic ID**: 9264
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/model-scalar-display-settings-reverted-from-manual-to-auto-when-saving-loading-scene/9264

---

## Post #1 by @stephan (2019-11-21 21:23 UTC)

<p>Hi,<br>
it looks like this bug: <a href="https://issues.slicer.org/view.php?id=4464" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4464</a> has been re-introduced recently. It had been fixed in r27208, but when I installed the current nightly (r28643) I found the same issue as had been reported before: When manually changing the displayed range of a scalar overlay, this reverts to the “auto” setting (i.e. display from min to max value of the scalar) upon saving and loading the scene.<br>
<a class="mention" href="/u/lassoan">@lassoan</a>, I think you fixed it back then - could you maybe have a look if the same bug has been re-introduced?</p>
<p>Thank you<br>
Stephan</p>

---

## Post #2 by @lassoan (2019-11-22 03:57 UTC)

<p>Thanks for reporting. There was mistake in a recent refactoring, I’ve fixed the issue now (in r28645).</p>

---
