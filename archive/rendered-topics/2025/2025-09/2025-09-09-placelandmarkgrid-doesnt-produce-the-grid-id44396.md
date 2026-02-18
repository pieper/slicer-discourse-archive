# PlaceLandmarkGrid doesn't produce the grid

**Topic ID**: 44396
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/placelandmarkgrid-doesnt-produce-the-grid/44396

---

## Post #1 by @kuoi (2025-09-09 02:46 UTC)

<p>Hello I am using PlaceLandmarkGrid in Slicer Morph on Linux, version c944db9 (2025-06-26)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b17eeeb52c135a7341ec33983ed0135a952bb054.png" data-download-href="/uploads/short-url/pkcsKP01bHoOjLUKovaIvkdtUSU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b17eeeb52c135a7341ec33983ed0135a952bb054.png" alt="image" data-base62-sha1="pkcsKP01bHoOjLUKovaIvkdtUSU" width="651" height="404"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">651×404 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to generate semi-landmarks on a grid from existing points, but instead of obtaining a grid containing the semi-landmarks as shown in the tutorial, I only ended up with <code>gridPatch_0</code> groups without the expected grid.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c55ab1a34376a7afd3fff5d41e67f8e0d75f7e7b.png" data-download-href="/uploads/short-url/s9Sn5J4JJQwRgUG5GEu1ZyXjIlt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55ab1a34376a7afd3fff5d41e67f8e0d75f7e7b_2_613x500.png" alt="image" data-base62-sha1="s9Sn5J4JJQwRgUG5GEu1ZyXjIlt" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55ab1a34376a7afd3fff5d41e67f8e0d75f7e7b_2_613x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c55ab1a34376a7afd3fff5d41e67f8e0d75f7e7b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c55ab1a34376a7afd3fff5d41e67f8e0d75f7e7b.png 2x" data-dominant-color="E9ECF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×538 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>screenshot as below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eea9318976a055f149e9c8f44d35991f83b73c79.jpeg" data-download-href="/uploads/short-url/y3i8gHrUbhHhDuF125ifJY7KH6p.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eea9318976a055f149e9c8f44d35991f83b73c79_2_368x500.jpeg" alt="image" data-base62-sha1="y3i8gHrUbhHhDuF125ifJY7KH6p" width="368" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eea9318976a055f149e9c8f44d35991f83b73c79_2_368x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eea9318976a055f149e9c8f44d35991f83b73c79.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eea9318976a055f149e9c8f44d35991f83b73c79.jpeg 2x" data-dominant-color="C3B8BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">409×555 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-09 02:53 UTC)

<p>Is there anything in the error log? It is not possible to tell what the issue might be from these screenshots.</p>
<p>Is it working correctly with the sample data provided in the tutorial?</p>

---

## Post #3 by @kuoi (2025-09-09 02:54 UTC)

<p>I tried example data, it still can’t</p>

---

## Post #4 by @muratmaga (2025-09-09 02:57 UTC)

<p>It is working for me with the sample data and tutorial. For the record, this is the tutorial I am using.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/GridBasedLandmarking">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GridBasedLandmarking" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/GridBasedLandmarking" target="_blank" rel="noopener">Tutorials/GridBasedLandmarking at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>What is your Slicer version and your operating system?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b2d87d85bb32cf4a66b27fe04a4e4590d85858.jpeg" data-download-href="/uploads/short-url/2OgfjvekPFZu01VGQ22izEZWOAo.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13b2d87d85bb32cf4a66b27fe04a4e4590d85858_2_690x379.jpeg" alt="image" data-base62-sha1="2OgfjvekPFZu01VGQ22izEZWOAo" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13b2d87d85bb32cf4a66b27fe04a4e4590d85858_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13b2d87d85bb32cf4a66b27fe04a4e4590d85858_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b2d87d85bb32cf4a66b27fe04a4e4590d85858.jpeg 2x" data-dominant-color="D5D6C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1140×627 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @kuoi (2025-09-09 03:02 UTC)

<p>I can attach the error log, I guess there are something</p>
<p>I am using archlinux and 5.8.1 slicer, I can’t find any error report are newly introduced when I used the module. Yeah, I am using this tutorail</p>
<p>But there are some related</p>
<pre><code class="lang-auto">
AddNewNodeByClass: failed to create node by class vtkMRMLMarkupsGridSurfaceNode


Traceback (most recent call last):
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 324, in initializeInteractivePatch
    self.onSampleGrid()
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 275, in onSampleGrid
    self.patch.initializeGrid(gridResolution)
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 472, in initializeGrid
    self.gridNode.SetOutputSurfaceModelNodeID(self.gridModel.GetID())
AttributeError: 'NoneType' object has no attribute 'SetOutputSurfaceModelNodeID'
AddNewNodeByClass: failed to create node by class vtkMRMLMarkupsGridSurfaceNode


Traceback (most recent call last):
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 263, in onResampleGrid
    self.patch.initializeGrid(gridResolution)
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 472, in initializeGrid
    self.gridNode.SetOutputSurfaceModelNodeID(self.gridModel.GetID())
AttributeError: 'NoneType' object has no attribute 'SetOutputSurfaceModelNodeID'
Switch to module:  "Data"
Switch to module:  "PlaceLandmarkGrid"
</code></pre>

---

## Post #6 by @muratmaga (2025-09-09 03:05 UTC)

<p>Is this error message generated while using the tutorial with the provided mouse skull?</p>
<p>Because it is working for me on Linux with the 5.8.1 perfectly fine.</p>

---

## Post #7 by @kuoi (2025-09-09 03:06 UTC)

<p>Yeah, it generate the same thing</p>

---

## Post #8 by @kuoi (2025-09-09 03:09 UTC)

<p>Additionally information, when the software starts</p>
<pre><code class="lang-auto">
Session start time .......: 20250909_130843
Slicer version ...........: 5.8.1-2025-03-02 (revision 33241 / 11eaf62) linux-amd64 - installed release
Operating system .........: Linux / 6.12.45-1-lts / #1 SMP PREEMPT_DYNAMIC Thu, 04 Sep 2025 17:54:55 +0000 / UTF-8 - 64-bit
Memory ...................: 15707 MB physical, 14999 MB virtual
CPU ......................: GenuineIntel Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz, 4 cores, 8 logical processors
VTK configuration ........: OpenGL2 rendering, TBB threading
Qt configuration .........: version 5.15.17, with SSL, requested OpenGL 3.2 (core profile)
DCMTK configuration ......: version 3.6.8, no SSL
Internationalization .....: disabled, language=
Developer mode ...........: disabled
Application path .........: /opt/3dslicer/bin
Additional module paths ..: /home/guoyi/.config/slicer.org/Extensions-33241/SegmentEditorExtraEffects/lib/Slicer-5.8/qt-loadable-modules, /home/guoyi/.config/slicer.org/Extensions-33241/SegmentEditorExtraEffects/lib/Slicer-5.8/qt-scripted-modules, /home/guoyi/.config/slicer.org/Extensions-33241/SurfaceMarkup/lib/Slicer-5.8/qt-loadable-modules, /home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules, /home/guoyi/.config/slicer.org/Extensions-33241/MarkupsToModel/lib/Slicer-5.8/qt-loadable-modules
  Error(s):
    Cannot load library /home/guoyi/.config/slicer.org/Extensions-33241/SurfaceMarkup/lib/Slicer-5.8/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.so: (libarchive.so.19: cannot open shared object file: No such file or directory)
  Error(s):
    Cannot load library /home/guoyi/.config/slicer.org/Extensions-33241/MarkupsToModel/lib/Slicer-5.8/qt-loadable-modules/libqSlicerMarkupsToModelModule.so: (libarchive.so.19: cannot open shared object file: No such file or directory)
libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
libarchive.so.19: cannot open shared object file: No such file or directory
Collecting mistune
  Using cached mistune-3.1.4-py3-none-any.whl.metadata (1.8 kB)
Requirement already satisfied: typing-extensions in /opt/3dslicer/lib/Python/lib/python3.9/site-packages (from mistune) (4.12.1)
Using cached mistune-3.1.4-py3-none-any.whl (53 kB)
Installing collected packages: mistune
ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/opt/3dslicer/lib/Python/lib/python3.9/site-packages/mistune'
Consider using the `--user` option or check the permissions.

Traceback (most recent call last):
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/SlicerMorphTutorials.py", line 9, in &lt;module&gt;
    import mistune
ModuleNotFoundError: No module named 'mistune'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/3dslicer/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/SlicerMorphTutorials.py", line 11, in &lt;module&gt;
    slicer.util.pip_install('mistune')
  File "/opt/3dslicer/bin/Python/slicer/util.py", line 3942, in pip_install
    _executePythonModule("pip", args)
  File "/opt/3dslicer/bin/Python/slicer/util.py", line 3896, in _executePythonModule
    logProcessOutput(proc)
  File "/opt/3dslicer/bin/Python/slicer/util.py", line 3862, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/opt/3dslicer/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'mistune']' returned non-zero exit status 1.
loadSourceAsModule - Failed to load file "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/SlicerMorphTutorials.py"  as module "SlicerMorphTutorials" !
Fail to instantiate module  "SlicerMorphTutorials"
The following modules failed to be instantiated:
   SlicerMorphTutorials
Scripted subject hierarchy plugin registered: SegmentEditor
Scripted subject hierarchy plugin registered: SegmentStatistics
Switch to module:  "Welcome"
Scripted subject hierarchy plugin registered: FormatMarkups
Adding SlicerMorph Volume Rendering Presets
</code></pre>

---

## Post #9 by @muratmaga (2025-09-09 03:14 UTC)

<p>You have a bunch of errors, including not being able to load the SurfaceMarkups extension that PlaceGridLandmark tool requires.</p>
<p>Error(s): Cannot load library /home/guoyi/.config/slicer.org/Extensions-33241/SurfaceMarkup/lib/Slicer-5.8/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.so: (libarchive.so.19: cannot open shared object file: No such file or directory) Error(s): Cannot load library /home/guoyi/.config/slicer.org/Extensions-33241/MarkupsToModel/lib/Slicer-5.8/qt-loadable-modules/libqSlicerMarkupsToModelModule.so: (libarchive.so.19: cannot open shared object file: No such file or directory) libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space libarchive.so.19: cannot open shared object file: No such file or directory Collecting mistune</p>
<p>I noticed that you have installed slicer to a location that might be read-only (/opt/slicer). I suggest trying to download and install slicer somewhere within your home directory (like your desktop) and retry.</p>

---

## Post #10 by @kuoi (2025-09-09 03:15 UTC)

<p>I tried to use ln -s to  solve .so problem, and it doesn’t report this error now, I think, it still has quite a lot of problems.</p>

---

## Post #11 by @muratmaga (2025-09-09 03:16 UTC)

<p>All I can say it works perfectly fine in ubuntu 24.04. I am not familiar with archlinux. But without the SurfaceMarkups extension working correctly, our tool will not work.</p>
<p>Also as I said, unless you install slicer to a folder where your account has write permission, things will continue not to work:</p>
<pre><code class="lang-auto">ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/opt/3dslicer/lib/Python/lib/python3.9/site-packages/mistune'
</code></pre>

---

## Post #12 by @kuoi (2025-09-09 03:24 UTC)

<p>I gave that permission now… then error reports still</p>
<pre><code class="lang-auto">
ReadDataInternal (vtkMRMLModelStorageNode2): File /home/guoyi/Downloads/PhD/wes/morphology/3ddata/Thersites.obj does not contain coordinate system information. Assuming LPS.


vtkMRMLMarkupsJsonIO::ReadFromFile: Error opening the file '/home/guoyi/Downloads/PhD/wes/morphology/3ddata/gridOutline_6.mrk.json'


vtkMRMLMarkupsJsonStorageNode::ReadDataInternal: Error: Error opening the file '/home/guoyi/Downloads/PhD/wes/morphology/3ddata/gridOutline_6.mrk.json'



vtkMRMLStorageNode::ReadData: Failed to read node gridOutline_6 (vtkMRMLMarkupsClosedCurveNode7) from filename='/home/guoyi/Downloads/PhD/wes/morphology/3ddata/gridOutline_6.mrk.json'


static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection*) Errors occurred while loading nodes: "Error: Loading /home/guoyi/Downloads/PhD/wes/morphology/3ddata/2025-09-08-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326\nvtkMRMLMarkupsClosedCurveNode (0x5ed9505485c0): vtkMRMLStorableNode::UpdateScene failed: Failed to read node gridOutline_6 (vtkMRMLMarkupsClosedCurveNode7) using storage node vtkMRMLMarkupsJsonStorageNode50.\n"
Switch to module:  "Data"
Switch to module:  "PlaceLandmarkGrid"
Generic Warning: In vtkProjectMarkupsCurvePointsFilter.cxx, line 208
No intersections found for 2 points for curve 


Generic Warning: In vtkProjectMarkupsCurvePointsFilter.cxx, line 208
No intersections found for 5 points for curve 


AddNewNodeByClass: failed to create node by class vtkMRMLMarkupsGridSurfaceNode


Traceback (most recent call last):
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 324, in initializeInteractivePatch
    self.onSampleGrid()
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 275, in onSampleGrid
    self.patch.initializeGrid(gridResolution)
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 472, in initializeGrid
    self.gridNode.SetOutputSurfaceModelNodeID(self.gridModel.GetID())
AttributeError: 'NoneType' object has no attribute 'SetOutputSurfaceModelNodeID'
</code></pre>

---

## Post #13 by @kuoi (2025-09-09 03:26 UTC)

<p>Whenever, I tried to adjust the resolution for landmark grid, it reports</p>
<pre><code class="lang-auto">
AddNewNodeByClass: failed to create node by class vtkMRMLMarkupsGridSurfaceNode


Traceback (most recent call last):
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 207, in onSampleRateChanged
    self.onResampleGrid()
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 263, in onResampleGrid
    self.patch.initializeGrid(gridResolution)
  File "/home/guoyi/.config/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/PlaceLandmarkGrid.py", line 472, in initializeGrid
    self.gridNode.SetOutputSurfaceModelNodeID(self.gridModel.GetID())
AttributeError: 'NoneType' object has no attribute 'SetOutputSurfaceModelNodeID'
</code></pre>

---

## Post #14 by @kuoi (2025-09-09 03:33 UTC)

<p>I can see the problem is that the complied version based on source code has different behaviour with the pre-compiled version … again, similar to FIJI things. Thanks for your help <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #15 by @muratmaga (2025-09-09 03:37 UTC)

<p>Looks like there is a library incompatibility. You have couple options</p>
<ol>
<li>You can try to build the Slicer from the source code locally with all the necessary extensions.</li>
<li>You can try the latest preview build (recently Slicer build environment has been modified to support more recent linux environments and deal with ABI issues)</li>
<li>Use ubuntu.</li>
</ol>

---

## Post #16 by @kuoi (2025-09-09 05:21 UTC)

<p>Thanks for your suggestions, I swtiched to the pre-compiled verrsion, then works well. However, I still have some questions. For example</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/250374c867bb2cb09067298fc26dc74c64f32f01.png" data-download-href="/uploads/short-url/5hr4pRxpjce4fL4g93sr7NkRkwV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/250374c867bb2cb09067298fc26dc74c64f32f01_2_459x499.png" alt="image" data-base62-sha1="5hr4pRxpjce4fL4g93sr7NkRkwV" width="459" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/250374c867bb2cb09067298fc26dc74c64f32f01_2_459x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/250374c867bb2cb09067298fc26dc74c64f32f01.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/250374c867bb2cb09067298fc26dc74c64f32f01.png 2x" data-dominant-color="705A6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">520×566 48.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>semi-landmark distribute like this, it seeems look not bad, however it doesn’t match the surface of shell.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc5d67d5e05d726c8191198d0222c62e4e768a0.jpeg" data-download-href="/uploads/short-url/kvS8VcJ3VOrhqzq3U6qUlDjJd16.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fc5d67d5e05d726c8191198d0222c62e4e768a0_2_459x499.jpeg" alt="image" data-base62-sha1="kvS8VcJ3VOrhqzq3U6qUlDjJd16" width="459" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fc5d67d5e05d726c8191198d0222c62e4e768a0_2_459x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc5d67d5e05d726c8191198d0222c62e4e768a0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fc5d67d5e05d726c8191198d0222c62e4e768a0.jpeg 2x" data-dominant-color="A99EA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">520×566 94.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could I get some suggestions?</p>

---

## Post #17 by @kuoi (2025-09-09 05:49 UTC)

<p>I also found that inner surface may influence the landmark distribution, making it unreasonable</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123a186e272a7095786267569158c5cb4c351651.png" data-download-href="/uploads/short-url/2Bf3Vx9PgGcqaKDIGMcl6hXQv7P.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123a186e272a7095786267569158c5cb4c351651_2_690x298.png" alt="image" data-base62-sha1="2Bf3Vx9PgGcqaKDIGMcl6hXQv7P" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123a186e272a7095786267569158c5cb4c351651_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123a186e272a7095786267569158c5cb4c351651_2_1035x447.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123a186e272a7095786267569158c5cb4c351651_2_1380x596.png 2x" data-dominant-color="B4B7DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1724×747 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and with model, it looks like this, is any solution to manually adjust this situlation?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3ddf717bd2c32bb2cb2ea225f14d6830cc067c1c.jpeg" data-download-href="/uploads/short-url/8PlQKhEx1aNSPZWOpy6ryUhRB0w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3ddf717bd2c32bb2cb2ea225f14d6830cc067c1c.jpeg" alt="image" data-base62-sha1="8PlQKhEx1aNSPZWOpy6ryUhRB0w" width="424" height="389"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">424×389 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @muratmaga (2025-09-09 14:45 UTC)

<aside class="quote no-group" data-username="kuoi" data-post="16" data-topic="44396">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>Could I get some suggestions?</p>
</blockquote>
</aside>
<p>In this situation, you can manually adjust the middle blue points to create a spline. So for example the middle blue point between 1 and 2 can be moved to closer to your coil stitch. This will force all interpolated points to follow that spline.</p>
<p>The tool only generatea a rectangular patch initially (based on that four corner points and the underlying surface) If the surface has high complexity like yours, you will have to manually move those points for semi-landmarks to follow the surface more closely.</p>

---

## Post #19 by @muratmaga (2025-09-09 14:47 UTC)

<aside class="quote no-group" data-username="kuoi" data-post="17" data-topic="44396">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>I also found that inner surface may influence the landmark distribution, making it unreasonable</p>
</blockquote>
</aside>
<p>Inner surface shouldn’t influence the landmark distribution. However they way you do the sequence of corner landmakrs, and the surface normals would. Sometime semilandmarks gets projected to the inner surface (if the surface normals are inverted or some other reason). If that’s the case simply hit the <strong>Flip Grid Orientation</strong> to corrrect it.</p>

---
