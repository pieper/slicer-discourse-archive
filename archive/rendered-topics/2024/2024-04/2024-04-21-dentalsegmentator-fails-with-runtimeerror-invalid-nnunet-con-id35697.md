# DentalSegmentator fails with "RuntimeError: Invalid nnUNet configuration. Model folder is missing the following folds"

**Topic ID**: 35697
**Date**: 2024-04-21
**URL**: https://discourse.slicer.org/t/dentalsegmentator-fails-with-runtimeerror-invalid-nnunet-configuration-model-folder-is-missing-the-following-folds/35697

---

## Post #1 by @ARtur_Zhumabekov (2024-04-21 05:55 UTC)

<p>Hello<br>
I get this error<br>
Failed to load the segmentation.</p>
<p>Check the inference folder content C:\Users\artur\AppData\Local\Temp\Slicer-vFmJLy\output</p>
<p>How i can fix it?</p>

---

## Post #2 by @Drhamidhmd (2024-04-21 09:10 UTC)

<p>hello<br>
first i would like to congratulate for this extension.<br>
super cool stuff<br>
i would like to inform you that i have installed the new version of slicer plus the extension… and tried but its not working even after upgrading pytorch  can you help me</p>

---

## Post #3 by @Thibault_Pelletier (2024-04-22 06:19 UTC)

<p>Hi <a class="mention" href="/u/artur_zhumabekov">@ARtur_Zhumabekov</a>  and <a class="mention" href="/u/drhamidhmd">@Drhamidhmd</a>,</p>
<p>Thank you for trying out our module.</p>
<p>Could you provide us with the following information so that we have a clearer view on what went wrong :</p>
<ul>
<li>Which OS did you try the module on</li>
<li>Which preview version date did you try it on. Slicer previews are built nightly and we made several fixes to the extension since it was added to the extension manager and you may want to test on the latest preview release to check if the problem is still there.</li>
<li>What is your machine configuration (RAM / CPU / GPU config)</li>
<li>Could you give us the information available in the module log. The logs are accessible by clicking on the (i) button next to the apply button</li>
<li>Could you give us the information available in the Python console</li>
</ul>
<p>Thanks in advance.</p>
<p>Best,<br>
Thibault</p>

---

## Post #4 by @Drhamidhmd (2024-04-23 08:56 UTC)

<p>Thanks for response.<br>
My problem got resolved… as pytorch was not working… I reinstalled it’s working properly.<br>
But it’s working with CbCt but not with medical ct scan</p>

---

## Post #5 by @Thibault_Pelletier (2024-04-23 14:34 UTC)

<p><a class="mention" href="/u/drhamidhmd">@Drhamidhmd</a> thanks for the update. Glad to know that it now works for you with your CBCT.</p>
<p>When you say the module doesn’t work with medical CT Scan, what do you mean? Does it not output the segmentation you are expecting? Does it not run to completion?</p>

---

## Post #7 by @Drhamidhmd (2024-05-05 08:14 UTC)

<p>Actually I uploaded the Medical scan on slicer and tried running the Dental segmentator…it took longer than normal time and got hanged… happened many time</p>

---

## Post #8 by @the_ice (2024-05-20 02:33 UTC)

<p>I came across a mistake :</p>
<pre><code class="lang-auto">RuntimeError: Invalid nnUNet configuration. Model folder is missing the following folds : [0].
Your model weight folder path should look like the following :
Dataset&lt;dataset_id&gt;/&lt;trainer_name&gt;__&lt;plan_name&gt;__&lt;conf_name&gt;

It should also contain a dataset.json file and fold_&lt;i_fold&gt; folders with model weights.

Provided model dir :
D:\ProgramData\slicer.org\Slicer 5.7.0-2024-05-15\slicer.org\Extensions-32859\DentalSegmentator\lib\Slicer-5.7\qt-scripted-modules\Resources\ML
</code></pre>
<p>It seems the path “DentalSegmentator\Resources\ML” created in SlicerDentalSegmentator is not well recognized by the nnUNet library.<br>
How can i fix it?</p>

---

## Post #9 by @the_ice (2024-05-20 06:38 UTC)

<p>First i would like to congratulate for this extension.<br>
I came across a mistake :</p>
<pre><code class="lang-auto">RuntimeError: Invalid nnUNet configuration. Model folder is missing the following folds : [0].
Your model weight folder path should look like the following :
Dataset&lt;dataset_id&gt;/&lt;trainer_name&gt;__&lt;plan_name&gt;__&lt;conf_name&gt;

It should also contain a dataset.json file and fold_&lt;i_fold&gt; folders with model weights.

Provided model dir :
D:\ProgramData\slicer.org\Slicer 5.7.0-2024-05-15\slicer.org\Extensions-32859\DentalSegmentator\lib\Slicer-5.7\qt-scripted-modules\Resources\ML
</code></pre>
<p>I read the related .py file.<br>
It seems the path “DentalSegmentator\Resources\ML” created in SlicerDentalSegmentator is not well recognized by the nnUNet library.<br>
In addition, the 3D Slicer is 5.7.0-2024-05-15 r32859 / 332732c, the nnUNet is Version:edb9b03 (2024-05-16).</p>

---

## Post #10 by @Thibault_Pelletier (2024-05-21 06:27 UTC)

<p>Hi <a class="mention" href="/u/the_ice">@the_ice</a> ,</p>
<p>Thank you for your feedback and your interest in our extension.<br>
It seems the model may not have been correctly downloaded / extracted in your ML folder.</p>
<p>To make up for that, you can follow the troubleshooting here : <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights" class="inline-onebox" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</a></p>
<p>It consists in :</p>
<ul>
<li>Downloading the latest .zip file from the release and extracting it in the <code>DentalSegmentator\Resources\ML</code>  folder</li>
<li>Creating a <code>download_info.json</code> in the ML folder with the following content : <code>{ "download_url": "https://github.com/gaudot/SlicerDentalSegmentator/releases/download/v1.0.0-alpha/Dataset111_453CT_v100.zip" }</code></li>
</ul>
<p>Please let me know if that solves the issue on your end.</p>
<p>Best,<br>
Thibault</p>

---

## Post #12 by @the_ice (2024-05-22 00:35 UTC)

<p>Thank you very much! The advice you gave me was very precise. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @karim_mamdouh (2024-06-08 14:52 UTC)

<p>hello<br>
i have the same issue<br>
Failed to load the segmentation.</p>
<p>Check the inference folder content C:\Users\Khateeb\AppData\Local\Temp\Slicer-iPdxkt\output</p>

---

## Post #15 by @Thibault_Pelletier (2024-06-10 06:22 UTC)

<p>Hi <a class="mention" href="/u/karim_mamdouh">@karim_mamdouh</a>,</p>
<p>Thanks for your interest in our extension.<br>
Could you give us the log content when you experience this error?</p>
<p>The logs can be found by pressing the (i) button next to the apply button</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/126a9c1c5b97dcaeeff9384f6f3fdcbea6332d5f.png" alt="image" data-base62-sha1="2CV0iWoY7dKEMQG4JboEHrMdWuX" width="601" height="124"></p>

---

## Post #16 by @Marce (2024-06-10 08:33 UTC)

<aside class="quote no-group quote-modified" data-username="karim_mamdouh" data-post="13" data-topic="35697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/karim_mamdouh/48/76890_2.png" class="avatar"> karim_mamdouh:</div>
<blockquote>
<p>o se pudo cargar la segmentación.</p>
<p>Verifique el contenido de la carpeta de inferencia C:\Users\Khateeb\AppData\Local\Temp\Slicer-</p>
</blockquote>
</aside>
<p>Hello, dowload:<br>
<a href="https://slicer-packages.kitware.com/api/v1/item/665d6717c8a295ea328461ef/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/665d6717c8a295ea328461ef/download</a></p>
<p>This is slicer package “Slicer-5.7.0-2024-06-01-win-amd64”. this work.</p>

---

## Post #17 by @viet_duc_Vu (2024-06-10 12:53 UTC)

<aside class="quote no-group" data-username="Marce" data-post="16" data-topic="35697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marce/48/76822_2.png" class="avatar"> Marce:</div>
<blockquote>
<p><a href="https://slicer-packages.kitware.com" rel="noopener nofollow ugc">https://slicer-packages.kitware.com</a></p>
</blockquote>
</aside>
<p>Thank you, this actually work !</p>

---

## Post #18 by @DrG (2024-06-14 22:15 UTC)

<p>This worked for me as well. Reinstalling everything did nothing, but going back from June10th version to this June1st, fixed it. Thanks!</p>

---

## Post #19 by @Marta_Fernandez (2024-08-26 16:12 UTC)

<p>Hi, thanks for the extensión but it still not working</p>

---

## Post #20 by @bina_magomedova (2024-10-14 07:57 UTC)

<p>I’ve been struggling with this problem for days and in no way. Please help me! I can’t work without this program<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c24eb1ca0f9ecb8d8c16f37fbfa270b8c1c991f2.jpeg" alt="photo_2024-10-10_20-25-30" data-base62-sha1="rIVelD0Br9hkA1W5XDrCd1Au9GO" width="500" height="175"></p>

---

## Post #21 by @jamesobutler (2024-10-14 11:40 UTC)

<p>Review the following DentalSegmentator GitHub posts for similar reports. If you are still having issues you can try creating a new GitHub issue as a method for contacting the DentalSegmentator library maintainers. They may be more responsive there compared to the Slicer discourse forum.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator/issues/10#issuecomment-2303831994">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/10#issuecomment-2303831994" target="_blank" rel="noopener nofollow ugc">github.com/gaudot/SlicerDentalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/10#issuecomment-2303831994" target="_blank" rel="noopener nofollow ugc">Fail to load segmentation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-06-17" data-time="21:30:44" data-timezone="UTC">09:30PM - 17 Jun 24 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2024-09-18" data-time="07:48:01" data-timezone="UTC">07:48AM - 18 Sep 24 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/nguyetun5" target="_blank" rel="noopener nofollow ugc">
          <img alt="nguyetun5" src="https://avatars.githubusercontent.com/u/173105651?v=4" class="onebox-avatar-inline" width="20" height="20">
          nguyetun5
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I'm using Slicer 5.7.0 revision 32900 6-16-2024 on Windows.  The error code read<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">s as fail to load segmentation.  I can get it to work on my Mac with M1 or M2 but can get the extension to work on Windows.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator/issues/8#issuecomment-2161600947">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/8#issuecomment-2161600947" target="_blank" rel="noopener nofollow ugc">github.com/gaudot/SlicerDentalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/8#issuecomment-2161600947" target="_blank" rel="noopener nofollow ugc">Failed to load the segmentation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-06-02" data-time="03:51:26" data-timezone="UTC">03:51AM - 02 Jun 24 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2024-06-17" data-time="06:12:08" data-timezone="UTC">06:12AM - 17 Jun 24 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/dentistfrankchen" target="_blank" rel="noopener nofollow ugc">
          <img alt="dentistfrankchen" src="https://avatars.githubusercontent.com/u/56914624?v=4" class="onebox-avatar-inline" width="20" height="20">
          dentistfrankchen
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Now I am using the 5.7.0 32881 3d slicer with EC2 ubuntu 22.04.
When I try usin<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">g the cpu version of  torch(2.2.1),everything works fine. However, when I use cu118 version, I get this error: failed to load the segmentation. Check ...
This seems to be error with SlicerNNUnet(with segmentationlogic.py)
Can you guys have a look?
Thank you.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
