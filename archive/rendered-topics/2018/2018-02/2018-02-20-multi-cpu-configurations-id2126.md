# Multi CPU configurations

**Topic ID**: 2126
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/multi-cpu-configurations/2126

---

## Post #1 by @ssousa (2018-02-20 16:03 UTC)

<p>Operating system:Ubuntu<br>
Slicer version:4.8.</p>
<p>Please can you help me in the multi CPU configurations to use with 3D Slicer. Is there any script that we can use?<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2018-02-20 16:43 UTC)

<p>Can you give a bit more detailed description of what you would like to achieve?</p>

---

## Post #3 by @ssousa (2018-02-20 17:43 UTC)

<p>Thanks for your fast reply. I would like to run UKF tractography for several subjects, using<br>
a computer cluster. Therefore I would like to know which are the needed configurations for the setup.</p>
<p>-------- Mensagem original --------</p>

---

## Post #4 by @jcfr (2018-02-20 18:18 UTC)

<p>Hi <a class="mention" href="/u/ssousa">@ssousa</a>,</p>
<p>Here are few more questions that will help answer:</p>
<p>Are you able to install Slicer on the different node of the cluster ?</p>
<p>If not, is there docker installed on each node ?</p>
<p>Is there a shared filesystem or do you have to transfer the data to each compute node ?</p>
<p>Last, what do you use to orchestrate the job on your cluster ?</p>

---

## Post #5 by @ssousa (2018-02-20 22:30 UTC)

<p>Hi Jean Christophe. Thanks for your prompt reply!</p>
<p>Please see answers to your queries below.</p>

---

## Post #6 by @ssousa (2018-02-20 22:41 UTC)

<blockquote>
<p>Are you able to install Slicer on the different node of the cluster ?</p>
</blockquote>
<p>YES</p>
<blockquote>
<p>Is there a shared filesystem or do you have to transfer the data to each compute node ?</p>
</blockquote>
<p>WE MAY USE A SHARED FILESYSTEM</p>
<blockquote>
<p>Last, what do you use to orchestrate the job on your cluster ?</p>
</blockquote>
<p>USING A R or MATLAB SCRIPT on LINUX?</p>

---
