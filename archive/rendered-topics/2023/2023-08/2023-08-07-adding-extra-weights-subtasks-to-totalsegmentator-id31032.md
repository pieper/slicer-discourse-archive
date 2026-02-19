---
topic_id: 31032
title: "Adding Extra Weights Subtasks To Totalsegmentator"
date: 2023-08-07
url: https://discourse.slicer.org/t/31032
---

# Adding extra weights/subtasks to TotalSegmentator

**Topic ID**: 31032
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/adding-extra-weights-subtasks-to-totalsegmentator/31032

---

## Post #1 by @evaherbst (2023-08-07 17:20 UTC)

<p>Hello,</p>
<p>I would like to be able to implement the additional license-dependent weights/subtasks for  TotalSegmentator in 3D Slicer.</p>
<p>I received the weights files from Jakob Wassterthal and have added them to the 3d_fullres weights folder (as per this post: <a href="https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-command-python-scripts-totalsegmentator-returned-non-zero-exit-status-120/26755/22" class="inline-onebox">TotalSegmentator error at first run: Command ...Python\Scripts\TotalSegmentator... returned non-zero exit status 120 - #22 by zhang_ming</a>)</p>
<p>However, since they are new weights, I think I need to adjust the TotalSegmentator.py code in “…AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\TotalSegmentator\lib\Slicer-5.2\qt-scripted-modules”.<br>
Is this correct?</p>
<p>I see where I can add new tasks to the GUI (lines 307-314) but I do not see where I can link the weights file for that task.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @evaherbst (2023-08-08 10:23 UTC)

<p>I had a closer look at the code and noticed the following:</p>
<p>The new subtasks I am trying to run (“bones_tissue_test” and “aortic_branches_test”) are present as arguments in the TotalSegmentator file in the TotalSegmentator repository (<a href="https://github.com/wasserth/TotalSegmentator/blob/master/bin/TotalSegmentator" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/blob/master/bin/TotalSegmentator</a>).</p>
<p>However, they are not listed in the TotalSegmentator file in the Python&gt;scripts folder in Slicer3D. I just tried reinstalling Slicer but that also did not update the subtasks.</p>
<p>If I replace the TotalSegmentator file in the Python&gt;scripts folder with the updated version from the github repo of Jakob Wasserthal, the 3D Slicer installation directory, I get an error that there are too many arguments.</p>
<p>Furthermore, I assume I need to not only add the new tasks in lines 207-315 in the TotalSegmentator.py script in the Slicer Total Segmentator folder, but also make sure all the label terminologies are included.</p>
<p>Could you advise me in</p>
<ol>
<li>how to add the new subtask arguments in the TotalSegmentator file in the Slicer Python scrips folder</li>
<li>how to adjust TotalSegmentator.py in the Slicer Total Segmentator extensions folder to add these subtasks and their corresponding labels?</li>
</ol>
<p>Thank you very much,<br>
Eva</p>

---

## Post #3 by @rbumm (2023-08-08 11:50 UTC)

<p>Do you want to run these tests in 3D Slicer and are you in for a complicated procedure?</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Here you go:</p>
<p>To run the new test tasks from the extension, you must “git install” the latest TotalSegmentator tool in the 3D Slicer directory.</p>
<p>In 3D Slicers Python console run</p>
<pre><code class="lang-auto">slicer.util.pip_uninstall("TotalSegmentator")
slicer.util.pip_install("git+https://github.com/wasserth/TotalSegmentator.git")
</code></pre>
<p>Then, find your 3D Slicer Python script directory.</p>
<p>On my Windows system, this is:<br>
C:\Users\Yourname\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts</p>
<p>Open a PowerShell in this directory.<br>
Copy your weights into this directory.</p>
<p>In order to update the TotalSegmentator weights (here: aortic branches, they are licensed and may not be shared), execute</p>
<pre><code class="lang-auto">python ./totalseg_import_weights -i ./Task435_Heart_vessels_118subj.zip
</code></pre>
<p>The next problem is that the TotelSegmentator 3D Slicer <strong>extension</strong> does not know yet about the newly installed tasks.</p>
<p>See the next post. <a class="mention" href="/u/lassoan">@lassoan</a> and I will find a way to integrate new test tasks as well as implement a way to add new or licensed weights in the extension. Until then, you can use my workaround.</p>

---

## Post #4 by @rbumm (2023-08-08 12:11 UTC)

<p>Find new tasks<br>
“aortic_branches_test” and “bones_tissue_test” implemented in my development version of<br>
<a href="https://github.com/rbumm/SlicerTotalSegmentator/blob/subset_dev_branch/TotalSegmentator/TotalSegmentator.py">Totalsegmentator.py</a></p>
<p>You could use this Python code file in your local TotalSegmentator extension folder until the standard extension gets updated.</p>
<p>Restart Slicer to see the new tasks.</p>

---

## Post #5 by @evaherbst (2023-08-08 12:36 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a>  Wow, thank you so much for this solution!</p>
<p>I am having trouble reinstalling TotalSegmentator due to a permission error:</p>
<blockquote>
<p>Could not install packages due to an OSError: [WinError 5] Access is denied: ‘C:\Users\[myname]\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\~harset_normalizer\md.cp39-win_amd64.pyd’</p>
<p>Consider using the <code>--user</code> option or check the permissions.</p>
</blockquote>
<p>I guess this is because of not having admin rights for our work computers.<br>
I’ll try to get temp admin access (not sure how to implement the --user option).</p>
<p>Thanks again, I will keep you updated whether it works!</p>

---

## Post #6 by @evaherbst (2023-08-08 13:36 UTC)

<p>Hi again.<br>
False alarm, it works perfectly now.</p>
<p>Thank you so so much <a class="mention" href="/u/rbumm">@rbumm</a> !</p>
<p>EDIT: I do get a warning now when I open Slicer that says:</p>
<blockquote>
<p>C:\Users.…\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\requests_<em>init</em>_.py:102: RequestsDependencyWarning: urllib3 (1.26.14) or chardet (5.1.0)/charset_normalizer (2.0.12) doesn’t match a supported version!<br>
warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn’t match a supported "</p>
</blockquote>
<p>Is this ok?</p>
<p>Best,<br>
Eva</p>

---

## Post #7 by @rbumm (2023-08-08 14:32 UTC)

<p>I get the same warning and no negative effects yet …</p>

---

## Post #8 by @evaherbst (2023-08-08 14:53 UTC)

<p>Great, thanks for the quick reply!</p>
<p>No issues on my end yet either.</p>
<p>Best,<br>
Eva</p>

---

## Post #9 by @Lee_Ho_Jun (2023-08-17 10:14 UTC)

<p>Hi!<br>
I’m trying to do the same thing as Eva, and I’m slightly confused.<br>
Should I do everything that is in the above post, and replace the Totalsegmentator.py?<br>
Or is it suffice to just repalce Totalsegmentator.py?<br>
Or is it now in the official extension, and should I wait for any update schedules?<br>
Thanks in advance.</p>
<p>HJ</p>

---

## Post #10 by @rbumm (2023-08-17 10:49 UTC)

<p>In the latest TotalSegmentator extension, we have implemented a checkbox “use latest development version” and a button “Import weights”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65c0f53b8d546ee3efb9fd9906fc0753255de3cc.png" alt="image" data-base62-sha1="ew9DmV6fFls6Pod24AkRwECDsjq" width="589" height="213"></p>
<p>When you add additional weights, you should make a "“Force reinstall” with “use latest development version” checked. Then press the “Import weights” button and search the zipped weight file on your hard drive. Select it and it will be automatically installed.</p>
<p>Please update the TotalsSegmentator extension or uninstall/reinstall it.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> For some reason, this does not work in 5.3.0 yet (I see the older extension after a reinstall)</p>

---

## Post #11 by @lassoan (2023-08-17 11:08 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="10" data-topic="31032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>For some reason, this does not work in 5.3.0 yet (I see the older extension after a reinstall)</p>
</blockquote>
</aside>
<p>Extensions are only updated for the latest Slicer Stable Release and the latest Slicer Preview Release. If you want to get the latest extension version for a Slicer Preview Release then you need to download and install the latest Slicer Preview Release.</p>

---

## Post #12 by @rbumm (2023-08-17 11:14 UTC)

<p>It would be good to have a warning message for such cases. Not very obvious …</p>

---

## Post #13 by @lassoan (2023-08-17 11:42 UTC)

<p>The extension update process is described <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#update-extensions-for-slicer-preview-releases">here</a>. Where would you show a warning?</p>

---

## Post #14 by @rbumm (2023-08-17 13:00 UTC)

<p>The best way would be to display a message box as soon as the user tries to load an extension from the extension manager:<br>
“You are loading a possibly outdated extension because you are not using the latest stable (x.x.x)  or the preview (y.y.y) version of 3D Slicer”</p>

---

## Post #16 by @evaherbst (2023-09-25 12:02 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>I recently downloaded Slicer 5.4 (stable release) and followed your instructions for adding the extra weights. It works well - after importing each weight, the restart/update was suggested automatically.</p>
<p>Thanks!<br>
Eva</p>

---

## Post #17 by @rbumm (2023-09-25 12:41 UTC)

<p>Thank you for the feedback, Eva!</p>
<p>A new version of TotalSegmentator is on the horizon. Stay tuned.</p>

---

## Post #18 by @Michael_Allen (2023-10-12 03:24 UTC)

<p>I am also running into issue using manually installed weights. Using Mac 12.6.1 with slicer 5.4/5.5. Mac intel i5, intel iris 6100</p>
<p>I received the zip file from Jakob for bone_tissue_test. I had previously (i believe with slicer 5.4) installed total segmentator, and manually installed the weights by either using the import function, or copying into the 3d full res folder, I can’t recall now. It was workign great for awhile, selecting bones_tissue_test as the segmentation task in drop down menu.</p>
<p>At some point I installed slicer 5.5 and now I’ve run into issues. I downgraded to 5.4 and have the same issues. It basically error-ed and said I couldn’t select bones_tissue_test anymore. I then fooled around, trying to reinstall segmentator, reinstall pytorch, reinstall weights, and cannot get it to work anymore.</p>
<p>Here is the python log:</p>
<p>/Applications/Slicer.app/Contents/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py:783: UserWarning: ‘has_cuda’ is deprecated, please use ‘torch.backends.cuda.is_built()’<br>
cuda = torch.cuda if torch.has_cuda and torch.cuda.is_available() else None<br>
[Python] Failed to compute results.<br>
[Python] Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/nv/5xxpc59s7rxbzpmwslgc90v00000gp/T/Slicer-allenm/__SlicerTemp__2023-10-11_19+15+50.643/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/nv/5xxpc59s7rxbzpmwslgc90v00000gp/T/Slicer-allenm/__SlicerTemp__2023-10-11_19+15+50.643/segmentation’, ‘–ml’, ‘–task’, ‘bones_tissue_test’]’ returned non-zero exit status 2.<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 271, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 868, in process<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 701, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/nv/5xxpc59s7rxbzpmwslgc90v00000gp/T/Slicer-allenm/__SlicerTemp__2023-10-11_19+15+50.643/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/nv/5xxpc59s7rxbzpmwslgc90v00000gp/T/Slicer-allenm/__SlicerTemp__2023-10-11_19+15+50.643/segmentation’, ‘–ml’, ‘–task’, ‘bones_tissue_test’]’ returned non-zero exit status 2.</p>
<p>Inside the total segmentator window, this is the output:</p>
<p>Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘/private/var/folders/nv/5xxpc59s7rxbzpmwslgc90v00000gp/T/Slicer-allenm/__SlicerTemp__2023-10-11_19+15+50.643/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/nv/5xxpc59s7rxbzpmwslgc90v00000gp/T/Slicer-allenm/__SlicerTemp__2023-10-11_19+15+50.643/segmentation’, ‘–ml’, ‘–task’, ‘bones_tissue_test’]<br>
/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator:5: DeprecationWarning: pkg_resources is deprecated as an API. See <a href="https://setuptools.pypa.io/en/latest/pkg_resources.html" class="inline-onebox" rel="noopener nofollow ugc">Package Discovery and Resource Access using pkg_resources - setuptools 68.2.2.post20231008 documentation</a><br>
from pkg_resources import require<br>
usage: TotalSegmentator [-h] -i filepath -o directory [-ml]<br>
[-nr NR_THR_RESAMP] [-ns NR_THR_SAVING] [-f]<br>
[-t NORA_TAG] [-p]<br>
[-ta {total,lung_vessels,cerebral_bleed,hip_implant,coronary_arteries,body,pleural_pericard_effusion,liver_vessels,bones_extremities,tissue_types,heartchambers_highres,head,aortic_branches,heartchambers_test,test}]<br>
[-rs ROI_SUBSET [ROI_SUBSET …]] [-s] [-r]<br>
[-cp CROP_PATH] [-bs] [-fs] [-q] [-v] [–test 0|1|2|3]<br>
[–version]<br>
TotalSegmentator: error: argument -ta/–task: invalid choice: ‘bones_tissue_test’ (choose from ‘total’, ‘lung_vessels’, ‘cerebral_bleed’, ‘hip_implant’, ‘coronary_arteries’, ‘body’, ‘pleural_pericard_effusion’, ‘liver_vessels’, ‘bones_extremities’, ‘tissue_types’, ‘heartchambers_highres’, ‘head’, ‘aortic_branches’, ‘heartchambers_test’, ‘test’)</p>
<p>Why is bones_tissue_test an invalid choice? In the totalsegmentator.py file it is listed in the self.tasks area?</p>
<p>Current pytorch util shows torch 2.1.0 and torchvision 0.16.0</p>
<p>Thanks for any help!</p>

---

## Post #19 by @rbumm (2023-10-12 13:04 UTC)

<p>The TotalSegmenter extension has not yet been upgraded to Totalsegmentator 2.0 yet.<br>
There are issues with the SimpleITK,  which may be incompatible with what Slicer uses, at least what lungmask uses.</p>
<pre><code class="lang-auto">Name: SimpleITK
Version: 2.3.0
Summary: SimpleITK is a simplified interface to the Insight Toolkit (ITK) for image registration and segmentation
Home-page: http://simpleitk.org/
Author: Insight Software Consortium
Author-email: insight-users@itk.org
License: Apache
Location: c:\users\rudolf\appdata\local\slicer.org\slicer 5.4.0_2\lib\python\lib\site-packages
Requires: 
Required-by: acvl-utils, lungmask, nnunetv2, TotalSegmentator
</code></pre>
<p>See a <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/32" rel="noopener nofollow ugc">PR here</a></p>

---

## Post #20 by @Michael_Allen (2023-10-13 02:14 UTC)

<p>Any idea how to go back to what I had working before? I rolled back to slicer 5.4 but that didn’t allow me to get it working again using the bone_tissue_test weight</p>

---

## Post #21 by @rbumm (2023-10-13 07:49 UTC)

<p>I would suggest deleting the complete 5.4 folders, reinstalling Slicer, reinstalling Pytorch, restarting Slicer, reinstalling TotalSegmentator, restarting Slicer, and then doing what you did to install the weights previously.</p>

---

## Post #22 by @rbumm (2023-10-13 08:01 UTC)

<p>But if you can, wait for TotalSegmentator v2 extension to be released.</p>

---
