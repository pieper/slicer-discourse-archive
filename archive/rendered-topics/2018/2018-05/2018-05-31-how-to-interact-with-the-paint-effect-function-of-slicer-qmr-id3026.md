---
topic_id: 3026
title: "How To Interact With The Paint Effect Function Of Slicer Qmr"
date: 2018-05-31
url: https://discourse.slicer.org/t/3026
---

# How to interact with the 'Paint' effect function of slicer.qMRMLSegmentEditorWidget instance

**Topic ID**: 3026
**Date**: 2018-05-31
**URL**: https://discourse.slicer.org/t/how-to-interact-with-the-paint-effect-function-of-slicer-qmrmlsegmenteditorwidget-instance/3026

---

## Post #1 by @Boyce_Doyle (2018-05-31 10:02 UTC)

<p>Happy Children’s Day.<br>
In fact, there are three problems.<br>
At first, my develop environment lists below.<br>
os:ubuntu 16.04.3<br>
slicer:latest stable version 4.8.1<br>
lauguage:python 3.6.4<br>
1.<br>
I met a demand of programming a script to get a roi from someone not familiar with the slicer.<br>
A clear guide for all processes is needed.<br>
I have a segmentation procedure.I got the plan as follows:<br>
step1:<br>
using the Paint effect to get a ROI.<br>
step2:<br>
using the ‘Threshold’ effect to generate the segmentation.<br>
I have tried using the markups while the coordinate is the ‘world’ not the index for array-computing.<br>
It didn’t work well.</p>
<ol start="2">
<li>
</li>
</ol>
<p>I’m not good enough in c++ programming.And when I use python scripts as follows:</p>
<pre><code>    exec_outside = ['python', '/home/cyan/PycharmProjects/adc/compute_model.py', str(flair_path)]
    subprocess_status = check_output(exec_outside, shell=True, env=slicer.util.startupEnvironment())
</code></pre>
<p>the slicer become black and won’t wake up anymore.<br>
2mins later ,I use htop command and find the cou is free.slicer is not on working.<br>
the python script can work well using the same command in the bash shell within 5secs.<br>
How could I use the subprocess module?</p>
<ol start="3">
<li>
</li>
</ol>
<p>when I try my own algorithm for computing the adc using dwi data<br>
# adc = np.ones(dwi_200.shape)<br>
# adc[(dwi_200 &lt; noise_threshold) | (dwi_2000 &lt; noise_threshold)] = 0<br>
# effective = adc==1<br>
# ineffective = adc==0<br>
# dwi_2000[ineffective] = 1<br>
# dwi_200[ineffective] = 1<br>
# adc[effective] = np.log(dwi_200[effective] / dwi_2000[effective]) / 1800<br>
the slicer python-interface gives me a runtimeerror said divide 0<br>
while this script can work well in my own python 3.6.4 env within 1 sec.<br>
I’m confused how slicer using the cpu.</p>
<p>And final, I have no idea how to add a model in the right position on a mrml scene.<br>
That to say , when I generate model using out-slicer computation(I can get the spacing,origin and the 3*3 matrix direction params using simpleITK),How can I transform the model in a loaded and mastered slicer mrmlscene?<br>
Sincerely,<br>
waiting for your reply.</p>

---

## Post #2 by @pieper (2018-05-31 15:00 UTC)

<p>Hi -</p>
<p>What you are trying to do sounds very achievable, but not quite trivial so you’ll want to take a step-by-step approach.  There shouldn’t be any need to use an external python subprocess.</p>
<p>I would suggest you start by using the Extension Wizard to make a skeleton for your process and then incrementally add functionality confirming your assumptions at each step.  You can follow the tutorial linked below to get started.  Ideally you should put the code in a github repository with each step as a commit.  As you run into specific questions at each step you can send a pointer to the code that worked and a commit that didn’t work as you expected and then we can give specific advice about how to accomplish that step.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer</a></p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @Boyce_Doyle (2018-06-05 02:43 UTC)

<p>Thank you for your enthusiastic suggestions.I have tried as you list.And the first barrier is that I can’t programmatically control the interactions to draw a arbitrary shape as segmentaiton-editor’s effect ‘Draw’ does.<br>
I have tried to clean out the other toggles on the editor with ‘Draw’ the only left.But I failed.The widget is written by C++ I can’t access it easily.Can you help me with showing a python-scripts way.</p>

---

## Post #4 by @lassoan (2018-06-05 03:57 UTC)

<p>The <a href="http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html">segment editor widget</a> is highly customizable by Python scripting. To show selected effects only, call <code>setEffectNameOrder</code> with the names of the effects that you would like to show and then set <code>unorderedEffectsVisible</code> to False.</p>

---
