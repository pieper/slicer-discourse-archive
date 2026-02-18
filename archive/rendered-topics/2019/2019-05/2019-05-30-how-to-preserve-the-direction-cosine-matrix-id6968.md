# How to preserve the direction cosine matrix

**Topic ID**: 6968
**Date**: 2019-05-30
**URL**: https://discourse.slicer.org/t/how-to-preserve-the-direction-cosine-matrix/6968

---

## Post #1 by @wpgao (2019-05-30 06:06 UTC)

<p>Hi Guys,</p>
<p>Recently, I had write a batch to resample a series of MR volumes. However, there is one problem that the direction cosine matrix of the output volume is not the same as that of the input volume.<br>
Thanks！</p>
<pre><code class="lang-auto">reader=sitk.ImageFileReader()
writer=sitk.ImageFileWriter()
reader.SetFileName(str(fi_d))
inputVolume=reader.Execute()
reader.ReadImageInformation()
if inputVolume is not None:
 			resample=sitk.ResampleImageFilter()
 			resample.SetInterpolator(sitk.sitkLinear)
 			resample.SetTransform(sitk.Transform(3,sitk.sitkIdentity))
 			resample.SetOutputDirection(reader.GetDirection())
 			print(reader.GetDirection())
 			resample.SetOutputOrigin(reader.GetOrigin())
 			out_spacing=[1.0,1.0,1.0]
 			resample.SetOutputSpacing(out_spacing)
 			original_spacing=reader.GetSpacing()
 			original_size=reader.GetSize()
 			out_size=[int(np.round(original_size[0]*(original_spacing[0]/out_spacing[0]))),int(np.round(original_size[1]*(original_spacing[1]/out_spacing[1]))),int(np.round(original_size[2]*(original_spacing[2]/out_spacing[2])))]
 			resample.SetSize(out_size)
 			resample.SetDefaultPixelValue(0.0)
 			out=resample.Execute(inputVolume)
 			prefix="%s_iso.nii"%fileName
 			resampleVolumeFilePath=os.path.join(self.saveVolumeDir,prefix)
 			writer.SetFileName(str(resampleVolumeFilePath))
 			writer.Execute(out)
</code></pre>

---

## Post #2 by @pieper (2019-05-30 15:32 UTC)

<p>This looks like a good question for <a href="https://discourse.itk.org/search?q=simpleitk" rel="nofollow noopener">the SimpleITK</a> forum.   From a quick look it seems you are setting the output direction to match the input, but maybe something else if going on.</p>

---

## Post #3 by @wpgao (2019-05-31 02:07 UTC)

<p>Hi Pieper,</p>
<p>Thanks for your advice!</p>

---
