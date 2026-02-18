# Tests broken by recent Python updates

**Topic ID**: 214
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/tests-broken-by-recent-python-updates/214

---

## Post #1 by @ihnorton (2017-04-27 17:06 UTC)

<p>Something in the changes between 25945 and 25971 seems to have broken a number of Python tests in extensions, e.g.:</p>
<p><a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-25&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Chest" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-25&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Chest</a></p>
<p><a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-26&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Chest" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-26&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=Chest</a></p>
<p>(also SlicerDMRI and others)</p>

---

## Post #2 by @lassoan (2017-04-27 17:30 UTC)

<p>Before rev 25970, many Python tests were actually not executed. Now they are, so you can expect test errors to show up. You have to review and fix those tests.</p>
<p>Details: There was a problem in CTK argument parser that made all parameters after --additional-module-paths argument ignored (all further arguments were interpreted as additional paths). All python tests that relied on running a python script using --python-script actually did not test anything, just started Slicer and quit.</p>

---
