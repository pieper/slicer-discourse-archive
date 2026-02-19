---
topic_id: 34423
title: "Error Giving Inputs From Console"
date: 2024-02-20
url: https://discourse.slicer.org/t/34423
---

# Error giving inputs from console

**Topic ID**: 34423
**Date**: 2024-02-20
**URL**: https://discourse.slicer.org/t/error-giving-inputs-from-console/34423

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-02-20 11:56 UTC)

<p>Hi to everyone. the question today is the following one:</p>
<p>· I’m trying to read some specific inputs from user in python console in Slicer. For this purpose I use:</p>
<pre><code class="lang-auto">def entryLetterReader(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_input = user_input.strip()  # Eliminar espacios en blanco al principio y al final

            if user_input and user_input.isalpha() and len(user_input) == 1:
                return user_input
            else:
                print("Invalid input. Please enter a letter.")
                
        except EOFError:
            print("EOFError: End of File reached. Please make sure to provide input.")
</code></pre>
<p>In this example I only want to accept the input when it is a letter. The first time my code calls the function works well, and for example if y click enter without type any letter, advises me to put one letter. Although, when my code calls the function for second time this apparently does not work, letting the user click enter and continue.</p>
<p>The code was tested in Spyder API and works fine, any suggestion about it?</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @SANTIAGO_PENDON_MING (2024-02-20 14:44 UTC)

<p>To clarify the problem:</p>
<ul>
<li>When we execute the code in function version, it only works well the first time. Then the following times the code can not manage the exception and pass thru the except without stopping. We tried it in Spyder and PyCharm, and only crashes in Slicer.</li>
</ul>

---

## Post #3 by @pieper (2024-02-20 18:51 UTC)

<p>You should use a Qt widget, like a QLineEdit with a button or a menu of choices, which you can get signals from.  This will integrated with Slicer’s event loop in a way that python’s input function is not.</p>

---

## Post #4 by @lassoan (2024-02-20 20:06 UTC)

<p>Slicer did not crash. While Slicer was running your Python commands, the application could not process events, so the application GUI could not respond. There are many ways to avoid this (pump the event loop, use timers, run processing in a subprocess, etc.), but as <a class="mention" href="/u/pieper">@pieper</a> suggested above, the right thing to do is to use the GUI of the application for user input.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">Slicer developer tutorials</a> on how to implement a simple Python-scripted module in Slicer that can get all the inputs from the user, run the processing, and display its outputs.</p>

---

## Post #5 by @SANTIAGO_PENDON_MING (2024-02-22 08:54 UTC)

<p>Thanks for your answers <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>. To be honest, creating interfaces with Qt and similar is a new world for me, I’m not very familiarized with it.</p>
<p>I was reading the documentation that you recommended me, but i’m not sure how to start. My goal is not very ambitious: I need to create a button that until pressed stops the code. When I click the same button, the code should run again. The process of stop and continue should happen multiple times during the execution of the code.</p>
<p>If you could give me some guidelines to start it, I will appreciate it.</p>
<p>Thanks a lot.</p>

---

## Post #6 by @pieper (2024-02-22 16:02 UTC)

<p>You basically just need to set up your code to be event driven rather than depending on a loop to iterate.  You could look at the Endoscopy module for example.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L404-L418">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L404-L418" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L404-L418" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L404-L418</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="404" style="counter-reset: li-counter 403 ;">
          <li>def setPlaybackEnabled(self, play):</li>
          <li>    if play:</li>
          <li>        # Start playback</li>
          <li>        self.timer.start()</li>
          <li>        # Enable the user to stop playback</li>
          <li>        self.playButton.text = _("Stop flythrough")</li>
          <li>        # Cannot save camera orientation during flythrough.</li>
          <li>        self.saveOrientationButton.enabled = False</li>
          <li>    else:</li>
          <li>        # Stop playback</li>
          <li>        self.timer.stop()</li>
          <li>        # Enable the user to start playback</li>
          <li>        self.playButton.text = _("Play flythrough")</li>
          <li>        # Once playback is stopped, saving the camera orientation is permitted.</li>
          <li>        self.saveOrientationButton.enabled = True</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
