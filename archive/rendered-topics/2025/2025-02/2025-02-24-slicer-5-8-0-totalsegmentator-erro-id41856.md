---
topic_id: 41856
title: "Slicer 5 8 0 Totalsegmentator Erro"
date: 2025-02-24
url: https://discourse.slicer.org/t/41856
---

# Slicer 5.8.0 totalsegmentator erro

**Topic ID**: 41856
**Date**: 2025-02-24
**URL**: https://discourse.slicer.org/t/slicer-5-8-0-totalsegmentator-erro/41856

---

## Post #1 by @hepato (2025-02-24 11:47 UTC)

<p>I installed slicer 5.8.0 and extension of total segmentator .But total segmentator  did not work successfully. And  total segmentator run successfully in slicer 5.6.2.<br>
I reinstalled slicer 5.8.0 and extension of total segmentator several times, but problem is still  not resolved.<br>
Could you give me some suggestion to resolve this problem?</p>
<p>error window pops up：</p>
<pre><code class="lang-auto">Failed to compute results.

Command '['/Applications/Slicer 2.app/Contents/bin/../bin/PythonSlicer', '/Applications/Slicer 2.app/Contents/lib/Python/bin/TotalSegmentator', '-i', '/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2025-02-24_19+49+25.194/total-segmentator-input.nii', '-o', '/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2025-02-24_19+49+25.194/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.

Traceback (most recent call last):
  File "/Applications/Slicer 2.app/Contents/bin/Python/slicer/util.py", line 3303, in tryWithErrorDisplay
    yield
  File "/Applications/Slicer 2.app/Contents/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "/Applications/Slicer 2.app/Contents/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 1037, in process
    self.processVolume(inputFile, inputVolume,
  File "/Applications/Slicer 2.app/Contents/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 1104, in processVolume
    self.logProcessOutput(proc)
  File "/Applications/Slicer 2.app/Contents/Extensions-33216/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py", line 883, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer 2.app/Contents/bin/../bin/PythonSlicer', '/Applications/Slicer 2.app/Contents/lib/Python/bin/TotalSegmentator', '-i', '/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2025-02-24_19+49+25.194/total-segmentator-input.nii', '-o', '/private/var/folders/xm/g5xx81wd55b1rvslqnrdgwv80000gn/T/Slicer-cy/__SlicerTemp__2025-02-24_19+49+25.194/segmentation', '--ml', '--task', 'total', '--fast']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @MasatoshiOBA (2025-02-24 12:15 UTC)

<p><strong>Are you using a GPU?</strong><br>
If so, could it be that GPU memory is not being released properly or is occupied by another process?</p>
<p>I had a similar issue before, and in my case, an <strong>“out of memory”</strong> error didn’t appear, which made it difficult to figure out the cause. You might want to check if GPU memory is still in use by running:</p>
<p>sh</p>
<pre><code class="lang-auto">nvidia-smi
</code></pre>
<p>If some process is occupying the memory, try terminating it and then running TotalSegmentator again.</p>

---

## Post #3 by @hepato (2025-02-24 12:23 UTC)

<p>thanks for your reply！<br>
I use MacBook Air m1,which gpu not available.<br>
And total segmentation work well in 5.6.2 version of slicer installed in my Macbook for long time.</p>

---

## Post #4 by @MasatoshiOBA (2025-02-24 12:44 UTC)

<p>Since you’re using a <strong>CPU</strong>, this topic might be relevant to your issue:</p>
<p><a href="https://discourse.slicer.org/t/how-to-solve-pytorch-version-error-in-totalsegmentator-using-cpu/36269">How to solve PyTorch version error in TotalSegmentator using CPU</a></p>
<p>It seems that there could be a <strong>PyTorch version compatibility issue</strong> when running TotalSegmentator on CPU. You might want to check if updating or downgrading PyTorch helps resolve the problem.</p>

---

## Post #5 by @hepato (2025-02-24 12:59 UTC)

<p>I check PyTorch module. and PyTorch 2.2.2 already installed ,using cpu.</p>

---
