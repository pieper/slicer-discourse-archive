# DeCAL: groupwise analysis

**Topic ID**: 43742
**Date**: 2025-07-16
**URL**: https://discourse.slicer.org/t/decal-groupwise-analysis/43742

---

## Post #1 by @MrMarkus (2025-07-16 15:11 UTC)

<p>Dear all,</p>
<p>I would like to analyse two groups of skull-data, micro-CT data.</p>
<p>The idea is to start with group1</p>
<ul>
<li>run DeCAL with the data of group1, use the models and fixed LMs to generate an atlas and the alignedLMs (group1)</li>
</ul>
<p>Next, repeat the DeCAL with the data of group2,  use the models and fixed LMs to generate an atlas and the alignedLMs (group2)</p>
<p>Now use DeCA to analyse group1 &amp; group2</p>
<ul>
<li>load atlas of group1</li>
<li>perform “Shape analysis”</li>
<li>model directory: folder of the alingedModels of group2</li>
<li>landmark directory: folder of the alingedLMs of group2</li>
</ul>
<p>I guess, important would be to merge the “fixed” and the “SemiLMs” as descripted<br>
in the tutorial.</p>
<p>The idea is to create an atlas based on group1. Next, to analyse “shape variances” between the atlas (group1) and each individual data set of group2. And, to analyse shape differences between the atlas1 and atlas2.</p>
<p>This approach is motivated by the fact that group1 varies in shape in comparison to group2, and therefor the atlas should be derived only from the data of group1.</p>
<p>Is such an analysis feasable with DeCA and DeCAL? And what are the important steps?</p>
<p>Thanks for your support.</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2025-07-16 17:47 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="43742">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>Is such an analysis feasable with DeCA and DeCAL? And what are the important steps?</p>
</blockquote>
</aside>
<p>This can be done in DeCAL and SLicerMorph up to a point. But there are couple important things to consider.</p>
<ol>
<li>Why are you building two atlases separately? This will create a headache for you, since during the dense semiLM creation there is no guarantee that it will create identical number of points for both groups, and if the point number and distribution is not identical, you cannot do a landmark-based shape analysis.</li>
<li>Instead you should build the atlas using all your samples (including group 1 and 2) and then create the semiLMs etc, and then use statistical models to find groupwise differences.</li>
<li>Statistical models are not yet available in SlicerMorph, but we do have a proposal to develop that. Until then you can migrate your data into R and then conduct the statistical analysis of group wise differences there.</li>
</ol>

---

## Post #3 by @MrMarkus (2025-07-21 12:25 UTC)

<p>Dear Murat,</p>
<p>thanks a lot for your response and the detailed insights!</p>
<p>Headache,… hmmm… should be avoided <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Will stick to your advise!</p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @MrMarkus (2025-07-22 11:30 UTC)

<p>Dear Murat,</p>
<p>could you please comment on the following steps. I tried to combined the DeCAL and the DeCA processing / analysis methods.</p>
<p>First DeCAL was used, on the mouse skull CT data; in addition 20 manually placed landmarks are considered.<br>
DeCAL was used to generated:</p>
<ul>
<li>atlas model of both groups</li>
<li>atlas landmarks (300 points in total) of both groups</li>
<li>aligned individual models</li>
<li>aligned individual landmarks (300 in total)</li>
</ul>
<p>Next the idea is to use DECA and perform shape analysis on the aligned data derived by DeCAL</p>
<ul>
<li>folder atlas model: DeCAL derived atlas model</li>
<li>folder atlas landmarks: DeCAL derived atlas landmarks (300 points)</li>
<li>model directory: DeCAL aligned individual models of mice skulls</li>
<li>landmark directory: DeCAL aligned indivual landmarks of mice skulls</li>
</ul>
<p>Finally the analysis should start by hitting “DeCA”.</p>
<p>Unfortunately only the Output folders were created, without any content, and the atlas model together with the landmarks are shown in the 3D view.<br>
But no computation?</p>
<p>Is this the correct way to go? Do I miss something here?</p>
<p>I am using Win10, Slicer 5.8.1</p>
<p>Thanks for your support!</p>
<p>Best,<br>
Markus</p>

---

## Post #5 by @muratmaga (2025-07-22 15:15 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="4" data-topic="43742">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>could you please comment on the following steps. I tried to combined the DeCAL and the DeCA processing / analysis methods.</p>
</blockquote>
</aside>
<p>Actually you do not need to use DeCAL for DeCA. All of the steps you mention can be accomplished in the DeCA. DeCAL is specifically for creating dense landmark sets that are constrained by anatomical landmarks and create an 3D atlas. Users of this module would usually run these landmarks using GPA module</p>
<p>DeCA would do all of this automatically. But since you already created your atlas, you can make use of that in DeCA (with the option load atlas, instead of create atlas) and continue the analysis.</p>
<aside class="quote no-group" data-username="MrMarkus" data-post="4" data-topic="43742">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>But no computation?</p>
</blockquote>
</aside>
<p>Let’s first make you are indeed running the latest version of DeCA extension. We have updated a couple months ago. It should look like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f0c350047c9c0b0f7466622e91a4467cf38fd62.png" data-download-href="/uploads/short-url/mH04pTUYM9U8cQvJ6225JDVZy1k.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f0c350047c9c0b0f7466622e91a4467cf38fd62.png" alt="image" data-base62-sha1="mH04pTUYM9U8cQvJ6225JDVZy1k" width="376" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">493×655 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @MrMarkus (2025-07-23 19:45 UTC)

<p>Hi,</p>
<p>okay.<br>
I am running: Version d8e6aa4 (2025-06-18)</p>
<p>I use DECA since in addition it offers to “adjust” the numbers of sampling<br>
points (semiLMs), kind of control.</p>
<p>Regarding DeCAL: there is some issue while running the analysis; here<br>
is the output of the python console:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-33241/DenseCorrespondenceAnalysis/lib/Slicer-5.8/qt-scripted-modules/DeCA.py”, line 603, in onDCApplyButton<br>
slicer.util.saveNode(atlasModel, atlasModelPath)<br>
UnboundLocalError: local variable ‘atlasModel’ referenced before assignment</p>
<p>I doubled-checked the input folders;<br>
option: load atlas: atlas.py &amp; atlas_aligned_LMs (semiLMs)</p>
<p>model folder: aligned_models *.py (derived from DeCAL)<br>
lm folder: aligned_LMs (derived from DeCAL, semiLMs)  // I moved  the atlas_aligned_LMs from this folder to a separate folder (which is used above in the load atlas section)</p>
<p>To me this should be ok?</p>
<p>Any ideas what´s wrong here?</p>
<p>THANKS!</p>
<p>Best,<br>
Markus</p>

---

## Post #7 by @muratmaga (2025-07-23 21:29 UTC)

<p>You are using the latest version. The error suggest atlas was tried to be saved before it is created, but I can’t replicate this on my end with my data.</p>
<p>Any chance you can share your input files as a zip archive? (you can upload them here <a href="https://faculty.uw.edu/maga/data_dropbox">https://faculty.uw.edu/maga/data_dropbox</a> if you do not want to share publicly).</p>

---

## Post #8 by @MrMarkus (2025-07-24 16:24 UTC)

<p>Dear Murat,</p>
<p>thanks for your support!</p>
<p>I moved the data to the suggested dropbox location.</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #9 by @muratmaga (2025-07-24 17:37 UTC)

<p>OK. I can replicate this issue with your data. Not sure why it is happening I opened an issue and pinged <a class="mention" href="/u/smrolfe">@smrolfe</a> to take a look.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis/issues/4">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis/issues/4" target="_blank" rel="noopener">github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis/issues/4" target="_blank" rel="noopener">DeCA fails when loading an existing atlas from DeCAL</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-24" data-time="17:35:24" data-timezone="UTC">05:35PM - 24 Jul 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">After I choose the atlas and the landmarks (from an existing DeCAL run), specifi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ced the model and LM directory, and then hit RUN  DECA, I get this: 

Getting this error:

Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-33241/DenseCorrespondenceAnalysis/lib/Slicer-5.8/qt-scripted-modules/DeCA.py", line 603, in onDCApplyButton
    slicer.util.saveNode(atlasModel, atlasModelPath)
UnboundLocalError: local variable 'atlasModel' referenced before assignment</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @muratmaga (2025-07-28 22:44 UTC)

<p><a class="mention" href="/u/smrolfe">@smrolfe</a> pushed a change that seems to fix the problem. Tomorrow, update your DeCA extension via the extension manager (if you are using 5.8.1) and give it a try.</p>

---

## Post #11 by @MrMarkus (2025-07-29 12:13 UTC)

<p>Hi,</p>
<p>today I updated DeCA. Unfortunately it didn´t improved the situation.</p>
<p>I tried DeCA on another set of CT skulls.</p>
<p>Steps:</p>
<ul>
<li>data of 32 skulls was processed with DeCAL, to expand the 20 fix landmarks, now in<br>
total 230 landmarks (fixed and semiLM merged) are available</li>
<li>atlas was also generated (but not further used)</li>
<li>DeCA: <strong>create atlas &amp; shape analysis</strong>
<ul>
<li>input folder model: aligned (after DeCAL) skull models</li>
<li>input folder LMs: aligned (after DeCAL) merged 230 landmakr</li>
</ul>
</li>
</ul>
<p>Resulting error log:</p>
<p><em>Traceback (most recent call last):</em></p>
<p><em>File “C:/Software/Slicer_5_8_1/slicer.org/Extensions-33241/DenseCorrespondenceAnalysis/lib/Slicer-5.8/qt-scripted-modules/DeCA.py”, line 599, in onDCApplyButton</em></p>
<p><em>self.atlasModel, self.atlasLMs = self.generateNewAtlas(removeScaleOption, self.logInfoDC)</em></p>
<p><em>File “C:/Software/Slicer_5_8_1/slicer.org/Extensions-33241/DenseCorrespondenceAnalysis/lib/Slicer-5.8/qt-scripted-modules/DeCA.py”, line 557, in generateNewAtlas</em></p>
<p><em>atlasModel, atlasLMs = logic.runMean(self.folderNames[‘tempAlignedLMs’], self.folderNames[‘tempAlignedModels’])</em></p>
<p><em>File “C:/Software/Slicer_5_8_1/slicer.org/Extensions-33241/DenseCorrespondenceAnalysis/lib/Slicer-5.8/qt-scripted-modules/DeCA.py”, line 883, in runMean</em></p>
<p><em>[denseCorrespondenceGroup, closestToMeanIndex] = self.denseCorrespondence(landmarks, models)</em></p>
<p><em>File “C:/Software/Slicer_5_8_1/slicer.org/Extensions-33241/DenseCorrespondenceAnalysis/lib/Slicer-5.8/qt-scripted-modules/DeCA.py”, line 1103, in denseCorrespondence</em></p>
<p><em>baseLandmarks = originalLandmarks.GetBlock(baseIndex).GetPoints()</em></p>
<p><em><strong>AttributeError: ‘NoneType’ object has no attribute ‘GetPoints’</strong></em></p>
<p>In the 3D viewer only the 230 landmarks are shown, and 4 empty folders were created on<br>
the hard disk (DeCA output folder).</p>
<p>Since the data (model &amp; landmarks) are already “alinged” by DeCAL, there is “nothing” left to do for the DeCA alignment &amp; atlas generation step which might give rise to the issue?</p>
<p>The previous version of DeCA was not able to handle a DeCAL generated atlas (load atlas &amp; peform shape analysis) BUT it was yesterday possible to use DeCA with the DeCAL aligned models &amp; LMs without the atlas (generate atlas &amp; perform shape analysis).</p>
<p>Could you try the latest version with the data I have sent you via dropbox?</p>
<p>THANKS!</p>
<p>Best,<br>
Markus</p>

---

## Post #12 by @muratmaga (2025-07-29 14:54 UTC)

<p>I am a little confused from your description here. It is not clear to me whether this error is generated by the data you shared with me or your new dataset.</p>
<p>I can run the dataset you shared with me successfully and visualize results with the updated data.</p>
<p>If you are still having issues, please share the “raw data” (original models and lms that you are trying to use with DeCA, not aligned ones from DeCAL).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f839c9e9cea789f886ffaf9a357766b7745ef30.jpeg" data-download-href="/uploads/short-url/2df8CqabTR8PQ9tqv31FiKAJKKY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f839c9e9cea789f886ffaf9a357766b7745ef30_2_495x500.jpeg" alt="image" data-base62-sha1="2df8CqabTR8PQ9tqv31FiKAJKKY" width="495" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f839c9e9cea789f886ffaf9a357766b7745ef30_2_495x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f839c9e9cea789f886ffaf9a357766b7745ef30_2_742x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f839c9e9cea789f886ffaf9a357766b7745ef30_2_990x1000.jpeg 2x" data-dominant-color="CBBED3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1226×1237 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @smrolfe (2025-07-29 18:42 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="6" data-topic="43742">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>I use DECA since in addition it offers to “adjust” the numbers of sampling<br>
points (semiLMs), kind of control.</p>
</blockquote>
</aside>
<p>Specifying semi-landmarks in DeCA is a new feature that is not currently supported in the released extension. If this function is important for your workflow, you’ll need to install a development version that includes it.</p>
<p>As things stand, running DeCAL followed by DeCA will not yield different results. That said, the error you’re encountering should be possible to track down. If you can reproduce it using the dataset you shared earlier and provide the steps, I’d be happy to help debug it.</p>

---

## Post #14 by @MrMarkus (2025-07-30 08:33 UTC)

<p>Hi,</p>
<p>finally got it!<img src="https://emoji.discourse-cdn.com/twitter/partying_face.png?v=14" title=":partying_face:" class="emoji" alt=":partying_face:" loading="lazy" width="20" height="20"></p>
<p>Troubles arise once one is working with the “merged” landmarks. Probably the<br>
ambiguity of the “label” causes the mentioned error: <em><strong>AttributeError: ‘NoneType’ object has no attribute ‘GetPoints’.</strong></em></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be0c8f75e8d0929e12cbcc3bae266115bba146f5.png" data-download-href="/uploads/short-url/r7fD3lwvRsFWpHDOUz9falFu8MR.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be0c8f75e8d0929e12cbcc3bae266115bba146f5.png" alt="grafik" data-base62-sha1="r7fD3lwvRsFWpHDOUz9falFu8MR" width="349" height="340"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">349×340 6.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The “Semi”Lms start with “label” from “0”, the “Fixed”LMs start with “label” from “1”-”20”, so there<br>
are points with the “label” 1 - 20 twice. Probably this ambiguity causes the troubles?</p>
<p>Now I know this and only use DeCA with the  semiLandmarks generated by DeCAL WITHOUT the initial fixed landmarks.</p>
<p>This workflow works now fine for me!</p>
<p>THANKS a LOT for YOUR SUPPORT! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #15 by @muratmaga (2025-07-30 15:48 UTC)

<p>So to be clear, DeCA is focused on visualizing each individual’s shape difference from the template. DeCAL is an automated landmarking tool (that allows you to combine fixed landmarks with surface based semi-landmarks through a template apporach). If your goal is to look at groupwise differences, you should run the DeCAL generated dense landmark set with GPA module and compare the means of each group to see what the differences are…</p>
<p>(or at the minimum look at the PCA warps, to see if there are clear separations between two groups you are analyzing).</p>

---
