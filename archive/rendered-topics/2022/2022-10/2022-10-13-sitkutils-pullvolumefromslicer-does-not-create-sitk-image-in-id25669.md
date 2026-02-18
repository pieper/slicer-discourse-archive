# sitkUtils.PullVolumeFromSlicer does not create sitk::Image in Slicer 5.1

**Topic ID**: 25669
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-does-not-create-sitk-image-in-slicer-5-1/25669

---

## Post #1 by @rbumm (2022-10-13 08:17 UTC)

<p>Using sitkUtils.PullVolumeFromSlicer</p>
<pre><code class="lang-auto">                from lungmask import mask
                import SimpleITK as sitk
                import sitkUtils

                self.showStatusMessage(' Creating lungs with AI ...')
                inputVolumeSitk = sitkUtils.PullVolumeFromSlicer(self.inputVolume)
                print(inputVolumeSitk)
</code></pre>
<p>to create an input volume for “lungmask” AI produces in Slicer 5.0.3 Stable correctly:</p>
<pre><code class="lang-auto">Image (000001DF82D79C40)
  RTTI typeinfo:   class itk::Image&lt;int,3&gt;
  Reference Count: 1
  Modified Time: 1021
  Debug: Off
  Object Name: 
  Observers: 
    none
  Source: (none)
  Source output name: (none)
  Release Data: Off
  Data Released: False
  Global Release Data: Off
  PipelineMTime: 1010
  UpdateMTime: 1020
  RealTimeStamp: 0 seconds 
  LargestPossibleRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [512, 512, 139]
  BufferedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [512, 512, 139]
  RequestedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [512, 512, 139]
  Spacing: [0.761719, 0.761719, 2.5]
  Origin: [-195, -171.7, -347.75]
  Direction: 
1 0 0
0 1 0
0 0 1

  IndexToPointMatrix: 
0.761719 0 0
0 0.761719 0
0 0 2.5

  PointToIndexMatrix: 
1.31282 0 0
0 1.31282 0
0 0 0.4

  Inverse Direction: 
1 0 0
0 1 0
0 0 1

  PixelContainer: 
    ImportImageContainer (000001DF835BDC50)
      RTTI typeinfo:   class itk::ImportImageContainer&lt;unsigned __int64,int&gt;
      Reference Count: 1
      Modified Time: 1018
      Debug: Off
      Object Name: 
      Observers: 
        none
      Pointer: 000001DF904FB040
      Container manages memory: true
      Size: 36438016
      Capacity: 36438016
</code></pre>
<hr>
<p>In Slicer Slicer 5.1.0-2022-10-11 (Windows 11) the same call produces</p>
<pre><code class="lang-auto">
Image (0000025AE2411E50)
  RTTI typeinfo:   class slicer_itk::Image&lt;int,3&gt;
  Reference Count: 1
  Modified Time: 6368
  Debug: Off
  Object Name: 
  Observers: 
    none
  Source: (none)
  Source output name: (none)
  Release Data: Off
  Data Released: False
  Global Release Data: Off
  PipelineMTime: 6349
  UpdateMTime: 6364
  RealTimeStamp: 0 seconds 
  LargestPossibleRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [512, 512, 139]
  BufferedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [512, 512, 139]
  RequestedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [512, 512, 139]
  Spacing: [0.761719, 0.761719, 2.5]
  Origin: [-195, -171.7, -347.75]
  Direction: 
1 0 0
0 1 0
0 0 1

  IndexToPointMatrix: 
0.761719 0 0
0 0.761719 0
0 0 2.5

  PointToIndexMatrix: 
1.31282 0 0
0 1.31282 0
0 0 0.4

  Inverse Direction: 
1 0 0
0 1 0
0 0 1

  PixelContainer: 
    ImportImageContainer (0000025AE1A17D20)
      RTTI typeinfo:   class slicer_itk::ImportImageContainer&lt;unsigned __int64,int&gt;
      Reference Count: 1
      Modified Time: 6361
      Debug: Off
      Object Name: 
      Observers: 
        none
      Pointer: 0000025AEEC28040
      Container manages memory: true
      Size: 36438016
      Capacity: 36438016
</code></pre>
<p>and leads to this exception:</p>
<pre><code class="lang-auto">Failed to compute results: in method 'GetByteArrayFromImage', argument needs to be of type 'sitk::Image *'
Traceback (most recent call last):
  File "C:/Users/Rudolf/Documents/MySlicerExtensions/SlicerLungCTAnalyzer/LungCTSegmenter/LungCTSegmenter.py", line 519, in onApplyButton
    self.logic.applySegmentation()
  File "C:/Users/Rudolf/Documents/MySlicerExtensions/SlicerLungCTAnalyzer/LungCTSegmenter/LungCTSegmenter.py", line 1510, in applySegmentation
    segmentation_np = mask.apply(inputVolumeSitk)  # default model is U-net(R231), output is numpy
  File "C:\Users\Rudolf\AppData\Local\NA-MIC\Slicer 5.1.0-2022-10-11\lib\Python\Lib\site-packages\lungmask\mask.py", line 31, in apply
    inimg_raw = sitk.GetArrayFromImage(image)
  File "C:\Users\Rudolf\AppData\Local\NA-MIC\Slicer 5.1.0-2022-10-11\lib\Python\Lib\site-packages\SimpleITK\extra.py", line 269, in GetArrayFromImage
    array_view = GetArrayViewFromImage(image)
  File "C:\Users\Rudolf\AppData\Local\NA-MIC\Slicer 5.1.0-2022-10-11\lib\Python\Lib\site-packages\SimpleITK\extra.py", line 255, in GetArrayViewFromImage
    image_memory_view = _GetMemoryViewFromImage(image)
TypeError: in method 'GetByteArrayFromImage', argument needs to be of type 'sitk::Image *'
</code></pre>

---

## Post #2 by @pieper (2022-10-13 14:16 UTC)

<p>Thanks for reporting.  <a class="mention" href="/u/jcfr">@jcfr</a> has been working on upgrades to the itk/sitk implementation and this should help him debug.</p>

---

## Post #3 by @jcfr (2022-10-13 21:43 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>I will look into the details and report back.</p>
<p>This problem is likely captured by the now failing test <code>py_nomainwindow_test_sitkUtils</code></p>
<p>Links:</p>
<ul>
<li>CDash / SlicerPreview / Linux: <a href="https://slicer.cdash.org/test/23216258">https://slicer.cdash.org/test/23216258</a>
</li>
<li>CDash / SlicerPreview / Windows: <a href="https://slicer.cdash.org/test/23218352">https://slicer.cdash.org/test/23218352</a>
</li>
</ul>

---

## Post #4 by @jamesobutler (2022-10-18 21:58 UTC)

<p>I ran into this as well when updating to use latest Slicer version in my custom app. I added a GitHub issue for it in addition to this post.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6598">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6598" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6598" target="_blank" rel="noopener nofollow ugc">SimpleITK usage in Slicer broken as observed in `test_sitkUtils`</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-10-18" data-time="21:58:08" data-timezone="UTC">09:58PM - 18 Oct 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

SimpleITK usage in Slicer has had problems since the merging of 0d<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">1ed30a34f96ad5c5f367626347bf5b3a4f1e95. This was also reported at https://discourse.slicer.org/t/sitkutils-pullvolumefromslicer-does-not-create-sitk-image-in-slicer-5-1/25669

This issue appears to be captured by Slicer failed test https://slicer.cdash.org/test/23247998

## Steps to reproduce

```
Python 3.9.10 (main, Oct 16 2022, 23:27:17) [MSC v.1930 64 bit (AMD64)] on win32
&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; sitk.ReadImage(r"C:\Users\butlej30383\Downloads\MRHead.nrrd")
&lt;SimpleITK.SimpleITK.Image; proxy of &lt;Swig Object of type 'slicer_itk::simple::Image *' at 0x0000017A7A8B8E10&gt; &gt;
&gt;&gt;&gt; image = sitk.ReadImage(r"C:\Users\butlej30383\Downloads\MRHead.nrrd")
&gt;&gt;&gt; image
&lt;SimpleITK.SimpleITK.Image; proxy of &lt;Swig Object of type 'slicer_itk::simple::Image *' at 0x0000017A7A8B8F00&gt; &gt;
&gt;&gt;&gt; image_array = sitk.GetArrayFromImage(image)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.1.0-2022-10-15\lib\Python\Lib\site-packages\SimpleITK\extra.py", line 269, in GetArrayFromImage
    array_view = GetArrayViewFromImage(image)
  File "C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.1.0-2022-10-15\lib\Python\Lib\site-packages\SimpleITK\extra.py", line 255, in GetArrayViewFromImage
    image_memory_view = _GetMemoryViewFromImage(image)
TypeError: in method 'GetByteArrayFromImage', argument needs to be of type 'sitk::Image *'
&gt;&gt;&gt; 
```

## Expected behavior

SimpleITK methods such as `GetArrayFromImage` should not return a traceback.

## Environment
- Slicer version: Slicer-5.1.0-2022-10-15
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbumm (2022-10-19 13:51 UTC)

<p>Hi,</p>
<p>Just for planning:<br>
… will this be solved before 5.1 becomes the new stable 5.2?</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2022-10-19 17:01 UTC)

<p>We will not release the new stable version (5.2) until this problem is fixed.</p>

---

## Post #7 by @jcfr (2022-10-20 23:49 UTC)

<p>Updates:</p>
<ul>
<li>The regression is expected to be fixed by pull request <a href="https://github.com/Slicer/Slicer/pull/6606">#6606</a> that just got integrated.</li>
<li>
<code>Preview</code> release packages should be available at <a href="https://download.slicer.org">https://download.slicer.org</a> tomorrow around 11am ET</li>
</ul>
<p>cc: <a class="mention" href="/u/blowekamp">@blowekamp</a></p>

---

## Post #8 by @rbumm (2022-10-22 15:12 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>, this seems to be fixed in 5.1.0-2022-10-21 r31237 / c1715b5 .</p>

---
