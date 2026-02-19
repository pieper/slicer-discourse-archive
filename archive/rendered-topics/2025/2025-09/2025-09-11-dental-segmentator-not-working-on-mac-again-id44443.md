---
topic_id: 44443
title: "Dental Segmentator Not Working On Mac Again"
date: 2025-09-11
url: https://discourse.slicer.org/t/44443
---

# Dental segmentator not working on mac again

**Topic ID**: 44443
**Date**: 2025-09-11
**URL**: https://discourse.slicer.org/t/dental-segmentator-not-working-on-mac-again/44443

---

## Post #1 by @mohammed_alshakhas (2025-09-11 06:26 UTC)

<p>DENTAL SEGMENTATOR NOT WORKING ON MAC AGAIN</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ee7d44b501943921242a05be78b2e0ac6f7fcee.png" data-download-href="/uploads/short-url/6GWEE0EKVHfSW0a31XIBSTmdYVo.png?dl=1" title="Screenshot 2025-09-11 at 09.23.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ee7d44b501943921242a05be78b2e0ac6f7fcee_2_690x324.png" alt="Screenshot 2025-09-11 at 09.23.48" data-base62-sha1="6GWEE0EKVHfSW0a31XIBSTmdYVo" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ee7d44b501943921242a05be78b2e0ac6f7fcee_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ee7d44b501943921242a05be78b2e0ac6f7fcee_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ee7d44b501943921242a05be78b2e0ac6f7fcee.png 2x" data-dominant-color="717070"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-09-11 at 09.23.48</span><span class="informations">1114×524 84.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sankalpa_Gamage (2026-01-26 08:19 UTC)

<p>same here</p>
<p>2026/01/26 13:46:58.505 :: nnUNet is already installed (2.6.2) and compatible with requested version (nnunetv2).</p>
<p>2026/01/26 13:47:04.521 :: Transferring volume to nnUNet in /private/var/folders/nf/nrhb0m1d6f50xtt7d9jx9ccw0000gn/T/Slicer-tByqnM</p>
<p>2026/01/26 13:47:06.421 :: Starting nnUNet with the following parameters:</p>
<p>2026/01/26 13:47:06.421 ::</p>
<p>2026/01/26 13:47:06.421 :: /Applications/Slicer.app/Contents/lib/Python/bin/nnUNetv2_predict -i /private/var/folders/nf/nrhb0m1d6f50xtt7d9jx9ccw0000gn/T/Slicer-tByqnM/input -o /private/var/folders/nf/nrhb0m1d6f50xtt7d9jx9ccw0000gn/T/Slicer-tByqnM/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cpu -chk checkpoint_final.pth --disable_tta</p>
<p>2026/01/26 13:47:06.421 ::</p>
<p>2026/01/26 13:47:06.421 :: JSON parameters :</p>
<p>2026/01/26 13:47:06.421 :: {</p>
<p>2026/01/26 13:47:06.421 :: “folds”: “0”,</p>
<p>2026/01/26 13:47:06.421 :: “device”: “cpu”,</p>
<p>2026/01/26 13:47:06.421 :: “stepSize”: 0.5,</p>
<p>2026/01/26 13:47:06.421 :: “disableTta”: true,</p>
<p>2026/01/26 13:47:06.421 :: “nProcessPreprocessing”: 1,</p>
<p>2026/01/26 13:47:06.421 :: “nProcessSegmentationExport”: 1,</p>
<p>2026/01/26 13:47:06.421 :: “checkPointName”: “”,</p>
<p>2026/01/26 13:47:06.421 :: “modelPath”: {</p>
<p>2026/01/26 13:47:06.421 :: “_path”: “/Applications/Slicer.app/Contents/Extensions-34045/DentalSegmentator/lib/Slicer-5.10/qt-scripted-modules/Resources/ML”</p>
<p>2026/01/26 13:47:06.421 :: }</p>
<p>2026/01/26 13:47:06.421 :: }</p>
<p>2026/01/26 13:47:06.434 :: nnUNet preprocessing…</p>
<p>2026/01/26 13:47:11.324 :: Traceback (most recent call last):</p>
<p>2026/01/26 13:47:11.324 :: File “/Applications/Slicer.app/Contents/lib/Python/bin/nnUNetv2_predict”, line 5, in </p>
<p>2026/01/26 13:47:11.329 :: from nnunetv2.inference.predict_from_raw_data import predict_entry_point</p>
<p>2026/01/26 13:47:11.329 :: File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/inference/predict_from_raw_data.py”, line 24, in </p>
<p>2026/01/26 13:47:11.329 :: from nnunetv2.inference.data_iterators import PreprocessAdapterFromNpy, preprocessing_iterator_fromfiles, \</p>
<p>2026/01/26 13:47:11.329 :: File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/inference/data_iterators.py”, line 12, in </p>
<p>2026/01/26 13:47:11.329 :: from nnunetv2.preprocessing.preprocessors.default_preprocessor import DefaultPreprocessor</p>
<p>2026/01/26 13:47:11.329 :: File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/preprocessing/preprocessors/default_preprocessor.py”, line 34, in </p>
<p>2026/01/26 13:47:11.329 :: from nnunetv2.utilities.plans_handling.plans_handler import PlansManager, ConfigurationManager</p>
<p>2026/01/26 13:47:11.329 :: File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/utilities/plans_handling/plans_handler.py”, line 18, in </p>
<p>2026/01/26 13:47:11.329 :: from nnunetv2.utilities.label_handling.label_handling import get_labelmanager_class_from_plans</p>
<p>2026/01/26 13:47:11.329 :: File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/utilities/label_handling/label_handling.py”, line 7, in </p>
<p>2026/01/26 13:47:11.329 :: from acvl_utils.cropping_and_padding.bounding_boxes import bounding_box_to_slice, insert_crop_into_image</p>
<p>2026/01/26 13:47:11.329 :: ImportError: cannot import name ‘insert_crop_into_image’ from ‘acvl_utils.cropping_and_padding.bounding_boxes’ (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/acvl_utils/cropping_and_padding/bounding_boxes.py)</p>
<p>2026/01/26 13:47:12.046 :: Loading inference results…</p>
<p>2026/01/26 13:47:18.960 :: Error loading results :</p>
<p>2026/01/26 13:47:18.960 :: Failed to load the segmentation.</p>
<p>2026/01/26 13:47:18.960 :: Something went wrong during the nnUNet processing.</p>
<p>2026/01/26 13:47:18.960 :: Please check the logs for potential errors and contact the library maintainers.</p>

---
