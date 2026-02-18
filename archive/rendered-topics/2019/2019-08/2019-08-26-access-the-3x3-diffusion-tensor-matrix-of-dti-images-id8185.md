# Access the 3x3 diffusion tensor matrix of dti images

**Topic ID**: 8185
**Date**: 2019-08-26
**URL**: https://discourse.slicer.org/t/access-the-3x3-diffusion-tensor-matrix-of-dti-images/8185

---

## Post #1 by @mshah (2019-08-26 20:16 UTC)

<p>Hi all,</p>
<p>I have a set of patients’ dti images. How do I extract the 3x3 diffusion tensor matrices per each voxel? Additionally how do I convert the DTI image to nrrd format, can I still use the DWIconvert module even though its not a DWI image?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2019-08-26 20:34 UTC)

<aside class="quote no-group" data-username="mshah" data-post="1" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> mshah:</div>
<blockquote>
<p>How do I extract the 3x3 diffusion tensor matrices per each voxel?</p>
</blockquote>
</aside>
<p>There are a couple ways, via vtk and numpy:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Access_values_in_a_DTI_tensor_volume" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Access_values_in_a_DTI_tensor_volume</a></p>
<aside class="quote no-group" data-username="mshah" data-post="1" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> mshah:</div>
<blockquote>
<p>Additionally how do I convert the DTI image to nrrd format,</p>
</blockquote>
</aside>
<p>If you have the data loaded in Slicer as a diffusion tensor, then saving in nrrd format should just work.</p>

---

## Post #3 by @mshah (2019-08-26 20:54 UTC)

<p>Hi,<br>
Thanks for the response, how do these methods to get the diffusion tensors translate to the slice depth. Per patient I have around 26 images, will the methods give me the tensors for a specified slice depth or for all of them? Additionally, when you run the code given in the links in the interactive python window, where does the information containing the diffusion tensors go? What format is it saved in?</p>

---

## Post #4 by @pieper (2019-08-26 21:14 UTC)

<p>Hi -</p>
<aside class="quote no-group" data-username="mshah" data-post="3" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> mshah:</div>
<blockquote>
<p>how do these methods to get the diffusion tensors translate to the slice depth. Per patient I have around 26 images, will the methods give me the tensors for a specified slice depth or for all of them?</p>
</blockquote>
</aside>
<p>You can get all the tensors.  The mapping between slices, rows, and columns (IJK) and tensor samples is by the 3D array where each element is a 3x3 tensor.  The mapping to patient space is defined by the <a href="https://www.slicer.org/wiki/Coordinate_systems">IJKToRAS transform</a> (and any other applied transforms).  The tensors themselves are <a href="https://na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format">measured with respect to the <code>Measurement Frame</code></a>, a 3x3 matrix you can get from the node.</p>
<aside class="quote no-group" data-username="mshah" data-post="3" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> mshah:</div>
<blockquote>
<p>Additionally, when you run the code given in the links in the interactive python window, where does the information containing the diffusion tensors go? What format is it saved in?</p>
</blockquote>
</aside>
<p>The values are stored in python variables so you can use them to perform further calculations or save them out to a file if you want.</p>
<aside class="quote no-group" data-username="mshah" data-post="3" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> mshah:</div>
<blockquote>
<p>Thanks for the response,</p>
</blockquote>
</aside>
<p>You’re very welcome.  Feel free to ask follow ups if needed.</p>

---

## Post #5 by @mshah (2019-08-26 21:30 UTC)

<p>Hi,<br>
So if they save as variables in python would I be able to access them through a jupyter notebook after they saved? How would I save them out as a file (sorry I’m new to this). Additionally, in the links you posted contain nested forloops, how does this work in the python window (since isnt the window just a line by line execution?)</p>
<p>Additionally, if I create a brain mask of each image and then extract the tensors, will this prevent me from getting the skull tensor data (which I dont need).</p>
<p>How can I create brain masks of all my patients and save them to the program so that whenever I come back to continue work I only work on the updated imaged? Is there a simple way I can save this, for example the format given in the DCM window that separates the data per patient and series?</p>

---

## Post #6 by @pieper (2019-08-26 22:13 UTC)

<p>You can have a look at some of the <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" rel="nofollow noopener">Slicer python tutorials</a> to get an idea of generally how python variables work to represent, save, and restore data.</p>
<p>Yes, you can do loops in the python interactor in Slicer.  Accessing a volume that way is shown as an example but usually not efficient.</p>
<p>The numpy array approach is usually better.  E.g. if you’ve downloaded <code>DTIBrain</code> from the SampleData module, then you can do this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a = array('DTIBrain')
&gt;&gt;&gt; a.shape
(85, 144, 144, 3, 3)
</code></pre>
<p>If you have a mask <a href="http://dmri.slicer.org/" rel="nofollow noopener">like from SlicerDMRI</a> you can also access it as a numpy array.</p>

---

## Post #7 by @mshah (2019-08-26 23:08 UTC)

<p>Again, thank you for the response!<br>
The tutorials helped a lot, but I still couldnt figure out how to save the diffusion tensors as a file. Specifically, I am trying to export all the diffusion tensors to matlab and work with them there. Is there a way to do this?</p>

---

## Post #8 by @lassoan (2019-08-26 23:23 UTC)

<p><code>slicer.util.saveNode</code> should work for diffusion images. You can load the generated .nrrd file into Matlab.</p>
<p>There are great Python packages for all kinds of data processing, including diffusion images. Why don’t you process the data directly in Python?</p>

---

## Post #9 by @pieper (2019-08-26 23:34 UTC)

<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a>, you should try to stick with Python if you can.</p>
<p>But if you need to work with matlab, you <a href="https://docs.scipy.org/doc/scipy/reference/tutorial/io.html" rel="nofollow noopener">this might be another option</a>.</p>

---

## Post #10 by @mshah (2019-08-28 05:53 UTC)

<p>Hi,</p>
<p>Thank you again for the replies. I am trying to use matlab to compare to another analysis done in that software. I have been trying save the image data however I keep getting this error. What am I doing wrong? Additionally, if I wanted to save as a .mat file how would i do so since scipy isnt built into slicer? Please let, I am really just trying to extract this data so I can work with it easier in Matlab.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64904c17ceff8743d7572669a6b051b5d80f8006.png" alt="13%20PM" data-base62-sha1="elCTX1BVZ8sGnAXmnDRyqAkFh7o" width="447" height="327"></p>

---

## Post #11 by @ljod (2019-08-28 07:20 UTC)

<p>Hi! I’m not sure what your goal is in the code? The code loops through the tensors but doesn’t do anything with the data. The last error is because the save function expects a node, but the code gives it an image data.</p>

---

## Post #12 by @mshah (2019-08-28 07:51 UTC)

<aside class="quote no-group" data-username="ljod" data-post="11" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ljod/48/652_2.png" class="avatar"> ljod:</div>
<blockquote>
<p>he code? The code loops through the tensors but doesn’t do anything with the data. The last error is because the save function expects a node, but the code gives it an image data.</p>
</blockquote>
</aside>
<p>hi i am trying to extract the 3x3 diffusion tensors per voxel and save as a .mat file</p>

---

## Post #13 by @Saima (2020-10-30 02:56 UTC)

<p>Hi Andras,<br>
How can I iterate or see values inside the tensor variable which is a vtkfloatarray. is there a way to convert to numpy and then iterate over the array.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #14 by @Saima (2020-10-30 06:27 UTC)

<p>Hi Andras,<br>
I have another question. How can I get position values of all the voxels greater than 0 from a volume image.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #15 by @Saima (2021-01-21 08:20 UTC)

<p>Hi,<br>
I need to get the tensor values from DTI image. I got the values using the following code but all the values are same. I think the values should be different for each voxel. Could you please tell me if there is something wrong with the following code:</p>
<pre><code class="lang-python">    tensors = slicer.util.array(inputVolume.GetID())
    volumeNode=slicer.util.getNode(inputVolume.GetID())
    imageData=volumeNode.GetImageData()
    tensors = imageData.GetPointData().GetTensors()
    extent = imageData.GetExtent()
    idx = 0
    for k in range(extent[4], extent[5]+1):
      for j in range(extent[2], extent[3]+1):
        for i in range(extent[0], extent[1]+1):
          tensors.GetTuple9(idx)
          idx += 1
    import json
    f = open('/home/saima/Downloads/Damon/Damon/Case131/tensors.txt', 'w')
    for x in range(5300):
        print(tensors.GetTuple(x))
        f.write(json.dumps(tensors.GetTuple(x)))
</code></pre>

---

## Post #16 by @pieper (2021-01-21 23:18 UTC)

<aside class="quote no-group" data-username="Saima" data-post="15" data-topic="8185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p><code>    tensors = slicer.util.array(inputVolume.GetID())</code></p>
</blockquote>
</aside>
<p>This was the right way to get the tensors as a numpy array.  You can just index it to get the tensor values.  You don’t need to use the VTK api.</p>

---
