---
topic_id: 3774
title: "Trigger event when CLI run has completed"
date: 2018-08-14
url: https://discourse.slicer.org/t/3774
last_bumped: 2026-03-19T13:36:03.069Z
---

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

## Post #5 by @Suhaim (2026-02-21 04:59 UTC)

<p>Hi,<br>
I am providing some more context to this problem I am facing, and any help in debugging this issue would be greatly appreciated.<br>
This is the pseudo code for what my CLI module is doing :-</p>
<pre><code class="lang-auto">import time


def main(mode: str):

     if mode == "sleep":

        time.sleep(30)  # vtkMRMLCommandLineModuleNode::StatusModifiedEvent arrives on time
     else:
        # vtkMRMLCommandLineModuleNode::StatusModifiedEvent only fires after UI interaction
        run_long_pipeline()  # torch + cv2 + long processing chain


def run_long_pipeline():

     # many steps...

     # process exits normally and outputs are valid

     pass


if __name__ == "__main__":

     main(mode="pipeline")
</code></pre>
<p>The reason I have written it this way is to demonstrate that, if I use a time.sleep(t) on the process running the CLI module, my custom widget is able to react precisely on time when the CLI module finishes execution. But when a custom pipeline I have written is called, the status of the CLI module’s node is not updating correctly.</p>
<p>I am certain that the cli node’s status is not updating correctly because I wrote a polling function using QTimer inside my custom widget “qSlicerExampleModuleWidget” to verify that. It’s status is updating only on specific interaction with the UI after it completes.</p>
<p>The UI interaction which does that is - if I change the current selected module after the cli module finished execution, the cli node’s status seems to update immediately, and my widget is able to react to it.</p>
<aside class="quote no-group" data-username="Suhaim" data-post="3" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/suhaim/48/81421_2.png" class="avatar"> Suhaim:</div>
<blockquote>
<p>Whatever is inside <code>moduleWidget-&gt;onCliStatusChanged</code>is only getting called when I move to the data module or click enter in the python console.</p>
</blockquote>
</aside>
<p>Another UI interaction that does the same is what I had mentioned above - which is clicking the enter button inside the python console. Would anyone have any idea what could cause such behaviour?</p>

---

## Post #6 by @pieper (2026-02-21 15:55 UTC)

<p>I’ve been working on a <a href="https://github.com/pieper/slicer-skill">slicer-skill</a> to see if AI agents can help  with slicer development.  I put your question in and I got the answer below.  I don’t know if it’ll fix your problem but it sounds about right.</p>
<p><code>&lt;ai&gt;</code></p>
<h2><a name="p-132152-root-cause-analysis-cli-statusmodifiedevent-not-firing-until-ui-interaction-1" class="anchor" href="#p-132152-root-cause-analysis-cli-statusmodifiedevent-not-firing-until-ui-interaction-1" aria-label="Heading link"></a>Root Cause Analysis: CLI <code>StatusModifiedEvent</code> Not Firing Until UI Interaction</h2>
<p>This is a well-understood architectural issue in Slicer. Here’s exactly what’s happening and why.</p>
<h3><a name="p-132152-the-status-update-chain-2" class="anchor" href="#p-132152-the-status-update-chain-2" aria-label="Heading link"></a>The Status Update Chain</h3>
<p>When a CLI module runs asynchronously via <code>Apply()</code>, status updates follow this path:</p>
<pre><code class="lang-auto">Background Thread (ApplyTask):
  node-&gt;SetStatus(Completing, false)   // flags InvokeStatusModifiedEvent=true, but NO Modified() call
  appLogic-&gt;RequestModified(node)      // pushes node onto a thread-safe queue
          |
          v
Main Thread Queue (InternalModifiedQueue):
  [node sits waiting in queue...]
          |
          v
QTimer::singleShot chain:             ← REQUIRES Qt EVENT LOOP TO BE SPINNING
  processAppLogicModified()
    → ProcessModified()
      → node-&gt;Modified()
        → StatusModifiedEvent          ← YOUR OBSERVER FIRES HERE
</code></pre>
<p>The critical link is <strong>step 3</strong>: <code>ProcessModified()</code> is triggered by a self-rescheduling <code>QTimer::singleShot</code> chain managed in <code>qSlicerCoreApplication</code>. These timers <strong>can only fire when Qt’s event loop is actively processing events</strong>.</p>
<h3><a name="p-132152-the-key-question-is-this-a-scripted-cli-or-executable-cli-3" class="anchor" href="#p-132152-the-key-question-is-this-a-scripted-cli-or-executable-cli-3" aria-label="Heading link"></a>The Key Question: Is This a Scripted CLI or Executable CLI?</h3>
<p><strong>If your CLI module is a <em>scripted</em> CLI module</strong> (Python-based, <code>*.py</code> with the CLI XML descriptor), this is almost certainly the cause:</p>
<ul>
<li><strong>Scripted CLI modules run in Slicer’s main thread</strong> due to Python’s GIL (Global Interpreter Lock). Even though Slicer tries to run them in a background thread, the GIL forces Python execution back onto the main thread.</li>
<li>While your <code>torch + cv2</code> pipeline is running, it monopolizes the main thread. The Qt event loop <strong>cannot spin</strong>, so <code>QTimer::singleShot</code> callbacks never fire, and <code>ProcessModified()</code> is never called.</li>
<li><code>time.sleep()</code> works because it <strong>releases the GIL</strong>, allowing the Qt event loop to process pending events during the sleep.</li>
</ul>
<p>This is confirmed by Steve Pieper in a <a href="https://discourse.slicer.org/t/running-scripted-cli-prevents-qprocess-from-finishing/26534">related discourse thread</a>: <em>“CLI modules are run in independent threads, while python code runs in the main thread, so that may be the difference.”</em></p>
<p><strong>If your CLI module is an <em>executable</em> CLI</strong> (separate process), the computation itself shouldn’t block the main thread, but something else in your setup might be (e.g., synchronous I/O waiting, a blocking call in the module widget, etc.).</p>
<h3><a name="p-132152-why-ui-interaction-fixes-it-4" class="anchor" href="#p-132152-why-ui-interaction-fixes-it-4" aria-label="Heading link"></a>Why UI Interaction “Fixes” It</h3>
<p>When you click in the Python console, switch modules, or perform any UI interaction, Qt processes pending events as part of handling that interaction. This finally allows the queued <code>QTimer::singleShot</code> to fire → <code>ProcessModified()</code> runs → <code>Modified()</code> is called → <code>StatusModifiedEvent</code> fires.</p>
<h3><a name="p-132152-solutions-5" class="anchor" href="#p-132152-solutions-5" aria-label="Heading link"></a>Solutions</h3>
<p><strong>Option 1: Convert to an executable CLI module</strong> (recommended for heavy computation)</p>
<p>Executable CLI modules run as a completely separate process, so they don’t block Slicer’s main thread or the Qt event loop. This is the cleanest solution for torch/cv2 pipelines.</p>
<p><strong>Option 2: If you must use a scripted CLI, call <code>slicer.app.processEvents()</code> periodically</strong></p>
<p>Insert calls to process the event loop during your pipeline:</p>
<pre><code class="lang-auto">import slicer

def run_long_pipeline():
    step1_result = step1()
    slicer.app.processEvents()  # let Qt process pending events
    
    step2_result = step2(step1_result)
    slicer.app.processEvents()
    
    # ... etc
</code></pre>
<p>This is a workaround, not ideal for production, but it unblocks the event loop during execution.</p>
<p><strong>Option 3: Use <code>slicer.cli.run()</code> with <code>wait_for_completion=False</code> and an observer</strong></p>
<p>If you’re launching the CLI from Python, the standard pattern is:</p>
<pre><code class="lang-auto">cliNode = slicer.cli.run(module, parameters, wait_for_completion=False)
cliNode.AddObserver('ModifiedEvent', onCLIStatusChanged)
</code></pre>
<p>But this still requires the event loop to be spinning in the main thread.</p>
<p><strong>Option 4: Use QProcess or subprocess to run the heavy pipeline externally</strong></p>
<p>Wrap your torch/cv2 pipeline as a standalone script that runs in a separate process via <code>QProcess</code> or Python’s <code>subprocess</code>, keeping the main thread free.</p>
<h3><a name="p-132152-relevant-discourse-threads-6" class="anchor" href="#p-132152-relevant-discourse-threads-6" aria-label="Heading link"></a>Relevant Discourse Threads</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/trigger-event-when-cli-run-has-completed/3774">Trigger event when CLI run has completed</a> — the thread where this exact issue is discussed (including your recent posts)</li>
<li><a href="https://discourse.slicer.org/t/running-scripted-cli-prevents-qprocess-from-finishing/26534">Running scripted-cli prevents QProcess from finishing</a> — confirms scripted CLIs block the main thread</li>
<li><a href="https://discourse.slicer.org/t/problems-listening-to-vtkmrmlcommandlinenode-events-from-loadable-module/2711">Problems listening to vtkMRMLCommandLineNode events</a> — related observer issues</li>
</ul>
<h3><a name="p-132152-tldr-7" class="anchor" href="#p-132152-tldr-7" aria-label="Heading link"></a>TL;DR</h3>
<p>Your heavy Python pipeline (torch + cv2) is blocking Slicer’s main thread via the GIL, which prevents the Qt event loop from processing the <code>QTimer::singleShot</code> callbacks that deliver <code>StatusModifiedEvent</code>. <code>time.sleep()</code> works because it releases the GIL. The fix is to either convert to an executable CLI module or ensure the main thread’s event loop can spin during execution.<br>
<code>&lt;/ai&gt;</code></p>

---

## Post #7 by @Suhaim (2026-02-25 04:29 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
Thank you for the quick and detailed reply. I will go through this and get back to you.</p>

---

## Post #8 by @Suhaim (2026-03-18 10:28 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
It was only now that I got time to come back to this issue I was facing. I wanted to share some problems I was having while implementing the alternatives you had suggested.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><strong>Option 1: Convert to an executable CLI module</strong> (recommended for heavy computation)</p>
</blockquote>
</aside>
<ol>
<li>I wanted to prototype my solution and it is working in python currently. I would prefer to port my scripted CLI module to an executable one later if that would be possible.</li>
</ol>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Option 2: If you must use a scripted CLI, call <code>slicer.app.processEvents()</code> periodically</p>
</blockquote>
</aside>
<ol start="2">
<li>I believe that a scripted cli module does not have access to the main qSlicerApplication instance, therefore I am getting this error inside the CLI module.</li>
</ol>
<pre><code class="lang-auto">slicer.app.processEvents()
^^^^^^^^^^

AttributeError: module ‘slicer’ has no attribute ‘app’
</code></pre>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Option 3: Use <code>slicer.cli.run()</code> with <code>wait_for_completion=False</code> and an observer</p>
</blockquote>
</aside>
<ol start="3">
<li>I am running the cli node from C++(from a loadable module) and regardless, this solution needs the event loop running like you mentioned.</li>
</ol>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><strong>Option 4: Use QProcess or subprocess to run the heavy pipeline externally</strong></p>
<p>Wrap your torch/cv2 pipeline as a standalone script that runs in a separate process via <code>QProcess</code> or Python’s <code>subprocess</code>, keeping the main thread free.</p>
</blockquote>
</aside>
<ol start="4">
<li>I didn’t understand this alternative fully, I would greatly appreciate it if you could elaborate what you meant with a minimal example.</li>
</ol>
<p>Any help on this matter would be greatly appreciated, as the asynchronous nature of the CLI module is something I need.<br>
Thanks!</p>

---

## Post #9 by @pieper (2026-03-18 13:18 UTC)

<p>Hi <a class="mention" href="/u/suhaim">@Suhaim</a> - I hope I was transparent that the post I made above was from an AI and not from me directly.  I was just trying to give you some clues because I didn’t have time to fully study your issues.</p>
<p>I will say, as a human, that it’s important to carefully consider your overall approach when implementing new features.  I still don’t have time to review the details of your question (I have my own work to do) but the sorts of things you mention, like running CLIs from C++, are not common patterns and are probably indications of some deeper architectural issues.  My general advice is to make small proof of concept implementations of your intended architecture (like a module that just has a stub implementation) and see if you can make it work.</p>

---

## Post #10 by @Suhaim (2026-03-19 04:32 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
I didn’t notice your ai tag around the entire answer. I now understand that what you posted was entirely AI generated.</p>
<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>My general advice is to make small proof of concept implementations of your intended architecture (like a module that just has a stub implementation) and see if you can make it work.</p>
</blockquote>
</aside>
<p>I will attempt to do this and isolate my issue.</p>
<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="3774">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>running CLIs from C++, are not common patterns and are probably indications of some deeper architectural issues.</p>
</blockquote>
</aside>
<p>Could you explain why this is problematic? I am a beginner and am trying to wrap my head around Qt’s architecture and how Slicer works. The way I was thinking of it was that prototyping in Python is easy, hence the use of the Python CLI.</p>

---

## Post #11 by @pieper (2026-03-19 13:36 UTC)

<p>Good - making small easily reproducible examples of any issues you run into is the best way to get help on the forum.  It’s hard for people to parse out-of-context C++ code snippets.</p>
<p>Regarding C++ and Python, it’s almost always better to have the main logic of your work in the scripted layer, so that you can easily reload and test.  Anything that is performance critical can be delegated to C++.  The layering should, as a general rule, be that python calls C++ and not the other way around.</p>

---
