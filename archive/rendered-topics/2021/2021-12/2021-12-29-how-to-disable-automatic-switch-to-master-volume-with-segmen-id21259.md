# How to disable automatic switch to master volume with Segment editor

**Topic ID**: 21259
**Date**: 2021-12-29
**URL**: https://discourse.slicer.org/t/how-to-disable-automatic-switch-to-master-volume-with-segment-editor/21259

---

## Post #1 by @Michele_Bailo (2021-12-29 09:33 UTC)

<p><a href="/u/Michele_Bailo">ichele_Bailo</a><a href="/u/Michele_Bailo">MickyB</a></p>
<p><a href="/t/how-to-disable-the-automatic-switch-to-master-volume-with-segment-editor/21258?u=michele_bailo">1m</a></p>
<p>Hi there,<br>
I’m working with segmentations to be checked on multiple (eight) coregistered volumes that are simultaneously displayed in the layout. However, every time I change the master volume or I change the segmentation node it reset all the layout forcing me to reposition and relink over and over again all the different imaging series displayed. Is there a way to disable this automatic switch to the master volume? Would it perhaps be possible to easily select/deselect this option in the “Segment editor” module or in the “Application settings” panel?</p>
<p>Thank you very much for all you efforts and kindness!</p>

---

## Post #2 by @Michele_Bailo (2023-07-16 08:31 UTC)

<p>Hi, I’m still struggling with this problem (which make me waste sooooo much time every time I use Slicer) since I wasn’t able to solve it by myself.<br>
Do you have any suggestion on how to disable the autoshow of master volume node when you enter in the segment editor?<br>
thank you very much</p>

---

## Post #3 by @lassoan (2023-07-16 12:36 UTC)

<p>Automatic showing of the source volume is optional, but it is not commonly requested, so no graphical user interface was added for it. You can type this line into the Python console (or for changing it permanently, add it to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">application startup file</a>):</p>
<pre><code class="lang-python">slicer.util.getModuleWidget('SegmentEditor').editor.autoShowSourceVolumeNode = False
</code></pre>

---

## Post #4 by @lassoan (2023-07-16 12:52 UTC)

<p>I was wondering if it was possible for someone to figure it out that this option existed, so I have typed the subject title of this topic into bing chat and it provided a quite useful answer:</p>
<blockquote>
<p><a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html">You can disable automatic showing of the master volume in slice views by turning off <code>autoShowMasterVolumeNode</code> property of the segment editor widget</a><a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html">1</a>.</p>
<p>I hope that helps. Let me know if you have any other questions.</p>
</blockquote>
<p>It did not tell how to get the segment editor widget, so I asked <code>how to disable automatic switching of source volume in Segment Editor in 3D Slicer by Python scripting?</code></p>
<p>For this it provided a complete answer, although with a few lines of extra code (that did not do any harm but was not necessary).</p>
<hr>
<p>You can disable automatic switching of source volume in Segment Editor in 3D Slicer by Python scripting. You can turn off autoShowMasterVolumeNode property of the segment editor widget to disable automatic showing of the matter volume in slice views. The new master volume is only shown in those views where the segmentation node is visible (based on view node IDs set in the segmentation’display node)¹.</p>
<p>Here is an example of how to disable automatic switching of source volume in Segment Editor in 3D Slicer by Python scripting:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setAutoShowMasterVolumeNode(False)
</code></pre>
<p>I hope this helps! Let me know if you have any other questions.</p>
<p>¹: <a href="https://discourse.slicer.org/t/setting-segmentation-in-segmenteditor-without-changing-volumes-in-slice-views/22977">Setting segmentation in SegmentEditor without changing volumes in slice views - Support - 3D Slicer Community</a></p>
<p>Source: Conversation with Bing, 7/16/2023<br>
(1) Setting segmentation in SegmentEditor without … - 3D Slicer Community. <a href="https://discourse.slicer.org/t/setting-segmentation-in-segmenteditor-without-changing-volumes-in-slice-views/22977" class="inline-onebox">Setting segmentation in SegmentEditor without changing volumes in slice views</a>.<br>
(2) Segmentations — 3D Slicer documentation - Read the Docs. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="inline-onebox">Segmentations — 3D Slicer documentation</a>.<br>
(3) Slicer/segmenteditor.md at main · Slicer/Slicer · GitHub. <a href="https://github.com/Slicer/Slicer/blob/main/Docs/user_guide/modules/segmenteditor.md">https://github.com/Slicer/Slicer/blob/main/Docs/user_guide/modules/segmenteditor.md</a>.<br>
(4) Segment editor — 3D Slicer documentation - Read the Docs. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="inline-onebox">Segment editor — 3D Slicer documentation</a>.<br>
(5) How to disable automatic switch to master volume with Segment editor … <a href="https://discourse.slicer.org/t/how-to-disable-automatic-switch-to-master-volume-with-segment-editor/21259" class="inline-onebox">How to disable automatic switch to master volume with Segment editor</a>.</p>
<hr>

---

## Post #5 by @Michele_Bailo (2023-07-16 12:52 UTC)

<p>Thank you very, very much for your help. As a neurosurgeon I work a lot with multiple coregistered volumes, displaying them simultaneously, especially when planning procedures. Unfortunately every time I switched back to the segment editor my dataset view was reset back to the master volume, so I had to recreate my ideal view again and again again, losing a lot of time.</p>
<p>Thank you again a lot<br>
MB</p>

---

## Post #6 by @Michele_Bailo (2024-12-12 15:45 UTC)

<p>Hi,<br>
I have the same problem when a new scalar volume is added. In my clinical and research practice I regularly use 3D slicer to monitor brain diseases at different time-points. Unfortunately, every time I add (or create) a new scalar volume to the scene, Slicer resets all the layouts to display the new volume, forcing me to reposition and relink over and over again all the different imaging series displayed.<br>
Is there a simple way to disable the behavior of automatically switching layouts when a new scalar volume is loaded?<br>
Many many thanks for all you help.</p>

---

## Post #7 by @chir.set (2024-12-12 19:47 UTC)

<aside class="quote no-group" data-username="Michele_Bailo" data-post="6" data-topic="21259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michele_bailo/48/67234_2.png" class="avatar"> Michele_Bailo:</div>
<blockquote>
<p>when a new scalar volume is loaded</p>
</blockquote>
</aside>
<p>If you are loading from a file, in the ‘<code>Load data</code>’ dialog, the ‘<code>Show</code>’ option can be unchecked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/514d880353f4e247e2f9089831f470ad0b1ae070.png" data-download-href="/uploads/short-url/bBeMG7KMvSG0b2abbALdsnWLbuU.png?dl=1" title="load_data_options" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/514d880353f4e247e2f9089831f470ad0b1ae070_2_690x306.png" alt="load_data_options" data-base62-sha1="bBeMG7KMvSG0b2abbALdsnWLbuU" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/514d880353f4e247e2f9089831f470ad0b1ae070_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/514d880353f4e247e2f9089831f470ad0b1ae070_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/514d880353f4e247e2f9089831f470ad0b1ae070.png 2x" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">load_data_options</span><span class="informations">1080×480 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>‘<code>slicer.util.loadVolume()</code>’ does this in Python.<br>
Type ‘<code>help(loadVolume)</code>’ in the Python console for a description of this function.</p>

---

## Post #8 by @pieper (2024-12-12 20:05 UTC)

<p>Also you may find unchecking the options to reset field of view / reset origin helpful when comparing different MR contrasts.  Right click on the ‘eye’ icon in the data module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0f48ee485f2e5706a485ae7b58426855b65496c.png" data-download-href="/uploads/short-url/rwXDxHfTrfnnoBOVklaybnv8oPy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0f48ee485f2e5706a485ae7b58426855b65496c_2_690x211.png" alt="image" data-base62-sha1="rwXDxHfTrfnnoBOVklaybnv8oPy" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0f48ee485f2e5706a485ae7b58426855b65496c_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0f48ee485f2e5706a485ae7b58426855b65496c_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0f48ee485f2e5706a485ae7b58426855b65496c.png 2x" data-dominant-color="E2E7EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1298×398 64.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Michele_Bailo (2024-12-17 12:29 UTC)

<p>Many thanks for your help.<br>
Unfortunately, I usually import scalar volume from DICOM files, after directly retrieving them for my hospital’s PACS network system, and I don’t see that option there.<br>
I also tried the Python string you suggested but it did not seem to solve the issue (perhaps I am doing something incorrectly)</p>

---

## Post #10 by @pieper (2024-12-17 18:35 UTC)

<p>What I would typically do is load all the series of interest from the dicom module, and then use the Data module (with the orientation and field of view options unchecked) to switch between MR contrasts.  I also like to use the CompareVolumes module to create linked view layouts and also setting foreground/background settings for cross-fades.</p>

---

## Post #11 by @Michele_Bailo (2024-12-18 13:09 UTC)

<p>Thanks for the advice, I did not know about the possibility of unchecking orientation and field of view options, that certainly helps. However, it does not solve my problem completely, because if I have to import a new DICOM series of an MRI performed after 6 months of follow up in a pre-existing dataset of a patient, it will keep replacing all the existing layouts.</p>
<p>I used to be enthusiastic of the CompareModule feature, but I had to stop using it because it permanently engulfed the working memory and processing units once used in a specific Slicer dataset, as described in this previous post ( <a href="https://discourse.slicer.org/t/compare-volumes-module-display-order/31261/6">“Compare Volumes” module - display order - Support / Feature requests - 3D Slicer Community</a>)</p>

---

## Post #12 by @jamesobutler (2024-12-18 13:39 UTC)

<p><a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> It appears your Slicer issue (linked below) about the Compare module was closed after not receiving a response from you. Can you provide further information there? The issue could then be re-opened.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7522">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7522" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7522" target="_blank" rel="noopener nofollow ugc">“Compare volumes” module permanently engulf working memory and processing units once used in a specific Slicer dataset.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-05" data-time="10:39:27" data-timezone="UTC">10:39AM - 05 Jan 24 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2024-09-18" data-time="05:01:35" data-timezone="UTC">05:01AM - 18 Sep 24 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/bailom" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/69755212?v=4" class="onebox-avatar-inline" width="20" height="20">
          bailom
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I'm not a computer expert (I'm a clinician and medical researcher). I posted the<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> issue in Slicer community forum first (https://discourse.slicer.org/t/compare-volumes-module-display-order/31261/5) and was suggested to report the issue also here. I apologize if, perhaps, I'm not doing it in right way.

I have been using the “compare volumes” a lot in the last months (with different Slicer versions, including the latest updates).

Unfortunately, I noticed that in those datasets where I used this module at least once, things start to go extremely slow thereafter: even scrolling a single series in the Red view alone shows extreme “lagging”. The problem persists even if save and close the scene, reboot the pc (which is an incredibly powerful workstation with 128 GB DDR RAM and 12th Gen Intel Core i9-12900F, 2400 Mhz, 16 Cores, 24 Logical Processors; Windows 11 Pro) and reload the saved scene.

On the contrary, this problem does not occur when I “manually” set the same number of panels, such as a “4 by 3” or even “7 by 3” scenes, without using the “compare volumes” module.

My impression is that once the “compare volumes” module is utilized to display multiple views, it somehow keeps occupying a huge amount of resources, even if the additional view-panels are not shown anymore. It gets better again if I manually delete all the additional Slice-views created from the “Data”-&gt;”All Nodes” module.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
