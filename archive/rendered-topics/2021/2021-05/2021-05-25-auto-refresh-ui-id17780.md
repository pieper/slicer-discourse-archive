# Auto Refresh UI

**Topic ID**: 17780
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/auto-refresh-ui/17780

---

## Post #1 by @SachidanandAlle (2021-05-25 00:40 UTC)

<p>Train task run in server.<br>
Periodically I would like to trigger a status check and update some UI button.</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L184-L186" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L184-L186" target="_blank" rel="noopener nofollow ugc">Project-MONAI/MONAILabel/blob/main/plugins/slicer/MONAILabel/MONAILabel.py#L184-L186</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="184" style="counter-reset: li-counter 183 ;">
          <li>self.ui.trainingButton.connect("clicked(bool)", self.onTraining)</li>
          <li>self.ui.stopTrainingButton.connect("clicked(bool)", self.onStopTraining)</li>
          <li>self.ui.trainingStatusButton.connect("clicked(bool)", self.onTrainingStatus)</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Basically I have Train start, status_check and stop buttons<br>
When I click start… we switch and enable stop button.  After sometime the actual training is finished.</p>
<p>However server provides a method to query the status.  How to do it behind the scene… I mean how to simulate the behaviour of auto click for status button for every N seconds.</p>

---

## Post #2 by @lassoan (2021-05-25 03:29 UTC)

<p>You can set up a QTimer to run a method periodically. See for example in Endoscopy module:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/d421cacd00045aee27edc164a5f71bc650b2361b/Modules/Scripted/Endoscopy/Endoscopy.py#L57-L59" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d421cacd00045aee27edc164a5f71bc650b2361b/Modules/Scripted/Endoscopy/Endoscopy.py#L57-L59" target="_blank" rel="noopener">Slicer/Slicer/blob/d421cacd00045aee27edc164a5f71bc650b2361b/Modules/Scripted/Endoscopy/Endoscopy.py#L57-L59</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="57" style="counter-reset: li-counter 56 ;">
          <li>self.timer = qt.QTimer()</li>
          <li>self.timer.setInterval(20)</li>
          <li>self.timer.connect('timeout()', self.flyToNext)</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
