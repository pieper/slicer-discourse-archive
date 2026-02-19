---
topic_id: 40580
title: "Version 5 7 0 Dentalsegmentator Problem"
date: 2024-12-09
url: https://discourse.slicer.org/t/40580
---

# Version 5.7.0 - DentalSegmentator - problem

**Topic ID**: 40580
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/version-5-7-0-dentalsegmentator-problem/40580

---

## Post #1 by @Ender (2024-12-09 14:41 UTC)

<p>I installed version 5.7.0. After reading the dcom file, I wanted to create DentalSegmentator. After pressing the “Apply” button and waiting a while, the following message appeared in the log.</p>
<p>2024/12/09 10:53:29.712 :: nnUNet is already installed (2.5.1) and compatible with requested version (nnunetv2).</p>
<p>2024/12/09 10:53:29.720 :: Downloading model weights…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a623bdf1576a68f6b6e4e32548b44e3315c047b7.jpeg" data-download-href="/uploads/short-url/nHJPT2r0htElFtoaBuBXKLnGbKD.jpeg?dl=1" title="File" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a623bdf1576a68f6b6e4e32548b44e3315c047b7.jpeg" alt="File" data-base62-sha1="nHJPT2r0htElFtoaBuBXKLnGbKD" width="495" height="188"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">File</span><span class="informations">495×188 17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Request for help</p>

---

## Post #2 by @jamesobutler (2024-12-11 12:22 UTC)

<p>DentalSegmentator has section about failed to download model weights. See the link below:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/2b4894b5c52b26bd0d59c73a8a14b2f7/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights" class="thumbnail">

  <h3><a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#failed-to-download--find-weights" target="_blank" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Specific code involved though the error message never display(?) so maybe not a problem with the download.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/gaudot/SlicerDentalSegmentator/blob/7eaa69532e59d468cac6a28ecdd6c6218107eccd/DentalSegmentator/DentalSegmentatorLib/PythonDependencyChecker.py#L125">
  <header class="source">

      <a href="https://github.com/gaudot/SlicerDentalSegmentator/blob/7eaa69532e59d468cac6a28ecdd6c6218107eccd/DentalSegmentator/DentalSegmentatorLib/PythonDependencyChecker.py#L125" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/gaudot/SlicerDentalSegmentator/blob/7eaa69532e59d468cac6a28ecdd6c6218107eccd/DentalSegmentator/DentalSegmentatorLib/PythonDependencyChecker.py#L125" target="_blank" rel="noopener nofollow ugc">gaudot/SlicerDentalSegmentator/blob/7eaa69532e59d468cac6a28ecdd6c6218107eccd/DentalSegmentator/DentalSegmentatorLib/PythonDependencyChecker.py#L125</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="115" style="counter-reset: li-counter 114 ;">
          <li>def downloadWeights(self, progressCallback) -&gt; bool:</li>
          <li>    """</li>
          <li>    Removes the weight folder and tries to download the weights from the GitHub page.</li>
          <li>    If an internet connection is not available, keeps the current weights unchanged.</li>
          <li></li>
          <li>    :returns: True if download was successful. False in case of no internet or failure during download.</li>
          <li>    """</li>
          <li>    import shutil</li>
          <li>    import requests</li>
          <li></li>
          <li class="selected">    progressCallback("Downloading model weights...")</li>
          <li>    if not self.hasInternetConnectionF():</li>
          <li>        self.errorDisplay(</li>
          <li>            "Failed to download weights (no internet connection). "</li>
          <li>            "Please retry or manually install them to proceed.\n"</li>
          <li>            "To manually install the weights, please refer to the documentation here :\n"</li>
          <li>            "https://github.com/gaudot/SlicerDentalSegmentator",</li>
          <li>        )</li>
          <li>        return False</li>
          <li></li>
          <li>    if self.destWeightFolder.exists():</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>cc <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a></p>

---

## Post #3 by @Thibault_Pelletier (2024-12-11 15:50 UTC)

<p>Hi <a class="mention" href="/u/ender">@Ender</a>,</p>
<p>Your problem is most likely related to nnUNet install error on Python 3.9 which have been also reported here : <a href="https://discourse.slicer.org/t/dental-segmantator/40519/2" class="inline-onebox">Dental segmantator - #2 by jamesobutler</a></p>
<p>You should have more information on the actual error in the Python console.</p>
<p>Best,<br>
Thibault</p>

---
