# Prevent transformix running in Slicer Elastix

**Topic ID**: 7902
**Date**: 2019-08-06
**URL**: https://discourse.slicer.org/t/prevent-transformix-running-in-slicer-elastix/7902

---

## Post #1 by @Prashant_Pandey (2019-08-06 21:09 UTC)

<p>Using Slicer 4.10.2</p>
<p>I am writing a runtime sensitive registration module which makes use of the slicer elastix module. As you can imagine elastix registration takes some time to run (about ~2 minutes for the data and parameters I am using). However transformix also runs after every run of elastix, and this takes an additional 30 seconds before the process is finished. How can I prevent transformix from running? I did not specify an output volume in Elastix, and my parameter file also specifies not to write an output image <code>(WriteResultImage "false")</code>.</p>

---

## Post #2 by @Prashant_Pandey (2019-08-06 21:49 UTC)

<p><em>Maybe</em> this is where the issue is:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerElastix/blob/9ded00135fd8a3d5da3ecedd3a68320e40d74d38/Elastix/Elastix.py#L584-L594" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerElastix/blob/9ded00135fd8a3d5da3ecedd3a68320e40d74d38/Elastix/Elastix.py#L584-L594" target="_blank" rel="nofollow noopener">lassoan/SlicerElastix/blob/9ded00135fd8a3d5da3ecedd3a68320e40d74d38/Elastix/Elastix.py#L584-L594</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="584" style="counter-reset: li-counter 583 ;">
<li>if not self.abortRequested:</li>
<li>  resultResampleDir = os.path.join(tempDir, 'result-resample')</li>
<li>  qt.QDir().mkpath(resultResampleDir)</li>
<li>  inputParamsTransformix = []</li>
<li>  inputParamsTransformix += ['-tp', resultTransformDir+'/TransformParameters.'+str(len(parameterFilenames)-1)+'.txt']</li>
<li>  inputParamsTransformix += ['-in', os.path.join(inputDir, 'moving.mha')]</li>
<li>  inputParamsTransformix += ['-out', resultResampleDir]</li>
<li>  if outputTransformNode:</li>
<li>    inputParamsTransformix += ['-def', 'all']</li>
<li>  tp = self.startTransformix(inputParamsTransformix)</li>
<li>  self.logProcessOutput(tp)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Since transformix’s purpose is to generate the output transformed volume, perhaps it should only be called when outputVolumeNode exists instead of being called every time?</p>

---

## Post #3 by @pieper (2019-08-06 22:10 UTC)

<p>Yes, that makes sense - would you be able to add that option and provide a pull request?</p>

---

## Post #4 by @Prashant_Pandey (2019-08-06 23:21 UTC)

<p>Sure, I’ll do that by this week!</p>

---

## Post #5 by @Prashant_Pandey (2019-08-07 03:52 UTC)

<p>Here is the pull request: <a href="https://github.com/lassoan/SlicerElastix/pull/19" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix/pull/19</a></p>

---

## Post #6 by @lassoan (2019-08-07 04:18 UTC)

<p>Transformix is always necessary now because we need to generate a resampled moving volume and/or a displacement field. Both are provided by Transformix.</p>
<p>We could avoid the need to run Transformix if we could read the proprietary Elastix transformation file format. I’ve started implementing a reader for linear transforms, but did not finish it. I include it below - it would be great if you could finish it and integrate it into SlicerElastix module. We should probably implement bspline reader, too.</p>
<pre><code class="lang-python"># Example input:
transformStr="(TransformParameters 0.022507 0.013835 0.013726 7.760838 4.879223 -0.014589)"

transformParams = transformStr.strip("()").split(" ")
transformParams.pop(0)
transformParams = [ float(x) for x in transformParams ]
(roll, pitch, yaw) = np.array(transformParams)[0:3]
computeZYX=False

[rx,ry,rz]=transformParams[0:3]
[tx,ty,tz]=transformParams[3:6]

from math import sin, cos
rotX = np.array([[1.0, 0.0, 0.0], [0.0, cos(rx), -sin(rx)], [0.0, sin(rx), cos(rx)]])
rotY = np.array([[cos(ry), 0.0, sin(ry)], [0.0, 1.0, 0.0], [-sin(ry), 0.0, cos(ry)]])
rotZ = np.array([[cos(rz), -sin(rz), 0.0], [sin(rz), cos(rz), 0.0], [0.0, 0.0, 1.0]])

if computeZYX:
    # Aply the rotation first around Y then X then Z
    fixedToMovingDirection = np.dot(np.dot(rotZ, rotY), rotX)
else:
    # Like VTK transformation order
    fixedToMovingDirection = np.dot(np.dot(rotZ, rotX), rotY)

fixedToMoving = np.eye(4)
fixedToMoving[0:3,0:3] = fixedToMovingDirection
fixedToMoving[0:3,3] = transformParams[3:6]

# Create Slicer linear transform ("to parent" direction, in RAS)
ras2lps = np.array([[-1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]])
movingToFixed = np.dot(np.dot(ras2lps, np.linalg.inv(fixedToMoving)), ras2lps)
slicer.util.updateTransformMatrixFromArray(getNode('Transform_1'),movingToFixed)</code></pre>

---

## Post #7 by @Prashant_Pandey (2019-08-07 04:34 UTC)

<p>I should have made clear that, in my pull request, transformix is still run but with limited parameters so that only the deformation field is written and not a new output image (unless required by the user). This saves a little of time overall.</p>
<p>I will take a look at your code for the linear transform conversion to see if i can contribute!</p>

---

## Post #8 by @Prashant_Pandey (2019-08-07 18:20 UTC)

<p>Have you confirmed that this is the correct transformation from the Euler angles to a linear transform? If so, is the only thing left to read the transform text file and write the transform to Slicer?</p>

---

## Post #9 by @lassoan (2019-08-07 19:54 UTC)

<p>Yes, the computation should be correct and the remaining task is to iterate through the transform files and apply this parser on them.</p>

---

## Post #10 by @Prashant_Pandey (2019-08-08 01:23 UTC)

<p>Here is the pull request for parsing linear transformations: <a href="https://github.com/lassoan/SlicerElastix/pull/21" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix/pull/21</a></p>
<p>I included support for translation only registrations too.</p>

---

## Post #11 by @lassoan (2019-08-10 12:49 UTC)

<p>Thank you. I’ve merged this and added reading of bspline transforms, too.</p>

---
