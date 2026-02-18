# Calculate harmonic energy of displacement vector field (DVF)

**Topic ID**: 5211
**Date**: 2018-12-28
**URL**: https://discourse.slicer.org/t/calculate-harmonic-energy-of-displacement-vector-field-dvf/5211

---

## Post #1 by @11118 (2018-12-28 12:06 UTC)

<p>After registration produces DVF, how to use 3Dslicer to calculate its jacobian and harmonic energy.Just like the evaluation framework in this article:A framework for deformable image registration validation in radiotherapy clinical applications.I can’t find this function?</p>

---

## Post #2 by @lassoan (2018-12-29 15:08 UTC)

<p>Sliver has several modules for qualitative, quantitative, and clinical application specific evaluation of registration.</p>
<ul>
<li>Qualitative: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_display_options" rel="nofollow noopener">Transforms</a> module offers rich visualization of transforms in slice and 3D views.</li>
<li>Anatomical metric - Hausdorff distance and Dice similarity coefficient: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison" rel="nofollow noopener">Segment comparison</a> module in SlicerRT</li>
<li>Dose metrics - <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseComparison" rel="nofollow noopener">Dose comparison</a>, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseVolumeHistogram" rel="nofollow noopener">Dose volume histogram metrics</a>, <a href="https://github.com/SlicerRt/SlicerRT/tree/master/DvhComparison" rel="nofollow noopener">Dose volume histogram comparison</a> modules in SlicerRT extension</li>
<li>Generic registration quality assurance: <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/blob/master/Documentation.md" rel="nofollow noopener">https://github.com/gsi-biomotion/SlicerRegistrationQA/blob/master/Documentation.md</a>
</li>
<li>You can also compute various custom metrics using Python (numpy, etc.) in Slicer’s Python console, <a href="https://github.com/Slicer/SlicerJupyter" rel="nofollow noopener">Slicer Jupyter notebook</a>, or by adding a scripted module</li>
</ul>
<p>If there are any additional metrics described in “A framework for deformable image registration validation in radiotherapy clinical applications” paper that you cannot find in Slicer then please contact the authors and ask them how to access those methods and report back to us. We can then help in getting those methods available in current version of Slicer.</p>

---

## Post #3 by @11118 (2018-12-30 09:16 UTC)

<p>thank you very much,I found the Jacobian but I can not found harmonic energy of DVF,</p>

---

## Post #4 by @lassoan (2018-12-30 14:01 UTC)

<p>I’m not sure if harmonic energy has any clinically relevant meaning and it is not commonly used, so you not miss much by not computing it. If you want the value anyway then contact the authors of the paper that you referred to above.</p>

---

## Post #5 by @11118 (2019-01-02 12:06 UTC)

<p>Thank you very much for your suggestion. Maybe I can take advantage of other features of DVF and give up one to find a more clinically available feature.</p>

---

## Post #6 by @labixin (2019-08-22 02:49 UTC)

<p>Hi all,</p>
<p>I am now doing quantitative evaluation of registration and I plan to use three categories of metrics.</p>
<ol>
<li>Segment comparison: Hausdorff distance and Dice similarity coefficient</li>
<li>Deformation vector field: Jacobian determinant</li>
<li>Anatomical landmarks: Target registration error</li>
</ol>
<p>I could’t find where to calculate TRE. I wonder if the <a href="https://discourse.slicer.org/t/evaluating-registration-error/3091/4">Fiducial registration wizard module</a> is similar to the TRE calculation.</p>
<p>Besides, is the Jacobian calculated within “RegistrationQA” module (Sorry but I couldn’t find it)? And the module can’t be installed using the latest Slicer preview version? (The log is shown below)</p>
<p>Hope for some suggestions. Thanks.</p>
<details>
<summary>
Error Log</summary>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “D:\Slicer 4.11.0-2019-08-13\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-28438/RegistrationQA/lib/Slicer-4.11/qt-scripted-modules/CreateRegistrationHierarchy.py”, line 294<br>
except Exception, e:<br>
^<br>
SyntaxError: invalid syntax<br>
loadSourceAsModule - Failed to load file “C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-28438/RegistrationQA/lib/Slicer-4.11/qt-scripted-modules/CreateRegistrationHierarchy.py”  as module “CreateRegistrationHierarchy” !<br>
Fail to instantiate module  “CreateRegistrationHierarchy”<br>
The following modules failed to be instantiated:<br>
CreateRegistrationHierarchy</p>
</details>
<p>Crayon</p>

---

## Post #7 by @lassoan (2019-08-22 18:45 UTC)

<aside class="quote no-group" data-username="labixin" data-post="6" data-topic="5211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>And the module can’t be installed using the latest Slicer preview version? (The log is shown below)</p>
</blockquote>
</aside>
<p>The module seem to use some Python2 syntax that is not compatible with Python3. It would be great if you could give it a go and make the changes (e.g., <code>except Exception as e</code> instead <code>except Exception, e</code>) and submit a pull request. If you have trouble fixing all the issues then let us know.</p>
<aside class="quote no-group" data-username="labixin" data-post="6" data-topic="5211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I could’t find where to calculate TRE. I wonder if the <a href="https://discourse.slicer.org/t/evaluating-registration-error/3091/4">Fiducial registration wizard module</a> is similar to the TRE calculation.</p>
</blockquote>
</aside>
<p>Fiducial registration wizard computes TRE (as RMS of the distance between fixed points and transformed moving points).</p>

---

## Post #8 by @labixin (2019-08-24 13:23 UTC)

<p>Thanks for your reply. Sorry but I am not familiar with python programming. Could you explain more about how to do that? Thanks a lot!</p>
<p>Besides, I have downloaded an early version of slicer which is compatible with Python2 (Slicer-4.11.0-2019-02-27-win-amd64) and gave it a try. But I still failed to calculate the “Fiducial Distance, Contour Measures, Inverse Consistency” after assigning roles (the Log is shown below). What’s more, when I click the “Jacobian determinant”, the software crashed down (showing something wrong with the vtkSlicerRegistrationQAModuleLogic.dll)? Is there something wrong with the module? Hope for some advice. Your help is highly appreciated!</p>
<details>
<summary>
Log</summary>
<p>Reading RegistrationQA parameter node<br>
Reading RegistrationQA parameter node<br>
Volumes not set!</p>
<p>InverseConsist: Can’t calculate inverse consistency!</p>
<p>CalculateRegQAFrom: Can’t calculate inverse consistency!</p>
<p>CalculateContourStatistic: No transform or vector!</p>
<p>CreateTransormFromVector: Volumes not set!</p>
<p>CalculateFiducialsDistance: Invalid input parameters!</p>
<p>CalculateRegQAFrom: Cannot calculate Fiducal distance!</p>
</details>
<p>Sincerely,</p>
<p>Crayon</p>

---

## Post #9 by @labixin (2019-08-25 13:37 UTC)

<p>Finally I have fixed all the issues with the syntax and succeeded in calculating all the values. And I found that the reason why slicer crashed down and output nothing was the incorrect input (the dvf must be loaded as “volume” but not “transform”). Very useful extension! Thank you all for building and integrating it with slicer.</p>
<p>Crayon</p>

---

## Post #10 by @lassoan (2019-08-26 19:00 UTC)

<p>Great! I don’t see any pull requests with your changes <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/pulls" rel="nofollow noopener">here</a>. Make sure you push all your changes to your fork and submit a pull request to the official repository to make RegistrationQA work for others, too (and to remove the burden of maintenance work from you). Thanks!</p>

---

## Post #11 by @labixin (2019-08-27 19:25 UTC)

<p>Hi,</p>
<p>I have submitted a pull request with my changes. I’m glad that I could ever make some contributions (never before).</p>
<p>Besides, I have a question relating to the evaluation of Jacobian determinant. I have registered two ct images which have different voxel intensities of ROI because of tumor resection and post-surgical changes. I wonder how to quantify the impact of intensity variation? Could the jacobian metric indicate something? (I am not sure about the interpretation of jacobian) Hope for some suggestions. Thank you!</p>
<p>Sincerely,<br>
Crayon</p>

---

## Post #12 by @lassoan (2019-08-28 14:56 UTC)

<aside class="quote no-group" data-username="labixin" data-post="11" data-topic="5211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I have submitted a pull request with my changes.</p>
</blockquote>
</aside>
<p>Could you please post the link to the pull request (just to make sure it is merged)?</p>
<aside class="quote no-group" data-username="labixin" data-post="11" data-topic="5211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I’m glad that I could ever make some contributions (never before).</p>
</blockquote>
</aside>
<p>We are glad, too, congratulations! <img src="https://emoji.discourse-cdn.com/twitter/champagne.png?v=12" title=":champagne:" class="emoji" alt=":champagne:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="labixin" data-post="11" data-topic="5211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I have registered two ct images which have different voxel intensities of ROI because of tumor resection and post-surgical changes. I wonder how to quantify the impact of intensity variation? Could the jacobian metric indicate something?</p>
</blockquote>
</aside>
<p>Usually when there is no correspondence between two images (instrument is visible in an intra-procedural image, tumor is not visible in post-procedural image, etc.) then you mask out that region in the images to make sure you don’t introduce any errors by trying to match unrelated things. These masked regions probably have to be excluded from further analysis, too.</p>

---

## Post #13 by @labixin (2019-09-02 03:16 UTC)

<p>Thanks for your extended help. I will focus more on the related things. Besides, here is the link <a href="https://github.com/crayonxx/SlicerRegistrationQA" rel="nofollow noopener">pull request</a>.</p>
<p>Crayon</p>

---

## Post #14 by @lassoan (2019-09-04 14:30 UTC)

<p>Thank you, I’ve found the updated file that you uploaded. It is not a “pull request” just an upload to your forked version of the repository, so the original author was not notified. I’ve created a pull request now (see <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/pulls" rel="nofollow noopener">here</a>), so your changes will hopefully get into the official version soon.</p>

---

## Post #15 by @labixin (2019-09-05 08:00 UTC)

<p>Thank you for keep following. I have checked that the pull request is now merged. Sorry that I forgot to pull request in the original repository. Thanks again for all your efforts in building slicer! <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>
<p>Crayon</p>

---

## Post #16 by @labixin (2020-10-12 14:50 UTC)

<p>Hi all,</p>
<p>I’m using Registration QA extension to calculate the Jacobian Determinant. I want to calculate it within specific segment (from Segmentation Module). The “Create ROI around segments” button could create a rectangular box around segment. However it’s not so conformal. How could I implement this? Where could I modify the source code?</p>
<p>Hope for some suggestions. Thanks a lot!</p>
<p>Crayon</p>

---
