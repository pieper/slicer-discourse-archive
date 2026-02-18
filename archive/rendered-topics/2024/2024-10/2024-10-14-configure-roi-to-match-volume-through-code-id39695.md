# Configure ROI to match volume through code

**Topic ID**: 39695
**Date**: 2024-10-14
**URL**: https://discourse.slicer.org/t/configure-roi-to-match-volume-through-code/39695

---

## Post #1 by @shai-ikko (2024-10-14 15:20 UTC)

<p>Hi,</p>
<p>I’m trying to use a ROI markup to designate a rotation transform (I don’t want an actual transform because reasons). I initially configure the ROI as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume" rel="noopener nofollow ugc">recommended in the script repository</a>. The problem is that this seems to create a “fragile” ROI – there is something funny going on between its <code>ObjectToNodeMatrix</code> and <code>ObjectToWorldMatrix</code>, and as a result, any further attempt to modify it via code throws it aside (the image origin is not at 0,0,0).</p>
<p>More details:</p>
<p>Right after running the code from the repository, if I pick up the ROI:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; nodes = slicer.mrmlScene.GetNodesByClass("vtkMRMLMarkupsROINode")
&gt;&gt;&gt; roi = nodes.GetItemAsObject(0)
</code></pre>
<p>And look at its matrices (some unimportant details removed)</p>
<pre><code class="lang-auto">&gt;&gt;&gt; print(roi.GetObjectToNodeMatrix())
    1 0 0 -64.8817 
    0 1 0 -65.6043 
    0 0 1 81.1599 
    0 0 0 1 
&gt;&gt;&gt; print(roi.GetObjectToWorldMatrix())
    1 0 0 -64.8817 
    0 1 0 -65.6043 
    0 0 1 81.1599 
    0 0 0 1 
</code></pre>
<p>But if now I trigger computations (which apparently should have happened) – without otherwise touching anything –</p>
<pre><code class="lang-auto">&gt;&gt;&gt; roi.GetObjectToNodeMatrix().Modified()
</code></pre>
<p>Then I can already see the ROI jump. If I now repeat the above, the <code>ObjectToNodeMatrix</code> looks the same, but</p>
<pre><code class="lang-auto">&gt;&gt;&gt; print(roi.GetObjectToWorldMatrix())
    1 0 0 0 
    0 1 0 0 
    0 0 1 0 
    0 0 0 1 
</code></pre>
<p>Is this as intended? Am I doing something wrong?</p>
<p>(Just to be on the safe side – in my code, I also set up two display nodes for the ROI, and turn interaction controls on and off, but I don’t think that should affect the translation matrices in any way)</p>
<p>Thanks!</p>

---
