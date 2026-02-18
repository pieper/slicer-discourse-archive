# Cropping an image in Jupyter notebook fails

**Topic ID**: 9741
**Date**: 2020-01-08
**URL**: https://discourse.slicer.org/t/cropping-an-image-in-jupyter-notebook-fails/9741

---

## Post #1 by @myousefi2016 (2020-01-08 21:06 UTC)

<p>I’m trying to crop an image in Jupyter notebook by using this code:</p>
<pre><code class="lang-auto">import SimpleITK as sitk

inputVolumeFnm  = "./test.nrrd"  
croppedImageFnm = "./testCropped.nrrd"

inIm = sitk.ReadImage(inputVolumeFnm)

cropper = sitk.CropImageFilter()
croppingBounds = [[117, 194, 95],[227, 351, 125]]
cropper.SetLowerBoundaryCropSize(croppingBounds[0])
cropper.SetUpperBoundaryCropSize(croppingBounds[1])
croppedImage = cropper.Execute(inIm) 

outIm = crop.Execute(inIm)
outIm.SetOrigin(inIm.GetOrigin())
outIm.SetDirection(inIm.GetDirection())
sitk.WriteImage(outIm, croppedImageFnm, True)
</code></pre>
<p>But, I’m getting this error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 12, in &lt;module&gt;
  File "/users/yousefi/Downloads/Slicer-4.11.0-2020-01-07-linux-amd64/lib/Python/lib/python3.6/site-packages/SimpleITK-1.3.0rc2.dev260-py3.6-linux-x86_64.egg/SimpleITK/SimpleITK.py", line 22692, in Execute
    return _SimpleITK.CropImageFilter_Execute(self, *args)
RuntimeError: Exception thrown in SimpleITK CropImageFilter_Execute: /work/Preview/Slicer-0-build/ITK/Modules/Core/Common/src/itkPoolMultiThreader.cxx:254:
itk::ERROR: Split count is greater than number of work units!
</code></pre>
<p>I’m using the latest Slicer nightly build and using Python3. Any idea what’s the reason for that error?</p>

---

## Post #2 by @lassoan (2020-01-08 21:10 UTC)

<p>Are you sure the file has been loaded successfully? Have you tried to load the image by specifying full path?</p>
<p>It seems like an error in ITK or how ITK is used. <a class="mention" href="/u/blowekamp">@blowekamp</a> <a class="mention" href="/u/thewtex">@thewtex</a> do you have any clues?</p>
<p>We’ll upgrade ITK and SimpleITK in Slicer to latest releases within a few days, which may fix this issue.</p>

---

## Post #3 by @myousefi2016 (2020-01-08 21:26 UTC)

<p>Yes, I believe it’s loaded successfully cause this print:</p>
<pre><code class="lang-auto">print(inIm.GetOrigin())
</code></pre>
<p>Shows me this:</p>
<pre><code class="lang-auto">(-177.32197570800784, -64.95606994628905, 1008.1570434570312)
</code></pre>
<p>One question: The crop bounds should be in extent format or range format? Extent means just integer values that corresponds to the structured points in the volumetric image but range means the 3D coordinate of points.</p>

---

## Post #4 by @lassoan (2020-01-08 21:48 UTC)

<p>Extents are integer values, referring to voxel indices. See more information in <a href="https://discourse.itk.org/t/how-to-crop-a-3d-image-with-a-specified-size/715/10">this ITK discussion</a>.</p>

---

## Post #5 by @blowekamp (2020-01-09 20:56 UTC)

<p>Hello,</p>
<p>The usage looks correct, and it certainly should produce that error.</p>
<p>This seems likely that it is a problem inside ITK. I’m note sure what version of ITK or SimpleITK is being used here.</p>
<p>You have a nice stand alone test case. Can you please try with two different stand alone versions of SimpleITK</p>
<ul>
<li>v1.2.4 - This is the versions that should be pip install able.</li>
<li>
<a href="https://github.com/SimpleITK/SimpleITK/releases" rel="nofollow noopener">latest nightly pre-release binary</a> - This is build against ITKv5.1rc1</li>
</ul>
<p>Please report back how these versions of SimpleITK/ITK work for this test case.</p>

---

## Post #6 by @myousefi2016 (2020-01-09 21:12 UTC)

<p>Hi <a class="mention" href="/u/blowekamp">@blowekamp</a>, I just found the solution. There was two problems in my code. First I executed the crop filter twice and also I didn’t know that instead of giving the upper bound of cropped image, I need to have the upper bound of original image - upper bound of cropped image. Thank you!</p>

---

## Post #7 by @blowekamp (2020-01-09 21:16 UTC)

<p>What is the size in pixels of “test.nrrd”?</p>

---

## Post #8 by @myousefi2016 (2020-01-09 21:31 UTC)

<p><code>test.nrrd</code> size is (512,512,144) or in terms of extent:</p>
<pre><code class="lang-auto">X extent: [0,511] (delta: 512)
Y extent: [0,511] (delta: 512)
Z extent: [0,143] (delta: 144)
</code></pre>
<p>and I wanted to crop this region based on its actual lower and upper bounds:</p>
<pre><code class="lang-auto">Lower bounds: [117,194,95]
Upper bounds: [227,351,125]
</code></pre>
<p>But I realized that crop filter take this as lower and upper bounds:</p>
<pre><code class="lang-auto">Lower bounds: [117,194,95]
Upper bounds: [511-227,511-351,143-125] = [284, 160, 18]
</code></pre>
<p>So, it just solved my problem and I don’t get that error anymore with same code.</p>

---

## Post #9 by @blowekamp (2020-01-09 21:52 UTC)

<p>I ran the following locally with the “latest” binary:</p>
<pre><code class="lang-auto">In [1]: import SimpleITK as sitk                                                                                                                        

In [2]: inIm = sitk.Image( (512,512,144), sitk.sitkUInt8)                                                                                               

In [3]:  
   ...: cropper = sitk.CropImageFilter() 
   ...: croppingBounds = [[117, 194, 95],[227, 351, 125]] 
   ...: cropper.SetLowerBoundaryCropSize(croppingBounds[0]) 
   ...: cropper.SetUpperBoundaryCropSize(croppingBounds[1]) 
   ...: croppedImage = cropper.Execute(inIm)  
   ...:                                                                                                                                                 

In [4]: print(croppedImage)                                                                                                                             
Image (0x7fbed5538090)
  RTTI typeinfo:   itk::Image&lt;unsigned char, 3u&gt;
  Reference Count: 1
  Modified Time: 813
  Debug: Off
  Object Name: 
  Observers: 
    none
  Source: (none)
  Source output name: (none)
  Release Data: Off
  Data Released: False
  Global Release Data: Off
  PipelineMTime: 799
  UpdateMTime: 809
  RealTimeStamp: 0 seconds 
  LargestPossibleRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [168, 18446744073709551583, 18446744073709551540]
  BufferedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [168, 18446744073709551583, 18446744073709551540]
  RequestedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [168, 18446744073709551583, 18446744073709551540]
</code></pre>
<p>It looks like there are some signed integer and/or underflow issue going on here. SimpleITK/ITK need to be more robust with the improper parameters.</p>

---

## Post #10 by @blowekamp (2020-01-09 22:20 UTC)

<p>Here is a pull request to fix the issue in ITK:<br>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1551" target="_blank" rel="nofollow noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1551" target="_blank" rel="nofollow noopener">BUG: Prevent integer underflow in CropImageFilter</a>
    </h4>

    <div class="branches">
      <code>InsightSoftwareConsortium:master</code> ← <code>blowekamp:FixCropImageSizeUnderflow</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-01-09" data-time="22:19:38" data-timezone="UTC">10:19PM - 09 Jan 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">
          <img alt="blowekamp" src="https://avatars1.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
          blowekamp
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 22 additions and 0 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1551/files" target="_blank" rel="nofollow noopener">
          <span class="added">+22</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>
  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
