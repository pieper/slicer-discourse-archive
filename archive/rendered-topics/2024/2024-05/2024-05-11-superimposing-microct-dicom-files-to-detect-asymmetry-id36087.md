# Superimposing MicroCT DICOM files to detect Asymmetry 

**Topic ID**: 36087
**Date**: 2024-05-11
**URL**: https://discourse.slicer.org/t/superimposing-microct-dicom-files-to-detect-asymmetry/36087

---

## Post #1 by @NeginRz (2024-05-11 15:56 UTC)

<p>Hi! I am working on a project where we placed appliances on the maxillary teeth of rats in an effort to constrict the maxillary jaw. I made 3D reconstruction of my models in Amira. I would like to merge all my control models into 1 model and then compare every experimental model to the control and see if the appliance resulted in any asymmetry rather than just comparing the width of the maxilla. Does the 3D slicer software have the ability to help me with that? and if yes would you mind guiding me on how I can do that?</p>
<p>Thank you very much for your help and look forward to hearing form you soon.</p>

---

## Post #2 by @muratmaga (2024-05-12 02:20 UTC)

<aside class="quote no-group" data-username="NeginRz" data-post="1" data-topic="36087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neginrz/48/76718_2.png" class="avatar"> NeginRz:</div>
<blockquote>
<p>I would like to merge all my control models into 1 model</p>
</blockquote>
</aside>
<p>Do you mean like creating an average model as reference?</p>
<p>In any event, you would probably find the DeCA tool useful for your needs. It does require an initial set of landmarks to do initial alignment, but then you can create an average model out of controls, and then visualize the difference in your treatment group.</p>
<p>You can find the chapter here: <a href="https://www.researchgate.net/publication/375111739_DeCA_A_Dense_Correspondence_Analysis_Toolkit_for_Shape_Analysis">https://www.researchgate.net/publication/375111739_DeCA_A_Dense_Correspondence_Analysis_Toolkit_for_Shape_Analysis</a></p>
<p>At this point you need to manually install the extension from: <a href="https://github.com/smrolfe/DeCa" class="inline-onebox">GitHub - smrolfe/DeCA: Dense Correspondence Analysis (DeCA) toolkit</a>.</p>

---

## Post #3 by @NeginRz (2024-05-12 14:18 UTC)

<p>Is there a way that I can schedule a video call to get a tutorial for ALPACA and DeCA?</p>

---

## Post #4 by @muratmaga (2024-05-12 16:13 UTC)

<p>If you have questions, you can join our SlicerMorph online user check-ins, 4th thursday of the month at 11 (PT).<br>
Next one is on May 28th.</p>

---

## Post #5 by @NeginRz (2024-06-18 16:28 UTC)

<p>Hey! Thank you so much for your advice. I’m trying to add the DeCa extension on 3D Slicer, but I can’t seem to find it in the “Extension Manager.” I also checked the link in the article you provided, but still had no luck. Could you help me figure out how to install this extension on 3D Slicer?</p>

---

## Post #6 by @LeidyMoraV (2024-06-18 17:26 UTC)

<p>You need to manually install the extension as Murat explained before:</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="36087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>At this point you need to manually install the extension from: <a href="https://github.com/smrolfe/DeCa" rel="noopener nofollow ugc">GitHub - smrolfe/DeCA: Dense Correspondence Analysis (DeCA) toolkit</a>.</p>
</blockquote>
</aside>

---

## Post #7 by @NeginRz (2024-06-18 18:28 UTC)

<p>I understand but I do not know how to install manually an dI was wondering if I could get guidance on how I need to do that.</p>

---

## Post #8 by @LeidyMoraV (2024-06-18 18:40 UTC)

<p>I guess you can do something like this:</p>
<ol>
<li>Clone or download the repository as a ZIP file</li>
<li>Extract all files</li>
<li>Go to DeCA_global-main &gt; DeCa</li>
</ol>
<p>Using Slicer:</p>
<ol>
<li>Go to Edit &gt; Application Settings</li>
<li>Under the ‘Modules’ drag and drop the DeCa folder</li>
<li>Restart Slicer</li>
</ol>
<p>Look for the module ‘DeCA Toolbox’ under the ‘Module Selection’ list or find the module ‘DeCA’</p>

---

## Post #9 by @muratmaga (2024-06-18 18:40 UTC)

<p>Go to the github repository link above, download the repo as a zip file (green CODE button, then choose download zip).</p>
<p>Then follow the instruction here on how to manually install extension packages:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection</a></p>
<p>Alternatively, you can also use the Extension Wizard module and choose “Select Extension”<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html</a></p>

---

## Post #10 by @NeginRz (2024-06-18 20:36 UTC)

<p>Thank you so much for your help. I am excited to let you know that I was able to get the rigid alignment using the DeCa toolkit; however, when trying to use the Dense correspondence I/O the software keeps crashing and its not responding. I was wondering if you have a solution for that as well.</p>
<p>I truly appreciate your help and guidance. It means a lot.</p>

---

## Post #11 by @muratmaga (2024-06-19 04:43 UTC)

<p>Can you provide the log file from the crash? Without that we can’t be able to help you much.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---
