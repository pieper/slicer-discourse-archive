# Linux factory not building

**Topic ID**: 95
**Date**: 2017-04-12
**URL**: https://discourse.slicer.org/t/linux-factory-not-building/95

---

## Post #1 by @ihnorton (2017-04-12 22:33 UTC)

<p>The Linux factory seems to have stopped running a few days ago:</p>
<p>04-08:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-08&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=linux" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-08&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=linux</a></p>
<p>04-09:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-09&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=linux" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-04-09&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=linux</a></p>

---

## Post #2 by @lassoan (2017-04-12 23:25 UTC)

<p>I think still only <a class="mention" href="/u/jcfr">@jcfr</a> has access to the factory machines.</p>

---

## Post #3 by @jcfr (2017-04-13 00:22 UTC)

<p>Thanks for the reminder.</p>
<p>I will restart the VM running on the macosx <code>factory-south</code>.</p>
<p>In the mean time, I will look into setting up our new dedicated build server to also run linux build (similar to the new windows build server)</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#overload.kitware_and_metroplex.kitware">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#overload.kitware_and_metroplex.kitware</a></p>
<p><strong>Update 1</strong>: The host machine needed some MacOSX updates and was waiting to be restarted …</p>
<p><strong>Update 2</strong>: As of 10.10pm EDT, the Linux VM is now up and running</p>

---
