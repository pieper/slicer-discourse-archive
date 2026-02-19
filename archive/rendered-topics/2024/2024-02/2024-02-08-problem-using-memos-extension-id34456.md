---
topic_id: 34456
title: "Problem Using Memos Extension"
date: 2024-02-08
url: https://discourse.slicer.org/t/34456
---

# Problem using MEMOS extension

**Topic ID**: 34456
**Date**: 2024-02-08
**URL**: https://discourse.slicer.org/t/problem-using-memos-extension/34456

---

## Post #1 by @coco (2024-02-08 14:25 UTC)

<p>Dear Murat,<br>
very excited to use this tool for tests but I seem to be stuck. Most likely a problem with my environment but any suggestion or help appreciated.<br>
I installed a fresh version of slicer (5.6.1) on windows 11. Memos seems to instal fine so as pytorch utilities.<br>
Upon selecting the downloaded IMPC sample data from your github as volume and the segmentation model “best_metric…pth”, I click Apply. It runs for a few seconds but no segments are visible…</p>

---

## Post #2 by @muratmaga (2024-02-08 16:01 UTC)

<p>Yeah, if it ran a few seconds and stop, it is mostly likely stopped due to an error (possibly torch). Please share your log file (CTRL+0).</p>

---

## Post #3 by @coco (2024-02-12 08:55 UTC)

<p>Thank you Murat,<br>
I had a couple of error messages:</p>
<p>1-</p>
<pre><code class="lang-auto">required package for reader itkreader is not installed, or the version doesn't match requirement.
</code></pre>
<p>2-</p>
<pre><code class="lang-auto">Using device: 0
MONAI version: 0.9.0
Numpy version: 1.26.1
Pytorch version: 2.2.0+cu118
MONAI flags: HAS_EXT = False, USE_COMPILED = False
MONAI rev id: af0e0e9f757558d144b655c63afcea3a4e0a06f5
MONAI __file__: C:\Users\steph\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\monai\__init__.py
Optional dependencies:
Pytorch Ignite version: NOT INSTALLED or UNKNOWN VERSION.
Nibabel version: 5.2.0
scikit-image version: NOT INSTALLED or UNKNOWN VERSION.
Pillow version: 10.1.0
Tensorboard version: NOT INSTALLED or UNKNOWN VERSION.
gdown version: NOT INSTALLED or UNKNOWN VERSION.
TorchVision version: 0.17.0+cu118
tqdm version: NOT INSTALLED or UNKNOWN VERSION.
lmdb version: NOT INSTALLED or UNKNOWN VERSION.
psutil version: NOT INSTALLED or UNKNOWN VERSION.
pandas version: NOT INSTALLED or UNKNOWN VERSION.
einops version: 0.7.0
transformers version: NOT INSTALLED or UNKNOWN VERSION.
mlflow version: NOT INSTALLED or UNKNOWN VERSION.
pynrrd version: 1.0.0

For details about installing the optional dependencies, please visit:
https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies

Using device: cuda
</code></pre>
<p>3-</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/steph/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py", line 245, in onApplySingleButton
    logic.runSingle(tempVolumeFile, self.modelPathSingle.currentPath, tempOutputPath)
  File "C:/Users/steph/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py", line 480, in runSingle
    output_raw = sliding_window_inference(
  File "C:\Users\steph\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\monai\inferers\utils.py", line 215, in sliding_window_inference
    output_image_list.append(torch.zeros(output_shape, dtype=compute_dtype, device=device))
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 5.35 GiB. GPU 0 has a total capacity of 6.00 GiB of which 1.88 GiB is free. Of the allocated memory 2.20 GiB is allocated by PyTorch, and 53.75 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
</code></pre>
<p>I’m sorry, but I am not exactly sure where to go from there on this windows version…</p>
<p>Kind regards</p>

---

## Post #4 by @muratmaga (2024-02-12 15:26 UTC)

<p>The important message is at the very end. You ran out of gpu memory. Our model requires gpu with at least 8GB, you have 6gb. You can try to install the cpu only version of the torch and retry, but it will be much slower.</p>

---

## Post #5 by @coco (2024-02-14 09:38 UTC)

<p>Thanks Murat,<br>
apologies for not checking this. In fact I had tried it on my own windows laptop after getting stuck somehow on a different system. So, I have a 5.6.1 version of slicer running in linux and a calculation server with a very powerful GPU.<br>
Slicer just crashes and I’m not able to recover a log.<br>
all I get is: “SlicerApp-real] exit abnormally - Report the problem.”</p>
<p>Kind regards</p>

---

## Post #6 by @lassoan (2024-02-14 11:41 UTC)

<p>Does this error occur when you start the segmentation?</p>
<p>You can view logs of previous Slicer sessions in the menu: Help / Report a bug.</p>

---

## Post #7 by @coco (2024-02-14 13:04 UTC)

<p>Dear Andras,<br>
thanks for your help,</p>
<p>It happens when I click apply. The programm thinks for 20secs, then crashes</p>
<p>The bug reports does not refer to a simple crash:<br>
I have only changed directory paths for safety issues</p>
<p>[DEBUG][Qt] 14.02.2024 10:25:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “MEMOS”<br>
[DEBUG][Qt] 14.02.2024 10:26:36 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “/MYDIRECTORY/IMPC_sample_data (2).nrrd” “[0.54s]”<br>
[INFO][Stream] 14.02.2024 10:26:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Checking python dependencies<br>
[DEBUG][Python] 14.02.2024 10:27:16 [Python] (/MYDIRECTORY/soft/Slicer-5.6.1-linux-amd64/slicer.org/Extensions-32438/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py:372) - Pillow Python package is required. Installing…<br>
[INFO][Stream] 14.02.2024 10:27:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Requirement already satisfied: pillow in /MYDIRECTORY/soft/Slicer-5.6.1-linux-amd64/lib/Python/lib/python3.9/site-packages (10.1.0)</p>
<p>As everyone guessed, I’m fairly novice here. Please let me know if there are any other type of information that may help and how to access them.<br>
…and thank you for making slicer such an amazing tool and vibrant community !</p>

---

## Post #8 by @muratmaga (2024-02-14 15:47 UTC)

<p>Is this the full log? Crash is not visible in this one.</p>

---

## Post #9 by @coco (2024-02-14 16:40 UTC)

<p><strong>Dear Murat, thank you again for your help.</strong></p>
<p><strong>I don’t see an error message after the crash as well.</strong></p>
<p><b>I repeated the steps to be sure, and this is the full log file content:</b></p>
<p>[DEBUG][Qt] 14.02.2024 17:29:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20240214_172903</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:03 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.1 (revision 32438 / 117ce5f) linux-amd64 - installed release</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Linux / 4.18.0-372.32.1.el8_6.x86_64 / <span class="hashtag-raw">#1</span> SMP Fri Oct 7 12:35:10 EDT 2022 / US-ASCII - 64-bit</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 12188948 MB physical, 16383 MB virtual</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Xeon(R) Gold 6252 CPU @ 2.10GHz, 384 cores, 768 logical processors</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /beegfs/data/MYDIRECTORY/soft/Slicer-5.6.1-linux-amd64/bin</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32438/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32438/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32438/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32438/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32438/MarkupsToModel/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32438/MarkupsToModel/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32438/MEMOS/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32438/MEMOS/lib/Slicer-5.6/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32438/PyTorch/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32438/PyTorch/lib/Slicer-5.6/qt-scripted-modules</a></p>
<p>[WARNING][Qt] 14.02.2024 17:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[WARNING][Qt] 14.02.2024 17:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile</p>
<p>[WARNING][Qt] 14.02.2024 17:29:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: too many profiles</p>
<p>[WARNING][Qt] 14.02.2024 17:29:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile</p>
<p>[DEBUG][Python] 14.02.2024 17:29:16 [Python] (/beegfs/data/MYDIRECTORY/soft/Slicer-5.6.1-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 14.02.2024 17:29:16 [Python] (/beegfs/data/MYDIRECTORY/soft/Slicer-5.6.1-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] 14.02.2024 17:29:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module: “Welcome”</p>
<p>[DEBUG][Python] 14.02.2024 17:29:17 [Python] (/beegfs/data/MYDIRECTORY/soft/Slicer-5.6.1-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: FormatMarkups</p>
<p>[INFO][Python] 14.02.2024 17:29:17 [Python] (:3) - Adding SlicerMorph Volume Rendering Presets</p>
<p><strong>However, I paid more attention to my terminal. In fact, here I might have further clues. Here is full log (from opening slicer, loading data, loading module, selecting IMPC sample data, and clicking apply in MEMOS):</strong></p>
<p>Execution de la commande sur le serveur GPU distant.</p>
<p>commande : ssh -X webern01 /opt/VirtualGL/bin/vglrun -d :0 /MYDIRECTORY/Slicer-5.6.1-linux-amd64/Slicer</p>
<p>st6962co@webern01’s password:</p>
<p>[VGL] NOTICE: Automatically setting VGL_CLIENT environment variable to</p>
<p>[VGL] 172.16.80.62, the IP address of your SSH client.</p>
<p>libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>libpng warning: iCCP: known incorrect sRGB profile</p>
<p>libpng warning: iCCP: too many profiles</p>
<p>libpng warning: iCCP: known incorrect sRGB profile</p>
<p>Switch to module: “Welcome”</p>
<p>Switch to module: “MEMOS”</p>
<p>“Volume” Reader has successfully read the file “/MYDIRECTORY/IMPC_sample_data.nrrd” “[2.81s]”</p>
<p>Checking python dependencies</p>
<p>Requirement already satisfied: pillow in /beegfs/data/MYDIRECTORY/Slicer-5.6.1-linux-amd64/lib/Python/lib/python3.9/site-packages (10.1.0)</p>
<p>“Color” Reader has successfully read the file “/MYDIRECTORY/Slicer-5.6.1-linux-amd64/slicer.org/Extensions-32438/MEMOS/lib/Slicer-5.6/qt-scripted-modules/Resources/Support/KOMP2.ctbl” “[0.02s]”</p>
<p>Using device: 0</p>
<p>MONAI version: 0.9.0</p>
<p>Numpy version: 1.26.1</p>
<p>Pytorch version: 2.2.0+cu118</p>
<p>MONAI flags: HAS_EXT = False, USE_COMPILED = False</p>
<p>MONAI rev id: af0e0e9f757558d144b655c63afcea3a4e0a06f5</p>
<p>MONAI <strong>file</strong>: /MYDIRECTORY/Slicer-5.6.1-linux-amd64/lib/Python/lib/python3.9/site-packages/monai/<strong>init</strong>.py</p>
<p>Optional dependencies:</p>
<p>Pytorch Ignite version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>Nibabel version: 5.2.0</p>
<p>scikit-image version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>Pillow version: 10.1.0</p>
<p>Tensorboard version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>gdown version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>TorchVision version: 0.17.0+cu118</p>
<p>tqdm version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>lmdb version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>psutil version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>pandas version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>einops version: 0.7.0</p>
<p>transformers version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>mlflow version: NOT INSTALLED or UNKNOWN VERSION.</p>
<p>pynrrd version: 1.0.0</p>
<p>For details about installing the optional dependencies, please visit:</p>
<p><a href="https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies" class="onebox" target="_blank" rel="noopener nofollow ugc">https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies</a></p>
<p>Using device: cuda</p>
<p>error: [/MYDIRECTORY/Slicer-5.6.1-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p><strong>Slicer quits at this last step</strong></p>

---

## Post #10 by @lassoan (2024-02-14 17:02 UTC)

<p>It would worth a try running the inference in a separate process, started within Slicer - added an issue for enabling this in SlicerMEMOS:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerMorph/SlicerMEMOS/issues/15">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMEMOS/issues/15" target="_blank" rel="noopener">github.com/SlicerMorph/SlicerMEMOS</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerMorph/SlicerMEMOS/issues/15" target="_blank" rel="noopener">Run inference in a separate process</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-02-14" data-time="16:54:48" data-timezone="UTC">04:54PM - 14 Feb 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">It seems that inference is run inside the Slicer process: https://github.com/Sli<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">cerMorph/SlicerMEMOS/blob/4b30659ee57b2be49b58c99822e16a221b12c4d0/MEMOS/MEMOS.py#L245

Many things can go wrong during a complex and heavy computation task, so you want to isolate it from the application by running it in a separate process. That allows you to keep using the application while the computation is running, you can stop the process anytime (by killing the computation process),  and you can prevent the application from crashing if the computation process is terminated (e.g., due to some errors in PyTorch or due to the operating system killing the process because of using too much resources).

You can use MONAIAuto3DSeg extension as an example. It launches [auto3dseg_segresnet_inference.py](https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py) script in a separate Python process.

Note that you would still use Slicer's Python environment, the only change would be that the inference is running in a separate process.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If it still crashes then you could try to run the script independently from Slicer (using the input files that Slicer generated). If still does not work then test if you can run the same script from a different Python environment. If still does not work then you may have some GPU driver issues. If the script works in the external Python environment then you can get hint about what’s wrong by comparing packages in Slicer’s Python environment and in the external Python environment.</p>

---

## Post #11 by @muratmaga (2024-02-14 17:37 UTC)

<p><a class="mention" href="/u/coco">@coco</a> I think you said this is a linux system. How are you running the Slicer application, are you using VirtualGL (vglrun)? If so, there is actually a bug that causes a crash in torch in specific server drivers (Nvidia grid drivers).</p><aside class="onebox githubissue" data-onebox-src="https://github.com/VirtualGL/virtualgl/issues/227">
  <header class="source">

      <a href="https://github.com/VirtualGL/virtualgl/issues/227" target="_blank" rel="noopener">github.com/VirtualGL/virtualgl</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/VirtualGL/virtualgl/issues/227" target="_blank" rel="noopener">vgl 3.0.90-20221122 crashing torch on ubuntu 22.04</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-02-23" data-time="21:33:46" data-timezone="UTC">09:33PM - 23 Feb 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">We are using vgl on a cloud server with A100 gpu (grid driver 525.60.13) with 3D<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> Slicer with egl backend.

If we invoke the slicer without vglrun, our torch based application works fine. If we start the Slicer via 
vglrun -d egl ./Slicer 

a little after the torch starts loading the trained model, application crashes. There is no error message (neither in Slicer not in vglrun) that I can locate. 

I am assuming it is a weird combination of the driver being used and VGL, as we can't replicate this crash on our local machine (though we use ubuntu 20.04, not 22.04, and we have RTX A4000 not A100). 

I would appreciate some pointers on how to troubleshoot this. Thanks.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you are using vglrun run, try starting Slicer without vglrun (it will probably give a bunch of complaints about lack of often openGL, but it should still run), and then give another try.</p>

---

## Post #12 by @coco (2024-02-15 09:13 UTC)

<p>Dear Murat, thank you again for your answer.<br>
I read your post <span class="hashtag-raw">#227</span> and your last answer echoes very much what is happening to me. The terminal prompt reads more or less identical to mine.<br>
I’m working on a calculcation server running linux (CentOS Linux release 7.7.1908 (Core))<br>
I connect to our calculation server cluster interactively using NoMachine for remote access. Slicer is then executed via a command line instruction <code>3dsub -q 3d@NAMEOFMACHINE</code> , targeting a machine with high GPU performance dedicated to us but on which I have little information. Unfortunately, I have a limited understanding or control of our computing environment and administrators are not easily reached.<br>
How would you run Slicer without vglrun ?<br>
Normally I just enter ‘3dsub -q 3d@MYMACHINE /MYDIRECTORY/Slicer’</p>
<p>Again, thanks for your help</p>

---

## Post #13 by @lassoan (2024-02-15 12:23 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> running the inference in a separate process might help with this, too. It may be enough to set <code>LD_PRELOAD</code> environment variable to empty in the environment that launches the MEMOS inference script.</p>

---

## Post #14 by @coco (2024-02-21 09:14 UTC)

<p>Thanks to you all,<br>
after a few discussion with the IT people managing our cluster, it turns out I need a separate machine where I could have a GPU with enough RAM and have better control on how to run slicer. I’m now doing this…</p>

---

## Post #15 by @muratmaga (2024-02-21 16:58 UTC)

<p>Yes, it is often quite challenging to get Slicer (or any interactive desktop application) work effectively in university HPC systems that are queue based. Try in a local system where you have more control over the computing environment parameters.</p>

---

## Post #16 by @RosieB (2024-04-15 14:20 UTC)

<p>Hello,<br>
I am having a similar problem to the previous person. When I try to run MEMOS, it thinks for a little while (~1 minute) then nothing happens.</p>
<p>I will paste in my log file here. I have to admit that it means very little to me.<br>
I am running Slicer on a Windows 10 computer with 32GB RAM, 6 CPU cores and an NVIDIA RTX A5000 GPU</p>
<p>Grateful for any suggestions.<br>
Thanks very much<br>
Rosie</p>
<pre><code class="lang-auto">[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Session start time .......: 20240415_144809
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Memory ...................: 32446 MB physical, 58716 MB virtual
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - CPU ......................: GenuineIntel , 12 cores, 12 logical processors
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Application path .........: C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 15.04.2024 14:48:09 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/MarkupsToModel/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-loadable-modules, slicer.org/Extensions-32448/SegmentEditorExtraEffects/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SurfaceWrapSolidify/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/NvidiaAIAssistedAnnotation/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/SegmentWithSAM/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules
[WARNING][Qt] 15.04.2024 14:48:17 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[WARNING][Qt] 15.04.2024 14:48:17 [] (unknown:0) - libpng warning: iCCP: too many profiles
[DEBUG][Python] 15.04.2024 14:48:20 [Python] (C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 15.04.2024 14:48:20 [Python] (C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 15.04.2024 14:48:20 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Python] 15.04.2024 14:48:22 [Python] (C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/NvidiaAIAssistedAnnotation/lib/Slicer-5.6/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/NvidiaAIAssistedAnnotation/lib/Slicer-5.6/qt-scripted-modules
[DEBUG][Qt] 15.04.2024 14:48:35 [] (unknown:0) - "Volume" Reader has successfully read the file "D:/microCT on D drive/RECONS E14.5-test_2024_02/E14.5 IMPC examples/20210709_Hpgd-tm1b_E14.5_4.4d_WT_XY_REC_scaled_4.6823_pixel_14.0001.nrrd" "[1.76s]"
[DEBUG][Qt] 15.04.2024 14:48:41 [] (unknown:0) - Switch to module:  "MEMOS"
[INFO][Stream] 15.04.2024 14:48:45 [] (unknown:0) - Checking python dependencies
[DEBUG][Python] 15.04.2024 14:48:55 [Python] (C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py:500) - Pillow Python package is required. Installing...
[INFO][Stream] 15.04.2024 14:49:00 [] (unknown:0) - Requirement already satisfied: pillow in c:\users\r.bunton-stasyshyn\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (10.1.0)
[DEBUG][Qt] 15.04.2024 14:49:15 [] (unknown:0) - "Color" Reader has successfully read the file "C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules\\Resources\\Support/KOMP2.ctbl" "[0.02s]"
[INFO][Stream] 15.04.2024 14:49:33 [] (unknown:0) - Using device:  0
[INFO][Stream] 15.04.2024 14:49:33 [] (unknown:0) - MONAI version: 0.9.0
[INFO][Stream] 15.04.2024 14:49:33 [] (unknown:0) - Numpy version: 1.26.1
[INFO][Stream] 15.04.2024 14:49:33 [] (unknown:0) - Pytorch version: 2.2.2+cu118
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - MONAI flags: HAS_EXT = False, USE_COMPILED = False
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - MONAI rev id: af0e0e9f757558d144b655c63afcea3a4e0a06f5
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - MONAI __file__: C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\monai\__init__.py
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) -
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - Optional dependencies:
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - Pytorch Ignite version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - Nibabel version: 5.2.1
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - scikit-image version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - Pillow version: 10.1.0
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - Tensorboard version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - gdown version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - TorchVision version: 0.17.2+cu118
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - tqdm version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - lmdb version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - psutil version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - pandas version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - einops version: 0.7.0
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - transformers version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - mlflow version: NOT INSTALLED or UNKNOWN VERSION.
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - pynrrd version: 1.0.0
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) -
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) - For details about installing the optional dependencies, please visit:
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) -     https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies
[INFO][Stream] 15.04.2024 14:49:34 [] (unknown:0) -
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) - Using device:  cuda
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) - Traceback (most recent call last):
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\MEMOS\lib\Slicer-5.6\qt-scripted-modules\Scripts\MEMOS_inference.py", line 101, in &lt;module&gt;
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -     fire.Fire(main)
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\fire\core.py", line 143, in Fire
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -     component_trace = _Fire(component, args, parsed_flag_args, context, name)
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\fire\core.py", line 477, in _Fire
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -     component, remaining_args = _CallAndUpdateTrace(
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\fire\core.py", line 693, in _CallAndUpdateTrace
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -     component = fn(*varargs, **kwargs)
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\slicer.org\Extensions-32448\MEMOS\lib\Slicer-5.6\qt-scripted-modules\Scripts\MEMOS_inference.py", line 90, in main
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -     output_raw = sliding_window_inference(image, (image_dim, image_dim, image_dim), 4, net, overlap=0.8)
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\monai\inferers\utils.py", line 215, in sliding_window_inference
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) -     output_image_list.append(torch.zeros(output_shape, dtype=compute_dtype, device=device))
[INFO][Stream] 15.04.2024 14:49:48 [] (unknown:0) - torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 28.18 GiB. GPU 0 has a total capacity of 23.99 GiB of which 18.49 GiB is free. Of the allocated memory 3.09 GiB is allocated by PyTorch, and 53.75 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -   File "C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py", line 306, in onApplySingleButton
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -     labelFilePath = self.launchInference(volumeNode)
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -   File "C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py", line 357, in launchInference
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -     logic.processInference(tempVolumeFile, self.modelPathSingle.currentPath, outputLabelPath, self.colorNode)
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -   File "C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules/MEMOS.py", line 480, in processInference
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -     slicer.util.logProcessOutput(proc)
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -   File "C:\Users\r.bunton-stasyshyn\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py", line 3814, in logProcessOutput
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 15.04.2024 14:49:49 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MEMOS/lib/Slicer-5.6/qt-scripted-modules\\Scripts\\MEMOS_inference.py', '--volume-path', "{'image': 'C:/Users/r.bunton-stasyshyn/AppData/Local/Temp/Slicer\\\\tempMEMOSVolume\\\\20210709_Hpgd-tm1b_E14.5_4.4d_WT_XY_REC_scaled_4.6823_pixel_14.0001.nii.gz'}", '--model-path', 'C:/Users/r.bunton-stasyshyn/AppData/Local/slicer.org/Slicer/cache/SlicerIO/best_metric_model_largePatch_noise.pth', '--output-path', 'C:/Users/r.bunton-stasyshyn/AppData/Local/Temp/Slicer\\tempMEMOSOut\\20210709_Hpgd-tm1b_E14.5_4.4d_WT_XY_REC_scaled_4.6823_pixel_14.0001_seg.nii.gz', '--color-node', 'vtkMRMLColorTableNode (000002D396F2D050)\n  ID: vtkMRMLColorTableNode1\n  ClassName: vtkMRMLColorTableNode\n  Name: KOMP2\n  Debug: false\n  MTime: 253812\n  Description: A color table read in from a text file, each line of the format: IntegerLabel  Name  R  G  B  Alpha\n  SingletonTag: (none)\n  HideFromEditors: false\n  Selectable: true\n  Selected: false\n  UndoEnabled: false\n  Attributes:\n    Category:File\n  Node references:\n    storage [storageNodeRef]: vtkMRMLColorTableStorageNode22\n  StorageNodeIDs[0]: vtkMRMLColorTableStorageNode22\n  Name: KOMP2\n  Type: (File)\n  NoName = (none)\n  Names array initialised: true\n  Color Names:\n    0 background (0, 0, 0, 1)\n    1 left lung (0.772549, 0.647059, 0.568627, 1)\n    2 cranial lobe (0.501961, 0.682353, 0.501961, 1)\n    3 middle lobe (0.945098, 0.839216, 0.568627, 1)\n    4 caudal lobe (0.694118, 0.478431, 0.396078, 1)\n    5 accessory lobe (0.435294, 0.721569, 0.823529, 1)\n    6 left kidney (0.72549, 0.4, 0.32549, 1)\n    7 right kidney (0.72549, 0.4, 0.32549, 1)\n    8 stomach wall (0.847059, 0.396078, 0.309804, 1)\n    9 stomach lumen (0.866667, 0.509804, 0.396078, 1)\n    10 medial lobe of liver (0.564706, 0.933333, 0.564706, 1)\n    ...\n  Look up table:\n    Debug: Off\n    Modified Time: 253791\n    Reference Count: 1\n    Registered Events: \n      Registered Observers:\n        vtkObserver (000002D397B13590)\n          Event: 33\n          EventName: ModifiedEvent\n          Command: 000002D395C72690\n          Priority: 0\n          Tag: 2\n        vtkObserver (000002D397B14010)\n          Event: 2\n          EventName: DeleteEvent\n          Command: 000002D395C72690\n          Priority: 0\n          Tag: 1\n    Alpha: 1\n    VectorMode: Component\n    VectorComponent: 0\n    VectorSize: -1\n    IndexedLookup: OFF\n    AnnotatedValues: 0 entries.\n    TableRange: (0, 50)\n    Scale: Linear\n    HueRange: (0, 0.66667)\n    SaturationRange: (1, 1)\n    ValueRange: (1, 1)\n    AlphaRange: (1, 1)\n    NanColor: (0.5, 0, 0, 1)\n    BelowRangeColor: (0, 0, 0, 1)\n    UseBelowRangeColor: OFF\n    AboveRangeColor: (1, 1, 1, 1)\n    UseAboveRangeColor: OFF\n    NumberOfTableValues: 51\n    NumberOfColors: 51\n    Ramp: SCurve\n    InsertTime: 253790\n    BuildTime: 0\n    Table: \n      Debug: Off\n      Modified Time: 253536\n      Reference Count: 1\n      Registered Events: (none)\n      Name: (none)\n      Data type: unsigned char\n      Size: 1040\n      MaxId: 203\n      NumberOfComponents: 4\n      Information: 0000000000000000\n      Name: (none)\n      Number Of Components: 4\n      Number Of Tuples: 51\n      Size: 1040\n      MaxId: 203\n      LookupTable: (none)\n\n']' returned non-zero exit status 1.
</code></pre>

---

## Post #17 by @muratmaga (2024-04-15 15:49 UTC)

<p>Your volume.is too big for your gpu. Downsample by 2 and try again.</p>

---

## Post #18 by @jamesobutler (2024-04-16 00:37 UTC)

<aside class="quote no-group" data-username="RosieB" data-post="16" data-topic="34456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/f05b48/48.png" class="avatar"> RosieB:</div>
<blockquote>
<p>it thinks for a little while (~1 minute) then nothing happens.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> maybe MEMOS can utilize a try/except to catch <code>torch.cuda.OutOfMemoryError</code> errors and present them in a more human readable form instead of relying on users reading traceback messages in the Python console?</p>

---
