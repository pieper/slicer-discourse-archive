---
topic_id: 9536
title: "Ai Assisted Segmentation Extension"
date: 2019-12-17
url: https://discourse.slicer.org/t/9536
---

# AI-assisted segmentation extension

**Topic ID**: 9536
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/ai-assisted-segmentation-extension/9536

---

## Post #1 by @lassoan (2019-12-17 21:03 UTC)

<blockquote>
<p><strong>Important note: NVIDIA-AIAA extension is still available, but it is not supported and not recommended anymore. It is no longer necessary to set up a server for segmentation and not necessary to even have a GPU. Instead, there are several new extensions that allow segmenting images much more easily. For example, TotalSegmentator and MONAIAuto3DSeg extensions.</strong></p>
</blockquote>
<p>We are excited to announce that <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/README.md">Nvidia AI-assisted segmentation extension</a> is ready to use in latest Slicer Preview Release (rev28686 or later). The extension has been developed by Nvidia, with contributions from Slicer core developers. While there have been other AI-assisted segmentation modules in Slicer (such as <a href="http://www.deepinfer.org/">DeepInfer</a>, <a href="https://github.com/faustomilletari/TOMAAT-Slicer">TOMAAT</a>, <a href="https://chestimagingplatform.org/workstation-slicer-cip">SlicerCIP</a>), this newest addition uses <a href="https://developer.nvidia.com/clara">Nvidia Clara</a>, a toolkit with significant industrial support and sufficient openness for researchers.</p>
<p>Few-minute overview video, showing guided MRI brain tumor and liver segmentation, and fully automatic liver, tumor, and spleen segmentation:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ucnvE16pkmI" data-video-title="AI-assisted segmentation using free tools - 3D Slicer and Nvidia Clara" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ucnvE16pkmI" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ucnvE16pkmI/maxresdefault.jpg" title="AI-assisted segmentation using free tools - 3D Slicer and Nvidia Clara" width="" height="">
  </a>
</div>

<p>Tutorial and detailed description: see <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/README.md">Nvidia AIAA extension documentation</a>.</p>
<p><strong>How does it work?</strong> The input image (and input points - in case of guided segmentation) are sent to a computer equipped with an Nvidia GPU, running Linux operating system and <a href="https://docs.nvidia.com/clara/aiaa/tlt-mi-ai-an-sdk-getting-started/">Nvidia Clara software</a>. The server computes segmentation using the selected AI model and sends back the results to Slicer for display and further processing.</p>
<p><strong>We have set up a demonstration server at the PerkLab</strong> (Queen’s University in Canada) to make it easier for Slicer users to get started without setting up their own processing computer. We uploaded a couple of AI models that Nvidia developed. We provide these models and the processing service as is, we don’t guarantee quality of this service (validity of segmentation results, speed, server uptime, etc.). No patient information is sent to the processing server and images and results are deleted from the server after processing, but users need to make sure they comply with their data management guidelines when using our server. If there are any confidentiality concerns then publicly available images may be used for testing: see Slicer’s Sample Data module or <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/TCIABrowser">TCIA Browser</a> extension, or download from other websites, such as <a href="http://medicaldecathlon.com/">Medical Decathlon</a>.</p>
<p><strong>If anyone would like to share their AI models for segmentation</strong>, let us know. As long as the model is compatible with Nvidia Clara, we should be able to install it on our server and make it available to the Slicer community.</p>
<p>Any questions and suggestions are welcome!</p>

---

## Post #2 by @muratmaga (2019-12-17 21:24 UTC)

<p>This looks great. I assume the existing trained models are for human clinical scans?<br>
Is it possible to add/train additional reference segmentation (e.g, mouse skulls?, embryos etc)</p>

---

## Post #3 by @lassoan (2019-12-17 21:32 UTC)

<p>All NVidia models are based on human clinical data sets (you can find more information <a href="https://docs.nvidia.com/clara/aiaa/tlt-mi-ai-an-sdk-getting-started/">here</a>). However, the methods are completely generic and you should be able to use <a href="https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v2.0/index.html">Clara Train</a> to build models from your data.</p>

---

## Post #4 by @manjula (2019-12-17 21:55 UTC)

<p>This is indeed great news !!! <img src="https://emoji.discourse-cdn.com/twitter/partying_face.png?v=9" title=":partying_face:" class="emoji" alt=":partying_face:"></p>
<p>However only segmentation spleen and segmentation liver and tumor is shown in mine.</p>

---

## Post #5 by @lassoan (2019-12-17 22:15 UTC)

<p>I’ve only installed liver+tumor and spleen models for fully automatic segmentation (others were listed to have rather low scores or just did not seem that interesting).</p>
<p>There are about 10 more models for boundary points based segmentation.</p>
<p>If you want us to install any other models listed <a href="https://docs.nvidia.com/clara/aiaa/tlt-mi-ai-an-sdk-getting-started/">here</a> then let me know.</p>

---

## Post #6 by @manjula (2019-12-17 22:38 UTC)

<p>Dear Prof  Lassoan,<br>
Well these AI trained modules at NVIDIA are not relevant to me  i looked at that out of interest and i thought it was due to something wrong with the linux version as i downloaded the new build moments ago. I would have loved to experiment with the training on oral cancer but unfortunately reuqired specs are out of my reach.</p>
<p>Hardware Requirements</p>
<p><strong>Recommended</strong></p>
<ul>
<li>1 GPU or more</li>
<li>16 GB GPU memory</li>
<li>8 core CPU</li>
<li>32 GB system RAM</li>
<li>80 GB free disk space</li>
</ul>

---

## Post #7 by @jdx-john (2019-12-17 23:15 UTC)

<p>This sounds really cool. <a class="mention" href="/u/lassoan">@lassoan</a> I wondered if you recall our CT cardio project… Any ideas if this might work for automatic segmentation of heart datasets like we were dealing with?</p>
<p>John</p>

---

## Post #8 by @keesh (2019-12-17 23:30 UTC)

<p>The automatic liver/spleen segmentation was impressive.  NVidia has come a long way fast since the manual point and click approach.  I plan to compare their approach to a Caffe 2D UNet paradigm.  My only concern is the low input resolution (128 x 128 x 128) required.</p>

---

## Post #9 by @JanWitowski (2019-12-18 06:35 UTC)

<p>Andras,<br>
this is amazing news. Thinking that we might have a true one-click segmentation very soon is so exciting.</p>
<p>I tested this extension, specifically liver segmentation models, on my local datasets and wanted to share some thoughts:</p>
<ol>
<li>Liver segmentation from boundary points works flawlessly. It is by far more accurate and faster than any other approach available in Slicer (grow from seeds, marching…). In most cases it doesn’t require any postprocessing. For people like me, who work with liver parenchyma segmentation regularly, this is another major upgrade.</li>
<li>Automatic liver and tumor segmentation has some accuracy issues, though. It looks like model is a little overfitted on Medical Decathlon dataset. I tested a few examples from that set and it did pretty accurate segmentation. On my local dataset it had a lot of trouble and is not functional at the moment (though it has some strong moments and can detect small lesions). Also, it’s too time-consuming for the effects you’re getting. A few examples:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b349980dc08a7f48419963f104851cf079bfffb4.jpeg" data-download-href="/uploads/short-url/pA38M5spdPBePPvUuNeHL3x06nq.jpeg?dl=1" title="clara-01.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b349980dc08a7f48419963f104851cf079bfffb4_2_690x333.jpeg" alt="clara-01.PNG" data-base62-sha1="pA38M5spdPBePPvUuNeHL3x06nq" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b349980dc08a7f48419963f104851cf079bfffb4_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b349980dc08a7f48419963f104851cf079bfffb4_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b349980dc08a7f48419963f104851cf079bfffb4_2_1380x666.jpeg 2x" data-dominant-color="73757D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clara-01.PNG</span><span class="informations">2531×1224 551 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db029dda8f2a60f0ff0d93c1bf51611bd61c17da.jpeg" data-download-href="/uploads/short-url/vfsaFyTf7QLiixhNEIJlzgb5Y8O.jpeg?dl=1" title="clara-02.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db029dda8f2a60f0ff0d93c1bf51611bd61c17da_2_690x345.jpeg" alt="clara-02.PNG" data-base62-sha1="vfsaFyTf7QLiixhNEIJlzgb5Y8O" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db029dda8f2a60f0ff0d93c1bf51611bd61c17da_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db029dda8f2a60f0ff0d93c1bf51611bd61c17da_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db029dda8f2a60f0ff0d93c1bf51611bd61c17da_2_1380x690.jpeg 2x" data-dominant-color="777780"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clara-02.PNG</span><span class="informations">2553×1280 599 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10efe69ae3aafd74d1404dc3e0b668866b55e4fc.jpeg" data-download-href="/uploads/short-url/2pPCJ34JJFmf0gFmCT65U3mCzWk.jpeg?dl=1" title="clara-03.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10efe69ae3aafd74d1404dc3e0b668866b55e4fc_2_690x347.jpeg" alt="clara-03.PNG" data-base62-sha1="2pPCJ34JJFmf0gFmCT65U3mCzWk" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10efe69ae3aafd74d1404dc3e0b668866b55e4fc_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10efe69ae3aafd74d1404dc3e0b668866b55e4fc_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10efe69ae3aafd74d1404dc3e0b668866b55e4fc_2_1380x694.jpeg 2x" data-dominant-color="82848C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clara-03.PNG</span><span class="informations">2542×1279 600 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
I will look at the Clara closer ASAP and try to figure out how to contribute models.</li>
</ol>

---

## Post #10 by @brhoom (2019-12-18 07:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Great news, I just downloaded Slicer 4.11.0 for windows but this extension does not appear in the extension manager. Another question, do you know if there is an automatic spine segmentation available?</p>
<aside class="quote no-group" data-username="JanWitowski" data-post="9" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p>It looks like model is a little overfitted on Medical Decathlon dataset</p>
</blockquote>
</aside>
<p>I think it is possible to fine-tune the models with new datasets. It would be nice if this is available in the slicer module.</p>

---

## Post #11 by @NoobForSlicer (2019-12-18 10:18 UTC)

<p>I have a question… Can this thing be used to segment whatever organ we want or just the ones they prepared the models of segmentation for?</p>

---

## Post #12 by @lassoan (2019-12-18 14:01 UTC)

<aside class="quote no-group" data-username="JanWitowski" data-post="9" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p>Liver segmentation from boundary points works flawlessly. It is by far more accurate and faster than any other approach available in Slicer (grow from seeds, marching…). In most cases it doesn’t require any postprocessing. For people like me, who work with liver parenchyma segmentation regularly, this is another major upgrade.</p>
</blockquote>
</aside>
<p>Thanks for the feedback. It’s great to hear that you find the extension useful.</p>
<aside class="quote no-group" data-username="JanWitowski" data-post="9" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p>Automatic liver and tumor segmentation has some accuracy issues, though</p>
</blockquote>
</aside>
<p>I think so, too. If the volume has different size or resolution then the model gets confused. The models are pretty good overall, considering that Nvidia provides these models as technology demonstrations, but if you spend some time with training, especially with your own data sets then you can expect much better results.</p>
<aside class="quote no-group" data-username="JanWitowski" data-post="9" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p>I will look at the Clara closer ASAP and try to figure out how to contribute models.</p>
</blockquote>
</aside>
<p>Awesome. If you can create models and willing to share them then we would be happy to upload them to our segmentation server.</p>
<aside class="quote no-group" data-username="brhoom" data-post="10" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Great news, I just downloaded Slicer 4.11.0 for windows but this extension does not appear in the extension manager.</p>
</blockquote>
</aside>
<p>There is a few-hour timeslot each day when the new nightly Slicer installer is already available but not all extensions are built yet. You either need to wait a few hours or download the preview release from the day before using this link: <a href="https://download.slicer.org/?offset=-1" class="inline-onebox">Download 3D Slicer | 3D Slicer</a></p>
<aside class="quote no-group" data-username="brhoom" data-post="10" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>I think it is possible to fine-tune the models with new datasets.</p>
</blockquote>
</aside>
<p>Yes, it is. It is not as easy as running a pre-trained model, so I’m not sure we can create a simple GUI for this in Slicer, but you can follow these <a href="https://docs.nvidia.com/clara/tlt-mi/tlt-mi-getting-started/">instructions</a>.</p>
<aside class="quote no-group" data-username="manjula" data-post="6" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>unfortunately reuqired specs are out of my reach.</p>
</blockquote>
</aside>
<p>These specs are just recommendations and only relevant for training (for inference, any hardware with a CUDA-capable GPU will do). For training, you should be fine with 8GB GPU memory and 16GB RAM but probably even half of that is enough for many applications.</p>
<aside class="quote no-group" data-username="NoobForSlicer" data-post="11" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>Can this thing be used to segment whatever organ we want or just the ones they prepared the models of segmentation for?</p>
</blockquote>
</aside>
<p>Each model can segment what it is trained for. You can fine-tune pre-trained models or train new models from scratch if you have enough data sets (for simple problems you might not need that much data and training parameter tuning) by following these <a href="https://docs.nvidia.com/clara/tlt-mi/tlt-mi-getting-started/">instructions</a> or creating a any model and bringing it into <a href="https://docs.nvidia.com/clara/tlt-mi/tlt-mi-getting-started/#medical_model_archive">MMAR format</a>.</p>
<aside class="quote no-group" data-username="jdx-john" data-post="7" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a6a055/48.png" class="avatar"> jdx-john:</div>
<blockquote>
<p>This sounds really cool. <a class="mention" href="/u/lassoan">@lassoan</a> I wondered if you recall our CT cardio project… Any ideas if this might work for automatic segmentation of heart datasets like we were dealing with?</p>
</blockquote>
</aside>
<p>The training framework is quite generic and heart segmentation on contrasted CT is fundamentally not very hard, so training a model should be feasible if you have enough data sets. There could be some special considerations to handle large 4D periodic data sets.</p>

---

## Post #13 by @e36alpine (2019-12-18 17:06 UTC)

<p>Very excited about these modules , however I must be doing something wrong.  I keep getting an error when I try to fetch models. It says "Failed to fetch models from server.  Make sure address is correct and retry. Not sure if my work PC is blocking me from accessing that server?  I have 0.0.0.0 for the server address.<br>
Details:<br>
Traceback (most recent call last):<br>
File “C:/Users/en12283/AppData/Roaming/NA-MIC/Extensions-28690/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 164, in onClickFetchModels<br>
models = self.logic.list_models(self.ui.modelFilterLabelLineEdit.text)<br>
File “C:/Users/en12283/AppData/Roaming/NA-MIC/Extensions-28690/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 692, in list_models<br>
result = self.aiaaClient.model_list(label)<br>
File “C:\Users\en12283\AppData\Roaming\NA-MIC\Extensions-28690\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 107, in model_list<br>
response = AIAAUtils.http_get_method(self.server_url, selector)<br>
File “C:\Users\en12283\AppData\Roaming\NA-MIC\Extensions-28690\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 402, in http_get_method<br>
conn = httplib.HTTPConnection(parsed.hostname, parsed.port)<br>
File “C:\Users\en12283\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-17\lib\Python\Lib\http\client.py”, line 849, in <strong>init</strong><br>
(self.host, self.port) = self._get_hostport(host, port)<br>
File “C:\Users\en12283\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-17\lib\Python\Lib\http\client.py”, line 881, in _get_hostport<br>
i = host.rfind(’:’)<br>
AttributeError: ‘NoneType’ object has no attribute ‘rfind’</p>
<p>I just did a Pancreatic tumor case and would love to see if the auto segment gets it close.  Thanks!</p>

---

## Post #15 by @JanWitowski (2019-12-18 17:15 UTC)

<p>Are you running a local server? If you’re trying to access publicly available models hosted by PerkLab, leave the “NVidia AIAA server” field empty.</p>

---

## Post #16 by @e36alpine (2019-12-19 14:05 UTC)

<p>I thought it was blank yesterday. I have no idea what I did different today but now it’s working!!  Sorry for wasting your time!  Thanks,Greg</p>

---

## Post #17 by @manjula (2019-12-19 19:34 UTC)

<p>Is it possible to train this to segment a area of bone defect (e.g Alveolar Cleft ) by  looking at predefine set of standard landmarks ?</p>
<p>I am Zero in AI.</p>
<p>Can someone be able to do a small tutorial on how to train to segment out a structure ?</p>

---

## Post #18 by @lassoan (2019-12-19 20:38 UTC)

<p>The extension allows users to run trained AI models. Creating models is a non-trivial task, but usually it is not too hard, if you already have large training data set (hundreds of manually segmented cases). You can search specifically for “nvidia clara train tutorial” (or look for any deep learning image segmentation tutorial on the web and then set up Clara interface to it).</p>

---

## Post #19 by @manjula (2019-12-19 20:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>oo hard, if you already have la</p>
</blockquote>
</aside>
<p>i do have access to large sets of CT and CBCT of data of head and neck region. But how much of manual segmentation will be needed for e.g</p>
<ol>
<li>to train on oral cancer detection in the Maxilla or Mandible ?  (we get like 150-200 oral cancers per year)<br>
or</li>
<li>more simple segmentation  like inferior alveolar nerve ? (big numbers of data)</li>
</ol>
<p>Also is there a way to compensate for conditions with lack of data ? for example in cleft lip and palate we don’t get patients in number of hundreds… what we have is like 20 new patients per year. So in those cases is it possible to train ?</p>

---

## Post #20 by @lassoan (2019-12-19 21:15 UTC)

<p>For training models for segmentation, you need to have manually segmentations as input (it is not enough to have just the CT volume). The more data the better, but a few hundred should be enough. If you only have a few ten cases, it may be feasible, too, but it makes the training more difficult (you may need to tune network structure and learning parameters more carefully, do more sophisticated data augmentation, etc.).</p>

---

## Post #21 by @manjula (2019-12-19 21:21 UTC)

<p>Thank you. I will try with simple inferior alveolar nerve training… i think i should be able to segment about 200 alveolar nerves and try this as a experiment.</p>
<p>Is the segmenting is the  usual process with Segment editor ?<br>
What format i need to save the segments/data in ?</p>
<p>Once i segment out 200 alveolar nerves i will try to set the clara interface to it.</p>

---

## Post #22 by @JanWitowski (2019-12-19 21:38 UTC)

<p>Before you start segmentation please take a look at tutorials / user guides. If you decide to use Nvidia Clara you can find more information e.g. here: <a href="https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v1.1/index.html" rel="noopener nofollow ugc">https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v1.1/index.html</a> In short: it depends on your approach.</p>
<p>Also, think about the structure that you want to segment. You might want to start with a larger structure than inferior alveolar nerve – small structures tend to be more difficult to understand by AI models.</p>
<blockquote>
<p>Is the segmenting is the usual process with Segment editor ?</p>
</blockquote>
<p>Yes, the process of creating the “ground truth” segmentation can be done completely with Slicer tools. Usually, you’ll want to export your segmentation masks into binary label maps (through the Segmentations module).</p>

---

## Post #23 by @manjula (2019-12-19 21:40 UTC)

<p>Thanks much appreciated. Will experiment with this.</p>

---

## Post #24 by @lzq3315 (2020-01-04 06:41 UTC)

<p>Hi ! I want to make segment for ovarion tumor but I can not find the suitable model . Could you set up one model for ovarian tumor please? Thank you very much!</p>

---

## Post #25 by @lassoan (2020-01-04 17:33 UTC)

<p>You can try other models (such as those developed for brain tumors). If they don’t work then you probably need to train your own model (see <a href="https://discourse.slicer.org/t/ai-assisted-segmentation-extension/9536/20">reply above</a>).</p>

---

## Post #26 by @tbuikr (2020-01-20 03:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>: Thank your team and NVIDIA to provide an interesting project.</p>
<p>Currently, we are working on object detection (i.e. tumor detection…) using faster-rcnn and plan to incorporate it into 3D Slicer and Nvidia Clara. This task is a new task and does not include in the current version of Nvidia Clara. I hope we can contribute it. However, I am newbie of Slicer and I would like to ask  you some questions:</p>
<p>My pipeline is : Load a json file --&gt; Draw a rectangular bounding box (4 points) --&gt; Modify the location of these points --&gt; Overwrite to the json file (Pascal VOC format)</p>
<p>Could you please suggest some tutorial to implement the pipeline in the Slicer with python extension? For write json file, I found a tutorial at <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Write_annotation_ROI_to_JSON_file" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Write_annotation_ROI_to_JSON_file</a></p>

---

## Post #27 by @lassoan (2020-01-20 09:39 UTC)

<p>Since NVidiaAIAA segment editor effect has already implemented the Clara API, I would recommend to start with modifying that effect in your own fork.</p>
<aside class="quote no-group" data-username="tbuikr" data-post="26" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbuikr/48/3899_2.png" class="avatar"> tbuikr:</div>
<blockquote>
<p>Draw a rectangular bounding box (4 points)</p>
</blockquote>
</aside>
<p>Probably the easiest is to use 4 markup fiducial points for this. Marking points is already implemented in the AIAA effect, you can connect them using a line as it is done in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCut.py">SurfaceCut</a> effect.</p>
<aside class="quote no-group" data-username="tbuikr" data-post="26" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbuikr/48/3899_2.png" class="avatar"> tbuikr:</div>
<blockquote>
<p>Load a json file</p>
</blockquote>
</aside>
<p>Save/load json file is very easy in Python. Let us know if you have any specific questions.</p>

---

## Post #28 by @caioath (2020-01-31 18:19 UTC)

<p>Thank you Prof Lasso and team for this extension. I’ve just trained a model with good results and I was able to deploy it right away in Slicer.<br>
I would like to complete a script to perform the autosegmentation on some datasets using this model (<a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">Extract skin</a>) with nvidia aiaa extension.<br>
I looked for the setMRMLDefault to find out the parameters, but I’m missing something. Also I miss the input for the AIAA server URL.</p>
<p>I appreciate any help. Thanks again</p>
<p>Caio</p>
<pre><code># NVIDIA auto segmentation
</code></pre>
<p>segmentEditorWidget.setActiveEffectByName(“NvidiaAIAA”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“SegmentationModel”, “my_model”)<br>
effect.self().onApply()</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘NoneType’ object has no attribute ‘setParameter’</p>

---

## Post #29 by @lassoan (2020-01-31 18:48 UTC)

<aside class="quote no-group" data-username="caioath" data-post="28" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caioath/48/9688_2.png" class="avatar"> caioath:</div>
<blockquote>
<p>Thank you Prof Lasso and team for this extension. I’ve just trained a model with good results and I was able to deploy it right away in Slicer.</p>
</blockquote>
</aside>
<p>Great!</p>
<aside class="quote no-group" data-username="caioath" data-post="28" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caioath/48/9688_2.png" class="avatar"> caioath:</div>
<blockquote>
<p>I would like to complete a script to perform the autosegmentation on some datasets using this model (<a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9">Extract skin </a>) with nvidia aiaa extension</p>
</blockquote>
</aside>
<p>Would you like to run extract skin example on an NVidia AIAA server?</p>
<aside class="quote no-group" data-username="caioath" data-post="28" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caioath/48/9688_2.png" class="avatar"> caioath:</div>
<blockquote>
<p>I looked for the setMRMLDefault to find out the parameters, but I’m missing something.</p>
</blockquote>
</aside>
<p>What parameters of what effect you are trying to find parameters of?</p>
<aside class="quote no-group" data-username="caioath" data-post="28" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caioath/48/9688_2.png" class="avatar"> caioath:</div>
<blockquote>
<p>I miss the input for the AIAA server URL</p>
</blockquote>
</aside>
<p>To use the default Slicer AIAA server, leave the URL field empty.</p>

---

## Post #30 by @caioath (2020-01-31 19:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="29" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you like to run extract skin example on an NVidia AIAA server?</p>
</blockquote>
</aside>
<p>I would like to run the autosegmentation by script (loading volumes, creating segmentations and using the nvidia aiaa-slicer extension by code). I used extract skin example to get the code for creating segmentation etc. I’m running a local AIAA server here with my model.<br>
Everything is working fine with my server and model, but I would like to skip the clicking parts of it executing a script.</p>
<aside class="quote no-group" data-username="lassoan" data-post="29" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What parameters of what effect you are trying to find parameters of?</p>
</blockquote>
</aside>
<p>Parameters of NVIDIA AIAA extension</p>
<aside class="quote no-group" data-username="caioath" data-post="28" data-topic="9536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caioath/48/9688_2.png" class="avatar"> caioath:</div>
<blockquote>
<p>segmentEditorWidget.setActiveEffectByName(“NvidiaAIAA”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“SegmentationModel”, “my_model”)<br>
effect.self().onApply()</p>
</blockquote>
</aside>

---

## Post #31 by @lassoan (2020-02-02 01:01 UTC)

<p>I’ve added an example for boundary points based AI segmentation in batch mode (without GUI):</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" target="_blank">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" target="_blank">https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5</a></h4>
<h5>NvidiaAiaaTumorSegmentation.py</h5>
<pre><code class="Python"># Load/generate input data
################################################

# Load master volume
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Define boundary points
import numpy as np</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" target="_blank">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #32 by @caioath (2020-02-02 13:50 UTC)

<p>Thanks so much. I’m learning coding as I go, and I was able to complete the script for the segmentation based on yours.</p>
<p>Auto segmentation<br>
segmentEditorWidget.setActiveEffectByName(“Nvidia AIAA”)<br>
effect = segmentEditorWidget.activeEffect()<br>
serverUrl = “http://AIAA_SERVER_ADDRESS:PORT/v1/models”<br>
effect.self().ui.serverComboBox.currentText = serverUrl<br>
effect.self().onClickFetchModels()<br>
aiaaModelName = “MY_MODEL”<br>
effect.self().ui.segmentationModelSelector.currentText = aiaaModelName<br>
effect.self().onClickSegmentation()</p>

---

## Post #33 by @Dunstan (2020-06-27 15:34 UTC)

<p>Hi, I’m also trying to automatically segment ovarian masses.<br>
I have a collection of over 200 manually segmented tumor lesions of both ovaries, several of them are bilateral and partly merged. How can I train my own model using this approach? Is there any tutorial available? Many thanks for your help!</p>

---

## Post #34 by @lassoan (2020-06-27 15:49 UTC)

<p>There are lots of deep learning tutorials online.</p>
<p>You can follow any keras or pytorch tutorial and feed your segmentations into them. Most likely it will not immediately work, but if the segmentation problem is not too hard then by tuning network layers, learning parameters, data preprocessing, you will eventually get to something usable.</p>
<p>If you want to have a model that runs directly in NVidia AIAA server then you can try to train a model using NVidia Clara. It is a higher-level library, which implements some commonly needed features and hides some of the low-level details, which may save you time, but also make the learning a bit harder (it may be a bit less clear what exactly happens internally).</p>

---

## Post #35 by @Fernando (2020-06-28 10:21 UTC)

<p>Hi <a class="mention" href="/u/dunstan">@Dunstan</a></p>
<p><a href="https://colab.research.google.com/drive/112NTL8uJXzcMw4PQbUvMQN-WHlVwQS3i?usp=sharing" rel="nofollow noopener">Here’s a tutorial</a> you can follow. It uses <a href="https://pytorch.org/" rel="nofollow noopener">PyTorch</a> and <a href="https://torchio.readthedocs.io/" rel="nofollow noopener">TorchIO</a> to train a 3D U-Net for segmentation. There will be a TorchIO extension available in Slicer soon. I hope this helps.</p>

---

## Post #36 by @ssyip (2020-07-07 22:43 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - We tested the AI organ segmentation extension on a bunch of public data. The extension worked very well. Awesome. However, as our research group would like to also analyze hospital / patient data, we do not feel comfortable sending our input image (even the deidentified ones) to “an external” server. Therefore, my question is “Is there any way to run the AI organ segmentation using our own hardware (e.g. GPU) w/o sending our data to an different server?” Thank you!</p>

---

## Post #37 by @lassoan (2020-07-08 12:40 UTC)

<p>You can set up your own server by following instructions on <a href="https://docs.nvidia.com/clara/tlt-mi/clara-train-sdk-v3.0/index.html">NVidia Clara website</a>.</p>

---

## Post #38 by @gpillajo (2020-08-20 00:24 UTC)

<p>Dear Prof Lasso:<br>
I have tried nvidia AIAA module in 3d slicer, there are my results:</p>
<ol>
<li>DExtr3D works fine.</li>
<li>Auto-segmentation does not work:<br>
Traceback (most recent call last):<br>
File “C:/Users/Expert Pro R2/AppData/Roaming/NA-MIC/Extensions-29276/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 361, in createAiaaSessionIfNotExists<br>
in_file, session_id = self.logic.createSession(inputVolume)<br>
File “C:/Users/Expert Pro R2/AppData/Roaming/NA-MIC/Extensions-29276/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 999, in createSession<br>
response = aiaaClient.create_session(in_file)<br>
File “C:\Users\Expert Pro R2\AppData\Roaming\NA-MIC\Extensions-29276\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 107, in create_session<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, response))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 404; Response: b’\n404 Not Found\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n’’)</li>
</ol>
<p>What would be the solution for this?<br>
Kind regards</p>

---

## Post #39 by @lassoan (2020-08-20 02:26 UTC)

<p>Please report this to NVidia engineers at <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues">https://github.com/NVIDIA/ai-assisted-annotation-client/issues</a>. Maybe we would just need to upgrade the default Slicer server (<a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/62">https://github.com/NVIDIA/ai-assisted-annotation-client/issues/62</a>).</p>

---

## Post #40 by @Rodrigo_Visconti (2020-08-22 16:19 UTC)

<p>There’s a way to incorporate US into the AI assisted segmentation module?</p>

---

## Post #41 by @ungi (2020-08-22 16:53 UTC)

<p>Ultrasound is very different from CT and MRI. There is code for training and deploying ultrasound segmentation in this repository: <a href="https://github.com/SlicerIGT/aigt" rel="nofollow noopener">https://github.com/SlicerIGT/aigt</a><br>
This repository is not very organized, but if you tell me more what you need to do, I can point you to more specific examples.</p>

---

## Post #42 by @epearlstone (2020-08-28 15:43 UTC)

<p>Is there a python script to run Boundary-point based segmentation?</p>

---

## Post #43 by @lassoan (2020-09-02 15:21 UTC)

<p>See example of running NVidia AI segmentation from Python script here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #44 by @epearlstone (2020-09-02 19:31 UTC)

<p>Thank you for your response. I’ve run through these examples but was hoping to find a script specific to Nvidia’s AI-assisted Boundary-points based segmentation mode. Something similar to the example you provided for doing brain tumor segmentation using Nvidia <a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" rel="nofollow noopener">here</a>. If you are aware of any other communities/sources I could use to search for something like this that would be a huge help.</p>

---

## Post #45 by @lassoan (2020-09-03 17:54 UTC)

<p>If you have a look at the source code of the AIAA module then is should not be too hard to figure out how to change the current example.</p>

---

## Post #46 by @epearlstone (2020-09-03 18:58 UTC)

<p>Where could I find the source code you are referring to? Do you mean the brain tumor segmentation code I linked to above or do you mean code that exists within the extension folder for Nvidia?<br>
I am also having trouble running the script you’ve given for brain tumor segmentation. I am running the script from the python console within Slicer and am getting the following error: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d8a8f827da1078e0ceb8d59c9aab5d07bff027d.jpeg" data-download-href="/uploads/short-url/fD2Um3jDI8TVrtBdDCVCkA11tmJ.jpeg?dl=1" title="Screen Shot 2020-09-03 at 2.53.14 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d8a8f827da1078e0ceb8d59c9aab5d07bff027d_2_690x406.jpeg" alt="Screen Shot 2020-09-03 at 2.53.14 PM" data-base62-sha1="fD2Um3jDI8TVrtBdDCVCkA11tmJ" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d8a8f827da1078e0ceb8d59c9aab5d07bff027d_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d8a8f827da1078e0ceb8d59c9aab5d07bff027d_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d8a8f827da1078e0ceb8d59c9aab5d07bff027d_2_1380x812.jpeg 2x" data-dominant-color="C5C4C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-09-03 at 2.53.14 PM</span><span class="informations">2878×1696 546 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The rest of the error message contains the following:</p>
<pre><code>Traceback (most recent call last):
File "/Applications/Slicer.app/Contents/Extensions-29345/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 472, in onClickAnnotation
result_file = self.logic.dextr3d(in_file, session_id, model, pointSet)
File "/Applications/Slicer.app/Contents/Extensions-29345/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 1053, in dextr3d
session_id=session_id)
File "/Applications/Slicer.app/Contents/Extensions-29345/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py", line 265, in dextr3d
points, crop = AIAAUtils.image_pre_process(image_in, cropped_file, point_set, pad, roi_size)
File "/Applications/Slicer.app/Contents/Extensions-29345/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py", line 558, in image_pre_process
points[::, 0] = points[::, 0] - x1
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
</code></pre>
<p>I am running the most updated version of Slicer 4.11 on a MacOS Mojave</p>

---

## Post #47 by @lassoan (2020-09-03 19:10 UTC)

<p>I mean that you can read the <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/NvidiaAIAA/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py">AIAA effect’s source code</a> and update the <a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5">AIAA example script</a> accordingly.</p>
<p>If you find any errors in NVidia AIAA segmentation then please report to <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues">https://github.com/NVIDIA/ai-assisted-annotation-client/issues</a>.</p>

---

## Post #48 by @sndkf (2020-09-04 01:35 UTC)

<p>Hello,</p>
<p>I am interested in this 3D Slicer extension for academic purposes (non-commercial), and I was wondering how you would like it to be cited/referenced?</p>
<p>Regards</p>

---

## Post #49 by @lassoan (2020-09-04 02:15 UTC)

<p>You can cite 3D Slicer as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#d-slicer-as-a-platform">here</a> and in addition to that you can refer to NVidia Clara by <a href="https://developer.nvidia.com/clara">this link</a>.</p>

---

## Post #50 by @PaoloZaffino (2020-09-14 07:18 UTC)

<p>Hi all,<br>
I was wondering if there is a list of ready to use servers/services for different applications.<br>
Something like:</p>
<ul>
<li>server 123.456.678 -&gt; CT segmentation</li>
<li>server test.test -&gt; prostate MR segmentation<br>
…<br>
…</li>
</ul>
<p>Thanks a lot.<br>
Paolo</p>

---

## Post #51 by @lassoan (2020-09-14 13:11 UTC)

<p>There is only one publicly available server (the default server - when you don’t specify any server address). It would be great if others would set up various servers, too, but there is not much incentive for anyone to do so. If grant funding agencies or journals started to require networks to be publicly available then this may change, but I don’t expect this to happen in the near future.</p>

---

## Post #52 by @PaoloZaffino (2020-09-14 14:36 UTC)

<p>Perfect, I got it.</p>
<p>Thanks</p>

---

## Post #53 by @epearlstone (2020-09-17 15:38 UTC)

<p>Thank you Andras. Do you happen to know how I might be able to run the  <a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" rel="noopener nofollow ugc">AIAA example script</a> from terminal? I’m not sure exactly where I should have the file saved/which folder to run the code from using terminal and also how to include the correct folder path. If you knew roughly what command to use from terminal to run this that would be a huge help.</p>

---

## Post #54 by @lassoan (2020-09-17 15:51 UTC)

<p>You can use <code>--python-script</code> argument to specify a script and command-line arguments to a script that you want to run in Slicer’s Python environment. See a complete example here: <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing">https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing</a></p>

---

## Post #55 by @psychicpotato (2020-10-01 19:56 UTC)

<p>Prof Lasso -</p>
<p>Many thanks for your work and sharing it with the community. We’re actually pondering a server setup to use within our small hospital group, but are a bit overwhelmed on where to start. Would you recommend going through the CLARA documentation to start and go from there? Is there any resource you would suggest as well?</p>
<p>Thanks,<br>
Alb</p>

---

## Post #56 by @lassoan (2021-03-29 00:09 UTC)

<p>2 posts were split to a new topic: <a href="/t/nvidia-aiaa-segment-editor-effect-returns-url-not-found-error/16811">NVidia AIAA segment editor effect returns “URL not found” error</a></p>

---

## Post #57 by @user1 (2021-04-22 14:22 UTC)

<p>Hi there, very great tool! Are there specific requirements to the CT-dataset (specific aquisition parameters like slice thickness …) Thank yu very much!</p>

---

## Post #58 by @lassoan (2021-04-22 19:18 UTC)

<p>Most models that NVidia created are trained on <a href="http://medicaldecathlon.com/">medical segmentation decathlon</a> data sets. You’ll get the best results if you use similar resolution and cropping. Fully automatic segmentation models are more sensitive and slower, so if you have trouble using those then you may switch to the ones that also take boundary points as inputs.</p>

---

## Post #59 by @yudhistira (2021-07-16 08:55 UTC)

<p>Hi, trying to connect, but the server is not responded. any solution regarding this?</p>
<p>thank you.</p>

---

## Post #60 by @lassoan (2021-07-16 11:30 UTC)

<p>The segmentation server address had changed, upgrade to the latest Slicer Stable Release or latest Slicer Preview Release and also update (or uninstall and install) the NVidia AI assisted segmentation extension.</p>

---

## Post #61 by @lassoan (2021-09-05 19:47 UTC)

<p>A post was merged into an existing topic: <a href="/t/nvidia-ai-assisted-segmentation-brain-tumor/19512/3">Nvidia AI-assisted segmentation (brain tumor)</a></p>

---

## Post #62 by @mhs (2023-10-29 08:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04d918cca3ba35a416723bafde35f407c8f7be98.jpeg" data-download-href="/uploads/short-url/GT2lftZeP2USMZ4yaJVxxkjch2.jpeg?dl=1" title="错误页面" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d918cca3ba35a416723bafde35f407c8f7be98_2_690x366.jpeg" alt="错误页面" data-base62-sha1="GT2lftZeP2USMZ4yaJVxxkjch2" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d918cca3ba35a416723bafde35f407c8f7be98_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d918cca3ba35a416723bafde35f407c8f7be98_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d918cca3ba35a416723bafde35f407c8f7be98_2_1380x732.jpeg 2x" data-dominant-color="9C9C9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">错误页面</span><span class="informations">1920×1021 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em><strong>After I downloaded the plug-in, an error appeared and the interface showed as follows. Could you please tell me how the author can solve this problem.</strong></em><br>
Traceback (most recent call last):<br>
File “E:/Slicer 5.4.0/slicer.org/Extensions-31938/NvidiaAIAssistedAnnotation/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 198, in fetchAIAAModels<br>
models = self.logic.list_models()<br>
File “E:/Slicer 5.4.0/slicer.org/Extensions-31938/NvidiaAIAssistedAnnotation/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1076, in list_models<br>
return aiaaClient.model_list(label)<br>
File “E:\Slicer 5.4.0\slicer.org\Extensions-31938\NvidiaAIAssistedAnnotation\lib\Slicer-5.4\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 190, in model_list<br>
status, response = AIAAUtils.http_method(‘GET’, self._server_url, selector)<br>
File “E:\Slicer 5.4.0\slicer.org\Extensions-31938\NvidiaAIAssistedAnnotation\lib\Slicer-5.4\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 620, in http_method<br>
conn = httplib.HTTPConnection(parsed.hostname, parsed.port)<br>
File “E:\Slicer 5.4.0\lib\Python\Lib\http\client.py”, line 857, in <strong>init</strong><br>
(self.host, self.port) = self._get_hostport(host, port)<br>
File “E:\Slicer 5.4.0\lib\Python\Lib\http\client.py”, line 891, in _get_hostport<br>
i = host.rfind(‘:’)<br>
AttributeError: ‘NoneType’ object has no attribute ‘rfind’</p>

---

## Post #63 by @lassoan (2023-10-29 12:30 UTC)

<p>The authors of the NVIDIA-AIAA engine has moved on to develop MONAILabel package and Slicer extension.</p>
<p>You can still use the NVIDIA-AIAA extension, but it is not supported and not recommended anymore. Demo server is no longer available so you need to set up your own server and specify its address in the module in Slicer.</p>

---

## Post #64 by @lassoan (2024-03-08 14:41 UTC)

<p>It is no longer necessary to set up a server for segmentation and not necessary to even have a GPU. Instead, there are several new extensions that allow segmenting images much more easily. For example, TotalSegmentator and MONAIAuto3DSeg extensions.</p>

---

## Post #65 by @LeidyMoraV (2024-05-14 21:38 UTC)

<p>Hi, Tamas<br>
I’m looking for the trained model (h5 file) shown in this video ( <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI" rel="noopener nofollow ugc">Tracked ultrasound AI segmentation and 3D reconstruction tutorial (youtube.com)</a>). I’m not able to find it in the github repository. Could you help me with that, please?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76d31f300d12a884137b30d12558e1c5e812c9bc.png" alt="image" data-base62-sha1="gXaFpz4tnAJmuCLfposkx0LDeaw" width="466" height="122"></p>

---

## Post #66 by @ungi (2024-05-16 14:47 UTC)

<p>Hi, that is a model saved in TensorFlow, in a version that is already a few years old. I wouldn’t recommend using it now. This folder contains the original data and a trained model: <a href="https://1drv.ms/f/s!AhiABcbe1DByhdt7psQ5658M_FYa6g?e=oIk8Pg" rel="noopener nofollow ugc">2019_SpineUs-Queens</a><br>
I recommend training a new model using MONAI rather than relying on the trained model in the folder.</p>

---

## Post #67 by @LeidyMoraV (2024-05-25 16:30 UTC)

<p>Hi,</p>
<p>Thank you for your response! I used the model available in the repository. Now, I would like to train a new model as you suggested. I’m very new to AI, so could you please guide me on how to do this using MONAI? Also, can I use the data provided in the repository to train the new model?</p>
<p>Thank you! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #68 by @pieper (2024-05-25 21:25 UTC)

<p>Here are some related posts:</p>
<p><a href="https://discourse.slicer.org/search?q=workshops+MONAI+Slicer+order%3Alatest">https://discourse.slicer.org/search?q=workshops+MONAI+Slicer+order%3Alatest</a></p>

---
