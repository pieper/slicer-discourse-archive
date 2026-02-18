# Layout change doesn't work

**Topic ID**: 14451
**Date**: 2020-11-05
**URL**: https://discourse.slicer.org/t/layout-change-doesnt-work/14451

---

## Post #1 by @mau_igna_06 (2020-11-05 20:25 UTC)

<p>I add this line slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView) on the end of the createUserInterface function on the ScrewStep.py module of the Pedicle Screw Simulator Extension and it doesn’t work. It keeps showing the ‘3D only’ view.<br>
But if I write that line on the python console, it works. Why this happens? I have checked with debug flags (before that line and after that line) and the code does run</p>

---

## Post #2 by @lassoan (2020-11-05 20:56 UTC)

<p>Please push your change to your fork and send a link to the line where you set the layout.</p>

---

## Post #3 by @mau_igna_06 (2020-11-05 21:54 UTC)

<p>Okey Andras. Here is the <a href="https://github.com/mauigna06/PedicleScrewSimulator/blob/b79fdc94e9c2337db5420c9f97774150c17eeb82/PedicleScrewSimulator/PedicleScrewSimulatorWizard/ScrewStep.py#L282" rel="noopener nofollow ugc">link</a>. Thanks for the help</p>

---

## Post #4 by @lassoan (2020-11-05 22:46 UTC)

<p>Thanks for the link. It makes it clear what the issue is. It is way too early to set the layout there, as the layout is set at each workflow step (search for <code>setLayout</code> in the code).</p>
<p>A debugger would help you tremendously - you can put a breakpoint, inspect variables, run any code at any time. See setup instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio_Code">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio_Code</a></p>

---

## Post #5 by @mau_igna_06 (2020-11-05 23:23 UTC)

<p>Thank you Andras. I’ll install Visual Studio Code and Slicer’s Python debugger module.</p>

---

## Post #6 by @mau_igna_06 (2020-11-06 19:32 UTC)

<p>I was able to set it up. I would suggest you include the contents of <a href="https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496/19">this</a> post in the tutorial of above because I had to edit settings.json file to make it work. Thank you for the help</p>

---

## Post #7 by @lassoan (2020-11-06 20:12 UTC)

<p>Setting up those additional paths takes a little effort and does not do much (see <a href="https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496/23">here</a>), so overall I would not recommend users to spend time with specifying these additional settings. If you can make VTK, MRML, CTK, or Qt <em>method name</em> (not just class name) auto-complete or documentation work then let me know - then it may worth the trouble of setting up more paths.</p>

---

## Post #8 by @mau_igna_06 (2020-11-06 21:25 UTC)

<p>You are right Andras. I think I just needed to set up the python.pythonPath variable to Slicer’s python to make it work and everything else on the settings.json file is not needed.</p>

---
