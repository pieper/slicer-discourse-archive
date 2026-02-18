# Problems listening to vtkMRMLCommandLineNode events from loadable module

**Topic ID**: 2711
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/problems-listening-to-vtkmrmlcommandlinenode-events-from-loadable-module/2711

---

## Post #1 by @Sam_Horvath (2018-04-26 20:27 UTC)

<p>Hi all:</p>
<p>I am working on a loadable module that does background processing using CLIs.  I am connecting callback functions in the widget to the end of the CLI processing using qvtkReconnect (as shown):</p>
<pre><code>    qvtkReconnect(d-&gt;cmdNode, vtkMRMLCommandLineModuleNode::StatusModifiedEvent, 
    this,SLOT(finishWrap()));
</code></pre>
<p>Unfortunately, I am running into access violation errors in vtkObject when it tries to process the StatusModified Event when the CLI is completed.  This exception occurs in:</p>
<p><code>vtkSubjectHelper::InvokeEvent(unsigned long event, void *callData,vtkObject *self)</code></p>
<p>at line 601.  It appears that one of the observers linked to the node is bad/invalid, but I do not know how it happens.  Nothing is being done with the node between invoking the CLI and picking up the Completed signal.<br>
Also, this error does not occur every time.  It is very intermittent.</p>
<p>Is there a better/more reliable way that I should be listening for the end of CLI processing?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-04-26 22:34 UTC)

<p>Could you check if your callback called in the main thread or in the CLI’s background processing thread?</p>

---

## Post #3 by @Sam_Horvath (2018-04-26 23:06 UTC)

<p>The callback is on the main thread.</p>

---

## Post #4 by @lassoan (2018-04-27 00:29 UTC)

<p>Without seeing the source code, it is really difficult to guess what the problem can be. Is there a chance that you can upload the source code of your extension to GitHub and copy-paste the link here?</p>

---

## Post #5 by @Sam_Horvath (2018-04-27 00:40 UTC)

<p>Sure.  It is already on GitHub:  <a href="https://github.com/KitwareMedical/OsteotomyPlanner" rel="nofollow noopener">https://github.com/KitwareMedical/OsteotomyPlanner</a></p>
<p>You can see one of the command line node connections here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/KitwareMedical/OsteotomyPlanner/blob/a61397e5ed11d85e1ce1be189005ce13537a3f85/Planner/qSlicerPlannerModuleWidget.cxx#L1597" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/OsteotomyPlanner/blob/a61397e5ed11d85e1ce1be189005ce13537a3f85/Planner/qSlicerPlannerModuleWidget.cxx#L1597" target="_blank" rel="nofollow noopener">KitwareMedical/OsteotomyPlanner/blob/a61397e5ed11d85e1ce1be189005ce13537a3f85/Planner/qSlicerPlannerModuleWidget.cxx#L1597</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1587" style="counter-reset: li-counter 1586 ;">
<li>this-&gt;qvtkReconnect(d-&gt;BrainReferenceNode, node,</li>
<li>                    vtkCommand::ModifiedEvent,</li>
<li>                    this, SLOT(updateWidgetFromMRML()));</li>
<li>this-&gt;qvtkReconnect(d-&gt;BrainReferenceNode, node,</li>
<li>                    vtkMRMLDisplayableNode::DisplayModifiedEvent,</li>
<li>                    this, SLOT(updateWidgetFromMRML(vtkObject*, vtkObject*)));</li>
<li>if(node &amp;&amp; node != d-&gt;BrainReferenceNode)</li>
<li>{</li>
<li>  d-&gt;cliFreeze = true;</li>
<li>  d-&gt;cmdNode =  this-&gt;plannerLogic()-&gt;createHealthyBrainModel(vtkMRMLModelNode::SafeDownCast(node));</li>
<li class="selected">  qvtkConnect(d-&gt;cmdNode, vtkMRMLCommandLineModuleNode::StatusModifiedEvent, this, SLOT(finishWrap()));</li>
<li>  d-&gt;MetricsProgress-&gt;setCommandLineModuleNode(d-&gt;cmdNode);</li>
<li>  d-&gt;BrainVisibilityCheckbox-&gt;setEnabled(true);</li>
<li>}</li>
<li>d-&gt;BrainReferenceNode = node;</li>
<li>this-&gt;updateMRMLFromWidget();</li>
<li>}</li>
<li>
</li>
<li>//-----------------------------------------------------------------------------</li>
<li>void qSlicerPlannerModuleWidget::updateCurrentCutNode(vtkMRMLNode* node)</li>
<li>{</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I’m in the middle of bugfixes and refactoring, so some of the code is rather… convoluted.  I was really just hoping that someone had seen a similar error.</p>

---

## Post #6 by @lassoan (2018-04-27 01:06 UTC)

<p>Great, thank you!</p>
<p>In the line that you highlighted, you should probably use <code>qvtkReconnect</code> instead of <code>qvtkConnect</code>, otherwise the connection to the old node may not be removed when you connect a new node.</p>
<p>Every simple C pointer as a class member variable is a potential point of failure and you have <em>many</em> of them. If you own the object or want to make sure a referenced object is not destroyed while you still want to use it, then you can use <code>vtkNew&lt;&gt;</code> or <code>vtkSmartPointer&lt;&gt;</code>. If you don’t want to prevent deletion of the object but you want to make sure that the object is valid, then use <code>vtkWeakPointer&lt;&gt;</code> and always check if the pointer is valid before using it.</p>
<p>Since Subject hierarchy node is introduced, model hierarchy has become kind of obsolete, since Subject hierarchy is much more flexible (can deal with any kind of nodes, can be extended using custom plugins, etc.) and simpler to use (no need to create nodes to just create folders or add a node to the subject hierarchy tree). I would recommend to switch to that instead of using model hierarchy.</p>
<p>If you’ve got rid of simple C pointers from member variables and finished up with your cleanup and you still have this problem then let me know and I have a look at the code again.</p>

---

## Post #7 by @Sam_Horvath (2018-04-27 01:22 UTC)

<p>Thanks!  Will let you know how it goes.</p>

---
