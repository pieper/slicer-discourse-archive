# TotalSegmentator returned non-zero exit status 1

**Topic ID**: 31668
**Date**: 2023-09-13
**URL**: https://discourse.slicer.org/t/totalsegmentator-returned-non-zero-exit-status-1/31668

---

## Post #1 by @Windy (2023-09-13 03:35 UTC)

<p>When I click apply, fast mode, it gives the below error:</p>
<pre><code class="lang-auto">No GPU detected. Running on CPU. This can be very slow. The '--fast' option can help to some extend.
Using 'fast' option: resampling to lower resolution (3mm)
Resampling...
  Resampled in 0.10s
Predicting...
  Predicted in 4.10s
Traceback (most recent call last):
  File "C:\Users\sabe848\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\nibabel\loadsave.py", line 100, in load
    stat_result = os.stat(filename)
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\sabe848\\AppData\\Local\\Temp\\nnunet_tmp_3xtp4mqi\\s01.nii.gz'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\sabe848\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator", line 93, in &lt;module&gt;
    main()
  File "C:\Users\sabe848\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator", line 86, in main
    totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
  File "C:\Users\sabe848\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 173, in totalsegmentator
    seg = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,
  File "C:\Users\sabe848\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py", line 272, in nnUNet_predict_image
    img_pred = nib.load(tmp_dir / "s01.nii.gz")
  File "C:\Users\sabe848\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\nibabel\loadsave.py", line 102, in load
    raise FileNotFoundError(f"No such file or no access: '{filename}'")
FileNotFoundError: No such file or no access: 'C:\Users\sabe848\AppData\Local\Temp\nnunet_tmp_3xtp4mqi\s01.nii.gz'
</code></pre>

---
