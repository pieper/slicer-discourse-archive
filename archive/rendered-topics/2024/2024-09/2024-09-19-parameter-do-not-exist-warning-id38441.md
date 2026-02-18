# Parameter do not exist warning

**Topic ID**: 38441
**Date**: 2024-09-19
**URL**: https://discourse.slicer.org/t/parameter-do-not-exist-warning/38441

---

## Post #1 by @bserrano (2024-09-19 11:36 UTC)

<p>Hi all,</p>
<p>I have a script for automating scalar volume resampling:</p>
<pre><code class="lang-auto">reslicedVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", name)
    parameters = {
        "outputPixelSpacing":"{:},{:},{:}".format(*[resolution]*3),
        "InputVolume":volumeNode.GetID(),
        "interpolationMode":'bspline',
        "referenceVolume": volumeNode.GetID(),
        "OutputVolume":reslicedVolumeNode.GetID()}
    
    cliNode = slicer.cli.runSync(slicer.modules.resamplescalarvolume, None, parameters)
</code></pre>
<p>After many experiments, I discovered that the parameter <code>interpolationMode</code> should actually be <code>interpolationType</code>. However, no error or warning is displayed, so I was unintentionally using the default ‘linear’ interpolation instead of ‘bspline’. Is it possible to implement a warning message to help avoid this kind of mistake? It was quite difficult to debug.<br>
I guess that the same happens with other modules as well.</p>
<p>Many thanks.</p>

---

## Post #2 by @chir.set (2024-09-19 12:25 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="38441">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Is it possible to implement a warning message to help avoid this kind of mistake?</p>
</blockquote>
</aside>
<p>I think that your request cannot be fulfilled (by the relevant developer).</p>
<p>You are basically passing a arbitrary field ‘interpolationMode’ that the reader is not looking for. Unless it checks all keys, it won’t react to unknown inputs. It’s doubtful developers would add an overhead to their code.</p>
<p>If someone else passes in a key type of - “Greetings” : ‘Coucou’ - why should the reader check for this key?</p>
<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="38441">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>It was quite difficult to debug.</p>
</blockquote>
</aside>
<p>Check available keys and values in 'lib/Slicer-5.7/cli-modules/ResampleScalarVolume.xml<br>
'.</p>

---
