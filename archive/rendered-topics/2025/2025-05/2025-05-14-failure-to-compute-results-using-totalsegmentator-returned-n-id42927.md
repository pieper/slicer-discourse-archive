# Failure to Compute Results using TotalSegmentator (returned non-zero exist status 1)

**Topic ID**: 42927
**Date**: 2025-05-14
**URL**: https://discourse.slicer.org/t/failure-to-compute-results-using-totalsegmentator-returned-non-zero-exist-status-1/42927

---

## Post #1 by @tjlotz (2025-05-14 16:25 UTC)

<p>Hello Slicer Support!</p>
<p>I have been trying to run TotalSegmentator, but it has been failing. The Slicer Error message that I have been receiving states, “… returned non-zero exit status 1.”</p>
<p>Can you please help me understand the issue? I have copy-and-pasted the full error message and process log below. Thank you!</p>
<pre><code class="lang-auto">Failed to compute results.

Command '['C:/Users/Gradient/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Gradient\\AppData\\Local\\slicer.org\\Slicer 5.8.1\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Gradient/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-14_10+38+28.644/total-segmentator-input.nii', '-o', 'C:/Users/Gradient/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-14_10+38+28.644/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>
<p>The process log information is as follows:</p>
<pre><code class="lang-auto">Processing started
Writing input file to C:/Users/Gradient/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-14_10+38+28.644/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI...
Total Segmentator arguments: ['-i', 'C:/Users/Gradient/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-14_10+38+28.644/total-segmentator-input.nii', '-o', 'C:/Users/Gradient/AppData/Local/Temp/Slicer/__SlicerTemp__2025-05-14_10+38+28.644/segmentation', '--ml', '--task', 'total']
Traceback (most recent call last):
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 143, in main
    totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 620, in totalsegmentator
    seg_img, ct_img, stats = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 440, in nnUNet_predict_image
    img_in_rsp = change_spacing(img_in, resample,
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\resampling.py", line 204, in change_spacing
    new_data = resample_img(data, zoom=zoom, order=order, nr_cpus=nr_cpus)  # cpu resampling
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\resampling.py", line 48, in resample_img
    img_sm = Parallel(n_jobs=nr_cpus)(delayed(_process_gradient)(grad_idx) for grad_idx in range(img.shape[3]))
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\joblib\parallel.py", line 1985, in __call__
    return output if self.return_generator else list(output)
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\joblib\parallel.py", line 1913, in _get_sequential_output
    res = func(*args, **kwargs)
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\totalsegmentator\resampling.py", line 37, in _process_gradient
    return ndimage.zoom(img[:, :, :, grad_idx], zoom, order=order)
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\scipy\ndimage\_interpolation.py", line 837, in zoom
    filtered = spline_filter(padded, order, output=numpy.float64,
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\scipy\ndimage\_interpolation.py", line 196, in spline_filter
    output = _ni_support._get_output(output, input,
  File "C:\Users\Gradient\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\scipy\ndimage\_ni_support.py", line 88, in _get_output
    output = numpy.zeros(shape, dtype=output)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.18 GiB for an array with shape (512, 512, 603) and data type float64
No GPU detected. Running on CPU. This can be very slow. The '--fast' or the `--roi_subset` option can help to reduce runtime.

If you use this tool please cite: https://pubs.rsna.org/doi/10.1148/ryai.230024

Resampling...
</code></pre>

---

## Post #2 by @lassoan (2025-05-14 16:28 UTC)

<blockquote>
<p>numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.18 GiB for an array with shape (512, 512, 603) and data type float64</p>
</blockquote>
<p>You have run out of memory. See tips on how to reduce memory usage or increase available memory space in the <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#problem-error-popup-on-the-first-run-failed-to-compute-results--command--pythonslicer-totalsegmentatorexe--returned-non-zero-exit-status-120">module documentation</a>.</p>

---

## Post #4 by @tjlotz (2025-05-15 16:22 UTC)

<aside class="quote no-group quote-modified" data-username="tjlotz" data-post="3" data-topic="42927" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tjlotz/48/80202_2.png" class="avatar"> tjlotz:</div>
<blockquote>
<p>Thank you for the quick response!</p>
<p>I am currently using my MacBook because I am traveling for work. However, I can setup Slicer on my PC at home after my trip. I suspect that will solve the problem caused by limited memory space. If not, I’ll review the tips for reducing memory usage and/or increasing memory space and try again.</p>
</blockquote>
</aside>
<p>Thank you for the quick response!</p>
<p>I am currently using my MacBook because I am traveling for work. However, I can setup Slicer on my PC at home after my trip. I suspect that will solve the problem caused by limited memory space. If not, I’ll review the tips for reducing memory usage and/or increasing memory space and try again.</p>

---
