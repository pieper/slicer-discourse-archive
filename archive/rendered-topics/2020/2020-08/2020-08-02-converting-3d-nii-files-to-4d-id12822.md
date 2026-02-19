---
topic_id: 12822
title: "Converting 3D Nii Files To 4D"
date: 2020-08-02
url: https://discourse.slicer.org/t/12822
---

# converting 3D nii files to 4D

**Topic ID**: 12822
**Date**: 2020-08-02
**URL**: https://discourse.slicer.org/t/converting-3d-nii-files-to-4d/12822

---

## Post #1 by @mindmap2 (2020-08-02 17:05 UTC)

<p>Dear 3D slicer community,<br>
I have 50 3D nii files that I want to convert them to 4D nii and view it as a movie.I wonder if 3D slicer has this ability.<br>
Thanks,</p>

---

## Post #2 by @lassoan (2020-08-02 17:13 UTC)

<p>You can view 4D volumes as movies (for example, using Volume Rendering) in Slicer. You can also export it as a mp4 video (using Screen Capture module), register, segment, analyze, etc.</p>
<p>4D volume sequences can be saved as nrrd files in Slicer. If you must save as nifti then you should be able to find Python packages that can import a 4D nrrd image and save it as 4D nifti.</p>

---

## Post #3 by @hjmjohnson (2022-08-18 15:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  I have combined 3 scalar 3D volumes (Flair, T1, TRACE) into and saved it as NRRD format.</p>
<p>1: When I have done this, as a “3D vector image” it always looks like it is displayed as an RGB image</p>
<p>2: When I concatenate into a 4D data set,  the nrrd file only loads 1 scalar value, and it looses it’s physical space representation.</p>
<p>I was expecting something akin to the DWI dataset to be loaded with an index for each component.</p>
<pre><code class="lang-python">import itk

ADCfn = "ADCSkullStrippedregistered.nii.gz"
FLfn = "FLAIRSkullStrippedregistered.nii.gz"
TRfn = "TRACEWSkullStrippedregistered.nii.gz"

DTYPE = itk.F
SIZE = 3
IMTYPE = itk.Image[DTYPE, SIZE]
VIMTYPE = itk.VectorImage[DTYPE, SIZE]
D4IMTYPE= itk.Image[DTYPE, 4]

jif = itk.JoinSeriesImageFilter[IMTYPE,D4IMTYPE].New()

ADC = itk.imread(ADCfn, pixel_type=DTYPE)
FL = itk.imread(FLfn, pixel_type=DTYPE)
TR = itk.imread(TRfn, pixel_type=DTYPE)

resample_ADC2FL = itk.ResampleImageFilter[IMTYPE,IMTYPE].New()
resample_ADC2FL.SetInput(ADC)
resample_ADC2FL.SetReferenceImage(FL)
resample_ADC2FL.UseReferenceImageOn()
resample_ADC2FL.Update()
rADC=resample_ADC2FL.GetOutput()

resample_TR2FL  = itk.ResampleImageFilter[IMTYPE,IMTYPE].New()
resample_TR2FL.SetInput(TR)
resample_TR2FL.SetReferenceImage(FL)
resample_TR2FL.UseReferenceImageOn()
resample_TR2FL.Update()
rTR=resample_TR2FL.GetOutput()

cif = itk.ComposeImageFilter[IMTYPE, VIMTYPE].New()
cif.SetInput(0, rTR)
cif.SetInput(1, rADC)
cif.SetInput(2, FL)
cif.SetInput(3, FL)
cif.SetInput(4, FL)
cif.Update()

output = cif.GetOutput()
itk.imwrite(output,"/tmp/test.nrrd")

jif = itk.JoinSeriesImageFilter[IMTYPE,D4IMTYPE].New()
jif.SetInput(0, rTR)
jif.SetInput(1, rADC)
jif.SetInput(2, FL)
jif.SetInput(3, FL)
jif.SetInput(4, FL)
jif.Update()

output = jif.GetOutput()
itk.imwrite(output,"/tmp/test4d.nrrd")
</code></pre>
<p>nrrd header for the 3D vector image</p>
<pre data-code-wrap="txt"><code class="lang-nohighlight">NRRD0004 
# Complete NRRD file format specification at: 
# http://teem.sourceforge.net/nrrd/format.html 
type: float 
dimension: 4 
space: left-posterior-superior 
sizes: 5 320 320 20 
space directions: none (0.74917204642169,0.013089305043978788,-0.032709554472705113) (0.013076845101263054,-0.74988577139539259,-0.000570947400907372) (0.3053356701418492,-4.0745362190901257e-10,6.9933375528812443) 
kinds: vector domain domain domain 
endian: little
encoding: raw
space origin: (-108.57624816894531,90.696868896484375,-87.553054809570312)
</code></pre>
<p>nrrd header for the concatenated 4D scalar volumes</p>
<pre data-code-wrap="txt"><code class="lang-nohighlight">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: float
dimension: 4
space dimension: 4
sizes: 320 320 20 5
space directions: (0.74917204642169,0.013089305043978788,-0.032709554472705113,0) (0.013076845101263054,-0.74988577139539259,-0.000570947400907372,0) (0.3053356701418492,-4.0745362190901257e-10,6.9933375528812443,0) (0,0,0,1)
kinds: domain domain domain domain
endian: little
encoding: raw
space origin: (-108.57624816894531,90.696868896484375,-87.553054809570312,0)
</code></pre>

---
