---
topic_id: 45862
title: "Got Error Msg While Applying Medsam2"
date: 2026-01-22
url: https://discourse.slicer.org/t/45862
---

# Got error msg while applying MedSam2

**Topic ID**: 45862
**Date**: 2026-01-22
**URL**: https://discourse.slicer.org/t/got-error-msg-while-applying-medsam2/45862

---

## Post #1 by @aiden.zhu (2026-01-22 13:04 UTC)

<p>Operating system: windows<br>
Slicer version: 5.11.0-2026-01-19<br>
Expected behavior: no errors<br>
Actual behavior: errors with pickling</p>
<p>Hi all,</p>
<p>Trying to work with MedSam2 and got the following error while clicking on “<strong>Segment Middle Slice</strong>” button.</p>
<p>“Traceback (most recent call last):</p>
<p>File “C:\Slicer.5.10.0\3D Slicer 5.11.0-2026-01-19\lib\Python\Lib\site-packages\numpy\lib\_npyio_impl.py”, line 494, in load</p>
<p>return pickle.load(fid, **pickle_kwargs)</p>
<p>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>_pickle.UnpicklingError: invalid load key, ‘&lt;’.</p>
<p>The above exception was the direct cause of the following exception:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Slicer.5.10.0/MedSAMSlicer-MedSAM2/MedSAMSlicer-MedSAM2/slicer/MedSAM2/MedSAM2/MedSAM2.py”, line 618, in getMiddleMask</p>
<p>segmentation_mask = np.load(result_path, allow_pickle=True)[‘segs’]</p>
<p>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>File “C:\Slicer.5.10.0\3D Slicer 5.11.0-2026-01-19\lib\Python\Lib\site-packages\numpy\lib\_npyio_impl.py”, line 496, in load</p>
<p>raise pickle.UnpicklingError(</p>
<p>_pickle.UnpicklingError: Failed to interpret file ‘C:\\Users\\AIDENZ~1\\AppData\\Local\\Temp\\tmpgwrurd7b/result.npz’ as a pickle</p>
<p>“</p>
<p>Any suggestion or help will be well appreciated. Thanks in advance.</p>
<p>Aiden</p>

---
