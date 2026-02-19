---
topic_id: 12122
title: "Debugging A Loadable Extension Linux"
date: 2020-06-19
url: https://discourse.slicer.org/t/12122
---

# Debugging a Loadable Extension (Linux)

**Topic ID**: 12122
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/debugging-a-loadable-extension-linux/12122

---

## Post #1 by @nsbosse (2020-06-19 19:07 UTC)

<p>OS: Linux CentOS 8<br>
Slicer git tag: 80f7a47e343266b5ca7cca59a09816fbbdd6101a</p>
<p>Hi there, I’m working on a loadable extension with a custom Slicer build made using SlicerCAT. I’m able to debug my extension by using “./SlicerWithMyExtension --attach-process” in the terminal and then attaching gdb to the process in vscode. From here, I’m able to set and hit breakpoints as expected within the loadable module.</p>
<p>I would also like to be able to set breakpoints in the built in loadable module source files (the ones located here: path/to/slicersources-src/modules/loadable). However, when I set breakpoints in these files I get the message “Module containing this breakpoint has not yet loaded or the breakpoint address could not be obtained”. I’m wondering if I’ve missed something simple or if I’ve set something up incorrectly. I think I’ve followed the debugging wiki instructions correctly. Should it be possible to hit breakpoints in these files in this way from a loadable extension?</p>

---

## Post #2 by @lassoan (2020-06-19 20:30 UTC)

<p>Shared libraries of modules are loaded during startup, so the message that you see is expected. You should still be able to set breakpoints in the modules.</p>
<p>Visual Studio on Windows indicates this during startup with a warning icon next to the breakpoint, but this goes away when shared library of the module is loaded. Maybe your debugger cannot do this automatic update and you can only set the breakpoint after shared library of your module is loaded.</p>

---

## Post #3 by @nsbosse (2020-06-19 21:19 UTC)

<p>Thank you for the help.</p>
<p>When I attach the debugger, all breakpoints become deactivated and I get an “attempting to bind breakpoint” message on each of them, which (I think) is akin to that warning in Visual Studio on Windows. After some time though, the breakpoints in the custom module become activated but the breakpoints in other modules change to “module containing this breakpoint has not yet loaded or the breakpoint address could not be obtained” so you must be right that the debugger isn’t updated when these libraries are loaded.</p>
<p>I tried loading the reformat module in my project, attaching the debugger, waiting for the working breakpoints to bind, and then, after the breakpoints bind, setting new breakpoints in the reformat module source files but I still found that these new breakpoints are unable bind to these files.</p>
<p>(Sorry if it turns out that this was more of a VSCode setup issue than a Slicer issue)</p>

---

## Post #4 by @lassoan (2020-06-19 21:53 UTC)

<p>Maybe the debugger cannot find the debug symbols? Make sure the debug symbol files are stored at locations where the debugger looks for them.</p>

---
