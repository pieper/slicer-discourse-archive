---
topic_id: 23705
title: "How To Load Dense Dvfs From Voxelmorph To Slicer"
date: 2022-06-05
url: https://discourse.slicer.org/t/23705
---

# How to load dense DVFs (from VoxelMorph) to Slicer

**Topic ID**: 23705
**Date**: 2022-06-05
**URL**: https://discourse.slicer.org/t/how-to-load-dense-dvfs-from-voxelmorph-to-slicer/23705

---

## Post #1 by @BraveDistribution (2022-06-05 00:12 UTC)

<p>Hello,</p>
<p>I have my whole pipeline implemented in Slicer (sequence registration (elastix) and application to surface models). I have ~20 patients and 2k volumes per patient (liver displacement due to respiratory cycle), which yields up total of 40 000 samples. I tried elastix registration for liver, however the inference time is ~7 minutes per volume, which makes it unfeasible.</p>
<p>I was looking into <a href="https://github.com/voxelmorph/voxelmorph" rel="noopener nofollow ugc">voxelmorph</a>, since the inference time is much faster. I get a tensor of shape (1, 3, vol size) where shape 3 is a displacement vector for x,y,z coordinates. How can I load torch tensor into Slicer as TransformNode?</p>
<p>thanks in advance.</p>

---

## Post #2 by @mau_igna_06 (2022-06-05 11:06 UTC)

<p>Why not sample some key points on the sequence and make.limear.transform approximations for that</p>
<p>Hope it helps</p>

---

## Post #3 by @pieper (2022-06-05 15:42 UTC)

<p>It would be great to use voxelmorph with Slicer.  It should just be a matter of assigning the numpy array into a <code>vtkMRMLGridTransformNode</code>.  If the grid geometry matches one of the input datasets you can just copy over the IJKToRAS.  <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L698-L740">You can follow this example.</a></p>
<p>If this works well it would be great to have a SlicerVoxelMorph extension.  It should be possible to run VoxelMorph using Slicer’s python environment.</p>

---

## Post #4 by @BraveDistribution (2022-06-05 16:45 UTC)

<p>So, vtkMRMLGridTransformNode is the output that I want to have? (the same output type as the one from Elastix?</p>
<pre><code class="lang-auto">gridTransform = slicer.vtkMRMLGridTransformNode()
gridTransform.SetName(slicer.mrmlScene.GenerateUniqueName(volumeNode.GetName()+' acquisition transform'))
gridTransform.SetAndObserveTransformToParent(transform)
</code></pre>
<p>To get the GridTransformNode, I need to have vtkOrientedGridTransform:</p>
<pre><code class="lang-auto">transform = slicer.vtkOrientedGridTransform()
transform.SetGridDirectionMatrix(directionMatrix)
transform.SetDisplacementGridData(gridImage)
</code></pre>
<p>and to get vtkOrientedGridTransform I need directionMatrix and gridImage.<br>
directionMatrix is obtained from the volume, same as gridImage.</p>
<p>So, let’s say, I have a fixed volume, moving volume. I want to perform fixed → moving volume through voxelmorph, which yields me a displacement field.</p>
<p>Which volume should I get the directionMatrix and gridImage from? Fixed volume or moving volume?</p>
<p>What about this part of the code?</p>
<pre><code class="lang-auto">displacements = slicer.util.arrayFromGridTransform(gridTransform)
      for sliceIndex in range(slices):
        for row in range(2):
          for column in range(2):
            displacements[sliceIndex][row][column] = targetCorners[sliceIndex][row][column] - sourceCorners[sliceIndex][row][column]
</code></pre>
<p>Thanks.</p>
<p>I’ll try this later today. Sorry if my questions are easy to answer, however I don’t have that much experience from this domain.</p>

---

## Post #5 by @pieper (2022-06-05 17:50 UTC)

<aside class="quote no-group" data-username="BraveDistribution" data-post="4" data-topic="23705">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bravedistribution/48/14564_2.png" class="avatar"> BraveDistribution:</div>
<blockquote>
<p>Which volume should I get the directionMatrix and gridImage from? Fixed volume or moving volume?</p>
</blockquote>
</aside>
<p>Yes, the easiest thing to do would be to examine the results of Elastix and replicate it.   Some things will depend on the conventions used by the registration code, such as whether the vectors in the array indicate where the moving voxels go (modeling transform) or where the fixed voxels come from (resampling transform).  They are effectively inverses of each other, but the transform is not always well defined.  See <a href="https://discourse.slicer.org/t/inverting-elastix-transform/8123/4">this post</a> and search for similar for more info.  For a modeling transform you would get the geometry from the moving volume, and for a resampling transform it would come from the fixed volume.</p>
<aside class="quote no-group" data-username="BraveDistribution" data-post="4" data-topic="23705">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bravedistribution/48/14564_2.png" class="avatar"> BraveDistribution:</div>
<blockquote>
<p>What about this part of the code?</p>
</blockquote>
</aside>
<p>Effectively you just need to create the transform node and grid transform and then use <code>slicer.util.arrayFromGridTransform(gridTransform)</code> to get a numpy array.  Unlike the dicom example, you should be able to just do a single assignment like <code>gridArray[:] = voxelmorphArray</code> although there may be some shuffling required if the data layout is not the same (unlikely).</p>
<p>The dicom example is a case where the transform has different dimensions than the volume, but if yours is a dense vector field you can just copy geometry from the input volumes.  In the end what matters is that the transformation is well defined at every point in space.</p>

---

## Post #6 by @mau_igna_06 (2022-06-05 19:05 UTC)

<p>Why not sample the sequencies</p>
<ul>
<li>a grid transform every n samples of total, let’s.say 10 or 5% of them. And you compute a.linear interpolation of the vectors betweem each time poimt</li>
</ul>
<p>Doing somethin likenon the example maybe</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.itk.org/t/how-to-speed-up-resample-interpolator/5026">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/how-to-speed-up-resample-interpolator/5026" target="_blank" rel="noopener" title="01:36AM - 31 May 2022">ITK – 31 May 22</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8a8379ed42cbc60fb262a064faca192c7d7111e7.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://discourse.itk.org/t/how-to-speed-up-resample-interpolator/5026" target="_blank" rel="noopener">how to speed up resample interpolator?</a></h3>

  <p>When i use BsplineInterpolator to resample my nifit file(315x512x512) to (369X663x663), it takes almost 20 min, that  is too low.  how can i to speed up this?  cpu: i5-4590 3.3ghz  The following is my resample code:  typedef itk::ResampleImageFilter...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 1 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2022-06-05 19:45 UTC)

<p>You can also look at ANTs registration library. It is available in Slicer via the SlicerANTs extension.</p>
<p>The 7 minute registration time is too long. You can typically get rigid registration in 10-20 seconds and deformable registration under 1 minute. Most likely you need to tune your optimization parameters to achieve registration in a minute.</p>
<p>However, spending your time with parameter optimization may not worth the effort, because you could reduce the overall computation time by running the registrations on many computers. You can rent hundreds of virtual machines from a cloud provider to get all your computations done in 1-2 days for a few hundred dollars.</p>
<p>I agree with <a class="mention" href="/u/pieper">@pieper</a> though that if voxelmorph looks promising - at least one magnitude faster than Elastix and ANTs and provides similar quality results - then it would be nice to make it available in Slicer.</p>

---

## Post #8 by @BraveDistribution (2022-06-05 19:59 UTC)

<p>Can you recommend any good 4D intra-patient parameters for MRI liver (abdominal)? If I had satisfactory results under 1 min per MRI volume, it would be possible to do it over cloud as you suggested. Right now, it goes around 7 min/volume on a server with better CPU.</p>
<p>I used following parameters: <a href="https://elastix.lumc.nl/modelzoo/par0057/" rel="noopener nofollow ugc">https://elastix.lumc.nl/modelzoo/par0057/</a> in Slicer Elastix plugin.</p>

---

## Post #9 by @lassoan (2022-06-05 20:28 UTC)

<p>Getting good quality results is the first and most important step. You can now experiment with all parameters that make the registration faster.</p>
<p>Check how long the rigid registration takes. If that’s negligible then you can focus on just the deformable step.</p>
<p>To make the registration faster, you can make every iteration faster by tuning the metric computation (e. g., number of samples) or do less iterations (make larger steps and/or stop earlier,  for example by reducing the maximum number of iterations).</p>
<p>You may also find that you get equivalent results by reducing your image resolution by a factor of 2x (or even 4x). That could make the registration faster, too.</p>

---

## Post #10 by @BraveDistribution (2022-06-05 20:33 UTC)

<p>Hi <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> ,</p>
<p>I am sorry but I don’t understand that much what you suggest.</p>
<p>So my problem is 50k volumes of 20 patients but I have only one segmentation per patient. I need to get the segmentation of all volumes by using transform on the segmented mask.</p>
<blockquote>
<p>Effectively you just need to create the transform node and grid transform and then use <code>slicer.util.arrayFromGridTransform(gridTransform)</code> to get a numpy array. Unlike the dicom example, you should be able to just do a single assignment like <code>gridArray[:] = voxelmorphArray</code> although there may be some shuffling required if the data layout is not the same (unlikely).</p>
</blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> thanks so far! however</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.arrayFromGridTransform(gridTransform)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 1604, in arrayFromGridTransform
    nshape = tuple(reversed(displacementGrid.GetDimensions()))
AttributeError: 'NoneType' object has no attribute 'GetDimensions'
</code></pre>
<p>I think, the gridTransform does not have displacementGrid set (if I follow the example above).</p>

---

## Post #11 by @BraveDistribution (2022-06-06 02:00 UTC)

<p>Just a minor update.</p>
<p>We can update the displacement field with following approach:<br>
1/ Register the volumes with simple rigid transform that takes just couple of seconds.<br>
2/ Use following approach to update the displacement field.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; b = slicer.util.arrayFromGridTransform(getNode("Transform_1"))
&gt;&gt;&gt; a = np.load('voxelmorph.npz')
&gt;&gt;&gt; b[:] = a
</code></pre>
<p>It does work for me, however the register volume looks terrible. I don’t know why right now, but as soon as I figure that out, I’ll accept your solution in forum.</p>

---

## Post #12 by @mau_igna_06 (2022-06-06 08:01 UTC)

<p>Let’s say you got n/6 dicoms (from the same patient) to process then you need to iterate through the first one, get a transform from n_0 to n_1, from that one do the following repeat applying the transform that you got previously to n1 and calculate from n_1 to n2 and apply it to n2 and so on, n times… The timeseries that are in the middle you approximate them with linear transforms swithching the angle on traslation and the translation slightly.+</p>
<p>Mauro</p>

---
