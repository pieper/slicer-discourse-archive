---
topic_id: 26755
title: "Totalsegmentator Error At First Run Command Python Scripts T"
date: 2022-12-15
url: https://discourse.slicer.org/t/26755
---

# TotalSegmentator error at first run: Command ...Python\Scripts\TotalSegmentator... returned non-zero exit status 120

**Topic ID**: 26755
**Date**: 2022-12-15
**URL**: https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-command-python-scripts-totalsegmentator-returned-non-zero-exit-status-120/26755

---

## Post #1 by @Augusto (2022-12-15 14:41 UTC)

<p>In line with this error, i get a similar one and don’t know why:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Augusto/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/Augusto/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 716, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/Augusto/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 625, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Augusto/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/Augusto/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_14+38+59.132/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Augusto/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_14+38+59.132/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Anyone can help?</p>

---

## Post #2 by @Augusto (2022-12-15 14:43 UTC)

<p>I have tried this and the extension is properly installed.</p>

---

## Post #3 by @don_balon (2022-12-15 16:50 UTC)

<p>I have the same problem.<br>
Tried installing Slicer several times, both 5.2.1 stable or 5.3.0 dev. version.<br>
Installed Git.<br>
Still same error, as Augusto mentioned.<br>
Any help? <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>Traceback (most recent call last):<br>
File “C:\Users\rstando\AppData\Local\NA-MIC\Slicer\bin\Python\slicer\util.py”, line 2963, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/rstando/AppData/Local/NA-MIC/Slicer/NA-MIC/Extensions-31464/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/rstando/AppData/Local/NA-MIC/Slicer/NA-MIC/Extensions-31464/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/rstando/AppData/Local/NA-MIC/Slicer/NA-MIC/Extensions-31464/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/rstando/AppData/Local/NA-MIC/Slicer/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\rstando\AppData\Local\NA-MIC\Slicer\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/rstando/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_17+49+15.611/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/rstando/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_17+49+15.611/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #4 by @lassoan (2022-12-15 20:02 UTC)

<p>Can you copy here the messages that are printed in the textbox below the Apply button?<br>
Does it work if you segment with a Slicer sample data set?</p>

---

## Post #5 by @octajuan (2022-12-15 21:06 UTC)

<p>I´m having the exact same problem trying to run totalsegmentator.</p>

---

## Post #6 by @lassoan (2022-12-15 21:09 UTC)

<p><a class="mention" href="/u/octajuan">@octajuan</a> I have the same questions to you, too:</p>
<ul>
<li>Can you copy here the messages that are printed in the textbox below the Apply button?</li>
<li>Does it work if you segment with a Slicer sample data set?</li>
</ul>

---

## Post #7 by @Augusto (2022-12-15 21:18 UTC)

<p>For the time being, since i have slicer installed in a computer which, by default, has no internet acess, i cannot download the sample data set and test TotalSegmentator with it. As soon as i have acess to internet, i will try.</p>
<p>The messages that appear after the Apply button are as follows:</p>
<p>Processing started<br>
Writing input file to C:/Users/Augusto/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_21+10+39.789/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/Augusto/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_21+10+39.789/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Augusto/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_21+10+39.789/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a><br>
preprocessing C:\Users\Augusto\AppData\Local\Temp\nnunet_tmp_kqifjdkf\s01.nii.gz<br>
before crop: (1, 228, 171, 171) after crop: (1, 228, 171, 171) spacing: [3. 3. 3.]<br>
no resampling necessary<br>
before: {‘spacing’: array([3., 3., 3.]), ‘spacing_transposed’: array([3., 3., 3.]), ‘data.shape (data is transposed)’: (1, 228, 171, 171)}</p>
<p>This worker has ended successfully, no errors to report<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 201, in <br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 179, in main<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 232, in nnUNet_predict_image<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 106, in nnUNet_predict<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 668, in predict_from_folder<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 493, in predict_cases_fastest<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\training\network_training\nnUNetTrainerV2.py”, line 211, in predict_preprocessed_data_return_seg_and_softmax<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\training\network_training\nnUNetTrainer.py”, line 516, in predict_preprocessed_data_return_seg_and_softmax<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\network_architecture\neural_network.py”, line 147, in predict_3D<br>
File “C:\Users\Augusto\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\network_architecture\neural_network.py”, line 356, in _internal_predict_3D_3Dconv_tiled<br>
RuntimeError: CUDA out of memory. Tried to allocate 1.30 GiB (GPU 0; 2.00 GiB total capacity; 120.31 MiB already allocated; 1.17 GiB free; 150.00 MiB reserved in total by PyTorch)<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’<br>
Resampling…<br>
Predicting…</p>

---

## Post #8 by @lassoan (2022-12-15 21:33 UTC)

<aside class="quote no-group" data-username="Augusto" data-post="7" data-topic="26755">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/augusto/48/17710_2.png" class="avatar"> Augusto:</div>
<blockquote>
<p>RuntimeError: CUDA out of memory.</p>
</blockquote>
</aside>
<p>Thank you for the report, it contained a nice and clear description of the error: you have run out of memory.  2GB GPU RAM is not nearly enough to do anything related to image segmentation.</p>
<p>You need to use your CPU. The easiest is to install the CPU version of pytorch by exiting Slicer and typing this into the Windows terminal:</p>
<pre data-code-wrap="txt"><code class="lang-txt">"%localappdata%\NA-MIC\Slicer 5.2.1\bin\PythonSlicer.EXE" -m pip install torch torchvision torchaudio --force-reinstall
</code></pre>
<p>We have been discussing in the TotalSegmentator issue tracker how we could avoid this workaround to make switching to CPU easier in case the computer has a GPU but not powerful enough:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/37">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/37" target="_blank" rel="noopener">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/37" target="_blank" rel="noopener">Add option to force using CPU</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-15" data-time="02:19:17" data-timezone="UTC">02:19AM - 15 Dec 22 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-12-22" data-time="03:28:09" data-timezone="UTC">03:28AM - 22 Dec 22 UTC</span>
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
    <p class="github-body-container">Background: TotalSegmentator works extremely well. It stands out among other seg<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">mentation tools with its robustness and the large number of segments, but also with its low resource needs - especially that it can run on a CPU. While all developers have access to computers with CUDA-capable GPU, most users (and basically anyone using a laptop) don't have CUDA-capable GPU. Uploading patient data to some remote server is not acceptable for many users. So, TotalSegmentator is awesome, it allows anyone to segment their own data locally, very conveniently within 3D Slicer, by a few clicks - and the [Slicer community is really excited about this](https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710).

Problem: People who have a weak NVIDIA GPU (e.g., something like a 4GB GPU on a laptop) cannot currently get full-resolution segmentations because their GPU is detected (so CUDA is used) but they don't have enough GPU memory.

Would it be possible to add an option to TotalSegmentator to specify what device to use?

The options could be:
- `automatic`: the current method, use CUDA if available, otherwise CPU
- `CPU`: force to use CPU, even if CUDA-capable GPU is available</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @Augusto (2022-12-15 21:47 UTC)

<p>Ok, will do! Thank you very much!</p>

---

## Post #10 by @don_balon (2022-12-16 07:49 UTC)

<p>My CPU is burning, but now it works perfect!<br>
Thank you!</p>

---

## Post #11 by @FraRizzetto (2022-12-17 15:11 UTC)

<p>Hi all, I have just tried the extension in fast mode (because no GPU is detected) and it gives me a similar error:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/yg/g0dyz18s69dcy2q5jm2tgf340000gn/T/Slicer-francesco/__SlicerTemp__2022-12-17_15+59+32.173/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/yg/g0dyz18s69dcy2q5jm2tgf340000gn/T/Slicer-francesco/__SlicerTemp__2022-12-17_15+59+32.173/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>
<p>I have already tried the workarounds suggested in previous posts, including the terminal command “%localappdata%\NA-MIC\Slicer 5.2.1\bin\PythonSlicer.EXE” -m pip install torch torchvision torchaudio --force-reinstall" and the command “%localappdata%\na-mic\Slicer 5.2.1\bin\PythonSlicer.exe” -m pip install git+https://github.com/wasserth/TotalSegmentator.git --no-deps. However, I always get the error.<br>
I am working with Slicer 5.2.1 on macOS 11.4.</p>
<p>Thank you very much for the support!</p>

---

## Post #12 by @lassoan (2022-12-17 16:00 UTC)

<aside class="quote no-group" data-username="FraRizzetto" data-post="11" data-topic="26755">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/49beb7/48.png" class="avatar"> FraRizzetto:</div>
<blockquote>
<p>I have already tried the workarounds suggested in previous posts</p>
</blockquote>
</aside>
<p>Those commands were not all for fixing issues but for diagnosing issues. If you executed those then they may have messed up your environment. For figuring out what’s wrong on your system, please remove Slicer, reinstall from scratch, run the segmentation on a Slicer sample data set, and provide here the content of the textbox under the Apply button.</p>

---

## Post #13 by @FraRizzetto (2022-12-17 17:06 UTC)

<p>I removed Slicer, reinstalled it and the TotalSegmentator extension, and tried it (fast mode) on a Slicer sample data. This time it asked me for updating PyTorch, then it ran smoothly performing the segmentations. Simple but effective advice. Thanks a lot!</p>

---

## Post #14 by @zhang_ming (2023-02-20 13:23 UTC)

<p>may the weights pre-downloaded by googledrive or somewhere else. Use this plugin downing weights would be terriable for me .cause I can’t download the weights file because of some ssl or network error.</p>

---

## Post #15 by @rbumm (2023-02-20 17:10 UTC)

<p>Have you really tried it yet?<br>
What were the configuration, data, machine, and network, what did you expect to happen, and what did not work?<br>
Can you provide a log from the TotalSegmentator extension output textbox?</p>
<p>Please avoid posting the same problem in different threads.<br>
Thank you.</p>

---

## Post #16 by @zhang_ming (2023-02-21 05:36 UTC)

<p>Sorry for submitting duplicate questions many times.<br>
here is the logs</p>
<pre><code class="lang-auto">Downloading pretrained weights for Task 251 (~230MB) ...
Traceback (most recent call last):
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connection.py", line 159, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\util\connection.py", line 61, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\socket.py", line 954, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11004] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connectionpool.py", line 670, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connectionpool.py", line 381, in _make_request
    self._validate_conn(conn)
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connectionpool.py", line 978, in _validate_conn
    conn.connect()
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connection.py", line 309, in connect
    conn = self._new_conn()
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connection.py", line 171, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: &lt;urllib3.connection.HTTPSConnection object at 0x00000287DC4D9D60&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\requests\adapters.py", line 489, in send
    resp = conn.urlopen(
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\connectionpool.py", line 726, in urlopen
    retries = retries.increment(
  File "C:\Users\someone\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-13\lib\Python\Lib\site-packages\urllib3\util\retry.py", line 446, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='zenodo.org', port=443): Max retries exceeded with url: /record/6802342/files/Task251_TotalSegmentator_part1_organs_1139subj.zip?download=1 (Caused by NewConnectionError('&lt;urllib3.connection.HTTPSConnection object at 0x00000287DC4D9D60&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed'))
</code></pre>

---

## Post #17 by @zhang_ming (2023-02-21 05:41 UTC)

<p>Sorry for submitting duplicate questions many times again<br>
the questions are following:</p>
<ol>
<li>can I load weights manually, without using slicer to download weights in case of bad network situation</li>
<li>can I use my own trained weight and model to infer the segmentation with your code framework<br>
thank you</li>
</ol>

---

## Post #18 by @rbumm (2023-02-21 06:19 UTC)

<p>Thanks for the details. Please allow some time for checking this out with the developer of TotalSegmentator and on our own systems.</p>

---

## Post #19 by @rbumm (2023-02-21 08:44 UTC)

<p>Just tested this with a fresh 3D Slicer 5.3.0.<br>
PyTorch and TotalSegmentator installed fine with no problems.</p>
<p>Please understand that the TotalSegmentator extension wraps the program for ease of use in 3D Slicer, and the original code is maintained <a href="https://github.com/wasserth/TotalSegmentator">here</a>.<br>
Your problem indicates a maybe regional network issue during access to Zenodo and similar problems have <a href="https://github.com/wasserth/TotalSegmentator/issues/70">already been reported</a> in the TotalSegmentator issue tracker on GitHub.</p>
<p>Please try installing Slicer and TS on a different machine or in a different network.</p>

---

## Post #20 by @wasserth (2023-02-21 09:26 UTC)

<p>You can download the weights manually and put them in the folder where 3D Slicer needs them. <a class="mention" href="/u/lassoan">@lassoan</a> can tell you where the weights are stored for the TotalSegmentator 3D Slicer extension.</p>
<p>The links to the weights can be seen here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/wasserth/TotalSegmentator/blob/master/totalsegmentator/libs.py#L75">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/blob/master/totalsegmentator/libs.py#L75" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/wasserth/TotalSegmentator/blob/master/totalsegmentator/libs.py#L75" target="_blank" rel="noopener nofollow ugc">wasserth/TotalSegmentator/blob/master/totalsegmentator/libs.py#L75</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="65" style="counter-reset: li-counter 64 ;">
          <li>        with zipfile.ZipFile(config_dir / "tmp_download_file.zip", 'r') as zip_f:</li>
          <li>            zip_f.extractall(config_dir)</li>
          <li>        print(f"  downloaded in {time.time()-st:.2f}s")</li>
          <li>    except Exception as e:</li>
          <li>        raise e</li>
          <li>    finally:</li>
          <li>        if tempfile.exists():</li>
          <li>            os.remove(tempfile)</li>
          <li>
          </li>
<li>
          </li>
<li class="selected">def download_pretrained_weights(task_id):</li>
          <li>
          </li>
<li>    if "TOTALSEG_WEIGHTS_PATH" in os.environ:</li>
          <li>        config_dir = Path(os.environ["TOTALSEG_WEIGHTS_PATH"]) / "nnUNet"</li>
          <li>    else:</li>
          <li>        # in docker container finding home not properly working therefore map to /tmp</li>
          <li>        home_path = Path("/tmp") if str(Path.home()) == "/" else Path.home()</li>
          <li>        config_dir = home_path / ".totalsegmentator/nnunet/results/nnUNet"</li>
          <li>    (config_dir / "3d_fullres").mkdir(exist_ok=True, parents=True)</li>
          <li>    (config_dir / "2d").mkdir(exist_ok=True, parents=True)</li>
          <li>
      </li>
</ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You could also replace those weights by your own trained weights. But you might easily run into problems doing this. You should be familiar with python when you do this.</p>

---

## Post #21 by @rbumm (2023-02-21 10:28 UTC)

<p>Thanks for your comment, <a class="mention" href="/u/wasserth">@wasserth</a>. I believe the weights are just at the “TOTALSEG_WEIGHTS_PATH” independent of 3D Slicer.</p>
<p>In Windows 11 I find the “3d_fullres” folder only once at</p>
<pre><code class="lang-auto">C:\Users\Rudolf\.totalsegmentator\nnunet\results\nnUNet\3d_fullres\
</code></pre>
<p>after a successful TotalSegmentator install.</p>

---

## Post #22 by @zhang_ming (2023-02-21 13:57 UTC)

<p>thank you very much<br>
and I have just find the path like you described  and I run the source TotalSegment code in linux and the path was ’ :~/.totalsegmentator/nnunet/results/nnUNet/3d_fullres’.<br>
and I have just put the weight zip files unzip there. the code run well , and the results were amazing<br>
thank you.</p>

---

## Post #23 by @lassoan (2023-03-15 15:15 UTC)

<p>5 posts were split to a new topic: <a href="/t/totalsegmentator-error-at-first-run-dummyfile-object-has-no-attribute-flush/28399">TotalSegmentator error at first run: ‘DummyFile’ object has no attribute ‘flush’</a></p>

---

## Post #24 by @xiaoli26 (2023-04-14 15:39 UTC)

<p>That’s right! Thank you very much!</p>

---

## Post #25 by @17banai99 (2024-04-06 14:28 UTC)

<p>Hello,<br>
I want to now if totalsegmenter goes fast with mac book M2, and which modules does it requere?<br>
Thanks</p>

---

## Post #26 by @lassoan (2024-04-06 14:56 UTC)

<p>AI support in Apple Silicon systems is still lagging behind. Apple MPS acceleration is available now for some pytorch features, which significantly improves speed. However, MPS-accelerated pytorch is not usable for TotalSegmentator yet, because <a href="https://github.com/wasserth/TotalSegmentator/issues/250">some features required by nn-UNet are not supported</a>.</p>

---

## Post #27 by @17banai99 (2024-04-06 15:34 UTC)

<p>So you don’t advise me to buy MacOs for 3d slicer?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15f0329bc2619eeb6dd9df82bb48c29198142bcc.jpeg" data-download-href="/uploads/short-url/384Eb7GlG07dcSWZSvIaPXjS7Za.jpeg?dl=1" title="IMG_2782" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f0329bc2619eeb6dd9df82bb48c29198142bcc_2_666x500.jpeg" alt="IMG_2782" data-base62-sha1="384Eb7GlG07dcSWZSvIaPXjS7Za" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f0329bc2619eeb6dd9df82bb48c29198142bcc_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f0329bc2619eeb6dd9df82bb48c29198142bcc_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f0329bc2619eeb6dd9df82bb48c29198142bcc_2_1332x1000.jpeg 2x" data-dominant-color="6E655D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_2782</span><span class="informations">4032×3024 2.99 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However i have done this with mac book air M2🤔</p>

---

## Post #28 by @pieper (2024-04-06 15:39 UTC)

<p>Generally Slicer on mac systems works pretty well most operations, however ML models aren’t as well supported since most of that work requires Nvidia systems for top performance currently.  That may change in the future, but that’s the state of things now.</p>

---

## Post #29 by @Nicolas_Larragueta (2024-07-31 14:16 UTC)

<p>I have a similar problem, can you help me? Thank you</p>
<p>Traceback (most recent call last):<br>
File “”, line 5, in <br>
File “”, line 148, in <br>
File “C:/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 971, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1045, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 817, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/3DSlicer/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\3DSlicer\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/Familia Larragueta/AppData/Local/Temp/Slicer/__SlicerTemp__2024-07-31_11+15+21.031/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Familia Larragueta/AppData/Local/Temp/Slicer/__SlicerTemp__2024-07-31_11+15+21.031/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’, ‘–device’, ‘cpu’]’ returned non-zero exit status 1.</p>

---

## Post #30 by @lassoan (2024-08-01 07:43 UTC)

<p>You probably have either ran out of memory (try on a smaller, lower-resolution CT) or there were problems installing required libraries. Please check the application log to get hints on what exactly happened.</p>

---
