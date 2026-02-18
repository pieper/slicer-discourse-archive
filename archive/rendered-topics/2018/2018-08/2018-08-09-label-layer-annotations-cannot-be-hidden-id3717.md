# Label layer annotations cannot be hidden

**Topic ID**: 3717
**Date**: 2018-08-09
**URL**: https://discourse.slicer.org/t/label-layer-annotations-cannot-be-hidden/3717

---

## Post #1 by @Fernando (2018-08-09 16:48 UTC)

<p>Hi all,</p>
<p>When I uncheck the <code>Bottom Left</code> checkbox in the Data Probe module, only annotations for background and foreground layers are hidden, but the one for the label layer stays.</p>
<p>There must be something wrong in <code>Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py</code>, but I haven’t been able to spot it.</p>
<p>I’ve tried getting the widget and doing <code>widget.sliceView().cornerAnnotation().SetText(0, '')</code> with no luck.</p>

---

## Post #2 by @pieper (2018-08-09 21:37 UTC)

<p>Hi Fernando -</p>
<p>It looks like <code>if self.bottomLeft:</code> needs to be added before the block at line 631.  Let me know if that fixes it for you and I can make the change.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L617-L635" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L617-L635" target="_blank">Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L617-L635</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="617" style="counter-reset: li-counter 616 ;">
<li>  if self.bottomLeft:</li>
<li>    foregroundVolumeName = foregroundVolume.GetName()</li>
<li>    self.cornerTexts[0]['2-Foreground']['text'] = 'F: ' + foregroundVolumeName</li>
<li>
</li>
<li>  uids = foregroundVolume.GetAttribute('DICOM.instanceUIDs')</li>
<li>  if uids:</li>
<li>    uid = uids.partition(' ')[0]</li>
<li>    # passed UID as bg</li>
<li>    self.makeDicomAnnotation(uid,None,sliceViewName)</li>
<li>    self.dicomVolumeNode = 1</li>
<li>  else:</li>
<li>    self.dicomVolumeNode = 0</li>
<li>
</li>
<li>if (labelVolume is not None):</li>
<li>  labelOpacity = sliceCompositeNode.GetLabelOpacity()</li>
<li>  labelVolumeName = labelVolume.GetName()</li>
<li>  self.cornerTexts[0]['1-Label']['text'] = 'L: ' + labelVolumeName + ' (' + str(</li>
<li>           "%d"%(labelOpacity*100)) + '%)'</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Fernando (2018-08-09 22:40 UTC)

<p>Hi Steve <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=5" title=":wave:" class="emoji" alt=":wave:"></p>
<p>Thanks for your answer, that worked.</p>
<p>You’ll need another <code>if self.bottomLeft:</code> for Case I, it doesn’t work either.<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L576-L599" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L576-L599" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L576-L599</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="576" style="counter-reset: li-counter 575 ;">
<li># Case I: Both background and foregraound</li>
<li>if ( backgroundVolume is not None and foregroundVolume is not None):</li>
<li>  foregroundOpacity = sliceCompositeNode.GetForegroundOpacity()</li>
<li>  backgroundVolumeName = backgroundVolume.GetName()</li>
<li>  foregroundVolumeName = foregroundVolume.GetName()</li>
<li>  self.cornerTexts[0]['3-Background']['text'] = 'B: ' + backgroundVolumeName</li>
<li>  self.cornerTexts[0]['2-Foreground']['text'] = 'F: ' + foregroundVolumeName +  ' (' + str(</li>
<li>           "%d"%(foregroundOpacity*100)) + '%)'</li>
<li>
</li>
<li>  bgUids = backgroundVolume.GetAttribute('DICOM.instanceUIDs')</li>
<li>  fgUids = foregroundVolume.GetAttribute('DICOM.instanceUIDs')</li>
<li>  if (bgUids and fgUids):</li>
<li>    bgUid = bgUids.partition(' ')[0]</li>
<li>    fgUid = fgUids.partition(' ')[0]</li>
<li>    self.dicomVolumeNode = 1</li>
<li>    self.makeDicomAnnotation(bgUid,fgUid,sliceViewName)</li>
<li>  elif (bgUids and self.backgroundDICOMAnnotationsPersistence):</li>
<li>    uid = bgUids.partition(' ')[0]</li>
<li>    self.dicomVolumeNode = 1</li>
<li>    self.makeDicomAnnotation(uid,None,sliceViewName)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/5e88dcc9aa3e543bdaf37c983132cf4bc5f9edf2/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L576-L599" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @Fernando (2018-08-10 19:48 UTC)

<p>I have submitted a PR:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1004">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1004" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1004" target="_blank" rel="noopener nofollow ugc">3D Viewer disapears after loading in MRML file</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:35:59" data-timezone="UTC">10:35PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:36:00" data-timezone="UTC">10:36PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener nofollow ugc">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1004). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @pieper (2018-08-10 20:00 UTC)

<p>Great! I"m just rebuilding now for a quick test and will commit.</p>

---

## Post #6 by @lassoan (2023-03-21 03:01 UTC)



---
