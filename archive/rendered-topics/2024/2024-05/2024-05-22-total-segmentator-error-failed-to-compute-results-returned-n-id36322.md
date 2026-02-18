# Total Segmentator error: Failed to compute results...returned non-zero exit status 1

**Topic ID**: 36322
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/total-segmentator-error-failed-to-compute-results-returned-non-zero-exit-status-1/36322

---

## Post #1 by @liyiranran2001 (2024-05-22 13:15 UTC)

<p>Operating system:windows11<br>
Slicer version:5.6.2</p>
<p>Hi,<br>
I have installed Pytorch and other python packages properly, and restarted and reinstalled Slicer for several times. No matter I choose the ‘fast’ mode or not, the process will stop after starting the downloading of models.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb6098fc8ea56ee659b31a51402c3a78baed0d1c.jpeg" data-download-href="/uploads/short-url/t19SVrMLuInjW3lmA8LjtjHkeXG.jpeg?dl=1" title="1716345893668" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb6098fc8ea56ee659b31a51402c3a78baed0d1c_2_690x411.jpeg" alt="1716345893668" data-base62-sha1="t19SVrMLuInjW3lmA8LjtjHkeXG" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb6098fc8ea56ee659b31a51402c3a78baed0d1c_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb6098fc8ea56ee659b31a51402c3a78baed0d1c_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb6098fc8ea56ee659b31a51402c3a78baed0d1c_2_1380x822.jpeg 2x" data-dominant-color="CAC7CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1716345893668</span><span class="informations">1920×1146 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db74d42a11b94b1c42b9bf568b5a006a1d432d43.png" data-download-href="/uploads/short-url/vjoRYedet6xMZULwq1FzSaH6Tlh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db74d42a11b94b1c42b9bf568b5a006a1d432d43_2_690x459.png" alt="image" data-base62-sha1="vjoRYedet6xMZULwq1FzSaH6Tlh" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db74d42a11b94b1c42b9bf568b5a006a1d432d43_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db74d42a11b94b1c42b9bf568b5a006a1d432d43.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db74d42a11b94b1c42b9bf568b5a006a1d432d43.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1027×684 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here is the details:</p>
<pre><code class="lang-auto">*[Python] Failed to compute results.*
*[Python] Command '['D:/Programmes/3DSlicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'D:\\Programmes\\3DSlicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/LiYiRan/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-22_10+47+37.137/total-segmentator-input.nii', '-o', 'C:/Users/LiYiRan/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-22_10+47+37.137/segmentation', '--fast']' returned non-zero exit status 1.*
*Traceback (most recent call last):*
*  File "D:/Programmes/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 298, in onApplyButton*
*    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),*
*  File "D:/Programmes/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 961, in process*
*    self.processVolume(inputFile, inputVolume,*
*  File "D:/Programmes/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1001, in processVolume*
*    self.logProcessOutput(proc)*
*  File "D:/Programmes/3DSlicer/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 807, in logProcessOutput*
*    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)*
*subprocess.CalledProcessError: Command '['D:/Programmes/3DSlicer/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'D:\\Programmes\\3DSlicer\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/LiYiRan/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-22_10+47+37.137/total-segmentator-input.nii', '-o', 'C:/Users/LiYiRan/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-22_10+47+37.137/segmentation', '--fast']' returned non-zero exit status 1.*
</code></pre>

---

## Post #2 by @lassoan (2024-05-22 13:21 UTC)

<p>I can see in the screenshot that there is an error message about network communication (<code>requests.exceptions.ConnectionError</code>), but most of the details are not visible. Could you please copy the content of the textbox below the “Apply” button?</p>

---

## Post #3 by @liyiranran2001 (2024-05-22 16:13 UTC)

<p>Thanks for your reply! <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"> I have solved this problem by downloading these models manually.<br>
Regarding the network issue mentioned, it may be due to my VPN usage. However, the process would start slowly and finally crash even without VPN.<br>
I didn’t save the details after <em><strong>requests.exceptions.ConnectionError</strong></em>, but here is the related information copied from temp documents:<br>
<em>requests.exceptions.ProxyError: HTTPSConnectionPool(host=‘<a href="http://github.com" rel="noopener nofollow ugc">github.com</a>’, port=443): Max retries exceeded with url: /wasserth/TotalSegmentator/releases/download/v2.0.0-weights/Dataset297_TotalSegmentator_total_3mm_1559subj.zip (Caused by ProxyError(‘Unable to connect to proxy’, SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))))</em><br>
Hope this could help.</p>

---

## Post #4 by @lassoan (2024-05-22 17:24 UTC)

<p>Thanks for the update. The error indicates that your firewall or proxy server was blocking the direct internet connection.</p>

---

## Post #5 by @Yang1 (2026-01-23 03:12 UTC)

<p>Hi.I meet the same problem.Could you please share how did you download models manually?Now there is just one of the Segmentation task named “Total” could work on my slicer.</p>

---
