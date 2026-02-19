---
topic_id: 34749
title: "Unable To Install Vmtk Using Conda Or Binary"
date: 2024-03-06
url: https://discourse.slicer.org/t/34749
---

# Unable to Install VMTK Using Conda or Binary

**Topic ID**: 34749
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/unable-to-install-vmtk-using-conda-or-binary/34749

---

## Post #1 by @adhar (2024-03-06 20:09 UTC)

<p>Hello folks,</p>
<p>I am trying to install vmtk 1.5 in order to run some custom Pypes scripts. I was previously able to use conda to install an earlier version, however, after uninstalling the previous version, no matter what command I use I always get a PackagesNotFoundError. My channels are conda-forge and defaults, and I can see that vmtk 1.5 is on the anaconda site.</p>
<p>I’ve tried with commands “conda install -c conda-forge vmtk” and " conda install vmtk=1.5," which I’ve seen working in other threads, but no luck for me.  I’ve also uninstalled anaconda and installed miniconda (which was a hassle), but still no luck. I’ve tried the binary packages for MacOS, but ‘vmtk &amp;’ returns “zsh: command not found: vmtk”, even though it seems like by bash profile is altered in the correct way.</p>
<p>Can anyone help?</p>

---

## Post #2 by @Sofia_Gonzalez (2024-10-09 08:10 UTC)

<p>Hello,<br>
I don’t know if you already solved this problem, but, you should do the next steps:</p>
<p>conda create --name name_of_your_environment python=3.6</p>
<p>This is the latest version that vmtk accepts.<br>
And to activate it:<br>
conda activate vmtk_env</p>
<p>Then you have to put:<br>
pip install vmtk</p>
<p>pip show vmtk</p>
<p>ANd with this last line you can see if it is installed.</p>

---
