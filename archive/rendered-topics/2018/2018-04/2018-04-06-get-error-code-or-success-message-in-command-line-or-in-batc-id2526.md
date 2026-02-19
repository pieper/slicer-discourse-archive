---
topic_id: 2526
title: "Get Error Code Or Success Message In Command Line Or In Batc"
date: 2018-04-06
url: https://discourse.slicer.org/t/2526
---

# Get error code or success message in command line or in batch file or get a Log file

**Topic ID**: 2526
**Date**: 2018-04-06
**URL**: https://discourse.slicer.org/t/get-error-code-or-success-message-in-command-line-or-in-batch-file-or-get-a-log-file/2526

---

## Post #1 by @anandmulay3 (2018-04-06 08:24 UTC)

<p>Hello,<br>
I’m using batch file to call slicer scriptable module , what i need is after completion of task or failure due to error that error should come in CMD.<br>
Can you please help in this ??</p>
<p>Thanks,</p>

---

## Post #2 by @pieper (2018-04-06 13:26 UTC)

<p>Most scripted modules are meant to be used interactively so their widget code generates error dialogs or other progress that may not be easy to use in batch mode.  Best practice would be for the scripted module logic to provide a non-gui api that would return error codes, etc and that would be better to use in a batch mode.  Not all scripted modules strictly follow that pattern, but if you find places where refactoring functionality into logic classes would be useful you could consider implementing contributing those changes.</p>

---
