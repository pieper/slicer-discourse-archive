# Bad alloc when importing STL file as segmentation

**Topic ID**: 3184
**Date**: 2018-06-14
**URL**: https://discourse.slicer.org/t/bad-alloc-when-importing-stl-file-as-segmentation/3184

---

## Post #1 by @ferhue (2018-06-14 19:41 UTC)

<p>Hello, I am trying to import a 13 Mb big STL file as Segmentation, however I get a std::bad_alloc error, because I think the module tries to allocate 65 Gb of data. Any idea how to circumvent this? How can I change the default 1 mm spacing? See below the error log.</p>
<pre><code>Session start time .......: 2018-06-14 15:22:57
Slicer version ...........: 4.9.0-2018-06-11 (revision 27246) win-amd64 - installed release
Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
Memory ...................: 24573 MB physical, 28157 MB virtual
CPU ......................: GenuineIntel , 24 cores, 24 logical processors
VTK configuration ........: OpenGL2 rendering, TBB threading
Developer mode enabled ...: no
Prefer executable CLI ....: yes
Additional module paths ..: C:/Users/user/AppData/Roaming/NA-MIC/Extensions-27246/SlicerRT/lib/Slicer-4.9/cli-modules, C:/Users/user/AppData/Roaming/NA-MIC/Extensions-27246/SlicerRT/lib/Slicer-4.9/qt-loadable-modules, C:/Users/user/AppData/Roaming/NA-MIC/Extensions-27246/SlicerRT/lib/Slicer-4.9/qt-scripted-modules
Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
Scripted subject hierarchy plugin registered: Annotations
libpng warning: iCCP: known incorrect sRGB profile
Scripted subject hierarchy plugin registered: SegmentEditor
Scripted subject hierarchy plugin registered: SegmentStatistics
Switch to module:  "Welcome"
CalculateOutputGeometry: No image geometry specified, default geometry is calculated with 1 mm spacing


Unable to allocate 8526249093 elements of size 8 bytes. 


"Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at http://slicer.org\n\n\nThe message detail is:\n\nException thrown in event: bad allocation"</code></pre>

---

## Post #2 by @cpinter (2018-06-14 20:03 UTC)

<p>If you import an STL into segmentation and start editing, then the surface is converted to labelmap. If no reference volume was defined (which is the case by default if you load the segmentation from STL), then 1x1x1mm3 grid is assumed, and if your model occupies a big enough region, then it may be huge. I think this is what is happening in your case.</p>
<p>To circumvent this, yo need to set a larger grid before you trigger conversion. This should work I think:</p>
<ol>
<li>Load STL as segmentation</li>
<li>Go to Segmentations module, long-click the Create button in the Binary labelmap row in the Representations section, choose Advanced</li>
<li>Change the Reference image geometry. If you have a volume you can use, then click Set from volume. Otherwise you need to come up with a sensible reference grid (for example load any sample data, then resample it in the Crop Volume module), and set that. Conversion will take place and now the created labelmap should be of a reasonable size and Slicer shouldn’t crash</li>
</ol>

---

## Post #3 by @lassoan (2018-06-14 20:07 UTC)

<p>The default 1mm pixel size creates too large binary labelmap representation. For now, you need to load the file as model, create a Segmentation node, set master representation to Closed surface, and import the model into this segmentation.</p>
<p>What would you like to do after you’ve imported the model as segmentation?</p>

---

## Post #4 by @ferhue (2018-06-14 20:34 UTC)

<p>Thanks, the Closed Surface option worked.</p>
<p>I want to export this STL file as a segmented ROI contour (RTSTRUCT) on top of a DICOM CT scan.</p>

---

## Post #5 by @lassoan (2018-06-14 20:56 UTC)

<p>I’ve updated loading of STL files as segmentation to use closed surface representation by default. Therefore, in Slicer nightly versions that you download tomorrow or later will be able to load the STL file directly.</p>

---
