---
topic_id: 7570
title: "Nvidia Clara Ai Assisted Annotation Extension"
date: 2019-07-14
url: https://discourse.slicer.org/t/7570
---

# NVIDIA Clara AI-Assisted Annotation Extension

**Topic ID**: 7570
**Date**: 2019-07-14
**URL**: https://discourse.slicer.org/t/nvidia-clara-ai-assisted-annotation-extension/7570

---

## Post #1 by @bsmarine (2019-07-14 18:01 UTC)

<p>Does anyone know of a group working on Slicer extension for the recently released NVIDIA Clara Train SDK AI-Assisted <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/README.md" rel="nofollow noopener">Annotation</a>? Our radiology department is eager to optimize our ground truth creation efforts and this looks like a promising approach. Looks like MITK already has implemented <a href="http://www.mitk.org/wiki/NvidiaAnnotationPlugin" rel="nofollow noopener">this</a>. Would love to collaborate with anyone working on this on the Slicer side, possibly to integrate with Case Iterator.</p>

---

## Post #2 by @lassoan (2019-07-14 18:33 UTC)

<p>We have not had a chance yet to evaluate Clara, but it is certainly a promising effort. It should not be too much work to put together a convenient workflow for training data generation for Clara (using Case iterator and Segment editor) and making Clara segmentation algorithm available as a Segment Editor effect. If you can spend some time with it, we would be happy to contribute.</p>
<p>You could start with trying to run the Clara examples from Slicer’s Python environment (just manual execution, scripting) and see if everything works as expected. We could discuss your findings in detail and set up a plan in an upcoming <a href="https://discourse.slicer.org/c/community/hangout">weekly hangout</a>.</p>

---

## Post #3 by @pieper (2019-07-14 20:49 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> mentioned that he saw a webinar about clara and that there was to be a video of it online somewhere.  Maybe he or someone can post a link?</p>

---

## Post #4 by @fedorov (2019-07-14 21:22 UTC)

<p>They were going to send the link to the materials at some point after the event, but they have not yet. At least I have not received it.</p>

---

## Post #5 by @drouin-simon (2019-07-14 22:38 UTC)

<p>According to this <a href="https://devblogs.nvidia.com/annotation-transfer-learning-clara-train/" rel="nofollow noopener">NVIDIA page</a>, the SDK is already integrated with Slicer <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>“Clara Train SDK’s AI Assisted Annotation accelerates the annotation process by enabling application developers to integrate deep learning tools built into the SDK with existing medical imaging viewers , such as MITK, ITK-Snap, <strong>3D Slicer</strong> or a custom-built application viewer”</p>

---

## Post #6 by @bsmarine (2019-07-14 22:50 UTC)

<p>The webinar actually had a slide with a diagram showing Slicer as a potential client for their AI-assisted annotation server. Apparently there’s a Slicer extension in development somewhere… That’s what prompted my reaching out <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>For those interested in the webinar you can access the full recording via <a href="https://www.nvidia.com/en-us/about-nvidia/webinar-portal/" rel="nofollow noopener">here</a>. Search for “Clara”. Will have to register with NVIDIA.</p>
<p>Key Takeaways From The Webinar:</p>
<ul>
<li>Two SDK container-based, open source packages: Clara Train SDK and Clara Deploy SDK</li>
<li>Introduces modular container-based approach for DL model training/inference/evaluation</li>
<li>Clara Train SDK allows use of free pre-trained models based off the <a href="http://medicaldecathlon.com/" rel="nofollow noopener">Medical Decathlon Challenge</a>
</li>
<li>Open source API offered for creating a server-client infrastructure where annotations/segmentations are generated from the server and can be touched up in client (eg Slicer, MITK, Snap-ITK) then used for re-training/transfer learning of the pre-trained models</li>
<li>Clara Deploy SDK attempts to allow end-to-end, DICOM compatible pipeline that can interface with a PACS, apply an inference and relevant post-processing then output DICOM images/renderings<br>
I haven’t been able to test everything out but am eager to collaborate with others to use Slicer with this. I think there’s much to gain on both the Slicer and NVIDIA ends.</li>
</ul>
<p><span class="mention">@alasso</span> I’ll keep you posted on our efforts here, but will also reach out to NVIDIA to find out who their Slicer collaborators!</p>

---

## Post #7 by @pieper (2019-07-14 23:22 UTC)

<p>Some earlier related work (<a href="https://github.com/faustomilletari/TOMAAT-Slicer">TOMAAT-Slicer</a>) was shown at RSNA in the nvidia booth in 2017.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/474e993eb758d58b0279c6eeaf9eb44d4caa332d.jpeg" data-download-href="/uploads/short-url/aaOiqg8tgHRQKI71rH2mSTIUf5r.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474e993eb758d58b0279c6eeaf9eb44d4caa332d_2_375x500.jpeg" alt="image" data-base62-sha1="aaOiqg8tgHRQKI71rH2mSTIUf5r" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474e993eb758d58b0279c6eeaf9eb44d4caa332d_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474e993eb758d58b0279c6eeaf9eb44d4caa332d_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474e993eb758d58b0279c6eeaf9eb44d4caa332d_2_750x1000.jpeg 2x" data-dominant-color="60674A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1170×1560 449 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/655747091df63c20e82a6db5f37c26ec68856946.jpeg" data-download-href="/uploads/short-url/esvdmZOBi4kh4gvWJWxdme54nmC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/655747091df63c20e82a6db5f37c26ec68856946_2_666x500.jpeg" alt="image" data-base62-sha1="esvdmZOBi4kh4gvWJWxdme54nmC" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/655747091df63c20e82a6db5f37c26ec68856946_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/655747091df63c20e82a6db5f37c26ec68856946_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/655747091df63c20e82a6db5f37c26ec68856946_2_1332x1000.jpeg 2x" data-dominant-color="364253"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1543×1157 386 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @fedorov (2019-07-15 13:53 UTC)

<aside class="quote no-group" data-username="bsmarine" data-post="6" data-topic="7570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bsmarine/48/3898_2.png" class="avatar"> bsmarine:</div>
<blockquote>
<p>For those interested in the webinar you can access the full recording via <a href="https://www.nvidia.com/en-us/about-nvidia/webinar-portal/">here </a></p>
</blockquote>
</aside>
<p>Thanks for the link!</p>
<p>Based on the picture, this is the webcast I joined last week:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9817e6c4081f589951c97eb7bd97beaa1d0b2fa7.png" alt="image" data-base62-sha1="lHtMC0XaMhtan8UrsBOaMuQQxtZ" width="302" height="315"></p>

---

## Post #9 by @bsmarine (2019-07-16 20:04 UTC)

<p>I reached out to NVIDIA and they shared the Slicer prototype extension they’re working on. Looks promising!</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/SachidanandAlle/Nvidia3DSlicerExtension" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/7339051?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/SachidanandAlle/Nvidia3DSlicerExtension" target="_blank" rel="nofollow noopener">SachidanandAlle/Nvidia3DSlicerExtension</a></h3>

<p>Contribute to SachidanandAlle/Nvidia3DSlicerExtension development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1cQgCBl4v3OqI3Hh8hzMvR01xiEBO2GLE/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:128/67;"><img src="https://lh6.googleusercontent.com/VhomW_MpjyJPdE0V5F74Sor2HqPcu0ZYrV-B5RUFvB5k25Yr1qHG7CWqcBY=w1200-h630-p" class="thumbnail"></div>

<h3><a href="https://drive.google.com/file/d/1cQgCBl4v3OqI3Hh8hzMvR01xiEBO2GLE/view?usp=drive_open" target="_blank" rel="nofollow noopener">3DSlicerWithNVIDASegmentation.mp4 (video)</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #10 by @lassoan (2019-07-16 20:43 UTC)

<p>It is very promising indeed. I’ve sent a pull request to make the extension compatible with Slicer Preview Releases and submitted an issue for asking clarification about how to access/set up an annotation server.</p>

---

## Post #11 by @bsmarine (2019-07-17 02:18 UTC)

<p>Here’s <a href="https://docs.nvidia.com/clara/aiaa/tlt-mi-ai-an-sdk-getting-started/index.html" rel="nofollow noopener">the latest documentation</a> for the AI-Assisted Server via NVIDIA’s Clara Train SDK.</p>
<p>I’ll also suggest to the NVIDIA team working on the extension to join in on the discussion here as I think they’d be happy provide as much detail as needed to facilitate this.</p>

---

## Post #12 by @SachidanandAlle (2019-07-18 15:11 UTC)

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/SachidanandAlle/Nvidia3DSlicerExtension/pull/1" target="_blank" rel="nofollow noopener">github.com/SachidanandAlle/Nvidia3DSlicerExtension</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">
    <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/SachidanandAlle/Nvidia3DSlicerExtension/pull/1" target="_blank" rel="nofollow noopener">Fix Python3 compatibility errors to allow running in Slicer Preview Release</a>
</h4>

<div class="date">
  by <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">lassoan</a>
  on <a href="https://github.com/SachidanandAlle/Nvidia3DSlicerExtension/pull/1" target="_blank" rel="nofollow noopener">08:36PM - 16 Jul 19 UTC</a>
</div>

<div class="github-commit-stats">
  <strong>1 commits</strong>
  changed <strong>1 files</strong>
  with <strong>19 additions</strong>
  and <strong>4 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thank for correcting and making it compatible <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #13 by @SachidanandAlle (2019-07-18 15:13 UTC)

<p>Some optimizations are possible specially related to image saving etc… before sending it to AIAA server.<br>
But otherwise, the next step is to add Polygon Editing feature (similar to what exists in MITK Nvidia Plugin)</p>

---

## Post #14 by @lassoan (2019-07-18 15:34 UTC)

<aside class="quote no-group" data-username="SachidanandAlle" data-post="13" data-topic="7570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/4491bb/48.png" class="avatar"> SachidanandAlle:</div>
<blockquote>
<p>next step is to add Polygon Editing feature</p>
</blockquote>
</aside>
<p>Curve nodes are added in recent Slicer Preview Releases that should be used for this. These new curve nodes provide interactive editing, various interpolation schemes, out-of-plane display, etc. You can also look at other segment editor effects, such as <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorSurfaceCut">Surface cut</a> and <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/tree/master/SegmentEditorDrawTube">Draw tube</a> to see how you can preserve editable curve points in segment tags. If you need any further help then we can continue the discussion in the <a href="https://github.com/SachidanandAlle/Nvidia3DSlicerExtension">extension’s repository</a> (you can add issues for each item to discuss/develop).</p>
<aside class="quote no-group" data-username="bsmarine" data-post="11" data-topic="7570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bsmarine/48/3898_2.png" class="avatar"> bsmarine:</div>
<blockquote>
<p>Here’s <a href="https://docs.nvidia.com/clara/aiaa/tlt-mi-ai-an-sdk-getting-started/index.html">the latest documentation </a> for the AI-Assisted Server via NVIDIA’s Clara Train SDK.</p>
</blockquote>
</aside>
<p>This process is very involved and most potentially interested users cannot complete all the steps. Would it be possible to set up a test server that would allow people to try the extension?</p>

---

## Post #15 by @SachidanandAlle (2019-07-18 15:45 UTC)

<p>We (NVIDIA) would like to… even if it is slow… but still helps user to understand about the feature.<br>
We (as part of NVIDIA) need to clear few security checks to make it public… hence it’s delayed</p>

---

## Post #16 by @bsmarine (2019-07-19 13:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I spoke with one if my colleagues here and standing up an annotation server for development is something we can help with. May take a couple of days but will keep you posted. Will post both here and on repository with details.</p>
<p>Exciting turn around on this work!</p>

---

## Post #17 by @SachidanandAlle (2019-07-22 15:56 UTC)

<p>Thank you… I have been referring the same extensions to start with.<br>
One thing I couldn’t find: when user clicks label (selects label like Spleen) I would like to send a request to AIAA server and keep the list of models ready… instead of additional click to “Fetch Models”</p>
<p>Is there a way I can get an event that label is selected from the labelmap?</p>

---

## Post #18 by @lassoan (2019-07-22 17:07 UTC)

<p>If you mean that you would like to know when the user changes the segment name (or double-clicks the color swatch and selects a terminology item) then you can add an observer to the <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html#a1a387d4572ce52ab0c0babbecbd5a4daab7c453a4ebba0f7e2e92dbc6e36f761a" rel="nofollow noopener">SegmentModified</a> event in the segmentation node. Whenever this event is invoked your observer can retrieve the segment’s name or terminology and request the appropriate model.</p>

---

## Post #19 by @fedorov (2019-07-22 17:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I think the question is how to get the event when the segment is selected in the segment list.</p>
<p><a class="mention" href="/u/sachidanandalle">@SachidanandAlle</a> in the <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QuantitativeReporting.py" rel="nofollow noopener">QuantitativeReporting</a> module we had a similar situation where we wanted to configure actions based on segment selection. I might not remember it correctly, but I think Christian (<a class="mention" href="/u/che85">@che85</a>) who implemented that module didn’t find a  way to get that event, and because of that had to customize Segment Editor in <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QRCustomizations/CustomSegmentEditor.py#L65" rel="nofollow noopener">this class</a>. I would’t be able to list all the reasons why that customization was needed, beyond this event handler.</p>

---

## Post #20 by @lassoan (2019-07-25 04:12 UTC)

<p>To get a notification immediately when the user selects a different segment, you can use the <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a9172bd5ffebecf7f8f71da4faddc9ace" rel="nofollow noopener"><code>currentSegmentIDChanged</code> signal</a> of the segment editor widget. If you want to check anytime what is the currently selected segment, you can get it from the segment using <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a28f777b232a84844f9bf83ce6baea805" rel="nofollow noopener"><code>currentSegmentID</code> method</a> (or from the <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#ab61fe048ca56b7cc6f0d8ef1dda5e3b2" rel="nofollow noopener">segment editor MRML node</a>).</p>

---

## Post #21 by @lassoan (2019-12-19 21:08 UTC)

<p>Just in case somebody comes across this topic now: NVidia Clara AIAA extension is now available in extension manager.</p>
<aside class="quote quote-modified" data-post="1" data-topic="9536">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/ai-assisted-segmentation-extension/9536">AI-assisted segmentation extension</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    We are excited to announce that <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/README.md">Nvidia AI-assisted segmentation extension</a> is ready to use in latest Slicer Preview Release (rev28686 or later). The extension has been developed by Nvidia, with contributions from Slicer core developers. While there have been other AI-assisted segmentation modules in Slicer (such as <a href="http://www.deepinfer.org/">DeepInfer</a>, <a href="https://github.com/faustomilletari/TOMAAT-Slicer">TOMAAT</a>, <a href="https://chestimagingplatform.org/workstation-slicer-cip">SlicerCIP</a>), this newest addition uses <a href="https://developer.nvidia.com/clara">Nvidia Clara</a>, a toolkit with significant industrial support and sufficient openness for researchers. 
Few-minute overview video…
  </blockquote>
</aside>


---

## Post #22 by @Bruno_Aragao (2020-02-28 01:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/895b1f61277da679dd7df9a1a8b8c0cfb3ce3b39.jpeg" data-download-href="/uploads/short-url/jB6DQqpx7xSYKsPrtcE2NU4VAkp.jpeg?dl=1" title="nvidia server error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/895b1f61277da679dd7df9a1a8b8c0cfb3ce3b39_2_690x358.jpeg" alt="nvidia server error" data-base62-sha1="jB6DQqpx7xSYKsPrtcE2NU4VAkp" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/895b1f61277da679dd7df9a1a8b8c0cfb3ce3b39_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/895b1f61277da679dd7df9a1a8b8c0cfb3ce3b39_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/895b1f61277da679dd7df9a1a8b8c0cfb3ce3b39_2_1380x716.jpeg 2x" data-dominant-color="8C8C93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">nvidia server error</span><span class="informations">1902×989 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello,</p>
<p>Does anyone knows why this message appears ? Is there any server configuration to be made?</p>
<p>Thanks</p>

---

## Post #23 by @lassoan (2020-02-28 03:15 UTC)

<p>Sorry, it seems that the latest updates to the extension broke the network communication. It should be fixed by tomorrow but until then you can use this release: <a href="https://download.slicer.org/?date=2020-02-20">https://download.slicer.org/?date=2020-02-20</a></p>

---

## Post #24 by @pieper (2020-04-27 16:28 UTC)

<p>Has anyone tried using DeepGrow?  <a class="mention" href="/u/lassoan">@lassoan</a> I recall we talked that it was 2D only, but their documentation implies it’s 3D (<a class="mention" href="/u/erikziegler">@erikziegler</a> pointed this out).</p>
<p><a href="https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v3.0/aiaa/key_features.html#deepgrow" class="onebox" target="_blank">https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v3.0/aiaa/key_features.html#deepgrow</a></p>

---

## Post #25 by @lassoan (2020-04-27 16:39 UTC)

<p>Yes, at the time it was released it was 2D, maybe it is 3D now. However, it does not use any underlying organ model, so it seems to be just another variant of Grow from seeds/Watershed/etc.</p>
<p>Nevertheless, it would be still interesting to try. That would require setting up the latest version of the AIAA server. <a class="mention" href="/u/pieper">@pieper</a> if you have time to set it up then I can give you access to the server.</p>

---

## Post #26 by @nanderson (2020-11-09 04:19 UTC)

<p>Hi There I am also getting the error.<br>
“Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser”<br>
Using a Windows machine and the url field is blank as advised.<br>
Just downloaded the extension yesterday. How can I resolve?<br>
Thanks a lot</p>

---

## Post #27 by @lassoan (2020-11-09 05:21 UTC)

<p>The server is up and running and works well from Slicer, from a Windows machine (I’ve just tried it now). If you are behind a company or hospital firewall that prevents web requests to go through then you may need to specify the web access proxy as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_configure_network_proxy_.3F">here</a>.</p>

---

## Post #28 by @nanderson (2020-11-09 06:53 UTC)

<p>Are there any models for segmenting the Bronchi from the lungs?<br>
Thanks a lot</p>

---

## Post #29 by @lassoan (2020-11-09 22:12 UTC)

<p>I’ve updated the demo Slicer AI server to use latest NVidia Clara 3.0 version and uploaded the latest models (NVidia provides over 20 image segmentation models as technology demonstration - you can see the list here: <a href="https://ngc.nvidia.com/catalog/collections/nvidia:claratrainframework">https://ngc.nvidia.com/catalog/collections/nvidia:claratrainframework</a>). You may find the fully automatic lung segmentation model useful.</p>
<p>In addition to this, you may find models at other places that can be loaded into the AIAA server directly, or brought into AIAA compatible format (see <a href="https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v3.0/aiaa/byom.html">instructions for bringing your own model</a>).</p>

---

## Post #30 by @bsmarine (2020-11-13 19:16 UTC)

<p>Hi Andras,</p>
<p>Do you know if there are any open-source COVID lung lesion models currently available in Clara, or elsewhere? And are you still providing a server to host models for the general public via AIAA Slicer plug-in?</p>
<p>Hope you are well.</p>
<p>-Brett</p>

---

## Post #31 by @lassoan (2020-11-13 19:49 UTC)

<p>Yes, we still provide the server. We are in the process of switching to Clara 3.0, which has a few COVID related models, for example a fully automatic lung segmentation model. See complete list by clicking on “Download COVID-19 models” button on <a href="https://developer.nvidia.com/clara-medical-imaging">this</a> page.</p>

---

## Post #32 by @bsmarine (2020-11-14 20:14 UTC)

<p>This is great, thank you!</p>

---

## Post #33 by @strakpe (2021-04-14 05:30 UTC)

<p>Hello Andras,</p>
<p>I have just started to explore the possibilities of Clara and its extension to 3DSlicer. I am quite impressed with the concept and how it works together. My main focus of interest is liver segmentation. There are two liver segmentation models provided by Nvidia and also a general 2D Deepgrow method. Unfortunately, I could not find any annotation model for liver which would make the liver segmentation much faster compared to 2D Deepgrow. I saw the annotation models in some older Clara videos by Nvidia but actual NGC catalog does not offer them anymore. Is there any place where I could download them? Or maybe, do you have any recommendations how to create them from the existing segmentation models?</p>
<p>Thank you,</p>
<p>Petr</p>

---

## Post #34 by @lassoan (2021-04-16 03:39 UTC)

<aside class="quote no-group" data-username="strakpe" data-post="33" data-topic="7570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c68b51/48.png" class="avatar"> strakpe:</div>
<blockquote>
<p>r segmentation models provided by Nvidia and also a general 2D Deepgrow method. Unfortunately, I could not find any annotation model for liver which would make the liver segmentation much faster compared to 2D Deepgrow. I saw the annotation models in some older Clara videos by Nvidia but actual NGC catalog</p>
</blockquote>
</aside>
<p>NVidia developed these models as technology demos, but has no intention of maintaining them. Instead, they provide funding to the <a href="https://monai.io/">monai</a> community to create and maintain models that can be used in Clara. I would recommend to check out monai, see what models they have, and maybe ask on their <a href="https://github.com/Project-MONAI/MONAI/discussions">discussion forum</a> about what they recommend for liver segmentation.</p>

---

## Post #35 by @lassoan (2021-06-07 04:12 UTC)

<p>A post was split to a new topic: <a href="/t/nvidia-aiaa-server-internal-error/17988">NVIDIA AIAA server internal error</a></p>

---

## Post #36 by @namnh (2023-08-08 14:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf68f82cbf1d73633315b453a2145ff68c8cde20.jpeg" data-download-href="/uploads/short-url/rji5KPzXszlD2I1AIBsBB9y6y08.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf68f82cbf1d73633315b453a2145ff68c8cde20_2_690x358.jpeg" alt="image" data-base62-sha1="rji5KPzXszlD2I1AIBsBB9y6y08" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf68f82cbf1d73633315b453a2145ff68c8cde20_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf68f82cbf1d73633315b453a2145ff68c8cde20_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf68f82cbf1d73633315b453a2145ff68c8cde20_2_1380x716.jpeg 2x" data-dominant-color="8C8C93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×989 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is Nvidia clara aaa support anymore</p>

---

## Post #37 by @lassoan (2023-08-08 14:58 UTC)

<p>We don’t provide a publicly usable NVIDIA-AIAA server anymore. You can set up and use your own server (or can run on any Linux computer that supports docker and has an NVIDIA GPU with at least about 8GB GPU RAM).</p>
<p>However, since its developers do not support NVIDIA-AIAA anymore, I would recommend to use MONAILabel instead.</p>

---
