---
topic_id: 21844
title: "How To Access Dicom Widget Components"
date: 2022-02-07
url: https://discourse.slicer.org/t/21844
---

# How to access dicom widget components

**Topic ID**: 21844
**Date**: 2022-02-07
**URL**: https://discourse.slicer.org/t/how-to-access-dicom-widget-components/21844

---

## Post #1 by @Dwij_Mistry (2022-02-07 19:40 UTC)

<p>How to access DICOM widget from Home / other module<br>
<strong>slicer.modules.DICOMWidget.ui.label_5.hide()</strong></p>
<p>Scenario: when we are starting a Slicer by default all module are not available in the Memory,<br>
In our scenario we are starting a Slicer with Home module in which we are trying to hide the DICOM module’s not required components. by using code like this <strong>slicer.modules.DICOMWidget.ui.label_5.hide()</strong> .</p>
<p>What is the correct way to access the other module components in the selected module. OR How we can achieve this.</p>

---

## Post #2 by @lassoan (2022-02-08 20:29 UTC)

<p>One option is to instantiate the DICOM module widget and modify its components. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">dicomModuleWidget = slicer.util.getModuleGui('DICOM')
dicomModuleWidget.ui.dicomPluginsFrame.hide()
</code></pre>
<p>If there is anything that it is not trivial to change or not exposed nicely then please send a pull request or start a discussion about it here. For example, <code>label_5</code> is just a default widget name that can be renamed anytime to a proper meaningful name and then your code will not work anymore, therefore if you want to hide this label then it should be renamed to <code>labelLoadedData</code> or something similar.</p>
<aside class="quote no-group" data-username="Dwij_Mistry" data-post="1" data-topic="21844">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dwij_mistry/48/15265_2.png" class="avatar"> Dwij_Mistry:</div>
<blockquote>
<p>when we are starting a Slicer by default all module are not available in the Memory</p>
</blockquote>
</aside>
<p>Modules are loaded in random order during application startup and then initialized based on an order determined from dependencies that each module declare. If you want to use any module from a Python scripted module then the simplest is to wait for the <code>slicer.app.startupCompleted()</code> signal.</p>

---

## Post #3 by @Dwij_Mistry (2022-02-09 06:42 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a>  for your response.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21844">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">dicomModuleWidget = slicer.util.getModuleGui('DICOM')
dicomModuleWidget.ui.dicomPluginsFrame.hide()
</code></pre>
</blockquote>
</aside>
<p>this is exactly what I was looking for.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21844">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If there is anything that it is not trivial to change or not exposed nicely then please send a pull request or start a discussion about it here</p>
</blockquote>
</aside>
<p>Yes sure, I found following labels name which we can change to something meaningful in the DICOM module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a653320753ef13ee9335499ed597897c58a1ce32.png" data-download-href="/uploads/short-url/nJnvl1qVr0vtHX2fDejqm7YUb1E.png?dl=1" title="Screenshot (88)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a653320753ef13ee9335499ed597897c58a1ce32.png" alt="Screenshot (88)" data-base62-sha1="nJnvl1qVr0vtHX2fDejqm7YUb1E" width="486" height="500" data-dominant-color="ADACAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (88)</span><span class="informations">673×691 18.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center">existing label name</th>
<th style="text-align:center">Proposed label name</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">label_5</td>
<td style="text-align:center">labelLoadedData</td>
</tr>
<tr>
<td style="text-align:center">label</td>
<td style="text-align:center">labelPullDataFromRemoteServer</td>
</tr>
<tr>
<td style="text-align:center">label_6</td>
<td style="text-align:center">labelStorageListener</td>
</tr>
<tr>
<td style="text-align:center">labe_7</td>
<td style="text-align:center">labelStartStorageListenerOnStartup</td>
</tr>
<tr>
<td style="text-align:center">label_8</td>
<td style="text-align:center">labelDatabaseLocation</td>
</tr>
<tr>
<td style="text-align:center">label_9</td>
<td style="text-align:center">labelAutoHideBrowserWindow</td>
</tr>
<tr>
<td style="text-align:center">label_10</td>
<td style="text-align:center">labelMaintenance</td>
</tr>
</tbody>
</table>
</div>

---

## Post #4 by @lassoan (2022-02-09 14:08 UTC)

<p>Please send a pull request with the suggested name changes.</p>
<p>Is the reason for accessing the labels that you want to hide them? If yes, then we could add API to show/hide entire sections. If you just want to rename or rearrange options (because they are not intuitive or convenient enough) then it might be better to make those changes directly in Slicer core.</p>

---

## Post #5 by @Dwij_Mistry (2022-02-09 15:26 UTC)

<p>Yes pull request created <a href="https://github.com/Slicer/Slicer/pull/6171" class="inline-onebox" rel="noopener nofollow ugc">ENH: given meaningful names to labels by dwijmistry11 · Pull Request #6171 · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="21844">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you just want to rename or rearrange options (because they are not intuitive or convenient enough) then it might be better to make those changes directly in Slicer core.</p>
</blockquote>
</aside>
<p>We resoled this issue by creating clone of DICOM module in the template; in which we hide the non frequently used part.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="21844">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is the reason for accessing the labels that you want to hide them?</p>
</blockquote>
</aside>
<p>We can have a Setting tab or something like that, to reduce complexity.<br>
But in latest release those all settings are having expandable and collapsable section.</p>

---

## Post #6 by @jamesobutler (2022-02-09 15:36 UTC)

<p>Maybe all the remote server stuff should be in an “Advanced” section of some sort with the focus on local import.</p>

---
