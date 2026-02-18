# How auto W/L is implemented in 3DSlicer?

**Topic ID**: 8797
**Date**: 2019-10-16
**URL**: https://discourse.slicer.org/t/how-auto-w-l-is-implemented-in-3dslicer/8797

---

## Post #1 by @Scorbinwen (2019-10-16 09:12 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1<br>
Expected behavior:NO<br>
Actual behavior:NO<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14fa5d66cc988e633cb650db1afcfcb6f72f7d76.gif" alt="%E6%8D%95%E8%8E%B7" data-base62-sha1="2ZzX7JKFbzIwPKb2sYJyVPoTDtI" width="638" height="50"><br>
How auto W/L is implemented in 3DSlicer?<br>
I’m fanscinated with the auto W/L module in 3DSlicer,which satisfies my requirement for visualizing MR volume.But I want to use this functionality for batch processing,so I want to know the exact algorithm.<br>
I want know whether this functionality can be implemented using ITK apis.<br>
Programmatic advice is welcome.<br>
Thank you <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2019-10-16 14:24 UTC)

<p>We define window/level based on the image histogram (using <a href="https://vtk.org/doc/nightly/html/classvtkImageHistogramStatistics.html" rel="nofollow noopener">vtkImageHistogramStatistics</a>):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/9cd58e8ebd623c554a73881c5a7c1e8cf05f5361/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L733-L770" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/9cd58e8ebd623c554a73881c5a7c1e8cf05f5361/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L733-L770" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/9cd58e8ebd623c554a73881c5a7c1e8cf05f5361/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L733-L770</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="733" style="counter-reset: li-counter 732 ;">
<li>if (this-&gt;HistogramStatistics == nullptr)</li>
<li>  {</li>
<li>  this-&gt;HistogramStatistics = vtkImageHistogramStatistics::New();</li>
<li>
</li>
<li>  // Set automatic window/level to include the entire intensity range</li>
<li>  // (except top/bottom 0.1%, to not let a very thin tail of the intensity</li>
<li>  // distribution to decrease the image contrast too much).</li>
<li>  // While in CT and sometimes in MRI, there may be a large empty area</li>
<li>  // outside the reconstructed image, which could be suppressed</li>
<li>  // by a larger lower percentile value, it would make the method</li>
<li>  // too specific to particular imaging modalities and could lead to</li>
<li>  // suboptimal results for other types of images.</li>
<li>  // Therefore, we choose small, symmetric percentile values here</li>
<li>  // and maybe add modality-specific methods later (e.g., for CT</li>
<li>  // images we could set lower value to -1000HU).</li>
<li>  this-&gt;HistogramStatistics-&gt;SetAutoRangePercentiles(0.1, 99.9);</li>
<li>
</li>
<li>  // Percentiles are very low (0.1%), so there is no need for</li>
<li>  // range expansion.</li>
<li>  this-&gt;HistogramStatistics-&gt;SetAutoRangeExpansionFactors(0.0, 0.0);</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/9cd58e8ebd623c554a73881c5a7c1e8cf05f5361/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L733-L770" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @cpinter (2019-10-16 15:50 UTC)

<aside class="quote no-group" data-username="Scorbinwen" data-post="1" data-topic="8797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/scorbinwen/48/2154_2.png" class="avatar"> Scorbinwen:</div>
<blockquote>
<p>I want to use this functionality for batch processing</p>
</blockquote>
</aside>
<p>I’m really curious what do you mean by this <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Because W/L is a strictly visualization feature that has no persistent effect on the data, but batch processing typically changes the data. Can you please shed some light on it for us?</p>

---

## Post #4 by @Scorbinwen (2019-10-17 03:17 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="8797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>visualization feature that has no persistent effect on the data, but batch processing typically changes the data. Can you please shed some light on it for us?</p>
</blockquote>
</aside>
<p>Oh,Sorry about my unclear statement,I want to convert the MRI volumes to PNG images,while maximally maintaining the MRI image’s detatils.Luckily, auto W/L module in 3DSlicer just satisfies  my very requirement.But  I know this W/L visualization feature has no persistent effect on the data,so I try to write a program to process these MRI data based on the auto W/L algorithm.<br>
Thank you for your kind reply, <span class="mention">@Iassoan</span> has solved my problem.<br>
Thank you both very much~~</p>

---

## Post #5 by @Scorbinwen (2019-10-17 03:50 UTC)

<p>Thank you for your kind reply,<br>
I will try this algorithm.<br>
Thank you~~</p>

---

## Post #6 by @Chris_Rorden (2019-10-18 15:15 UTC)

<p>I would be very cautious about scaling medical imaging data to PNG. While PNG <a href="https://en.wikipedia.org/wiki/Portable_Network_Graphics" rel="nofollow noopener">can support 16-bit grayscale</a>, most implementations only support 8-bit (e.g. 256 shades of gray). While that may be sufficient with many machine learning algorithms (e.g. facial recognition of photographs) I would be very wary of using 8-bits to represent medical imaging data. Since you mention MR scans, in fMRI scans a 1% signal change is huge. Most of the brightness comes from constant properties (e.g. amount of water in the voxel), and we are seeking a very small but reliable change in signal. You really want to be careful to preserve the precision of your data. As a minimum, you might want to consider first doing your desired low/high pass filter, then subtracting each image from the mean, and looking at scaling these residual values from 0…255.</p>

---

## Post #7 by @Scorbinwen (2019-11-25 06:29 UTC)

<p>Thank you for your advice,I’m reconsidering my problems.</p>

---

## Post #8 by @shai-ikko (2023-12-13 13:02 UTC)

<p>Since I was just looking for this, and the code link is no longer valid, here’s an updated (and more durable, hopefully) link:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/v5.6.1/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L749-L786">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/v5.6.1/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L749-L786" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/v5.6.1/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L749-L786" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/v5.6.1/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L749-L786</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="749" style="counter-reset: li-counter 748 ;">
          <li>if (this-&gt;HistogramStatistics == nullptr)</li>
          <li>  {</li>
          <li>  this-&gt;HistogramStatistics = vtkImageHistogramStatistics::New();</li>
          <li></li>
          <li>  // Set automatic window/level to include the entire intensity range</li>
          <li>  // (except top/bottom 0.1%, to not let a very thin tail of the intensity</li>
          <li>  // distribution to decrease the image contrast too much).</li>
          <li>  // While in CT and sometimes in MRI, there may be a large empty area</li>
          <li>  // outside the reconstructed image, which could be suppressed</li>
          <li>  // by a larger lower percentile value, it would make the method</li>
          <li>  // too specific to particular imaging modalities and could lead to</li>
          <li>  // suboptimal results for other types of images.</li>
          <li>  // Therefore, we choose small, symmetric percentile values here</li>
          <li>  // and maybe add modality-specific methods later (e.g., for CT</li>
          <li>  // images we could set lower value to -1000HU).</li>
          <li>  this-&gt;HistogramStatistics-&gt;SetAutoRangePercentiles(0.1, 99.9);</li>
          <li></li>
          <li>  // Percentiles are very low (0.1%), so there is no need for</li>
          <li>  // range expansion.</li>
          <li>  this-&gt;HistogramStatistics-&gt;SetAutoRangeExpansionFactors(0.0, 0.0);</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/v5.6.1/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L749-L786" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
