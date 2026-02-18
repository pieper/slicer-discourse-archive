# Runtime Error R6036 (microsoft visual c++ run time library)

**Topic ID**: 10884
**Date**: 2020-03-28
**URL**: https://discourse.slicer.org/t/runtime-error-r6036-microsoft-visual-c-run-time-library/10884

---

## Post #1 by @xlucox (2020-03-28 01:34 UTC)

<p>Hi everyone.</p>
<p>I have had problems when importing Scipy in Slicer 4.10.2 on Windows 10.</p>
<p>After write ‘import scipy’ I get a Runtime Error R6036.</p>
<p>I have installed Scipy from Python interactor in Slicer with the following command:</p>
<p>from pip._internal import main as pipmain<br>
pipmain([‘install’,‘scipy’]).</p>
<p>I would be really appreciated it if somebody could let me know how I can fix it.<br>
Thank you very much.</p>

---

## Post #2 by @lassoan (2020-03-28 01:34 UTC)

<p>You need to use recent Slicer-4.11 versions to be able to install packages from PyPI.</p>

---

## Post #3 by @jamesobutler (2020-03-28 13:51 UTC)

<p><a class="mention" href="/u/xlucox">@xlucox</a> Scipy is now included by default in the most recent versions of Slicer 4.11 preview , so you won’t even need to install scipy manually.</p>

---

## Post #4 by @xlucox (2020-03-28 20:37 UTC)

<p>Yes. Thank you very much.</p>
<p>I changed the older version for the newest and it works.</p>

---
