# Slicer IGT Multiple Tools, Plus ToolKit

**Topic ID**: 18328
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/slicer-igt-multiple-tools-plus-toolkit/18328

---

## Post #1 by @jasmine-lou (2021-06-24 15:59 UTC)

<p>Hi all,</p>
<p>I had a question about how to implement tracking multiple tools using the NDI Aurora EM system and multiple coils. Right now, it seems that the first tool/coil is working fine but the Plus/Slicer connection doesn’t seem to be able to recognize or pick up the second tool/coil. We’ve tried changing the Plus Configuration file to include a second data source, a second output channel, and a second Default Client Info, but it seems that when we connect the server from the Slicer side through OpenIGTLinkIF the second coil does not show up in the I/O configuration. Any help would be appreciated, thanks!</p>

---

## Post #2 by @lassoan (2021-06-24 20:45 UTC)

<p>Most Plus configuration files use several tools (reference, stylus, probe, etc). Have a look at those again. If you still have problems then upload your condig file somewhere and post the link here.</p>

---
