---
topic_id: 1485
title: "Elastix Registration Returns With Error Status"
date: 2017-11-16
url: https://discourse.slicer.org/t/1485
---

# Elastix registration returns with error status

**Topic ID**: 1485
**Date**: 2017-11-16
**URL**: https://discourse.slicer.org/t/elastix-registration-returns-with-error-status/1485

---

## Post #1 by @alireza (2017-11-16 22:54 UTC)

<p>This is great,<br>
Any Idea why I am getting an error on Slicer 4.8.0 r26489 Linux ?<br>
It shows that It has finished doing the registration but an error happens after that</p>
<pre><code>  Progress: 98%
  Progress: 99%
  Progress: 100%
  Progress: 100%
  Writing image ...
  Applying final transform took 0.89s

Final metric value  = -0.616632
Settings of AdaptiveStochasticGradientDescent for all resolutions:
( SP_a 20060.421365 71030.105546 120402.996469 81953.145725 )
( SP_A 20.000000 20.000000 20.000000 20.000000 )
( SP_alpha 1.000000 1.000000 1.000000 1.000000 )
( SigmoidMax 1.000000 1.000000 1.000000 1.000000 )
( SigmoidMin -0.055680 -0.202084 -0.604650 -0.914502 )
( SigmoidScale 0.000000 0.000000 0.000000 0.000000 )

Time spent on saving the results, applying the final transform etc.: 904 ms.
Running elastix with parameter file 1: "/home/user/.config/NA-MIC/Extensions-26489/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Resources/RegistrationParameters/Parameters_BSpline.txt", has finished.


Current time: Thu Nov 16 17:47:16 2017.
Time used for running elastix with this parameter file:
  14.0s.

-------------------------------------------------------------------------

Total time elapsed: 17.4s.


Command 'elastix' returned non-zero exit status -11
Traceback (most recent call last):
  File "/home/user/.config/NA-MIC/Extensions-26489/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py", line 325, in onApplyButton
    movingVolumeMaskNode = self.movingVolumeMaskSelector.currentNode())
  File "/home/user/.config/NA-MIC/Extensions-26489/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py", line 556, in registerVolumes
    self.logProcessOutput(ep)
  File "/home/user/.config/NA-MIC/Extensions-26489/SlicerElastix/lib/Slicer-4.8/qt-scripted-modules/Elastix.py", line 496, in logProcessOutput
    raise subprocess.CalledProcessError(return_code, "elastix")
CalledProcessError: Command 'elastix' returned non-zero exit status -11</code></pre>

---

## Post #2 by @lassoan (2017-11-18 05:33 UTC)

<p>Please check “Keep temporary files” checkbox in advanced section before starting the registration. When it completes, click “Show temp folder” button and see if the most recently created folder contains <code>input</code> and <code>result-transform</code> folders. Are there result.0.mhd and result.1.mhd files in there?</p>
<p>Have you installed or built Elastix yourself, or you use Elastix that is bundled with the Slicer extension?</p>

---

## Post #3 by @alireza (2017-12-14 00:26 UTC)

<p>Thanks for the help,<br>
I checked and It contains the <code>input</code> and <code>result-transform</code> folders and the <code>results.0.mhd</code> and <code>results.1.mhd</code> are also in there.</p>
<p>I have downloaded the Linux 64 bit binaries from their <a href="http://elastix.isi.uu.nl/download_links.php" rel="nofollow noopener">website</a> and after extracting, I’m selecting the <code>bin</code> folder location for the <code>custom elastix toolbax location</code> section of the Advance section</p>

---

## Post #4 by @lassoan (2017-12-14 02:08 UTC)

<p>We’ve made some fixes, so if you use most recent nightly versions then it may not be necessary to set up your own Elastix (the one bundled with the extension should work).</p>
<p>If it still doesn’t work then set up your own Elastix. Downloading and extracting Elastix is not enough but you also need to “install” it as described <a href="https://superuser.com/questions/884179/how-to-install-elastix-a-toolbox-for-rigid-and-nonrigid-registration-of-images">here</a>.</p>

---
