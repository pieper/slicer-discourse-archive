# Having trouble with TotalSegmentator

**Topic ID**: 43710
**Date**: 2025-07-14
**URL**: https://discourse.slicer.org/t/having-trouble-with-totalsegmentator/43710

---

## Post #1 by @Celina_Hallal (2025-07-14 13:48 UTC)

<p>Operating system: MacOS Sequoia 15.5<br>
Slicer version: 5.9.0<br>
Expected behavior: Automated segmentation of organs, segmentation of liver segments<br>
Actual behavior: Extension fails to compute results</p>
<p>I am trying to use TotalSegmentator, but it keeps returning the same error even after reinstalling it</p>
<p>Failed to compute results.</p>
<p>Command ‘[’/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/cy/jc_jw_l536l0p8_ky67hg0sm0000gn/T/Slicer-celinahallal/__SlicerTemp__2025-07-14_10+12+45.692/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/cy/jc_jw_l536l0p8_ky67hg0sm0000gn/T/Slicer-celinahallal/__SlicerTemp__2025-07-14_10+12+45.692/segmentation’, ‘–fast’]’ returned non-zero exit status 1.</p>
<p>Processing started<br>
Writing input file to /private/var/folders/cy/jc_jw_l536l0p8_ky67hg0sm0000gn/T/Slicer-celinahallal/__SlicerTemp__2025-07-14_10+12+45.692/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI (pre-run)…<br>
Total Segmentator arguments: [‘-i’, ‘/private/var/folders/cy/jc_jw_l536l0p8_ky67hg0sm0000gn/T/Slicer-celinahallal/__SlicerTemp__2025-07-14_10+12+45.692/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/cy/jc_jw_l536l0p8_ky67hg0sm0000gn/T/Slicer-celinahallal/__SlicerTemp__2025-07-14_10+12+45.692/segmentation’, ‘–fast’]<br>
No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the <code>--roi_subset</code> option can help to reduce runtime.</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 8, in <br>
sys.exit(main())<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/bin/TotalSegmentator.py”, line 141, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/python_api.py”, line 127, in totalsegmentator<br>
from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/nnunet.py”, line 40, in <br>
from totalsegmentator.dicom_io import dcm_to_nifti, save_mask_as_rtstruct<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/dicom_io.py”, line 13, in <br>
import dicom2nifti<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/dicom2nifti/<strong>init</strong>.py”, line 19, in <br>
from dicom2nifti.convert_dicom import dicom_series_to_nifti<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/dicom2nifti/convert_dicom.py”, line 17, in <br>
import dicom2nifti.common as common<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/dicom2nifti/common.py”, line 16, in <br>
from pydicom.pixels import apply_modality_lut<br>
ModuleNotFoundError: No module named ‘pydicom.pixels’</p>
<p>I have already reinstalled PyTorch (but not manually) and TotalSegmentator. I’ve also already read <a href="https://discourse.slicer.org/t/totalsegmentator-slicer-5-8-1-modulenotfounderror-no-module-named-pydicom-pixels/42386">TotalSegmentator + Slicer 5.8.1 - “ModuleNotFoundError: No module named ‘pydicom.pixels’”</a>.</p>
<p>I also cannot find the Liver Segments task, only Liver Vessels.</p>
<p>Thanks in advance</p>

---

## Post #2 by @Celina_Hallal (2025-07-14 14:32 UTC)

<p>Ok, so I installed dicom2nifti v 2.5.1 using the Python console and the segmentation works! But I still can’t find some of the tasks like liver_segments and abdominal_muscles…</p>

---
