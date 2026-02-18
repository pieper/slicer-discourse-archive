# Create, invoke and observe vtk custom event

**Topic ID**: 11794
**Date**: 2020-05-30
**URL**: https://discourse.slicer.org/t/create-invoke-and-observe-vtk-custom-event/11794

---

## Post #1 by @PaoloZaffino (2020-05-30 14:09 UTC)

<p>Hi all,<br>
I’m using the function SetParameter() of a vtkMRMLScriptedModuleNode object.<br>
From a different class I observe that node and I run a function if the parameter changes…all run smoothly right so far, since I have a single parameter to take care of.</p>
<p>What about if I need to set two parameters (not at the same time) and I want to get a different notification for each modified parameter?</p>
<p>Do I have to create, invoke and observe two different vtk custom events?</p>
<p>If so, do you have a python snippet of code to suggest?</p>
<p>Thank you!</p>
<p>Paolo</p>

---

## Post #2 by @pieper (2020-05-30 16:54 UTC)

<p>Hi Paolo -</p>
<p>Good point - right now you get the same ModifiedEvent no matter what parameter changed.  You would need to keep track of the old values and check which one had changed.</p>
<p>Currently we just call <code>Modified</code> in <code>SetParameter</code>, but we could change that to be <code>this-&gt;InvokeEvent(vtkCommand::ModifiedEvent, name)</code></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/421d1c06a9ac4ead72bdd338dd7358ea48008b25/Libs/MRML/Core/vtkMRMLScriptedModuleNode.cxx#L144">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/421d1c06a9ac4ead72bdd338dd7358ea48008b25/Libs/MRML/Core/vtkMRMLScriptedModuleNode.cxx#L144" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/421d1c06a9ac4ead72bdd338dd7358ea48008b25/Libs/MRML/Core/vtkMRMLScriptedModuleNode.cxx#L144" target="_blank" rel="noopener">Slicer/Slicer/blob/421d1c06a9ac4ead72bdd338dd7358ea48008b25/Libs/MRML/Core/vtkMRMLScriptedModuleNode.cxx#L144</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="134" style="counter-reset: li-counter 133 ;">
          <li>}</li>
          <li></li>
          <li>//----------------------------------------------------------------------------</li>
          <li>void vtkMRMLScriptedModuleNode</li>
          <li>::SetParameter(const std::string&amp; name, const std::string&amp; value)</li>
          <li>{</li>
          <li>  const std::string currentValue = this-&gt;GetParameter(name);</li>
          <li>  if (value != currentValue)</li>
          <li>    {</li>
          <li>    this-&gt;Parameters[name] = value;</li>
          <li class="selected">    this-&gt;Modified();</li>
          <li>    }</li>
          <li>}</li>
          <li></li>
          <li>//----------------------------------------------------------------------------</li>
          <li>void vtkMRMLScriptedModuleNode::UnsetParameter(const std::string&amp; name)</li>
          <li>{</li>
          <li>  int count = this-&gt;Parameters.erase(name);</li>
          <li>  if (count &gt; 0)</li>
          <li>    {</li>
          <li>    this-&gt;Modified();</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Then you should be able to get the parameter using the method described <a href="https://discourse.slicer.org/t/custom-events-for-vtk/1286/3">here</a></p><aside class="quote quote-modified" data-post="3" data-topic="1286">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/custom-events-for-vtk/1286/3">Custom Events for VTK</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    For some types of data can add a decorator to your callback that interprets the call data in python. 
<a href="https://github.com/Kitware/VTK/blob/master/Wrapping/Python/vtk/util/misc.py#L6-L27" class="onebox" target="_blank" rel="noopener">https://github.com/Kitware/VTK/blob/master/Wrapping/Python/vtk/util/misc.py#L6-L27</a> 
For most data types in Slicer, a vtkObject is actually returned as a wrapped version of whatever concrete subclass was passed in the payload, so it actually covers all slicer events that come from nodes or the scene or other classes. 


You can also call InvokeEvent from python with a calldata (payload) argument. …
  </blockquote>
</aside>


---

## Post #3 by @PaoloZaffino (2020-05-30 20:53 UTC)

<p>Hi Steve,<br>
thanks for helping.</p>
<p>Let me explain better my use case, maybe I do not need two events.<br>
We are working on arduino connection layer, the COVID19 situation slowed down the work, but we are confident to release something fully working soon.</p>
<p>I have my extension and I created a dedicated node. When a message is received from arduino I set it into the node and an event is fired as well. If one or more classes (e.g. something built on top of connection layer) are observing the node, they will be notified. I already did this and it works very well.<br>
In this case I need an event since I do not know when a message will be received.</p>
<p>At the same time I need also to send a message from Slicer to the board.<br>
The idea was to observe the node in the opposite direction and, in case, run the proper function into my logic extension. That’s why I asked for two events.<br>
Actually I do not need an event, because I know when I want to send a message.<br>
Which is the best way of exposing a function from my logic to someone that wants to send a message form his own piece of code?</p>
<p>Something “easy and raw” could be put in my logic something like:<br>
slicer.sendMessageToArduino = self.sendMessage()<br>
but I mean, it’s quite brutal!</p>
<p>Thanks a lot!<br>
Paolo</p>

---

## Post #4 by @pieper (2020-05-30 22:03 UTC)

<p>Hi Paolo -  Ah, yes, I see what you mean.</p>
<p>Well, in this case maybe just do something like:</p>
<pre><code class="lang-auto">import Arduino
Arduino.ArduinoLogic(arduinoNode).sendMessage("ciao!")
</code></pre>

---

## Post #5 by @PaoloZaffino (2020-05-30 22:56 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>!<br>
It is exactly what I was looking for!</p>

---

## Post #6 by @PaoloZaffino (2020-05-30 23:13 UTC)

<p>Just a little edit: the node should be not given</p>
<p>This works:</p>
<blockquote>
<p>import Arduino<br>
Arduino.ArduinoLogic().sendMessage(“ciao!”)</p>
</blockquote>
<p>Thanks again!</p>

---

## Post #7 by @PaoloZaffino (2020-06-01 12:26 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,<br>
actually I didn’t reach the point, sorry.</p>
<p>By using</p>
<blockquote>
<p>Arduino.ArduinoLogic().sendMessage(“ciao!”)</p>
</blockquote>
<p>I have access to the generic function, but I actually need to access the method of an instance of the class.</p>
<p>When I run the module (by UI) I create an object of the logic class and then I establish a connection (with all the required parameters). I need to access the function of this specific object, not to the (static) method of the class.<br>
That’s why I thought the extremely raw was of putting into the logic constructor</p>
<blockquote>
<p>slicer.sendMessageToArduino = self.sendMessage()</p>
</blockquote>
<p>Thanks for helping!</p>

---

## Post #8 by @pieper (2020-06-01 15:29 UTC)

<p>Hi Paulo -</p>
<p>Right - that’s what I was thinking in my original suggestion, to include an instance of your node in the constructor of the logic class.  That way the node could provide the “context” so that the <code>sendMessage</code> could determine the right connection to use, perhaps by storing a connection ID as a parameter in the node.</p>
<p>Do you have your code available on line?</p>

---

## Post #9 by @PaoloZaffino (2020-06-01 15:34 UTC)

<p>I’m afraid that a connection ID is not enough.<br>
Yes, the code is <a href="https://github.com/pzaffino/SlicerArduinoController/blob/master/ArduinoConnect/ArduinoConnect.py" rel="nofollow noopener">here</a></p>
<p>Thanks a lot!</p>

---

## Post #10 by @pieper (2020-06-01 16:14 UTC)

<p>Are you planning to have multiple connections to different devices?  If so, then your module can maintain a mapping from a connection ID, also stored in the node, and any other info you need, like file descriptor, state, or device config.  Maybe make a helper class for all that and then in the logic you just have a dictionary that tracks them by ID.</p>
<p>By the way, did you try using <a href="https://doc.qt.io/qt-5/qserialport.html">QSerialPort</a> instead of python serial?  If you did you could replace all the polling with signal/slot event driven code that would be more efficient and also probably scale better.</p>

---

## Post #11 by @PaoloZaffino (2020-06-01 17:27 UTC)

<p>Right now no, I’m not planning to support multiple devices (maybe in the future).<br>
Thanks for the qt solution…it’s incredible, qt has a solution for whatever problem!</p>
<p>Regarding the ID in the node, as far as I know, it is not enough for reading/writing, since I have to access the object.<br>
That’s why I thought to two events or to the raw top level exposure of the method during the object initialization.</p>
<p>Another raw solution could be to rely on a single event, store the action into the node parameter, and inspect the parameter to figure out which function has to be fired.<br>
Something like:</p>
<ul>
<li>“READ:50” if 50 has been read</li>
<li>“WRITE:100” if I want to write 100</li>
</ul>
<p>but, I mean, it’s a huge huge workaround!</p>

---

## Post #12 by @pieper (2020-06-01 19:00 UTC)

<p>Hmm, I’m not seeing where the issue is.  It seems to me that if you have code that is build on top of the Arduino infrastructure you can have it access the methods of the Logic class as needed.  Can you describe the use case scenario a bit more?</p>

---

## Post #13 by @PaoloZaffino (2020-06-01 19:41 UTC)

<p>I have the logic where I run the arduino connection.<br>
When the data (a string) is received, I exposeit  to the Slicer environment by putting it into a node parameter. In this way someone else interested in reading data (e.g. to built another module) can have access to the data just observing the node.</p>
<p>The problem is if the user (not me) wants to write a string from whatever point of slicer (again, for example, from his own module) to arduino. I have the function to send the data, but it’s “locked” into the instantiated logic object. I should expose this inner function of the instantiated logic object in order to be reachable from whatever point.<br>
That’s why I suggested (even if is not elegant) to punt into the constructor of the logic a line like:</p>
<blockquote>
<p>slicer.sendMessageToArduino = self.sendMessage</p>
</blockquote>
<p>In this way the user ha just to run</p>
<blockquote>
<p>slicer.sendMessageToArduino(“test”)</p>
</blockquote>
<p>to write the message.</p>
<p>Sorry for being not so linear!</p>

---

## Post #14 by @lassoan (2020-06-01 20:51 UTC)

<p>Module logics are available from other modules. In scripted modules, typically the logic is instantiated by the widget (we did not want to make the module manager to instantiate it, as it would have made module reload more complicated). This is how is done in current scripted module template. You can access it by something like this: <code>slicer.modules.mymodule.widgetRepresentation.self().logic</code>. See some more information in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">PerkLab Slicer programming tutorials</a>.</p>

---

## Post #15 by @PaoloZaffino (2020-06-01 21:23 UTC)

<p>Thanks!<br>
That’s what I was looking for!</p>

---
