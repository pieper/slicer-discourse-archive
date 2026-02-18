# RAS to IJK conversion issues

**Topic ID**: 41863
**Date**: 2025-02-24
**URL**: https://discourse.slicer.org/t/ras-to-ijk-conversion-issues/41863

---

## Post #1 by @patricklynch7 (2025-02-24 23:42 UTC)

<p>Hey guys,</p>
<p>I have a series of nifti files, Slicer mrml files, and the .mrk.json files corresponding to their respective annotated control points. I am having trouble recovering the correct coordinates/IJK plane that were used in Slicer during the annotation process. I know the output control points in the .mrk.json files are LPS, which I first convert to RAS. Then to recover the IJK voxel coordinates from RAS, I do something like:</p>
<pre><code class="lang-auto">    brain = nib.load(path)
    affine = brain.affine 
    ras_to_ijk = np.linalg.inv(affine)

    RAS_homog = np.array([R, A, S, 1])
    ijk_homog = ras_to_ijk @ RAS_homog
    IJK_point = np.round(ijk_homog[:3]).astype(int)
</code></pre>
<p>I expect to see that all the IJK control points should be fixed in one dimension since they are on the same plane (like they were annotated), but they often vary instead.</p>
<p>My question is, should I not be using the original nifti affine matrix? Should I be extracting the ijkToRASDirections property from the mrml file to use for something instead? Perhaps there are other mistakes I might be overlooking.</p>
<p>Sorry for the beginner question. Any and all help or pointers would be very much appreciated. Thanks so much.</p>

---

## Post #2 by @muratmaga (2025-02-25 06:29 UTC)

<p>I used Bing copilot to generate this code, and it seems to work as expected. The control points that are in the same slice share common IJK coordinate values:</p>
<pre><code class="lang-auto">import slicer
import numpy as np
import vtk

# Get the Markup object F
markup_node = slicer.util.getNode('F')

# Get the MRHead volume node
volume_node = slicer.util.getNode('MRHead')

# Get the IJK to RAS and RAS to IJK matrices
ijk_to_ras_matrix = vtk.vtkMatrix4x4()
ras_to_ijk_matrix = vtk.vtkMatrix4x4()
volume_node.GetIJKToRASMatrix(ijk_to_ras_matrix)
vtk.vtkMatrix4x4.Invert(ijk_to_ras_matrix, ras_to_ijk_matrix)

# Loop over each control point in the Markup object
for i in range(markup_node.GetNumberOfControlPoints()):
    # Get the RAS coordinates of the control point
    markup_ras_coordinate = [0, 0, 0]
    markup_node.GetNthControlPointPosition(i, markup_ras_coordinate)
    
    # Convert the markup RAS coordinate to IJK coordinate
    markup_ras = np.array(markup_ras_coordinate + [1])
    markup_ijk = ras_to_ijk_matrix.MultiplyPoint(markup_ras)
    markup_ijk = np.round(markup_ijk[:3]).astype(int)
    
    print(f'Control Point {i+1}: RAS coordinate {markup_ras_coordinate}, Pixel coordinate {tuple(markup_ijk)}')
</code></pre>

---

## Post #3 by @patricklynch7 (2025-02-25 15:17 UTC)

<p>Thank you for the response! I think the issue for me is that I’m doing this analysis outside of 3D slicer, so the slicer package and all of its functions are not available to me (as far as I’m aware).</p>
<p>I’m wondering if I can accomplish the same thing with just the nifti, mrmrl, and mrk.json files, or if I should just bite the bullet the reformat all the outputs somehow within the 3D slicer software.</p>

---

## Post #4 by @cpinter (2025-02-25 15:21 UTC)

<p>The MRML infrastructure and the mrk.json format are specific to 3D Slicer. If you want exclusively Slicer-free advice I think the Slicer forum may not be the best place to ask <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>What prevents you from using Slicer? Are you in a hospital and cannot install it?</p>

---

## Post #5 by @patricklynch7 (2025-02-25 15:33 UTC)

<p>I just mean that I am trying to perform this conversion over ~10 mrk.jsons for ~50 nifti files each, so I was hoping to just do the conversion with a python script all at once as opposed to using the software to reformat each one.</p>
<p>If you don’t it will be that bad, I’ll trust you and just go the slicer software route instead.</p>
<p>Thanks again.</p>

---

## Post #6 by @cpinter (2025-02-25 15:44 UTC)

<p>If you use mrk.json you already use Slicer if I understand correctly. Fortunately Slicer has a Python console that lets you automate basically anything. So yes I do suggest that you use Slicer, but not one-by-one through the UI, but by scripting.</p>

---

## Post #7 by @muratmaga (2025-02-25 15:49 UTC)

<aside class="quote no-group" data-username="patricklynch7" data-post="5" data-topic="41863">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/patricklynch7/48/79547_2.png" class="avatar"> patricklynch7:</div>
<blockquote>
<p>d to using the software to reformat each one.</p>
</blockquote>
</aside>
<p>I am not sure why or what you will reformat. Slicer reads nifti as is, mrk.json is a Slicer specific file. All you have to do is to add a line to read the nifti and markup json to the script I provided and then iterate it over your volumes and markup objects. You can look at the Slicer script repository (or use copilots) have to add those one liners to load the data programmatically.</p>
<p>If you have created these files without using Slicer from other software, there might be your original issue of coordinates not correctly converting. That’s a completely separate issue.</p>

---
