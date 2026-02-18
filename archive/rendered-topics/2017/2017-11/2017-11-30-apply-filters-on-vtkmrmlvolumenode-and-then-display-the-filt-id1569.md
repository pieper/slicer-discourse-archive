# Apply filters on vtkMRMLVolumeNode and then display the filtered volume in Slicer

**Topic ID**: 1569
**Date**: 2017-11-30
**URL**: https://discourse.slicer.org/t/apply-filters-on-vtkmrmlvolumenode-and-then-display-the-filtered-volume-in-slicer/1569

---

## Post #1 by @urbancsaba (2017-11-30 20:38 UTC)

<p>Hi All,</p>
<p>I have a custom loadable modul. In this modul, I want to apply IKT or VTK filters on the previously loaded DICOM volume. I have something like this:</p>
<pre><code>vtkMRMLVolumeNode* volumeNode = d-&gt;MRMLVolumeNode; // this contains the loaded DICOM volume
vtkImageData* imageData = volumeNode-&gt;GetImageData();    //now I have the image data of that volume
</code></pre>
<p>//apply filter, for example:</p>
<pre><code>vtkSmartPointer&lt;vtkImageGaussianSmooth&gt; gaussianSmoothFilter = vtkSmartPointer&lt;vtkImageGaussianSmooth&gt;::New();
gaussianSmoothFilter-&gt;SetInputData( const_cast&lt;vtkImageData*&gt;( imageData ) );
</code></pre>
<p>I think I missed something from here because assertation happens during debug in the Update() function<br>
<code>gaussianSmoothFilter-&gt;Update();</code></p>
<p>Maybe I missed the <code>gaussianSmoothFilter-&gt;SetInputConnection(...)</code> function call before the Update(), but how can I get the proper input for this function? I have only the <code>volumeNode</code> object…</p>
<p>But now let’s assume that the <code>filtered</code> pointer holds the Gaussian filtered image:<br>
<code>vtkImageData* filtered = gaussianSmoothFilter-&gt;GetOutput();</code></p>
<p>My question is, how can I display this volume in the slice viewes?<br>
(Example codes are highly appreciated.)</p>
<p>Thank’s,<br>
Csaba</p>

---

## Post #2 by @lassoan (2017-11-30 20:44 UTC)

<p>Something like this should work:</p>
<pre><code>vtkMRMLVolumeNode* volumeNode = d-&gt;MRMLVolumeNode;
vtkNew&lt;vtkImageGaussianSmooth&gt; gaussianSmoothFilter;
gaussianSmoothFilter-&gt;SetInputData(volumeNode-&gt;GetImageData());
gaussianSmoothFilter-&gt;Update();
volumeNode-&gt;SetImageData(gaussianSmoothFilter-&gt;GetOutput());</code></pre>

---

## Post #3 by @lassoan (2017-11-30 20:54 UTC)

<p>For applying ITK and VTK filters, you don’t need to develop C++ loadable modules. The simplest is to use Python scripted modules or CLI modules. There are lots of examples for various module types <a href="https://github.com/Slicer/Slicer/tree/master/Modules">in the Slicer core</a>.</p>

---

## Post #4 by @urbancsaba (2017-11-30 22:33 UTC)

<p>Thank you Andras!</p>
<p>A little correction:</p>
<p>This one causes exception in Update():<br>
<code>gaussianSmoothFilter-&gt;SetInputData(volumeNode-&gt;GetImageData());</code><br>
but this is okay and works well:<br>
<code>gaussianSmoothFilter-&gt;SetInputConnection( volumeNode-&gt;GetImageDataConnection() );</code></p>

---

## Post #5 by @lassoan (2017-12-01 02:27 UTC)

<p>What exception did you get?</p>

---

## Post #6 by @Saima (2018-09-04 08:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SetInputData(volumeNode-&gt;GetImageData()); gaussianSmoothFilter-&gt;Update();</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Would you please tell me what I am doing wrong in the code below:</p>
<p>I need to apply normalize image filter of simple filters to volume.</p>
<pre><code>normal = vtk.vtkImageNormalize()
normal.SetInputData(volumeNode.GetImageData())
normal.Update()
volumeNode.SetImageData(normal.GetOutput())
</code></pre>
<p>Error:<br>
Traceback (most recent call last): File “&lt;string&gt;”, line 8, in &lt;module&gt; AttributeError: ‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘SetImageData’</p>

---

## Post #7 by @Saima (2018-09-04 09:03 UTC)

<p>I got the results with below but its not showing correct results when compared to results obtained using slicer APP. is this the correct filter for normalize image filter?</p>
<blockquote>
<p>normal = vtk.vtkImageNormalize()<br>
normal.SetInputConnection(volumeNode.GetImageDataConnection())<br>
normal.Update()<br>
volumeNode.SetImageDataConnection(normal.GetOutputPort())</p>
</blockquote>

---

## Post #8 by @lassoan (2018-09-05 03:45 UTC)

<p>What do you expect this filter would do? What happens instead?<br>
How did you obtain the good results that you mentioned?<br>
Why would you like to normalize an image?</p>

---

## Post #9 by @Saima (2018-09-05 04:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ld you like to normalize an image</p>
</blockquote>
</aside>
<p>I was expecting normalized image intensities. The result are:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bdd45c37229ecf4d6b9d95cd8300190cfa5dd25.png" data-download-href="/uploads/short-url/d6FwucdyhVhHdoqP8RzA2mxdBOd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bdd45c37229ecf4d6b9d95cd8300190cfa5dd25_2_690x388.png" alt="image" data-base62-sha1="d6FwucdyhVhHdoqP8RzA2mxdBOd" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bdd45c37229ecf4d6b9d95cd8300190cfa5dd25_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bdd45c37229ecf4d6b9d95cd8300190cfa5dd25_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bdd45c37229ecf4d6b9d95cd8300190cfa5dd25_2_1380x776.png 2x" data-dominant-color="4C4848"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
was expecting<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f721f973cc1c00bf44cad25def187bb5ace66764.jpeg" data-download-href="/uploads/short-url/zgeIX9JFNnunX6kOSzFuHINWnmQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f721f973cc1c00bf44cad25def187bb5ace66764_2_690x388.jpeg" alt="image" data-base62-sha1="zgeIX9JFNnunX6kOSzFuHINWnmQ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f721f973cc1c00bf44cad25def187bb5ace66764_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f721f973cc1c00bf44cad25def187bb5ace66764_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f721f973cc1c00bf44cad25def187bb5ace66764_2_1380x776.jpeg 2x" data-dominant-color="524F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to normalize an image to obtain standardize intensities before doing automatic segmentation.</p>

---

## Post #10 by @lassoan (2018-09-06 05:18 UTC)

<aside class="quote no-group" data-username="Saima" data-post="9" data-topic="1569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I want to normalize an image to obtain standardize intensities before doing automatic segmentation.</p>
</blockquote>
</aside>
<p>Applying linear intensity scaling will most likely not affect automatic segmentation results. Even the most basic methods are insensitive to global image brightness/contrast adjustments.</p>
<p>Check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">segmentation tutorials</a> and read these posts to have an idea how you can segment semi-automatically or automatically in Slicer:</p>
<aside class="quote quote-modified" data-post="3" data-topic="3161">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/automated-spinal-cord-segmentation/3161/3">Automated Spinal Cord Segmentation</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Some initialization (albeit very limited) is required by the user (which may impede its effectiveness) 

You can usually automate seed placement and thus have a completely automatic method. For example you can register a generic “atlas” image and transferring seeds to the patient image. Or you may use simple global thresholding to get candidate regions and keep the most likely candidate (that meets minimum size and shape requirements). You may also use the segmentation that sct provides as seed…
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="1980">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/7ba0ec/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-method-for-cerebrspinal-fluid-space/1980">Segmentation method for cerebrspinal fluid space</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I am a new 3D slicer user. I am looking to build a 3D model of the cerebrospinal fluid space from CT images of the human brain. I was wondering if someone could elaborate on how I should go about it. I tried using thresholding in the editor module as they have a predefined scale for CSF space, but that didn’t quite work out. 
Any help would be great!
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="5" data-topic="960">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/9dc877/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960/5">Bone segmentation to create 3D-printable STL</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Prof. Doc. Andras, 
Dear Everyone, 
I was writing back to you . I  have fixed the stl export issue. I used 
segmentaions module&gt;export,models&gt;export. and finally could save it as a 
stl file. 
Thank you again Professor for the support. 
All the best, 
Hanaa[image] 
[image]
  </blockquote>
</aside>


---

## Post #11 by @Saima (2018-09-11 09:32 UTC)

<p>Dear Andras,<br>
Is there a way to do automated segmentation for brain, tumor and ventricles together in any MRI without user input?</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #12 by @lassoan (2018-09-11 17:56 UTC)

<p>Fully automatic segmentation is probably not the best approach, but you can get very close to it (probably 1-2 minutes of user’s time) if you implement a custom script:</p>
<ul>
<li>brain: you can use SwissSkullStripper extension to get the brain completely automatically</li>
<li>ventricles: probably you can get ventricles by thresholding in brain segment region, potentially with some pre/post processing for optimal results</li>
<li>tumor: there is a large variety of their size, location, and appearance, so fully automatic detection may be very difficult; however, you should be able to segment a tumor within one minute, with minimal user input, using “Grow from seeds” effect</li>
</ul>

---

## Post #13 by @Saima (2018-09-12 08:14 UTC)

<p>Does the swiss skull stripper always use the atlas image and atlas mask. Is it reliable to use the same mask and image for any mri for extracting brain.</p>

---

## Post #14 by @Saima (2018-09-12 11:05 UTC)

<p>in accessing the swissskullmodule one step is to convert the atlasmask which is in volume into labelvolume.</p>
<p>I am doing this through script but have some problem. Dont get the correct output result for swiss.</p>
<p>I know the problem is in the mask setting it to labelvolume as the downloaded atlas is a scalarvolumenode. I did it using the GUI and it does it job.</p>
<pre><code>vol = slicer.modules.volumes
log = vol.logic()
outputlabelnode = slicer.vtkMRMLLabelMapVolumeNode()
labelVolNode = log.CreateLabelVolumeFromVolume(slicer.mrmlScene, outputlabelnode, nodeMaskAtlas)
</code></pre>
<p>Is this the way to convert a volumenode to labelvolume.</p>
<p>Problem with one parameter atlasmaskvolume as it takes the labelvolume.</p>
<p>full code: I do not know what I am doing wrong. tried alot but dont get the extracted skull in outputvolume.</p>
<pre><code>import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()
[success, atlasImage] = slicer.util.loadVolume('D:/atlasImage.mha', returnNode = True)
[success2, atlasMask] = slicer.util.loadVolume('D:/atlasMask.mha', returnNode = True)

nodeImageAtlas = slicer.util.getNode(atlasImage.GetName())
nodeMaskAtlas = slicer.util.getNode(atlasMask.GetName())

vol = slicer.modules.volumes
log = vol.logic()
vol =log.SetActiveVolumeNode(nodeMaskAtlas)
#scal = slicer.vtkMRMLScalarVolumeNode()
#slicer.mrmlScene.AddNode(scal)
labelVolume = log.CreateAndAddLabelVolume(slicer.mrmlScene, nodeMaskAtlas, nodeMaskAtlas.GetName())

outVolume = slicer.vtkMRMLScalarVolumeNode()
slicer.mrmlScene.AddNode(outVolume)
maskLabel = slicer.vtkMRMLLabelMapVolumeNode()
slicer.mrmlScene.AddNode(maskLabel)

parameters = {}
parameters['atlasMRIVolume'] = nodeImageAtlas.GetID()
parameters['atlasMaskVolume'] = labelVolume.GetID()
parameters['patientVolume'] = masterVolumeNode.GetID()

parameters['patientOutputVolume'] = outVolume.GetID()
parameters['patientMaskLabel'] = maskLabel.GetID()

swissSkullStripper = slicer.modules.swissskullstripper
slicer.cli.runSync(swissSkullStripper,None, parameters)</code></pre>

---

## Post #15 by @lassoan (2018-09-13 05:39 UTC)

<aside class="quote no-group" data-username="Saima" data-post="14" data-topic="1569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Is this the way to convert a volumenode to labelvolume</p>
</blockquote>
</aside>
<p>Yes, <code>CreateLabelVolumeFromVolume</code> method converts a scalar volume to a label volume. However, in your full script you used <code>CreateAndAddLabelVolume</code> method, which creates an empty label volume based on geometry specified by another volume.</p>
<p>The simplest is to load the label volume with the correct loading function: <code>slicer.util.loadLabelVolume()</code> - then you don’t need any conversion.</p>

---

## Post #16 by @Saima (2018-09-21 07:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="1569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>tumor: there is a large variety of their size, l</li>
</ul>
</blockquote>
</aside>
<p>Hi Andras,<br>
Could you please share the ventricle segmentation tutorial so I can get the idea of workflow and write the script for ventricle extraction. It can be done automatically through script calling modules. right?<br>
I was using threshold and island effect but island effect require user input which I do not want.</p>

---
