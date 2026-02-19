---
topic_id: 28399
title: "Totalsegmentator Error At First Run Dummyfile Object Has No"
date: 2023-03-15
url: https://discourse.slicer.org/t/28399
---

# TotalSegmentator error at first run: ‘DummyFile’ object has no attribute ‘flush’

**Topic ID**: 28399
**Date**: 2023-03-15
**URL**: https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-dummyfile-object-has-no-attribute-flush/28399

---

## Post #1 by @antoniozidaric (2023-03-15 11:55 UTC)

<p>Hi Iassoan, I’m trying to use the TotalSegmentator Tool but i receive this error below the Apply button:</p>
<p>RuntimeError: FIND was unable to find an engine to execute this computation</p>
<p>Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000002765B9EE4F0&gt;</p>
<p>AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>I checked if could be an error due to the GPU’s memory but on my laptop is 10Gb of Memory.<br>
Thanks for you time<br>
AZ</p>

---

## Post #2 by @rbumm (2023-03-15 14:01 UTC)

<p>Could you provide some more details? What is the brand and model of the GPU?</p>

---

## Post #3 by @antoniozidaric (2023-03-15 14:38 UTC)

<p>Sure. The model is “GPU intel(r) uhd graphics 620”</p>

---

## Post #4 by @rbumm (2023-03-15 14:55 UTC)

<p>Unfortunately, GPU processing will require an NVIDIA GPU, so you could switch to CPU processing which will take longer to run (30 minutes vs. 2 minutes).</p>
<p>Switch here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d66d7eb21328ccbba07cb9e671e3d8670f5c8f4.png" alt="image" data-base62-sha1="msriQb13I95Iy7iMB2SscOm1X80" width="406" height="403"></p>

---

## Post #5 by @antoniozidaric (2023-03-15 15:13 UTC)

<p>I don’t know why but it doesn’t switch the computation on CPU, it still remain on GPU and ask me if i want to enable the ‘fast’ mode.</p>

---

## Post #6 by @lassoan (2023-03-15 15:17 UTC)

<p>You need to uninstall the GPU version of pytorch, restart Slicer, and install the CPU version of pytorch - as described<br>
<a href="https://github.com/lassoan/SlicerTotalSegmentator#segmentation-fails-while-predicting">here</a>.</p>

---

## Post #7 by @antoniozidaric (2023-03-15 15:23 UTC)

<p>Ok, now it is correctly working. Thank you so much for your time</p>

---

## Post #8 by @J_UWA (2023-05-09 04:59 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>, I have uninstalled the GPU version of pytorch, restart Slicer, and install the CPU version of pytorch. However, still encountering the same error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c59e6862492e07d227a0383ebc25adfe2afa35a.png" data-download-href="/uploads/short-url/mj95Y8tEXLdNWLoy2fm0q8Zl9PQ.png?dl=1" title="Screenshot 2023-05-09 125818" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c59e6862492e07d227a0383ebc25adfe2afa35a.png" alt="Screenshot 2023-05-09 125818" data-base62-sha1="mj95Y8tEXLdNWLoy2fm0q8Zl9PQ" width="690" height="166" data-dominant-color="F0F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-09 125818</span><span class="informations">1082×261 9.87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2023-05-09 10:45 UTC)

<p>What is the installed pytorch version?</p>

---

## Post #10 by @J_UWA (2023-05-09 16:02 UTC)

<p>I found your other post here.</p><aside class="quote quote-modified" data-post="7" data-topic="26755">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/augusto/48/17710_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-command-python-scripts-totalsegmentator-returned-non-zero-exit-status-120/26755/7">TotalSegmentator error at first run: Command ...Python\Scripts\TotalSegmentator... returned non-zero exit status 120</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    For the time being, since i have slicer installed in a computer which, by default, has no internet acess, i cannot download the sample data set and test TotalSegmentator with it. As soon as i have acess to internet, i will try. 
The messages that appear after the Apply button are as follows: 
Processing started 
Writing input file to C:/Users/Augusto/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-15_21+10+39.789/total-segmentator-input.nii 
Creating segmentations with TotalSegmentator AI… 
Tota…
  </blockquote>
</aside>

<p>It’s been resolved. Thank you !</p>

---

## Post #11 by @yongchanghuang95 (2024-06-21 09:46 UTC)

<p>I’m having the same problem，somebody can analysis for me？</p>
<blockquote>
<p>The “DummyFile” object does not have a “flush” attribute<br>
returned non-zero exit status 120.</p>
</blockquote>
<p>I can not find the information about <strong>The “DummyFile” object does not have a “flush” attribute</strong></p>
<p>the follow  pytorch version detail :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c6284eb5f0fa0ba6c86ef07fec8357120577e9.png" data-download-href="/uploads/short-url/jENXKYeBw0oHVYFzOjXyfhUbYlr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89c6284eb5f0fa0ba6c86ef07fec8357120577e9_2_690x287.png" alt="image" data-base62-sha1="jENXKYeBw0oHVYFzOjXyfhUbYlr" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89c6284eb5f0fa0ba6c86ef07fec8357120577e9_2_690x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c6284eb5f0fa0ba6c86ef07fec8357120577e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89c6284eb5f0fa0ba6c86ef07fec8357120577e9.png 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">985×410 23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>error detail :</p>
<pre data-code-wrap="Processing"><code class="lang-Processing">Writing input file to C:/Users/26686/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-21_17+33+47.251/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI (pre-run)...
Total Segmentator arguments: ['-i', 'C:/Users/26686/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-21_17+33+47.251/total-segmentator-input.nii', '-o', 'C:/Users/26686/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-21_17+33+47.251/segmentation', '--fast']
D:\Slicer 5.6.2\lib\Python\Lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
D:\Slicer 5.6.2\lib\Python\Lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
D:\Slicer 5.6.2\lib\Python\Lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
multiprocessing.pool.RemoteTraceback:
"""
Traceback (most recent call last):
  File "D:\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
  File "D:\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py", line 51, in starmapstar
    return list(itertools.starmap(args[0], args[1]))
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\export_prediction.py", line 39, in export_prediction_from_softmax
    segmentation = label_manager.convert_logits_to_segmentation(predicted_array_or_file)
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\utilities\label_handling\label_handling.py", line 182, in convert_logits_to_segmentation
    return self.convert_probabilities_to_segmentation(probabilities)
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\utilities\label_handling\label_handling.py", line 175, in convert_probabilities_to_segmentation
    segmentation = predicted_probabilities.argmax(0)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 6.85 GiB for an array with shape (287, 233, 233, 118) and data type float32
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "D:\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "D:\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 127, in main
    totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 293, in totalsegmentator
    seg_img, ct_img = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 395, in nnUNet_predict_image
    nnUNetv2_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta,
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 178, in nnUNetv2_predict
    predict_from_raw_data(dir_in,
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 347, in predict_from_raw_data
    [i.get() for i in r]
  File "D:\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 347, in &lt;listcomp&gt;
    [i.get() for i in r]
  File "D:\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py", line 771, in get
    raise self._value
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 6.85 GiB for an array with shape (287, 233, 233, 118) and data type float32
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000001E2BB5F6B20&gt;
AttributeError: 'DummyFile' object has no attribute 'flush'

If you use this tool please cite: https://pubs.rsna.org/doi/10.1148/ryai.230024

Using 'fast' option: resampling to lower resolution (3mm)
Resampling...
  Resampled in 4.25s
Predicting...
type or paste code here
</code></pre>

---

## Post #12 by @lassoan (2024-06-21 12:32 UTC)

<p><code>AttributeError: 'DummyFile' object has no attribute 'flush'</code> is a <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/README.md#attributeerror-dummyfile-object-has-no-attribute-flush">false alarm</a>, you can ignore this message.</p>
<p>In general, you need to look for the first error in the output - all further errors may be consequences of the first one. In your case, the first error was that you have ran out of memory:</p>
<aside class="quote no-group" data-username="yongchanghuang95" data-post="11" data-topic="28399">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bbce88/48.png" class="avatar"> yongchanghuang95:</div>
<blockquote>
<pre><code class="lang-auto">numpy.core._exceptions._ArrayMemoryError: Unable to allocate 6.85 GiB for an array with shape (287, 233, 233, 118) and data type float32
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000001E2BB5F6B20&gt;
AttributeError: 'DummyFile' object has no attribute 'flush'
</code></pre>
</blockquote>
</aside>
<p>To solve the issue, you need to reduce the image size or increase available memory size. See detailed instructions <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/README.md#numpycore_exceptions_arraymemoryerror-unable-to-allocate">here</a>.</p>

---

## Post #13 by @yongchanghuang95 (2024-06-24 01:25 UTC)

<p>Many thanks for taking the time to respond，I try  set up the bigger virtual memory to run again。</p>

---
