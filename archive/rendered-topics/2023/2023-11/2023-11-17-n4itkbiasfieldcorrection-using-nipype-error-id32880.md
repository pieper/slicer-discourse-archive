# N4ITKBiasFieldCorrection using nipype error

**Topic ID**: 32880
**Date**: 2023-11-17
**URL**: https://discourse.slicer.org/t/n4itkbiasfieldcorrection-using-nipype-error/32880

---

## Post #1 by @georgek (2023-11-17 16:09 UTC)

<p>Hi all,</p>
<p>I am just getting started with nipype and trying to perform N4 bias field correction on MR images. Here is the relevant code:</p>
<p>import nipype<br>
import nipype.interfaces.slicer as Slicer</p>
<p>BFC=Slicer.N4ITKBiasFieldCorrection()</p>
<p>BFC.inputs.inputimage= ‘T1.nii.gz’<br>
BFC.inputs.maskimage = ‘mask.nii.gz’<br>
BFC.inputs.outputimage= ‘T1_slicer_n4BFC.nii.gz’<br>
BFC.run()</p>
<p>and I am getting the following error:<br>
231117-11:56:45,217 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.217168:terminate called after throwing an instance of ‘slicer_itk::ImageFileReaderException’<br>
231117-11:56:45,218 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.217168:  what():  /work/Stable/Slicer-0-build/ITK/Modules/IO/ImageBase/include/itkImageFileReader.hxx:132:<br>
231117-11:56:45,218 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.217168: Could not create IO object for reading file --inputimage<br>
231117-11:56:45,219 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.217168:The file doesn’t exist.<br>
231117-11:56:45,219 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.217168:Filename = --inputimage<br>
231117-11:56:45,220 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.217168:<br>
231117-11:56:45,331 nipype.interface INFO:<br>
stderr 2023-11-17T11:56:45.331166:Aborted (core dumped)</p>
<p>Just to point out that I have been able to just use the background masking tool successfully just before that code so I presume it is not an installation or PATH issue<br>
masking =Slicer.BRAINSROIAuto()<br>
masking.inputs.inputVolume= ‘T1.nii.gz’<br>
masking.inputs.outputROIMaskVolume= ‘mask.nii.gz’<br>
masking.run()</p>
<p>Moreover, I can open the image using sitk.ReadImage (‘T1.nii.gz’) without any issues.</p>
<p>I am currently out of ideas. Has anyone got any ideas?</p>

---
