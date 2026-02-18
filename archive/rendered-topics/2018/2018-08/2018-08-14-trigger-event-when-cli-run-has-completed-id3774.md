# Trigger event when CLI run has completed

**Topic ID**: 3774
**Date**: 2018-08-14
**URL**: https://discourse.slicer.org/t/trigger-event-when-cli-run-has-completed/3774

---

## Post #1 by @dominicrushforth (2018-08-14 15:07 UTC)

<p>As in the title I would like to be able to trigger some code after a CLI run has completed.</p>
<p>I know I can use the parameter wait_for_completion=True to pause the code execution, however if I do this the GUI does not update and the qCLIProgressBar does not run making it look as though the program has hung.</p>
<p>I have tried setting a connect condition to be triggered by the progress bar…</p>
<p>self.bar3.connect(‘valueChanged(int)’, self.onBar3)</p>
<p>but the qSlicerCLIProgressBar does not seem to give out the same signals as the qProgressBar.</p>
<p>I also tried using a While / Sleep loop to check the status of the cliNode (cliNode.GetStatus()) but this freezes the GUI just like the wait_for_completion parameter.</p>
<p>Is there any way to wait for the CLI to complete without freezing the GUI or (which would seem neater to me) to trigger a new routine once it has completed.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2018-08-14 15:28 UTC)

<p>Yes, you can put an observer on the command line module node and get events when the state changes.  See  “<em>Running CLI in the background</em>” here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #3 by @Suhaim (2026-02-17 07:54 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
I am facing an issue when trying to react to a cli node’s execution completion. I saw the example you have linked below.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>See “<em>Running CLI in the background</em>” here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>
</blockquote>
</aside>
<p>I attempted to do the same in cpp. The problem I am facing is that, until I open the python console and click enter, or open the data module, the status of my CLI node is not updating. For example, I send a request for a CLI module’s execution and opened the CLI module’s widget. The widget’s timer keeps updating till the CLI module runs. For example if the module’s execution took 20s, the widget reaches 20s and stops counting. Once the data module is opened after the 20s it needed for execution, the callbacks I registered are getting called. But these callbacks had to run when the vtkMRMLCommandLineModuleNode::StatusModifiedEvent fired as soon as the 20s where over, not when I am opening the data module or clicking enter into the python console. It seems that the event - vtkMRMLCommandLineModuleNode::StatusModifiedEvent is not getting fired even after the CLI node has finished execution.</p>
<p>This is how I am registering the callbacks inside my qSlicerExampleModuleWidget :-</p>
<pre><code class="lang-auto">vtkSmartPointer&lt;vtkCallbackCommand&gt; statusCallback = vtkSmartPointer&lt;vtkCallbackCommand&gt;::New();
statusCallback-&gt;SetCallback([](vtkObject* caller, unsigned long eventId, void* clientData, void* callData) {
  auto* moduleWidget = static_cast&lt;qSlicerExampleModuleWidget*&gt;(clientData);
  if (!moduleWidget)
  {
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": failed to cast clientData to qSlicerExampleModuleWidget";
    return;
  }

  auto* cliNode = vtkMRMLCommandLineModuleNode::SafeDownCast(caller);
  if (!cliNode)
  {
    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": failed to cast caller to vtkMRMLCommandLineModuleNode";
    return;
  }

  moduleWidget-&gt;onCliStatusChanged(caller, (void*)cliNode-&gt;GetID(), eventId, callData);
});
statusCallback-&gt;SetClientData(this);
cliNode-&gt;AddObserver(vtkMRMLCommandLineModuleNode::StatusModifiedEvent, statusCallback);

cliNode-&gt;SetParameterAsString("inputPathA", std::string(inputPathA));
cliNode-&gt;SetParameterAsString("inputPathB", std::string(inputPathB));

cliLogic-&gt;Apply(cliNode, false);

qInfo() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": CLI request sent successfully";
</code></pre>
<p>Whatever is inside <code>moduleWidget-&gt;onCliStatusChanged</code>is only getting called when I move to the data module or click enter in the python console. Any suggestions on why this could be happening? I tried using the vtkCommand::ModifiedEvent as well but got the same results. Any help would be greatly appreciated.</p>
<p>Thanks!</p>

---

## Post #4 by @Suhaim (2026-02-17 09:48 UTC)

<p>Hi all,<br>
When I am running the CLI module synchronously, the callbacks are executing as soon as the CLI execution completes. But it is in the asynchronous CLI execution I am facing problems on the CLI node’s status updating reliably.</p>
<p>Working code :-</p>
<pre><code class="lang-auto">**everything else the same**

 cliLogic-&gt;ApplyAndWait(cliNode, false);

</code></pre>

---
