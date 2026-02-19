---
topic_id: 9645
title: "Importing Slicer Libraries Separately Outside Embedded Pytho"
date: 2019-12-29
url: https://discourse.slicer.org/t/9645
---

# Importing slicer libraries separately, outside embedded Python, like in Conda or Jupiter environments

**Topic ID**: 9645
**Date**: 2019-12-29
**URL**: https://discourse.slicer.org/t/importing-slicer-libraries-separately-outside-embedded-python-like-in-conda-or-jupiter-environments/9645

---

## Post #1 by @Jason_West (2019-12-29 16:46 UTC)

<p>Hey Everyone,<br>
I was curious if anyone here has had success using the slicer libraries importing from an outside Python, perhaps a lightweight build using swig to give access to all the libraries available in “import slicer.”?</p>
<p>That would be incredibly useful, you could pull in slicer libraries into any conda or jupyter environment, even just being able to integrate into IDE environment would be nice.</p>
<p>I have been able to do this using pip wheels with ctk and vtk libraries, if something similar could be done with the slicer libraries would be awesome <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Any thoughts on this?</p>
<p>Thanx!</p>

---

## Post #2 by @lassoan (2019-12-29 19:10 UTC)

<p>Fundamental libraries that Slicer is built on are already available as separate Python packages (VTK, ITK, etc.). There are more libraries that could be made available as standalone Python packages (such as MRML, FreeSurfer, SegmentationCore, <a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/40a315ef/">PythonQt</a>) with some more work. However, Slicer’s main added value (compared to just using fundamental libraries from Python scripts) that it is an end-user application and so most of the development efforts focuses on improving this aspect.</p>
<p>You can consider each Slicer installation as a virtual Python environment - the same way as you create virtual environments using conda. You should be able to use Slicer’s executables in place of Python executables for most use cases: you can use Slicer application as a Jupyter kernel (<a href="https://github.com/Slicer/SlicerJupyter">https://github.com/Slicer/SlicerJupyter</a>), if you need any more features you can import any Python packages from pip directly into Slicer’s environment, you can connect to Slicer using an external debugger, run Slicer scripts from the command-line, run CLI modules as standalone applications, etc.</p>

---
