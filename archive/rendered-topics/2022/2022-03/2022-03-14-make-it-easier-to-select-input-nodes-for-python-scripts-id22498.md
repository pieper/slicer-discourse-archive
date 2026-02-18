# Make it easier to select input nodes for Python scripts

**Topic ID**: 22498
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/make-it-easier-to-select-input-nodes-for-python-scripts/22498

---

## Post #1 by @lassoan (2022-03-14 16:03 UTC)

<p>While discussing a <a href="https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485">problem due to selecting the wrong input node in a Python script</a>, we started to brainstorm about how to make it easier to select input nodes for Python scripts.</p>
<p>The first idea was to <a href="https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485/6">change vtkMRMLScene::GetFirstNodeByName to return non-hidden node</a> by default.</p>
<p>Then <a class="mention" href="/u/pieper">@pieper</a> raised the idea of <a href="https://discourse.slicer.org/t/probevolumewithmodel-produces-wrong-output-in-code/22485/7">adding a <code>slicer.util.pickNode</code> method to show a popup where the user can select a node</a>.</p>
<p>I’ve created this topic to make this discussion more visible and get some more ideas and feedback from more developers.</p>

---

## Post #2 by @lassoan (2022-03-14 16:08 UTC)

<p>Adding a <code>pickNode</code> function could be useful, especially if it supported multiple nodes, each with a label and a default selection.</p>
<p>We could also consider <a class="mention" href="/u/pieper">@pieper</a>’s idea that came up some time ago: expose nodes as attribute of a Python object so that auto-complete could be used to look up nodes. It is nice that it also works in Jupyter notebooks.</p>
<p>I’ve implemented a very simple prototype - see a short demo:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc379691352af5cdf7e0e63c0e1976d7397ac9e2.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc379691352af5cdf7e0e63c0e1976d7397ac9e2.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc379691352af5cdf7e0e63c0e1976d7397ac9e2.mp4</a>
    </source></video>
  </div><p></p>
<p>Implementation:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L41-L73">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L41-L73" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L41-L73" target="_blank" rel="noopener">SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L41-L73</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
          <li>class Nodes(object):</li>
          <li>    """This object has MRML nodes in the slicer scene available as attributes.</li>
          <li>    The attribute name is generated from the node name, replacing invalid characters by underscore</li>
          <li>    and prepending `n` to node names that start with a number.</li>
          <li>    """</li>
          <li>    def __init__(self, ignoreHiddenNodes=True):</li>
          <li>        self.variableNameToId = {}</li>
          <li>        self.ignoreHiddenNodes = ignoreHiddenNodes</li>
          <li>    def __getattr__(self, name):</li>
          <li>        ''' will only get called for undefined attributes '''</li>
          <li>        return slicer.mrmlScene.GetNodeByID(self.variableNameToId[name])</li>
          <li>    @property</li>
          <li>    def __dict__(self):</li>
          <li>        import slicer</li>
          <li>        import re</li>
          <li>        attributes = {}</li>
          <li>        scene = slicer.mrmlScene</li>
          <li>        count = scene.GetNumberOfNodes()</li>
          <li>        for idx in range(count):</li>
          <li>            node = scene.GetNthNode(idx)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L41-L73" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>To try it, copy-paste all the highlighted lines into the Python console and then type this to make the nodes object conveniently available there as <code>n</code>:</p>
<pre><code class="lang-python">slicer.util.n = Nodes()
</code></pre>

---

## Post #3 by @pieper (2022-03-14 16:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve implemented a very simple prototype</p>
</blockquote>
</aside>
<p>Oh, I like that very much!</p>

---

## Post #4 by @mikebind (2022-03-14 18:04 UTC)

<p>I like it a lot also.  As your prototype acknowledges for spaces, might there be possible problems due to other non-letter characters?  Names of nodes can pretty much be arbitrary strings, right?  Leading numbers could be an issue (as is typical of DICOM imports which start with series number). Parentheses and brackets also aren’t allowed as part of attribute names.</p>
<p>Even with a simple and lossy solution like “replace any non-permitted character with an underscore”, I think this would be very helpful and I would use this all the time in the python interactor.</p>

---

## Post #5 by @rbumm (2022-03-14 20:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve implemented a very simple prototype</p>
</blockquote>
</aside>
<p>I am not so familiar with working directly in the interactor - would probably vote to have a picknode function or to have that auto-complete (which is cool)  be transferred into notepad++ or VS .<br>
Could we not just make a better error message if someone calls on a hidden input node?</p>

---

## Post #6 by @jamesobutler (2022-03-14 21:38 UTC)

<p>Just having a filter search tool for the Data module’s list of nodes would be helpful for me. That would allow easier finding the correct node name or node ID and then using Python to get that node reference. Maybe not the exact type of issue trying to be solved here, but in general it would allow for finding the node that I’m interested in getting a reference to for Python scripts.</p>
<p>I just discovered that this exists… Having the filter be above the table would be better as that is where I expected it to be. A filter above the table exists for the Segment table. Maybe a filter can be added for all Node tables.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17dc46a056e1c509c81555e7735999c5d4ca4a62.png" data-download-href="/uploads/short-url/3p4V5gEburXqgyojspWKCvwWrOa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17dc46a056e1c509c81555e7735999c5d4ca4a62.png" alt="image" data-base62-sha1="3p4V5gEburXqgyojspWKCvwWrOa" width="512" height="500" data-dominant-color="FBF8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">628×613 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88da9f461f6f72041f07f59c56ba0a7f27708187.png" alt="image" data-base62-sha1="jwFkzsOKhEAaXuuCsD5EHvYe0Xd" width="546" height="440"></p>

---

## Post #7 by @lassoan (2022-03-15 01:35 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>As your prototype acknowledges for spaces, might there be possible problems due to other non-letter characters? Names of nodes can pretty much be arbitrary strings, right?</p>
</blockquote>
</aside>
<p>Yes, Python variable names are restricted to a-z, A-Z, numbers, and underscore, starting with non-number. I’ve added a regexp to replace invalid characters by <code>_</code> and prepend an <code>n</code> if the name starts with number (starting with underscore would mean that it is a private attribute and it would be placed to the end of the auto-complete list).</p>
<p>As an experiment, I’ve added this feature to the DebuggingTools extension:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L24-L73">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L24-L73" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L24-L73" target="_blank" rel="noopener">SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L24-L73</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="24" style="counter-reset: li-counter 23 ;">
          <li>    slicer.app.connect("startupCompleted()", self.initializeNodesObject)</li>
          <li></li>
          <li>  def initializeNodesObject(self):</li>
          <li>    """Create nodes object and add it to the Python console's namespace.</li>
          <li>    It makes MRML nodes available in the Python console by autcomplete,by typing `n.` and pressing `Tab` key.</li>
          <li>    For example, the `MRHead` node becomes available in the Python console as `n.MRHead`.</li>
          <li>    """</li>
          <li>    # Create a Nodes object</li>
          <li>    slicer.nodes = Nodes()</li>
          <li>    # Make the object available in the Python console</li>
          <li>    pm = slicer.app.pythonManager()</li>
          <li>    pm.executeString("from slicer import nodes as n")</li>
          <li></li>
          <li>#</li>
          <li># Nodes object that makes all MRML nodes available as attribute.</li>
          <li>#</li>
          <li></li>
          <li>class Nodes(object):</li>
          <li>    """This object has MRML nodes in the slicer scene available as attributes.</li>
          <li>    The attribute name is generated from the node name, replacing invalid characters by underscore</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/e104b8d0d68f9623d9b878b98ba63976d5695e02/NodeInfo/NodeInfo.py#L24-L73" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The NodeInfo module adds a <code>nodes</code> variable in the global <code>slicer</code> namespace, which is available from everywhere. For user convenience, it also imports this variable as <code>n</code> in the Python console’s namespace.</p>
<p>In tomorrow’s Slicer Preview Release, <strong>if DebuggingTools extension is installed then typing <code>n.</code> in the Python console and hitting <code>Tab</code> key will allow selecting MRML nodes using auto-complete.</strong></p>
<p>Let’s see if it proves to be useful. If it does and it matures a bit then we may consider adding it to the Slicer core (maybe enabled just in developer mode).</p>
<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I am not so familiar with working directly in the interactor - would probably vote to have a picknode function or to have that auto-complete (which is cool) be transferred into notepad++ or VS</p>
</blockquote>
</aside>
<p>The nice thing in this auto-complete method that it works everywhere where you already have auto-complete - in Jupyter notebooks or any Python debugger (PyCharm, VS Code, etc.).</p>
<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Could we not just make a better error message if someone calls on a hidden input node?</p>
</blockquote>
</aside>
<p>Hidden nodes simply don’t show up, so I don’t think a special error message would be needed.<br>
Note that you can run <code>n.ignoreHiddenNodes=False</code> to show hidden nodes, too. But it mostly just makes color nodes show up in the list, making it harder to find what you need. Maybe we could display hidden nodes with a <code>_</code> prefix (it means private variable) if it turns out that access of hidden variables is useful.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I think this would be good and fairly safe compared to trying to add attributes of a class which could open a bunch of edge cases based on node name as indicated by <a class="mention" href="/u/mikebind">@mikebind</a>.</p>
</blockquote>
</aside>
<p>Invalid characters is easy to handle (see above). There are still complications, for example multiple nodes with the same name. However, accessing nodes as attributes is just a convenience function for interactive debugging, so it does not have to handle edge cases robustly (we have plenty of other ways to get nodes in a robust way).</p>
<p>I agree that a right-click menu for creating Python variable (initialized with the simplified node name, and potentially allowing the user to change it) could be useful. It would be also easy to implement because it could be added via a scripted subject hierarchy plugin.</p>
<p>The right-click menu in the subject hierarchy tree is probably more convenient when you have dozens or more nodes in the scene (or you have already found your node of interest in the tree), while <code>n.NodeName</code> is more convenient if you work in the console and you already have an idea of the node name or you don’t have too many nodes.</p>

---

## Post #8 by @jamesobutler (2022-03-15 02:00 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Locating nodes in the data tree could help if we added a right-click menu to create a Python variable for the selected node</p>
</blockquote>
</aside>
<p>I think this would be good and fairly safe compared to trying to add attributes of a class which could open a bunch of edge cases based on node name as indicated by <a class="mention" href="/u/mikebind">@mikebind</a>. The right click would just create a reference using a simple variable name like volume_node or something or let the user define the variable themselves.</p>

---

## Post #9 by @pieper (2022-03-17 18:09 UTC)

<p>I agree node names are very free-form text, but I think it would be really useful to be able to tab complete them in the python console and it’s okay to map non-identifier-friendly characters to _.</p>
<p>It could also be cool to add a ways of getting python access to data based on the state of the gui.  For example <code>slicer.gui.views.red.background</code> could give you the node currently displayed in the background of the red viewer.  Tab completing <code>slicer.gui.views</code> which give you the list of view ids that you could quickly pick.  Something like <code>slicer.gui.data.selection</code> could give you the currently selected node from the data module.  This kind of access could be pretty easy to add with custom <code>__getattr__</code> code.</p>

---

## Post #10 by @lassoan (2022-03-18 14:19 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="22498">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It could also be cool to add a ways of getting python access to data based on the state of the gui.</p>
</blockquote>
</aside>
<p>This is a very interesting idea, it would result in kind of a “macro language” for Slicer programming. Do you envision this could be used in module development or just for automation scripts?</p>
<p>Macro scripts could be generated by <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/SceneRecorder">MRML-based event recording</a> or QtTesting-based recording.</p>

---
