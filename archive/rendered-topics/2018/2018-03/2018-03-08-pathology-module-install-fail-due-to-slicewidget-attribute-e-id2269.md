---
topic_id: 2269
title: "Pathology Module Install Fail Due To Slicewidget Attribute E"
date: 2018-03-08
url: https://discourse.slicer.org/t/2269
---

# Pathology module install fail due to sliceWidget attribute error

**Topic ID**: 2269
**Date**: 2018-03-08
**URL**: https://discourse.slicer.org/t/pathology-module-install-fail-due-to-slicewidget-attribute-error/2269

---

## Post #1 by @Alvin_Chen (2018-03-08 15:25 UTC)

<p>hello,</p>
<p>[environment]<br>
MacOS 10.13.3 /Ubuntu 16.04 /Win10 have same behavior<br>
Slicer 4.8.1</p>
<p>[Description]<br>
when I install pathology module by Extension Manager, after restart slicer<br>
I will get the following error message in Python Interactor, and there is no Pathology option in module list</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/Extensions-26813/SlicerPathology/lib/Slicer-4.8/qt-scripted-modules/SlicerPathology.py”, line 749, in <br>
red_logic = slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic()<br>
AttributeError: ‘NoneType’ object has no attribute ‘sliceWidget’</p>
<p>[btw]</p>
<ol>
<li>if I input the following code in Python Interactor, there is no error message<br>
red_logic = slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic()</li>
<li>if i modify SlicerPathology.py", line 749 as<br>
lm  = slicer.app.layoutManager()                           ==&gt; no error message<br>
red_logic = lm.sliceWidget(“Red”).sliceLogic()     ==&gt; fail in this line</li>
</ol>
<p>Alvin</p>

---

## Post #2 by @pieper (2018-03-08 15:44 UTC)

<p>It looks like that module is doing things at the global level (during module discovery) that should really not happen until the application has finished start up.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SBU-BMI/SlicerPathology/blob/master/SlicerPathology/SlicerPathology.py#L749-L783" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SBU-BMI/SlicerPathology/blob/master/SlicerPathology/SlicerPathology.py#L749-L783" target="_blank" rel="nofollow noopener">SBU-BMI/SlicerPathology/blob/master/SlicerPathology/SlicerPathology.py#L749-L783</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="749" style="counter-reset: li-counter 748 ;">
<li>red_logic = slicer.app.layoutManager().sliceWidget("Red").sliceLogic()</li>
<li>red_cn = red_logic.GetSliceCompositeNode()</li>
<li>
</li>
<li>fgrdVolID = red_cn.GetBackgroundVolumeID()</li>
<li>fgrdNode = slicer.util.getNode(fgrdVolID)</li>
<li>fgrdNode.SetSpacing(1.0, 1.0, 1.0)</li>
<li>r = slicer.app.layoutManager().sliceWidget("Red").sliceController()</li>
<li>r.fitSliceToBackground()</li>
<li>
</li>
<li>fMat = vtk.vtkMatrix4x4()</li>
<li>fgrdNode.GetIJKToRASDirectionMatrix(fMat)</li>
<li>bgrdName = fgrdNode.GetName() + '_gray'</li>
<li>self.tilename = fgrdNode.GetName() + '_gray'</li>
<li>self.parameterNode.SetParameter("SlicerPathology,tilename", self.tilename)</li>
<li>
</li>
<li># Create dummy grayscale image</li>
<li>magnitude = vtk.vtkImageMagnitude()</li>
<li>magnitude.SetInputData(fgrdNode.GetImageData())</li>
<li>magnitude.Update()</li>
<li>bgrdNode = slicer.vtkMRMLScalarVolumeNode()</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/SBU-BMI/SlicerPathology/blob/master/SlicerPathology/SlicerPathology.py#L749-L783" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>That code should be wrapped in a function and connected to a signal like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L70-L71" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L70-L71" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L70-L71</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="70" style="counter-reset: li-counter 69 ;">
<li># Tasks to execute after the application has started up</li>
<li>slicer.app.connect("startupCompleted()", self.performPostModuleDiscoveryTasks)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/alvin_chen">@Alvin_Chen</a> can you give that a try?</p>

---

## Post #3 by @Alvin_Chen (2018-03-08 17:10 UTC)

<p>hi Steve<br>
i am not sure my modification is corrected or not.<br>
in SlicerPathology.py, i add a similar code to end of SlicerPathology class, but it is not work<br>
i got same error message.<br>
btw, in my previous experiment 1)<br>
if I input the following single-line code in Python Interactor, there is no error message</p>
<pre><code class="lang-auto">red_logic = slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic()
</code></pre>
<p>since all platform have same behavior, could you reproduce this case?</p>
<pre><code class="lang-auto">  29 class SlicerPathology(ScriptedLoadableModule):
  30     def __init__(self, parent):
  31         ScriptedLoadableModule.__init__(self, parent)
  32         self.parent.title = "Slicer Pathology"
  33         self.parent.categories = ["Pathology"]
  34         self.parent.dependencies = []
  35         self.parent.contributors = ["Erich Bremer, Joel Saltz, Yi Gao, Tammy DiPrima (Stony Brook University)"]
  36         self.parent.helpText = """
  37     Automatic and semi-automatic pathology segmentation tools.
  38     """
  39         self.parent.acknowledgementText = """
  40     This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
  41     and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
  42     """  # replace with organization, grant and thanks.
  43         slicer.app.connect("startupCompleted()", self.SlicerPathologyWidget) &lt;-- this line
</code></pre>

---

## Post #4 by @pieper (2018-03-08 18:04 UTC)

<p>Actually it looks like that code was added by mistake - you should just delete <a href="https://github.com/SBU-BMI/SlicerPathology/blame/master/SlicerPathology/SlicerPathology.py#L749-L783">those lines</a> and see if the if you are able to use the rest of the module as expected.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> do you know the status?</p>

---

## Post #5 by @fedorov (2018-03-08 20:02 UTC)

<p>I don’t. SBU team maintains this module. <a class="mention" href="/u/tdiprima">@tdiprima</a> can you comment?</p>

---

## Post #6 by @pieper (2018-03-08 20:27 UTC)

<p>I filed an issue for reference <a href="https://github.com/SBU-BMI/SlicerPathology/issues/100">https://github.com/SBU-BMI/SlicerPathology/issues/100</a></p>

---

## Post #7 by @Alvin_Chen (2018-03-09 02:37 UTC)

<p>hi Steve</p>
<p>thanks for your information<br>
in my ubuntu 16.04 platform<br>
Pathology module work after this following two steps</p>
<ol>
<li>remove line 749-783 (all non-subroutine code) in SlicerPathology.py</li>
<li>fix the following subroutine’s indent error in SlicerPathology.py
<ul>
<li>Four2ThreeChannel</li>
<li>loadTCGAData</li>
<li>clear_and_open</li>
<li>loademup</li>
</ul>
</li>
</ol>
<p>Alvin</p>

---

## Post #8 by @pieper (2018-03-09 13:52 UTC)

<p>Great thanks for reporting <a class="mention" href="/u/alvin_chen">@Alvin_Chen</a>.  You might consider making a pull request with the fixes to the <a href="https://github.com/SBU-BMI/SlicerPathology">SlicerPathology repository</a>.</p>

---

## Post #9 by @ebremer (2018-05-03 03:07 UTC)

<p>Thanks Alvin for reporting this!  We’ll take a look at this and get it fixed.   - Erich</p>

---

## Post #10 by @fedorov (2018-05-24 22:17 UTC)

<p>To follow up on this issue, <a class="mention" href="/u/ebremer">@ebremer</a> committed a fix that should resolve the problem in the next nightly. Please report if you have troubles with the extension.</p>

---

## Post #11 by @PaoloZaffino (2018-10-04 12:25 UTC)

<p>Hi all,<br>
I’m trying to find the Pathology module into the extension manager (Linux nightly build) but it looks like it’s missing.<br>
Any idea?</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Paolo</p>

---

## Post #12 by @fedorov (2018-10-04 13:52 UTC)

<p><a class="mention" href="/u/ebremer">@ebremer</a> it appears that SlicerPathology build is currently failing for all operating systems on the dashboard: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerPathology">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerPathology</a>.</p>

---

## Post #13 by @PaoloZaffino (2019-01-16 15:42 UTC)

<p>Hi all,<br>
any news about this module?</p>
<p>Thank you very much!</p>

---

## Post #14 by @fedorov (2019-01-16 16:28 UTC)

<p>I’ve just emailed directly the developers and the PI of the project, will let you know if/when they respond, and whether we get any clarity on the status of support for this extension.</p>

---

## Post #15 by @PaoloZaffino (2019-01-16 22:19 UTC)

<p>Thank you very much <a class="mention" href="/u/fedorov">@fedorov</a> !</p>

---

## Post #16 by @fedorov (2019-01-17 19:24 UTC)

<p>Here’s the response I received from Joel Saltz, who is the PI of the effort:</p>
<blockquote>
<p>Yes, we will be maintaining the extension and we are also plan a new version that leverages software components that we’ve developed over the past couple of years  as part of our QuIP U24. Erich will get the current version back up and running very soon.</p>
</blockquote>
<p>Hopefully <a class="mention" href="/u/ebremer">@ebremer</a> will get back to this sometime soon.</p>

---

## Post #17 by @PaoloZaffino (2019-01-17 22:27 UTC)

<p>Great news!<br>
Thank you again.</p>
<p>Paolo</p>

---
