---
topic_id: 4122
title: "Vissim Cochlea Tools Extension Is Now Public"
date: 2018-09-15
url: https://discourse.slicer.org/t/4122
---

# VisSim Cochlea Tools extension is now public

**Topic ID**: 4122
**Date**: 2018-09-15
**URL**: https://discourse.slicer.org/t/vissim-cochlea-tools-extension-is-now-public/4122

---

## Post #1 by @brhoom (2018-09-15 14:16 UTC)

<p>I added video tutorials on how to <a href="https://www.youtube.com/watch?v=oRQ767ojS9o&amp;t=159s" rel="nofollow noopener">register and fuse</a> and <a href="https://www.youtube.com/watch?v=A_mTcT3eT_c&amp;t=31s" rel="nofollow noopener">segment</a> cochlea multi-modal images using our <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea" rel="nofollow noopener">VisSim Tools extension</a> that uses <a href="https://github.com/SuperElastix/elastix" rel="nofollow noopener">elastix toolbox</a> as well. The source code can be found <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea" rel="nofollow noopener">here</a>.<br>
Sample cochlea datasets are also shared and can be downloaded using “Data Store”<br>
module.</p>
<p>This is still a beta version and more enhancement will be added to both source code and videos.</p>

---

## Post #2 by @brhoom (2018-09-20 17:54 UTC)

<p>The <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerCochlea.s4ext" rel="nofollow noopener">SlicerCochlea</a> extension is already merged few days ago but it does not appear in the extension manager. Is there something wrong?</p>

---

## Post #3 by @torquil (2018-10-24 13:53 UTC)

<p>It does appear in the extension manager for me with the current nightly build on Linux (4.11.0-2018-10-23 r27518), but it doesn’t seem to work. I’m getting the following error messsage in the terminal window where I start Slicer:</p>
<pre><code class="lang-auto">$ slicer
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/torquil/.config/NA-MIC/Extensions-27518/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules/CochleaReg.py", line 24, in &lt;module&gt;
    import Tkinter, tkFileDialog
ImportError: No module named Tkinter
loadSourceAsModule - Failed to load file "/home/torquil/.config/NA-MIC/Extensions-27518/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules/CochleaReg.py"  as module "CochleaReg" !
Fail to instantiate module  "CochleaReg"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/torquil/.config/NA-MIC/Extensions-27518/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules/CochleaSeg.py", line 25, in &lt;module&gt;
    import Tkinter, tkFileDialog
ImportError: No module named Tkinter
loadSourceAsModule - Failed to load file "/home/torquil/.config/NA-MIC/Extensions-27518/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules/CochleaSeg.py"  as module "CochleaSeg" !
Fail to instantiate module  "CochleaSeg"
</code></pre>
<p>When it works I will be happy to try it.</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #4 by @brhoom (2018-10-24 14:45 UTC)

<p>Thanks for interesting in our work.</p>
<p>I tested it on Slicer 4.81. I will update it and test it on the recent versions 4.10 and 4.11 next week.</p>
<p>Not sure why Tkinter does not work, maybe Slicer 11 uses python 3? I just updated the code, hopefully, this problem is fixed in the next build.</p>

---

## Post #5 by @jamesobutler (2018-10-24 15:15 UTC)

<p><a class="mention" href="/u/brhoom">@brhoom</a>  Slicer is not using python 3 yet, but you might want to review the comment in this thread <a href="https://discourse.slicer.org/t/should-we-do-something-about-em-segmenter/4382">Should we do something about EM segmenter?</a>.  TCL support was recently disabled in Slicer.</p>

---

## Post #6 by @brhoom (2018-10-24 15:36 UTC)

<p>Thanks for the info. I will remove Tkinter and tk from the code.</p>

---

## Post #7 by @brhoom (2018-10-25 08:23 UTC)

<p>The extension is updated and it should work with recent slicer version 4.10 and 4.11 when it builds next time.</p>
<p>I don’t know why the extension icon and screenshots do not appear, is there something I should do to fix it?</p>

---

## Post #8 by @lassoan (2018-10-25 13:40 UTC)

<p>Icon URLs in s4ext file are not used, they are for information purposes only. What matters is the URLs in the CMakeLists.txt file (<a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/blob/master/CMakeLists.txt">https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/blob/master/CMakeLists.txt</a>).</p>
<p>Also, URL seems incorrect. URL to raw data on github usually looks like this: <a href="https://raw.githubusercontent.com/MedicalImageAnalysisTutorials/SlicerCochlea/master/SlicerCochlea.png">https://raw.githubusercontent.com/MedicalImageAnalysisTutorials/SlicerCochlea/master/SlicerCochlea.png</a></p>

---

## Post #9 by @brhoom (2018-10-28 11:27 UTC)

<p>Thanks, Andras, now it is clear. I updated the links with raw links in both s4ext and CMakeLists.txt.</p>

---

## Post #10 by @torquil (2018-10-29 22:01 UTC)

<p>Ok, I installed the latest Slicer 3D nightly for Linux, and now I’m getting this error on the terminal after picking a point in the middle of the cochlea in a CT image, and then clicking on “Run”:</p>
<pre><code class="lang-auto">Switch to module:  "CochleaSeg"
 
=======================================================
   Automatic Cochlea Image Segmentation               
=======================================================
   Default Settings: 
      VisSimTools folder: /home/torquil/VisSimTools
      Output folder : /home/torquil/VisSimTools/outputs
      Parameter file: /home/torquil/VisSimTools/pars/parCochSeg.txt
      Cropping Length: 10
elastix binaries are found in /home/torquil/VisSimTools/sw/elastix-4.9.0/bin/elastix
Other files are found !
Traceback (most recent call last):
  File "/home/torquil/.config/NA-MIC/Extensions-27526/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules/CochleaSeg.py", line 746, in updateLengthBtnClick
    ptsRASNode =  self.markupsNode
AttributeError: CochleaSegWidget instance has no attribute 'markupsNode'
 ..... getting cochlea location in the input image

 ..... cochlea location RAS: [38.186453904880466, 170.83668361478453, 225.1563957681987, 1.0]
 ..... cochlea location in the fixed image set to: [85, 301, 299]
removing old output folder!
Traceback (most recent call last):
  File "/home/torquil/.config/NA-MIC/Extensions-27526/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules/CochleaSeg.py", line 465, in runBtnClick
    self.inputPath = self.inputNode.GetStorageNode().GetFileName()
AttributeError: 'NoneType' object has no attribute 'GetFileName'
</code></pre>
<p>Within Slicer, the “Run”-button turned red and says “…please wait”, but nothing is happening and the timer is not counting.</p>

---

## Post #11 by @brhoom (2018-11-14 18:27 UTC)

<p>Thanks for testing.<br>
I could not reproduce the problem. Does the cochlea registration module work?</p>
<p>Please try these steps:</p>
<ol>
<li>
<p>save your cochlea image in  your home folder as nrrd format. Sometimes elastix does not recognize filenames with special characters or spaces, e.g. use this filename.  /home/torquil/img.nrrd</p>
</li>
<li>
<p>delete the output contents</p>
<pre><code>  rm -r /home/torquil/VisSimTools/outputs/*
</code></pre>
</li>
<li>
<p>restart slicer</p>
</li>
<li>
<p>load your nrrd cochlea image</p>
</li>
<li>
<p>run the cochlea segmentation module</p>
</li>
</ol>
<p>Let me know if this works.</p>

---

## Post #12 by @brhoom (2018-11-14 19:59 UTC)

<p>I just retest it again on a clean installation of Ubuntu 18.04. The only thing I needed to do is to install opencl:</p>
<pre><code>sudo apt install ocl-icd-opencl-dev
</code></pre>
<p>please make sure you have this install before trying the above steps.</p>

---

## Post #13 by @lassoan (2018-11-15 00:56 UTC)

<p>Do you really need OpenCL? Could you include runtime libraries in the extension instead of asking the user to manually download and install development packages? Many users are not comfortable with installing additional software tools.</p>
<p>If there is no chance for a better solution then at least the extension should detect if some OpenCL component is missing and display a meaningful error message - with an explanation and download link.</p>

---

## Post #14 by @brhoom (2018-11-15 09:02 UTC)

<blockquote>
<p>Do you really need OpenCL? Could you include runtime libraries in the extension instead of asking the user to manually download and install development packages?</p>
</blockquote>
<p>Thanks for your comment. You are right. I used my elastix binaries as a temporary solution as I am planning to use  <a href="https://github.com/lassoan/SlicerElastix/issues/8" rel="noopener nofollow ugc">SlicerElastix</a> instead.</p>

---

## Post #15 by @brhoom (2018-12-06 17:46 UTC)

<p><strong>Update:</strong></p>
<ul>
<li>Runtime libraries are included now in the elastix binaries.</li>
<li>Logic classes are added so some useful function can be called from external Slicer modules.</li>
<li>Tests classes are added so the user can run them using Slicer Developer Mode and the button “Reload and Test”.</li>
<li>Minor bugs are fixed.</li>
</ul>

---

## Post #16 by @Bence_Horvath (2021-06-04 09:13 UTC)

<p>Hi,</p>
<p>I have a problem with the cochlea segmentation module.<br>
This modul create always the same cochlea that is not consist with the real image. I used Slicer 4.10.0 (on the latest version 4.11. this extension not work, always drop an error: 2 arguments expected but 4 were given)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6952cbb8d85e891bcbba45eefff77ad12ed5e871.png" data-download-href="/uploads/short-url/f1Jwsyq6cvYQIW9LKdZFtE2kKD7.png?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6952cbb8d85e891bcbba45eefff77ad12ed5e871_2_689x500.png" alt="Screenshot_3" data-base62-sha1="f1Jwsyq6cvYQIW9LKdZFtE2kKD7" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6952cbb8d85e891bcbba45eefff77ad12ed5e871_2_689x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6952cbb8d85e891bcbba45eefff77ad12ed5e871_2_1033x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6952cbb8d85e891bcbba45eefff77ad12ed5e871.png 2x" data-dominant-color="CFCECF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">1086×788 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The modul segment this random cochlea also, when I put the markups anywhere on the image.<br>
What is the problem? I tried what happened if I check the right side box.</p>
<p>Best regards!<br>
Bence</p>

---

## Post #17 by @lassoan (2021-06-04 20:51 UTC)

<p>Do you see any errors in the application log?<br>
If you don’t get an answer here within a couple of days then you can submit a bug report to the extension’s github repository.</p>

---

## Post #18 by @Bence_Horvath (2021-06-07 08:19 UTC)

<p>Thanks! I will report it on github!</p>

---
