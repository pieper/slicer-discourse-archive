# Converting .nrrd file to .stl (using python)

**Topic ID**: 24166
**Date**: 2022-07-03
**URL**: https://discourse.slicer.org/t/converting-nrrd-file-to-stl-using-python/24166

---

## Post #1 by @rbaheti (2022-07-03 22:22 UTC)

<p>Is there a way to convert .nrrd file to a .stl file on python?<br>
The nrrd file is binary (every voxel has a value of either 0 or 255).</p>

---

## Post #2 by @mau_igna_06 (2022-07-04 00:31 UTC)

<p>You should be able to do it using some kind of marching cubes filter</p>

---

## Post #3 by @BrentFoster (2022-07-05 15:09 UTC)

<p>Hi Ron</p>
<p>I think the below script should work for this, but let me know if you have any questions on it.</p>
<p>import vtk<br>
label = 255<br>
nrrd_file_path = “”<br>
output_stl_path = “”</p>
<p>reader = vtk.vtkNrrdReader()<br>
reader.SetFileName(nrrd_file_path)<br>
reader.Update()<br>
img = read.GetOutput()</p>
<p>marching_cubes_filter = vtk.vtkDiscreteMarchingCubes()<br>
marching_cubes_filter.SetInputData(img)<br>
marching_cubes_filter.SetValue(0, 255)<br>
marching_cubes_filter.Update()<br>
polydata = marching_cubes_filter.GetOutput()</p>
<p>writer = vtk.vtkSTLWriter()<br>
writer.SetInputData(polydata)<br>
writer.SetFileName(output_stl_path)<br>
writer.Write()</p>

---

## Post #4 by @lassoan (2022-07-05 16:06 UTC)

<p>If you want to see correctly reconstructed (smooth) surface then you can run these commands in Slicer’s Python environment:</p>
<pre><code class="lang-python">segmentation = slicer.util.loadSegmentation("/path/to/labelmap.nrrd")
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles("/path/to/folder", segmentation)
</code></pre>
<p>See more useful code snippets for loading, processing, saving data in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.htm">script repository</a>.</p>

---

## Post #5 by @rbaheti (2022-07-05 22:41 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
Thanks for the suggestion. I referred this <a href="https://kitware.github.io/vtk-examples/site/Python/VisualizationAlgorithms/HeadBone/" rel="noopener nofollow ugc">link</a> to see how to use VTK to convert a file to stl format. I made the following changes to the code to suit my needs:</p>
<pre><code class="lang-auto">def get_program_parameters():
    parser.add_argument('filename', help='Trial.stl.')

def main():
    reader.SetFileName("trial_file.seg.nrrd")
</code></pre>
<p>The code, however, gives parsing error. I don’t understand the nature of this error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc68b9a5634d8645a58ec4b27a9a9b09d9ec64ca.png" alt="image" data-base62-sha1="A0UH6puGsGOvKjZpWC76Cryjx2y" width="463" height="95"></p>

---

## Post #6 by @rbaheti (2022-07-05 22:44 UTC)

<p><a class="mention" href="/u/brentfoster">@BrentFoster</a><br>
Thanks for the suggestion. This was a very straightforward approach [changed read.GetOutput() to reader.GetOutput()]!<br>
It created an STL file but the file is “malformed” and fails to open (the file size is 1KB).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f483eeaeb500ac0cf210e2a8c432a338c58aad12.png" alt="image" data-base62-sha1="yT5akedVnl1S5AQHPA6eOZtozHI" width="501" height="171"></p>
<p>What exactly is going wrong?</p>

---

## Post #7 by @rbaheti (2022-07-05 22:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you for the suggestion. Just as BrentFoster’s suggestion, the code is straightforward and doesn’t give any error while execution but no file is created. This is the output on the Python interface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f397282c272ec00fef1b65fa20d2b4ad1679a64.png" data-download-href="/uploads/short-url/4sdSFV3cnthqd9BQlkueEGJVSMA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f397282c272ec00fef1b65fa20d2b4ad1679a64.png" alt="image" data-base62-sha1="4sdSFV3cnthqd9BQlkueEGJVSMA" width="690" height="16" data-dominant-color="F0F0FF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1418×33 2.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2022-07-06 00:40 UTC)

<p>The output path must be a folder, not a filename, because this method exports all the segments of the segmentation, each as a separate file in the specified folder.</p>

---

## Post #9 by @rbaheti (2022-07-06 00:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for the reply!</p>
<p>To streamline the method I’m implementing is there a way to execute these commands on Spyder or Jupyter Notebook?</p>

---

## Post #10 by @lassoan (2022-07-06 01:05 UTC)

<p>Yes, sure, you can <a href="https://github.com/Slicer/SlicerJupyter">use Slicer as a Jupyter Notebook kernel</a>.</p>

---
