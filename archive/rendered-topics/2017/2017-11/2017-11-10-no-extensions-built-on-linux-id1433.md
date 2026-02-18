# No extensions built on Linux

**Topic ID**: 1433
**Date**: 2017-11-10
**URL**: https://discourse.slicer.org/t/no-extensions-built-on-linux/1433

---

## Post #1 by @fedorov (2017-11-10 15:27 UTC)

<p>There are no linux extension builds on the dashboard today.</p>

---

## Post #2 by @jcfr (2017-11-10 18:50 UTC)

<p>Thanks for the note.</p>
<p>Last night I manually deleted the CDash entry for the Slicer build, fixed the dashboard script and manually re-triggered the nightly build.</p>
<p><a href="https://github.com/Slicer/DashboardScripts/commit/a4e8b6b8a42a39edb4a80d5cbce6c98b258cfc14" class="onebox" target="_blank">https://github.com/Slicer/DashboardScripts/commit/a4e8b6b8a42a39edb4a80d5cbce6c98b258cfc14</a></p>
<p>Since this happen early morning, extension are currently being build</p>
<p>And you can now start to see some of them: <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=site&amp;compare1=61&amp;value1=factory-south-ubuntu-64bits.kitware&amp;field2=groupname&amp;compare2=61&amp;value2=Extensions-Nightly">http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=site&amp;compare1=61&amp;value1=factory-south-ubuntu-64bits.kitware&amp;field2=groupname&amp;compare2=61&amp;value2=Extensions-Nightly</a></p>

---
