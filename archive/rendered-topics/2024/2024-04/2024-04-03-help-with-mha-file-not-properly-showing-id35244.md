# Help With .mha file not properly showing

**Topic ID**: 35244
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/help-with-mha-file-not-properly-showing/35244

---

## Post #1 by @DHK (2024-04-03 03:44 UTC)

<p>I’ve use the PlusMATLABUtil’s MATLABMetaFileIO to combine 2D ultrasound images with an optical tracking system into a .mha file. In it, there are ImageToProbe and ProbeToReference transforms that I have multiplied to get the ImageToReference transform and 325 frames of 814*552 images at the very end.</p>
<p>I can get a volume when I load the .mha file as a volume, but when I load it as a sequence metafile and try to copy the steps in the example document SlicerIGT-U32_TrackedUsVisualization.pptx, I don’t get a moveable 2D image as I do with the example. Nor can I get it to work with Volume Reconstruction, which I need as my goal is to get a model of a blood vessel combined with the tracking system.</p>
<p>Would anybody able to tell me what I did wrong?</p>
<p>Here’s the first few and last few lines of the code:</p>
<blockquote>
<p>ObjectType = Image<br>
NDims = 3<br>
BinaryData = True<br>
BinaryDataByteOrderMSB = False<br>
CompressedData = False<br>
CenterOfRotation = 0 0 0<br>
Offset = 0 0 0<br>
DimSize = 814 552 325<br>
ElementType = MET_UCHAR<br>
ElementSpacing = 6.172840e-02 6.172840e-02 6.172840e-02<br>
ElementByteOrderMSB = False<br>
TransformMatrix = 0 1 0 0 0 -1 -1 0 0<br>
UltrasoundImageOrientation = MF<br>
UltrasoundImageType = BRIGHTNESS<br>
Seq_Frame0000_FrameNumber = 1<br>
Seq_Frame0000_ProbeToReferenceTransform = -9.273654e-01 -1.198580e-01 -3.544398e-01 -3.082373e+02 1.606707e-02 9.336714e-01 -3.577702e-01 -1.905464e+02 -3.738119e-01 3.374785e-01 8.639288e-01 9.434536e+02 0 0 0 1<br>
Seq_Frame0000_ProbeToReferenceTransformStatus = OK<br>
Seq_Frame0000_ImageToProbeTransform = 3.467000e-01 1.316000e-01 0 1.091116e+02 -2.807000e-01 -6.200000e-02 0 1.549904e+02 1.460000e-01 3.940000e-02 0 5.965800e+00 0 0 0 1<br>
Seq_Frame0000_ImageToProbeTransformStatus = OK<br>
Seq_Frame0000_ImageToReferenceTransform = -3.194031e-01 8.131641e-02 -1.699668e-01 -2.283019e+01 2.593153e-01 -2.424350e-02 1.216730e-01 2.533265e+02 -1.347623e-01 1.928739e-02 -6.584435e-02 -4.654438e+01 0 0 0 1<br>
Seq_Frame0000_ImageToReferenceTransformStatus = OK<br>
Seq_Frame0000_UnfilteredTimestamp = 0<br>
Seq_Frame0000_Timestamp = 0<br>
Seq_Frame0000_ImageStatus = OK</p>
</blockquote>
<p>(skip)</p>
<blockquote>
<p>Seq_Frame0324_FrameNumber = 325<br>
Seq_Frame0324_ProbeToReferenceTransform = -9.270131e-01 -2.674204e-01 -2.629316e-01 -3.280601e+02 -1.103972e-01 8.646172e-01 -4.901527e-01 -1.783717e+02 -3.584120e-01 4.253510e-01 8.310339e-01 9.150596e+02 0 0 0 1<br>
Seq_Frame0324_ProbeToReferenceTransformStatus = OK<br>
Seq_Frame0324_ImageToProbeTransform = 3.467000e-01 1.316000e-01 0 1.091116e+02 -2.807000e-01 -6.200000e-02 0 1.549904e+02 1.460000e-01 3.940000e-02 0 5.965800e+00 0 0 0 1<br>
Seq_Frame0324_ImageToProbeTransformStatus = OK<br>
Seq_Frame0324_ImageToReferenceTransform = -3.359237e-01 2.106895e-02 -1.556625e-01 -2.810055e+01 2.670572e-01 2.145865e-02 1.041944e-01 2.581359e+02 -1.396936e-01 -4.977467e-03 -5.770003e-02 -4.895882e+01 0 0 0 1<br>
Seq_Frame0324_ImageToReferenceTransformStatus = OK<br>
Seq_Frame0324_UnfilteredTimestamp = 1.079967e+01<br>
Seq_Frame0324_Timestamp = 1.079967e+01<br>
Seq_Frame0324_ImageStatus = OK<br>
ElementDataFile = LOCAL</p>
</blockquote>

---
