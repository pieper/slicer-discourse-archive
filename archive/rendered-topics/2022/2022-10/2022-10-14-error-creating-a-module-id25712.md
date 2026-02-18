# Error creating a module

**Topic ID**: 25712
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/error-creating-a-module/25712

---

## Post #1 by @LuisaDantas (2022-10-14 23:17 UTC)

<p>Hey,</p>
<p>I’m following PerkLab’s Slicer bootcamp tutorial on how to create a Module for 3D Slicer. But when I try to run the code to see the changes it returns this error:</p>
<p><code>ModuleNotFoundError: No module named 'vtkmodules.vtkCommonCore'</code></p>
<p>I tried to instal this library and vmtk, vtk, itk, but then this error appears:</p>
<p><code>ImportError: Module use of python39.dll conflicts with this version of Python.</code></p>
<p>I’m using Windows 10 and python 3.10.6. Does anyone know why this might be happenning, I didn’t found anythin similar</p>

---

## Post #2 by @lassoan (2022-10-19 05:42 UTC)

<p>VTK is already installed in 3D Slicer’s Python environment. You must not install VTK using pip, because it may conflict with the version that is bundled already.</p>
<p>Slicer also makes it very convenient to access VTK classes. You don’t need to struggle with finding the right VTK module for a specific class, but instead you can simply use <code>vtk.vtkSomeClassName</code> syntax.</p>

---

## Post #3 by @LuisaDantas (2022-10-25 13:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I’m using VS Code, I don’t know if it’s a problem from the editor with Slicer but it doesn’t seem to be importing none of the packages.</p>
<p>These below are the packages that came when I created the module through Extension Wizard.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af29b07def1d85302eda2911d672597a147a0289.png" alt="image" data-base62-sha1="oZySlh4omQpWczcXMLUOKuCoGDf" width="390" height="159"></p>

---

## Post #4 by @lassoan (2022-10-25 13:27 UTC)

<p>VS Code can only load basic Python packages that are available in the standalone Python interpreter that you specify. VS Code does not know about packages that Slicer creates dynamically, so most of the IDE features that depend on static code analysis tools will not work.</p>
<p>To access all packages and classes, documentation, auto-complete, etc., you need to start Slicer and attach VS code to it. See more information starting from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">this page</a>. Attaching to a running Python interpreter is certainly not as convenient as just running a standalone Python script from the IDE, but once you got used to it, there is not much difference in overall productivity.</p>

---

## Post #5 by @LuisaDantas (2022-10-25 13:56 UTC)

<p>Sorry to be bothering you again.</p>
<p>But it fails to download the debbuger extension (shown on image below). Do you have any preference or other sugestions on ways to develop scripts to Slicer, I tried to follow some tutorials but wasn’t able to implement my script through none of them.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f49ba53406e3306089eafbb208329b25fc9327fb.png" alt="image" data-base62-sha1="yTTYdUrYjhUQXMU8f2cePaNrMLx" width="290" height="54"></p>

---

## Post #6 by @lassoan (2022-10-25 18:42 UTC)

<p>What Slicer version do you use, on what operating system? Are you behind some kind of firewall or proxy server?</p>

---

## Post #7 by @LuisaDantas (2022-10-26 10:08 UTC)

<p>Slicer 5.0.3 on Windows 10.<br>
I am but it usually doesn’t block the download of plugins, packages or even softwares.</p>

---

## Post #8 by @lassoan (2022-10-26 11:43 UTC)

<p>The extension manager frontend server downloads packages from the backend server. This operation may be blocked by ghmisconfigured/too aggressive proxy servers.</p>
<p>Please check if you can download if you open the Extensions Manager in your default web browser - see detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection">here</a>.</p>
<p>If this does not work then let us know, there are several other ways to do it.</p>

---

## Post #9 by @pieper (2022-10-26 11:50 UTC)

<p>I’m thinking that if the extension manager fails to connect we should put instructions or links to instructions to workarounds directly in the extension manager window.  I have another report yesterday about a linux machine behind a hospital firewall that couldn’t access the extension server and the user didn’t know what to do about it (or maybe the info is there and he just missed it - I don’t have the error myself so I’m not sure what is currently displayed).</p>
<p>I also note that our instructions require the user to create the link manually based on the revision numbers and OS.  Probably we should provide this link automatically.</p>

---

## Post #11 by @LuisaDantas (2022-11-03 14:34 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> , I tried different methods but the VS Code still doesn’t load <code>slicer.ScriptedLoadableModule</code> and <code>slicer.util</code>. I don’t know what else to try.</p>

---

## Post #12 by @LuisaDantas (2022-11-03 17:47 UTC)

<p><code>import slicer</code> doesn’t work either <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @lassoan (2022-11-08 14:09 UTC)

<p>You can only run the module in Slicer application. Start Slicer, attach the Python debugger, and add a breakpoint where you want to interact with your code.</p>

---

## Post #14 by @LuisaDantas (2022-11-08 14:17 UTC)

<p>I attached the python to slicer and still it doesn’t recognize the packages</p>

---

## Post #15 by @lassoan (2022-11-08 14:19 UTC)

<p>Attaching the debugger is a good start. Now add a breakpoint and make Slicer reach the breakpoint. You have access to all symbols, packages, etc. in that context.</p>

---

## Post #16 by @LuisaDantas (2022-11-08 14:41 UTC)

<p>Had some improvements. VS Code still shows warnings about the packages in the file, but Slicer reached the breakpoint. I think that means it worked, might be something in VS Code.</p>
<p>Thank you for all the help!<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #17 by @lassoan (2022-11-08 14:48 UTC)

<p>VS Code probably uses static code analysis for syntax highlighting, which may prevent it from seeing dynamically loaded packages.</p>

---
