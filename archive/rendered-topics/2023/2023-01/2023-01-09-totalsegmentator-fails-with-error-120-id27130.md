# TotalSegmentator fails with error 120

**Topic ID**: 27130
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/totalsegmentator-fails-with-error-120/27130

---

## Post #1 by @LipTeck_Chew (2023-01-09 05:49 UTC)

<p>Hi Lassoan</p>
<p>I have tried the cpu without fast option selected. It exited with status 120 after predicting part 1/5. Is there a workaround?</p>
<p>Thank you.</p>
<p>Regards<br>
Lip Teck</p>

---

## Post #2 by @lassoan (2023-01-09 14:17 UTC)

<p>Most likely your installation is corrupted. We have improved robustness of TotalSegmentator installation recently, so reinstallation from scratch may fix the problem. Please remove your Slicer installation completely, then install Slicer and TotalSegmentator again.</p>
<p>If it did not fix the issue then copy here the content of the window that is displayed below the “Apply” button.</p>

---

## Post #3 by @LipTeck_Chew (2023-01-11 00:51 UTC)

<p>Hi Lassoan,</p>
<p>After uninstallaing and re-installing, the fast option went well but without fast it failed with exit 120.</p>
<p><strong>Here’s the slicer’s error:</strong></p>
<p>Traceback (most recent call last):</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py”, line 2961, in tryWithErrorDisplay</p>
<p>yield</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton</p>
<p>self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 647, in process</p>
<p>self.logProcessOutput(proc)</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 556, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[’/home/lipteck/Slicer-5.2.1-linux-amd64/bin/…/bin/PythonSlicer’, ‘/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/tmp/Slicer-lipteck/__SlicerTemp__2023-01-11_08+36+20.388/total-segmentator-input.nii’, ‘-o’, ‘/tmp/Slicer-lipteck/__SlicerTemp__2023-01-11_08+36+20.388/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>
<p><strong>Here’s the display below apply:</strong></p>
<p>Processing started</p>
<p>Writing input file to /tmp/Slicer-lipteck/__SlicerTemp__2023-01-11_08+36+20.388/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘/tmp/Slicer-lipteck/__SlicerTemp__2023-01-11_08+36+20.388/total-segmentator-input.nii’, ‘-o’, ‘/tmp/Slicer-lipteck/__SlicerTemp__2023-01-11_08+36+20.388/segmentation’, ‘–ml’, ‘–task’, ‘total’]</p>
<p>/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/torch/cuda/amp/grad_scaler.py:115: UserWarning: torch.cuda.amp.GradScaler is enabled, but CUDA is not available. Disabling.</p>
<p>warnings.warn(“torch.cuda.amp.GradScaler is enabled, but CUDA is not available. Disabling.”)</p>
<p>/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/torch/cuda/amp/autocast_mode.py:120: UserWarning: torch.cuda.amp.autocast only affects CUDA ops, but CUDA is not available. Disabling.</p>
<p>warnings.warn(“torch.cuda.amp.autocast only affects CUDA ops, but CUDA is not available. Disabling.”)</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" rel="noopener nofollow ugc">https://doi.org/10.48550/arXiv.2208.05868</a></p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ option can help to some extend.</p>
<p>Resampling…</p>
<p>Resampled in 15.49s</p>
<p>Predicting part 0 of 5 …</p>
<p>Traceback (most recent call last):</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/bin/TotalSegmentator”, line 242, in </p>
<p>main()</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/bin/TotalSegmentator”, line 219, in main</p>
<p>seg = nnUNet_predict_image(args.input, args.output, task_id, model=model, folds=folds,</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/totalsegmentator/nnunet.py”, line 217, in nnUNet_predict_image</p>
<p>nnUNet_predict(tmp_dir, tmp_dir, tid, model, folds, trainer, tta)</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/totalsegmentator/nnunet.py”, line 106, in nnUNet_predict</p>
<p>predict_from_folder(model_folder_name, dir_in, dir_out, folds, save_npz, num_threads_preprocessing,</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/nnunet/inference/predict.py”, line 668, in predict_from_folder</p>
<p>return predict_cases_fastest(model, list_of_lists[part_id::num_parts], output_files[part_id::num_parts], folds,</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/nnunet/inference/predict.py”, line 468, in predict_cases_fastest</p>
<p>trainer, params = load_model_and_checkpoint_files(model, folds, mixed_precision=mixed_precision, checkpoint_name=checkpoint_name)</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/nnunet/training/model_restore.py”, line 140, in load_model_and_checkpoint_files</p>
<p>trainer = restore_model(join(folds[0], “%s.model.pkl” % checkpoint_name), fp16=mixed_precision)</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/nnunet/training/model_restore.py”, line 56, in restore_model</p>
<p>info = load_pickle(pkl_file)</p>
<p>File “/home/lipteck/Slicer-5.2.1-linux-amd64/lib/Python/lib/python3.9/site-packages/batchgenerators/utilities/file_and_folder_operations.py”, line 49, in load_pickle</p>
<p>with open(file, mode) as f:</p>
<p>FileNotFoundError: [Errno 2] No such file or directory: ‘/home/lipteck/.totalsegmentator/nnunet/results/nnUNet/3d_fullres/Task252_TotalSegmentator_part2_vertebrae_1139subj/nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1/fold_0/model_final_checkpoint.model.pkl’</p>
<p>Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x7f4d03bec400&gt;</p>
<p>AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" rel="noopener nofollow ugc">https://doi.org/10.48550/arXiv.2208.05868</a></p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ option can help to some extend.</p>
<p>Resampling…</p>
<p>Resampled in 15.49s</p>
<p>Predicting part 0 of 5 …</p>
<p>Predicting part 1 of 5 …</p>
<p>Thank you and regards,</p>
<p>LipTeck</p>

---

## Post #4 by @lassoan (2023-01-11 03:11 UTC)

<aside class="quote no-group" data-username="LipTeck_Chew" data-post="3" data-topic="27130">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lipteck_chew/48/13519_2.png" class="avatar"> LipTeck_Chew:</div>
<blockquote>
<p>FileNotFoundError: [Errno 2] No such file or directory: ‘/home/lipteck/.totalsegmentator/nnunet/results/nnUNet/3d_fullres/Task252_TotalSegmentator_part2_vertebrae_1139subj/nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1/fold_0/model_final_checkpoint.model.pkl’</p>
</blockquote>
</aside>
<p>It seems that your model files download was incomplete, either due to some transient network issues or the download was interrupted.</p>
<p>You need to erase the /home/lipteck/.totalsegmentator/ folder and start again.</p>
<aside class="quote no-group" data-username="LipTeck_Chew" data-post="3" data-topic="27130">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lipteck_chew/48/13519_2.png" class="avatar"> LipTeck_Chew:</div>
<blockquote>
<p>No GPU detected. Running on CPU. This can be very slow.</p>
</blockquote>
</aside>
<p>This indicates that there is an issue with your CUDA installation. Currently, pytorch supports CUDA 11.6 and 11.7 on Linux, for best compatibility install one of these CUDA  versions. Then check if CUDA version shown in PyTorchUtils module in Slicer matches the installed CUDA version.</p>

---

## Post #5 by @LipTeck_Chew (2023-01-12 09:13 UTC)

<p>Hi Lassoan</p>
<p>I removed the .totalsegmentator in my home directory with rm -rf command and it is now working.</p>
<p>Thank you!</p>
<p>By the way, is there any plan to segment structures - the organs at risk frequently used in radiation treatment planning by body section?</p>
<p>Regards<br>
Lip Teck</p>

---

## Post #6 by @pieper (2023-01-12 13:42 UTC)

<p>We are planning a session at the upcoming <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/">Project Week</a> to discuss TotalSegmentator and related machine learning segmentation tools, so you may want to join that discussion to see where things are headed and add your wishlist for future segmentation features.</p>

---

## Post #7 by @lassoan (2023-02-15 05:12 UTC)

<p>A post was split to a new topic: <a href="/t/create-derived-segments-with-aapm-nomenclature-form-totalsegmentator-output/27817">Create derived segments with AAPM nomenclature form TotalSegmentator output</a></p>

---
