# Debugging Issues using VS Code

**Topic ID**: 35291
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/debugging-issues-using-vs-code/35291

---

## Post #1 by @Istvan (2024-04-04 15:45 UTC)

<p>Hi,</p>
<p>Windows version: 10.0.19045<br>
Slicer Version: 4.11.20200930 r29402 / 002be18<br>
VS Code version: 1.87.2</p>
<p>in order to make a debugging in VS Code using the <code>Python debugger</code> module of Slicer I´ve followed the instructrions written in <a href="https://github.com/SlicerRt/SlicerDebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a><br>
I’ve saved the following simple script into the working directory:<br>
for i in range(3):<br>
print(i)</p>
<p>I’ve started the connection with the debug server in the Slicer and after that the debugging in VS Code. The process seem to work (at least I haven’t got any error messages), however at the debugging tab the buttons <em>step over, step into and step out</em> are greyed out. I can place breakpoints into the script, but the debugging itself does not work. Any suggestions how I can fix this problem? Thanks in advance. Istvan</p>

---

## Post #2 by @lassoan (2024-04-04 15:51 UTC)

<p>Your script is executed line-by-line, so breakpoints will not work there. However, you don’t really need it, as you can just use the Python console or Jupyter notebooks (SlicerJupyter extension) to run code snippets and inspect the results.</p>
<p>You can use breakpoints when debugging code in your module. When you make any modifications then you can reload the module by a single click.</p>

---
