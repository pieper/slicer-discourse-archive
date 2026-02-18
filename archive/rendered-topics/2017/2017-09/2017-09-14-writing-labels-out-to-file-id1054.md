# Writing labels out to file

**Topic ID**: 1054
**Date**: 2017-09-14
**URL**: https://discourse.slicer.org/t/writing-labels-out-to-file/1054

---

## Post #1 by @ebremer (2017-09-14 23:40 UTC)

<p>I’m trying to print out a single label image with the following in Slicer 4.7.9-2017-09-10</p>
<h1>=================================================<br>
labelNodes = slicer.util.getNodes(‘vtkMRMLLabelMapVolumeNode*’)<br>
vs = labelNodes.values()<br>
v = vs[0]<br>
sNode = slicer.vtkMRMLVolumeArchetypeStorageNode()<br>
sNode.SetFileName(‘label.tif’))<br>
sNode.SetWriteFileFormat(‘tif’)<br>
sNode.SetURI(None)<br>
success = sNode.WriteData(v)<br>
print success</h1>
<p>I get a all-black image (ALL ZEROS) with the correct size.  No actual label data with the value of 1 as I expected.  Am I doing something wrong here?</p>

---

## Post #2 by @lassoan (2017-09-15 00:35 UTC)

<p>Saving to consumer image formats (tiff, JPEG, png) has been broken for a good while, see <a href="https://issues.slicer.org/view.php?id=4091">https://issues.slicer.org/view.php?id=4091</a></p>
<p>You can add a note to the issue describing why it is important for you to have this working. Until it is fixed, you may try using an VTK or ITK reader directly.</p>

---

## Post #3 by @ebremer (2017-09-15 13:40 UTC)

<p>Ha!  I forgot, I’m the one who opened that issue!  Tiff’s were working at that point, but they are now also broken.</p>

---

## Post #4 by @ebremer (2017-09-15 14:19 UTC)

<p>Saving to “consumer” image formats allows Slicer to interact with a larger community of software and encourages people to use Slicer’s output for further analysis and software development.  As far as a note why it should be fixed, I would think this is self-evident.</p>

---

## Post #5 by @lassoan (2017-09-15 15:02 UTC)

<p>You lose a lot of information if you use consumer file formats (slice spacing, image position, orientation, other metadata) and you may have image artifacts due to compression, so images saved in these formats are not well suited for further analysis. ScreenCapture module can be used for exporting view contents to image files/videos for presentation. It is clear that it is a nice to be able to export to tiff, but for me it is not self-evident if this is really important.</p>
<p>What would you use the exported files for? How do you manage the lost metadata (image position, orientation, slice spacing, …)? What software you use to further process tiff files? Do these software support standard medical image computing file formats (nrrd, metaimage, nifti) or DICOM?</p>

---
