---
topic_id: 29326
title: "Failed To Fetch Models From Remote Server Make Sure Server A"
date: 2023-05-07
url: https://discourse.slicer.org/t/29326
---

# Failed to fetch models from remote server. ..Make sure server address is correct and <server_uri>/v1/models is accessible in browser

**Topic ID**: 29326
**Date**: 2023-05-07
**URL**: https://discourse.slicer.org/t/failed-to-fetch-models-from-remote-server-make-sure-server-address-is-correct-and-server-uri-v1-models-is-accessible-in-browser/29326

---

## Post #1 by @hepato (2023-05-07 12:17 UTC)

<p>when I use Nvidia AIAA，error happen. feedback like below.<br>
could you do me a favor to tell me how to resolve this problem?</p>
<pre><code class="lang-python">Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-31734/NvidiaAIAssistedAnnotation/lib/Slicer-5.3/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 198, in fetchAIAAModels
    models = self.logic.list_models()
  File "/Applications/Slicer.app/Contents/Extensions-31734/NvidiaAIAssistedAnnotation/lib/Slicer-5.3/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 1076, in list_models
    return aiaaClient.model_list(label)
  File "/Applications/Slicer.app/Contents/Extensions-31734/NvidiaAIAssistedAnnotation/lib/Slicer-5.3/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py", line 190, in model_list
    status, response = AIAAUtils.http_method('GET', self._server_url, selector)
  File "/Applications/Slicer.app/Contents/Extensions-31734/NvidiaAIAssistedAnnotation/lib/Slicer-5.3/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py", line 626, in http_method
    conn.request(method, selector)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py", line 1040, in _send_output
    self.send(msg)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py", line 980, in send
    self.connect()
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py", line 946, in connect
    self.sock = self._create_connection(
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/socket.py", line 844, in create_connection
    raise err
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/socket.py", line 832, in create_connection
    sock.connect(sa)
TimeoutError: [Errno 60] Operation timed out
</code></pre>

---

## Post #2 by @lassoan (2023-05-10 05:07 UTC)

<p>Developers of NVIDIA AIAA extension deprecated it and switched over to developing MONAILabel extension instead. MONAILabel is not only for running existing models but you can use it to train your own models.</p>
<p>For segmenting almost anything on CT (all major organs, bones, vessels, etc.) you can now use the <a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator extension</a> (100+ structures, fully automatically in 2 minutes, even without a GPU).</p>

---

## Post #3 by @hepato (2023-05-12 07:54 UTC)

<p>Thank you for help!<br>
Your answer help me a lot!<br>
I try to use  total segments extension.I installed successfully.<br>
But errors happened.<br>
my computer is MacBook Air m1. 16gb<br>
slicer version is 5.2.2<br>
Could you tell me how to reslolve this problem?</p>
<p>errors feedback :<br>
failed to compute results.</p>
<p>Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_15+52+24.819/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_15+52+24.819/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>raceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 799, in process<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_15+52+24.819/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_15+52+24.819/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #4 by @hepato (2023-05-12 13:29 UTC)

<p>I reinstalled the slicer again，preview version 5.3.0.<br>
and install PyTorch for cpu ,install total segment extension again.<br>
errors happened again.</p>
<p>what can I do to resolve this problem?<br>
feedback:<br>
Failed to compute results.</p>
<p>Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_21+25+33.298/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_21+25+33.298/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2973, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 799, in process<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-31734/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_21+25+33.298/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2023-05-12_21+25+33.298/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #5 by @chir.set (2023-05-12 14:56 UTC)

<p>I’m having trouble with ‘Total segmentator’ on Linux too, since <em>recently</em>, don’t know if mines are related to yours.</p>
<pre><code class="lang-auto">....
....

    ret = self.network.predict_3D(data, do_mirroring=do_mirroring, mirror_axes=mirror_axes,
  File "/home/user/programs/Slicer/lib/Python/lib/python3.9/site-packages/nnunet/network_architecture/neural_network.py", line 147, in predict_3D
    res = self._internal_predict_3D_3Dconv_tiled(x, step_size, do_mirroring, mirror_axes, patch_size,
  File "/home/user/programs/Slicer/lib/Python/lib/python3.9/site-packages/nnunet/network_architecture/neural_network.py", line 348, in _internal_predict_3D_3Dconv_tiled
    gaussian_importance_map[gaussian_importance_map == 0] = gaussian_importance_map[
RuntimeError: "min_all" not implemented for 'Half'
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x7fd3d45f8c10&gt;
AttributeError: 'DummyFile' object has no attribute 'flush'
</code></pre>
<p>I noticed that it happens when the input is a whole volume, for instance, CTA-cardio. If it is cropped down to the abdomen or the thorax, ‘Total segmentator’ completes nicely. And the cropped volume must not be too big. If it includes abdomen and thorax, then it fails likewise.</p>
<p>Using Fast mode with AMD GPU on laptop and desktop.</p>

---

## Post #6 by @lassoan (2023-05-12 18:40 UTC)

<p>Error 120 means PyTorch is not installed correctly or the version is incompatible with your hardware. Restarting your computer and installing pytorch manually may fix th problem.</p>
<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p><code>RuntimeError: "min_all" not implemented for 'Half'</code></p>
</blockquote>
</aside>
<p>What is your current pytorch version?<br>
Do you use cuda or cpu version?</p>
<p>To solve this issue, you probably need to upgrade to pytorch&gt;=2. Please uninstall Pytorch restart Slicer, and then force installation using <code>pip_install('torch&gt;=2')</code></p>

---

## Post #7 by @chir.set (2023-05-12 19:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your current pytorch version?<br>
Do you use cuda or cpu version?</p>
</blockquote>
</aside>
<p>I was using 1.8.1+cpu.</p>
<p>After installing Torch 2 as you advised, ‘Total segmentator’ works normally with a full CTA-cardio volume as test.</p>
<p>My machines do not run with NVidia GPUs, so I’m compelled to use CPU only;</p>
<p>Thank you very much.</p>

---

## Post #8 by @lassoan (2023-05-12 19:10 UTC)

<p>On linux, you can try to utilize your AMD GPU by using the ROCm edition of PyTorch. See manual install instructions <a href="https://pytorch.org/get-started/locally/">here</a>. Let us know if it works and if the performance is better then with CPU.</p>

---

## Post #9 by @chir.set (2023-05-12 19:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your current pytorch version?</p>
</blockquote>
</aside>
<p>I’m using <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">SlicerPyTorch</a> to install Torch. It always install 1.8.1. Is there another helper module that would install the latest version ? I can of course note the command and type it whenever needed.</p>

---

## Post #10 by @lassoan (2023-05-12 19:33 UTC)

<p>I don’t know why on some systems why not the latest pytorch is installed by default. Maybe because an older version of ltt is installed, which does not know about torch-2.x yet? If you install Slicer in a new folder and install TotalSegmentator then which torch version gets installed?</p>

---

## Post #11 by @chir.set (2023-05-12 20:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>which torch version gets installed?</p>
</blockquote>
</aside>
<p>Using Slicer preview 5.3.0-2023-05-11 r31736 / 10e85ca in a new folder, ‘Total segmentator’ installs Torch 1.8.1+cpu.</p>

---

## Post #12 by @chir.set (2023-05-12 20:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the ROCm edition of PyTorch</p>
</blockquote>
</aside>
<p>I installed this ROCm edition in Slicer’s python console using their instructions :</p>
<p>pip_install(“torch torchvision torchaudio --index-url <a href="https://download.pytorch.org/whl/rocm5.4.2" rel="noopener nofollow ugc">https://download.pytorch.org/whl/rocm5.4.2</a>”)</p>
<p>The installation was flawless : 2.0.2+rocm5.4.2 in ‘PyTorch utils’. But ‘Total segmentator’ can’t use the GPU on my laptop featuring an ‘AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx’ APU with shared VRAM.</p>
<p>I suppose it’s because it’s an integrated GPU. I’ll be able to test on my work machine tomorrow or on Monday. It has a Radeon RX 6700 XT video card, it should hopefully be seen and used by Torch. I’ll keep you updated of course. Thanks for your input.</p>

---

## Post #13 by @lassoan (2023-05-12 22:15 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="11" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Using Slicer preview 5.3.0-2023-05-11 r31736 / 10e85ca in a new folder, ‘Total segmentator’ installs Torch 1.8.1+cpu.</p>
</blockquote>
</aside>
<p>I’m not sure why not the latest pytorch is installed. I’ve submitted an issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/fepegar/SlicerPyTorch/issues/10">
  <header class="source">

      <a href="https://github.com/fepegar/SlicerPyTorch/issues/10" target="_blank" rel="noopener">github.com/fepegar/SlicerPyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fepegar/SlicerPyTorch/issues/10" target="_blank" rel="noopener">torch 1.x is installed by default</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-05-12" data-time="22:12:03" data-timezone="UTC">10:12PM - 12 May 23 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2023-05-14" data-time="22:07:47" data-timezone="UTC">10:07PM - 14 May 23 UTC</span>
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
    <p class="github-body-container">For some reason, on some configurations, this extension installs pytorch-1.x by <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">default, which is a problem, because the most widely used AI segmentation tool, TotalSegmentator only works with pytorch&gt;=2.x.

@fepegar, do you have any clue why not the latest version is installed by default?
Could we hardcode the `torch&gt;=2` version requirement in the installation parameters?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="chir.set" data-post="12" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>‘Total segmentator’ can’t use the GPU on my laptop featuring an ‘AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx’ APU with shared VRAM.</p>
</blockquote>
</aside>
<p>I’m not surprised that it does not work with an integrated GPU. Looking forward to seeing if it works with the discrete AMD GPU.</p>

---

## Post #14 by @hepato (2023-05-13 01:02 UTC)

<p>Thanks again for your answer!<br>
According to your suggestion,I  uninstalled the PyTorch (version 1.8.1),install PyTorch (version 2.0.1).<br>
This time, total segmentor works!<br>
I succeed in segmenting abdominal organ in fast mode，although fail in normal mode（taking about 50 minutes，cpu mode）.<br>
Thank you very much for your help!<br>
Wish you happy weekend!</p>

---

## Post #15 by @chir.set (2023-05-14 09:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Looking forward to seeing if it works with the discrete AMD GPU.</p>
</blockquote>
</aside>
<p>Installed the rocm5.4.2 version on my desktop with discrete ‘RX 6700 XT’ video card using <code>pip_install("torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2")</code>. Things got worse.</p>
<p>It does not propose GPU at all. And fails to process a cropped CTA-cardio volume, while this would succeed with Torch &lt; 2.</p>
<p>Uninstalled rocm5.4.2 and installed torch with <code>pip_install('torch&gt;=2')</code>. Torch version is 2.0.1+cu117. GPU is not used as expected. But processing a full CTA-cardio succeeds.</p>

---

## Post #16 by @lassoan (2023-05-14 14:40 UTC)

<p>It seems that nnunet developers did not make their framework compatible with AMD. They only use CUDA on Linux, so TotalSegmentator has to use a special version that Jakob modified to be able to run on CPU and Windows. So, it is not surprising that AMD does not work without some fixes.</p>

---

## Post #17 by @chir.set (2023-05-14 15:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="29326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it is not surprising that AMD does not work</p>
</blockquote>
</aside>
<p>Yes, everything I tried failed. It’s not a big issue as I work with cropped volumes very often, so CPU mode is decently fast. It’s good to know there’s an effort being made towards AMD GPUs.</p>

---
