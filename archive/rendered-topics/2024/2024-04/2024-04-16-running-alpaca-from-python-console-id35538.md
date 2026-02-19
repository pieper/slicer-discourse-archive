---
topic_id: 35538
title: "Running Alpaca From Python Console"
date: 2024-04-16
url: https://discourse.slicer.org/t/35538
---

# Running ALPACA from Python Console

**Topic ID**: 35538
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/running-alpaca-from-python-console/35538

---

## Post #1 by @evaherbst (2024-04-16 16:39 UTC)

<p>Hello, I am trying to run ALPACA from the Python console.</p>
<p>I am accessing the logic with:</p>
<blockquote>
<p>import ALPACA<br>
AlpacaLogic = ALPACA.ALPACALogic()<br>
Then I define my paths and directories as inputs for ALPACA batch mode.<br>
I set skipScaling to False</p>
</blockquote>
<p>When I try to run:<br>
AlpacaLogic.process(sourceModelPath, sourceLandmarkPath, targetModelDirectory, outputDirectory, skipScaling)</p>
<p>i get the error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 10, in <br>
File “C:/Users/eherbst/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 3085, in process<br>
“InputVolume”: inputVolume.GetID(),<br>
AttributeError: ‘str’ object has no attribute ‘GetID’</p>
</blockquote>
<p>I see in the ALPACA.py code that running Alpaca also requires the ProjectionFactor and Parameters, but if I do not define them as inputs, does it just use the defaults?</p>
<p>hank you,<br>
Eva</p>

---

## Post #2 by @smrolfe (2024-04-16 22:21 UTC)

<p>AlpacaLogic.process is a test utility and doesn’t run the method from the command line. The batch mode tab of the module is intended to handle bundled jobs, maybe if you could describe your use case for running this from the command line I can help find a solution?</p>

---

## Post #3 by @chz31 (2024-04-17 02:25 UTC)

<p>I agree with Sara that the best way is probably just to run the batch mode in the UI.</p>
<p>If you want to run the batch mode in Python, you can use the function <code>runLandmarkMultiprocess()</code> in the <code>ALPACALogic</code>. There is a parameter <code>self.parameterDictionary</code> that would have all the required parameters. So far, the default parameters work for most of my cases.You can also check the function <code>onApplyLandmarkMulti()</code> to see how the batch mode runs using the <code>runLandmarkMultiprocess</code> function.</p>

---

## Post #4 by @evaherbst (2024-04-17 07:16 UTC)

<p>Thank you Sara and Chi!</p>
<p>My use case is that I process a lot of scans (segmentation → landmark transfer via Alpaca → cropping based on landmarks) and since the segmentation and cropping is automated, it would be nice to also automate the Alpaca step to run everything together without manual input.</p>
<p>I will try the runLandmarkMultiprocess function.</p>
<p>Thanks again!<br>
Eva</p>

---

## Post #5 by @evaherbst (2024-04-19 16:42 UTC)

<p>Hi all,</p>
<p>Thanks for your help!<br>
I got it working with the following function:</p>
<blockquote>
<p>def runAlpaca(scapulaModelOutputDir, sourceModelPath, sourceLandmarkPath, landmarkOutputDirectory):<br>
import ALPACA<br>
AlpacaLogic = ALPACA.ALPACALogic()<br>
targetModelDirectory = scapulaModelOutputDir<br>
scalingOption= True<br>
projectionFactor = 0.01<br>
useJSONFormat = True<br>
parameters = { <span class="hashtag-raw">#from</span> Alpaca defaults<br>
“projectionFactor”: 0.01,<br>
“pointDensity”: 1.00,<br>
“normalSearchRadius”: 2,<br>
“FPFHNeighbors”: 100,<br>
“FPFHSearchRadius”: 5.00,<br>
“distanceThreshold”: 3.00,<br>
“maxRANSAC”: 1000000,<br>
“ICPDistanceThreshold”: 1.50,<br>
“alpha”: 2.0,<br>
“beta”: 2.0,<br>
“CPDIterations”: 100,<br>
“CPDTolerance”: 0.001,<br>
“Acceleration”: False,<br>
“BCPDFolder”: “T:/Slicer/bcpd-master/bcpd-master/win”<br>
}<br>
AlpacaLogic.runLandmarkMultiprocess(sourceModelPath, sourceLandmarkPath, targetModelDirectory, landmarkOutputDirectory, scalingOption, projectionFactor, useJSONFormat, parameters)</p>
</blockquote>
<p>I copied all of the default parameters from the GUI, since I couldn’t figure out how to retrieve them from the command line.<br>
Maybe there is a more elegant solution that would update based on user inputs in the GUI, or the plugin’s defaults (in case they ever change).</p>
<p>Also, for projection factor, the default in the GUI is 1.0, but I saw that the code divides this by 100, so I did the same when hard coding the defaults (since it looks like the division happens and then the value is updated in the parameter list).</p>
<p>Setting it directly to 1.0 in the parameter list gave a bad landmark transfer so it looks like this scaling is very important.</p>
<p>Thanks again!<br>
Eva</p>

---

## Post #6 by @muratmaga (2024-04-19 19:17 UTC)

<p>I am glad this worked.</p>
<p>However, what is the purpose of running ALPACA in this way? If you are going to use fixed parameters, I think batch mode will be easier. I thought maybe you are trying to do a parameter sweep (i.e., try many samples with different sets of parameters).</p>

---

## Post #7 by @evaherbst (2024-04-22 08:01 UTC)

<p>I want to batch process a lot of scans, and am using Alpaca to transfer landmarks to then fit an ROI to each bone and then analyse it. The steps before and after Alpaca are all run from python so it helps to run everything together in an automated way.</p>

---

## Post #8 by @evaherbst (2024-10-01 16:46 UTC)

<p>Hello again,</p>
<p>I just tried running this after not using it for a while.</p>
<p>I am testing it with a single source model for now, which previously worked.</p>
<p>I previously specified the specific .ply and the mrk.json files in the code as the source model path and source landmark path, not just the directories (similar to how those individual files can be selected in the MALPACA GUI)</p>
<p>However, doing that now gives me an error that mrk.json file that it should be a directory:</p>
<blockquote>
<p>NotADirectoryError: [WinError 267] The directory name is invalid:&gt;<br>
‘P:…/source_landmarks/lm_2NHJX1.mrk.json’</p>
</blockquote>
<p>When I replace the specific files with directories, that prevents the above error about the directory but the results remain empty (medianEstimates and individualEstimates folders are created but empty)</p>
<p>My inputs look like this now (previously the first two were pointing to specific files.<br>
sourceModelPath = …/source_scapula_model"<br>
sourceLandmarkPath = “…/source_landmarks”<br>
targetModelPath = “…/scapula_model_output”<br>
targetLandmarkPath = “…/landmark_output”</p>
<p>Do you have any recommendations how to fix this issue to enable batch running Alpaca/Malpaca like I did before?</p>
<p>I checked the Alpaca logic on github but didnt see find changes that could explain this new error.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #9 by @chz31 (2024-10-01 17:19 UTC)

<p>I haven’t tried MALPACA from scripting for a while. I think the batch mode in <code>runLandmarkMultiProcess</code> should simply iterate through <code>sourceModelList</code> from the source directory, then run <code>pairwiseAlignment</code> for each source model to generate a predicted lm array for each source, and then use np.median() to output the median:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1540C1-L1553C26">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1540C1-L1553C26" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1540C1-L1553C26" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1540C1-L1553C26</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1540" style="counter-reset: li-counter 1539 ;">
          <li>    array = self.pairwiseAlignment(</li>
          <li>        sourceFilePath,</li>
          <li>        sourceLandmarkFile,</li>
          <li>        targetFilePath,</li>
          <li>        outputFilePath,</li>
          <li>        scalingOption,</li>
          <li>        projectionFactor,</li>
          <li>        parameters,</li>
          <li>    )</li>
          <li>    landmarkList.append(array)</li>
          <li>medianLandmark = np.median(landmarkList, axis=0)</li>
          <li>outputMedianNode = self.exportPointCloud(</li>
          <li>    medianLandmark, "Median Predicted Landmarks"</li>
          <li>)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Are there any other error printed out? If you have time to add <code>print(array)</code> after line 1548, will it print out the landmark array?</p>

---

## Post #10 by @evaherbst (2024-10-03 12:39 UTC)

<p>Thank you Chi, we will test this.<br>
I also thought it shouldn’t be a problem to have a single landmark source.<br>
I didn’t get any errors when specifying the overall folder paths for the source models and source landmarks which is strange.<br>
The output landmark folders are created but empty.</p>
<p>We will try with the print(array) statement.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #11 by @muratmaga (2024-10-03 17:58 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="10" data-topic="35538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>I also thought it shouldn’t be a problem to have a single landmark source.</p>
</blockquote>
</aside>
<p>MALPACA is for multiple templates (multiple sources). If you have a single source, use ALPACA (single-template option).</p>
<p>If you are using MALPACA logic, then it is normal it is expecting a directory of inputs, as opposed to a single source file.</p>

---

## Post #12 by @chz31 (2024-10-03 18:37 UTC)

<p>If you run MALPACA by scripting using multi-template option by putting a single file in the folder, it should simply iterate through that single file in the folder and export the median equivalent to the output that the single template. Hopefully it can be printed out.</p>
<p>When you specify “single template” in the batch mode, it should simply read that particular template file in the folder and run <code>pairwiseAlignment</code> and export the predictions of that template: :<a href="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1381C1-L1387C14" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/ALPACA/ALPACA.py at 259a0f496551d0e1c5a6851e4233946d672c1391 · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>Then it will pass that single file to <code>runLandmarkMultiProcess</code> to do batch mode for a single template when the boolean function detects the sourceModelPath points to a particular file:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1556C1-L1568C36">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1556C1-L1568C36" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1556C1-L1568C36" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/259a0f496551d0e1c5a6851e4233946d672c1391/ALPACA/ALPACA.py#L1556C1-L1568C36</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1556" style="counter-reset: li-counter 1555 ;">
          <li>elif os.path.isfile(sourceModelPath):</li>
          <li>    rootName = os.path.splitext(targetFileName)[0]</li>
          <li>    outputFilePath = os.path.join(</li>
          <li>        outputDirectory, rootName + extensionLM</li>
          <li>    )</li>
          <li>    array = self.pairwiseAlignment(</li>
          <li>        sourceModelPath,</li>
          <li>        sourceLandmarkPath,</li>
          <li>        targetFilePath,</li>
          <li>        outputFilePath,</li>
          <li>        scalingOption,</li>
          <li>        projectionFactor,</li>
          <li>        parameters,</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’ll also see if I can try it over the weekend. I’m surprised that there’s no output there. If you run batch mode in ALPACA GUI, will it output things normally?</p>

---

## Post #13 by @evaherbst (2024-10-06 08:00 UTC)

<p>Thank you Murat and Chi!</p>
<p>We want to use MALPACA in the future but were testing with a single template for now, which worked in the past.</p>
<p>I think I might have found the error.</p>
<p>The landmarks and meshes were recreated after my initial tests by another member in my group and had slightly different names from each other. Apologies for my oversight in not catching this.<br>
This would also explain why alpaca worked in the gui since there was just one template and it wouldn’t need to match in that case.</p>
<p>We will double check it tomorrow.</p>
<p>Thank you,<br>
Eva</p>

---
