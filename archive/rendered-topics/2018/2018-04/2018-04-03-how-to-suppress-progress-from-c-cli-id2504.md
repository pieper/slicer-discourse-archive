# How to suppress #Progress from c++ CLI

**Topic ID**: 2504
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/how-to-suppress-progress-from-c-cli/2504

---

## Post #1 by @kayarre (2018-04-03 16:11 UTC)

<p>when runnning a command from c++ CLI, how can you suppress the <span class="hashtag">#Progress:</span> 0 meter?<br>
I can redirect to a file on linux, but I was curious if there a better way to deal with it?</p>
<p>example command,</p>
<p>"N4ITKBiasFieldCorrection  MRA.nrrd  MRA_BIAS.nrrd</p>

---

## Post #2 by @lassoan (2018-04-04 06:30 UTC)

<p>You can call SetQuiet on the plugin watcher to reduce progress output. However, probably redirection to file is simpler - it works on Windows and Mac essentially the same way.</p>

---
