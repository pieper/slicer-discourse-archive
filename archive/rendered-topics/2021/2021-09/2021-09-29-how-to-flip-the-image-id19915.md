# How to flip the image

**Topic ID**: 19915
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/how-to-flip-the-image/19915

---

## Post #1 by @akmal871026 (2021-09-29 14:47 UTC)

<p>anyone can help how to flip the image either from right to left, or up to down?</p>

---

## Post #2 by @chir.set (2021-09-29 15:00 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="1" data-topic="19915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>flip the image</p>
</blockquote>
</aside>
<p>In slice views or 3D views ?</p>

---

## Post #3 by @akmal871026 (2021-09-29 15:06 UTC)

<p>in slicer view and also 3D viewer</p>

---

## Post #4 by @chir.set (2021-09-29 15:31 UTC)

<p>In 3D views, you have the orientation widget already :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d045d45edfa5f9c2c2368e86aa4cf27009a842.png" alt="Screenshot_20210929_172743" data-base62-sha1="qe5Bahb8JHzBM6WxZdy600U1HJU" width="104" height="98"></p>
<p>Additionally, you can rotate a 3D view with CTRL + left click + move.</p>
<p>In slice views, this <a href="https://github.com/chir-set/FlipViewPoint" rel="noopener nofollow ugc">module</a> may help.</p>

---

## Post #5 by @akmal871026 (2021-09-29 15:36 UTC)

<p>But, how to install in 3D Slicer</p>

---

## Post #6 by @chir.set (2021-09-29 16:11 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="5" data-topic="19915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>how to install in 3D Slicer</p>
</blockquote>
</aside>
<p>Like with any module that is not in the extension repository, download it from the source repository.</p>
<p>You may then add it using the GUI :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b587ac3b4dd3b6ee68c92ae309aded4d9eae0f0.png" data-download-href="/uploads/short-url/fjCEFgBSSzVsfm6zNTA39qOuB6U.png?dl=1" title="Screenshot_20210929_180434" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b587ac3b4dd3b6ee68c92ae309aded4d9eae0f0_2_690x105.png" alt="Screenshot_20210929_180434" data-base62-sha1="fjCEFgBSSzVsfm6zNTA39qOuB6U" width="690" height="105" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b587ac3b4dd3b6ee68c92ae309aded4d9eae0f0_2_690x105.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b587ac3b4dd3b6ee68c92ae309aded4d9eae0f0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b587ac3b4dd3b6ee68c92ae309aded4d9eae0f0.png 2x" data-dominant-color="2B2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20210929_180434</span><span class="informations">746×114 10 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>or make a custom start script with ‘–additional-module-paths &lt;/path/to/directory/containing/py_file&gt;’.</p>
<p>This second method is in fact the best way to use any module.</p>
<p>Yes, there’s some work to do; there’s always some work to do.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2021-09-29 17:59 UTC)

<p>You can flip slice views using “Reformat” module: select a slice view then set the LR, PA, or IS slider value to 180. We could add flip buttons there, but in general, it is not recommended to flip slice views, as using non-standard view orientations could lead to misinterpretation of the images.</p>
<p>If you always want Slicer to use “patient right is screen right” slice orientation convention instead of the default (and most widely used) “patient right is screen left”, then you can modify that in menu: Edit / Application settings / Views / Slice viewer defaults.</p>
<p>If you want to flip the image because the imaging technologist did not set the patient orientation correctly (e.g., image was acquired HFP, but the technologist forgot to switch from the default HFS patient orientation) then you must not change the slice views but instead apply a transform to the volume and rotate the volume to the correct orientation. Note that this is a rotation - it should never be necessary to flip (mirror) a 3D volume, except very few special cases (for example, create a mirrored image of the healthy side of the face to be used as a template for reconstructing the damaged other side).</p>
<p><a class="mention" href="/u/akmal871026">@akmal871026</a> Which one is your case? Why do you need to flip the images?</p>

---

## Post #8 by @Stuart (2024-05-19 20:16 UTC)

<p>Hi Andras,</p>
<p>I segmented a file and just learned that there was an orientation problem when the material was originally scanned so I would indeed like to flip (mirror) the resulting 3D volume. Is there a way to do this?</p>
<p>Thanks.</p>

---

## Post #9 by @pearsonm (2024-05-20 00:13 UTC)

<p>This python snippet will flip the dataset. The index can be 0, 1 or 2 depending on the way you want to flip. I use this code to flip nuclear medicine data that is acquired on 180 degree opposed heads. The display must be refreshed to see the change.</p>
<pre><code class="lang-auto">def flipNode(node, index):
    import numpy
    from vtk.util.numpy_support import vtk_to_numpy, numpy_to_vtk
    imageData = node.GetImageData()
    nshape = tuple(reversed(imageData.GetDimensions()))
    narray = None
    narray = vtk_to_numpy(imageData.GetPointData().GetScalars()).reshape(nshape)
    print(narray.shape)
    imgdata = numpy.flip(narray, index)
    varr = numpy_to_vtk(imgdata.ravel())
    imageData.GetPointData().SetScalars(varr)

import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()
volumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
flipNode(volumeNode, 0)
</code></pre>
<p>Mark</p>

---

## Post #10 by @lassoan (2024-05-22 13:55 UTC)

<p>A post was split to a new topic: <a href="/t/flip-image-around-an-axis/36326">Flip image around an axis</a></p>

---
