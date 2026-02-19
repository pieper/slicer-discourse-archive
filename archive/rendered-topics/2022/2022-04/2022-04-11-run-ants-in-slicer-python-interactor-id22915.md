---
topic_id: 22915
title: "Run Ants In Slicer Python Interactor"
date: 2022-04-11
url: https://discourse.slicer.org/t/22915
---

# Run ANTs in Slicer Python Interactor

**Topic ID**: 22915
**Date**: 2022-04-11
**URL**: https://discourse.slicer.org/t/run-ants-in-slicer-python-interactor/22915

---

## Post #1 by @hotsen (2022-04-11 21:28 UTC)

<p><a class="mention" href="/u/simonoxen">@simonoxen</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Hi all,</p>
<p>I tried Ants extension in Slicer, the registration worked very good. However, I want to write a script and run ANTs from Slicer Python interactor. I am able to import antsRegistration, but can’t find a way to input all the parameters.</p>
<p>The following command generates syntax error. VolumeNodes fix, move, outTrans, outVolume can be defined and used successfully.<br>
antsRegistration --dimensionality 3 --use-histogram-matching 1 --winsorize-image-intensities [0.005,0.995] --float 0 --verbose 1 --interpolation LanczosWindowedSinc --output [outTrans,outVolume] --write-composite-transform 1 --collapse-output-transforms 1 --initial-moving-transform [fix,move,1] --transform Rigid[0.1] --metric MI[fix,move,0.25] --convergence [1000x500x250,1e-6,10] --smoothing-sigmas 3x2x1vox --shrink-factors 8x4x2</p>
<p>Thank you.</p>

---

## Post #2 by @simonoxen (2022-04-12 07:52 UTC)

<p>Hi, the logic from antsRegistration (scripted) module calls the antsRegistrationCLI module. You can run a registration and see in the log file how the command to antsRegistrationCLI is generated.</p>
<p>You could also mimic how the scripted module works from python. You can see a small test in the module to see how to do this.</p>

---

## Post #3 by @hotsen (2022-04-12 15:05 UTC)

<p>Hi Simon,</p>
<p>Thank you for your reply. The code I posted is actually copied from the log file of a successful registration, but when entered in Slicer python interactor it not works. The antsRegistrationCLI module you mentioned, did you mean slicer.cli.run(antsCommand (“parameters here”))? This is not working neither. Could you please provide an example code for testing? Really appreciate your help!</p>

---

## Post #4 by @simonoxen (2022-04-12 17:00 UTC)

<aside class="quote no-group" data-username="hotsen" data-post="3" data-topic="22915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ba9def/48.png" class="avatar"> hotsen:</div>
<blockquote>
<p>but when entered in Slicer python interactor it not works</p>
</blockquote>
</aside>
<p>how do you enter it?</p>
<aside class="quote no-group" data-username="hotsen" data-post="3" data-topic="22915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ba9def/48.png" class="avatar"> hotsen:</div>
<blockquote>
<p>did you mean slicer.cli.run(antsCommand (“parameters here”))?</p>
</blockquote>
</aside>
<p>no, see <a href="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L504" class="inline-onebox" rel="noopener nofollow ugc">SlicerANTs/antsRegistration/antsRegistration.py at master · netstim/SlicerANTs · GitHub</a> on how the CLI is run.</p>

---

## Post #5 by @hotsen (2022-04-13 17:20 UTC)

<p>Thank you for the GitHub example, I finally got it to work! Last question, when I run the CLI (antsRegistrationLogic().process()), is there a way to add this argument “wait_for_completion=True”?</p>
<p>I include two steps, ANTs registration and feature extraction in one function. I found that the extraction get no data because it starts before registration complete.</p>
<p>Thanks.</p>

---

## Post #6 by @simonoxen (2022-04-14 07:12 UTC)

<p>Right now, from <code>process()</code>, this is hardcoded. You can specify the CLI params and then run the CLI module with <code>wait_for_completion=True</code>.</p>

---

## Post #7 by @hotsen (2022-04-18 19:47 UTC)

<p>I couldn’t find any CLI params can change “wait_for_completion” status, looks like slicer.cli.run was implemented inside “antsRegistrationLogic().process()”, how could you control it from outside? I changed it to true in the source code and it worked fine, but I wish to find a better way so others can replicate the method. Thank you.</p>

---

## Post #8 by @simonoxen (2022-04-19 07:29 UTC)

<p>yes, as mentioned, this is hardcoded. You can run slicer.cli.run from python interactor, specifying the cli params.</p>

---

## Post #9 by @Vathsan (2022-06-18 20:50 UTC)

<p>Hi <a class="mention" href="/u/simonoxen">@simonoxen</a> and <a class="mention" href="/u/hotsen">@hotsen</a> ,</p>
<p>Could you please provide a sample code to run the registration from Python interactor? How do we pass the arguments to the process() function?</p>
<p>I am passing the following parameters,</p>
<pre><code class="lang-auto">sampleParams = {'stages': [{'transformParameters': {'transform': 'Rigid', 'settings': '0.1'}, 'metrics': [{'type': 'MI', 'fixed': '/media/srivathsan/Vol_011_20220119_144127_3D.nii.gz', 'moving': '/media/srivathsan/Vol_005_20220119_143403_3D.nii.gz', 'settings': '1,32,Regular,0.25'}], 'levels': {'steps': [{'convergence': 1000, 'smoothingSigmas': 4, 'shrinkFactors': 12}, {'convergence': 500, 'smoothingSigmas': 3, 'shrinkFactors': 8}, {'convergence': 250, 'smoothingSigmas': 2, 'shrinkFactors': 4}, {'convergence': 0, 'smoothingSigmas': 1, 'shrinkFactors': 2}], 'smoothingSigmasUnit': 'vox', 'convergenceThreshold': 6, 'convergenceWindowSize': 10}, 'masks': {'fixed': None, 'moving': None}}, {'transformParameters': {'transform': 'Affine', 'settings': '0.1'}, 'metrics': [{'type': 'MI', 'fixed': None, 'moving': None, 'settings': '1,32,Regular,0.25'}], 'levels': {'steps': [{'convergence': 1000, 'smoothingSigmas': 4, 'shrinkFactors': 12}, {'convergence': 500, 'smoothingSigmas': 3, 'shrinkFactors': 8}, {'convergence': 250, 'smoothingSigmas': 2, 'shrinkFactors': 4}, {'convergence': 0, 'smoothingSigmas': 1, 'shrinkFactors': 2}], 'smoothingSigmasUnit': 'vox', 'convergenceThreshold': 6, 'convergenceWindowSize': 10}, 'masks': {'fixed': None, 'moving': None}}, {'transformParameters': {'transform': 'SyN', 'settings': '0.1,3,0'}, 'metrics': [{'type': 'MI', 'fixed': None, 'moving': None, 'settings': '1,32'}], 'levels': {'steps': [{'convergence': 100, 'smoothingSigmas': 5, 'shrinkFactors': 10}, {'convergence': 100, 'smoothingSigmas': 3, 'shrinkFactors': 6}, {'convergence': 70, 'smoothingSigmas': 2, 'shrinkFactors': 4}, {'convergence': 50, 'smoothingSigmas': 1, 'shrinkFactors': 2}, {'convergence': 0, 'smoothingSigmas': 0, 'shrinkFactors': 1}], 'smoothingSigmasUnit': 'vox', 'convergenceThreshold': 6, 'convergenceWindowSize': 10}, 'masks': {'fixed': None, 'moving': None}}], 'outputSettings': {'transform': None, 'volume': '/media/srivathsan/antsCli/cliOutput.nii.gz', 'interpolation': 'Linear'}, 'initialTransformSettings': {'initializationFeature': 1}, 'generalSettings': {'dimensionality': 3, 'histogramMatching': 0, 'winsorizeImageIntensities': [0.005, 0.995], 'computationPrecision': 'float'}}

import antsRegistration
antsRegistration.antsRegistrationLogic().process(sampleParams)
</code></pre>
<p>But it generates the following error,</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: process() missing 1 required positional argument: 'outputSettings'
</code></pre>
<p>Thank you.</p>

---

## Post #10 by @Vathsan (2022-06-19 03:06 UTC)

<aside class="quote no-group" data-username="Vathsan" data-post="9" data-topic="22915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vathsan/48/15691_2.png" class="avatar"> Vathsan:</div>
<blockquote>
<pre><code class="lang-auto">import antsRegistration
antsRegistration.antsRegistrationLogic().process(sampleParams)
</code></pre>
</blockquote>
</aside>
<p>I was passing the wrong arguments. I tried to pass the arguments as in the GitHub example.</p>
<p><code>antsRegistration.antsRegistrationLogic().process([{'transformParameters': {'transform': 'Rigid', 'settings': '0.1'}, 'metrics': [{'type': 'MI', 'fixed': '/tmp/Slicer-srivathsan/vtkMRMLScalarVolumeNode1.nrrd', 'moving': '/tmp/Slicer-srivathsan/vtkMRMLScalarVolumeNode2.nrrd', 'settings': '1,32,Regular,0.25'}], 'levels': {'steps': [{'convergence': 1000, 'smoothingSigmas': 4, 'shrinkFactors': 12}, {'convergence': 500, 'smoothingSigmas': 3, 'shrinkFactors': 8}, {'convergence': 250, 'smoothingSigmas': 2, 'shrinkFactors': 4}, {'convergence': 0, 'smoothingSigmas': 1, 'shrinkFactors': 2}], 'smoothingSigmasUnit': 'vox', 'convergenceThreshold': 6, 'convergenceWindowSize': 10}, 'masks': {'fixed': None, 'moving': None}}, {'transformParameters': {'transform': 'Affine', 'settings': '0.1'}, 'metrics': [{'type': 'MI', 'fixed': None, 'moving': None, 'settings': '1,32,Regular,0.25'}], 'levels': {'steps': [{'convergence': 1000, 'smoothingSigmas': 4, 'shrinkFactors': 12}, {'convergence': 500, 'smoothingSigmas': 3, 'shrinkFactors': 8}, {'convergence': 250, 'smoothingSigmas': 2, 'shrinkFactors': 4}, {'convergence': 0, 'smoothingSigmas': 1, 'shrinkFactors': 2}], 'smoothingSigmasUnit': 'vox', 'convergenceThreshold': 6, 'convergenceWindowSize': 10}, 'masks': {'fixed': None, 'moving': None}}, {'transformParameters': {'transform': 'SyN', 'settings': '0.1,3,0'}, 'metrics': [{'type': 'MI', 'fixed': None, 'moving': None, 'settings': '1,32'}], 'levels': {'steps': [{'convergence': 100, 'smoothingSigmas': 5, 'shrinkFactors': 10}, {'convergence': 100, 'smoothingSigmas': 3, 'shrinkFactors': 6}, {'convergence': 70, 'smoothingSigmas': 2, 'shrinkFactors': 4}, {'convergence': 50, 'smoothingSigmas': 1, 'shrinkFactors': 2}, {'convergence': 0, 'smoothingSigmas': 0, 'shrinkFactors': 1}], 'smoothingSigmasUnit': 'vox', 'convergenceThreshold': 6, 'convergenceWindowSize': 10}, 'masks': {'fixed': None, 'moving': None}}], {'transform': None, 'volume': '/tmp/Slicer-srivathsan/BFCDJ_vtkMRMLScalarVolumeNode3.nrrd', 'interpolation': 'Linear'}, {'initializationFeature': 1}, {'dimensionality': 3, 'histogramMatching': 0, 'winsorizeImageIntensities': [0.005, 0.995], 'computationPrecision': 'float'})</code></p>
<p>Though it fixed the previous issue, now I get the following error,<br>
Traceback (most recent call last):</p>
<pre><code class="lang-auto">  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/srivathsan/Slicer-4.13.0-2022-04-17-linux-amd64/NA-MIC/Extensions-30785/SlicerANTs/lib/Slicer-4.13/qt-scripted-modules/antsRegistration.py", line 517, in process
    self.getOrSetCLIParam(stages[0]['metrics'][0]['fixed']) # put in first position. will be used as reference in cli
  File "/home/srivathsan/Slicer-4.13.0-2022-04-17-linux-amd64/NA-MIC/Extensions-30785/SlicerANTs/lib/Slicer-4.13/qt-scripted-modules/antsRegistration.py", line 599, in getOrSetCLIParam
    nodeID = mrmlNode.GetID()
AttributeError: 'str' object has no attribute 'GetID'
</code></pre>
<p>Appreciate any help on this.</p>

---

## Post #11 by @lassoan (2022-06-23 17:41 UTC)

<p>You need to provide a node object (you provided a filename). You can load a volume and get the node object using <code>slicer.util.loadVolume</code>.</p>

---

## Post #12 by @hotsen (2022-07-20 16:39 UTC)

<p>Hi Vathsan,<br>
Sorry for the late reply. Just call<br>
antsRegistration.antsRegistrationLogic().process(stages=stages, outputSettings=outputSettings, initialTransformSettings=initialTransformSettings, generalSettings=generalSettings)<br>
and feed all your settings.<br>
For example,<br>
generalSettings = {<br>
‘dimensionality’ : 3,<br>
‘histogramMatching’ : True,<br>
‘winsorizeImageIntensities’ : [0.005,0.995],<br>
‘computationPrecision’ : ‘double’<br>
}</p>
<p>I think the error you got is because you pass a string instead of slicer volume node. Try to create one using Volume = slicer.vtkMRMLScalarVolumeNode() or get an existing one using Volume = slicer.util.getNode(“NodeNameHere”).</p>
<p>Hope this helps.</p>
<p>Hotsen</p>

---

## Post #13 by @Fabien_Rech (2023-03-11 15:47 UTC)

<p>Hi,</p>
<p>Like hotsen, I tried to perform a two steps script, with ANTS registration and then other functions but it is necessary to use “wait_for_completion = True” otherwise the two processes are performed simultaneously.</p>
<p>However I do not understand how the CLI is working. I have no problem to pass the parameters for the antsRegistration.antsRegistrationLogic().process (by using the preset parameters of the github repository and changing the corresponding volume) but I have some problems with the slicer.cli.run function, I don’t understand how to launch it via the python interpreter with the same preset as in the slicerANTs github repository.</p>
<p>Could someone provide an example with the slicer.cli.run function ?</p>
<p>Thank you</p>
<p>Fabien</p>

---

## Post #14 by @lassoan (2023-03-11 16:28 UTC)

<p>I would recommend to modify the module logic to accept an optional <code>wait_for_completion</code> argument here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L502">
  <header class="source">

      <a href="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L502" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L502" target="_blank" rel="noopener">netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L502</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="492" style="counter-reset: li-counter 491 ;">
          <li>    parameterNode.SetParameter("HistogramMatching", str(presetParameters["generalSettings"]["histogramMatching"]))</li>
          <li>  if not parameterNode.GetParameter("WinsorizeImageIntensities"):</li>
          <li>    parameterNode.SetParameter("WinsorizeImageIntensities", ",".join([str(x) for x in presetParameters["generalSettings"]["winsorizeImageIntensities"]]))</li>
          <li>  if not parameterNode.GetParameter("ComputationPrecision"):</li>
          <li>    parameterNode.SetParameter("ComputationPrecision", presetParameters["generalSettings"]["computationPrecision"])</li>
          <li>
          </li>
<li>def cancelRegistration(self):</li>
          <li>  if self._cliNode:</li>
          <li>    self._cliNode.Cancel()</li>
          <li>
          </li>
<li class="selected">def process(self, stages, outputSettings, initialTransformSettings=None, generalSettings=None):</li>
          <li>  """</li>
          <li>  :param stages: list defining registration stages</li>
          <li>  :param outputSettings: dictionary defining output settings</li>
          <li>  :param initialTransformSettings: dictionary defining initial moving transform</li>
          <li>  :param generalSettings: dictionary defining general registration settings</li>
          <li>  See presets examples to see how these are specified</li>
          <li>  """</li>
          <li>
          </li>
<li>  if generalSettings is None:</li>
          <li>    generalSettings = {}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You could then replace the hardcoded <code> wait_for_completion=False</code> setting here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L530">
  <header class="source">

      <a href="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L530" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L530" target="_blank" rel="noopener">netstim/SlicerANTs/blob/master/antsRegistration/antsRegistration.py#L530</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="520" style="counter-reset: li-counter 519 ;">
          <li>  self._cliParams["antsCommand"] = self.getAntsRegistrationCommand(stages, outputSettings, initialTransformSettings, generalSettings)</li>
          <li>
          </li>
<li>  if outputSettings["transform"] is not None:</li>
          <li>    if ("useDisplacementField" in outputSettings) and outputSettings["useDisplacementField"]:</li>
          <li>      self._cliParams["outputDisplacementField"] = outputSettings["transform"]</li>
          <li>    else:</li>
          <li>      self._cliParams["outputCompositeTransform"] = outputSettings["transform"]</li>
          <li>  </li>
          <li>  self._cliParams["useFloat"] = (generalSettings["computationPrecision"]  == "float")</li>
          <li>
          </li>
<li class="selected">  self._cliNode = slicer.cli.run(slicer.modules.antsregistrationcli, None, self._cliParams, wait_for_completion=False, update_display=False)</li>
          <li>
          </li>
<li>def getAntsRegistrationCommand(self, stages, outputSettings, initialTransformSettings=None, generalSettings=None):</li>
          <li>  if generalSettings is None:</li>
          <li>    generalSettings = {}</li>
          <li>  if initialTransformSettings is None:</li>
          <li>    initialTransformSettings = {}</li>
          <li>  antsCommand = self.getGeneralSettingsCommand(**generalSettings)</li>
          <li>  antsCommand = antsCommand + self.getOutputCommand(interpolation=outputSettings['interpolation'], volume=outputSettings['volume'])</li>
          <li>  antsCommand = antsCommand + self.getInitialMovingTransformCommand(**initialTransformSettings)</li>
          <li>  for stage in stages:</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If it all works well for you on your computer then you can submit a pull request to the SlicerANTs repository.</p>

---

## Post #15 by @Fabien_Rech (2023-03-11 23:06 UTC)

<p>Thank you very much Andras,</p>
<p>I have tried first to replace False by True in line 530 and it worked perfectly.</p>
<p>I will try later to modify the module logic to set it as optional.</p>
<p>Best regards</p>
<p>Fabien</p>

---
