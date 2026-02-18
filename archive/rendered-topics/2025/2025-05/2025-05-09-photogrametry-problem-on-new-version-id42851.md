# photogrametry problem on new version

**Topic ID**: 42851
**Date**: 2025-05-09
**URL**: https://discourse.slicer.org/t/photogrametry-problem-on-new-version/42851

---

## Post #1 by @akaya (2025-05-09 13:37 UTC)

<p>Hello everyone</p>
<p>I hope everything is fine. I tried and used photogametry in the previous 3d slicer version, there was no problem, but I installed the new version (5.8.1), I open it, but it does not open when taking pictures and gives the script these errors written below. I looked at Google but I couldn’t solve it. I don’t know if this problem is the connection or the lack of files. I would appreciate your help.</p>
<p>All the best</p>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>Using CPU for SAM.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>Traceback (most recent call last):</p>
<p>File “/Users/alaettinkaya/foto3d/SlicerPhotogrammetry-master/Photogrammetry/Photogrammetry.py”, line 1188, in onImageSetSelected</p>
<p>self.restoreSetState(self.currentSet)</p>
<p>File “/Users/alaettinkaya/foto3d/SlicerPhotogrammetry-master/Photogrammetry/Photogrammetry.py”, line 1277, in restoreSetState</p>
<p>self.refreshButtonStatesBasedOnCurrentState()</p>
<p>File “/Users/alaettinkaya/foto3d/SlicerPhotogrammetry-master/Photogrammetry/Photogrammetry.py”, line 1362, in refreshButtonStatesBasedOnCurrentState</p>
<p>st = self.imageStates[self.currentImageIndex][“state”]</p>
<p>KeyError: 0</p>
<p>Traceback (most recent call last):</p>
<p>File “/Users/alaettinkaya/foto3d/SlicerPhotogrammetry-master/Photogrammetry/Photogrammetry.py”, line 1133, in onProcessFoldersClicked</p>
<p>self.restoreSetState(self.currentSet)</p>
<p>File “/Users/alaettinkaya/foto3d/SlicerPhotogrammetry-master/Photogrammetry/Photogrammetry.py”, line 1277, in restoreSetState</p>
<p>self.refreshButtonStatesBasedOnCurrentState()</p>
<p>File “/Users/alaettinkaya/foto3d/SlicerPhotogrammetry-master/Photogrammetry/Photogrammetry.py”, line 1362, in refreshButtonStatesBasedOnCurrentState</p>
<p>st = self.imageStates[self.currentImageIndex][“state”]</p>
<p>KeyError: 0</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00dc750) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e88b00) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageMapToColors (0x7fbee00e9f30) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageShiftScale (0x7fbee00f4740) has 0 connections but is not optional.</p>
<p>[VTK] Input port 0 of algorithm vtkImageRGBToHSI (0x600003e8b000) has 0 connections but is not optional.</p>

---

## Post #2 by @muratmaga (2025-05-09 15:11 UTC)

<p><a class="mention" href="/u/akaya">@akaya</a><br>
Based on the log files you shared, I think you are using the locally cloned version of the repo. Depending on when you downloaded or cloned the repo, I would make sure you are running the latest version. Extension is now part of the extension catalogue.</p>
<p>But more importantly, from the paths, i think you are using a Mac. We do NOT support Mac or windows officially, due to the challenges of installing all other necessary libraries (such as docker) and configuring them. Only Linux is supported. But if you are up for challenge, you can follow the instructions from this link to try:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/SlicerPhotogrammetry?tab=readme-ov-file#running-locally-on-your-computer">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerPhotogrammetry?tab=readme-ov-file#running-locally-on-your-computer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/c5880eca324eded0ba9be092e7e60f77/SlicerMorph/SlicerPhotogrammetry?tab=readme-ov-file#running-locally-on-your-computer" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/SlicerPhotogrammetry?tab=readme-ov-file#running-locally-on-your-computer" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerPhotogrammetry</a></h3>

    <p><span class="github-repo-description">Contribute to SlicerMorph/SlicerPhotogrammetry development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Also, make sure you are using a preview version. I don’t think we tested extensively with the stable.</p>
<p>The easiest way to run Photogrammetry extension is actually to use it through MorphoCloud:<br>
<a href="https://instances.morpho.cloud" rel="noopener nofollow ugc">https://instances.morpho.cloud</a> It will probably be faster too, thanks to large GPUs in these systems.</p>

---

## Post #3 by @muratmaga (2025-05-09 15:22 UTC)

<p><a class="mention" href="/u/akaya">@akaya</a></p>
<p>On my Mac with a recent Preview, everything works fine up to running ODM. I don’t have docker on my mac, so that part I can’t test… But if you have docker installed correctly, the rest should be working:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ade6f8bf3ba105b904c5a0a3f8fcf6957e259679.jpeg" data-download-href="/uploads/short-url/oOpskl2qqI3YcatRhf2hwkF7zPX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade6f8bf3ba105b904c5a0a3f8fcf6957e259679_2_572x500.jpeg" alt="image" data-base62-sha1="oOpskl2qqI3YcatRhf2hwkF7zPX" width="572" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade6f8bf3ba105b904c5a0a3f8fcf6957e259679_2_572x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade6f8bf3ba105b904c5a0a3f8fcf6957e259679_2_858x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade6f8bf3ba105b904c5a0a3f8fcf6957e259679_2_1144x1000.jpeg 2x" data-dominant-color="9C9898"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1412×1233 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also as a comparison, using the CPU and the lowest resolution SAM model, on my Mac estimated processing time for 64 photos is 25 minutes. On MorphoCloud the same 64 photos would take 2-3 minutes. There are 320 photos in this set.</p>
<p>Same with the 3D model reconstruction… So you will really benefit from using it on the cloud.</p>

---
