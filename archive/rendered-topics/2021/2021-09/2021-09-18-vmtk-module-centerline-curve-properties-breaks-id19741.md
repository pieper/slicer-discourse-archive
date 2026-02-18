# Vmtk Module - Centerline curve/properties Breaks

**Topic ID**: 19741
**Date**: 2021-09-18
**URL**: https://discourse.slicer.org/t/vmtk-module-centerline-curve-properties-breaks/19741

---

## Post #1 by @adamgranthendry (2021-09-18 22:50 UTC)

<p>When creating a vessel centerline, I can create a model, but when I check to have the curve or properties output, the program hangs and dies.</p>
<p>I am using 3D Slicer 4.13.0-2021-09-16</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b74ca2c68ce8baa10c33f7955810d39258800d37.png" data-download-href="/uploads/short-url/q9xzfNFq312us37C6pPimcl52cv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b74ca2c68ce8baa10c33f7955810d39258800d37_2_690x377.png" alt="image" data-base62-sha1="q9xzfNFq312us37C6pPimcl52cv" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b74ca2c68ce8baa10c33f7955810d39258800d37_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b74ca2c68ce8baa10c33f7955810d39258800d37_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b74ca2c68ce8baa10c33f7955810d39258800d37_2_1380x754.png 2x" data-dominant-color="8587AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1399 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @adamgranthendry (2021-09-18 23:00 UTC)

<p>The <code>Network Curve</code> features work flawlessly. I’m a little vague on the differences between the <code>Network</code> output vs. the <code>Tree</code> output . What is the difference?</p>

---

## Post #3 by @chir.set (2021-09-19 09:53 UTC)

<aside class="quote no-group" data-username="adamgranthendry" data-post="1" data-topic="19741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamgranthendry/48/12180_2.png" class="avatar"> adamgranthendry:</div>
<blockquote>
<p>the program hangs and dies.</p>
</blockquote>
</aside>
<p>Have you created endpoints using the ‘auto-detect’ feature ?</p>
<p>I do see constant crashes when using this feature, both when creating centerline models and centerline curves. You could either adjust the positions of your endpoints or place them all manually. In the latter placement mode, no crashes were seen, even with multiple endpoints.</p>
<p>It does not crash with Network extraction as this does not require any endpoints.</p>
<p>The crash in a debugger is quite weird, no backtrace could be obtained with Slicer and VMTK built with RelWithDebInfo configuration option, just a stdout :</p>
<pre><code class="lang-auto">"Segmentation" Reader has successfully read the file "/home/user/tmp/Slicer/test6/Segmentation.seg.nrrd" "[0.06s]"
Switch to module:  "ExtractCenterline"
Found CommandLine Module, target is  /home/user/programs/Slicer/bin/../lib/Slicer-4.13/cli-modules/Decimation
ModuleType: CommandLineModule
Decimation command line: 

/home/user/programs/Slicer/bin/../lib/Slicer-4.13/cli-modules/Decimation --reductionFactor 0.341412 --method FastQuadric --deleteBoundary --aggressiveness 4 /tmp/Slicer/BEBGA_vtkMRMLModelNodeE.obj /tmp/Slicer/BEBGA_vtkMRMLModelNodeF.obj 

Process 14160 stopped and restarted: thread 1 received signal: SIGCHLD
Decimation standard output:

Input: 7592 vertices,15180 triangles (target 9997)
Output: 5000 vertices,9996 triangles (0.341502 reduction)

Decimation completed without errors

ReadDataInternal (vtkMRMLModelStorageNode1): File /tmp/Slicer/BEBGA_vtkMRMLModelNodeF.obj does not contain coordinate system information. Assuming LPS.


Found CommandLine Module, target is  /home/user/programs/Slicer/bin/../lib/Slicer-4.13/cli-modules/Decimation
ModuleType: CommandLineModule
Decimation command line: 

/home/user/programs/Slicer/bin/../lib/Slicer-4.13/cli-modules/Decimation --reductionFactor 0.341412 --method FastQuadric --deleteBoundary --aggressiveness 4 /tmp/Slicer/BEBGA_vtkMRMLModelNodeG.obj /tmp/Slicer/BEBGA_vtkMRMLModelNodeH.obj 

Process 14160 stopped and restarted: thread 1 received signal: SIGCHLD
Decimation standard output:

Input: 7592 vertices,15180 triangles (target 9997)
Output: 5000 vertices,9996 triangles (0.341502 reduction)

Decimation completed without errors

ReadDataInternal (vtkMRMLModelStorageNode2): File /tmp/Slicer/BEBGA_vtkMRMLModelNodeH.obj does not contain coordinate system information. Assuming LPS.


Warning: In /home/arc/src/SlicerExtension-VMTK-SuperBuild9/VMTK/vtkVmtk/ComputationalGeometry/vtkvmtkSteepestDescentLineTracer.cxx, line 213
vtkvmtkSteepestDescentLineTracer (0x55555d9610a0): Can't find a steepest descent edge. Target not reached.


Error while constructing cell map: Invalid cell size for lines.


error: libstdc++.so.6 {0x00181389}: DIE has DW_AT_ranges(0x119c8) attribute, but range extraction failed (missing or invalid range list table), please file a bug and attach the file at the start of this error message
Fatal Python error: init_import_site: Failed to import the site module
Python runtime state: initialized
Traceback (most recent call last):
  File "/home/user/programs/Slicer/bin/../lib/Python/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/home/user/programs/Slicer/bin/../lib/Python/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/home/user/programs/Slicer/bin/../lib/Python/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/home/user/programs/Slicer/bin/../lib/Python/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/home/user/programs/Slicer/bin/../lib/Python/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/home/user/programs/Slicer/lib/Python/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/home/user/programs/Slicer/lib/Python/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/home/user/programs/Slicer/lib/Python/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata__linux_x86_64-linux-gnu'
</code></pre>
<p>At least one <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/41#issue-987071072" rel="noopener nofollow ugc">other</a> crash context has been seen.</p>
<p>This centerline extraction is very, very complex, you’ll agree if you just quickly overview the source code. We may adapt our workflow to do what’s working as is, and much of it is awesome. Corner cases will have to be dealt with per-case.</p>
<aside class="quote no-group" data-username="adamgranthendry" data-post="2" data-topic="19741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamgranthendry/48/12180_2.png" class="avatar"> adamgranthendry:</div>
<blockquote>
<p>What is the difference?</p>
</blockquote>
</aside>
<p>I would like to know it also, core developers may jump in here.</p>
<p>Incidentally, does the model in your image originate from a human ? It’s hard to completely map it to known anatomy. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @adamgranthendry (2021-09-19 16:40 UTC)

<blockquote>
<p>Have you created endpoints using the ‘auto-detect’ feature ?</p>
</blockquote>
<p>No, these were set manually</p>
<blockquote>
<p>It does not crash with Network extraction as this does not require any endpoints.</p>
</blockquote>
<p>Why does it not require any endpoints?</p>
<blockquote>
<p>Incidentally, does the model in your image originate from a human?</p>
</blockquote>
<p>This is a typical neuro model.</p>
<p>Additionally, even with Network model/curve/properties, I get memory leak errors when I close 3D Slicer:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e01e72ce66feb5021ab1aad7d9d6d7c9e5678b4d.png" alt="image" data-base62-sha1="vYEbIapwWFRPjPTJbyrwFNX5Sbz" width="405" height="275"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3c735b19b1b88f00ca21a54f0da7708fe6f21c1.png" alt="image" data-base62-sha1="yMyPtn19zNnoISytB99oNN05qKZ" width="402" height="252"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aae687bdaefbfc6015bb1606349058360df580e.png" alt="image" data-base62-sha1="3O2550vFj16K4xZ8eIyQPk5BmlU" width="382" height="183"></p>

---
