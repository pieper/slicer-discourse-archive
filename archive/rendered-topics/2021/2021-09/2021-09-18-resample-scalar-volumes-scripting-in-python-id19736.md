---
topic_id: 19736
title: "Resample Scalar Volumes Scripting In Python"
date: 2021-09-18
url: https://discourse.slicer.org/t/19736
---

# Resample Scalar Volumes - Scripting in Python

**Topic ID**: 19736
**Date**: 2021-09-18
**URL**: https://discourse.slicer.org/t/resample-scalar-volumes-scripting-in-python/19736

---

## Post #1 by @Sharada (2021-09-18 05:07 UTC)

<p>Hello,</p>
<p>I am trying to generate transformations and resample scalar volumes in Slicer programmatically with Python. And have two questions:</p>
<ol>
<li>I am unable to find a scripted module corresponding to ‘Resample Scalar/Vector/DWI Volume’ on GitHub. The steps I need to implement are - set input volume, create new output volume as, set the transform, reference volume, and ensure linear interpolation. Can someone please help me to get started?</li>
<li>I am working in a Jupyter Notebook with Slicer kernel. As an attempt at automation, I am trying to pause my run, prompt user to add fiducials to the image on Slicer, and then continue running the script.<br>
This is not working as it just freezes my jupyter notebook and fails the kernel. Any suggestions on how I could implement this?</li>
</ol>
<p>Thank you,<br>
Sharada</p>

---

## Post #2 by @lassoan (2021-09-18 18:03 UTC)

<aside class="quote no-group" data-username="Sharada" data-post="1" data-topic="19736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>‘Resample Scalar/Vector/DWI Volume’ on GitHub</p>
</blockquote>
</aside>
<p>It is implemented in C++, see source code <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI/ResampleScalarVectorDWIVolume">here</a>. You can call CLI module from Python as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">here</a>.</p>
<aside class="quote no-group" data-username="Sharada" data-post="1" data-topic="19736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ba8739/48.png" class="avatar"> Sharada:</div>
<blockquote>
<p>As an attempt at automation, I am trying to pause my run, prompt user to add fiducials to the image on Slicer, and then continue running the script.</p>
</blockquote>
</aside>
<p>Notebooks are great for development and batch processing but if you want to implement interactive workflows for end users then scripted modules is a much more suitable option. You can create a simple GUI that contains a node selector to place markups points, maybe some more GUI widgets to set parameters, etc. Script in your notebook will become the module logic. I would recommend the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab bootcamp Slicer programming tutorial</a> to learn how to turn your script into a Slicer module.</p>

---

## Post #3 by @Sharada (2021-09-18 19:16 UTC)

<p>Hi Andras,</p>
<p>Thank you for the quick response! I tried following the example you provided for the 1st problem and I still have an error. I have an input volume labeled ‘Axial’ and a transform ‘ACPC Transform’ already created in Slicer.</p>
<p>I don’t understand why there is no data assigned to “Input Volume” when I clearly have.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae83fc712cf60642ffc9fe7b07c0ba2bf3ebbbfe.png" data-download-href="/uploads/short-url/oTPRf8GzfYPE5lEHrSNfv4dX9h4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae83fc712cf60642ffc9fe7b07c0ba2bf3ebbbfe.png" alt="image" data-base62-sha1="oTPRf8GzfYPE5lEHrSNfv4dX9h4" width="690" height="405" data-dominant-color="F1EFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">781×459 22.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried looking for similar issues and could not troubleshoot. I might be missing something very minor as I am new to Slicer. Could you please help?</p>
<p>I will follow your advice about my 2nd question - thanks for the input on that.</p>
<p>Thanks,<br>
Sharada</p>

---

## Post #4 by @rbumm (2021-09-18 19:37 UTC)

<p>Probably you should do something like</p>
<pre><code class="lang-auto">firstVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
...
parameters["inputVolume"] = firstVolumeNode
...

</code></pre>
<p>Plus: you need to 100 % sure about each parameter name. At least “Reference Volume (xxxx)” from your example seems not correct.</p>

---

## Post #5 by @rbumm (2021-09-18 19:53 UTC)

<p>Just checked the source of resampleModule (link above) and it shows that the CLI call needs the following parameter strings:  “inputVolume”, “outputVolume”, “referenceVolume”, “transformationFile” and “interpolationType” .</p>

---

## Post #6 by @Sharada (2021-09-18 20:00 UTC)

<p>Thank you, yes. I also found the same thing after your comment about verifying the parameter names. Unfortunately, I have the same error still. I tried pulling the volumes using “slicer.mrmlScene.GetFirstNodeByClass” like you mentioned, instead of “slicer.util.getNode” just to see if it would make a difference. I still have the same error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64ace2dadb9715784ee4e042f9f8b2377704de47.png" data-download-href="/uploads/short-url/emC9xENoS3xt2rRfQfYnrlEu4gD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64ace2dadb9715784ee4e042f9f8b2377704de47.png" alt="image" data-base62-sha1="emC9xENoS3xt2rRfQfYnrlEu4gD" width="690" height="371" data-dominant-color="F2F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">956×515 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not familiar with C++, so it is a little hard for me to understand the logic. Any other suggestions?</p>
<p>Thanks,<br>
Sharada</p>

---

## Post #8 by @rbumm (2021-09-18 20:57 UTC)

<p><a href="https://nipype.readthedocs.io/en/latest/api/generated/nipype.interfaces.slicer.filtering.resamplescalarvectordwivolume.html" rel="noopener nofollow ugc">Here</a> is a complete description of all the parameters.</p>
<p>“inputVolume” (a pathlike object or string representing an existing file) – Input Volume to be resampled.</p>

---

## Post #9 by @lassoan (2021-09-18 21:02 UTC)

<p>As the error message tells, you provided a collection of nodes, instead of a volume node. This is because the method you used provides a collection of nodes. I would recommend to use <code>slicer.util</code> helper functions to get nodes from the scene because they are easier to use in Python.</p>

---

## Post #10 by @Sharada (2021-09-18 21:14 UTC)

<p>Thank you so much Rudolf and Andras! I was able to follow your advice and pass the right datatype. I visualized the volume resampled manually using Slicer and the one I did with Python - They match perfectly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dc0f34190cbe85e2ef648a371ba6553d8b3297c.png" data-download-href="/uploads/short-url/6wKSz8rSHecWdlyGa4EVxeFVS3y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dc0f34190cbe85e2ef648a371ba6553d8b3297c.png" alt="image" data-base62-sha1="6wKSz8rSHecWdlyGa4EVxeFVS3y" width="690" height="212" data-dominant-color="EFEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1053×325 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/089e7bdf294ea7353cdec14783c7a5dcfcf54482.jpeg" data-download-href="/uploads/short-url/1efmVSVtLrXly1cWimiTW8ftGZc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/089e7bdf294ea7353cdec14783c7a5dcfcf54482_2_690x439.jpeg" alt="image" data-base62-sha1="1efmVSVtLrXly1cWimiTW8ftGZc" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/089e7bdf294ea7353cdec14783c7a5dcfcf54482_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/089e7bdf294ea7353cdec14783c7a5dcfcf54482_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/089e7bdf294ea7353cdec14783c7a5dcfcf54482_2_1380x878.jpeg 2x" data-dominant-color="405762"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1382×880 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My 3D rendering is not working for some reason, but I think this definitely solved my issue.</p>
<p>Thanks again for the wonderful software and all the support you provide!</p>
<p>Best,<br>
Sharada</p>

---

## Post #11 by @Sharada (2021-09-18 21:43 UTC)

<p>Quick update - ‘slicer.util.getNode’ works too! The parameter names were the only thing that changed between what you see below and what I had before.</p>
<p>outputVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
outputVolumeNode.SetName(‘Axial ACPC’)</p>
<p>resampleModule = slicer.modules.resamplescalarvectordwivolume</p>
<p>parameters = {}<br>
parameters[‘inputVolume’] =  slicer.util.getNode(‘Axial’)<br>
parameters[‘outputVolume’] = slicer.util.getNode(‘Axial ACPC’)<br>
parameters[‘referenceVolume’] = slicer.util.getNode(‘Axial’)<br>
parameters[‘transformationFile’] =  slicer.util.getNode(‘ACPC_Transform’)<br>
parameters[‘interpolationType’] = ‘linear’</p>
<p>cliNode = slicer.cli.runSync(resampleModule,None,parameters)</p>
<p>if cliNode.GetStatus() &amp; cliNode.ErrorsMask:<br>
errorText = cliNode.GetErrorText()<br>
slicer.mrmlScene.RemoveNode(cliNode)<br>
raise ValueError("CLI execution failed: " + errorText)</p>

---
