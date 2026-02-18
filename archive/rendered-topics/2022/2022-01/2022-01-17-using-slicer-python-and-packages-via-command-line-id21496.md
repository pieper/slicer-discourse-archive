# Using Slicer python and packages via command line

**Topic ID**: 21496
**Date**: 2022-01-17
**URL**: https://discourse.slicer.org/t/using-slicer-python-and-packages-via-command-line/21496

---

## Post #1 by @Karthik (2022-01-17 16:48 UTC)

<p>Hi everyone.<br>
I am currently using Slicer version 4.11.20210226 on ubuntu 20.04.<br>
I have certain extensions installed such as SlicerVMTK, etc.<br>
When I use the python interactor inside Slicer application, I am able to import, test and use scripts, binaries from these extensions such as vtkvmtkSegmentationPython.<br>
However, if I run PythonSlicer from terminal, I am unable to import and use any binaries, scripts that are installed via extensions. I am only able to use packages like numpy which are built into Slicer by default.<br>
I would like to use all libraries that Slicer application has access to through terminal. Since the environment already exists within the application, it should be possible to replicate it outside as well, right?</p>

---

## Post #2 by @Karthik (2022-01-22 13:01 UTC)

<p>Basically, what I’m trying to get at is…</p>
<p>Is it possible to run python scripts using PythonSlicer?<br>
Is it also possible to include other libraries that may not be a part of PythonSlicer by default but still exists within the same Slicer Application. Ex: using vmtk shared object files or using vmtkscripts from the SlicerVMTK extension?</p>

---

## Post #3 by @Karthik (2022-01-27 04:43 UTC)

<p>Hi everyone. I have achieved it using <code>export PYTHONPATH</code> and <code>export LD_LIBRARY_PATH</code> commands.</p>
<p>PYTHONPATH is location where we search for python scripts. LD_LIBRARY_PATH is location where we search for shared object files. If we want to include just python scripts, then ‘export PYTHONPATH’ is sufficient. However, if the library contains shared object files that also need to be used, then ‘export LD_LIBRARY_PATH’ is also required.</p>

---
