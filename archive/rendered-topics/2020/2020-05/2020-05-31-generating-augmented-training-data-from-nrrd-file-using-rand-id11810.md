# Generating augmented training data from nrrd file using random translations, rotations, and deformations

**Topic ID**: 11810
**Date**: 2020-05-31
**URL**: https://discourse.slicer.org/t/generating-augmented-training-data-from-nrrd-file-using-random-translations-rotations-and-deformations/11810

---

## Post #1 by @eran_bam (2020-05-31 16:09 UTC)

<p>Hi everybody,<br>
I don’t find any tutorial on how to connect between python and 3Dslicer without using python interactor.<br>
After doing segmentation in 3d slicer I read the file in python:<br>
readdata, header = nrrd.read(filename)</p>
<p>And I want to use the nrrd file to see the segmentation on python, in the header I have some array, but I don’t know how to show the segmentation.<br>
Can someone guide me to some tutorial or help me to understand what to do now.</p>
<p>I’m very new with 3Dslicer,<br>
I don’t want to use with python interactor.</p>

---

## Post #2 by @pieper (2020-05-31 16:48 UTC)

<aside class="quote no-group" data-username="eran_bam" data-post="1" data-topic="11810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eran_bam/48/6991_2.png" class="avatar"> eran_bam:</div>
<blockquote>
<p>I’m very new with 3Dslicer,<br>
I don’t want to use with python interactor.</p>
</blockquote>
</aside>
<p>Not sure I understand this part…  Do you mean you want to use a different python interpreter and not Slicer?  In that case you would just use matpilotlib or whatever you want to visualize the array.</p>

---

## Post #3 by @lassoan (2020-05-31 18:08 UTC)

<p>Can you tell us a bit more about what you are trying to achieve?</p>
<p>Slicer segmentations are standard 3D or 4D nrrd files with <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">additional metadata</a>, which can be read with any nrrd reader. For 3D medical image visualization in Python, I would recommend to use Slicer. I have not seen anything that would even come close to it. You can even <a href="https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569">use it from Jupyter notebooks</a>.</p>

---

## Post #4 by @eran_bam (2020-06-01 08:51 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/247d98d4d89f974a8b619237c88ff05eb29faaea.png" alt="Ud" data-base62-sha1="5cOhju9XP64owjPGYrWy2rStAAa" width="590" height="433"></p>
<p>Sorry if I was not so clear, I upload the picture of the model and files.</p>
<p>I want to load this model on python (using pycharm) and I want to do data augmentation (rotate the 3D image), and after that to decompose the model into 3 images (what I segment).<br>
I don’t know how to use it and this is the reason I ask for a tutorial.</p>

---

## Post #5 by @lassoan (2020-06-02 20:57 UTC)

<p>You can apply random linear and warping transforms to a 3D volume is quite easy using Slicer modules as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Apply_random_deformations_to_image">this Python code snippet</a> and then you can use these augmented data sets to train your network as you would do it in any other Python environment.</p>
<p>Note that since Slicer includes a full Python environment, you can do everything without leaving Slicer. The advantages that 1. you have access to full, interactive 3D visualization of lots of 3D data types and 2. you can Slicer’s built in features to specify inputs, verify outputs, quantify, and quality-control results. We managed to integrate all these with usual Python tools, so while Slicer is running, you can still connect to it using Pycharm - either using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">debugging interface</a> or <a href="https://github.com/Slicer/SlicerJupyter">Jupyter notebook interface</a>.</p>

---

## Post #6 by @eran_bam (2020-06-03 05:32 UTC)

<p>Thank you for your help.<br>
You convinced me , and I try to do data augmentation with 3Dslicer, but can you know how can I do it automatically, Because I want to create 10e3 samples, and I would do it with hands it will take a years.</p>
<p>I want to take the cube (slices, h,w) - CT  and to transform it (rotate, affine etc…) and to save the model in some file on my computer. After that, load the model on pycharm and train it.</p>

---

## Post #7 by @pieper (2020-06-03 13:22 UTC)

<p><a class="mention" href="/u/eran_bam">@eran_bam</a> this is isn’t exactly what you are looking for but it will give you an idea of how you might approach this.  The function creates a numpy array with a bunch of randomly positioned and oriented slices from a volume.  The array could then be fed into a machine learning network.  If you study the scripts that Andras linked above you can modify this to perturb the parameters of transforms and also extract volume arrays instead of just slices.  This kind of code could also be wrapped in a generator so your network can get new training batches on demand rather than creating them all in advance.</p>
<pre><code class="lang-auto">def randomSlices(volume, sliceCount, sliceShape):
    layoutManager = slicer.app.layoutManager()
    redWidget = layoutManager.sliceWidget('Red')
    sliceNode = redWidget.mrmlSliceNode()
    sliceNode.SetDimensions(*sliceShape, 1)
    sliceNode.SetFieldOfView(*sliceShape, 1)
    bounds = [0]*6
    volume.GetRASBounds(bounds)
    imageReslice = redWidget.sliceLogic().GetBackgroundLayer().GetReslice()

    sliceSize = sliceShape[0] * sliceShape[1]
    X = numpy.zeros([sliceCount, sliceSize])

    for sliceIndex in range(sliceCount):
        position = numpy.random.rand(3) * 2 - 1
        position = [bounds[0] + bounds[1]-bounds[0] * position[0],
                    bounds[2] + bounds[3]-bounds[2] * position[1],
                    bounds[4] + bounds[5]-bounds[4] * position[2]]
        normal = numpy.random.rand(3) * 2 - 1
        normal = normal / numpy.linalg.norm(normal)
        transverse = numpy.cross(normal, [0,0,1])
        orientation = 0
        sliceNode.SetSliceToRASByNTP( normal[0], normal[1], normal[2], 
                                      transverse[0], transverse[1], transverse[2], 
                                      position[0], position[1], position[2],
                                      orientation) 
        if sliceIndex % 100 == 0:
            slicer.app.processEvents()
        imageReslice.Update()
        imageData = imageReslice.GetOutputDataObject(0)
        array = vtk.util.numpy_support.vtk_to_numpy(imageData.GetPointData().GetScalars())
        X[sliceIndex] = array
    return X

</code></pre>

---

## Post #8 by @lassoan (2020-06-03 15:58 UTC)

<p>I’ve updated the volume augmentation script to apply random translations and rotations in addition to the random deformations, and to also take screenshots so that you can get a quick overview of how the augmented data looks like.</p>
<p>Gallery of example output:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/997a93c14e8d46858b371c0bb1ce5d88c278940b.jpeg" data-download-href="/uploads/short-url/lTJFKml7VlX5O7UgDfcVrHSJzaX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997a93c14e8d46858b371c0bb1ce5d88c278940b_2_690x187.jpeg" alt="image" data-base62-sha1="lTJFKml7VlX5O7UgDfcVrHSJzaX" width="690" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997a93c14e8d46858b371c0bb1ce5d88c278940b_2_690x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997a93c14e8d46858b371c0bb1ce5d88c278940b_2_1035x280.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997a93c14e8d46858b371c0bb1ce5d88c278940b_2_1380x374.jpeg 2x" data-dominant-color="262221"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2000×543 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Script that generated it:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/428af5285da75dc033d32ebff65ba940">
  <header class="source">

      <a href="https://gist.github.com/lassoan/428af5285da75dc033d32ebff65ba940" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/428af5285da75dc033d32ebff65ba940" target="_blank" rel="noopener">https://gist.github.com/lassoan/428af5285da75dc033d32ebff65ba940</a></h4>

  <h5>volumeAugment.py</h5>
  <pre><code class="Python"># This script randomly warps a 3D volume and adds random translations, rotations,
# and save each resulting 3D volume (and a screenshot for quick overview)
#
# The script can be executed by copy-pasting into 3D Slicer's Python console
# or in a Jupyter notebook running 3D Slicer kernel (provided by SlicerJupyter extension).
#
# Prerequisites:
# - Recent Slicer-4.11 version
# - SlicerIGT extension installed (for random deformations)
</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/428af5285da75dc033d32ebff65ba940" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @eran_bam (2020-06-06 13:32 UTC)

<p>Hi Steve and lassoan,</p>
<p>I tried to do everything you told me, but it does not work.<br>
To simplify the question can you guide me  how can I do this step:</p>
<ol>
<li>load nrrd file : images.nrrd, Segmentation_1.seg.nrrd   -&gt; (cube, cube_seg)</li>
<li>To translate the two cubes (with some matrix, never mind) and multiply between them (translate_cube * translate_cube_seg).</li>
<li>sum up the column (a bunch of slices, height, width) of the multiply cubes to create a 2D image<br>
(like: Img = sum(multi_cube[:, I, :])<br>
image[i, :] = Img).</li>
<li>save that image</li>
</ol>
<p>I think it’s very simple but I don’t know how to do this with a 3D slicer package.<br>
I try to do this with a regular python package, but it does not work on 3D.</p>
<p>Thanks for helping me.</p>

---

## Post #10 by @lassoan (2020-06-06 15:29 UTC)

<aside class="quote no-group" data-username="eran_bam" data-post="9" data-topic="11810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eran_bam/48/6991_2.png" class="avatar"> eran_bam:</div>
<blockquote>
<p>I tried to do everything you told me, but it does not work.</p>
</blockquote>
</aside>
<p>Have you tried to copy-paste the <a href="https://gist.github.com/lassoan/428af5285da75dc033d32ebff65ba940">complete example</a> that I posted above?</p>
<p>If it works, then you can modify input parameters one by one. For example, use your input volume instead of download a sample data.</p>
<p>I’ve updated the example to also transform a segmentation (or label volume) that corresponds to the same volume. This way you get pairs of volume &amp; label that you can directly use for training.</p>
<p>Let us know how it works.</p>

---

## Post #11 by @eran_bam (2020-06-10 09:55 UTC)

<p>I think I will try another way, that what I get<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d93bd8b1219624d3261f8d8581f576a4299c6d49.jpeg" data-download-href="/uploads/short-url/uZJPymNd0AAYZ3Zwobg04xS6sAh.jpeg?dl=1" title="transformedVolume_0000" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d93bd8b1219624d3261f8d8581f576a4299c6d49_2_345x244.jpeg" alt="transformedVolume_0000" data-base62-sha1="uZJPymNd0AAYZ3Zwobg04xS6sAh" width="345" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d93bd8b1219624d3261f8d8581f576a4299c6d49_2_345x244.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d93bd8b1219624d3261f8d8581f576a4299c6d49_2_517x366.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d93bd8b1219624d3261f8d8581f576a4299c6d49_2_690x488.jpeg 2x" data-dominant-color="272525"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">transformedVolume_0000</span><span class="informations">1266×898 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And I try to figure it out, but I failed.</p>

---

## Post #12 by @lassoan (2020-06-10 12:41 UTC)

<p>Does the example work, if you run it as is?</p>
<p>Does the example work if you just change the input volume?</p>
<p>If the 3D volume appears off center in the screenshots, as it can be seen in the screenshot above then that’s just a cosmetic issue - all the generated volumes are still good - and you can fix the screenshots by centering the 3D view before starting the script.</p>
<p>Make sure you use a very recent Slicer Preview Release.</p>

---
