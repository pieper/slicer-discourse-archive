# Swiss Skull Stripper: troubles invoking from python console

**Topic ID**: 305
**Date**: 2017-05-13
**URL**: https://discourse.slicer.org/t/swiss-skull-stripper-troubles-invoking-from-python-console/305

---

## Post #1 by @drAl (2017-05-13 15:37 UTC)

<p>Hi everyone!</p>
<p>I’m trying to run the Swiss Skull Stripper from script and I’m getting this error every time:</p>
<hr>
<p>"Swiss Skull Stripper standard error:</p>
<p>Exception caught !</p>
<p>itk::ImageFileReaderException (0000001D6C5BD080)<br>
Location: "unknown"<br>
File: c:\d\p\slicer-462-package\itkv4\modules\io\imagebase\include\itkImageFileReader.hxx<br>
Line: 87<br>
Description: FileName must be specified</p>
<hr>
<p>I’m trying to figure out if there’s an error with parameters when invoking the module. I’m using this (in this order):<br>
’’‘<br>
parameters = {}<br>
1. "atlasImage"<br>
2. "atlasMask"<br>
3. “patientVolume” 3<br>
4. “patientOutputVolume” 4<br>
5. “patientMaskLabel” 5<br>
’’'<br>
I’m running the module:<br>
sss = slicer.modules.swissskullstripper<br>
return (slicer.cli.run(sss, None, parameters))</p>
<p>Anyone have any idea!?</p>
<p>Thanks in advance!! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=5" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #2 by @lassoan (2017-05-13 16:05 UTC)

<p>One of the required inputs are not specified in <code>parameters</code> variable, probably because you use incorrect parameter name. Parameter names can be printed using the script here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>
<p>Parameter (0/0): <strong>atlasMRIVolume</strong> (Atlas Volume)<br>
Parameter (0/1): <strong>atlasMaskVolume</strong> (Atlas Mask Volume)<br>
Parameter (1/0): <strong>patientVolume</strong> (Patient Volume)<br>
Parameter (2/0): <strong>patientOutputVolume</strong> (Patient Output Volume)<br>
Parameter (2/1): <strong>patientMaskLabel</strong> (Patient Mask Label)</p>

---

## Post #3 by @brhoom (2017-05-13 16:26 UTC)

<p>Sometimes I get itkImageFileReader error in Linux because:</p>
<ul>
<li>The path or the file name contains spaces or special characters.</li>
<li>Don’t have permission to access the file.<br>
Good luck!</li>
</ul>

---

## Post #4 by @drAl (2017-05-13 16:48 UTC)

<p>Thanks for answering!!</p>
<p>that is the piece of code I’m using, but still not working!</p>
<p>I get your point, though. I’m loading/creating this four parameters (atlasMRIVolume, atlasMaskVolume, patientOutputVolume and patientMaskLabel) but for the patient volume I am just getting the ID:</p>
<p>(parameters[“patientVolume”] = volumeNode.GetID())</p>
<p>I don’t know if (maybe) I should perform any other instruction before setting this volume to the parameters.</p>
<p>Do you know where can I find documentation about swiss skull stripping module?</p>
<p>I’ll keep trying <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Again thanks for tip <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #5 by @drAl (2017-05-13 16:49 UTC)

<p>hey!! Thanks brhoom!</p>
<p>I’ll double check the syntaxis again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>thankks!! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #6 by @drAl (2017-05-17 16:29 UTC)

<p>Hi again!!</p>
<p>So after almost a week…I haven’t been able to invoke the module without an error.</p>
<p>Does anyone know where can I found some documentation about the skull stripper or the swiss skull stripper?? I would really appreciate it.</p>
<p>Another way to find out what I need (what to pass as to the function!!!) would be to read the source code of the swissskullstripper module. Any idea how to do that???</p>
<p>&lt;&gt;Desperate <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"> &lt;&gt;</p>
<p>Thank you all!</p>

---

## Post #7 by @lassoan (2017-05-17 19:00 UTC)

<p>We’ve updated SkullStripper, it should be very easy to use now.</p>
<p>Slicer <a href="https://discourse.slicer.org/t/its-2017-05-16-nightly-build-is-still-2017-05-09/323/7">download page doesn’t show the latest version</a> so you have to download the latest version of Slicer from the dashboard (small yellow icon in the Build Name column): <a href="http://slicer.cdash.org/index.php?project=Slicer4">http://slicer.cdash.org/index.php?project=Slicer4</a></p>

---

## Post #8 by @drAl (2017-05-17 19:24 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer download page doesn’t show the latest version so you have to download the latest version of Slicer from the dashboard (small yellow icon in the Build Name column): <a href="http://slicer.cdash.org/index.php" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>
</blockquote>
</aside>
<p>wow!!<br>
Ok, I’ll update the Slicer.<br>
I’m trying to write a script for the python console: do you know what do I need to define and how to invoke (parameters needed) the skullstripper module <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ???</p>
<p>Thanks in advance lassoan <img src="https://emoji.discourse-cdn.com/twitter/sunny.png?v=12" title=":sunny:" class="emoji" alt=":sunny:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2017-05-17 19:54 UTC)

<p>First use it from the GUI. Everything should be self-explaining. If not, then ask here.</p>
<p>If it works well, then follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">instructions for how to call a CLI from Python</a>.</p>

---

## Post #10 by @drAl (2017-05-17 20:29 UTC)

<p>hi again!</p>
<p>I appreciate the guidance…I already tested the GUI  -and the results are quite interesting. I’ve tested the stripping changing parameters for different sets of images and now I would like to set all this values from the command line. Thanks for linking again the “Running a CLI from Python” code. I assure you that I have almost learnt those lines…the problem is, as you might be already guessing, that the parameters required for the Skull Stripping are not “Input Volume” and “Output Geometry” (as shown in the linked example). That’s what I’m looking for…some kind of documentation about the use of this module.</p>
<p>Thanks lassoan. I really appreciate the time you’re taking to help me out. <img src="https://emoji.discourse-cdn.com/twitter/muscle.png?v=5" title=":muscle:" class="emoji" alt=":muscle:"> <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #11 by @jcfr (2017-05-17 22:09 UTC)

<aside class="quote no-group" data-username="drAl" data-post="10" data-topic="305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dral/48/176_2.png" class="avatar"> drAl:</div>
<blockquote>
<p>the problem is, as you might be already guessing, that the parameters required for the Skull Stripping are not “Input Volume” and “Output Geometry” (as shown in the linked example).</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>If not already done, consider looking at the module documentation, you can find there some example of atlases:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper</a></p>
<p>Looking at the description of its parameters could also be helpful:</p>
<p><a href="https://github.com/lorensen/SwissSkullStripperExtension/blob/master/SwissSkullStripper/SwissSkullStripper.xml" class="inline-onebox">SwissSkullStripperExtension/SwissSkullStripper/SwissSkullStripper.xml at master · lorensen/SwissSkullStripperExtension · GitHub</a></p>

---
