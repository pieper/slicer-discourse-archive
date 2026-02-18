# Perk Tutor - Return more than one value in custom metric function

**Topic ID**: 9137
**Date**: 2019-11-13
**URL**: https://discourse.slicer.org/t/perk-tutor-return-more-than-one-value-in-custom-metric-function/9137

---

## Post #1 by @Prashant_Pandey (2019-11-13 22:55 UTC)

<p>I’ve written a simple metric for Perk Tutor (see code below) to analyze the deviation between the tool and an entry point. Instead of returning the final RMS deviation, I also want to return the R, A, S components of the error. How would I do this? I tried returning multipel values in GetMetric(), but this isn’t allowed.</p>
<pre><code>import math
import vtk
from PythonMetricsCalculator import PerkEvaluatorMetric

class EntryDeviation( PerkEvaluatorMetric ):


  # Static methods
  @staticmethod
  def GetMetricName():
    return "Entry Deviation"
  
  @staticmethod  
  def GetMetricUnit():
    return "mm"
  
  @staticmethod
  def GetTransformRoles():
    return [ "Needle" ]
  
  @staticmethod
  def GetAnatomyRoles():
    return { "Targets": "vtkMRMLMarkupsFiducialNode" }
    
    
  # Instance methods    
  def __init__( self ):
    PerkEvaluatorMetric.__init__( self )
    self.R_deviation = []
    self.A_deviation = []
    self.S_deviation = []
    self.needleTipTargetDistance = []

    
  def SetAnatomy( self, role, node ):   
    if ( role == "Targets" ):
      self.targets = node  
      return True
      
    return False

    
  def AddTimestamp( self, time, matrix, point, role ):  
    currTargetPosition = [ 0, 0, 0 ]
    self.targets.GetNthFiducialPosition(0, currTargetPosition ) #Assume first fid point is the entry point
    currTargetPosition_RAS = [ currTargetPosition[ 0 ], currTargetPosition[ 1 ], currTargetPosition[ 2 ] ]
    
    # Find the needle tip in RAS
    needleTip_RAS = point[0:3]
    
    self.R_deviation.append(currTargetPosition[0] - needleTip_RAS[0])
    self.A_deviation.append(currTargetPosition[1] - needleTip_RAS[1])
    self.S_deviation.append(currTargetPosition[2] - needleTip_RAS[2])

    self.needleTipTargetDistance.append(math.sqrt( vtk.vtkMath.Distance2BetweenPoints( currTargetPosition_RAS, needleTip_RAS ) ))
    
    
  def GetMetric( self ):
    return self.needleTipTargetDistance[-1]</code></pre>

---

## Post #2 by @mholden8 (2019-11-14 03:53 UTC)

<p>Typically what we do is return a tab delimited string with all the values. See, for example, here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/PerkTutor/PythonMetrics/blob/master/BoundingBoxExtent.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/PerkTutor/PythonMetrics/blob/master/BoundingBoxExtent.py" target="_blank" rel="nofollow noopener">PerkTutor/PythonMetrics/blob/master/BoundingBoxExtent.py</a></h4>
<pre><code class="lang-py">from PythonMetricsCalculator import PerkEvaluatorMetric

class BoundingBoxExtent( PerkEvaluatorMetric ):

  # Static methods
  @staticmethod
  def GetMetricName():
    return "Bounding Box Extent"
  
  @staticmethod  
  def GetMetricUnit():
    return "mm"
    
    
  # Instance methods  
  def __init__( self ):
    PerkEvaluatorMetric.__init__( self )
    
    self.minX = None
    self.minY = None
</code></pre>

  This file has been truncated. <a href="https://github.com/PerkTutor/PythonMetrics/blob/master/BoundingBoxExtent.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This makes it easy to copy or load the table of metrics into Excel/Sheets/SPSS/etc. for statistical analysis.</p>
<p>If you let us know what you would like to do with the metric values after you have computed them, I may be able to suggest a better solution.</p>

---

## Post #3 by @Prashant_Pandey (2019-11-14 04:51 UTC)

<p>Thanks, that will work for me.</p>
<p>I was also wondering how can I log and save the metric values at each sequence frame, instead of getting summary values only at the end of the sequence?</p>

---

## Post #4 by @mholden8 (2019-11-14 15:23 UTC)

<p>By default, metric values at each frame are not logged. But you could add a few lines at the end of your AddTimestamp function to write the current metric value to file.</p>
<p>For example, adding something like this line at the end of the AddTimestamp function could work:</p>
<pre><code class="lang-auto">with open("my_filename.txt", "a") as myfile:
    myfile.write(str(self.GetMetric()))
</code></pre>
<p>But usually I would suggest to do all your computations from within the metric, so you don’t have to do log the values at each frame. What is your particular use case for this? If you let us know, I may be able to suggest a better solution.</p>

---

## Post #5 by @Prashant_Pandey (2019-11-14 21:00 UTC)

<p>I want to get the trajectory of the tracked tool with respect to the target fiducial / annotation ruler. This is why I want time stamped R, A, S coordinates - having this information can let me calculate most other metrics without having to write new metrics in perk tutor.</p>
<p>The trace and visualize trajectory metrics help with visualization, but they don’t provide an easy way to access the trajectory points.</p>

---

## Post #6 by @Prashant_Pandey (2019-11-15 01:14 UTC)

<p><a class="mention" href="/u/mholden8">@mholden8</a> Another issue I’m having is that I can’t seem to import modules other than math and vtk in my metric file.<br>
For example I tried ‘import time’ and ‘from datetime import datetime’ so that I could add date-time to my filenames following on from your previous suggestion. But if I do this the metric does not work.</p>

---

## Post #7 by @mholden8 (2019-11-15 03:34 UTC)

<p>You should be able to import modules into your metrics just like you would into any other Python script. I tried importing the modules you mentioned into a metric, and it worked for me. When you say “the metric does not work”, what is the error message you get in the log or Python console? If you also send along the latest version of your metric, I can have a look to see what the issue might be.</p>
<p>May I ask why you do not want to write other metrics in Perk Tutor? Is there a way we could make writing metrics in Perk Tutor easier?</p>

---

## Post #8 by @Prashant_Pandey (2019-11-15 04:56 UTC)

<p>That’s strange. Here is my metric file that I’m having import issues with: <a href="https://gist.github.com/prash-p/d360ea06ef6de8cd7e086516eb4cec5d" class="inline-onebox" rel="noopener nofollow ugc">Entry Deviation Perk Tutor Metric · GitHub</a></p>
<p>If I comment out the import datetime line (and change line 35), the metric runs fine. If I leave the import in, I can add the metric to Slicer but it does not load the ‘Anatomy’ node selector box properly. Furthermore if I run the analysis, the metric does not return any values. No errors get thrown.</p>
<p>Here is another metric I’m having issue with, but can’t understand why: <a href="https://gist.github.com/prash-p/8fb131406b592a5a77185a7d55133da2" class="inline-onebox" rel="noopener nofollow ugc">Trajectory Deviation Perk Tutor metric · GitHub</a><br>
For this I get the error that the AddTimestamp() method expects 5 inputs but only 4 were given. I couldn’t figure it out. The metric doesn’t run at all.</p>
<aside class="quote no-group" data-username="mholden8" data-post="7" data-topic="9137">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mholden8/48/1112_2.png" class="avatar"> mholden8:</div>
<blockquote>
<p>May I ask why you do not want to write other metrics in Perk Tutor? Is there a way we could make writing metrics in Perk Tutor easier?</p>
</blockquote>
</aside>
<p>The reason is because I want to analyse the metrics over time - for example I want velocity per sequence frame, displacement per frame, accuracy per frame. In my application, it is more useful to have a detaile analysis of the tool trajectory over time rather than a summary metric at the end - and from my understanding it’s not possible to do that (unless you output all your data as one string)?</p>
<p>If the solution to that is to write to a .txt or .csv file from the Perk Tutor metric, then I’d rather do it only once from perk tutor and derive the other metrics from the log file.</p>
<p>Thanks for taking the time to help!</p>

---

## Post #9 by @Prashant_Pandey (2019-11-15 04:59 UTC)

<p>Forgot to mention I’m on Windows 10, Slicer 4.10.2</p>

---

## Post #10 by @mholden8 (2019-11-18 16:15 UTC)

<p>I had a look, and it seems like it was a Python 2 vs Python 3 issue. I’ve pushed a fix to Perk Tutor so that <code>import</code> statements will work in Slicer 4.10.2 with Python 2. It should be available in Slicer 4.10.2 the next time extensions are built for it. Until then, it is already working in the latest nightly.</p>
<p>The issue with your second metric is on line 52:</p>
<pre><code class="lang-auto">File "&lt;string&gt;", line 52, in AddTimestamp
TypeError: unsupported operand type(s) for -: 'list' and 'list'
</code></pre>
<p>I will work on a fix to make the error messages more useful…</p>

---

## Post #11 by @Prashant_Pandey (2019-11-18 19:30 UTC)

<p>Thanks! Somehow missed that error message.</p>

---

## Post #12 by @Prashant_Pandey (2019-11-28 21:56 UTC)

<p>Confirmed that Perk Tutor is working with imports now in Slicer 4.10.2</p>
<p>Thanks for your help!</p>

---

## Post #13 by @Prashant_Pandey (2019-11-28 23:19 UTC)

<p><a class="mention" href="/u/mholden8">@mholden8</a> Is there a way to make the ‘Start/Stop’ button within the Transform Recorder module into a shortcut or something that could be accessibe by a footswitch for example?</p>

---

## Post #14 by @lassoan (2019-11-28 23:56 UTC)

<p>You can define keyboard shortcuts for any function as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_keyboard_shortcuts">here</a>.</p>

---

## Post #15 by @Prashant_Pandey (2020-02-04 23:12 UTC)

<p><a class="mention" href="/u/mholden8">@mholden8</a> Is there a way to access the Sequence Browser node that the metrics are being calculated on, from the PerkEvaluatorClass? I would like to get the name of that node</p>

---

## Post #16 by @mholden8 (2020-02-05 02:34 UTC)

<p>Yes, given the Perk Evaluator node, you can get the Sequence Browser node using the function:</p>
<pre><code class="lang-auto">perkEvaluatorNode.GetTrackedSequenceBrowserNode()
</code></pre>
<p>It is defined here: <a href="https://github.com/PerkTutor/PerkTutor/blob/master/PerkEvaluator/MRML/vtkMRMLPerkEvaluatorNode.h#L122" rel="nofollow noopener">https://github.com/PerkTutor/PerkTutor/blob/master/PerkEvaluator/MRML/vtkMRMLPerkEvaluatorNode.h#L122</a>.</p>

---

## Post #17 by @Prashant_Pandey (2020-02-05 03:46 UTC)

<p>Amazing, thank you!!</p>

---
