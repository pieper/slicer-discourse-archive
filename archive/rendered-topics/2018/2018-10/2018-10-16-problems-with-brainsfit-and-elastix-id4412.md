# Problems with BRAINSfit and Elastix

**Topic ID**: 4412
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/problems-with-brainsfit-and-elastix/4412

---

## Post #1 by @torquil (2018-10-16 12:46 UTC)

<p>Hi!</p>
<p>I’m using the latest nightly build of Slicer on Linux, and I’m trying to learn how to do registration of one temporal bone CT onto another. When I try to use “General Registration (BRAINSfit)”, I’m getting “Status: Completed with errors” and the following message after choosing fixed/moving images as well as “Output image volume” in the Output settings, and then clicking on apply:</p>
<pre><code>"General Registration (BRAINS) standard error:

terminate called after throwing an instance of 'itk::ImageFileReaderException'
  what():  /work/Preview/Slicer-0-build/ITKv4/Modules/IO/ImageBase/include/itkImageFileReader.hxx:143:
 Could not create IO object for reading file /tmp/Slicer-torquil/CEAHH_vtkMRMLScalarVolumeNodeB.nrrd
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    DCMTKImageIO
    GDCMImageIO
    GiplImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    GE4ImageIO
    GE5ImageIO
    HDF5ImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type."
</code></pre>
<p>As an alternative, I have installed the SlicerElastix module, but when I use that I get an empty error message:</p>
<p><code>"Error:"</code></p>
<p>It does not matter if I choose different Preset values.</p>
<p>In the log files ~/.xsession-errors I’m seeing the following at each click on Apply:</p>
<pre><code>"Volume registration is started in working directory: /tmp/Slicer-torquil/Elastix/20181016_144358_133
Generic Warning: In /work/Preview/Slicer-0/Libs/MRML/Core/vtkDataFileFormatHelper.cxx, line 237
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to 'File format name (.ext)' format! Current format string: .mha


MetaImage: M_WriteElementsData: file stream is fail after write
Generic Warning: In /work/Preview/Slicer-0/Libs/MRML/Core/vtkDataFileFormatHelper.cxx, line 237
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to 'File format name (.ext)' format! Current format string: .mha


MetaImage: M_WriteElementsData: file stream is fail after write
Register volumes...
Register volumes using: /home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/elastix: ['-f', u'/tmp/Slicer-torquil/Elastix/20181016_144358_133/input/fixed.mha', '-m', u'/tmp/Slicer-torquil/Elastix/20181016_144358_133/input/moving.mha', '-out', u'/tmp/Slicer-torquil/Elastix/20181016_144358_133/result-transform', '-p', '/home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Resources/RegistrationParameters/Parameters.Par0009.affine.txt', '-p', '/home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Resources/RegistrationParameters/Parameters.Par0009.elastic.txt']

elastix is started at Tue Oct 16 14:43:58 2018.

which elastix:   /home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/elastix
elastix runs at: lenovo-p51
  Linux 4.18.0-2-amd64 (x64), #1 SMP Debian 4.18.10-2 (2018-10-07)
  with 15830 MB memory, and 4 cores @ 3835 MHz.
-------------------------------------------------------------------------

Running elastix with parameter file 0: "/home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Resources/RegistrationParameters/Parameters.Par0009.affine.txt".

Current time: Tue Oct 16 14:43:58 2018.
Reading the elastix parameters from file ...

ERROR: could not read fixed image.

itk::ImageFileReaderException (0x361de80)
Location: "unknown"
File: /work/Preview/Slicer-0-build/ITKv4/Modules/IO/ImageBase/include/itkImageFileReader.hxx
Line: 143
Description:  Could not create IO object for reading file /tmp/Slicer-torquil/Elastix/20181016_144358_133/input/fixed.mha
  Tried to create one of the following:
    BMPImageIO
    BioRadImageIO
    Bruker2dseqImageIO
    DCMTKImageIO
    GDCMImageIO
    GE4ImageIO
    GE5ImageIO
    GiplImageIO
    HDF5ImageIO
    JPEGImageIO
    LSMImageIO
    MGHImageIO
    MINCImageIO
    MRCImageIO
    MetaImageIO
    NiftiImageIO
    NrrdImageIO
    PNGImageIO
    StimulateImageIO
    TIFFImageIO
    VTKImageIO
    MRMLIDImageIO
  You probably failed to set a file suffix, or
    set the suffix to an unsupported type.



Errors occurred!
vtkDebugLeaks has found no leaks.

Command 'elastix' returned non-zero exit status 1
Traceback (most recent call last):
  File "/home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py", line 327, in onApplyButton
    movingVolumeMaskNode = self.movingVolumeMaskSelector.currentNode())
  File "/home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py", line 579, in registerVolumes
    self.logProcessOutput(ep)
  File "/home/torquil/.config/NA-MIC/Extensions-27483/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py", line 519, in logProcessOutput
    raise subprocess.CalledProcessError(return_code, "elastix")
CalledProcessError: Command 'elastix' returned non-zero exit status 1"
</code></pre>
<p>I’m using the following version of elastix</p>
<pre><code>$ elastix --version
elastix version: 4.800</code></pre>

---

## Post #2 by @lassoan (2018-10-16 14:30 UTC)

<p>Maybe you <a href="https://issues.slicer.org/view.php?id=4340">don’t have access to temporary folder</a>. Try to change your temporary folder in application settings / modules / temporary directory.</p>
<p>There has been an <a href="https://discourse.slicer.org/t/2018-10-15-windows-nightly-build-unable-to-import-vtk/4403/3">error</a> in latest nightly package that might have caused various issues. Please try again with the nightly version tomorrow.</p>

---
