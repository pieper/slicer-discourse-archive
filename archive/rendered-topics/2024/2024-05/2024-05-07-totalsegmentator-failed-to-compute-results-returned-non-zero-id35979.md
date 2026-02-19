---
topic_id: 35979
title: "Totalsegmentator Failed To Compute Results Returned Non Zero"
date: 2024-05-07
url: https://discourse.slicer.org/t/35979
---

# TotalSegmentator "Failed to compute results." , "returned non-zero exit status 120"

**Topic ID**: 35979
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results-returned-non-zero-exit-status-120/35979

---

## Post #1 by @jimlytras (2024-05-07 22:34 UTC)

<p>Operating system: Windows 11 Home<br>
Slicer version: 5.6.2<br>
CPU: Intel(R) Core™ i5-9300H CPU @ 2.40GHz   2.40 GHz<br>
RAM: 8.00 GB (7.81 GB usable)<br>
Free disc space: 51.8 GB (SSD Windows C:)<br>
PyTorch version:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a082492e44443b0311f364e53d4a1eda3327fbd.png" alt="image" data-base62-sha1="cQspW8NNaQHA3RotIg4atPYvWln" width="484" height="70"></p>
<p>I have come across a relatively common problem (as I can see from the support forum).<br>
Specifically when I tried running TotalSegmentator (fast) on several CT scans (one at a time) i got the error “<strong>Failed to compute results</strong>”. The exact error text:</p>
<details>
<summary>
Summary</summary>
<p>Failed to compute results.</p>
<p>Command ‘[‘C:/Users/jimly/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_08+54+49.068/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_08+54+49.068/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/jimly/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 298, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/jimly/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 961, in process<br>
self.processVolume(inputFile, inputVolume,<br>
File “C:/Users/jimly/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 1035, in processVolume<br>
self.logProcessOutput(proc)<br>
File “C:/Users/jimly/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 807, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/jimly/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_08+54+49.068/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_08+54+49.068/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
</details>
<p>After reading the advice available on this topic, I did the following:</p>
<ol>
<li>Uninstalled PyTorch Util</li>
<li>Restarted 3D Slicer</li>
<li>Re-installed PyTorch Util with the requirement: &gt;=2</li>
<li>Restarted Slicer once more</li>
<li>Run TotalSegmentator again</li>
</ol>
<p>I got the same error.</p>
<p>I then did the following:</p>
<ol>
<li>Unistalled 3D Slicer</li>
<li>Entirely deleted the folders:<br>
C:\Users\jimly.totalsegmentator<br>
C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2<br>
C:\Users\jimly\AppData\Local\slicer.org\Slicer</li>
<li>Reinstalled 3D Slicer</li>
<li>Uninstalled PyTorch Util - Restarted 3D Slicer - Re-installed PyTorch Util with the requirement: &gt;=2 - Restarted Slicer once more</li>
<li>Forced TotalSegmentator Python Package to Reinstall</li>
<li>Run TotalSegmentator</li>
</ol>
<p>I got the exact same error.</p>
<p>I should also quote the system dialogue that occured while running TotalSegmentator:</p>
<details>
<summary>
Summary</summary>
<p>Processing started<br>
Writing input file to C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_15+40+18.698/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_15+40+18.698/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jimly/AppData/Local/Temp/Slicer/__SlicerTemp__2024-05-07_15+40+18.698/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>TotalSegmentator sends anonymous usage statistics. If you want to disable it check the documentation.<br>
Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Downloading model for Task 297 …</p>
<p>Downloading:   0%|          | 0.00/135M [00:00&lt;?, ?B/s]<br>
Downloading:   0%|          | 655k/135M [00:00&lt;00:24, 5.53MB/s]<br>
Downloading:   1%|          | 1.31M/135M [00:00&lt;00:22, 5.99MB/s]<br>
Downloading:   1%|1         | 1.97M/135M [00:00&lt;00:25, 5.21MB/s]<br>
Downloading:   2%|1         | 2.62M/135M [00:00&lt;00:23, 5.65MB/s]<br>
Downloading:   2%|2         | 3.28M/135M [00:00&lt;00:22, 5.84MB/s]<br>
Downloading:   3%|2         | 3.93M/135M [00:00&lt;00:21, 5.98MB/s]<br>
Downloading:   3%|3         | 4.59M/135M [00:00&lt;00:21, 6.10MB/s]<br>
Downloading:   4%|3         | 5.24M/135M [00:00&lt;00:21, 6.15MB/s]<br>
Downloading:   4%|4         | 5.90M/135M [00:00&lt;00:20, 6.20MB/s]<br>
Downloading:   5%|4         | 6.55M/135M [00:01&lt;00:20, 6.24MB/s]<br>
Downloading:   5%|5         | 7.21M/135M [00:01&lt;00:20, 6.12MB/s]<br>
Downloading:   6%|5         | 7.86M/135M [00:01&lt;00:20, 6.17MB/s]<br>
Downloading:   6%|6         | 8.52M/135M [00:01&lt;00:20, 6.20MB/s]<br>
Downloading:   7%|6         | 9.18M/135M [00:01&lt;00:20, 6.24MB/s]<br>
Downloading:   7%|7         | 9.83M/135M [00:01&lt;00:20, 6.25MB/s]<br>
Downloading:   8%|7         | 10.5M/135M [00:01&lt;00:19, 6.28MB/s]<br>
Downloading:   8%|8         | 11.1M/135M [00:01&lt;00:19, 6.29MB/s]<br>
Downloading:   9%|8         | 11.8M/135M [00:01&lt;00:19, 6.30MB/s]<br>
Downloading:   9%|9         | 12.5M/135M [00:02&lt;00:19, 6.30MB/s]<br>
Downloading:  10%|9         | 13.1M/135M [00:02&lt;00:19, 6.26MB/s]<br>
Downloading:  10%|#         | 13.8M/135M [00:02&lt;00:19, 6.31MB/s]<br>
Downloading:  11%|#         | 14.4M/135M [00:02&lt;00:19, 6.31MB/s]<br>
Downloading:  11%|#1        | 15.1M/135M [00:02&lt;00:19, 6.31MB/s]<br>
Downloading:  12%|#1        | 15.7M/135M [00:02&lt;00:18, 6.30MB/s]<br>
Downloading:  12%|#2        | 16.4M/135M [00:02&lt;00:18, 6.31MB/s]<br>
Downloading:  13%|#2        | 17.0M/135M [00:02&lt;00:18, 6.30MB/s]<br>
Downloading:  13%|#3        | 17.7M/135M [00:02&lt;00:18, 6.30MB/s]<br>
Downloading:  14%|#3        | 18.4M/135M [00:02&lt;00:18, 6.31MB/s]<br>
Downloading:  14%|#4        | 19.0M/135M [00:03&lt;00:18, 6.29MB/s]<br>
Downloading:  15%|#4        | 19.7M/135M [00:03&lt;00:18, 6.29MB/s]<br>
Downloading:  15%|#5        | 20.3M/135M [00:03&lt;00:18, 6.31MB/s]<br>
Downloading:  15%|#5        | 21.0M/135M [00:03&lt;00:18, 6.21MB/s]<br>
Downloading:  16%|#6        | 21.8M/135M [00:03&lt;00:17, 6.32MB/s]<br>
Downloading:  17%|#6        | 22.4M/135M [00:03&lt;00:17, 6.31MB/s]<br>
Downloading:  17%|#7        | 23.1M/135M [00:03&lt;00:17, 6.32MB/s]<br>
Downloading:  18%|#7        | 23.7M/135M [00:03&lt;00:17, 6.25MB/s]<br>
Downloading:  18%|#8        | 24.4M/135M [00:03&lt;00:17, 6.33MB/s]<br>
Downloading:  18%|#8        | 25.0M/135M [00:04&lt;00:17, 6.29MB/s]<br>
Downloading:  19%|#8        | 25.7M/135M [00:04&lt;00:18, 5.88MB/s]<br>
Downloading:  19%|#9        | 26.3M/135M [00:04&lt;00:19, 5.64MB/s]<br>
Downloading:  20%|#9        | 27.0M/135M [00:04&lt;00:18, 5.83MB/s]<br>
Downloading:  20%|##        | 27.7M/135M [00:04&lt;00:18, 5.97MB/s]<br>
Downloading:  21%|##        | 28.3M/135M [00:04&lt;00:17, 6.03MB/s]<br>
Downloading:  21%|#<span class="hashtag-raw">#1</span>       | 29.0M/135M [00:04&lt;00:17, 6.14MB/s]<br>
Downloading:  22%|#<span class="hashtag-raw">#1</span>       | 29.6M/135M [00:04&lt;00:17, 6.18MB/s]<br>
Downloading:  22%|#<span class="hashtag-raw">#2</span>       | 30.3M/135M [00:04&lt;00:16, 6.23MB/s]<br>
Downloading:  23%|#<span class="hashtag-raw">#2</span>       | 30.9M/135M [00:05&lt;00:16, 6.24MB/s]<br>
Downloading:  23%|#<span class="hashtag-raw">#3</span>       | 31.6M/135M [00:05&lt;00:16, 6.19MB/s]<br>
Downloading:  24%|#<span class="hashtag-raw">#3</span>       | 32.2M/135M [00:05&lt;00:17, 6.07MB/s]<br>
Downloading:  24%|#<span class="hashtag-raw">#4</span>       | 32.9M/135M [00:05&lt;00:16, 6.07MB/s]<br>
Downloading:  25%|#<span class="hashtag-raw">#4</span>       | 33.6M/135M [00:05&lt;00:16, 6.05MB/s]<br>
Downloading:  25%|#<span class="hashtag-raw">#5</span>       | 34.2M/135M [00:05&lt;00:16, 6.03MB/s]<br>
Downloading:  26%|#<span class="hashtag-raw">#5</span>       | 34.9M/135M [00:05&lt;00:16, 6.05MB/s]<br>
Downloading:  26%|#<span class="hashtag-raw">#6</span>       | 35.5M/135M [00:05&lt;00:16, 5.94MB/s]<br>
Downloading:  27%|#<span class="hashtag-raw">#6</span>       | 36.2M/135M [00:05&lt;00:17, 5.67MB/s]<br>
Downloading:  27%|#<span class="hashtag-raw">#7</span>       | 36.8M/135M [00:06&lt;00:17, 5.49MB/s]<br>
Downloading:  28%|#<span class="hashtag-raw">#7</span>       | 37.5M/135M [00:06&lt;00:18, 5.40MB/s]<br>
Downloading:  28%|#<span class="hashtag-raw">#8</span>       | 38.1M/135M [00:06&lt;00:17, 5.43MB/s]<br>
Downloading:  29%|#<span class="hashtag-raw">#8</span>       | 38.8M/135M [00:06&lt;00:17, 5.47MB/s]<br>
Downloading:  29%|#<span class="hashtag-raw">#9</span>       | 39.5M/135M [00:06&lt;00:17, 5.57MB/s]<br>
Downloading:  30%|#<span class="hashtag-raw">#9</span>       | 40.1M/135M [00:06&lt;00:16, 5.69MB/s]<br>
Downloading:  30%|###       | 40.8M/135M [00:06&lt;00:16, 5.75MB/s]<br>
Downloading:  31%|###       | 41.4M/135M [00:06&lt;00:16, 5.85MB/s]<br>
Downloading:  31%|##<span class="hashtag-raw">#1</span>      | 42.1M/135M [00:06&lt;00:15, 5.94MB/s]<br>
Downloading:  32%|##<span class="hashtag-raw">#1</span>      | 42.7M/135M [00:07&lt;00:15, 6.01MB/s]<br>
Downloading:  32%|##<span class="hashtag-raw">#2</span>      | 43.4M/135M [00:07&lt;00:16, 5.72MB/s]<br>
Downloading:  33%|##<span class="hashtag-raw">#2</span>      | 44.0M/135M [00:07&lt;00:17, 5.26MB/s]<br>
Downloading:  33%|##<span class="hashtag-raw">#3</span>      | 44.7M/135M [00:07&lt;00:18, 4.83MB/s]<br>
Downloading:  33%|##<span class="hashtag-raw">#3</span>      | 45.2M/135M [00:07&lt;00:19, 4.53MB/s]<br>
Downloading:  34%|##<span class="hashtag-raw">#3</span>      | 45.7M/135M [00:07&lt;00:20, 4.45MB/s]<br>
Downloading:  34%|##<span class="hashtag-raw">#4</span>      | 46.3M/135M [00:07&lt;00:20, 4.45MB/s]<br>
Downloading:  35%|##<span class="hashtag-raw">#4</span>      | 46.8M/135M [00:07&lt;00:19, 4.50MB/s]<br>
Downloading:  35%|##<span class="hashtag-raw">#4</span>      | 47.3M/135M [00:08&lt;00:19, 4.60MB/s]<br>
Downloading:  35%|##<span class="hashtag-raw">#5</span>      | 47.8M/135M [00:08&lt;00:18, 4.70MB/s]<br>
Downloading:  36%|##<span class="hashtag-raw">#5</span>      | 48.4M/135M [00:08&lt;00:18, 4.83MB/s]<br>
Downloading:  36%|##<span class="hashtag-raw">#6</span>      | 48.9M/135M [00:08&lt;00:17, 4.91MB/s]<br>
Downloading:  36%|##<span class="hashtag-raw">#6</span>      | 49.4M/135M [00:08&lt;00:19, 4.50MB/s]<br>
Downloading:  37%|##<span class="hashtag-raw">#6</span>      | 49.9M/135M [00:08&lt;00:19, 4.30MB/s]<br>
Downloading:  37%|##<span class="hashtag-raw">#7</span>      | 50.5M/135M [00:08&lt;00:19, 4.32MB/s]<br>
Downloading:  38%|##<span class="hashtag-raw">#7</span>      | 51.0M/135M [00:08&lt;00:19, 4.32MB/s]<br>
Downloading:  38%|##<span class="hashtag-raw">#8</span>      | 51.5M/135M [00:09&lt;00:19, 4.24MB/s]<br>
Downloading:  38%|##<span class="hashtag-raw">#8</span>      | 52.0M/135M [00:09&lt;00:19, 4.28MB/s]<br>
Downloading:  39%|##<span class="hashtag-raw">#8</span>      | 52.6M/135M [00:09&lt;00:21, 3.86MB/s]<br>
Downloading:  39%|##<span class="hashtag-raw">#9</span>      | 53.1M/135M [00:09&lt;00:23, 3.55MB/s]<br>
Downloading:  39%|##<span class="hashtag-raw">#9</span>      | 53.5M/135M [00:09&lt;00:22, 3.64MB/s]<br>
Downloading:  40%|##<span class="hashtag-raw">#9</span>      | 54.0M/135M [00:09&lt;00:21, 3.76MB/s]<br>
Downloading:  40%|####      | 54.4M/135M [00:09&lt;00:23, 3.50MB/s]<br>
Downloading:  40%|####      | 54.8M/135M [00:10&lt;00:24, 3.35MB/s]<br>
Downloading:  41%|####      | 55.2M/135M [00:10&lt;00:23, 3.35MB/s]<br>
Downloading:  41%|###<span class="hashtag-raw">#1</span>     | 55.6M/135M [00:10&lt;00:23, 3.37MB/s]<br>
Downloading:  41%|###<span class="hashtag-raw">#1</span>     | 56.0M/135M [00:10&lt;00:22, 3.48MB/s]<br>
Downloading:  42%|###<span class="hashtag-raw">#1</span>     | 56.4M/135M [00:10&lt;00:22, 3.56MB/s]<br>
Downloading:  42%|###<span class="hashtag-raw">#2</span>     | 56.9M/135M [00:10&lt;00:21, 3.71MB/s]<br>
Downloading:  42%|###<span class="hashtag-raw">#2</span>     | 57.4M/135M [00:10&lt;00:20, 3.88MB/s]<br>
Downloading:  43%|###<span class="hashtag-raw">#2</span>     | 57.9M/135M [00:10&lt;00:19, 3.99MB/s]<br>
Downloading:  43%|###<span class="hashtag-raw">#3</span>     | 58.5M/135M [00:10&lt;00:18, 4.07MB/s]<br>
Downloading:  44%|###<span class="hashtag-raw">#3</span>     | 59.0M/135M [00:11&lt;00:17, 4.29MB/s]<br>
Downloading:  44%|###<span class="hashtag-raw">#3</span>     | 59.5M/135M [00:11&lt;00:16, 4.48MB/s]<br>
Downloading:  44%|###<span class="hashtag-raw">#4</span>     | 60.2M/135M [00:11&lt;00:15, 4.73MB/s]<br>
Downloading:  45%|###<span class="hashtag-raw">#4</span>     | 60.8M/135M [00:11&lt;00:15, 4.97MB/s]<br>
Downloading:  45%|###<span class="hashtag-raw">#5</span>     | 61.5M/135M [00:11&lt;00:14, 5.12MB/s]<br>
Downloading:  46%|###<span class="hashtag-raw">#5</span>     | 62.1M/135M [00:11&lt;00:13, 5.28MB/s]<br>
Downloading:  46%|###<span class="hashtag-raw">#6</span>     | 62.8M/135M [00:11&lt;00:13, 5.29MB/s]<br>
Downloading:  47%|###<span class="hashtag-raw">#6</span>     | 63.4M/135M [00:11&lt;00:15, 4.73MB/s]<br>
Downloading:  47%|###<span class="hashtag-raw">#7</span>     | 64.0M/135M [00:12&lt;00:16, 4.27MB/s]<br>
Downloading:  48%|###<span class="hashtag-raw">#7</span>     | 64.5M/135M [00:12&lt;00:17, 4.01MB/s]<br>
Downloading:  48%|###<span class="hashtag-raw">#8</span>     | 65.0M/135M [00:12&lt;00:17, 3.94MB/s]<br>
Downloading:  48%|###<span class="hashtag-raw">#8</span>     | 65.5M/135M [00:12&lt;00:17, 3.92MB/s]<br>
Downloading:  49%|###<span class="hashtag-raw">#8</span>     | 66.1M/135M [00:12&lt;00:17, 3.96MB/s]<br>
Downloading:  49%|###<span class="hashtag-raw">#9</span>     | 66.6M/135M [00:12&lt;00:16, 4.05MB/s]<br>
Downloading:  50%|###<span class="hashtag-raw">#9</span>     | 67.1M/135M [00:12&lt;00:16, 4.22MB/s]<br>
Downloading:  50%|###<span class="hashtag-raw">#9</span>     | 67.6M/135M [00:12&lt;00:15, 4.33MB/s]<br>
Downloading:  50%|#####     | 68.2M/135M [00:13&lt;00:14, 4.50MB/s]<br>
Downloading:  51%|#####     | 68.7M/135M [00:13&lt;00:14, 4.66MB/s]<br>
Downloading:  51%|####<span class="hashtag-raw">#1</span>    | 69.2M/135M [00:13&lt;00:14, 4.51MB/s]<br>
Downloading:  52%|####<span class="hashtag-raw">#1</span>    | 69.7M/135M [00:13&lt;00:16, 3.97MB/s]<br>
Downloading:  52%|####<span class="hashtag-raw">#1</span>    | 70.3M/135M [00:13&lt;00:18, 3.46MB/s]<br>
Downloading:  52%|####<span class="hashtag-raw">#2</span>    | 70.6M/135M [00:13&lt;00:21, 3.01MB/s]<br>
Downloading:  52%|####<span class="hashtag-raw">#2</span>    | 71.0M/135M [00:14&lt;00:23, 2.79MB/s]<br>
Downloading:  53%|####<span class="hashtag-raw">#2</span>    | 71.4M/135M [00:14&lt;00:23, 2.76MB/s]<br>
Downloading:  53%|####<span class="hashtag-raw">#3</span>    | 71.8M/135M [00:14&lt;00:22, 2.79MB/s]<br>
Downloading:  53%|####<span class="hashtag-raw">#3</span>    | 72.2M/135M [00:14&lt;00:22, 2.87MB/s]<br>
Downloading:  54%|####<span class="hashtag-raw">#3</span>    | 72.6M/135M [00:14&lt;00:20, 3.02MB/s]<br>
Downloading:  54%|####<span class="hashtag-raw">#3</span>    | 73.0M/135M [00:14&lt;00:19, 3.18MB/s]<br>
Downloading:  54%|####<span class="hashtag-raw">#4</span>    | 73.4M/135M [00:14&lt;00:18, 3.36MB/s]<br>
Downloading:  55%|####<span class="hashtag-raw">#4</span>    | 73.9M/135M [00:14&lt;00:17, 3.56MB/s]<br>
Downloading:  55%|####<span class="hashtag-raw">#4</span>    | 74.3M/135M [00:15&lt;00:24, 2.48MB/s]<br>
Downloading:  55%|####<span class="hashtag-raw">#5</span>    | 74.8M/135M [00:15&lt;00:21, 2.88MB/s]<br>
Downloading:  56%|####<span class="hashtag-raw">#5</span>    | 75.4M/135M [00:15&lt;00:18, 3.28MB/s]<br>
Downloading:  56%|####<span class="hashtag-raw">#6</span>    | 75.9M/135M [00:15&lt;00:16, 3.67MB/s]<br>
Downloading:  56%|####<span class="hashtag-raw">#6</span>    | 76.4M/135M [00:15&lt;00:14, 4.00MB/s]<br>
Downloading:  57%|####<span class="hashtag-raw">#6</span>    | 76.9M/135M [00:15&lt;00:13, 4.30MB/s]<br>
Downloading:  57%|####<span class="hashtag-raw">#7</span>    | 77.5M/135M [00:15&lt;00:13, 4.42MB/s]<br>
Downloading:  58%|####<span class="hashtag-raw">#7</span>    | 78.0M/135M [00:15&lt;00:13, 4.24MB/s]<br>
Downloading:  58%|####<span class="hashtag-raw">#7</span>    | 78.5M/135M [00:16&lt;00:13, 4.09MB/s]<br>
Downloading:  58%|####<span class="hashtag-raw">#8</span>    | 79.0M/135M [00:16&lt;00:14, 3.86MB/s]<br>
Downloading:  59%|####<span class="hashtag-raw">#8</span>    | 79.6M/135M [00:16&lt;00:13, 4.00MB/s]<br>
Downloading:  59%|####<span class="hashtag-raw">#9</span>    | 80.1M/135M [00:16&lt;00:13, 4.21MB/s]<br>
Downloading:  60%|####<span class="hashtag-raw">#9</span>    | 80.6M/135M [00:16&lt;00:12, 4.40MB/s]<br>
Downloading:  60%|####<span class="hashtag-raw">#9</span>    | 81.1M/135M [00:16&lt;00:11, 4.57MB/s]<br>
Downloading:  60%|######    | 81.7M/135M [00:16&lt;00:11, 4.65MB/s]<br>
Downloading:  61%|######    | 82.2M/135M [00:16&lt;00:11, 4.72MB/s]<br>
Downloading:  61%|#####<span class="hashtag-raw">#1</span>   | 82.8M/135M [00:17&lt;00:10, 4.81MB/s]<br>
Downloading:  62%|#####<span class="hashtag-raw">#1</span>   | 83.4M/135M [00:17&lt;00:11, 4.71MB/s]<br>
Downloading:  62%|#####<span class="hashtag-raw">#1</span>   | 83.9M/135M [00:17&lt;00:11, 4.55MB/s]<br>
Downloading:  62%|#####<span class="hashtag-raw">#2</span>   | 84.4M/135M [00:17&lt;00:11, 4.49MB/s]<br>
Downloading:  63%|#####<span class="hashtag-raw">#2</span>   | 84.9M/135M [00:17&lt;00:11, 4.58MB/s]<br>
Downloading:  63%|#####<span class="hashtag-raw">#3</span>   | 85.5M/135M [00:17&lt;00:10, 4.66MB/s]<br>
Downloading:  64%|#####<span class="hashtag-raw">#3</span>   | 86.0M/135M [00:17&lt;00:10, 4.50MB/s]<br>
Downloading:  64%|#####<span class="hashtag-raw">#3</span>   | 86.5M/135M [00:17&lt;00:11, 4.22MB/s]<br>
Downloading:  64%|#####<span class="hashtag-raw">#4</span>   | 87.0M/135M [00:18&lt;00:11, 4.06MB/s]<br>
Downloading:  65%|#####<span class="hashtag-raw">#4</span>   | 87.6M/135M [00:18&lt;00:11, 4.06MB/s]<br>
Downloading:  65%|#####<span class="hashtag-raw">#5</span>   | 88.1M/135M [00:18&lt;00:11, 4.15MB/s]<br>
Downloading:  65%|#####<span class="hashtag-raw">#5</span>   | 88.6M/135M [00:18&lt;00:11, 4.22MB/s]<br>
Downloading:  66%|#####<span class="hashtag-raw">#5</span>   | 89.1M/135M [00:18&lt;00:10, 4.38MB/s]<br>
Downloading:  66%|#####<span class="hashtag-raw">#6</span>   | 89.7M/135M [00:18&lt;00:10, 4.52MB/s]<br>
Downloading:  67%|#####<span class="hashtag-raw">#6</span>   | 90.2M/135M [00:18&lt;00:09, 4.68MB/s]<br>
Downloading:  67%|#####<span class="hashtag-raw">#6</span>   | 90.7M/135M [00:18&lt;00:09, 4.81MB/s]<br>
Downloading:  67%|#####<span class="hashtag-raw">#7</span>   | 91.4M/135M [00:18&lt;00:08, 4.99MB/s]<br>
Downloading:  68%|#####<span class="hashtag-raw">#7</span>   | 91.9M/135M [00:19&lt;00:08, 4.94MB/s]<br>
Downloading:  68%|#####<span class="hashtag-raw">#8</span>   | 92.4M/135M [00:19&lt;00:12, 3.41MB/s]<br>
Downloading:  69%|#####<span class="hashtag-raw">#8</span>   | 93.1M/135M [00:19&lt;00:10, 3.96MB/s]<br>
Downloading:  69%|#####<span class="hashtag-raw">#9</span>   | 93.7M/135M [00:19&lt;00:09, 4.44MB/s]<br>
Downloading:  70%|#####<span class="hashtag-raw">#9</span>   | 94.4M/135M [00:19&lt;00:08, 4.87MB/s]<br>
Downloading:  70%|#######   | 95.0M/135M [00:19&lt;00:07, 5.21MB/s]<br>
Downloading:  71%|#######   | 95.7M/135M [00:19&lt;00:07, 5.50MB/s]<br>
Downloading:  71%|######<span class="hashtag-raw">#1</span>  | 96.3M/135M [00:20&lt;00:06, 5.71MB/s]<br>
Downloading:  72%|######<span class="hashtag-raw">#1</span>  | 97.0M/135M [00:20&lt;00:06, 5.88MB/s]<br>
Downloading:  72%|######<span class="hashtag-raw">#2</span>  | 97.6M/135M [00:20&lt;00:06, 5.99MB/s]<br>
Downloading:  73%|######<span class="hashtag-raw">#2</span>  | 98.3M/135M [00:20&lt;00:06, 6.09MB/s]<br>
Downloading:  73%|######<span class="hashtag-raw">#3</span>  | 99.0M/135M [00:20&lt;00:05, 6.15MB/s]<br>
Downloading:  74%|######<span class="hashtag-raw">#3</span>  | 99.6M/135M [00:20&lt;00:05, 6.19MB/s]<br>
Downloading:  74%|######<span class="hashtag-raw">#4</span>  | 100M/135M [00:20&lt;00:05, 6.24MB/s]<br>
Downloading:  75%|######<span class="hashtag-raw">#4</span>  | 101M/135M [00:20&lt;00:05, 6.25MB/s]<br>
Downloading:  75%|######<span class="hashtag-raw">#5</span>  | 102M/135M [00:20&lt;00:05, 6.25MB/s]<br>
Downloading:  76%|######<span class="hashtag-raw">#5</span>  | 102M/135M [00:20&lt;00:05, 6.28MB/s]<br>
Downloading:  76%|######<span class="hashtag-raw">#5</span>  | 103M/135M [00:21&lt;00:05, 6.28MB/s]<br>
Downloading:  76%|######<span class="hashtag-raw">#6</span>  | 104M/135M [00:21&lt;00:05, 6.33MB/s]<br>
Downloading:  77%|######<span class="hashtag-raw">#6</span>  | 104M/135M [00:21&lt;00:04, 6.27MB/s]<br>
Downloading:  77%|######<span class="hashtag-raw">#7</span>  | 105M/135M [00:21&lt;00:05, 5.78MB/s]<br>
Downloading:  78%|######<span class="hashtag-raw">#7</span>  | 106M/135M [00:21&lt;00:05, 5.59MB/s]<br>
Downloading:  78%|######<span class="hashtag-raw">#8</span>  | 106M/135M [00:21&lt;00:06, 4.51MB/s]<br>
Downloading:  79%|######<span class="hashtag-raw">#8</span>  | 107M/135M [00:21&lt;00:06, 4.21MB/s]<br>
Downloading:  79%|######<span class="hashtag-raw">#9</span>  | 107M/135M [00:22&lt;00:06, 4.02MB/s]<br>
Downloading:  80%|######<span class="hashtag-raw">#9</span>  | 108M/135M [00:22&lt;00:06, 3.99MB/s]<br>
Downloading:  80%|######<span class="hashtag-raw">#9</span>  | 108M/135M [00:22&lt;00:06, 4.08MB/s]<br>
Downloading:  80%|########  | 109M/135M [00:22&lt;00:06, 4.16MB/s]<br>
Downloading:  81%|########  | 109M/135M [00:22&lt;00:06, 4.30MB/s]<br>
Downloading:  81%|#######<span class="hashtag-raw">#1</span> | 110M/135M [00:22&lt;00:05, 4.35MB/s]<br>
Downloading:  82%|#######<span class="hashtag-raw">#1</span> | 110M/135M [00:22&lt;00:06, 4.06MB/s]<br>
Downloading:  82%|#######<span class="hashtag-raw">#1</span> | 111M/135M [00:22&lt;00:06, 3.65MB/s]<br>
Downloading:  82%|#######<span class="hashtag-raw">#2</span> | 111M/135M [00:23&lt;00:07, 3.44MB/s]<br>
Downloading:  82%|#######<span class="hashtag-raw">#2</span> | 112M/135M [00:23&lt;00:07, 3.36MB/s]<br>
Downloading:  83%|#######<span class="hashtag-raw">#2</span> | 112M/135M [00:23&lt;00:06, 3.36MB/s]<br>
Downloading:  83%|#######<span class="hashtag-raw">#3</span> | 112M/135M [00:23&lt;00:06, 3.40MB/s]<br>
Downloading:  83%|#######<span class="hashtag-raw">#3</span> | 113M/135M [00:23&lt;00:06, 3.48MB/s]<br>
Downloading:  84%|#######<span class="hashtag-raw">#3</span> | 113M/135M [00:23&lt;00:06, 3.65MB/s]<br>
Downloading:  84%|#######<span class="hashtag-raw">#4</span> | 114M/135M [00:23&lt;00:06, 3.41MB/s]<br>
Downloading:  84%|#######<span class="hashtag-raw">#4</span> | 114M/135M [00:23&lt;00:05, 3.62MB/s]<br>
Downloading:  85%|#######<span class="hashtag-raw">#4</span> | 115M/135M [00:24&lt;00:05, 3.86MB/s]<br>
Downloading:  85%|#######<span class="hashtag-raw">#5</span> | 115M/135M [00:24&lt;00:04, 4.08MB/s]<br>
Downloading:  86%|#######<span class="hashtag-raw">#5</span> | 116M/135M [00:24&lt;00:04, 4.30MB/s]<br>
Downloading:  86%|#######<span class="hashtag-raw">#5</span> | 116M/135M [00:24&lt;00:04, 4.52MB/s]<br>
Downloading:  86%|#######<span class="hashtag-raw">#6</span> | 117M/135M [00:24&lt;00:03, 4.72MB/s]<br>
Downloading:  87%|#######<span class="hashtag-raw">#6</span> | 118M/135M [00:24&lt;00:03, 4.96MB/s]<br>
Downloading:  87%|#######<span class="hashtag-raw">#7</span> | 118M/135M [00:24&lt;00:03, 5.10MB/s]<br>
Downloading:  88%|#######<span class="hashtag-raw">#7</span> | 119M/135M [00:24&lt;00:03, 5.31MB/s]<br>
Downloading:  88%|#######<span class="hashtag-raw">#8</span> | 120M/135M [00:24&lt;00:03, 4.93MB/s]<br>
Downloading:  89%|#######<span class="hashtag-raw">#8</span> | 120M/135M [00:25&lt;00:03, 4.76MB/s]<br>
Downloading:  89%|#######<span class="hashtag-raw">#9</span> | 121M/135M [00:25&lt;00:03, 4.68MB/s]<br>
Downloading:  89%|#######<span class="hashtag-raw">#9</span> | 121M/135M [00:25&lt;00:03, 4.70MB/s]<br>
Downloading:  90%|#######<span class="hashtag-raw">#9</span> | 122M/135M [00:25&lt;00:02, 4.74MB/s]<br>
Downloading:  90%|######### | 122M/135M [00:25&lt;00:02, 4.80MB/s]<br>
Downloading:  91%|######### | 123M/135M [00:25&lt;00:02, 4.87MB/s]<br>
Downloading:  91%|#########1| 123M/135M [00:25&lt;00:02, 4.66MB/s]<br>
Downloading:  92%|#########1| 124M/135M [00:25&lt;00:02, 4.74MB/s]<br>
Downloading:  92%|#########2| 125M/135M [00:26&lt;00:02, 4.86MB/s]<br>
Downloading:  92%|#########2| 125M/135M [00:26&lt;00:02, 4.70MB/s]<br>
Downloading:  93%|#########2| 126M/135M [00:26&lt;00:02, 4.59MB/s]<br>
Downloading:  93%|#########3| 126M/135M [00:26&lt;00:01, 4.60MB/s]<br>
Downloading:  94%|#########3| 127M/135M [00:26&lt;00:01, 4.65MB/s]<br>
Downloading:  94%|#########4| 127M/135M [00:26&lt;00:01, 4.70MB/s]<br>
Downloading:  94%|#########4| 128M/135M [00:26&lt;00:01, 4.81MB/s]<br>
Downloading:  95%|#########4| 128M/135M [00:26&lt;00:01, 4.96MB/s]<br>
Downloading:  95%|#########5| 129M/135M [00:26&lt;00:01, 5.03MB/s]<br>
Downloading:  96%|#########5| 130M/135M [00:27&lt;00:01, 5.20MB/s]<br>
Downloading:  96%|#########6| 130M/135M [00:27&lt;00:00, 5.38MB/s]<br>
Downloading:  97%|#########6| 131M/135M [00:27&lt;00:00, 5.54MB/s]<br>
Downloading:  97%|#########7| 132M/135M [00:27&lt;00:00, 5.39MB/s]<br>
Downloading:  98%|#########7| 132M/135M [00:27&lt;00:00, 5.06MB/s]<br>
Downloading:  98%|#########8| 133M/135M [00:27&lt;00:00, 4.92MB/s]<br>
Downloading:  98%|#########8| 133M/135M [00:27&lt;00:00, 4.25MB/s]<br>
Downloading:  99%|#########8| 134M/135M [00:28&lt;00:00, 3.58MB/s]<br>
Downloading:  99%|#########9| 134M/135M [00:28&lt;00:00, 3.39MB/s]<br>
Downloading:  99%|#########9| 135M/135M [00:28&lt;00:00, 3.30MB/s]<br>
Downloading: 100%|#########9| 135M/135M [00:28&lt;00:00, 3.30MB/s]<br>
Downloading: 100%|##########| 135M/135M [00:28&lt;00:00, 3.31MB/s]<br>
Downloading: 100%|##########| 135M/135M [00:28&lt;00:00, 4.74MB/s]<br>
multiprocessing.pool.RemoteTraceback:<br>
“”"<br>
Traceback (most recent call last):<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py”, line 125, in worker<br>
result = (True, func(*args, **kwds))<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py”, line 51, in starmapstar<br>
return list(itertools.starmap(args[0], args[1]))<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\export_prediction.py”, line 39, in export_prediction_from_softmax<br>
segmentation = label_manager.convert_logits_to_segmentation(predicted_array_or_file)<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\utilities\label_handling\label_handling.py”, line 181, in convert_logits_to_segmentation<br>
probabilities = self.apply_inference_nonlin(predicted_logits)<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\utilities\label_handling\label_handling.py”, line 140, in apply_inference_nonlin<br>
probabilities = self.inference_nonlin(logits_torch)<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\utilities\helpers.py”, line 5, in softmax_helper_dim0<br>
return torch.softmax(x, 0)<br>
RuntimeError: [enforce fail at alloc_cpu.cpp:114] data. DefaultCPUAllocator: not enough memory: you tried to allocate 1889976736 bytes.<br>
“”"</p>
<p>The above exception was the direct cause of the following exception:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
return _run_code(code, main_globals, None,<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File "C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 127, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 293, in totalsegmentator<br>
seg_img, ct_img = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 395, in nnUNet_predict_image<br>
nnUNetv2_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta,<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 178, in nnUNetv2_predict<br>
predict_from_raw_data(dir_in,<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 347, in predict_from_raw_data<br>
[i.get() for i in r]<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 347, in <br>
[i.get() for i in r]<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\multiprocessing\pool.py”, line 771, in get<br>
raise self._value<br>
RuntimeError: [enforce fail at alloc_cpu.cpp:114] data. DefaultCPUAllocator: not enough memory: you tried to allocate 1889976736 bytes.<br>
Exception in thread Thread-5:<br>
Traceback (most recent call last):<br>
File “C:\Users\jimly\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\threading.py”, line 973, in _bootstrap_inner<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000001CF5434B130&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’<br>
Download finished. Extracting…<br>
Resampling…<br>
Resampled in 63.89s<br>
Predicting…</p>
</details>
<p>Please help me.</p>

---

## Post #2 by @Matteboo (2024-05-13 11:51 UTC)

<p>Hello,<br>
Are running totalSegmentator on the sample data or on some of your data?<br>
Maybe try on the sample data to make sure that the error is still there</p>

---

## Post #3 by @jimlytras (2024-06-01 08:54 UTC)

<p>Thanks for the feedback!</p>
<p>I have tried it on some sample data and it works.<br>
What can I do to apply totalSegmentator on my data?</p>

---

## Post #4 by @lassoan (2024-06-01 11:45 UTC)

<aside class="quote no-group" data-username="Matteboo" data-post="2" data-topic="35979">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>Are running totalSegmentator on the sample data or on some of your data?<br>
Maybe try on the sample data to make sure that the error is still there</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="jimlytras" data-post="3" data-topic="35979">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jimlytras/48/79192_2.png" class="avatar"> jimlytras:</div>
<blockquote>
<p>I have tried it on some sample data and it works.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/matteboo">@Matteboo</a>, very good intuition.</p>
<aside class="quote no-group" data-username="jimlytras" data-post="3" data-topic="35979">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jimlytras/48/79192_2.png" class="avatar"> jimlytras:</div>
<blockquote>
<p>What can I do to apply totalSegmentator on my data?</p>
</blockquote>
</aside>
<p>As the error message described, your computer does not have enough memory to process your image:</p>
<blockquote>
<p>RuntimeError: [enforce fail at alloc_cpu.cpp:114] data. DefaultCPUAllocator: not enough memory: you tried to allocate 1889976736 bytes.</p>
</blockquote>
<p>You can use Crop volume module to crop the your image to the relevant region and/or resample (with using a scaling factor &gt;1) until the memory usage drops low enough so that your computer can handle it.</p>
<p>Alternatively, you can add more physical RAM to your computer (you need to buy additional hardware component and put it into your computer) or adjust your Windows system settings to increase the amount of virtual memory (you can add as much virtual memory as you have free disk space, but processing can be many times slower).</p>

---

## Post #5 by @jimlytras (2024-06-01 12:47 UTC)

<p>Thanks a lot for the prompt response!<br>
I will try physically upgrading my RAM and I will return with some feedback.</p>
<p>How much RAM would you suggest I add?</p>
<p>I read that I should have 10-fold memory than the ammount of data I am trying to load. If that holds true and I tried to load 1889976736 bytes (~2 gb), then I should have at least 20 gb RAM.</p>

---

## Post #6 by @lassoan (2024-06-01 13:33 UTC)

<p>I would say nowadays 16GB would be a minimum, but if you work with larger images then 32GB may be useful, too.</p>
<p>For AI image segmentation the biggest difference in computation time would be if you could get a good NVIDIA GPU. If you only use pre-trained models then I would recommend one with at least 16GB RAM, if you want to do training as well then I would recommend at least 24GB GPU RAM.</p>

---
