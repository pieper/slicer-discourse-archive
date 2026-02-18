# vmtkcenterlines openprofiles issue

**Topic ID**: 21906
**Date**: 2022-02-11
**URL**: https://discourse.slicer.org/t/vmtkcenterlines-openprofiles-issue/21906

---

## Post #1 by @hemjo (2022-02-11 03:49 UTC)

<p>I am trying to use vmtkcenterlines, but even on the test data <code>aorta-surface-open-ends.stl</code> when I run</p>
<pre><code class="lang-auto">vmtksurfacereader -ifile aorta-surface-open-ends.stl --pipe vmtkcenterlines -seedselector openprofiles -endpoints 1 -ofile aorta-ctl.vtk
</code></pre>
<p>I get an error after closing the GUI (not sure why it shows up in the first place). Am I using this wrong? I’d expect it to find centerlines connecting each opening to the others. I have installed version 1.5 from <code>conda-forge</code> on Fedora 34.</p>
<pre><code class="lang-auto">Please input list of inlet profile ids: Traceback (most recent call last):
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/pypeserver.py", line 48, in RunPypeProcess
    pipe.Execute()
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/pype.py", line 324, in Execute
    scriptObject.Execute()
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/vmtkcenterlines.py", line 601, in Execute
    self.SeedSelector.Execute()
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/vmtkcenterlines.py", line 312, in Execute
    self._SourceSeedIds.InsertNextId(int(seedIdString.strip()))
ValueError: invalid literal for int() with base 10: ''
</code></pre>
<p>Full output</p>
<pre><code class="lang-auto">Automatic piping vmtksurfacereader
Parsing options vmtksurfacereader
    InputFileName = aorta-surface-open-ends.stl
Explicit piping vmtksurfacereader
Input vmtksurfacereader members:
    Id = 0
    Disabled = 0
    Format = 
    GuessFormat = 1
    Surface = 0
    InputFileName = aorta-surface-open-ends.stl
    SurfaceOutputFileName = 
Executing vmtksurfacereader ...
Reading STL surface file.
Done executing vmtksurfacereader.
Output vmtksurfacereader members:
    Id = 0
    Surface = vtkPolyData

Automatic piping vmtkcenterlines
    Surface = vmtksurfacereader-0.Surface
Parsing options vmtkcenterlines
    SeedSelectorName = openprofiles
    AppendEndPoints = 1
    AppendEndPoints = 1
    CenterlinesOutputFileName = aorta-ctl.vtk
Explicit piping vmtkcenterlines
Input vmtkcenterlines members:
    Id = 0
    Disabled = 0
    Surface = vtkPolyData
    SurfaceInputFileName = 
    SeedSelectorName = openprofiles
    SourceIds = []
    TargetIds = []
    SourcePoints = []
    TargetPoints = []
    AppendEndPoints = 1
    CheckNonManifold = 0
    FlipNormals = 0
    CapDisplacement = 0.0
    DelaunayTolerance = 0.001
    RadiusArrayName = MaximumInscribedSphereRadius
    AppendEndPoints = 1
    Resampling = 0
    ResamplingStepLength = 1.0
    DelaunayTessellation = None
    SimplifyVoronoi = 0
    UseTetGen = 0
    TetGenDetectInter = 1
    CostFunction = 1/R
    vmtkRenderer = None
    PoleIds = None
    VoronoiDiagram = None
    VoronoiDiagramInputFileName = 
    StopFastMarchingOnReachingTarget = 0
    CenterlinesOutputFileName = aorta-ctl.vtk
    DelaunayTessellationOutputFileName = 
    VoronoiDiagramOutputFileName = 
Executing vmtkcenterlines ...
Cleaning surface.
Triangulating surface.
Capping surface.
Quit renderer
Please input list of inlet profile ids: Traceback (most recent call last):
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/pypeserver.py", line 48, in RunPypeProcess
    pipe.Execute()
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/pype.py", line 324, in Execute
    scriptObject.Execute()
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/vmtkcenterlines.py", line 601, in Execute
    self.SeedSelector.Execute()
  File "/home/user/anaconda3/envs/vmtkcf/lib/python3.7/site-packages/vmtk/vmtkcenterlines.py", line 312, in Execute
    self._SourceSeedIds.InsertNextId(int(seedIdString.strip()))
ValueError: invalid literal for int() with base 10: ''
</code></pre>

---

## Post #2 by @ramtingh (2022-02-11 09:19 UTC)

<p>openprofiles isn’t automated, it opens the GUI so you can manually select the inlets and outlets.</p>

---

## Post #3 by @ramtingh (2022-02-11 09:22 UTC)

<p>Have a look at the options available (<a href="http://www.vmtk.org/vmtkscripts/vmtkcenterlines.html" class="inline-onebox" rel="noopener nofollow ugc">vmtk - the Vascular Modelling Toolkit</a>), in most cases you’d need to provide the Ids or points for the inlets/outlets yourself. <code>carotidprofiles</code> would be the only as far as I know to select them automatically.</p>

---

## Post #4 by @hemjo (2022-02-11 11:43 UTC)

<p>Thanks <a class="mention" href="/u/ramtingh">@ramtingh</a>  for the tips. What happens is the display pops up to show the geometry and open profiles. With no prompt, but after hitting q, the selection prompt briefly shows up and the immediately closes before I am able to enter the inlet id. I have reproduced this on Ubuntu 20.04 as well.</p>

---

## Post #5 by @ramtingh (2022-02-11 22:57 UTC)

<p>I see, that’s not supposed to behave that way. I’m not sure yet if it is a vmtk problem (probably caused by moving to vtk 9) or a conda packaging problem, but the renderer  doesn’t seem to be waiting for inputs and just accepting empty strings. I’ll look into it.</p>

---

## Post #6 by @lassoan (2022-02-12 05:28 UTC)

<p>Vessel segmentation and centerline extraction is an interactive process. The scripts that come with VMTK and implement some interactions are very extremely limited. I always use 3D Slicer as GUI for doing any interactive operations with VMTK.</p>
<p>For centerline extraction there is a very convenient, full-featured module: it can detect automatic vessel endpoints automatically, then each can be interactively moved/deleted/toggled between inflow/outflow. It can check errors in the input mesh, optimize the input mesh so that extraction becomes magnitudes faster, and then it uses network and/or centerline extraction method to get the centerlines.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>

<p>There are other modules with convenient GUI that can use the computed centerline for exploring, reslicing the input image, quantify the curve, straighten the curve, etc.</p>

---
