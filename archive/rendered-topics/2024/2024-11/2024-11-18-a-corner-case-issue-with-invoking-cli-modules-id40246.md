# A corner-case issue with invoking CLI modules

**Topic ID**: 40246
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/a-corner-case-issue-with-invoking-cli-modules/40246

---

## Post #1 by @shai-ikko (2024-11-18 16:37 UTC)

<p>Hi,</p>
<p>TL;DR: There’s a little clash between Slicer CLI module invocation and Python’s <code>argparse</code>, in a corner case; there’s a non-obvious workaround; maybe there should be a fix.</p>
<p>I’m developing some functionality in Slicer as a pair of modules – a UI module which invokes a CLI module. The CLI module is, in fact, just a wrapper around an existing, non-Slicer-related executable, so I wrote it in Python, using the stdlib’s <code>argparse</code> to parse parameters.</p>
<p>One of the parameters I want to pass from the UI to the CLI module is a float-vector indicating spatial direction. So, in typical use, it looks like <code>1.0,0.0,0.0</code>. But it can also look like <code>-1.0,0.5,0.5</code>. For clarity of description, let’s say it’s called “vector”.</p>
<p>My UI module invokes the CLI module as exemplified in documentation, using<br>
<code>slicer.cli.runSync(slicer.modules.&lt;my-module&gt;, None, cliParams)</code>.<br>
This builds a command line with the parameters as defined in the module’s XML file, and that all seems fine.</p>
<p>The issue is that argparse, when it sees an argument which starts with the flag prefix character (<code>-</code>), and doesn’t <a href="https://docs.python.org/3/library/argparse.html#arguments-containing" rel="noopener nofollow ugc">“look like a negative number”</a>, thinks it is seeing an option. So when I tried to invoke the module with something like<br>
<code>--vector -1.0,0.5,0.5</code><br>
I got exactly the error in the last example in the argparse documentation:<br>
<code>error: argument --vector: expected one argument</code></p>
<p>The obvious fix would be to use something unambiguous like<br>
<code>--vector=-1.0,0.5,0,5</code><br>
but there is no way to tell Slicer to do that. The next thing I hoped for was to try to change the option prefix character (argparse lets you say that options should be prefixed by e.g. <code>+</code> instead of <code>-</code>), but alas, the <code>-</code> as prefix is also hard-coded in Slicer.</p>
<p>The workaround I found was to format the vector as string myself, and add a space in its front. Then it doesn’t start with a <code>-</code>, but whoever needs to parse floats out of it still manages to do so.</p>
<p>In case anyone seeks to improve the code handling this, a word of warning: The function which actually does the invocation, as far as I can see, is <code>vtkSlicerCLIModuleLogic::ApplyTask()</code>, in <code>Slicer/Base/QTCLI/vtkSlicerCLIModuleLogic.cxx</code>; at least in version 5.6.2, this function seems to be &gt;1500 lines long.</p>

---
