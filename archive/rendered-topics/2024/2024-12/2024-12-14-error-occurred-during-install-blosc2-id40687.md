#  Error occurred during install : blosc2?

**Topic ID**: 40687
**Date**: 2024-12-14
**URL**: https://discourse.slicer.org/t/error-occurred-during-install-blosc2/40687

---

## Post #1 by @RamonWest (2024-12-14 02:33 UTC)

<p>Hi there, someone familiar with this report(read below) when pushing the button ‘Aplly’ with the DentalSegmentator add on?</p>
<hr>
<p>2024/12/13 20:00:12.016 :: Start nnUNet install with requirements : nnunetv2</p>
<p>2024/12/13 20:00:12.019 :: - Installing pandas…</p>
<p>2024/12/13 20:00:20.642 :: - Installing pillow&lt;10.1…</p>
<p>2024/12/13 20:00:25.217 :: - Installing nnunetv2 --no-deps…</p>
<p>2024/12/13 20:00:26.838 :: - Installing acvl-utils&lt;0.3,&gt;=0.2 --no-deps…</p>
<p>2024/12/13 20:00:27.646 :: - Installing batchgenerators --no-deps…</p>
<p>2024/12/13 20:00:28.497 :: - Installing scikit-image --no-deps…</p>
<p>2024/12/13 20:00:30.600 :: - Installing networkx&gt;=2.8 --no-deps…</p>
<p>2024/12/13 20:00:32.761 :: - Installing imageio&gt;=2.33 --no-deps…</p>
<p>2024/12/13 20:00:33.912 :: - Installing tifffile&gt;=2022.8.12 --no-deps…</p>
<p>2024/12/13 20:00:35.387 :: - Installing lazy-loader&gt;=0.4 --no-deps…</p>
<p>2024/12/13 20:00:36.125 :: - Installing scikit-learn --no-deps…</p>
<p>2024/12/13 20:00:39.518 :: - Installing joblib&gt;=1.2.0 --no-deps…</p>
<p>2024/12/13 20:00:40.543 :: - Installing threadpoolctl&gt;=3.1.0 --no-deps…</p>
<p>2024/12/13 20:00:41.250 :: - Installing future --no-deps…</p>
<p>2024/12/13 20:00:42.768 :: - Installing unittest2 --no-deps…</p>
<p>2024/12/13 20:00:43.661 :: - Installing argparse --no-deps…</p>
<p>2024/12/13 20:00:44.361 :: - Installing traceback2 --no-deps…</p>
<p>2024/12/13 20:00:45.067 :: - Installing linecache2 --no-deps…</p>
<p>2024/12/13 20:00:45.750 :: - Installing connected-components-3d --no-deps…</p>
<p>2024/12/13 20:00:46.687 :: - Installing blosc2&gt;=3.0.0b4 --no-deps…</p>
<p>2024/12/13 20:00:47.254 :: Install returned non-zero exit status : Command ‘[‘C:/Users/Ramon/AppData/Local/slicer.org/Slicer 5.7.0-2024-12-12/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘blosc2&gt;=3.0.0b4’, ‘–no-deps’]’ returned non-zero exit status 1… Attempting to continue…</p>
<p>2024/12/13 20:00:47.260 :: Error occurred during install : blosc2</p>
<p>Hope someone can help me with the segmentation of my DICOM.</p>
<p>Kind regards,</p>
<p>Ramon Westerhuis</p>

---

## Post #2 by @lassoan (2024-12-14 02:35 UTC)

<p>It is due to a problem in a third-party library. See more information and description of how to fix here: <a href="https://github.com/gaudot/SlicerDentalSegmentator/issues/21#issuecomment-2528041138" class="inline-onebox">DentalSegmentator doesnt work · Issue #21 · gaudot/SlicerDentalSegmentator · GitHub</a></p>

---
