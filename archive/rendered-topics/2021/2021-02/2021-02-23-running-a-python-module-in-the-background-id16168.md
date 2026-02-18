# Running a python module in the background

**Topic ID**: 16168
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/running-a-python-module-in-the-background/16168

---

## Post #1 by @marianaslicer (2021-02-23 21:28 UTC)

<p>Hi everyone,</p>
<p>I’m using the latest 3D Slicer version (4.13.20201207) and I have been working on a python scripted module. The module requires two inputs (by the user) and there is a button to run the algorithm. I would like to run this module in the background but I don’t know how to start doing it (I never did it before).</p>
<p>Can you advise me on how to do that? I am not familiar with C++.</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-02-23 21:38 UTC)

<p>You can create a new Python scripted CLI (command-line interface) module, which performs the time-consuming processing in the background in a separate process. Your interactive Python scripted loadable module remains almost the same, it just starts the CLI module and adds an observer (or checks status of the CLI module node from time to time). You can find an example of a Python scripted CLI module <a href="https://github.com/lassoan/SlicerPythonCLIExample">here</a> and how to run CLI module in the background <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#running-cli-in-the-background">here</a>.</p>

---

## Post #3 by @marianaslicer (2021-02-23 22:00 UTC)

<p>Thank you so much for replying.<br>
I will look into your suggestions and if I have questions I will come back again.</p>

---

## Post #4 by @marianaslicer (2021-02-24 21:42 UTC)

<p>Hi again,</p>
<p>I am trying to run a complex algorithm in the background but I am getting some issues.<br>
The main part of the algorithm is to do image registration and I am using the Elastix registration available in Slicer. I would like to run it in the background, but since it is a scripted loaded module how can I do it?<br>
I also needed access to python packages and class objects from other python modules, can I do it using the cli module?<br>
Is it possible to use a class object as parameter of cli module?</p>
<p>Sorry for the questions. I have a scripted python module 100% working but I would like to run it in the background in order to use Slicer at the same time.</p>
<p>Thank you for the help.</p>

---

## Post #5 by @lassoan (2021-02-25 06:22 UTC)

<aside class="quote no-group" data-username="marianaslicer" data-post="4" data-topic="16168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marianaslicer/48/8555_2.png" class="avatar"> marianaslicer:</div>
<blockquote>
<p>The main part of the algorithm is to do image registration and I am using the Elastix registration available in Slicer. I would like to run it in the background, but since it is a scripted loaded module how can I do it?</p>
</blockquote>
</aside>
<p>Elastix is already a separate process, this is even easier, because you don’t need to create a CLI. All you need to change is to not block the application while Elastix is running. Instead of blocking the application by using <a href="https://github.com/lassoan/SlicerElastix/blob/ab9cb496dde896f40d2065ce3a59c8d0f1cb9835/Elastix/Elastix.py#L712-L719">this while loop</a> check the status of Elastix execution in a function that is called regularly by a QTimer. You can make this change in your SlicerElastix module or you can copy relevant parts from SlicerElastix module to your module.</p>
<aside class="quote no-group" data-username="marianaslicer" data-post="4" data-topic="16168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marianaslicer/48/8555_2.png" class="avatar"> marianaslicer:</div>
<blockquote>
<p>I also needed access to python packages and class objects from other python modules, can I do it using the cli module?</p>
</blockquote>
</aside>
<p>Since only Elastix process will run in the background, everything else can remain in a regular Python scripted module. No need for Python CLI module for your case.</p>

---

## Post #6 by @marianaslicer (2021-02-26 17:03 UTC)

<p>Hello again,</p>
<p>I managed to run Elastix without freeze Slicer, but not the rest of the code. Anyway, I would like to know if it is possible (and how) to perform the following tasks automatically:</p>
<p>1- Connect Slicer into a server. Whenever new DICOM data is on the server, import it into the Slicer’s database.</p>
<p>2- Run a python scripted module (in the Slicer’s module list) with the new data.</p>
<p>I would appreciate any suggestion. P.S: I’m no a programming expert.</p>

---

## Post #7 by @lassoan (2021-02-27 02:37 UTC)

<aside class="quote no-group" data-username="marianaslicer" data-post="6" data-topic="16168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marianaslicer/48/8555_2.png" class="avatar"> marianaslicer:</div>
<blockquote>
<p>Connect Slicer into a server. Whenever new DICOM data is on the server, import it into the Slicer’s database.</p>
</blockquote>
</aside>
<p>There is no DICOM service that allows an application entity to “subscribe” to all new images. You can set up auto-push on the server, so that the server sends any new images to the Slicer listening server (C-STORE SCP). You could also poll the server (Slicer acts as C-FIND SCU) and retrieve (Slicer acts as C-MOVE SCU) if something new is found, which is more complicated, but may be necessary if auto-push is not available.</p>
<aside class="quote no-group" data-username="marianaslicer" data-post="6" data-topic="16168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marianaslicer/48/8555_2.png" class="avatar"> marianaslicer:</div>
<blockquote>
<p>Run a python scripted module (in the Slicer’s module list) with the new data.</p>
</blockquote>
</aside>
<p>Received DICOM images are automatically added to the database. To automatically process or incoming data, you can connect functions to <code>patientAdded</code>, <code>studyAdded</code>, etc. signals emitted by the <code>ctkDICOMDatabase</code>.</p>

---

## Post #8 by @Mwoon (2023-02-23 12:40 UTC)

<p>Hi, sorry to exhume this subject but I have a similar dilemma.<br>
I want to run a python script in the background, but this is cumbersome to create a xml file for every script file I would like to use. Is there any other solutions other than to make them scripted CLI ?</p>

---

## Post #9 by @pieper (2023-02-23 15:02 UTC)

<p>You might try the <a href="https://github.com/pieper/SlicerParallelProcessing">ParallelProcessing</a> extension.</p>

---
