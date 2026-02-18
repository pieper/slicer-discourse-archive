# MultiVolumeExplorer - labeling chart error

**Topic ID**: 15508
**Date**: 2021-01-13
**URL**: https://discourse.slicer.org/t/multivolumeexplorer-labeling-chart-error/15508

---

## Post #1 by @Diana (2021-01-13 16:38 UTC)

<p>Hi there,</p>
<p>I am expieriencing an error when I try using the static plotting in MultiVolumeExplorer when I want to plot signal drop with time:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Users/Diana/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-loadable-modules/Python/qSlicerMultiVolumeExplorerModuleWidget.py”, line 520, in onLabeledChartRequested<br>
chartViewNode.requestChartCreation()<br>
File “C:\Users\Diana\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-loadable-modules\Python\qSlicerMultiVolumeExplorerCharts.py”, line 422, in requestChartCreation<br>
chartNode = self.createChartNodeAndInsertData()<br>
File “C:\Users\Diana\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-loadable-modules\Python\qSlicerMultiVolumeExplorerCharts.py”, line 493, in createChartNodeAndInsertData<br>
colorStr = Helper.RGBtoHex(rgb[0] * 255, rgb[1] * 255, rgb[2] * 255)<br>
File “C:\Users\Diana\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-loadable-modules\Python\qSlicerMultiVolumeExplorerModuleHelper.py”, line 9, in RGBtoHex<br>
return ‘#%02X%02X%02X’ % (r,g,b)<br>
TypeError: %X format: an integer is required, not float</p>
</blockquote>
<p>I have different samples (different segments) in one volume, and they end up totally messed up on the chart… can anyone help me solve this out, please?</p>
<p>I use the newest stable version (4.11.20200930)</p>
<p>Thanks for any help!</p>

---

## Post #2 by @lassoan (2021-01-13 21:14 UTC)

<p>Does plotting works correctly if you load the data as a volume sequence and use plotting in Sequences module?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38ff62b94f2cc49a9cf0dba81b546e47f4b36a74.jpeg" data-download-href="/uploads/short-url/88dTLThmhywB23TDO64fiRPzves.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38ff62b94f2cc49a9cf0dba81b546e47f4b36a74_2_690x419.jpeg" alt="image" data-base62-sha1="88dTLThmhywB23TDO64fiRPzves" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38ff62b94f2cc49a9cf0dba81b546e47f4b36a74_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38ff62b94f2cc49a9cf0dba81b546e47f4b36a74_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/38ff62b94f2cc49a9cf0dba81b546e47f4b36a74_2_1380x838.jpeg 2x" data-dominant-color="767474"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If not, please save your scene as .mrb file, upload it somewhere and post the link here so that we can investigate.</p>

---

## Post #3 by @Diana (2021-01-19 10:09 UTC)

<p>Dear Andras,</p>
<p>thank you very much for your reply! The interactive plotting works fine for both, the Sequences and MiltiVolumeExplorer modules. The problem appears when I want to plot the chart:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e65f883698bcef81f3348fefd10d665a0c103e5.png" alt="image" data-base62-sha1="6CsqY2YFr2XxHiWqBnqtiEJVBdz" width="556" height="388"></p>
<p>I tried the previous stable version (4.10.2) and there it worked fine, the arrays are labelled accordingly to segments (samples):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/729ee874c4565fb5a38575ea8e94ea9cb580e50b.png" alt="image" data-base62-sha1="glYTd9BCwPnDX544iTqFfmNLdbl" width="565" height="393"></p>
<p>Can this be fixed in the newest version?</p>

---

## Post #4 by @lassoan (2021-01-19 14:44 UTC)

<p>Can you describe the steps to create this chart (what module you open, what buttons you click)?</p>

---

## Post #5 by @Diana (2021-01-20 09:11 UTC)

<p>I load the data (as a 29 frames MultiVolume by EchoTime) and create a segmentation with 14 segments in ‘SegmentEditor’. Then in ‘Segmentations’ I export as LabelMap.</p>
<p>I open the MultiVolumeExplorer, and in interactive plotting everything looks fine,  I select ‘Probed label volume’ under ‘Plotting Settings’ and when I click ‘Chart’ the error above occurs. The chart is first empty, I have to manually click it in the drop down menu (in the 4.10.2 version, the chart appeared automatically). The values look correct but the assignment to the segments is not.</p>

---

## Post #6 by @XJGB (2021-07-30 12:21 UTC)

<p>Hi everyone I encounter the same problem working on a windows system, exactly as described by Diana?<br>
Has there been a solution in the meantime?<br>
Thanks for your Help<br>
best Florian</p>

---

## Post #7 by @lassoan (2021-08-01 21:44 UTC)

<p>It works fine, you just need to use a scatter plot of an X and Y series.</p>
<p>Line plot just shows one series, which defines the Y values. X values simply contain the indices (0, 1, 2,…).</p>

---

## Post #8 by @XJGB (2021-08-02 15:00 UTC)

<p>Thanks for your response!<br>
I m not sure if I have understood correctly. But maybe I have also not expressed my problem in enough detail.<br>
I have a perfusion dataset and wish to picture signal intesity over time within different ROIs.<br>
So scatter plotting is not really an option.<br>
How do I have to tell slicer which ROI refers to which color and to represent the Signal Intensity over time accordingly?<br>
Thanks again Florian</p>

---

## Post #9 by @lassoan (2021-08-02 17:21 UTC)

<p>MultiVolume module is being replaced by Sequences module. We’ll add a dedicated module for time-intensity plots, but for now you can copy-paste <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#plot-segments-average-intensity-over-time">this code snippet</a> into Slicer’s Python console to generate the plot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55a1bb3499056483911269c1eab985b2ba99221c.jpeg" data-download-href="/uploads/short-url/cdx5K6rHRY6D3aY3tJoDhSHpOa0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55a1bb3499056483911269c1eab985b2ba99221c_2_690x268.jpeg" alt="image" data-base62-sha1="cdx5K6rHRY6D3aY3tJoDhSHpOa0" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55a1bb3499056483911269c1eab985b2ba99221c_2_690x268.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55a1bb3499056483911269c1eab985b2ba99221c_2_1035x402.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55a1bb3499056483911269c1eab985b2ba99221c_2_1380x536.jpeg 2x" data-dominant-color="91918E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1430×557 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @XJGB (2021-08-10 09:00 UTC)

<p>Hi Andras, unfortunately that didn’t work as easily as I was hoping.<br>
I get a couple of error messages which are not that easy to decioher to a newby to Slicer and Python…<br>
I am sure these are easy to fix once one has mastered the Slicer Coding structure … but this will take some time… maybe you could help me along with the first one?</p>
<p>Thanks!</p>
<pre><code class="lang-python">&gt;&gt;&gt; # get volume sequence as numpy array

&gt;&gt;&gt; volumeSequenceBrowserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForProxyNode(volumeSequenceProxyNode)

Traceback (most recent call last):

File "&lt;console&gt;", line 1, in &lt;module&gt;

AttributeError: 'vtkSlicerSequencesModuleLogicPython.vtkSlicerSeque' object has no attribute 'GetFirstBrowserNodeForProxyNode'
</code></pre>

---

## Post #11 by @lassoan (2021-08-10 16:14 UTC)

<p>Sorry, I forgot to mention that you need to use the latest Slicer Preview Release for this script.</p>

---

## Post #12 by @XJGB (2021-08-12 14:44 UTC)

<p>Thanks Andras for your help!<br>
Unfortunately there are still some errors… I’ll try and tackle them on the go, as I get the gist of the code…<br>
for now I will use version 4.10. as a workaround !</p>
<p>Thanks and greets<br>
Florian</p>

---

## Post #13 by @lassoan (2021-08-12 17:28 UTC)

<aside class="quote no-group" data-username="XJGB" data-post="12" data-topic="15508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xjgb/48/11830_2.png" class="avatar"> XJGB:</div>
<blockquote>
<p>Unfortunately there are still some errors… I’ll try and tackle them on the go, as I get the gist of the code…<br>
for now I will use version 4.10. as a workaround !</p>
</blockquote>
</aside>
<p>You don’t need to resort to using an ancient release, such as Slicer-4.10. You can copy-paste the error message here and we can tell you what’s wrong.</p>

---

## Post #14 by @XJGB (2021-08-13 08:51 UTC)

<p>Wow that’s really nice! Thanks!<br>
I am copying the code line by line into the python console<br>
the first error occurs in the Section:<br>
" # get volume sequence as numpy array</p>
<p>volumeSequenceBrowserNode = slicer.modules.sequences.logic().GetFirstBrowserNodeForProxyNode(volumeSequenceProxyNode)</p>
<p>volumeSequenceNode = volumeSequenceBrowserNode.GetSequenceNode(volumeSequenceProxyNode)"</p>
<p>"Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>AttributeError: ‘NoneType’ object has no attribute ‘GetSequenceNode’"</p>

---

## Post #15 by @lassoan (2021-08-13 13:01 UTC)

<p>You can need to load the 4D data set as “Volume sequence” and set <code>volumeSequenceProxyNode</code> to the volume node that displays the image that is changing in time.</p>

---

## Post #16 by @XJGB (2021-08-16 08:49 UTC)

<p>Thanks Andras ! Problem solved! Perfect!</p>

---
