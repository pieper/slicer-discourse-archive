# How to use python script to install module in additional module paths?

**Topic ID**: 33410
**Date**: 2023-12-16
**URL**: https://discourse.slicer.org/t/how-to-use-python-script-to-install-module-in-additional-module-paths/33410

---

## Post #1 by @derekcbr (2023-12-16 03:02 UTC)

<p>currentPaths = slicer.util.settingsValue(‘Modules/AdditionalPaths’, <span class="chcklst-box fa fa-square-o fa-fw"></span>)<br>
if isinstance(currentPaths, str):<br>
currentPaths = [currentPaths]<br>
if modulePath not in currentPaths:<br>
currentPaths.append(modulePath)<br>
slicer.util.setSettingsValue(‘Modules/AdditionalPaths’, currentPaths)<br>
I try above code but it did not work. Is there a soultion? Thanks.</p>

---

## Post #2 by @Raj_Kumar_Ranabhat (2024-07-23 15:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> : Do you have solution for this work for python scripted module ?</p>

---

## Post #3 by @lassoan (2024-07-23 18:34 UTC)

<p>You can see how the Extension WIzard does it <a href="https://github.com/Slicer/Slicer/blob/909126663f2ff3bbbe1ce56b5e445372a6406ae9/Modules/Scripted/ExtensionWizard/ExtensionWizard.py#L331-L405">here</a>.</p>
<p>However, this should not be necessary and probably there are better ways. What are you trying to achieve?</p>

---
