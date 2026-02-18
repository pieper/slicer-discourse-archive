# Training Segmentation Model with Custom Labels in MonaILabel

**Topic ID**: 32152
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/training-segmentation-model-with-custom-labels-in-monailabel/32152

---

## Post #1 by @FWSU (2023-10-11 08:02 UTC)

<p>I am looking to train a segmentation model using MonaILabel. However, instead of using the pre-existing labels such as (‘kidney_left’, ‘kidney_right’, etc.), I want to use custom labels (‘label1’, ‘label2’, ‘label3’).</p>
<p>My dataset already has segmentation maps defined.(had 3 labels) Could you guide me on how I can train the provided segmentation model in MonaILabel with these new labels?</p>
<p>If there are any related documents or resources that could help me understand this process better, please do share them.</p>

---

## Post #2 by @rbumm (2023-10-11 13:10 UTC)

<p>There are several good training videos of <a class="mention" href="/u/diazandr3s">@diazandr3s</a> available.<br>
Here is one at the timeframe where it is shown how to set your own labels.<br>
As MONAILabel is always expanding and prone to change, you might need to re-ask.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="3HTh2dqZqew" data-video-title="MONAI Label - Training from Scratch" data-video-start-time="43" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=3HTh2dqZqew&amp;t=43" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/3HTh2dqZqew/maxresdefault.jpg" title="MONAI Label - Training from Scratch" width="" height="">
  </a>
</div>


---

## Post #3 by @muratmaga (2023-10-11 19:01 UTC)

<aside class="quote no-group" data-username="FWSU" data-post="1" data-topic="32152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fwsu/48/67257_2.png" class="avatar"> FWSU:</div>
<blockquote>
<p>I want to use custom labels (‘label1’, ‘label2’, ‘label3’).</p>
</blockquote>
</aside>
<p>Assuming you are planning to use deepedit.py, you need to change these lines to match your labels. However, I would advise against changing them to label_1, label_2, but instead use proper names of what they are…</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/blob/d4209ce0026584ee8316bdeb48c5249fc3f781c9/sample-apps/radiology/lib/configs/deepedit.py#L41">
  <header class="source">

      <a href="https://github.com/Project-MONAI/MONAILabel/blob/d4209ce0026584ee8316bdeb48c5249fc3f781c9/sample-apps/radiology/lib/configs/deepedit.py#L41" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Project-MONAI/MONAILabel/blob/d4209ce0026584ee8316bdeb48c5249fc3f781c9/sample-apps/radiology/lib/configs/deepedit.py#L41" target="_blank" rel="noopener">Project-MONAI/MONAILabel/blob/d4209ce0026584ee8316bdeb48c5249fc3f781c9/sample-apps/radiology/lib/configs/deepedit.py#L41</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="31" style="counter-reset: li-counter 30 ;">
          <li>logger = logging.getLogger(__name__)</li>
          <li></li>
          <li></li>
          <li>class DeepEdit(TaskConfig):</li>
          <li>    def init(self, name: str, model_dir: str, conf: Dict[str, str], planner: Any, **kwargs):</li>
          <li>        super().init(name, model_dir, conf, planner, **kwargs)</li>
          <li></li>
          <li>        self.epistemic_enabled = None</li>
          <li>        self.epistemic_samples = None</li>
          <li></li>
          <li class="selected">        # Multilabel</li>
          <li>        self.labels = {</li>
          <li>            "spleen": 1,</li>
          <li>            "right kidney": 2,</li>
          <li>            "left kidney": 3,</li>
          <li>            "liver": 6,</li>
          <li>            "stomach": 7,</li>
          <li>            "aorta": 8,</li>
          <li>            "inferior vena cava": 9,</li>
          <li>            "background": 0,</li>
          <li>        }</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
