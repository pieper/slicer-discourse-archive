# Importing Numpy & NPZ files into Slicer

**Topic ID**: 8497
**Date**: 2019-09-19
**URL**: https://discourse.slicer.org/t/importing-numpy-npz-files-into-slicer/8497

---

## Post #1 by @stevenagl12 (2019-09-19 15:05 UTC)

<p>Hi, I have been working in python on a new deep learning algorithm. I would like to use Slicer to display the output to evaluate, but I am not sure how to import the output npz files into slicer for display, nor how to convert it into a SimpleITK image for proper orientation in Slicer and create a mesh from the image?</p>

---

## Post #2 by @lassoan (2019-09-19 18:52 UTC)

<p>You can set voxels in a volume node from numpy array by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray" rel="nofollow noopener"><code>updateVolumeFromArray</code></a>.</p>

---

## Post #3 by @stevenagl12 (2019-09-19 19:08 UTC)

<p>How do I import the npz file in the first place though? When I drag and drop or direct the data import to the files, it doesn’t import anything.</p>

---

## Post #4 by @stevenagl12 (2019-09-19 19:10 UTC)

<p>Also, I’m assuming this method correct the spacing in the normal simpleITK way? Where z,x,y get converted to x,y,z dimensions?</p>

---

## Post #5 by @lassoan (2019-09-19 19:28 UTC)

<p>You can load npz file into a numpy array using standard numpy commands (<code>numpy.load</code>).</p>
<p>If you load plain numpy arrays then you need to store metadata (such as origin, spacing, axis directions) before numpy array conversion, then retrieve it when needed. This may become easier in the future (see this <a href="https://discourse.itk.org/t/images-in-physical-space-in-python/2124/15" rel="nofollow noopener">discussion</a>), but for now there is no standard solution.</p>

---

## Post #6 by @stevenagl12 (2019-09-19 20:14 UTC)

<p>I don’t understand. I looked at the documentation, but how do yoy store the metadata information to convert?</p>

---

## Post #7 by @stevenagl12 (2019-09-19 20:15 UTC)

<p>Also, is there a way to import .nii.gz files into slicer?</p>

---

## Post #8 by @lassoan (2019-09-19 23:07 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="6" data-topic="8497" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>I don’t understand. I looked at the documentation, but how do yoy store the metadata information to convert?</p>
</blockquote>
</aside>
<p>If you load an image (nrrd, nift, etc.) then you have all the basic metadata. If you decide to convert to numpy then it is your responsibility to store the metadata somewhere where you can later find it (e.g., write to csv file that contains metadata for each file).</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="7" data-topic="8497" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Also, is there a way to import .nii.gz files into slicer?</p>
</blockquote>
</aside>
<p>That’s a nifti file, you can load it as any other supported volume file formats: drag-and-drop the image file to the application window, using menu / File / Add data, or calling <code>slicer.util.loadVolume</code>.</p>

---

## Post #9 by @stevenagl12 (2019-09-20 15:45 UTC)

<p>I have the metadata information from the original files, but when I convert them to numpy/tensor and back for pytorch, I would like to import them into slicer. So if I call in the file with np.load, and then use the updateVolumeFromArray command, how can I add the metadata to get the appropriate image?</p>

---

## Post #10 by @lassoan (2019-09-20 17:33 UTC)

<p>You can set origin, spacing, axis directions on the MRML volume node that you created from the numpy array.</p>

---

## Post #11 by @stevenagl12 (2019-09-23 15:01 UTC)

<p>I have loaded in my numpy arrays, but when I go to run the updateVolumeFromArray, I am getting the error AttributeError: ‘numpy.ndarray’ object has no attribute ‘GetImageData’. I have tried to change it to a SimpleITK image, and this is not working either.</p>

---

## Post #12 by @lassoan (2019-09-23 15:10 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="11" data-topic="8497">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>I am getting the error AttributeError: ‘numpy.ndarray’ object has no attribute ‘GetImageData’.</p>
</blockquote>
</aside>
<p>You need to provide the output MRML node as first atgument and input numpy array as second argument. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray">updateVolumeFromArray documentation</a>.</p>

---

## Post #13 by @stevenagl12 (2019-09-23 15:33 UTC)

<p>I have been using that exact syntax. I created an empty volume called Mask and I have used the update volume from array function. This is the output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66043988ff7574be9c6fdcc66061d0231b0c784e.png" data-download-href="/uploads/short-url/eytKIjwjvS3dyPkAz8SJyC6Ktjg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66043988ff7574be9c6fdcc66061d0231b0c784e_2_690x488.png" alt="image" data-base62-sha1="eytKIjwjvS3dyPkAz8SJyC6Ktjg" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66043988ff7574be9c6fdcc66061d0231b0c784e_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66043988ff7574be9c6fdcc66061d0231b0c784e_2_1035x732.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66043988ff7574be9c6fdcc66061d0231b0c784e.png 2x" data-dominant-color="5A5858"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1085×768 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have tried with quotations and without. As you can see I have the volume present in the data module, but it is saying there is no volume.</p>

---

## Post #14 by @stevenagl12 (2019-09-23 15:43 UTC)

<p>Do we have to create a volume node prior to manipulating it with this function? Or can this function create the volume node as well?</p>

---

## Post #15 by @lassoan (2019-09-23 15:50 UTC)

<p>You have a different error now. You pass a “str” object instead of a volume node object. You need to provide a valid volume node as input to store the results. You can create a volume node as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume" rel="nofollow noopener">this example</a>.</p>

---

## Post #16 by @lassoan (2019-11-08 17:59 UTC)

<p>A post was split to a new topic: <a href="/t/cannot-import-numpy-array-using-updatevolumefromarray/9091">Cannot import numpy array using updateVolumeFromArray</a></p>

---
