# Error in Nvidia AIAA

**Topic ID**: 20730
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/error-in-nvidia-aiaa/20730

---

## Post #1 by @user5 (2021-11-22 16:55 UTC)

<p>Since my Nvidia AIAA has lacked of  the model of annotation_mri_brain_tumors_t1ce_tc, I reinstalled the Nvidia AIAA.<br>
After I reinstall the Nvidia AIAA, it happen a error call “Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser”. How to fix it?</p>

---

## Post #2 by @lassoan (2021-11-22 18:36 UTC)

<p>What server address do you use?<br>
If you open that server address with <code>/v1/models</code> appended in the web browser (e.g., <code>http://perklabseg.asuscomm.com:5000/v1/models</code>) then what do you see?</p>

---

## Post #3 by @user5 (2021-11-23 00:19 UTC)

<pre><code class="lang-json">[
  {
    "name": "clara_pt_brain_mri_annotation_t1c",
    "labels": [
      "brain tumor core"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the tumor from MRI T1C image using DEXtr3D",
    "version": "1",
    "type": "annotation"
  },
  {
    "name": "clara_pt_brain_mri_segmentation_t1c",
    "labels": [
      "tumor"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the tumor core from MRI T1c image",
    "version": "1",
    "type": "segmentation"
  },
  {
    "name": "clara_pt_covid19_ct_lesion_segmentation",
    "labels": [
      "COVID-19 affected regions"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of COVID-19 affected regions in the lung from CT image",
    "version": "1",
    "type": "segmentation"
  },
  {
    "name": "clara_pt_covid19_ct_lung_annotation",
    "labels": [
      "lung"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the lung from CT image using DEXtr3D",
    "version": "1",
    "type": "annotation"
  },
  {
    "name": "clara_pt_covid19_ct_lung_segmentation",
    "labels": [
      "lung"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the Lung from CT image",
    "version": "1",
    "type": "segmentation"
  },
  {
    "name": "clara_pt_deepgrow_2d_annotation",
    "labels": [],
    "description": "2D DeepGrow model based on Unet",
    "version": "1",
    "type": "deepgrow",
    "deepgrow": "2D"
  },
  {
    "name": "clara_pt_deepgrow_3d_annotation",
    "labels": [],
    "description": "3D DeepGrow model based on Unet",
    "version": "1",
    "type": "deepgrow",
    "deepgrow": "3D"
  },
  {
    "name": "clara_pt_liver_and_tumor_ct_segmentation",
    "labels": [
      "liver",
      "liver tumor"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the liver and tumor from CT",
    "version": "1",
    "type": "segmentation"
  },
  {
    "name": "clara_pt_pancreas_and_tumor_ct_segmentation",
    "labels": [
      "pancreas",
      "pancreas tumor"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the pancreas and tumor from portal venous phase CT",
    "version": "1",
    "type": "segmentation"
  },
  {
    "name": "clara_pt_prostate_mri_segmentation",
    "labels": [
      "prostate central gland",
      "prostate peripheral zone"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the liver and tumor from MRI",
    "version": "1",
    "type": "segmentation"
  },
  {
    "name": "clara_pt_spleen_ct_annotation",
    "labels": [
      "spleen"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the spleen from CT image using DEXtr3D",
    "version": "1",
    "type": "annotation"
  },
  {
    "name": "clara_pt_spleen_ct_segmentation",
    "labels": [
      "spleen"
    ],
    "description": "A pre-trained model for volumetric (3D) segmentation of the spleen from CT image",
    "version": "1",
    "type": "segmentation"
  }
]
</code></pre>

---

## Post #4 by @user5 (2021-11-23 00:20 UTC)

<p>I am using default server address</p>

---

## Post #5 by @lassoan (2021-11-23 00:36 UTC)

<p>The server response looks good. Which Slicer version are you using? Are you behind a hospital/corporate firewall or proxy server?</p>

---

## Post #6 by @user5 (2021-11-23 00:54 UTC)

<p>version 4.13.0, I am using university network.</p>

---

## Post #7 by @lassoan (2021-11-23 01:12 UTC)

<p>Which Slicer-4.13.0 version exactly? I’ve just tested latest Slicer Preview Release and it works well.<br>
Do you use a proxy server to connect to the internet?</p>

---

## Post #8 by @user5 (2021-11-23 01:20 UTC)

<p>2021-11-21<br>
I can use it now, after I shutdown the Anti-Virus software.<br>
But it still lack of the model of annotation_mri_brain_tumors_t1ce_tc</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66dfe08cceea5c81fa32baa7a26ba95c02638a64.png" data-download-href="/uploads/short-url/eG4m6DieqSunTNtCiFgAWYIVile.png?dl=1" title="螢幕擷取畫面 (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66dfe08cceea5c81fa32baa7a26ba95c02638a64_2_690x364.png" alt="螢幕擷取畫面 (2)" data-base62-sha1="eG4m6DieqSunTNtCiFgAWYIVile" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66dfe08cceea5c81fa32baa7a26ba95c02638a64_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66dfe08cceea5c81fa32baa7a26ba95c02638a64_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66dfe08cceea5c81fa32baa7a26ba95c02638a64_2_1380x728.png 2x" data-dominant-color="AAABC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">螢幕擷取畫面 (2)</span><span class="informations">1917×1014 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-11-23 01:27 UTC)

<p>I’ve installed all the models that I’ve found on <a href="https://catalog.ngc.nvidia.com/models?filters=&amp;orderBy=scoreDESC&amp;pageNumber=0&amp;query=clara_pt&amp;quickFilter=">NGC for latest Clara4</a> a few months ago. If you know about any additional pretrained models that you would like to see on the server then let me know.</p>

---

## Post #10 by @user5 (2021-11-23 05:18 UTC)

<p>After I download the models, Is it just put it into the extension file of Nvidia and it’s fine?</p>

---

## Post #11 by @lassoan (2021-11-23 05:20 UTC)

<p>The models must be installed on the server. If there are any Clara v4 pre-trained models that are not installed on the server already then send me the download link and I’ll install on the server.</p>

---

## Post #12 by @user5 (2021-11-23 05:27 UTC)

<p>I would like to these two model.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_brain_mri_segmentation_t1c">
  <header class="source">

      <a href="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_brain_mri_segmentation_t1c" target="_blank" rel="noopener nofollow ugc">NGC Catalog</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_brain_mri_segmentation_t1c" target="_blank" rel="noopener nofollow ugc">clara_pt_brain_mri_segmentation_t1c | NVIDIA NGC</a></h3>

  <p>A pre-trained model for volumetric (3D) annotation of the tumor core (TC) from MRI scans (T1c).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_fed_learning_brain_tumor_mri_segmentation">
  <header class="source">

      <a href="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_fed_learning_brain_tumor_mri_segmentation" target="_blank" rel="noopener nofollow ugc">NGC Catalog</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/med/models/clara_pt_fed_learning_brain_tumor_mri_segmentation" target="_blank" rel="noopener nofollow ugc">clara_pt_fed_learning_brain_tumor_mri_segmentation | NVIDIA NGC</a></h3>

  <p>A federated learning demo for volumetric (3D) segmentation of brain tumors from multimodal MRIs.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @lassoan (2021-11-23 05:39 UTC)

<p>clara_pt_brain_mri_segmentation_t1c - already installed</p>
<p>clara_pt_fed_learning_brain_tumor_mri_segmentation -  this model requires 4 channel MRI (4 aligned MRIs T1c, T1, T2, FLAIR at 1x1x1 mm), which GUI clients, such as the NVidia AIAA Segment Editor effect in 3D Slicer does not support. You need to do some custom Python scripting, as described here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/92">
  <header class="source">

      <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/92" target="_blank" rel="noopener">github.com/NVIDIA/ai-assisted-annotation-client</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/92" target="_blank" rel="noopener">Slicer 3D - Error Using nVIDIA AIAA - Prostate Model</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-28" data-time="12:26:59" data-timezone="UTC">12:26PM - 28 Oct 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/marioboccia1992" target="_blank" rel="noopener">
          <img alt="marioboccia1992" src="https://avatars.githubusercontent.com/u/93326712?v=4" class="onebox-avatar-inline" width="20" height="20">
          marioboccia1992
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Dear all,

Unfortunately I’m facing issue using nVIDIA AIAA module "clara_pt_p<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rostate_mri_segmentation" in 3D Slicer.

Running the AI I get this error:

" Traceback (most recent call last):

File “C:/Users/M/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 410, in onClickSegmentation

extreme_points, result_file = self.logic.segmentation(in_file, session_id, model)

File “C:/Users/M/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1092, in segmentation

session_id=session_id,

File “C:\Users\M\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 389, in inference

raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, form))

NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 500; Response: b’{“error”:{“message”:[],“type”:“InferenceServerException”},“success”:false}\n’’) "

The prostate model probably fails because it requires two input images (T2 and ADC), but on Slicer I do not have the option to select two volumes.

Thank you very much !

M.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can add a comment to this issue requesting this feature to be implemented in the GUI, but since NVidia the developers currently mostly focus on <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel</a>, most likely you’ll get more help if you ask for making this model available in the MONAILabel Slicer extension.</p>

---

## Post #15 by @user5 (2021-11-23 06:37 UTC)

<p>Is clara_pt_brain_mri_segmentation_t1c only use in auto segmentation? I would to use it in segment from boundary points.</p>

---

## Post #16 by @lassoan (2021-11-23 06:51 UTC)

<p>Each model is for a specific segmentation method. For example, a model created for “auto-segmentation” can only be used for “auto-segmentation”, and it cannot be used for “segment from boundary points”.</p>

---

## Post #17 by @Pari_TF (2022-05-05 18:26 UTC)

<p>Dear Andres,</p>
<p>I have the same error. I was using the NVIDIA AIAA segmenting the lung tumour using the annotation lung tumor model (Segment from boundary points) this morning, but now this error appears.<br>
I installed it on another computer, it doesn’t have any error, but now it doesn’t conssist the annotation_lung_tumor (it just has the covid models for lung) and there is no model for the lung tumour anymore. I would be grateful if you help me, please.</p>
<p>Best regards,<br>
Parisa</p>

---

## Post #18 by @lassoan (2022-05-05 21:46 UTC)

<p>For lung segmentation, on the default Slicer AIAA segmentation server you can find the <code>clara_pt_covid19_ct_lung_segmentation</code> automatic segmentation model and the <code>clara_pt_covid19_ct_lung_annotation</code> point based segmentation model.</p>
<p>You can find more pre-trained models for <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer">MONAILabel</a>.</p>
<p>You can also segment lungs using <a href="https://github.com/rbumm/SlicerLungCTAnalyzer#lung-ct-analyzer">LungCTAnalyzer</a> and <a href="https://github.com/pzaffino/SlicerDensityLungSegmentation#slicerdensitylungsegmentation">DensityLungSegmentation</a> extensions.</p>

---

## Post #19 by @lassoan (2022-05-05 22:36 UTC)

<aside class="quote no-group" data-username="Pari_TF" data-post="17" data-topic="20730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pari_tf/48/15222_2.png" class="avatar"> Pari_TF:</div>
<blockquote>
<p>but now it doesn’t conssist the annotation_lung_tumor</p>
</blockquote>
</aside>
<p>Are you sure this model is available for the latest NVidia Clara AIAA server version? I don’t see it on <a href="https://catalog.ngc.nvidia.com/models?filters=&amp;orderBy=scoreDESC&amp;query=label:%22Clara%22">NGC</a>. If you can send a download link on NGC then I can install it on the server.</p>

---

## Post #20 by @Pari_TF (2022-05-06 10:04 UTC)

<p>Thanks for your reply.<br>
No, unfortunately it’s not available anymore.<br>
There is no model for lung tumor (not the whole lung).<br>
It was very helpful. But, it seems this model is not available now.</p>

---

## Post #21 by @Pari_TF (2022-05-06 10:08 UTC)

<p>Yesterday I could use it for a couple of hours. Because I had installed the NVIDIA AIAA on 3D-Slicer a long time ago and I was using the lung tumor annotation model. But suddenly it stopped and this error appeared.</p>

---

## Post #22 by @lassoan (2022-05-06 12:49 UTC)

<p>You can ask MONAILabel developers to help you port the old model into a MONAILabel app.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>

---

## Post #23 by @diazandr3s (2022-05-06 14:02 UTC)

<p>Thanks for the ping, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p><a class="mention" href="/u/pari_tf">@Pari_TF</a>, have you considered using MONAI Label (<a href="https://github.com/Project-MONAI/MONAILabel" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a>)?</p>
<p>It is easy to get a pretrained model for lung segmentation using MONAI Label. Are you using a public dataset?</p>

---

## Post #24 by @Pari_TF (2022-05-12 12:59 UTC)

<p>Thanks for your reply. No, I haven’t used MONAI Label. That’s great. I will try it. Thank you so much. Yes, I’m working on a public dataset.</p>

---

## Post #25 by @scorey1983 (2022-05-18 09:10 UTC)

<p>I am using my own data to segment lung nodules. The training set has been using the annotation_lung_tumor model of Nvidia AIAA. Now that the test set is ready, I found that the above model is no longer available, which caused me a lot of trouble. Can you help me add the old model to MONAI Label, thanks.</p>

---

## Post #26 by @diazandr3s (2022-05-18 23:09 UTC)

<p>Do you know which dataset they used to get that pretrained model? I think it is Task06_Lung (<a href="https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2" class="inline-onebox" rel="noopener nofollow ugc">MSD - Google Drive</a>) from the Medical Segmentation Decathlon but I’m not sure.</p>
<p>If that’s the dataset, you should be able to get a pretrained model fairly easy. Do you have a GPU-based PC?</p>

---

## Post #27 by @scorey1983 (2022-05-19 02:55 UTC)

<p>It is indeed a model pre-trained with the Task06_Lung dataset, and we use boundary-point based segmentation of lung tumor on CT (AIAA for 3D Slicer). But now the model is not found in NVIDIA. Also, we have GPU-based PC.</p>

---

## Post #28 by @rbumm (2022-05-19 11:15 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="23" data-topic="20730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>It is easy to get a pretrained model for lung segmentation using MONAI Label. Are you using a public dataset?</p>
</blockquote>
</aside>
<p>I was going to try this out but I am consistently running into</p>
<pre><code class="lang-auto">monailabel apps --download --name deepedit --output apps
Using PYTHONPATH=/home/rbumm:
App deepedit =&gt; /usr/monailabel/sample-apps/deepedit not exists
</code></pre>
<p>after a</p>
<pre><code class="lang-auto">pip install monailabel
</code></pre>
<p>This is with and w/o an elevated bash on Windows 10 Ubuntu WSL. Any ideas?</p>

---

## Post #29 by @diazandr3s (2022-05-19 12:30 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> there were recently some changes in folder structure. Please try out the monailabel-weekly instead (pip install monailabel-weekly)</p>
<p>Then download the radiology app as follows:</p>
<pre><code>monailabel apps --download --name radiology --output apps
</code></pre>
<p>As an example you could download and use the spleen dataset:</p>
<pre><code>monailabel datasets --download --name Task09_Spleen --output datasets
</code></pre>
<p>Then start the server using the Deepedit model:</p>
<pre><code>monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models deepedit
</code></pre>
<p>Here you can see more details: <a href="https://github.com/Project-MONAI/MONAILabel#release-candidate" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>

---

## Post #30 by @rbumm (2022-05-19 12:48 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="29" data-topic="20730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>pip install monailabel-weekly</p>
</blockquote>
</aside>
<p>Thanks, Andres, tried this already - pip uninstalled monailabel and pip installed monailabel-weekly,  but there is a similar message:</p>
<pre><code class="lang-auto">monailabel apps --download --name radiology --output apps
Using PYTHONPATH=/home/rbumm:
App radiology =&gt; /usr/monailabel/sample-apps/radiology not exists
</code></pre>
<p>Probably a permission problem.</p>

---

## Post #32 by @diazandr3s (2022-05-19 18:06 UTC)

<p>This is strange <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"><br>
Probably the weekly installation wasn’t clean. Please do a clean installation using a clean Python virtual environment.</p>

---

## Post #33 by @rbumm (2022-05-20 12:40 UTC)

<p>Needed to install monailabel via github to make this working in Windows 10 WSL (<a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/31">see here</a>).</p>

---

## Post #34 by @diazandr3s (2022-05-20 16:04 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>,</p>
<p>My bad, I just realised the weekly version doesn’t install the candidate release 0.4.0 <img src="https://emoji.discourse-cdn.com/twitter/slightly_frowning_face.png?v=12" title=":slightly_frowning_face:" class="emoji" alt=":slightly_frowning_face:" loading="lazy" width="20" height="20"><br>
In order to use the radiology app you should either use directly the GitHub repo as you did or install directly the candidate release:</p>
<p>pip install monailabel==0.4.0rc3</p>
<p>Please let me know how that goes. Happy to help.</p>
<p>Andres</p>

---

## Post #35 by @Bor_Antolic (2023-01-03 13:55 UTC)

<p>Hi!<br>
I would like to use NVidia AIAA in 3d Slicer on my work (hospital) computer.<br>
I get the error<br>
Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser</p>
<p>I cannot access <a href="http://perklabseg.asuscomm.com:5000/v1/models" rel="noopener nofollow ugc">http://perklabseg.asuscomm.com:5000/v1/models</a> from my browser.<br>
I am probably behind a proxy. How I can configure the settings, so the AIAA would work?<br>
Thanks!<br>
Bor</p>

---

## Post #36 by @xux7306 (2024-07-14 04:07 UTC)

<p>Hello, I entered the URL <code>http://perklabseg.asuscomm.com:5000/v1/models</code>, but it shows that <code>perklabseg.asuscomm.com</code> is currently unable to handle this request. HTTP ERROR 502. What should I do? I can’t connect to the default server. Please help me.</p>

---

## Post #37 by @lassoan (2024-07-14 14:07 UTC)

<p>This is a quickly evolving field. We don’t provide the NVIDIA AIAA demo server anymore, as the developers of this segmentation tool moved on to new technologies.</p>
<p>You can now use tools such as <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg">MONAIAuto3DSeg</a> and <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#totalsegmentator">TotalSegmentator</a> extensions for simple server-less running of pre-trained models and <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer#readme">MONAILabel</a> for training your own models.</p>

---

## Post #38 by @jamesobutler (2024-07-14 17:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Is it time to archive Nvidia AIAA from the Slicer extensions index? Otherwise it is likely a “tier 5” extension as it is not under active development with little to no support. This will help the community better understand what are the higher quality AI based extensions to use in Slicer.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/de1784752880fbb490262060da28efb81aa96893/NvidiaAIAssistedAnnotation.json">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/de1784752880fbb490262060da28efb81aa96893/NvidiaAIAssistedAnnotation.json" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/de1784752880fbb490262060da28efb81aa96893/NvidiaAIAssistedAnnotation.json" target="_blank" rel="noopener nofollow ugc">Slicer/ExtensionsIndex/blob/de1784752880fbb490262060da28efb81aa96893/NvidiaAIAssistedAnnotation.json</a></h4>


      <pre><code class="lang-json">{
  "$schema": "https://raw.githubusercontent.com/Slicer/Slicer/main/Schemas/slicer-extension-catalog-entry-schema-v1.0.0.json#",
  "build_dependencies": [],
  "build_subdirectory": ".",
  "category": "Segmentation",
  "scm_revision": "master",
  "scm_url": "https://github.com/NVIDIA/ai-assisted-annotation-client.git"
}
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #39 by @lassoan (2024-07-14 18:47 UTC)

<p>I agree, making it a low-tier extension (when the tier system is introduced) is a good idea.</p>

---
