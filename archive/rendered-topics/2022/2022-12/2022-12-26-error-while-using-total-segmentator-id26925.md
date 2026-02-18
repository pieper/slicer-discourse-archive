# Error While using 'Total Segmentator'

**Topic ID**: 26925
**Date**: 2022-12-26
**URL**: https://discourse.slicer.org/t/error-while-using-total-segmentator/26925

---

## Post #1 by @Dror1 (2022-12-26 15:07 UTC)

<p>hey all,</p>
<p>I’m having an error while trying to use the ‘total segmentator’ module.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\dror\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/dror/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 248, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/Users/dror/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 532, in setupPythonRequirements<br>
slicer.util.pip_install(totalSegmentatorPackage + " --no-deps" + (" --upgrade" if upgrade else “”))<br>
File “C:\Users\dror\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3571, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\dror\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3533, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\dror\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3502, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/dror/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/wasserth/TotalSegmentator.git’, ‘–no-deps’]’ returned non-zero exit status 1.</p>
<p>Does anyone know how to fix it?</p>

---

## Post #2 by @lassoan (2022-12-26 15:25 UTC)

<p>Totalsegmentator is downloaded using git (revision control tool), therefore you need to have git installed on your system. If you update the extension to the latest version then it automatically offers to install it. If this does not work for you for any reason then you can install git manually from <a href="https://git-scm.com/download">here</a>. After git installation, restart your computer and TotalSegmentator installation should succeed. If there is still problem then let me know and I send further instructions.</p>

---

## Post #4 by @Dror1 (2022-12-27 07:32 UTC)

<p>Thank you very much, it’s working.</p>

---

## Post #5 by @RenskeS (2022-12-27 09:38 UTC)

<p>I got the exact same error message while using the TotalSegmentator module. I did already install git (git version 2.39.0.windows.2), restarted Slicer and my laptop, but still get the same message when pressing “Apply” in the module. What could be other possibilities to fix this error?</p>
<p>Thanks in advance for thinking along!</p>

---

## Post #6 by @rbumm (2022-12-27 12:46 UTC)

<p>If you are on Windows, could you try to install TotalSegmentator from the command line:</p>
<pre><code class="lang-auto">"C:\Users\yourname\AppData\Local\NA-MIC\Slicer 5.2.1\bin/PythonSlicer.EXE" -m pip install git+https://github.com/wasserth/TotalSegmentator.git --no-deps
</code></pre>
<p>and post eventual error messages?</p>

---

## Post #7 by @RenskeS (2022-12-27 13:00 UTC)

<p>I do not get an error message when entering the command line and installing TotalSegmentator, the installation is fully successful. Unfortunately, I still get the same error when applying the module in Slicer.</p>

---

## Post #8 by @rbumm (2022-12-27 13:07 UTC)

<p>Are you getting any messages here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e14ae4fe74657ebf040e76db1602be2f1cd8670.png" data-download-href="/uploads/short-url/b8JybkaKlTXLVG9q9tc5I1nCyKA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e14ae4fe74657ebf040e76db1602be2f1cd8670_2_689x390.png" alt="image" data-base62-sha1="b8JybkaKlTXLVG9q9tc5I1nCyKA" width="689" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e14ae4fe74657ebf040e76db1602be2f1cd8670_2_689x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e14ae4fe74657ebf040e76db1602be2f1cd8670_2_1033x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e14ae4fe74657ebf040e76db1602be2f1cd8670.png 2x" data-dominant-color="A9A7A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1209×684 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you specify your hardware and run 3D Slicer in admin mode for a test?<br>
Please use the CTChest demo dataset from “Sample Data”</p>

---

## Post #9 by @RenskeS (2022-12-27 13:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19b91f6af189b47a5b955fe20e7ef9d3a0080c42.png" data-download-href="/uploads/short-url/3FyyK4eB3zKMUYAwvOIVsDweOOK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19b91f6af189b47a5b955fe20e7ef9d3a0080c42_2_690x329.png" alt="image" data-base62-sha1="3FyyK4eB3zKMUYAwvOIVsDweOOK" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19b91f6af189b47a5b955fe20e7ef9d3a0080c42_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19b91f6af189b47a5b955fe20e7ef9d3a0080c42_2_1035x493.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19b91f6af189b47a5b955fe20e7ef9d3a0080c42_2_1380x658.png 2x" data-dominant-color="66666E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×914 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what I get when running in admin mode.</p>
<p>I have Windows 10 Home on a Lenovo Thinkpad T460s with the following processor: Intel(R) Core™ i5-6200U CPU @ 2.30GHz, 2400 Mhz, 2 Core(s), 4 Logical Processor(s)</p>

---

## Post #10 by @rbumm (2022-12-27 13:41 UTC)

<p>What happens if you go to the “PyTorch” extension and press the button “Install PyTorch”? Probably the same?</p>

---

## Post #11 by @RenskeS (2022-12-27 15:51 UTC)

<p>Yes that is correct, then I get the same error</p>

---

## Post #12 by @rbumm (2022-12-27 16:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> has just made a helpful update of the PyTorch extension:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00b0bf51a0e1130c1afda4e137ce364713b579d0.png" alt="image" data-base62-sha1="66G7IIrnsUBvZYNVbUsLZOiLuw" width="548" height="386"></p>
<p>you may want to uninstall and reinstall PyTorch after updating. Please bear in mind that your laptop will run TotalSegmentator in CPU mode.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> it would be great if you could add a “Check CUDA” button</p>

---

## Post #13 by @RenskeS (2022-12-27 16:46 UTC)

<p>Thanks, I indeed read it somewhere else as well. This update fixed the first error I had, <a class="mention" href="/u/lassoan">@lassoan</a> thank you for that!</p>
<p>With the reinstalled PyTorch I got some errors for missing modules, which I pip installed. My access got denied when installing xvfbwrapper and it mentioned that I got a too new version of ITK-snap as well for totalsegmentator.  In Slicer I currently get the following error:</p>
<p>Processing started<br>
Writing input file to C:/Users/schra/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-27_17+37+33.895/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/schra/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-27_17+37+33.895/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/schra/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-27_17+37+33.895/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>with</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\schra\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/schra/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/schra/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 714, in process<br>
proc = slicer.util.launchConsoleProcess(totalSegmentatorCommand + options)<br>
File “C:\Users\schra\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3463, in launchConsoleProcess<br>
proc = subprocess.Popen(args, env=startupEnv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, startupinfo=info, cwd=cwd)<br>
File “C:\Users\schra\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\subprocess.py”, line 951, in <strong>init</strong><br>
self._execute_child(args, executable, preexec_fn, close_fds,<br>
File “C:\Users\schra\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\subprocess.py”, line 1420, in _execute_child<br>
hp, ht, pid, tid = _winapi.CreateProcess(executable, args,<br>
OSError: [WinError 193] %1 is not a valid Win32 application</p>
<p>Was installing the separate missing modules not the correct thing to do? And what can I do to overrule the denial of the missing xvfbwrapper module? Or is this not the way to go?</p>
<p>Again, thanks a lot for thinking along!</p>

---

## Post #14 by @RenskeS (2022-12-27 17:24 UTC)

<p>I managed to install the xvfbwrapper and right ITK-snap version. Everything seems to work now!</p>
<p>Thanks for the help!</p>

---

## Post #15 by @R.Boellaard (2022-12-28 14:13 UTC)

<p>Hi there,</p>
<p>I installed Git etc. I ininstalled PyTorch and got a message that it was installed. I then tried install PyTorch, but nothing happens, even not messages…is there any additional package I need such that pytorch wil be installed?</p>
<p>Thnx<br>
Ronald</p>

---

## Post #16 by @rbumm (2022-12-28 15:54 UTC)

<p>Hi Ronald,</p>
<p>Have you been using the PyTorch extension for uninstalling and then installing PyTorch <a href="https://discourse.slicer.org/t/error-while-using-total-segmentator/26925/12">as outlined above</a>?</p>

---

## Post #17 by @R.Boellaard (2022-12-28 16:17 UTC)

<p>Dear Rudolf</p>
<p>I tried several times and finally I disconnected my PC and used wifi with eduroam and now it was able to unistall and install pytorch. But I encountered the next error "Processing started</p>
<p>Writing input file to C:/Users/Ronald/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_17+14+28.271/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/Ronald/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_17+14+28.271/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Ronald/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_17+14+28.271/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 10, in </p>
<p>import nibabel as nib</p>
<p>ModuleNotFoundError: No module named ‘nibabel’</p>
<p>"</p>
<p>So, it seems i need to install the nibabel package. Should I do so within slider using the python window or do you recommend to do so thru cmd window.</p>
<p>Thnx<br>
Ronald</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5832dc008835c3900a4e9e67a9901d64ac773c27.png" alt="Outlook-cid_image0.png" data-base62-sha1="cAeYX8hOZYIXHrz3PKbK1hrrTGD" width="265" height="45"></p>

---

## Post #18 by @rbumm (2022-12-28 16:37 UTC)

<p>Please “Upgrade” the Totalsegmentator package first from the extension, now with running public WLAN.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/835ba999a8c24c9481ec43ea3eaaccae86ec910a.png" data-download-href="/uploads/short-url/iK2VWINXTsxIqkM6a0UsxdIoo8q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/835ba999a8c24c9481ec43ea3eaaccae86ec910a.png" alt="image" data-base62-sha1="iK2VWINXTsxIqkM6a0UsxdIoo8q" width="498" height="500" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">542×544 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If that does not help, you could pip install missing packages from the Python Interactor like this:</p>
<pre><code class="lang-auto">slicer.util.pip_install("nibabel")
</code></pre>

---

## Post #19 by @R.Boellaard (2022-12-28 16:57 UTC)

<p>Some steps further:-)</p>
<p>Still an error:<br>
Processing started<br>
Writing input file to C:/Users/Ronald/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_17+54+58.904/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/Ronald/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_17+54+58.904/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Ronald/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_17+54+58.904/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>preprocessing C:\Users\Ronald\AppData\Local\Temp\nnunet_tmp_8pv33ag1\s01.nii.gz<br>
using preprocessor GenericPreprocessor<br>
before crop: (1, 293, 200, 200) after crop: (1, 293, 200, 200) spacing: [3. 3. 3.]</p>
<p>no resampling necessary<br>
no resampling necessary<br>
before: {‘spacing’: array([3., 3., 3.]), ‘spacing_transposed’: array([3., 3., 3.]), ‘data.shape (data is transposed)’: (1, 293, 200, 200)}<br>
after:  {‘spacing’: array([3., 3., 3.]), ‘data.shape (data is resampled)’: (1, 293, 200, 200)}</p>
<p>(1, 293, 200, 200)<br>
This worker has ended successfully, no errors to report<br>
Traceback (most recent call last):<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 201, in <br>
main()<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 179, in main<br>
seg = nnUNet_predict_image(args.input, args.output, task_id, model=model, folds=folds,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 232, in nnUNet_predict_image<br>
nnUNet_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta)<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 106, in nnUNet_predict<br>
predict_from_folder(model_folder_name, dir_in, dir_out, folds, save_npz, num_threads_preprocessing,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 668, in predict_from_folder<br>
return predict_cases_fastest(model, list_of_lists[part_id::num_parts], output_files[part_id::num_parts], folds,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 493, in predict_cases_fastest<br>
res = trainer.predict_preprocessed_data_return_seg_and_softmax(d, do_mirroring=do_tta,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\training\network_training\nnUNetTrainerV2.py”, line 211, in predict_preprocessed_data_return_seg_and_softmax<br>
ret = super().predict_preprocessed_data_return_seg_and_softmax(data,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\training\network_training\nnUNetTrainer.py”, line 516, in predict_preprocessed_data_return_seg_and_softmax<br>
ret = self.network.predict_3D(data, do_mirroring=do_mirroring, mirror_axes=mirror_axes,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\network_architecture\neural_network.py”, line 147, in predict_3D<br>
res = self._internal_predict_3D_3Dconv_tiled(x, step_size, do_mirroring, mirror_axes, patch_size,<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\network_architecture\neural_network.py”, line 384, in _internal_predict_3D_3Dconv_tiled<br>
predicted_patch = self._internal_maybe_mirror_and_pred_3D(<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\network_architecture\neural_network.py”, line 510, in _internal_maybe_mirror_and_pred_3D<br>
result_torch = to_cuda(result_torch, gpu_id=self.get_device())<br>
File “C:\Users\Ronald\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\nnunet\utilities\to_torch.py”, line 31, in to_cuda<br>
data = data.cuda(gpu_id, non_blocking=non_blocking)<br>
RuntimeError: CUDA out of memory. Tried to allocate 356.00 MiB (GPU 0; 6.00 GiB total capacity; 4.75 GiB already allocated; 0 bytes free; 4.78 GiB reserved in total by PyTorch) If reserved memory is &gt;&gt; allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x0000020E346E5250&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’<br>
Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Resampling…<br>
Resampled in 4.12s<br>
Predicting…</p>
<p>I got CUDA out of memory. Should I try to install the CPU pytorch version? I do have an nvidia card, but the amount of memory is very low…</p>
<p>Thnx<br>
Ronald</p>

---

## Post #20 by @rbumm (2022-12-28 18:24 UTC)

<p>No personal experience, but yes, you may want to try that, uninstall PyTorch with the extension and reinstall it in CPU mode:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34c5f816f3a704394d0b3519fe6971ceee2f0f17.png" alt="image" data-base62-sha1="7wQYt4lO34vJ3Xiq5XHrie4waeb" width="535" height="141"></p>
<p>Please let us know how it works.</p>

---

## Post #21 by @R.Boellaard (2022-12-29 07:26 UTC)

<p>Dear Rudolf</p>
<p>It works! Many thanks for your help and suggestions. It is relatively fast (even with CPU) and worked quite well even for a low dose CT (done along with a PET scan)…so it generates quite well segmentations for a poor quality scan.</p>
<p>Regards<br>
Ronald</p>

---

## Post #22 by @muratmaga (2023-01-14 01:25 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a><br>
Does total segmentator require cuDNN beyond regular cuda installation? I am getting this error message on Ubuntu 22.04 with Slicer 5.2.1. Cuda 12.0 is installed, and pytorch extension installed cu118 enabled torch.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/exouser/Slicer/bin/Python/slicer/util.py", line 2961, in tryWithErrorDisplay
    yield
  File "/home/exouser/Slicer/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 258, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "/home/exouser/Slicer/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 647, in process
    self.logProcessOutput(proc)
  File "/home/exouser/Slicer/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 556, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/home/exouser/Slicer/bin/../bin/PythonSlicer', '/home/exouser/Slicer/lib/Python/bin/TotalSegmentator', '-i', '/tmp/Slicer-exouser/__SlicerTemp__2023-01-14_01+20+25.853/total-segmentator-input.nii', '-o', '/tmp/Slicer-exouser/__SlicerTemp__2023-01-14_01+20+25.853/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
</code></pre>
<p>and then there is this error on the module pane:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d926d8afd5048e9656fc092f20d11982e874bd4d.jpeg" data-download-href="/uploads/short-url/uZ0Q1PAiRFyLsbErCdrTfpy8OHr.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d926d8afd5048e9656fc092f20d11982e874bd4d_2_690x90.jpeg" alt="image" data-base62-sha1="uZ0Q1PAiRFyLsbErCdrTfpy8OHr" width="690" height="90" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d926d8afd5048e9656fc092f20d11982e874bd4d_2_690x90.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d926d8afd5048e9656fc092f20d11982e874bd4d_2_1035x135.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d926d8afd5048e9656fc092f20d11982e874bd4d.jpeg 2x" data-dominant-color="E7E7E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1361×178 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @mau_igna_06 (2023-01-14 01:45 UTC)

<p>Hi</p>
<p>I think you need CUDA 11.6 or 11.7</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pytorch.org/get-started/locally/">
  <header class="source">
      <img src="https://pytorch.org/favicon.ico?" class="site-icon" width="32" height="32">

      <a href="https://pytorch.org/get-started/locally/" target="_blank" rel="noopener nofollow ugc">pytorch.org</a>
  </header>

  <article class="onebox-body">
    <img src="https://pytorch.org/assets/images/pytorch-logo.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://pytorch.org/get-started/locally/" target="_blank" rel="noopener nofollow ugc">PyTorch</a></h3>

  <p>An open source machine learning framework that accelerates the path from research prototyping to production deployment.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #24 by @muratmaga (2023-01-14 01:49 UTC)

<p>Thanks I already got the cuda part taken care of. PyTorch worked fine. The issue was indeed the missing cuDNN library, which is not part of the CUDA package and you actually have to register with Nvidia, agree to their terms and download it. <a href="https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html" rel="noopener nofollow ugc">https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html</a></p>
<p>I can confirm that after installing it (cuDNN8.7.0), everything it worked fine. It is shame though that Nvidia makes getting cuDNN so hard.</p>

---

## Post #25 by @rbumm (2023-01-14 08:44 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> great that it works now, on my windows systems cudnn and it´s folders seem to be present automatically on every Python where TotalSegmentator is installed, and there has never be the need for separate downloads. Would be interesting to find out why it was necessary on your system …</p>

---

## Post #26 by @lassoan (2023-01-14 16:26 UTC)

<p>I use Windows, too, and I don’t remember ever having to manually install cuDNN either. Nobody else has reported this issue until now either. So, probably this manual cuDNN installation is only needed on certain Linux systems.</p>

---

## Post #27 by @pieper (2023-01-14 16:43 UTC)

<p>I’ve run into this before too.  The Nvidia cuDNN instructions clearly say you need to get it via the developer program for both windows and linux: <a href="https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#download-windows" class="inline-onebox">Installation Guide - NVIDIA Docs</a>).</p>
<p>But apparently this is bundled in pytorch: <a href="https://discuss.pytorch.org/t/how-to-check-if-torch-uses-cudnn/21933/3" class="inline-onebox">How to check if torch uses cuDNN - #3 by timonbimon - PyTorch Forums</a></p>
<blockquote>
<p>“if you want to use pytorch with an NVIDIA GPU, all you need to do is install pytorch binaries and start using it. We ship with everything in-built (pytorch binaries include CUDA, CuDNN, NCCL, MKL, etc.).”</p>
</blockquote>

---

## Post #28 by @lassoan (2023-01-14 16:48 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> is it possible that your CUDA version is not 11.6 or 11.7?</p>

---

## Post #29 by @jamesobutler (2023-01-14 17:10 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="22" data-topic="26925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Ubuntu 22.04 with Slicer 5.2.1. Cuda 12.0 is installed,</p>
</blockquote>
</aside>
<p>Latest Cuda (Cuda 12) is not supported with latest PyTorch binaries.</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discuss.pytorch.org/t/pytorch-for-cuda-12/169447/2">
  <header class="source">
      <img src="https://discuss.pytorch.org/uploads/default/optimized/2X/b/bb2eeaba4e9f7e4a5944a0d83f52c4f2bf1b6a85_2_32x32.png" class="site-icon" width="" height="">

      <a href="https://discuss.pytorch.org/t/pytorch-for-cuda-12/169447/2" target="_blank" rel="noopener nofollow ugc" title="09:28PM - 02 January 2023">PyTorch Forums – 2 Jan 23</a>
  </header>

  <article class="onebox-body">
    <img src="https://discuss.pytorch.org/uploads/default/original/2X/1/15a7e2573aeb9e6ba8995f824d3b63171a433041.png" class="thumbnail" width="" height="">

<div class="title-wrapper">
  <h3><a href="https://discuss.pytorch.org/t/pytorch-for-cuda-12/169447/2" target="_blank" rel="noopener nofollow ugc">PyTorch for Cuda 12</a></h3>
</div>

  <p>You should be able to build PyTorch from source using CUDA 12.0, but the binaries are not ready yet (and the nightlies with CUDA 11.8 were just added ~2 weeks ago).  If you decide to build from source, note that a few fixes still need to land...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #30 by @muratmaga (2023-01-15 03:19 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="29" data-topic="26925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Latest Cuda (Cuda 12) is not supported with latest PyTorch binaries</p>
</blockquote>
</aside>
<p>That’s interesting because I used the pytorch extension to install and it clearly brought torch with cuda (11.8) but without the cudnn.</p>

---

## Post #31 by @lassoan (2023-01-15 13:01 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Have you installed CUDA? Which version? What CUDA version do you see in pytorch util module in Slicer (cuNNN)?</p>

---

## Post #32 by @muratmaga (2023-01-15 17:14 UTC)

<p>Yes, Cuda 12.0 is installed on this machine. This is what torch reports in Slicer through python:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; torch.__version__
'1.13.1+cu117'
</code></pre>
<p>(I thought it was 118, but were mistaken).</p>
<p>And this is from pyutils<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b7a29e02bf84735fd5e0b3f7c1e8e719ef8512d.png" alt="image" data-base62-sha1="d3fbpylRBWwJ9dET2I5VUiIPM8l" width="400" height="66"></p>

---

## Post #33 by @muratmaga (2023-01-15 17:29 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="32" data-topic="26925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Yes, Cuda 12.0 is installed on this machine. This is what torch reports in Slicer through python:</p>
</blockquote>
</aside>
<p>A bit more clarification.</p>
<p>I wasn’t aware that pytorch extension (through light the torch) bring all the necessary cuda/cudnn and stuff internally, without requiring the OS based manual installation. I can confirm that this works (and much more simply. yay).</p>
<p>However, if you do have CUDA manually installed and it is path is listed on your LD_LIBRARY_PATH, this seems to interfere with the pyTorch util detection, and you will need to provide the cuDNN manually.</p>
<p>Sorry for the confusion.</p>

---

## Post #34 by @lassoan (2023-01-15 20:41 UTC)

<p>Thanks for the clarification. Do you mean that on linux you don’t event need to install CUDA, but only the NVIDIA drivers?</p>

---

## Post #35 by @muratmaga (2023-01-15 22:13 UTC)

<p>Yep! That’s what the link <a class="mention" href="/u/pieper">@pieper</a> cited said, and I can confirm it is indeed the case.</p>

---

## Post #36 by @lassoan (2023-01-16 19:01 UTC)

<p>3 posts were split to a new topic: <a href="/t/use-amd-rocm-for-totalsegmentator/27270">Use AMD ROCm for TotalSegmentator</a></p>

---

## Post #37 by @lassoan (2023-02-15 20:49 UTC)

<p>A post was merged into an existing topic: <a href="/t/total-segmentor-module-showing-errors/27834/3">Total segmentor module showing errors</a></p>

---
