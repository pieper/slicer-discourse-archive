# Print dataprobe text with shift key

**Topic ID**: 21331
**Date**: 2022-01-04
**URL**: https://discourse.slicer.org/t/print-dataprobe-text-with-shift-key/21331

---

## Post #1 by @mau_igna_06 (2022-01-04 21:32 UTC)

<p>I would like to print the background scalarVolume value where the crosshair is when it is repositioned with Shift key.</p>
<p>Here is my code, it doesn’t work:</p>
<pre><code class="lang-auto">def probeBackgroundVolumeOverMouse():
    infoWidget = slicer.modules.DataProbeInstance.infoWidget
    if infoWidget.layerValues['B'].text == '':
        return
    #
    cleanedTextOfDataProbe = infoWidget.layerValues['B'].text.split('&lt;b&gt;')[1].split('&lt;/b&gt;')[0]
    #
    if cleanedTextOfDataProbe.isdecimal():
        print(cleanedTextOfDataProbe)
    elif cleanedTextOfDataProbe[1:].isdecimal():
        print(cleanedTextOfDataProbe)


shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence('Shift')) #this doesn't work
#shortcut.setKey(qt.QKeySequence('.')) #this does work
shortcut.activated.connect(probeBackgroundVolumeOverMouse)
</code></pre>
<p>I guess there is some conflict because the Shift key is already used.</p>
<p>Really I’m just trying to get the value of the scalarVolume where the crosshair is. This is the first method that came to my mind but others are welcomed. Although retrieving the value using the Shift key is very important so it keeps it simple for the user.</p>

---

## Post #2 by @jamesobutler (2022-01-04 23:52 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="21331">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Really I’m just trying to get the value of the scalarVolume where the crosshair is.</p>
</blockquote>
</aside>
<p>So you’re trying to replicate the DataProbe module? Do you not want this updated value on the cursor position moved event? The DataProbe module gets this value by doing the following:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/ae608a672b49d3fd11efef89f7a2a425f11e11a3/Modules/Scripted/DataProbe/DataProbe.py#L99">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/ae608a672b49d3fd11efef89f7a2a425f11e11a3/Modules/Scripted/DataProbe/DataProbe.py#L99" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ae608a672b49d3fd11efef89f7a2a425f11e11a3/Modules/Scripted/DataProbe/DataProbe.py#L99" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/ae608a672b49d3fd11efef89f7a2a425f11e11a3/Modules/Scripted/DataProbe/DataProbe.py#L99</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="89" style="counter-reset: li-counter 88 ;">
          <li>  self.pen = qt.QPen()</li>
          <li></li>
          <li>  self._createSmall()</li>
          <li></li>
          <li>  #Helper class to calculate and display tensor scalars</li>
          <li>  self.calculateTensorScalars = CalculateTensorScalars()</li>
          <li></li>
          <li>  # Observe the crosshair node to get the current cursor position</li>
          <li>  self.CrosshairNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLCrosshairNode')</li>
          <li>  if self.CrosshairNode:</li>
          <li class="selected">    self.CrosshairNodeObserverTag = self.CrosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.processEvent)</li>
          <li></li>
          <li></li>
          <li>def __del__(self):</li>
          <li>  self.removeObservers()</li>
          <li></li>
          <li>def fitName(self,name,nameSize=None):</li>
          <li>  if not nameSize:</li>
          <li>    nameSize = self.nameSize</li>
          <li>  if len(name) &gt; nameSize:</li>
          <li>    preSize = int(nameSize / 2)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mau_igna_06 (2022-01-05 00:35 UTC)

<p>Thanks. That’s very useful</p>

---

## Post #4 by @mau_igna_06 (2022-01-05 12:53 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. I’ve got to reuse the code of the dataProbe but I still cannot execute my function on shift key press. Is this reacheable in Python? I was able to detect them on the sliceInteractor but I would prefer them to be detected on the mainWindow because sliceInteractor doesn’t react if it is not “selected” (i.e. it hasn’t been clicked inside)</p>

---

## Post #5 by @jamesobutler (2022-01-05 13:08 UTC)

<p>I tried but just using the shift key did not work for me.</p>

---

## Post #6 by @mau_igna_06 (2022-01-05 13:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Do you have any suggestions on how to execute a callback by pressing the shiftkey? Is it possible on Python? Ideally the callback would be called multiple times while shift is still pressed.</p>

---

## Post #7 by @jamesobutler (2022-01-05 13:15 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="21331">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Ideally the callback would be called multiple times while shift is still pressed.</p>
</blockquote>
</aside>
<p>All of this I don’t think will work. This all sounds like a mouse move event as is done already with the DataProbe module.</p>

---

## Post #8 by @mau_igna_06 (2022-01-05 13:24 UTC)

<p>One call per press would be fine anyway.</p>
<p>I presented a simplified version of my problem. I need to use the sampled HU value as input for a process of the logic.</p>

---

## Post #9 by @lassoan (2022-01-05 14:27 UTC)

<p>Crosshair node is intended for continuous sampling. For taking discrete samples I would recommend to use markup points node. If you don’t want to allow your users to change the input points then you can immediately hide or delete the point after it has been placed.</p>

---
