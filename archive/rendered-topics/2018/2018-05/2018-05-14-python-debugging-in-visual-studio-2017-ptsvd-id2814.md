# Python Debugging in Visual Studio 2017 (ptsvd)

**Topic ID**: 2814
**Date**: 2018-05-14
**URL**: https://discourse.slicer.org/t/python-debugging-in-visual-studio-2017-ptsvd/2814

---

## Post #1 by @mcfly3001 (2018-05-14 13:33 UTC)

<p>Hi all,</p>
<p>I am quite new to slicer development and I am trying to create a small slicelet in Python. Therefore I was trying to attach the debugger in Visual Studio 2017 as described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio</a></p>
<p>When trying to attach though I also end up with the error “…make sure that ptvsd.enable_attach() has been called…”.<br>
I tried to use the Python Debugger extension as well as manually calling “enable_attach” and “wait_for_attach”. I also tried the release as well the nightly version of Slicer. I also made sure to have the newest version of ptvsd which is 3.2.1.</p>
<p>Any ideas what could be wrong here? Or is VS2017 simply not supported?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-05-14 16:14 UTC)

<p>Visual Studio remode debugging server version (ptvsd-2.2) that was bundled with the DebuggingTools extension was only compatible with Visual Studio 2013 and 2015. I’ve now added ptvsd-3.2.1 as well, so now you can use VS2017, too. The updated extension will be available in tomorrow’s nightly build or you can <a href="https://github.com/SlicerRt/SlicerDebuggingTools">download it now from github</a>.</p>

---

## Post #3 by @mcfly3001 (2018-06-25 13:24 UTC)

<p>Thanks for updating the ptvsd. I will give it a try asap!</p>

---
