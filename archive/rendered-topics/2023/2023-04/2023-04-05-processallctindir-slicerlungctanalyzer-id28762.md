---
topic_id: 28762
title: "Processallctindir Slicerlungctanalyzer"
date: 2023-04-05
url: https://discourse.slicer.org/t/28762
---

# ProcessAllCTInDir - SlicerLungCTAnalyzer

**Topic ID**: 28762
**Date**: 2023-04-05
**URL**: https://discourse.slicer.org/t/processallctindir-slicerlungctanalyzer/28762

---

## Post #1 by @giurdeluca (2023-04-05 17:07 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a> first of all thank you for your work!<br>
I want to segment and analyze many lung CT images (i’m interested in emphysema features), so doing it with a batch script from command line would be the best to achieve complete automatization. I’ve seen in the SlicerLungCTAnalyzer github repo that you provide <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py" rel="noopener nofollow ugc">this script</a> for this purpose, but it seems that it just automatize the analysis part, while the segmented lungs images are requested as input, am I correct? If so, is there a suggested way to segment all CT in a directory given as input? Thank you in advance,<br>
Giulia</p>

---

## Post #2 by @rbumm (2023-04-05 17:29 UTC)

<p>Hi <a class="mention" href="/u/giurdeluca">@giurdeluca</a> we recently implemented batch processing in both Lung CT Segmenter and Lung CT Analyzer.<br>
There is a description in the Wiki <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Batch-processing-with-Lung-CT-Segmenter">here</a> and <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Batch-Processing-with-Lung-CT-Analyzer">here</a>. Supports nrrd and NIFTI input.<br>
If questions remain please ask again.<br>
It works great, just did 100 CTs in a row without major issues …</p>

---

## Post #3 by @giurdeluca (2023-04-05 17:38 UTC)

<p>Thank you for your prompt answer! Yes I saw that but it seems that they are executed from the Slicer GUI, while i want to interact just with the cmd (Windows). Is it possible? Maybe this is a dumb question but I’m quite new in scripting on cmd</p>

---

## Post #4 by @rbumm (2023-04-05 18:13 UTC)

<p>ProcessallCTinDir is a Python script - you will need programming help to adapt it to lung CT segmented. It was written before AI tools were available in LCTA  so this step had to be done manually at that time.<br>
Now the situation is much easier, there is excellent AI for lung masks and you could adjust all parameters from the GUI. You could also batch-process the segmentations first with AI then run an adapted ProcessallCTinDir.</p>

---

## Post #5 by @giurdeluca (2023-04-05 18:16 UTC)

<p>I think i got it now, I’ll try what you suggested.<br>
Thank you</p>

---

## Post #6 by @giurdeluca (2023-04-13 14:22 UTC)

<p>Dear Bumm, sorry to bother you again.<br>
I’ve managed to execute the ProcessAllCTInDir.py script from my wsl terminal with the following command:<br>
<code>&lt;path/to/Slicer.exe&gt; --python-code "exec(open(r'path/to/processAllCTInDir.py').read())"</code>.<br>
Note that at the end of the script I’ve added <code>sys.exit()</code> to make Slicer close once it has completed the execution (as you suggested here <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>)<br>
Since i would run this script from a server for batch processing, i wish to disable any Slicer window, but when i run<br>
<code>&lt;path/to/Slicer.exe&gt; --python-code "exec(open(r'path/to/processAllCTInDir.py').read())" -no-splash -no-splash --no-main-window</code><br>
the execution never ends (i do not get a new line in the terminal nor see the result.csv file in the output folder).<br>
Where am I wrong?</p>

---

## Post #7 by @pieper (2023-04-13 14:41 UTC)

<p>The easiest is probably to install xvfb on your server and then use <a href="https://manpages.ubuntu.com/manpages/xenial/man1/xvfb-run.1.html">xvfb-run</a> as a prefix to your Slicer command.  Another alternative would be to use <a href="https://github.com/pieper/SlicerDockers">docker</a>.</p>

---

## Post #8 by @rbumm (2023-04-13 15:48 UTC)

<p>So you installed Slicer in WSL and ran this command from a WSL Linux shell?</p>

---

## Post #9 by @giurdeluca (2023-04-13 15:51 UTC)

<p>Actually I’ve followed the standard procedure to install Slicer (5.2.2 version) let’s say ‘system-wide’, but yes I ran the previous command from a WSL Linux shell</p>

---

## Post #10 by @rbumm (2023-04-13 15:54 UTC)

<p>And you intend to run this on a Linux-only server? Just need to understand the scope of the problem …</p>

---

## Post #11 by @giurdeluca (2023-04-13 15:55 UTC)

<p>Yes it’s a linux only server</p>

---

## Post #12 by @rbumm (2023-04-13 16:01 UTC)

<p>To be honest I never ran Slicer (or the script) under these conditions, without a desktop environment. But I am sure others did. You should probably start these trials with very simple hello world Python scripts, then include scanning the directory, then call a simple extension logic,  and see how it goes.</p>

---

## Post #13 by @giurdeluca (2023-04-13 16:06 UTC)

<p>I understand, thank you again for your support!</p>

---

## Post #14 by @rbumm (2023-04-13 16:28 UTC)

<p>You seem to be on the right track, here is the GPT-4 response to your problem:</p>
<p>Human:</p>
<p>Hi GPT, could I run 3D Slicer on a Linux server without GUI  in combination with a Python script for batch processing CT data?</p>
<p>AI:</p>
<p>Sure! You can run 3D Slicer on a Linux server without a GUI and use it in combination with Python scripts for batch processing CT data. To do this, you will need to use 3D Slicer’s command-line interface (CLI) and Python scripting capabilities.</p>
<p>Here are the general steps to set up and run 3D Slicer on a Linux server without a GUI:</p>
<ol>
<li>Download and install 3D Slicer: Download the latest version of 3D Slicer for Linux from the official website (<a href="https://download.slicer.org/">https://download.slicer.org/</a>). You can use <code>wget</code> or <code>curl</code> to download the archive directly on the server, then extract it to a directory of your choice:</li>
</ol>
<pre><code class="lang-auto">wget https://download.slicer.org/bitstream/ID -O slicer.tar.gz
tar -xzvf slicer.tar.gz
</code></pre>
<p>Replace “ID” with the actual download ID found on the website.</p>
<ol start="2">
<li>Enable remote access and command-line operation: Make sure you can remotely access your Linux server through SSH or another remote command-line interface.</li>
<li>Install Python and required packages: Install Python on the Linux server if it is not already installed. Also, install any required Python packages for your script using <code>pip</code>.</li>
<li>Run 3D Slicer from the command line: You can run 3D Slicer from the command line using the <code>Slicer</code> executable found in the extracted folder. You can use the <code>--no-main-window</code> argument to prevent the GUI from launching, like this:</li>
</ol>
<pre><code class="lang-auto">&lt;path-to-slicer&gt;/Slicer --no-main-window
</code></pre>
<ol start="5">
<li>Execute Python script: You can execute your Python script with 3D Slicer by providing the <code>--python-script</code> argument followed by the path to your Python script:</li>
</ol>
<pre><code class="lang-auto">&lt;path-to-slicer&gt;/Slicer --no-main-window --python-script &lt;path-to-your-python-script&gt;
</code></pre>
<p>Make sure your Python script uses Slicer’s Python API (slicer.util, slicer.modules, etc.) for batch processing and any other necessary operations on the CT data. This way, your script can take advantage of 3D Slicer’s capabilities without launching the GUI.</p>
<p>Please note that running 3D Slicer without a GUI may have some limitations, and certain features may not work as expected. However, for batch processing and other basic operations, this setup should work.</p>

---

## Post #15 by @giurdeluca (2023-04-14 10:21 UTC)

<p>So it appears i should proceed as <a class="mention" href="/u/pieper">@pieper</a> suggested before.<br>
I really thank both of you for your fast and kind help!<br>
I’ll try in this way and inform you on the outcome (if this might be helpful for anyone).<br>
Giulia</p>

---

## Post #16 by @rbumm (2023-04-16 12:36 UTC)

<p>Installing 3D Slicer 5.2.2 in Windows 11 WSL Ubuntu is quite complicated, but can be accomplished by:</p>
<pre><code class="lang-auto">cd $HOME
# get the link below from 3D Slicer download page
wget https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7 -O slicer.tar.gz

# decompress the archive
tar -xzvf ./slicer.tar.gz

# install libraries
sudo apt-get install libpulse-dev libnss3 libglu1-mesa
sudo apt-get install --reinstall libxcb-xinerama0

# Thank you GPT-4. It seems that 3D Slicer still requires a connection to an X server even in --no-main-window mode, 
# although it doesn't display the GUI. To work around this, you can use a virtual framebuffer (Xvfb) to 
# create a virtual X server where the application can run without the need for a physical display.
# For Debian-based systems (such as Ubuntu), you can install Xvfb using the following command:

sudo apt-get update
sudo apt-get install xvfb

# Start Xvfb:
# Run Xvfb on a specific display number (e.g., 99) and set the screen resolution and depth:

Xvfb :99 -screen 0 1024x768x24 &amp;

# Set the DISPLAY environment variable to the display number you chose when starting Xvfb:

export DISPLAY=:99

# Now you can run 3D Slicer with the --no-main-window argument, and it should no longer throw the 
# "could not connect to display" error

</code></pre>
<p>This will install 3D Slicer into a new directory in your $HOME directory</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db0be81a1a849bd089ded9463f08a99f6db0589f.png" alt="image" data-base62-sha1="vfM4HMdgN0ffv1rkmVfm4DyO5k3" width="529" height="168"></p>
<p>Put a test.py script file with <code>print("Hello")</code> into this folder, <code>cd</code> to the Slicer folder and run:</p>
<pre><code class="lang-auto">./Slicer --no-main-window --python-script ./test.py
</code></pre>
<p>results in:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3bcb54254aaea2e991cacf179721c8af58025d.png" data-download-href="/uploads/short-url/aSoozzeNrZ76k40JEMpVCcuTuWN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3bcb54254aaea2e991cacf179721c8af58025d.png" alt="image" data-base62-sha1="aSoozzeNrZ76k40JEMpVCcuTuWN" width="690" height="68" data-dominant-color="1C1D1D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">900×89 8.26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
