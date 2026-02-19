---
topic_id: 37072
title: "Loading Scriptedcli Python Cli Modules With The Extension"
date: 2024-06-27
url: https://discourse.slicer.org/t/37072
---

# Loading scriptedCLI (python cli) modules with the extension

**Topic ID**: 37072
**Date**: 2024-06-27
**URL**: https://discourse.slicer.org/t/loading-scriptedcli-python-cli-modules-with-the-extension/37072

---

## Post #1 by @MartinBGregorio (2024-06-27 16:00 UTC)

<p>I am building a python extension that uses both scripted and scriptedcli modules. I am trying to streamline the installation process by simply dropping the extension folder inside the slicer window (equiv to using the extension wizard) but only the scripted modules appear in the resulting window and are then loaded. I can still import the scriptedcli modules through settings&gt;modules&gt;Additional module paths, but this makes the install process cumbersome for users. Is there a way to import the scriptedcli modules as I first explained, or are we bound to import them ourselves ?</p>

---

## Post #2 by @lassoan (2024-06-27 16:05 UTC)

<p>For end-user deployment, I would recommend to submit to the extensions index (or at least create an extension package), as most users would not be comfortable with cloning a github repository or downloading and unzipping an archive.</p>
<p>For developers, it would be useful to allow adding Python scripted CLIs to additional module paths by drag-and-drop. To achieve this you can enhance <a href="https://github.com/Slicer/Slicer/blob/b0ed88351af465159b101fc434802c83fd438522/Modules/Scripted/ExtensionWizard/ExtensionWizardLib/ModuleInfo.py#L35-L85">ModuleInfo.py</a> to recognize Python scripted CLI scripts. Once it works for you locally, it would be great if you could submit a pull request to update the script in Slicer core.</p>

---
