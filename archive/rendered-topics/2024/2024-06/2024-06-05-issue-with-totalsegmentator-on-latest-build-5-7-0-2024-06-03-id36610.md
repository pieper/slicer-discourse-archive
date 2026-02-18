# Issue with totalSegmentator on latest build (5.7.0-2024-06-03) Window

**Topic ID**: 36610
**Date**: 2024-06-05
**URL**: https://discourse.slicer.org/t/issue-with-totalsegmentator-on-latest-build-5-7-0-2024-06-03-window/36610

---

## Post #1 by @Matteboo (2024-06-05 15:27 UTC)

<p>Hello,<br>
I get an error message when trying to run total segmentator on the latest build.<br>
Here is the error message I get</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-03\bin\Python\slicer\util.py", line 3295, in tryWithErrorDisplay
    yield
  File "C:/Users/matte/AppData/Local/slicer.org/Slicer 5.7.0-2024-06-03/slicer.org/Extensions-32891/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 298, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/matte/AppData/Local/slicer.org/Slicer 5.7.0-2024-06-03/slicer.org/Extensions-32891/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 965, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/matte/AppData/Local/slicer.org/Slicer 5.7.0-2024-06-03/slicer.org/Extensions-32891/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 1039, in processVolume
    self.logProcessOutput(proc)
  File "C:/Users/matte/AppData/Local/slicer.org/Slicer 5.7.0-2024-06-03/slicer.org/Extensions-32891/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py", line 811, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/matte/AppData/Local/slicer.org/Slicer 5.7.0-2024-06-03/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\matte\\AppData\\Local\\slicer.org\\Slicer 5.7.0-2024-06-03\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/matte/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-05_16+55+30.623/total-segmentator-input.nii', '-o', 'C:/Users/matte/AppData/Local/Temp/Slicer/__SlicerTemp__2024-06-05_16+55+30.623/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.

</code></pre>
<p>I can’t run TotalSegmentator on the sample data</p>
<p>Contrary to most of the time, no error message shows up in the box<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01966c6ec0cde04e7d6baa03a5218fc7c16c8a23.png" data-download-href="/uploads/short-url/e2L1z7ychdpKDYQDpvgaxDerT5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01966c6ec0cde04e7d6baa03a5218fc7c16c8a23_2_690x206.png" alt="image" data-base62-sha1="e2L1z7ychdpKDYQDpvgaxDerT5" width="690" height="206" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01966c6ec0cde04e7d6baa03a5218fc7c16c8a23_2_690x206.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01966c6ec0cde04e7d6baa03a5218fc7c16c8a23.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01966c6ec0cde04e7d6baa03a5218fc7c16c8a23.png 2x" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">721×216 26.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
