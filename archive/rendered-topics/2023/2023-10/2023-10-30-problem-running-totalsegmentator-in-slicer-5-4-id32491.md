# Problem running TotalSegmentator in Slicer-5.4

**Topic ID**: 32491
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/problem-running-totalsegmentator-in-slicer-5-4/32491

---

## Post #1 by @Investigacion_y_des1 (2023-10-30 18:41 UTC)

<p>Hi ! I have a question, do the previous version works with Slicer 5.4? because I’m not been able to run it on my pc. I will appreciate an answer, best regards.</p>

---

## Post #2 by @lassoan (2023-10-30 18:58 UTC)

<p>Yes, TotalSegmentator extension still works well in Slicer-5.4. It uses the TotalSegmentator v1 model. There are constant updates in Python packages and so we had to make some fixes recently. If you experience any problems then I would recommend to reinstall Slicer (remove the existing application installation folder completely; or reinstall Slicer in a completely new folder) and then install TotalSegmentator extension.</p>

---

## Post #3 by @philippe (2024-02-19 18:15 UTC)

<p>Hello,</p>
<p>I tried TotalSegmentator v2 within Slicer 5.6.1.<br>
The limbs are missing (below the knee / humerus) on all CTs I tried (5).</p>
<p>Version 5.5 is mentioned there:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/238">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/238" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/238" target="_blank" rel="noopener nofollow ugc">bug : bones extremities segmentation task does not work</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-11-26" data-time="06:44:11" data-timezone="UTC">06:44AM - 26 Nov 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/ivanstepanovftw" target="_blank" rel="noopener nofollow ugc">
          <img alt="ivanstepanovftw" src="https://avatars.githubusercontent.com/u/8203898?v=4" class="onebox-avatar-inline" width="20" height="20">
          ivanstepanovftw
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">```
Traceback (most recent call last):
  File "/home/i/Downloads/Slicer-5.4.0-<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">linux-amd64/bin/Python/slicer/util.py", line 3146, in tryWithErrorDisplay
    yield
  File "/home/i/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py", line 271, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "/home/i/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py", line 790, in process
    self.readSegmentation(outputSegmentation, outputSegmentationFile, task)
  File "/home/i/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py", line 864, in readSegmentation
    labelValueToSegmentName = class_map[task]
KeyError: 'bones_extremities'
```
Using CPU only on Fedora. Reproduce is as usual: selected bones extremities, create new segmentation on apply, then clicked on Apply.
More logs

&lt;details&gt;&lt;summary&gt;Details&lt;/summary&gt;
&lt;p&gt;

```
Processing started
Writing input file to /tmp/Slicer-i/__SlicerTemp__2023-11-26_09+37+05.403/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI (pre-run)...
Total Segmentator arguments: ['-i', '/tmp/Slicer-i/__SlicerTemp__2023-11-26_09+37+05.403/total-segmentator-input.nii', '-o', '/tmp/Slicer-i/__SlicerTemp__2023-11-26_09+37+05.403/segmentation', '--fast']
/home/i/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/bin/TotalSegmentator:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import require
/home/i/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.1.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
/home/i/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/torch/cuda/amp/grad_scaler.py:125: UserWarning: torch.cuda.amp.GradScaler is enabled, but CUDA is not available.  Disabling.
  warnings.warn(
/home/i/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/torch/amp/autocast_mode.py:250: UserWarning: User provided device_type of 'cuda', but CUDA is not available. Disabling
  warnings.warn(

If you use this tool please cite: https://doi.org/10.48550/arXiv.2208.05868

No GPU detected. Running on CPU. This can be very slow. The '--fast' option can help to some extend.
Using 'fast' option: resampling to lower resolution (3mm)
Resampling...
  Resampled in 3.14s
Predicting...

If you use this tool please cite: https://doi.org/10.48550/arXiv.2208.05868

No GPU detected. Running on CPU. This can be very slow. The '--fast' option can help to some extend.
Using 'fast' option: resampling to lower resolution (3mm)
Resampling...
  Resampled in 3.14s
Predicting...
  Predicted in 10.04s
Resampling...
Saving segmentations...

  0%|          | 0/104 [00:00&lt;?, ?it/s]
  1%|          | 1/104 [00:11&lt;20:03, 11.69s/it]
  7%|▋         | 7/104 [00:12&lt;02:13,  1.38s/it]
  8%|▊         | 8/104 [00:15&lt;02:36,  1.63s/it]
  9%|▊         | 9/104 [00:15&lt;02:08,  1.35s/it]
 10%|▉         | 10/104 [00:15&lt;01:41,  1.08s/it]
 12%|█▎        | 13/104 [00:16&lt;00:53,  1.69it/s]
 13%|█▎        | 14/104 [00:16&lt;00:54,  1.66it/s]
 14%|█▍        | 15/104 [00:17&lt;01:02,  1.44it/s]
 15%|█▌        | 16/104 [00:18&lt;00:55,  1.59it/s]
 17%|█▋        | 18/104 [00:18&lt;00:34,  2.47it/s]
 18%|█▊        | 19/104 [00:18&lt;00:35,  2.41it/s]
 19%|█▉        | 20/104 [00:18&lt;00:28,  2.95it/s]
 20%|██        | 21/104 [00:19&lt;00:24,  3.43it/s]
 21%|██        | 22/104 [00:20&lt;00:39,  2.06it/s]
 22%|██▏       | 23/104 [00:20&lt;00:32,  2.47it/s]
 23%|██▎       | 24/104 [00:20&lt;00:26,  3.04it/s]
 24%|██▍       | 25/104 [00:21&lt;00:30,  2.56it/s]
 25%|██▌       | 26/104 [00:21&lt;00:26,  2.94it/s]
 26%|██▌       | 27/104 [00:21&lt;00:21,  3.61it/s]
 27%|██▋       | 28/104 [00:21&lt;00:23,  3.23it/s]
 28%|██▊       | 29/104 [00:22&lt;00:24,  3.12it/s]
 30%|██▉       | 31/104 [00:22&lt;00:21,  3.34it/s]
 31%|███       | 32/104 [00:23&lt;00:24,  2.94it/s]
 33%|███▎      | 34/104 [00:23&lt;00:19,  3.56it/s]
 34%|███▎      | 35/104 [00:23&lt;00:21,  3.21it/s]
 36%|███▌      | 37/104 [00:24&lt;00:18,  3.66it/s]
 37%|███▋      | 38/104 [00:24&lt;00:21,  3.12it/s]
 38%|███▊      | 39/104 [00:25&lt;00:20,  3.19it/s]
 38%|███▊      | 40/104 [00:25&lt;00:17,  3.65it/s]
 39%|███▉      | 41/104 [00:25&lt;00:23,  2.67it/s]
 41%|████▏     | 43/104 [00:26&lt;00:18,  3.26it/s]
 42%|████▏     | 44/104 [00:26&lt;00:19,  3.15it/s]
 43%|████▎     | 45/104 [00:27&lt;00:26,  2.19it/s]
 44%|████▍     | 46/104 [00:27&lt;00:24,  2.33it/s]
 45%|████▌     | 47/104 [00:29&lt;00:44,  1.28it/s]
 47%|████▋     | 49/104 [00:30&lt;00:28,  1.91it/s]
 48%|████▊     | 50/104 [00:30&lt;00:24,  2.17it/s]
 49%|████▉     | 51/104 [00:30&lt;00:20,  2.62it/s]
 50%|█████     | 52/104 [00:30&lt;00:16,  3.06it/s]
 51%|█████     | 53/104 [00:31&lt;00:18,  2.78it/s]
 53%|█████▎    | 55/104 [00:31&lt;00:14,  3.40it/s]
 54%|█████▍    | 56/104 [00:31&lt;00:14,  3.39it/s]
 55%|█████▍    | 57/104 [00:31&lt;00:12,  3.86it/s]
 56%|█████▌    | 58/104 [00:32&lt;00:10,  4.21it/s]
 57%|█████▋    | 59/104 [00:32&lt;00:12,  3.59it/s]
 59%|█████▊    | 61/104 [00:32&lt;00:10,  4.21it/s]
 60%|█████▉    | 62/104 [00:33&lt;00:10,  3.86it/s]
 61%|██████    | 63/104 [00:33&lt;00:09,  4.13it/s]
 62%|██████▏   | 64/104 [00:33&lt;00:08,  4.45it/s]
 62%|██████▎   | 65/104 [00:34&lt;00:11,  3.47it/s]
 64%|██████▍   | 67/104 [00:34&lt;00:08,  4.32it/s]
 65%|██████▌   | 68/104 [00:34&lt;00:11,  3.15it/s]
 66%|██████▋   | 69/104 [00:35&lt;00:10,  3.21it/s]
 67%|██████▋   | 70/104 [00:35&lt;00:09,  3.74it/s]
 68%|██████▊   | 71/104 [00:35&lt;00:10,  3.00it/s]
 70%|███████   | 73/104 [00:36&lt;00:07,  4.20it/s]
 71%|███████   | 74/104 [00:36&lt;00:08,  3.48it/s]
 72%|███████▏  | 75/104 [00:36&lt;00:08,  3.42it/s]
 73%|███████▎  | 76/104 [00:37&lt;00:07,  3.75it/s]
 74%|███████▍  | 77/104 [00:37&lt;00:07,  3.44it/s]
 76%|███████▌  | 79/104 [00:37&lt;00:05,  4.88it/s]
 77%|███████▋  | 80/104 [00:37&lt;00:05,  4.00it/s]
 78%|███████▊  | 81/104 [00:38&lt;00:05,  3.92it/s]
 79%|███████▉  | 82/104 [00:38&lt;00:05,  4.12it/s]
 80%|███████▉  | 83/104 [00:38&lt;00:05,  3.87it/s]
 82%|████████▏ | 85/104 [00:38&lt;00:03,  5.56it/s]
 83%|████████▎ | 86/104 [00:39&lt;00:04,  4.38it/s]
 84%|████████▎ | 87/104 [00:39&lt;00:04,  4.07it/s]
 85%|████████▍ | 88/104 [00:39&lt;00:04,  3.87it/s]
 86%|████████▌ | 89/104 [00:40&lt;00:03,  3.76it/s]
 88%|████████▊ | 91/104 [00:40&lt;00:02,  5.52it/s]
 88%|████████▊ | 92/104 [00:40&lt;00:02,  4.29it/s]
 89%|████████▉ | 93/104 [00:40&lt;00:02,  4.35it/s]
 90%|█████████ | 94/104 [00:41&lt;00:02,  3.77it/s]
 91%|█████████▏| 95/104 [00:41&lt;00:02,  3.75it/s]
 93%|█████████▎| 97/104 [00:41&lt;00:01,  5.29it/s]
 94%|█████████▍| 98/104 [00:42&lt;00:01,  4.40it/s]
 95%|█████████▌| 99/104 [00:42&lt;00:01,  4.50it/s]
 96%|█████████▌| 100/104 [00:42&lt;00:01,  3.94it/s]
 97%|█████████▋| 101/104 [00:42&lt;00:00,  4.18it/s]
 99%|█████████▉| 103/104 [00:43&lt;00:00,  6.11it/s]
100%|██████████| 104/104 [00:43&lt;00:00,  6.56it/s]
100%|██████████| 104/104 [00:43&lt;00:00,  2.41it/s]
  Saved in 44.44s
Creating segmentations with TotalSegmentator AI...
Total Segmentator arguments: ['-i', '/tmp/Slicer-i/__SlicerTemp__2023-11-26_09+37+05.403/total-segmentator-input.nii', '-o', '/tmp/Slicer-i/__SlicerTemp__2023-11-26_09+37+05.403/segmentation', '--ml', '--task', 'bones_extremities']
/home/i/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/bin/TotalSegmentator:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import require
/home/i/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.1.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "

If you use this tool please cite: https://doi.org/10.48550/arXiv.2208.05868

No GPU detected. Running on CPU. This can be very slow. The '--fast' option can help to some extend.

This model is only available upon purchase of a license (free licenses available for academic projects).
Contact jakob.wasserthal@usb.ch if you are interested.

Importing segmentation results...
```

&lt;/p&gt;
&lt;/details&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
but not available in the collection of older slicer packages on Kitware’s site (5.4-&gt;5.6).</p>
<p>Did anyone have luck with the limbs?<br>
Using which version of slicer?</p>
<p>Thanks<br>
Philippe<br>
PS: i’ll post on github too and update if I have a response</p>

---

## Post #4 by @jamesobutler (2024-02-19 20:22 UTC)

<p>TotalSegmentator v2 began to work with Slicer Preview 5.5 which ultimately became Slicer Stable 5.6.x. So using Slicer 5.6.1 is sufficient for your case and going back to Slicer 5.5 won’t get you anything more.</p>
<p>Are the segment tasks that you are expecting in the list of the ones available in v2? Do you have a license for the ones that require a license? See below:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/wasserth/TotalSegmentator?tab=readme-ov-file#subtasks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/wasserth/TotalSegmentator?tab=readme-ov-file#subtasks" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/ceb1264f311b9f31e7a5705fb8f9e4e228513e286a47b895d5a3f36a38d47662/wasserth/TotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/wasserth/TotalSegmentator?tab=readme-ov-file#subtasks" target="_blank" rel="noopener nofollow ugc">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of &gt;100...</a></h3>

  <p>Tool for robust segmentation of &gt;100 important anatomical structures in CT images - wasserth/TotalSegmentator</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbumm (2024-02-20 10:33 UTC)

<p>Maybe you can get a free academic license if you contact Jakob Wasserthal from TotalSegmentator.</p>

---

## Post #6 by @philippe (2024-02-20 10:44 UTC)

<aside class="quote no-group" data-username="philippe" data-post="3" data-topic="32491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f14d63/48.png" class="avatar"> philippe:</div>
<blockquote>
<p>Philippe<br>
PS: i’ll post on git</p>
</blockquote>
</aside>
<p>Dummy me. I did not realize that they called the extremities “appendicular bones”.<br>
Thanks for the pointer. I’ll ask a license</p>

---

## Post #7 by @philippe (2024-02-20 12:31 UTC)

<p>Sorry to post again.<br>
I got a license but there is an error installing it:</p>
<pre><code class="lang-auto">Failed to set TotalSegmentator license.

Command '['C:/Users/-------/AppData/Local/slicer.org/Slicer 5.6.1/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\-------\\AppData\\Local\\slicer.org\\Slicer 5.6.1\\lib\\Python\\Scripts\\totalseg_set_license.exe', '-l', '

Traceback (most recent call last):
  File "C:\\Users\\-------\\AppData\\Local\\slicer.org\\Slicer 5.6.1\\bin\\Python\\slicer\\util.py", line 3255, in tryWithErrorDisplay
    yield
  File "C:/Users/-------/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 318, in onSetLicense
    self.logic.setlicense(self.ui.licenseLineEdit.text)
  File "C:/Users/-------/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 831, in setlicense
    licenseToolOutput = self.logProcessOutput(proc, returnOutput=True)
  File "C:/Users/-------/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 779, in logProcessOutput
    if not line:
UnboundLocalError: local variable \'line\' referenced before assignment']' returned non-zero exit status 1.
</code></pre>
<p>The error is related to line 779:</p>
<pre><code class="lang-auto">try:
                line = proc.stdout.readline()
except UnicodeDecodeError as e:
                # Code page conversion happens because `universal_newlines=True` sets process output to text mode,
                # and it fails because probably system locale is not UTF8. We just ignore the error and discard the string,
                # as we only guarantee correct behavior if an UTF8 locale is used.
</code></pre>
<p>My PC is in french. Slicer is set in english.<br>
There are no special characters in the license key;<br>
Total segmentator works fine otherwise.</p>
<p>Any idea on how to solve it?<br>
Thanks<br>
Philippe</p>

---

## Post #8 by @rbumm (2024-02-20 15:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> could you please check this? Thank you</p>

---

## Post #9 by @lassoan (2024-02-20 18:46 UTC)

<p>Thank you, I’ve <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/f838b29c191fa799394324f66d348661ce489f60">pushed a fix</a> that will be available in the extensions manager from tomorrow. Please update the extension tomorrow and try again.</p>

---

## Post #10 by @philippe (2024-02-21 19:17 UTC)

<p>Thanks a lot.<br>
I confirm the license is working now.<br>
Philippe</p>

---

## Post #11 by @lassoan (2024-02-21 19:18 UTC)

<p>Awesome, thanks for testing.</p>

---

## Post #12 by @rnvwnvvir (2024-02-23 08:43 UTC)

<p>Hello,my slicer is 3.6.1.The following error occurs when using TotalSegmentator.<br>
Restart is unuseful.</p>
<p>Application is required to complete installation of required Python packages.</p>
<p>Press OK to restart.</p>

---
