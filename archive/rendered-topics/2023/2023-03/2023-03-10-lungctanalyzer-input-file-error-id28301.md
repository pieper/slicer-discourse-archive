# LungCTAnalyzer input file error

**Topic ID**: 28301
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/lungctanalyzer-input-file-error/28301

---

## Post #1 by @JasonYangchen (2023-03-10 20:19 UTC)

<p>CUDA available: True<br>
3Dslicer5.0.3</p>
<p>Error occurs when I use my patient data<br>
RuntimeError: unexpected EOF, expected 10008318 more bytes. The file might be corrupted.</p>
<p>How con I slove this problem?<br>
thanks</p>

---

## Post #2 by @rbumm (2023-03-11 01:38 UTC)

<p>Please update your 3D Slicer version to version 5.2.2 stable. Does the error persist?</p>
<p>Please describe in more detail how you load your data. Is this DICOM, a *.nrrd file, or a *.mrb file?<br>
Have you run Lung CT Segmenter before Lung CT Analyzer?</p>
<p>It would be helpful if you could provide a screenshot of the error message and/or a log file. It could also help if you would provide the Lung CT Analyzer version number.</p>

---

## Post #3 by @JasonYangchen (2023-03-11 09:00 UTC)

<p>I have updated the version to 5.2.2 stable version, pythoch1.13.1+cu117, Chest_ Imaging_ Platform version: fccea26 (2023-02-22), LungCTAnalyzer version: 3ae8061 (2023-03-10), but the error still exists.<br>
I want to use the Lung CT Segmenter plug-in, which is available when using lungmask R231, and use lungmask LTRCLobes_ R231 reported an error<br>
The imported patient file is in. dcm format, and the screenshot of Python Console is as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08ce747c506c7579c502264f48e4500356b60959.png" data-download-href="/uploads/short-url/1fU99p7a46DgQvWU33fdeLM2tjX.png?dl=1" title="屏幕截图 2023-03-11 170013" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08ce747c506c7579c502264f48e4500356b60959_2_690x388.png" alt="屏幕截图 2023-03-11 170013" data-base62-sha1="1fU99p7a46DgQvWU33fdeLM2tjX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08ce747c506c7579c502264f48e4500356b60959_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08ce747c506c7579c502264f48e4500356b60959_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08ce747c506c7579c502264f48e4500356b60959_2_1380x776.png 2x" data-dominant-color="E9E4E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 170013</span><span class="informations">1920×1080 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @rbumm (2023-03-11 09:53 UTC)

<p>Thank you. In this case, the AI tool “lungmask LTRCLobes_R231” generates this exception.</p>
<p>Is it correct to assume that you imported your  DCM data via the DICOM database → “Import DICOM data”?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f97c875a64a56c79ca85ba1130047f08ff7f839c.png" alt="image" data-base62-sha1="zB3GSTAhM5IaD97oYe85pnLp9XC" width="288" height="67"></p>
<p>Could you please do an additional test:<br>
Close 3D Slicer, reopen it and load the CTChest sample dataset</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcace536938d7aac037fe5fa427c462010a0fdde.png" alt="image" data-base62-sha1="A3gKrMk92H3S1nXYUATWYLjVQv4" width="506" height="327"></p>
<p>Process Lung CT Segmenter with lungmask AI just to make sure the basic installation works.</p>

---

## Post #5 by @JasonYangchen (2023-03-11 10:01 UTC)

<p>Yes, but there are also problems when using the test lung CT<br>
Unfortunately, I was wondering if there was something wrong with my installation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f00d7d94701772777511241ede27d3bf29814a95.png" data-download-href="/uploads/short-url/yfBuLEYVikrDG9TTNy3766vr9Bz.png?dl=1" title="屏幕截图 2023-03-11 175910" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00d7d94701772777511241ede27d3bf29814a95_2_690x388.png" alt="屏幕截图 2023-03-11 175910" data-base62-sha1="yfBuLEYVikrDG9TTNy3766vr9Bz" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00d7d94701772777511241ede27d3bf29814a95_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00d7d94701772777511241ede27d3bf29814a95_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f00d7d94701772777511241ede27d3bf29814a95_2_1380x776.png 2x" data-dominant-color="D6D1D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 175910</span><span class="informations">1920×1080 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @rbumm (2023-03-11 11:39 UTC)

<p>Please provide system information:<br>
Processor, memory, GPU brand and model, dedicated video RAM</p>

---

## Post #7 by @JasonYangchen (2023-03-11 11:54 UTC)

<p>OK, I reinstalled 3dslicer and used CTChest sample dataset for testing. The first error is shown in the following screenshot<br>
My system CPU: 11th Gen Intel (R) Core ™ i5-11400H @ 2.70GHz 2.69 GHz<br>
Graphics card: NVIDIA GeForce RTX 3050 Laptop<br>
Dedicated video RAM: only 4GB, I know it may not meet the minimum requirement of 6GB, but I still want to try this plug-in. Is there any way?<br>
Could there be an error updating my pip?<br>
ImportError: DLL load failed while importing _ Ufuncs: The specified module cannot be found.<br>
Thank you very much for answering my questions<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bca19dcb3ee3885681e76c4b03a9969870798ae4.png" data-download-href="/uploads/short-url/qUI1BJUr0zemlpnVV0nZO7S3u04.png?dl=1" title="屏幕截图 2023-03-11 193838" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca19dcb3ee3885681e76c4b03a9969870798ae4_2_690x388.png" alt="屏幕截图 2023-03-11 193838" data-base62-sha1="qUI1BJUr0zemlpnVV0nZO7S3u04" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca19dcb3ee3885681e76c4b03a9969870798ae4_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca19dcb3ee3885681e76c4b03a9969870798ae4_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bca19dcb3ee3885681e76c4b03a9969870798ae4_2_1380x776.png 2x" data-dominant-color="DDD8DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 193838</span><span class="informations">1920×1080 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55254da054196fa30ead22831fb8da87b54db878.png" data-download-href="/uploads/short-url/c9evq51ijhcNyUmWpnjHQkZuvgY.png?dl=1" title="屏幕截图 2023-03-11 195847" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55254da054196fa30ead22831fb8da87b54db878_2_690x388.png" alt="屏幕截图 2023-03-11 195847" data-base62-sha1="c9evq51ijhcNyUmWpnjHQkZuvgY" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55254da054196fa30ead22831fb8da87b54db878_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55254da054196fa30ead22831fb8da87b54db878_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55254da054196fa30ead22831fb8da87b54db878_2_1380x776.png 2x" data-dominant-color="EDE8E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 195847</span><span class="informations">1920×1080 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @rbumm (2023-03-11 12:29 UTC)

<p>Please restart 3D Slicer (“run as Administrator”), type</p>
<pre><code class="lang-auto">slicer.util.pip_install("lungmask")
</code></pre>
<p>into the Python Console and post the output.</p>

---

## Post #9 by @JasonYangchen (2023-03-11 12:42 UTC)

<p>Thank you. It seems that “lungmask” has been installed, but the same error may be reported after that:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5536e6507526f48ab43eb80fe871984b27c6ef.png" data-download-href="/uploads/short-url/8sSJZMbg8PxuIwZJZTRnk4r5FIr.png?dl=1" title="屏幕截图 2023-03-11 203937" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5536e6507526f48ab43eb80fe871984b27c6ef.png" alt="屏幕截图 2023-03-11 203937" data-base62-sha1="8sSJZMbg8PxuIwZJZTRnk4r5FIr" width="690" height="422" data-dominant-color="F1F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 203937</span><span class="informations">1260×772 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0aa2b6cb0fd41517c91c415f01e5f98cb02c4df.png" data-download-href="/uploads/short-url/yl1b8AgBT9tVtku9pKpk9b3dtrV.png?dl=1" title="屏幕截图 2023-03-11 204022" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0aa2b6cb0fd41517c91c415f01e5f98cb02c4df_2_690x388.png" alt="屏幕截图 2023-03-11 204022" data-base62-sha1="yl1b8AgBT9tVtku9pKpk9b3dtrV" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0aa2b6cb0fd41517c91c415f01e5f98cb02c4df_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0aa2b6cb0fd41517c91c415f01e5f98cb02c4df_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0aa2b6cb0fd41517c91c415f01e5f98cb02c4df_2_1380x776.png 2x" data-dominant-color="E5E1E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 204022</span><span class="informations">1920×1080 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
RuntimeError: unexpected EOF, expected 10008318 more bytes. The file might be corrupted.<br>
Everything goes back to the previous question<br>
I’m going to crash. Thank you very much for answering my questions all the time<br>
What should I do next？</p>

---

## Post #10 by @rbumm (2023-03-11 12:45 UTC)

<p>Try running “lungmask R231”. Same result?</p>

---

## Post #11 by @JasonYangchen (2023-03-11 12:50 UTC)

<p>“Lungmask R231” can always operate normally<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e497fed221a3303b187ee2e72938abb38c9748d4.png" data-download-href="/uploads/short-url/wCevJI9JimXe7CEAoPFdL9eSGoc.png?dl=1" title="屏幕截图 2023-03-11 204912" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e497fed221a3303b187ee2e72938abb38c9748d4_2_690x388.png" alt="屏幕截图 2023-03-11 204912" data-base62-sha1="wCevJI9JimXe7CEAoPFdL9eSGoc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e497fed221a3303b187ee2e72938abb38c9748d4_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e497fed221a3303b187ee2e72938abb38c9748d4_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e497fed221a3303b187ee2e72938abb38c9748d4_2_1380x776.png 2x" data-dominant-color="C8C4C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2023-03-11 204912</span><span class="informations">1920×1080 503 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @jamesobutler (2023-03-11 12:52 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Your code specifies to install the latest of the lungmask python module.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/d613598f8b97015dbb78b3d2dc06294292074247/LungCTSegmenter/LungCTSegmenter.py#L2135">
  <header class="source">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/d613598f8b97015dbb78b3d2dc06294292074247/LungCTSegmenter/LungCTSegmenter.py#L2135" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/d613598f8b97015dbb78b3d2dc06294292074247/LungCTSegmenter/LungCTSegmenter.py#L2135" target="_blank" rel="noopener nofollow ugc">rbumm/SlicerLungCTAnalyzer/blob/d613598f8b97015dbb78b3d2dc06294292074247/LungCTSegmenter/LungCTSegmenter.py#L2135</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="2125" style="counter-reset: li-counter 2124 ;">
          <li>        self.showStatusMessage('Uninstalling lungmask AI ...')
</li>
          <li>        slicer.util.pip_uninstall("lungmask")
</li>
          <li>        # Slicer must be restarted for this to take effect.
</li>
          <li>        slicer.util.restart()
</li>
          <li># Import the required libraries
</li>
          <li>self.showStatusMessage(' Importing lungmask AI ...')
</li>
          <li>try:
</li>
          <li>    import lungmask
</li>
          <li>except ModuleNotFoundError:
</li>
          <li>    self.showStatusMessage(' Installing lungmask AI ...')
</li>
          <li class="selected">    lungmaskPackage = "https://github.com/JoHof/lungmask/archive/master.zip"
</li>
          <li>    slicer.util.pip_install(lungmaskPackage)
</li>
          <li>    import lungmask
</li>
          <li>
</li>
          <li>from lungmask import mask
</li>
          <li>                   
</li>
          <li>inputVolumeSitk = sitkUtils.PullVolumeFromSlicer(self.inputVolume)
</li>
          <li>if self.engineAI == "lungmask R231":
</li>
          <li>    self.showStatusMessage('Creating lungs with lungmask AI ...')
</li>
          <li>    model = mask.get_model('unet','R231')
</li>
          <li>    segmentation_np = mask.apply(inputVolumeSitk, model)
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The lungmask python module appears to require a specific version of Simple ITK (1.2.4)?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/requirements.txt#L7">
  <header class="source">

      <a href="https://github.com/JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/requirements.txt#L7" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/requirements.txt#L7" target="_blank" rel="noopener nofollow ugc">JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/requirements.txt#L7</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>pydicom==1.3.0</li>
          <li>numpy==1.22.0</li>
          <li>scikit_image==0.15.0</li>
          <li>torch==1.2.0</li>
          <li>torchvision==0.4.0a0+6b959ee</li>
          <li>scipy==1.3.1</li>
          <li class="selected">SimpleITK==1.2.4</li>
          <li>skimage==0.0</li>
          <li>fill_voids</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However uninstalling Slicer’s SimpleITK version and replacing it with an older version is not supported currently.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6711">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6711" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6711" target="_blank" rel="noopener nofollow ugc">Slicer's embedded SimpleITK can be removed by pip</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-30" data-time="03:18:50" data-timezone="UTC">03:18AM - 30 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

When installing a package that requires a specific SimpleITK versi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">on (e.g., TotalSegmentator requires SimpleITK==2.0.2) then installation of that package may replace Slicer's SimpleITK.

The new SimpleITK package mostly works, but the ITK IO plugins that Slicer provides (e.g., for in-memory file transfer between Slicer and ITK) don't work anymore.

## Steps to reproduce

Run `pip_install('TotalSegmentator')`.
Slicer's SimpleITK is uninstalled and SimpleITK-2.0.2 is installed.

## Expected behavior

Slicer's SimpleITK should not be uninstalled.

## Environment
- Slicer version: Slicer-5.2.1
- Operating system: Windows 11</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @rbumm (2023-03-11 12:55 UTC)

<p>If “lungmask R231” runs normally it indicates that hardware limitations, most probable the limited dedicated video RAM that you have available on your system, could cause the error when using “lungmask LCTRLobes_R231”.</p>

---

## Post #15 by @JasonYangchen (2023-03-11 13:15 UTC)

<p>Indeed, it seems that this is the key point of the problem. Is there any other solution for me to use “lungmask LCTRLobes_R231”?</p>

---

## Post #16 by @JasonYangchen (2023-03-11 13:16 UTC)

<p>I thought so at the beginning, but under the existing hardware conditions, is it possible for me to try and experience “lungmask LTRCLobes_R231”?<br>
As [jamesobutler]said, it may be the reason for the Simple ITK version? Will it help me switch to the old version of 3dslicer?</p>

---

## Post #17 by @rbumm (2023-03-11 13:22 UTC)

<p>Thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>When I create a fresh 3D Slicer install and just do:</p>
<pre><code class="lang-auto">slicer.util.pip_install("https://github.com/JoHof/lungmask/archive/master.zip")
</code></pre>
<p>the SimpleITK requirement seems to be “already satisfied” and not getting downgraded?</p>
<pre><code class="lang-auto">Collecting https://github.com/JoHof/lungmask/archive/master.zip
  Using cached https://github.com/JoHof/lungmask/archive/master.zip
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: pydicom in c:\users\rudol\appdata\local\na-mic\slicer 5.2.2_2\lib\python\lib\site-packages (from lungmask==0.2.13) (2.3.1)
Requirement already satisfied: numpy in c:\users\rudol\appdata\local\na-mic\slicer 5.2.2_2\lib\python\lib\site-packages (from lungmask==0.2.13) (1.23.4)
Collecting torch
  Using cached torch-1.13.1-cp39-cp39-win_amd64.whl (162.5 MB)
Requirement already satisfied: scipy in c:\users\rudol\appdata\local\na-mic\slicer 5.2.2_2\lib\python\lib\site-packages (from lungmask==0.2.13) (1.9.2)
Requirement already satisfied: SimpleITK in c:\users\rudol\appdata\local\na-mic\slicer 5.2.2_2\lib\python\lib\site-packages (from lungmask==0.2.13) (2.2.0rc2.dev368)
Collecting tqdm
  Using cached tqdm-4.65.0-py3-none-any.whl (77 kB)
Collecting scikit-image
  Using cached scikit_image-0.20.0-cp39-cp39-win_amd64.whl (23.9 MB)
Collecting fill_voids
  Using cached fill_voids-2.0.3-cp39-cp39-win_amd64.whl (178 kB)
Collecting fastremap
  Using cached fastremap-1.13.4-cp39-cp39-win_amd64.whl (507 kB)
Collecting networkx&gt;=2.8
  Using cached networkx-3.0-py3-none-any.whl (2.0 MB)
Collecting imageio&gt;=2.4.1
  Using cached imageio-2.26.0-py3-none-any.whl (3.4 MB)
Requirement already satisfied: packaging&gt;=20.0 in c:\users\rudol\appdata\local\na-mic\slicer 5.2.2_2\lib\python\lib\site-packages (from scikit-image-&gt;lungmask==0.2.13) (23.0)
Collecting PyWavelets&gt;=1.1.1
  Using cached PyWavelets-1.4.1-cp39-cp39-win_amd64.whl (4.2 MB)
Collecting tifffile&gt;=2019.7.26
  Using cached tifffile-2023.2.28-py3-none-any.whl (216 kB)
Collecting lazy_loader&gt;=0.1
  Using cached lazy_loader-0.1-py3-none-any.whl (8.6 kB)
Collecting scipy
  Using cached scipy-1.9.1-cp39-cp39-win_amd64.whl (38.6 MB)
Requirement already satisfied: pillow&gt;=9.0.1 in c:\users\rudol\appdata\local\na-mic\slicer 5.2.2_2\lib\python\lib\site-packages (from scikit-image-&gt;lungmask==0.2.13) (9.4.0)
Collecting typing-extensions
  Using cached typing_extensions-4.5.0-py3-none-any.whl (27 kB)
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Building wheels for collected packages: lungmask
  Building wheel for lungmask (setup.py): started
  Building wheel for lungmask (setup.py): finished with status 'done'
  Created wheel for lungmask: filename=lungmask-0.2.13-py3-none-any.whl size=17476 sha256=b49b8d28794a12f0b903dbbe61639249da51ff2b93cab977ee251d4187200a8c
  Stored in directory: C:\Users\rudol\AppData\Local\Temp\pip-ephem-wheel-cache-fhpk5mbp\wheels\83\9e\4b\d1090037a85238e9974cad92f6ed6755ab08e7227327dbfc6b
Successfully built lungmask
Installing collected packages: typing-extensions, tifffile, scipy, PyWavelets, networkx, lazy_loader, imageio, fastremap, colorama, tqdm, torch, scikit-image, fill_voids, lungmask
  WARNING: The scripts lsm2bin.exe, tiff2fsspec.exe, tiffcomment.exe and tifffile.exe are installed in 'C:\Users\rudol\AppData\Local\NA-MIC\Slicer 5.2.2_2\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: scipy
    Found existing installation: scipy 1.9.2
    Uninstalling scipy-1.9.2:
      Successfully uninstalled scipy-1.9.2
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'C:\\Users\\rudol\\AppData\\Local\\NA-MIC\\Slicer 5.2.2_2\\lib\\Python\\Lib\\site-packages\\~cipy\\_lib\\_ccallback_c.cp39-win_amd64.pyd'
Consider using the `--user` option or check the permissions.


[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
</code></pre>

---

## Post #18 by @rbumm (2023-03-11 13:31 UTC)

<p>It will not help to switch to an old version of Slicer. “lungmask LCTRLobe R231” works fine on two test systems (one with 6 GB video RAM, one with 8 GB dedicated video RAM) - even that is the low limit for the AI tools. You will probably need to upgrade the hardware or switch to a different computer.</p>

---

## Post #19 by @JasonYangchen (2023-03-11 13:38 UTC)

<p>Unfortunately, I will try another device<br>
Thank you very much for answering my questions<br>
Have a good day.</p>

---

## Post #20 by @jamesobutler (2023-03-11 15:00 UTC)

<p>Thanks for checking that. Yes, it appears setup.py specifies a versionless SimpleITK which is good. It is just that the requirements.txt in that repo appears outdated.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/setup.py#L26">
  <header class="source">

      <a href="https://github.com/JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/setup.py#L26" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/setup.py#L26" target="_blank" rel="noopener nofollow ugc">JoHof/lungmask/blob/0fe26b940aeff52196e34909d265c1d15488867c/setup.py#L26</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="16" style="counter-reset: li-counter 15 ;">
          <li>    entry_points={</li>
          <li>        'console_scripts': [</li>
          <li>            'lungmask = lungmask.__main__:main'</li>
          <li>        ]</li>
          <li>    },</li>
          <li>    install_requires=[</li>
          <li>        'pydicom',</li>
          <li>        'numpy',</li>
          <li>        'torch',</li>
          <li>        'scipy',</li>
          <li class="selected">        'SimpleITK',</li>
          <li>        'tqdm',</li>
          <li>        'scikit-image',</li>
          <li>        'fill_voids'</li>
          <li>    ],</li>
          <li>    classifiers=[</li>
          <li>        "Programming Language :: Python :: 3",</li>
          <li>        "Operating System :: OS Independent"</li>
          <li>    ],</li>
          <li>    python_requires='&gt;=3.6',</li>
          <li>)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #21 by @JasonYangchen (2023-03-18 09:34 UTC)

<p>I made a new attempt<br>
I tried a 1660ti graphics card with 6GB of independent graphics memory, running on version 5.2.2 of 3DSlicer, and was unable to call CUDA. However, CUDA is available on version 5.0.3 of 3DSlicer, and it seems that the graphics memory has exploded.</p>

---
