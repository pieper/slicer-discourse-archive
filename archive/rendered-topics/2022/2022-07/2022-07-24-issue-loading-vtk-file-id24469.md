# Issue loading VTK file

**Topic ID**: 24469
**Date**: 2022-07-24
**URL**: https://discourse.slicer.org/t/issue-loading-vtk-file/24469

---

## Post #1 by @jsalas424 (2022-07-24 17:04 UTC)

<p>Hello,</p>
<p>I generated a VTK file  matlab using <a href="https://www.mathworks.com/matlabcentral/fileexchange/47814-vtkwrite-exports-various-2d-3d-data-to-paraview-in-vtk-file-format" rel="noopener nofollow ugc">vtkwrite</a> from triangle mesh data.</p>
<p>The raw data looks like this:</p>
<pre><code class="lang-auto">16.2150000000000	13.2360000000000	126.065000000000
16.1490000000000	14.2370000000000	125.708000000000
16.8430000000000	13.7070000000000	125.851000000000
15.1780000000000	14.2980000000000	127.202000000000
16.7530000000000	14.3570000000000	125.554000000000
17.0650000000000	12.6940000000000	126.724000000000
16.1660000000000	12.0880000000000	126.873000000000
...............
</code></pre>
<p>Here’s the VTK exported file: <a href="https://pastebin.com/E9YH6KLq" class="inline-onebox" rel="noopener nofollow ugc"># vtk DataFile Version 2.0VTK from MatlabASCIIDATASET POLYDATAPOINTS 100 - Pastebin.com</a></p>
<p>When I load this into Slicer 5.0.3 it just crashes immediately</p>
<p>So I opened up Slicer 4.11.20210226 and got the following error:</p>
<pre><code class="lang-auto">- Error: Loading C:/.../mesh.vtk - ERROR: In D:\D\S\Slicer-1-build\VTK\IO\Legacy\vtkDataReader.cxx, line 3177
vtkPolyDataReader (000001BD00FACD60): Error reading ascii cell data! for file: C:/..../mesh.vtk
- Error: Loading C:/.../mesh.vtk - Failed to read node mesh_1 (vtkMRMLModelNode5) from filename='C:/.../mesh.vtk'
</code></pre>

---

## Post #2 by @pieper (2022-07-24 17:47 UTC)

<p>Someone here may be able to help, but this question would be better directed to a matlab forum (or if you really think the file is correct then the vtk forum, but I suspect the issue is how the matlab code created the file).</p>

---

## Post #3 by @jsalas424 (2022-07-24 19:15 UTC)

<p>I opened an issue with the vtkwrite Git here: <a href="https://github.com/joe-of-all-trades/vtkwrite/issues/5" class="inline-onebox" rel="noopener nofollow ugc">Issue loading vtkwrite-generated file into 3D Slicer · Issue #5 · joe-of-all-trades/vtkwrite · GitHub</a></p>
<p>Any other suggestions about how to generate a slicer-compatible VTK given x, y, z vertex coordinate data?</p>

---

## Post #4 by @jsalas424 (2022-07-24 21:46 UTC)

<p>This is solved. It was an issue with the VTK file. I’ve figured it out!</p>
<p>I was using the OpenEP platform to import CARTO data, so the following solution will be how to generate VTK’s from OpenEP using vtkwrite in Matlab.</p>
<pre><code class="lang-auto">x = userdata.surface.triRep.X(1:end,1);
y = userdata.surface.triRep.X(1:end,2);
z = userdata.surface.triRep.X(1:end,3);
vtkwrite('mesh.vtk','polydata','triangle',x,y,z,userdata.surface.triRep.Triangulation);
</code></pre>

---
