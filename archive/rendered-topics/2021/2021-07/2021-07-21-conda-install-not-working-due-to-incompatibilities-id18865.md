---
topic_id: 18865
title: "Conda Install Not Working Due To Incompatibilities"
date: 2021-07-21
url: https://discourse.slicer.org/t/18865
---

# Conda install not working due to incompatibilities

**Topic ID**: 18865
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/conda-install-not-working-due-to-incompatibilities/18865

---

## Post #1 by @perecanals (2021-07-21 15:54 UTC)

<p>Hi,</p>
<p>OS: Linux (Ubuntu 20.04.2)</p>
<p>I was trying to install VMTK via conda in an already created environment (Python 3.7.10) and I get the following error:</p>
<pre><code class="lang-auto">Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
failed                                                                                               

UnsatisfiableError: The following specifications were found
to be incompatible with the existing python installation in your environment:

Specifications:

  - vmtk -&gt; python[version='&gt;=2.7,&lt;2.7.15.0a0|&gt;=3.5,&lt;3.5.2.0a0|&gt;=3.6,&lt;3.6.2.0a0']
  - vtk -&gt; python[version='&gt;=3.8,&lt;3.9.0a0|&gt;=3.9,&lt;3.10.0a0']

Your python: python=3.7

If python is on the left-most side of the chain, that's the version you've asked for.
When python appears to the right, that indicates that the thing on the left is somehow
not available for the python version you are constrained to. Note that conda will not
change your python version to a different minor version unless you explicitly specify
that.

The following specifications were found to be incompatible with each other:

Output in format: Requested package -&gt; Available versions

Package _openmp_mutex conflicts for:
itk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; _openmp_mutex[version='&gt;=4.5']
python=3.7 -&gt; libgcc-ng[version='&gt;=7.5.0'] -&gt; _openmp_mutex[version='&gt;=4.5']
vtk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; _openmp_mutex[version='&gt;=4.5']
vmtk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; _openmp_mutex[version='&gt;=4.5']

Package ca-certificates conflicts for:
vtk -&gt; python[version='&gt;=2.7,&lt;2.8.0a0'] -&gt; ca-certificates
python=3.7 -&gt; openssl[version='&gt;=1.1.1k,&lt;1.1.2a'] -&gt; ca-certificatesThe following specifications were found to be incompatible with your system:

  - feature:/linux-64::__glibc==2.31=0
  - itk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; __glibc[version='&gt;=2.17']
  - python=3.7 -&gt; libgcc-ng[version='&gt;=7.5.0'] -&gt; __glibc[version='&gt;=2.17']
  - vmtk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; __glibc[version='&gt;=2.17']
  - vtk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; __glibc[version='&gt;=2.17']

Your installed version is: 2.31
</code></pre>
<p>I tried creating a new environment with Python 3.6, tried specifying the vtk (8.1.0), itk (4.13.0) and vmtk (1.4.0) versions that work on my other system (MacOS Big Sur 11.3, Python 3.7.4) and I can’t finish the install. It looks like it has something to do with <code>glibc</code> (not sure what this is), but even if the incompatibilities of specific packages vary a little bit when I try to install vmtk in these different circumstances, the last lines at the end are always very similar:</p>
<pre><code class="lang-auto">
  - feature:/linux-64::__glibc==2.31=0
  - itk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; __glibc[version='&gt;=2.17']
  - python=3.7 -&gt; libgcc-ng[version='&gt;=7.5.0'] -&gt; __glibc[version='&gt;=2.17']
  - vmtk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; __glibc[version='&gt;=2.17']
  - vtk -&gt; libgcc-ng[version='&gt;=7.2.0'] -&gt; __glibc[version='&gt;=2.17']

Your installed version is: 2.31
</code></pre>
<p>I have found several posts (not from vmtk) complaining about this, but haven’t found a solution yet. I am gonna continue looking out there, but if anybody has faced this issue and has been able to solve it, it would be great if you could explain how you did it! Thank you,</p>

---

## Post #2 by @lassoan (2021-07-21 19:46 UTC)

<p>The Slicer community got VMTK updated for VTK9 (see <a href="https://github.com/vmtk/vmtk/pull/372" class="inline-onebox">Add support for building against VTK 9.0 and remove support for VTK 7.1 by jcfr · Pull Request #372 · vmtk/vmtk · GitHub</a>). It’ll be probably merged within a few weeks, after thorough testing in Slicer’s Python environment. After that we’ll work on PyPI submission.</p>
<p>I don’t think there is anyone planning to support conda builds, but if you were inrerested then give it a try and set it up. If everything works well for you then I’m sure the official recipes can be updated accordingly.</p>

---

## Post #3 by @perecanals (2021-07-22 09:51 UTC)

<p>Thank you for your quick response! I guess I will wait for the official submission on PyPI, I understand that should make the installation work on my system. I don’t think I have the skill to try and make the installation work through conda on my system, and I don’t really have a preference for conda anyway.</p>

---
