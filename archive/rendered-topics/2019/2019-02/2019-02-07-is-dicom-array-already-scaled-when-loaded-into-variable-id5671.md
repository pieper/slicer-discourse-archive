# Is DICOM array already scaled when loaded into variable?

**Topic ID**: 5671
**Date**: 2019-02-07
**URL**: https://discourse.slicer.org/t/is-dicom-array-already-scaled-when-loaded-into-variable/5671

---

## Post #1 by @Alex_Vergara (2019-02-07 09:21 UTC)

<p>I have a silly question but anyway:<br>
When I do</p>
<pre><code class="lang-python">    arr = slicer.util.array(ImageDicom).astype(float)
</code></pre>
<p>I can obtain the voxel array of the image, but in the case of DICOM files it is oftenly not the real values which must be calculated using the rescale and slope parameters within the DICOM header itself.</p>
<p>My question is: Are this values already applied whn you obtain the array or do I have to read them and apply by myself?? I have some weird cases in which the rescaling is not done, but I wonder if this is the general rule.</p>

---

## Post #2 by @pieper (2019-02-07 12:35 UTC)

<p>The dicom data in slicer should always have the rescale slope applied (it happens in the itk reader layer) unless for some reason your files are non-standard, for example if the slope is in a private tag or something.  If you have files that don’t seem to work maybe you could share an anonymized example.</p>
<p>The slicer.util.array command will give you a numpy array that is a view of the same memory that the slicer volume node uses (allowing you to modify directly from python). When you create a float version it’ll be a copy and you need to cast and copy back if you want to modify the volume node.</p>
<p>Hope that helps.</p>

---
