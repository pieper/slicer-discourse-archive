# Exporting fibre vector to other softwares

**Topic ID**: 4061
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/exporting-fibre-vector-to-other-softwares/4061

---

## Post #1 by @AzamAhmad (2018-09-11 13:09 UTC)

<p>Dear all,</p>
<p>I am a new user of 3D slicer, working mostly on brain MRI segmentation. So far, I’m quite happy with the tools provided in 3D slicer. I have a question regarding DT-MRI fibre bundle.</p>
<p>So far, I have managed to create fibre bundle (.vtk) file from DT-MRI images. I need to export the fibre vector (x,y,z components) to finite element software i.e. COMSOL. We typically need the fibre vector direction data in .csv file in order to export this. I noticed the fibre bundle can only be saved as .vtk, .vtp, .obj, .stl, and .ply. Is it possible to convert the fibre bundle into vector data in .csv or .txt.?</p>
<p>Thank you for all your assistance.</p>
<p>Best regards,<br>
Azam</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @ihnorton (2018-09-12 17:07 UTC)

<p>There is a PLY export tool (<code>Diffusion -&gt; Import and Export -&gt; Export Tractography to PLY (mesh)</code>), but a quick google suggests Comsol only supports STL.</p>
<p>If you want an ASCII format, the simplest option is to export as either .vtk text format, or .obj. Either of those will be a list of points, followed by lists of point-ids contained in each line (each line is a cell in vtk terminology).</p>
<ul>
<li>OBJ is simpler, because each point triplet is on a separate line</li>
<li>In ASCII VTK, all triplets are consecutive, read them by 3s. For ASCII .vtk, make sure to click “Show options” in the <code>Save Data</code> dialog, and uncheck the “Compress” button next to the .vtk file, or see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Enable_or_disable_compression_while_saving_a_volume">here</a> for how to do programmatically.</li>
</ul>
<p>If you want to do something else programmatically, I just added an example of how to iterate over lines in (almost) pure NumPy:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_tract_.28FiberBundle.29_streamline_points">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_tract_.28FiberBundle.29_streamline_points</a></li>
</ul>

---
