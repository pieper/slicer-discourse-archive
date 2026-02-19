---
topic_id: 45451
title: "Can The Nninteractive Server Environment Be In A Read Only F"
date: 2025-12-11
url: https://discourse.slicer.org/t/45451
---

# Can the nninteractive server environment be in a read-only folder

**Topic ID**: 45451
**Date**: 2025-12-11
**URL**: https://discourse.slicer.org/t/can-the-nninteractive-server-environment-be-in-a-read-only-folder/45451

---

## Post #1 by @muratmaga (2025-12-11 21:53 UTC)

<p>During the workshops there are a lot of interest from biologists to use NNInteractive. However, it does take a while to set it up the server, particularly if you are not familiar that kind of thing.</p>
<p>In MorphoCloud, we can map a read-only share to our instances. If I create the virtual environment and install the NNinteractive server there, can the users safely activate the environment and run the the command <code>nninteractive-slicer-server --host 0.0.0.0 --port 1527</code> from that location; i.e., does the server need any write access to the folder while its running.</p>

---

## Post #2 by @pieper (2025-12-11 22:36 UTC)

<p>Yes, I would think so.  Should be easy to try.</p>

---

## Post #3 by @muratmaga (2025-12-12 16:21 UTC)

<p>It seems to work locally. I think I will test on MorphoCloud next workshop.</p>
<p>Meanwhile, it would be nice if the NNINteractive can be self-contained and install the server under Slicer. That way its footprint will be a bit smaller and possibly time to install to start using will be faster as there won’t be two different copies torch and other cuda related large libraries installed in two different environment (venv for the server, and inside the Slicer for the extension itself).</p>

---

## Post #4 by @muratmaga (2025-12-12 16:43 UTC)

<p>For posterity here are the instructions:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive/QuickStart_on_MC.MD">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive/QuickStart_on_MC.MD" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive/QuickStart_on_MC.MD" target="_blank" rel="noopener nofollow ugc">MorphoCloud/NNInteractive/QuickStart_on_MC.MD</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive/QuickStart_on_MC.MD" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md">## Run NNinteractive without installing any libraries:

We maintain a python virtual environment all necessary files for running the NNInteractiver server is install. For quick tests, it might be faster to use this environment instead of creating one for yourself as explained in the NNInteractive readme.  There are a few downsides of using this environment: 

1. If the share is not available, you can't use it
2. It is a read-onl folder, you cannot make changes if things don't work out for you.

As such, if you are planning to use NNInteractive regularly, we still suggest creating your own python virtual environment where you have the full control over. 

Here are the quick instructions.
1. First paste this command in a terminal window to map the share that contains NNinteractive virtual environment (one time setup):
```
curl https://jetstream2.exosphere.app/exosphere/assets/scripts/mount_ceph.py | sudo python3 - mount \
  --access-rule-name="NNInteractive-ro" \
  --access-rule-key="AQCMQTxpTikzNxAAssyTNC8+spC8seJJVnZ+BQ==" \
  --share-path="149.165.158.38:6789,149.165.158.22:6789,149.165.158.54:6789,149.165.158.70:6789,149.165.158.86:6789:/volumes/_nogroup/b27879c9-bfd4-4290-a87e-91a3dad87107/55c933bc-5291-450d-997c-ee407a05c740" \
  --share-name="NNInteractive"
```
2. In the same window, type this command to activate the environment
```
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MorphoCloud/NNInteractive/QuickStart_on_MC.MD" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
