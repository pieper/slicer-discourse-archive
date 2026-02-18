# Problem with TotalSegmentator

**Topic ID**: 36418
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/problem-with-totalsegmentator/36418

---

## Post #1 by @vieimar (2024-05-27 13:25 UTC)

<p>I am trying to use TotalSegmentator but I have a problem : “Traceback (most recent call last):<br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 961, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1035, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 807, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/__SlicerTemp__2024-05-27_15+18+36.694/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/__SlicerTemp__2024-05-27_15+18+36.694/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.” I don’t undersantand where the problem comes from ? Thank you for your help.</p>

---

## Post #2 by @Matteboo (2024-05-27 13:37 UTC)

<p>Hello,<br>
Could you give us the error message in this box please. It’s a more pertinent error message<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd3278f326e0f5a17f9fedcd247bb1842503d73.jpeg" data-download-href="/uploads/short-url/xN34VFe7t7bWlxywMQBKuvhTbq3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd3278f326e0f5a17f9fedcd247bb1842503d73_2_690x328.jpeg" alt="image" data-base62-sha1="xN34VFe7t7bWlxywMQBKuvhTbq3" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd3278f326e0f5a17f9fedcd247bb1842503d73_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd3278f326e0f5a17f9fedcd247bb1842503d73_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd3278f326e0f5a17f9fedcd247bb1842503d73_2_1380x656.jpeg 2x" data-dominant-color="605C62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1924×916 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @vieimar (2024-05-27 13:45 UTC)

<p>Yes: here is my problem : Processing started<br>
Writing input file to C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/__SlicerTemp__2024-05-27_15+33+06.139/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/__SlicerTemp__2024-05-27_15+33+06.139/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/maria/AppData/Local/slicer.org/Slicer 5.6.2/__SlicerTemp__2024-05-27_15+33+06.139/segmentation’, ‘–ml’, ‘–task’, ‘total’]<br>
Traceback (most recent call last):<br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return <em>run_code(code, main_globals, None,<br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 4, in <br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 8, in <br>
from totalsegmentator.python_api import totalsegmentator<br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 11, in <br>
from totalsegmentator.statistics import get_basic_statistics, get_radiomics_features_for_entire_dir<br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\statistics.py”, line 8, in <br>
import pandas as pd<br>
File "C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pandas_<em>init</em></em>.py", line 77, in <br>
from pandas.core.api import (<br>
File “C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pandas\core\api.py”, line 1, in <br>
from pandas.<em>libs import (<br>
File "C:\Users\maria\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\pandas_libs_<em>init</em></em>.py", line 16, in <br>
import pandas._libs.pandas_parser  # isort: skip # type: ignore[reportUnusedImport]<br>
ModuleNotFoundError: No module named ‘pandas._libs.pandas_parser’</p>

---

## Post #4 by @lassoan (2024-06-19 13:50 UTC)

<p>It seems that some required Python libraries were not installed correctly (or an incompatible version was installed by some other extensions). “Force reinstall” in “Advanced” section in TotalSegmentator module should fix the issue. If not then you may need to install Slicer from scratch again.</p>

---
