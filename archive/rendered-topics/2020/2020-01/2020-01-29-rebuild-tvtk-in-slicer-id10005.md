# Rebuild? TVTK in Slicer

**Topic ID**: 10005
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/rebuild-tvtk-in-slicer/10005

---

## Post #1 by @hkirvesl (2020-01-29 17:55 UTC)

<p>We are developing a Slicer Extension for aligning 3D shapes.</p>
<p>We have previously created our module and it runs like a charm, but because the algorithm is bit time consuming we wanted to parallelize the algorithm.</p>
<p>Because vtk objects cannot be pickled (which is needed for the multiprocessing), we successfully replaced the vtk with tvtk in our independent python module, and everything is looking good.</p>
<p>However, when I try to connect it to our Slicer module, upon opening Slicer I get the error</p>
<hr>
<p>WARNING: Imported VTK version (8.2) does not match the one used<br>
to build the TVTK classes (8.1). This may cause problems.<br>
Please rebuild TVTK.</p>
<hr>
<p>and the algorithm fails. Am running Ubuntu 18.04 with Slicer 4.11.0-2019-07-27 r28412, but we would of course like the extension work on all OS.</p>
<p>Is there a way I can rebuild the tvtk in Slicer, as the prompt suggests? Or should I try something completely else? Any pointers greatly appreciated, am hitting a wall here pretty badly.</p>

---

## Post #2 by @lassoan (2020-01-29 18:27 UTC)

<p>I don’t think you can use different VTK versions in the same application. You may rebuild TVTK as suggested, but it is probably simpler to <a href="https://docs.python.org/3/library/pickle.html#pickle-inst">add custom pickling functions</a> to vtkImageData (for example, you can serialize the image data to nrrd file).</p>
<p>If all you need is to run some processing in the background then it is probably simpler to run your processing script as a CLI module. See an example <a href="https://github.com/lassoan/SlicerPythonCLIExample">here</a>.</p>

---

## Post #3 by @hkirvesl (2020-01-29 18:47 UTC)

<p>Thanks a bunch Andras! That seems like a good solution in the long run.<br>
Suppose I wanted to rebuild the TVTK, how would I proceed?</p>

---

## Post #4 by @lassoan (2020-01-29 20:04 UTC)

<p>Download <a href="https://github.com/Slicer/Slicer/blob/f37e82ae51ee9b4caf730138aee66d74d824b6d5/SuperBuild/External_VTK.cmake#L117-L125">Slicer’s VTK version from github</a> and build TVTK with it according to TVTK build instructions.</p>
<p>It is important to use the exact same build options as Slicer, which might be somewhat tricky. You may try to build with default options and if you find the binaries incompatible (crash when you try to use TVTK) then build Slicer and then build TVTK using Slicer’s VTK.</p>
<p>You may also write to <a href="https://discourse.vtk.org">VTK forum</a>, asking for improving VTK’s Python wrapping by making VTK objects pickleable.</p>
<p>Do you do all these to just run some processing in the background?</p>

---

## Post #5 by @muratmaga (2020-02-02 22:28 UTC)

<p><a class="mention" href="/u/hkirvesl">@hkirvesl</a></p>
<p>Do you need this to run the auto3Dgm module independently for multiple cores? Did you consider CLI module alternative <a class="mention" href="/u/lassoan">@lassoan</a> suggested?</p>
<p>If you create a custom build of Slicer, you will not have access to extension platform (i.e., any extension will need to be build manually against your custom build).</p>

---

## Post #6 by @hkirvesl (2020-02-02 23:57 UTC)

<p>My interest in the custom build stemmed that since we are building a custom slicer to begin with, if solving the issue on that end is not an insurmountable task, that would give us parallelization in that custom build immediately. Clearly it is not a good long term solution.</p>
<p>We will need to be able to run the auto3dgm python package in parallel, but not the auto3dgm slicer module itself. So pass arguments with Slicer to the python package, which then runs it in parallel and returns the results.</p>
<p>For long term yes, I believe CLI module seems like a promising alternative, provided that the interfaces therein are easy enough for the audience to use. Another option would be refactoring the python package to use numpy arrays in lieu of tvtk objects.</p>

---
