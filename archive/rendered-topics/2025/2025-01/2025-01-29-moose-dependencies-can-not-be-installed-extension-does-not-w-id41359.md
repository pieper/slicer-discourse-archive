---
topic_id: 41359
title: "Moose Dependencies Can Not Be Installed Extension Does Not W"
date: 2025-01-29
url: https://discourse.slicer.org/t/41359
---

# MOOSE dependencies can not be installed - extension does not work

**Topic ID**: 41359
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/moose-dependencies-can-not-be-installed-extension-does-not-work/41359

---

## Post #1 by @MaxVs (2025-01-29 15:29 UTC)

<p>As the newest version 5.9.0 appeard, I found some new extensions.<br>
One of these is MOOSE extension, but unfortunatelly it doesnt work.<br>
Every time I click install dependencies, I wait even couple hours and nothing happens.<br>
All I can see is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdd0d27f7023bb901d03f1fea656de7f29e8b232.png" data-download-href="/uploads/short-url/r5bDM4hsKfkjvzPBFAXz9H7laZs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdd0d27f7023bb901d03f1fea656de7f29e8b232.png" alt="image" data-base62-sha1="r5bDM4hsKfkjvzPBFAXz9H7laZs" width="572" height="247"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">572×247 7.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would be great if someone can tell me if had the same problem, or solved it, and how <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @muratmaga (2025-01-29 15:48 UTC)

<aside class="quote no-group" data-username="MaxVs" data-post="1" data-topic="41359">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/maxvs/48/81480_2.png" class="avatar"> MaxVs:</div>
<blockquote>
<p>Every time I click install dependencies, I wait even couple hours and nothing happens.<br>
All I can see is:</p>
</blockquote>
</aside>
<p>It would be helpful if you can provide the log file (CTRL + 0). Also what OS are you running? On MacOS with 5.8.0 it seems to install the dependencies fine and starts the segmentation task.</p>

---

## Post #3 by @MaxVs (2025-01-29 15:50 UTC)

<p>I tried to use it on Windows 11… Is is available only on OS?</p>

---

## Post #4 by @muratmaga (2025-01-29 15:52 UTC)

<p>No, it is available. but it looks like Moose brings a lot of python packages. If one of them is not available or has issues, it will probaby not going to work. THat’s why you want to look into your log file and see if there are any errors reported.</p>
<pre><code class="lang-auto">Collecting torch
  Using cached torch-2.2.2-cp39-none-macosx_10_9_x86_64.whl.metadata (25 kB)
Collecting filelock (from torch)
  Downloading filelock-3.17.0-py3-none-any.whl.metadata (2.9 kB)
Requirement already satisfied: typing-extensions&gt;=4.8.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (4.12.1)
Collecting sympy (from torch)
  Downloading sympy-1.13.3-py3-none-any.whl.metadata (12 kB)
Collecting networkx (from torch)
  Using cached networkx-3.2.1-py3-none-any.whl.metadata (5.2 kB)
Collecting jinja2 (from torch)
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting fsspec (from torch)
  Downloading fsspec-2024.12.0-py3-none-any.whl.metadata (11 kB)
Collecting MarkupSafe&gt;=2.0 (from jinja2-&gt;torch)
  Using cached MarkupSafe-3.0.2-cp39-cp39-macosx_10_9_universal2.whl.metadata (4.0 kB)
Collecting mpmath&lt;1.4,&gt;=1.1.0 (from sympy-&gt;torch)
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Using cached torch-2.2.2-cp39-none-macosx_10_9_x86_64.whl (150.8 MB)
Downloading filelock-3.17.0-py3-none-any.whl (16 kB)
Downloading fsspec-2024.12.0-py3-none-any.whl (183 kB)

Downloading jinja2-3.1.5-py3-none-any.whl (134 kB)

Using cached networkx-3.2.1-py3-none-any.whl (1.6 MB)
Downloading sympy-1.13.3-py3-none-any.whl (6.2 MB)

Downloading MarkupSafe-3.0.2-cp39-cp39-macosx_10_9_universal2.whl (14 kB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Installing collected packages: mpmath, sympy, networkx, MarkupSafe, fsspec, filelock, jinja2, torch
Successfully installed MarkupSafe-3.0.2 filelock-3.17.0 fsspec-2024.12.0 jinja2-3.1.5 mpmath-1.3.0 networkx-3.2.1 sympy-1.13.3 torch-2.2.2
Collecting git+https://github.com/Keyn34/MOOSE.git@SlicerMOOSE
  Cloning https://github.com/Keyn34/MOOSE.git (to revision SlicerMOOSE) to /private/var/folders/fj/1nyb9wg10hz1nmtq9kqvskwjt46qsd/T/pip-req-build-16gufprv
  Running command git clone --filter=blob:none --quiet https://github.com/Keyn34/MOOSE.git /private/var/folders/fj/1nyb9wg10hz1nmtq9kqvskwjt46qsd/T/pip-req-build-16gufprv
  Running command git checkout -b SlicerMOOSE --track origin/SlicerMOOSE
  Switched to a new branch 'SlicerMOOSE'
  branch 'SlicerMOOSE' set up to track 'origin/SlicerMOOSE'.
  Resolved https://github.com/Keyn34/MOOSE.git to commit b74dc7f909e5e68bba889cf985d36a6d858ff1b4
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting acvl-utils==0.2 (from moosez==3.0.6)
  Downloading acvl_utils-0.2.tar.gz (18 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting nnunetv2 (from moosez==3.0.6)
  Downloading nnunetv2-2.5.1.tar.gz (196 kB)

  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting halo~=0.0.31 (from moosez==3.0.6)
  Downloading halo-0.0.31.tar.gz (11 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: SimpleITK in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from moosez==3.0.6) (2.4.0rc2.dev213)
Collecting pydicom~=2.2.2 (from moosez==3.0.6)
  Downloading pydicom-2.2.2-py3-none-any.whl.metadata (6.4 kB)
Collecting argparse~=1.4.0 (from moosez==3.0.6)
  Downloading argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: numpy&lt;2.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from moosez==3.0.6) (1.26.4)
Collecting mpire~=2.3.3 (from moosez==3.0.6)
  Downloading mpire-2.3.5-py3-none-any.whl.metadata (11 kB)
Collecting openpyxl~=3.0.9 (from moosez==3.0.6)
  Downloading openpyxl-3.0.10-py2.py3-none-any.whl.metadata (2.4 kB)
Collecting pyfiglet~=0.8.post1 (from moosez==3.0.6)
  Downloading pyfiglet-0.8.post1-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting natsort~=8.1.0 (from moosez==3.0.6)
  Downloading natsort-8.1.0-py3-none-any.whl.metadata (20 kB)
Collecting colorama~=0.4.6 (from moosez==3.0.6)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting dask (from moosez==3.0.6)
  Downloading dask-2024.8.0-py3-none-any.whl.metadata (3.8 kB)
Collecting rich (from moosez==3.0.6)
  Downloading rich-13.9.4-py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: pandas in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from moosez==3.0.6) (2.2.3)
Collecting dicom2nifti~=2.4.8 (from moosez==3.0.6)
  Downloading dicom2nifti-2.4.11-py3-none-any.whl.metadata (1.3 kB)
Collecting matplotlib (from moosez==3.0.6)
  Using cached matplotlib-3.9.4-cp39-cp39-macosx_10_12_x86_64.whl.metadata (11 kB)
Collecting psutil (from moosez==3.0.6)
  Downloading psutil-6.1.1-cp36-abi3-macosx_10_9_x86_64.whl.metadata (22 kB)
Collecting nibabel (from moosez==3.0.6)
  Downloading nibabel-5.3.2-py3-none-any.whl.metadata (9.1 kB)
Collecting batchgenerators (from acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading batchgenerators-0.25.1.tar.gz (76 kB)

  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: torch in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from acvl-utils==0.2-&gt;moosez==3.0.6) (2.2.2)
Collecting scikit-image (from acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading scikit_image-0.24.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (14 kB)
Collecting connected-components-3d (from acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading connected_components_3d-3.22.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (32 kB)
Requirement already satisfied: scipy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from dicom2nifti~=2.4.8-&gt;moosez==3.0.6) (1.13.1)
Collecting python-gdcm (from dicom2nifti~=2.4.8-&gt;moosez==3.0.6)
  Downloading python_gdcm-3.0.24.1-cp39-cp39-macosx_10_9_x86_64.whl.metadata (3.7 kB)
Collecting log_symbols&gt;=0.0.14 (from halo~=0.0.31-&gt;moosez==3.0.6)
  Downloading log_symbols-0.0.14-py3-none-any.whl.metadata (523 bytes)
Collecting spinners&gt;=0.0.24 (from halo~=0.0.31-&gt;moosez==3.0.6)
  Downloading spinners-0.0.24-py3-none-any.whl.metadata (576 bytes)
Collecting termcolor&gt;=1.1.0 (from halo~=0.0.31-&gt;moosez==3.0.6)
  Downloading termcolor-2.5.0-py3-none-any.whl.metadata (6.1 kB)
Requirement already satisfied: six&gt;=1.12.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from halo~=0.0.31-&gt;moosez==3.0.6) (1.16.0)
Collecting tqdm (from mpire~=2.3.3-&gt;moosez==3.0.6)
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)

Collecting et-xmlfile (from openpyxl~=3.0.9-&gt;moosez==3.0.6)
  Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
Collecting click&gt;=8.1 (from dask-&gt;moosez==3.0.6)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting cloudpickle&gt;=1.5.0 (from dask-&gt;moosez==3.0.6)
  Downloading cloudpickle-3.1.1-py3-none-any.whl.metadata (7.1 kB)
Requirement already satisfied: fsspec&gt;=2021.09.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from dask-&gt;moosez==3.0.6) (2024.12.0)
Requirement already satisfied: packaging&gt;=20.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from dask-&gt;moosez==3.0.6) (24.0)
Collecting partd&gt;=1.4.0 (from dask-&gt;moosez==3.0.6)
  Downloading partd-1.4.2-py3-none-any.whl.metadata (4.6 kB)
Collecting pyyaml&gt;=5.3.1 (from dask-&gt;moosez==3.0.6)
  Downloading PyYAML-6.0.2-cp39-cp39-macosx_10_9_x86_64.whl.metadata (2.1 kB)
Collecting toolz&gt;=0.10.0 (from dask-&gt;moosez==3.0.6)
  Downloading toolz-1.0.0-py3-none-any.whl.metadata (5.1 kB)
Collecting importlib-metadata&gt;=4.13.0 (from dask-&gt;moosez==3.0.6)
  Downloading importlib_metadata-8.6.1-py3-none-any.whl.metadata (4.7 kB)
Collecting contourpy&gt;=1.0.1 (from matplotlib-&gt;moosez==3.0.6)
  Using cached contourpy-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl.metadata (5.4 kB)
Collecting cycler&gt;=0.10 (from matplotlib-&gt;moosez==3.0.6)
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools&gt;=4.22.0 (from matplotlib-&gt;moosez==3.0.6)
  Downloading fonttools-4.55.7-cp39-cp39-macosx_10_9_x86_64.whl.metadata (100 kB)

Collecting kiwisolver&gt;=1.3.1 (from matplotlib-&gt;moosez==3.0.6)
  Using cached kiwisolver-1.4.7-cp39-cp39-macosx_10_9_x86_64.whl.metadata (6.3 kB)
Requirement already satisfied: pillow&gt;=8 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from matplotlib-&gt;moosez==3.0.6) (10.3.0)
Requirement already satisfied: pyparsing&gt;=2.3.1 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from matplotlib-&gt;moosez==3.0.6) (3.1.2)
Requirement already satisfied: python-dateutil&gt;=2.7 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from matplotlib-&gt;moosez==3.0.6) (2.9.0.post0)
Collecting importlib-resources&gt;=3.2.0 (from matplotlib-&gt;moosez==3.0.6)
  Downloading importlib_resources-6.5.2-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: typing-extensions&gt;=4.6 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nibabel-&gt;moosez==3.0.6) (4.12.1)
Collecting dynamic-network-architectures&lt;0.4,&gt;=0.3.1 (from nnunetv2-&gt;moosez==3.0.6)
  Downloading dynamic_network_architectures-0.3.1.tar.gz (20 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: scikit-learn in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nnunetv2-&gt;moosez==3.0.6) (1.6.1)
Collecting graphviz (from nnunetv2-&gt;moosez==3.0.6)
  Downloading graphviz-0.20.3-py3-none-any.whl.metadata (12 kB)
Collecting tifffile (from nnunetv2-&gt;moosez==3.0.6)
  Downloading tifffile-2024.8.30-py3-none-any.whl.metadata (31 kB)
Requirement already satisfied: requests in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from nnunetv2-&gt;moosez==3.0.6) (2.32.3)
Collecting seaborn (from nnunetv2-&gt;moosez==3.0.6)
  Downloading seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
Collecting imagecodecs (from nnunetv2-&gt;moosez==3.0.6)
  Downloading imagecodecs-2024.12.30-cp39-cp39-macosx_10_14_x86_64.whl.metadata (19 kB)
Collecting yacs (from nnunetv2-&gt;moosez==3.0.6)
  Downloading yacs-0.1.8-py3-none-any.whl.metadata (639 bytes)
Collecting batchgeneratorsv2&gt;=0.2 (from nnunetv2-&gt;moosez==3.0.6)
  Downloading batchgeneratorsv2-0.2.1.tar.gz (34 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting einops (from nnunetv2-&gt;moosez==3.0.6)
  Downloading einops-0.8.0-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: pytz&gt;=2020.1 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from pandas-&gt;moosez==3.0.6) (2024.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from pandas-&gt;moosez==3.0.6) (2025.1)
Collecting markdown-it-py&gt;=2.2.0 (from rich-&gt;moosez==3.0.6)
  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting pygments&lt;3.0.0,&gt;=2.13.0 (from rich-&gt;moosez==3.0.6)
  Downloading pygments-2.19.1-py3-none-any.whl.metadata (2.5 kB)
Collecting future (from batchgenerators-&gt;acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
Collecting unittest2 (from batchgenerators-&gt;acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading unittest2-1.1.0-py2.py3-none-any.whl.metadata (15 kB)
Requirement already satisfied: threadpoolctl in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from batchgenerators-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (3.5.0)
Collecting fft-conv-pytorch (from batchgeneratorsv2&gt;=0.2-&gt;nnunetv2-&gt;moosez==3.0.6)
  Downloading fft_conv_pytorch-1.2.0-py3-none-any.whl.metadata (2.8 kB)
Collecting zipp&gt;=3.20 (from importlib-metadata&gt;=4.13.0-&gt;dask-&gt;moosez==3.0.6)
  Using cached zipp-3.21.0-py3-none-any.whl.metadata (3.7 kB)
Collecting mdurl~=0.1 (from markdown-it-py&gt;=2.2.0-&gt;rich-&gt;moosez==3.0.6)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting locket (from partd&gt;=1.4.0-&gt;dask-&gt;moosez==3.0.6)
  Downloading locket-1.0.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: networkx&gt;=2.8 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from scikit-image-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (3.2.1)
Collecting imageio&gt;=2.33 (from scikit-image-&gt;acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading imageio-2.37.0-py3-none-any.whl.metadata (5.2 kB)
Collecting lazy-loader&gt;=0.4 (from scikit-image-&gt;acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading lazy_loader-0.4-py3-none-any.whl.metadata (7.6 kB)
Requirement already satisfied: filelock in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (3.17.0)
Requirement already satisfied: sympy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (1.13.3)
Requirement already satisfied: jinja2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (3.1.5)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from requests-&gt;nnunetv2-&gt;moosez==3.0.6) (3.3.2)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from requests-&gt;nnunetv2-&gt;moosez==3.0.6) (3.7)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from requests-&gt;nnunetv2-&gt;moosez==3.0.6) (2.2.1)
Requirement already satisfied: certifi&gt;=2017.4.17 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from requests-&gt;nnunetv2-&gt;moosez==3.0.6) (2024.2.2)
Requirement already satisfied: joblib&gt;=1.2.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from scikit-learn-&gt;nnunetv2-&gt;moosez==3.0.6) (1.4.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from jinja2-&gt;torch-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (3.0.2)
Requirement already satisfied: mpmath&lt;1.4,&gt;=1.1.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from sympy-&gt;torch-&gt;acvl-utils==0.2-&gt;moosez==3.0.6) (1.3.0)
Collecting traceback2 (from unittest2-&gt;batchgenerators-&gt;acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading traceback2-1.4.0-py2.py3-none-any.whl.metadata (1.5 kB)
Collecting linecache2 (from traceback2-&gt;unittest2-&gt;batchgenerators-&gt;acvl-utils==0.2-&gt;moosez==3.0.6)
  Downloading linecache2-1.0.0-py2.py3-none-any.whl.metadata (1000 bytes)
Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading dicom2nifti-2.4.11-py3-none-any.whl (43 kB)

Downloading mpire-2.3.5-py3-none-any.whl (284 kB)

Downloading natsort-8.1.0-py3-none-any.whl (37 kB)
Downloading openpyxl-3.0.10-py2.py3-none-any.whl (242 kB)

Downloading pydicom-2.2.2-py3-none-any.whl (2.0 MB)

Downloading pyfiglet-0.8.post1-py2.py3-none-any.whl (865 kB)

Downloading dask-2024.8.0-py3-none-any.whl (1.2 MB)

Using cached matplotlib-3.9.4-cp39-cp39-macosx_10_12_x86_64.whl (7.9 MB)
Downloading nibabel-5.3.2-py3-none-any.whl (3.3 MB)

Downloading psutil-6.1.1-cp36-abi3-macosx_10_9_x86_64.whl (247 kB)

Downloading rich-13.9.4-py3-none-any.whl (242 kB)

Downloading click-8.1.8-py3-none-any.whl (98 kB)

Downloading cloudpickle-3.1.1-py3-none-any.whl (20 kB)
Using cached contourpy-1.3.0-cp39-cp39-macosx_10_9_x86_64.whl (265 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.55.7-cp39-cp39-macosx_10_9_x86_64.whl (2.3 MB)

Downloading importlib_metadata-8.6.1-py3-none-any.whl (26 kB)
Downloading importlib_resources-6.5.2-py3-none-any.whl (37 kB)
Using cached kiwisolver-1.4.7-cp39-cp39-macosx_10_9_x86_64.whl (65 kB)
Downloading log_symbols-0.0.14-py3-none-any.whl (3.1 kB)
Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Downloading partd-1.4.2-py3-none-any.whl (18 kB)
Downloading pygments-2.19.1-py3-none-any.whl (1.2 MB)

Downloading PyYAML-6.0.2-cp39-cp39-macosx_10_9_x86_64.whl (184 kB)

Downloading scikit_image-0.24.0-cp39-cp39-macosx_10_9_x86_64.whl (14.1 MB)

Downloading spinners-0.0.24-py3-none-any.whl (5.5 kB)
Downloading termcolor-2.5.0-py3-none-any.whl (7.8 kB)
Downloading tifffile-2024.8.30-py3-none-any.whl (227 kB)

Downloading toolz-1.0.0-py3-none-any.whl (56 kB)

Downloading connected_components_3d-3.22.0-cp39-cp39-macosx_10_9_x86_64.whl (802 kB)

Downloading einops-0.8.0-py3-none-any.whl (43 kB)

Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Downloading graphviz-0.20.3-py3-none-any.whl (47 kB)

Downloading imagecodecs-2024.12.30-cp39-cp39-macosx_10_14_x86_64.whl (18.0 MB)

Downloading python_gdcm-3.0.24.1-cp39-cp39-macosx_10_9_x86_64.whl (12.7 MB)

Downloading seaborn-0.13.2-py3-none-any.whl (294 kB)

Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)

Downloading yacs-0.1.8-py3-none-any.whl (14 kB)
Downloading imageio-2.37.0-py3-none-any.whl (315 kB)

Downloading lazy_loader-0.4-py3-none-any.whl (12 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Using cached zipp-3.21.0-py3-none-any.whl (9.6 kB)
Downloading fft_conv_pytorch-1.2.0-py3-none-any.whl (6.8 kB)
Downloading future-1.0.0-py3-none-any.whl (491 kB)

Downloading locket-1.0.0-py2.py3-none-any.whl (4.4 kB)
Downloading unittest2-1.1.0-py2.py3-none-any.whl (96 kB)

Downloading traceback2-1.4.0-py2.py3-none-any.whl (16 kB)
Downloading linecache2-1.0.0-py2.py3-none-any.whl (12 kB)
Building wheels for collected packages: moosez, acvl-utils, halo, nnunetv2, batchgenerators, batchgeneratorsv2, dynamic-network-architectures
  Building wheel for moosez (setup.py): started
  Building wheel for moosez (setup.py): finished with status 'done'
  Created wheel for moosez: filename=moosez-3.0.6-py3-none-any.whl size=39657 sha256=fbdbde94d706c0186bfb766577970260afc6d7ae35ed0222e0b6e0f65f1f7a22
  Stored in directory: /private/var/folders/fj/1nyb9wg10hz1nmtq9kqvskwjt46qsd/T/pip-ephem-wheel-cache-2hwkvaty/wheels/87/92/26/cd3075c30751fa3f01c8d0eff9755f35325c053eb19ecd8e2d
  Building wheel for acvl-utils (setup.py): started
  Building wheel for acvl-utils (setup.py): finished with status 'done'
  Created wheel for acvl-utils: filename=acvl_utils-0.2-py3-none-any.whl size=22438 sha256=f60c2f10be5533fb8f847a858b36f192d8c99732502e39fe7b36f050d6fd86e9
  Stored in directory: /Users/amaga/Library/Caches/pip/wheels/db/79/df/6ffb48299bba36fd2fc5d14dc8ae7d1caa3416aa7e96d605b7
  Building wheel for halo (setup.py): started
  Building wheel for halo (setup.py): finished with status 'done'
  Created wheel for halo: filename=halo-0.0.31-py3-none-any.whl size=11232 sha256=0fa82b99f082921174dea203774d2fd7b93a5d5396e82aadcaed3fe88bcec38f
  Stored in directory: /Users/amaga/Library/Caches/pip/wheels/bb/85/47/b7c7338ab52808105f937bd8c04aec5d98a543311ac2c8bed2
  Building wheel for nnunetv2 (pyproject.toml): started
  Building wheel for nnunetv2 (pyproject.toml): finished with status 'done'
  Created wheel for nnunetv2: filename=nnunetv2-2.5.1-py3-none-any.whl size=264369 sha256=317ef6e69d7c89cfb82f10b47b01c34342b32fe43998f8051a3feb11c9671266
  Stored in directory: /Users/amaga/Library/Caches/pip/wheels/7b/85/af/51e5381b7cf9cc417ca071b9cd6e35afc59236a0ebb4462249
  Building wheel for batchgenerators (setup.py): started
  Building wheel for batchgenerators (setup.py): finished with status 'done'
  Created wheel for batchgenerators: filename=batchgenerators-0.25.1-py3-none-any.whl size=93093 sha256=e00d7cacba78345a19aa659b2fc33e37cc53eff7322b315fe6bba67e4bcb1daf
  Stored in directory: /Users/amaga/Library/Caches/pip/wheels/97/8d/b9/3a9435d619b6a4bcd98f8cb8b324da29b6173555bb80860bdd
  Building wheel for batchgeneratorsv2 (pyproject.toml): started
  Building wheel for batchgeneratorsv2 (pyproject.toml): finished with status 'done'
  Created wheel for batchgeneratorsv2: filename=batchgeneratorsv2-0.2.1-py3-none-any.whl size=45187 sha256=e68e69a34705856d48dbf19313c670b48399a3ac19a948dcae4ea01e33044980
  Stored in directory: /Users/amaga/Library/Caches/pip/wheels/8c/29/14/3fdf4a97638724355746fb142b55db6868f1c0f1698af26ebd
  Building wheel for dynamic-network-architectures (setup.py): started
  Building wheel for dynamic-network-architectures (setup.py): finished with status 'done'
  Created wheel for dynamic-network-architectures: filename=dynamic_network_architectures-0.3.1-py3-none-any.whl size=30051 sha256=3e434889e376b36ee09e485f2f0ef207dca923a10b4f386bedd37df295c2a1c7
  Stored in directory: /Users/amaga/Library/Caches/pip/wheels/ec/59/c1/e65ad8b5ac7df95651f913251875b4cc8275644e0e28e82c63
Successfully built moosez acvl-utils halo nnunetv2 batchgenerators batchgeneratorsv2 dynamic-network-architectures
Installing collected packages: spinners, pyfiglet, linecache2, argparse, zipp, traceback2, tqdm, toolz, tifffile, termcolor, pyyaml, python-gdcm, pygments, pydicom, psutil, natsort, mdurl, locket, lazy-loader, kiwisolver, imageio, imagecodecs, graphviz, future, fonttools, et-xmlfile, einops, cycler, contourpy, connected-components-3d, colorama, cloudpickle, click, yacs, unittest2, scikit-image, partd, openpyxl, mpire, markdown-it-py, log_symbols, importlib-resources, importlib-metadata, rich, nibabel, matplotlib, halo, fft-conv-pytorch, dynamic-network-architectures, dask, batchgenerators, seaborn, dicom2nifti, batchgeneratorsv2, acvl-utils, nnunetv2, moosez
  Attempting uninstall: pydicom
    Found existing installation: pydicom 2.4.4
    Uninstalling pydicom-2.4.4:
      Successfully uninstalled pydicom-2.4.4
Successfully installed acvl-utils-0.2 argparse-1.4.0 batchgenerators-0.25.1 batchgeneratorsv2-0.2.1 click-8.1.8 cloudpickle-3.1.1 colorama-0.4.6 connected-components-3d-3.22.0 contourpy-1.3.0 cycler-0.12.1 dask-2024.8.0 dicom2nifti-2.4.11 dynamic-network-architectures-0.3.1 einops-0.8.0 et-xmlfile-2.0.0 fft-conv-pytorch-1.2.0 fonttools-4.55.7 future-1.0.0 graphviz-0.20.3 halo-0.0.31 imagecodecs-2024.12.30 imageio-2.37.0 importlib-metadata-8.6.1 importlib-resources-6.5.2 kiwisolver-1.4.7 lazy-loader-0.4 linecache2-1.0.0 locket-1.0.0 log_symbols-0.0.14 markdown-it-py-3.0.0 matplotlib-3.9.4 mdurl-0.1.2 moosez-3.0.6 mpire-2.3.5 natsort-8.1.0 nibabel-5.3.2 nnunetv2-2.5.1 openpyxl-3.0.10 partd-1.4.2 psutil-6.1.1 pydicom-2.2.2 pyfiglet-0.8.post1 pygments-2.19.1 python-gdcm-3.0.24.1 pyyaml-6.0.2 rich-13.9.4 scikit-image-0.24.0 seaborn-0.13.2 spinners-0.0.24 termcolor-2.5.0 tifffile-2024.8.30 toolz-1.0.0 tqdm-4.67.1 traceback2-1.4.0 unittest2-1.1.0 yacs-0.1.8 zipp-3.21.0
</code></pre>

---

## Post #5 by @MaxVs (2025-01-29 16:01 UTC)

<p>Okey! Thanks, here it is <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20250129_165911<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.9.0-2025-01-26 (revision 33428 / 2a19ce0) win-amd64 - installed release<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 26100, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 65460 MB physical, 69556 MB virtual<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 7 5700X 8-Core Processor             , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/Bartek/AppData/Local/slicer.org/Slicer 5.9.0-2025-01-26/bin<br>
[DEBUG][Qt] 29.01.2025 16:59:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-33428/AirwaySegmentation/lib/Slicer-5.9/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/AirwaySegmentation/lib/Slicer-5.9/cli-modules</a>, <a href="http://slicer.org/Extensions-33428/AirwaySegmentation/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/AirwaySegmentation/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/TotalSegmentator/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/TissueSegmentation/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/TissueSegmentation/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SurfaceWrapSolidify/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SurfaceWrapSolidify/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SurfaceFragmentsRegistration/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SurfaceFragmentsRegistration/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerVMTK/lib/Slicer-5.9/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerVMTK/lib/Slicer-5.9/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerVMTK/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerVMTK/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerPythonTestRunner/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerPythonTestRunner/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerDevelopmentToolbox/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerDevelopmentToolbox/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerDentalModelSeg/lib/Slicer-5.9/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerDentalModelSeg/lib/Slicer-5.9/cli-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerDentalModelSeg/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerDentalModelSeg/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerConda/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerConda/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SkullStripper/lib/Slicer-5.9/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SkullStripper/lib/Slicer-5.9/cli-modules</a>, <a href="http://slicer.org/Extensions-33428/AutomatedDentalTools/lib/Slicer-5.9/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/AutomatedDentalTools/lib/Slicer-5.9/cli-modules</a>, <a href="http://slicer.org/Extensions-33428/AutomatedDentalTools/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/AutomatedDentalTools/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/BrainVolumeRefinement/lib/Slicer-5.9/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/BrainVolumeRefinement/lib/Slicer-5.9/cli-modules</a>, <a href="http://slicer.org/Extensions-33428/CurveMaker/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/CurveMaker/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/DCMQI/lib/Slicer-5.9/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/DCMQI/lib/Slicer-5.9/cli-modules</a>, <a href="http://slicer.org/Extensions-33428/DebuggingTools/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/DebuggingTools/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/DentalSegmentator/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/DentalSegmentator/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/ExtraMarkups/lib/Slicer-5.9/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/ExtraMarkups/lib/Slicer-5.9/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-33428/HDBrainExtraction/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/HDBrainExtraction/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/MONAIAuto3DSeg/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/MONAIAuto3DSeg/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/MONAILabel/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/MONAILabel/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/MONAIViz/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/MONAIViz/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/MarkupsToModel/lib/Slicer-5.9/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/MarkupsToModel/lib/Slicer-5.9/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-33428/NNUNet/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/NNUNet/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/PyTorch/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/PyTorch/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/QuantitativeReporting/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/QuantitativeReporting/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/Sandbox/lib/Slicer-5.9/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/Sandbox/lib/Slicer-5.9/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-33428/Sandbox/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/Sandbox/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SegmentEditorExtraEffects/lib/Slicer-5.9/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SegmentEditorExtraEffects/lib/Slicer-5.9/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-33428/SegmentEditorExtraEffects/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SegmentEditorExtraEffects/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SegmentationVerification/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SegmentationVerification/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerMOOSE/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerMOOSE/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SegmentHumanBody/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SegmentHumanBody/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/RVXLiverSegmentation/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/RVXLiverSegmentation/lib/Slicer-5.9/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-33428/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-33428/SlicerElastix/lib/Slicer-5.9/qt-scripted-modules</a><br>
[CRITICAL][Qt] 29.01.2025 16:59:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
CLI executable: C:/Users/Bartek/AppData/Local/slicer.org/Slicer 5.9.0-2025-01-26/slicer.org/Extensions-33428/SlicerVMTK/lib/Slicer-5.9/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 29.01.2025 16:59:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 29.01.2025 16:59:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 29.01.2025 16:59:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 29.01.2025 16:59:14 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 29.01.2025 16:59:14 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 29.01.2025 16:59:15 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Python] 29.01.2025 16:59:15 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: Elastix<br>
[DEBUG][Python] 29.01.2025 16:59:17 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:341) - matplotlib data path: C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib\mpl-data<br>
[DEBUG][Python] 29.01.2025 16:59:17 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:341) - CONFIGDIR=C:\Users\Bartek.matplotlib<br>
[DEBUG][Python] 29.01.2025 16:59:17 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:1512) - interactive is False<br>
[DEBUG][Python] 29.01.2025 16:59:17 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:1513) - platform is win32<br>
[DEBUG][Python] 29.01.2025 16:59:17 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib_<em>init</em>_.py:341) - CACHEDIR=C:\Users\Bartek.matplotlib<br>
[DEBUG][Python] 29.01.2025 16:59:17 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\lib\Python\Lib\site-packages\matplotlib\font_manager.py:1580) - Using fontManager instance from C:\Users\Bartek.matplotlib\fontlist-v390.json<br>
[DEBUG][Qt] 29.01.2025 16:59:24 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “MOOSE”<br>
[INFO][Python] 29.01.2025 16:59:26 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\slicer.org\Extensions-33428\PyTorch\lib\Slicer-5.9\qt-scripted-modules\PyTorchUtils.py:153) - Importing torch…<br>
[INFO][Python] 29.01.2025 16:59:26 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\slicer.org\Extensions-33428\PyTorch\lib\Slicer-5.9\qt-scripted-modules\PyTorchUtils.py:190) - PyTorch 2.5.1+cu124 imported successfully<br>
[INFO][Python] 29.01.2025 16:59:26 [Python] (C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\slicer.org\Extensions-33428\PyTorch\lib\Slicer-5.9\qt-scripted-modules\PyTorchUtils.py:191) - CUDA available: True<br>
[INFO][Stream] 29.01.2025 16:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting git+https://github.com/Keyn34/MOOSE.git@SlicerMOOSE<br>
[INFO][Stream] 29.01.2025 16:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Cloning <a href="https://github.com/Keyn34/MOOSE.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Keyn34/MOOSE: MOOSE (Multi-organ objective segmentation) a data-centric AI solution that generates multilabel organ segmentations to facilitate systemic TB whole-person research.The pipeline is based on nn-UNet and has the capability to segment 120 unique tissue classes from a whole-body 18F-FDG PET/CT image.</a> (to revision SlicerMOOSE) to c:\users\bartek\appdata\local\temp\pip-req-build-2cq_jshj<br>
[INFO][Stream] 29.01.2025 16:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 29.01.2025 16:59:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ERROR: Cannot find command ‘git’ - do you have ‘git’ installed and in your PATH?<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/Bartek/AppData/Local/slicer.org/Slicer 5.9.0-2025-01-26/slicer.org/Extensions-33428/SlicerMOOSE/lib/Slicer-5.9/qt-scripted-modules/MOOSE.py”, line 117, in button_install_dependencies_clicked<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     slicer.util.pip_install(“git+https://github.com/Keyn34/MOOSE.git@SlicerMOOSE”)<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\bin\Python\slicer\util.py”, line 3942, in pip_install<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     _executePythonModule(“pip”, args)<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\bin\Python\slicer\util.py”, line 3896, in _executePythonModule<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     logProcessOutput(proc)<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\Bartek\AppData\Local\slicer.org\Slicer 5.9.0-2025-01-26\bin\Python\slicer\util.py”, line 3862, in logProcessOutput<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
[CRITICAL][Stream] 29.01.2025 16:59:27 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - subprocess.CalledProcessError: Command ‘[‘C:/Users/Bartek/AppData/Local/slicer.org/Slicer 5.9.0-2025-01-26/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/Keyn34/MOOSE.git@SlicerMOOSE’]’ returned non-zero exit status 1.</p>

---

## Post #6 by @jamesobutler (2025-01-29 16:25 UTC)

<p>I’ve reported the issue to the SlicerMOOSE developers. You can track the work at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/mprires/SlicerMOOSE/issues/2">
  <header class="source">

      <a href="https://github.com/mprires/SlicerMOOSE/issues/2" target="_blank" rel="noopener nofollow ugc">github.com/mprires/SlicerMOOSE</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/mprires/SlicerMOOSE/issues/2" target="_blank" rel="noopener nofollow ugc">User unable to install MOOSE when missing git</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-01-29" data-time="16:24:33" data-timezone="UTC">04:24PM - 29 Jan 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As originally reported at https://discourse.slicer.org/t/moose-dependencies-can-<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">not-be-installed-extension-does-not-work/41359/5?u=jamesobutler, a user is unable to install MOOSE successfully because they do not have git installed on their computer. It is expected for users of Slicer to not have dev tools like git.

https://github.com/mprires/SlicerMOOSE/blob/d54bfc5103ea8459ac2a5acbcef7db3d4b37f73b/MOOSE/MOOSE.py#L117

@Keyn34 is there a valid MOOSE version on PyPI that can be pulled instead of using latest master? You could also change the code below to point to the https link to download the zip instead of using git. See how SlicerTotalSegmentator does it [here](https://github.com/lassoan/SlicerTotalSegmentator/blob/c9dc3cf479a6463d3d17ca40b66de18156d06247/TotalSegmentator/TotalSegmentator.py#L373).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @MaxVs (2025-01-29 16:37 UTC)

<p>I’ll track the topic till they’ll find the solution. Thank you very much!</p>

---
