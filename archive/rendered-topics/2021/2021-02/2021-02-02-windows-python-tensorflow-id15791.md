---
topic_id: 15791
title: "Windows Python Tensorflow"
date: 2021-02-02
url: https://discourse.slicer.org/t/15791
---

# Windows python tensorflow

**Topic ID**: 15791
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/windows-python-tensorflow/15791

---

## Post #1 by @dSC (2021-02-02 09:58 UTC)

<p>Hi Guys,</p>
<p>I’m trying to install tensorflow using the command  <strong>pip_install(‘tensorflow’).</strong><br>
The installation failed with this error:</p>
<p><em>ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: ‘C:\…\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\tensorflow\include\external\llvm-project\mlir\_virtual_includes\LinalgStructuredInterfacesIncGen\mlir\Dialect\Linalg\IR\LinalgStructuredOpsInterfaces.cpp.inc’</em></p>
<p>I solved this using:<br>
<strong>pip_install(’–user tensorflow’)</strong></p>
<p>I can look TF among the installed packages.</p>
<p>The issue is on:<br>
<strong>import tensorflow as tf</strong></p>
<p>that shows:<br>
<em>ModuleNotFoundError: No module named ‘tensorflow.python’</em></p>
<p>Can you help me?</p>
<p>Best<br>
dSc</p>
<p>NB under Ubuntu it works</p>

---

## Post #2 by @lassoan (2021-02-02 14:01 UTC)

<p>It works well for me for a recent Slicer Preview Release (see below). Probably your username is long (the file that is not found has an extremely long path, which may exceed maximum path length limitations) or contain non-ASCII characters. Install Slicer into a simpler shorter folder, such as C:\Test" and see if you can install tensorflow then.</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Jan 21 2021, 23:19:39) [MSC v.1924 64 bit (AMD64)] on win32

&gt;&gt;&gt; pip_install('tensorflow')

Collecting tensorflow

Downloading tensorflow-2.4.1-cp36-cp36m-win_amd64.whl (370.7 MB)

Requirement already satisfied: six~=1.15.0 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from tensorflow) (1.15.0)

Requirement already satisfied: wrapt~=1.12.1 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from tensorflow) (1.12.1)

Requirement already satisfied: numpy~=1.19.2 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from tensorflow) (1.19.2)

Requirement already satisfied: wheel~=0.35 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from tensorflow) (0.35.1)

Collecting gast==0.3.3

Using cached gast-0.3.3-py2.py3-none-any.whl (9.7 kB)

Collecting absl-py~=0.10

Downloading absl_py-0.11.0-py3-none-any.whl (127 kB)

Collecting astunparse~=1.6.3

Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)

Collecting flatbuffers~=1.12.0

Downloading flatbuffers-1.12-py2.py3-none-any.whl (15 kB)

Collecting google-pasta~=0.2

Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)

Collecting grpcio~=1.32.0

Downloading grpcio-1.32.0-cp36-cp36m-win_amd64.whl (2.6 MB)

Collecting h5py~=2.10.0

Using cached h5py-2.10.0-cp36-cp36m-win_amd64.whl (2.4 MB)

Collecting keras-preprocessing~=1.1.2

Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)

Collecting opt-einsum~=3.3.0

Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)

Collecting protobuf&gt;=3.9.2

Downloading protobuf-3.14.0-cp36-cp36m-win_amd64.whl (904 kB)

Collecting tensorboard~=2.4

Downloading tensorboard-2.4.1-py3-none-any.whl (10.6 MB)

Requirement already satisfied: requests&lt;3,&gt;=2.21.0 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from tensorboard~=2.4-&gt;tensorflow) (2.24.0)

Requirement already satisfied: setuptools&gt;=41.0.0 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from tensorboard~=2.4-&gt;tensorflow) (50.3.2)

Collecting google-auth&lt;2,&gt;=1.6.3

Downloading google_auth-1.24.0-py2.py3-none-any.whl (114 kB)

Collecting cachetools&lt;5.0,&gt;=2.0.0

Downloading cachetools-4.2.1-py3-none-any.whl (12 kB)

Collecting google-auth-oauthlib&lt;0.5,&gt;=0.4.1

Downloading google_auth_oauthlib-0.4.2-py2.py3-none-any.whl (18 kB)

Collecting markdown&gt;=2.6.8

Using cached Markdown-3.3.3-py3-none-any.whl (96 kB)

Collecting pyasn1-modules&gt;=0.2.1

Using cached pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)

Collecting pyasn1&lt;0.5.0,&gt;=0.4.6

Using cached pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)

Requirement already satisfied: idna&lt;3,&gt;=2.5 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from requests&lt;3,&gt;=2.21.0-&gt;tensorboard~=2.4-&gt;tensorflow) (2.10)

Requirement already satisfied: certifi&gt;=2017.4.17 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from requests&lt;3,&gt;=2.21.0-&gt;tensorboard~=2.4-&gt;tensorflow) (2020.6.20)

Requirement already satisfied: chardet&lt;4,&gt;=3.0.2 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from requests&lt;3,&gt;=2.21.0-&gt;tensorboard~=2.4-&gt;tensorflow) (3.0.4)

Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,&lt;1.26,&gt;=1.21.1 in c:\users\andra\appdata\local\na-mic\slicer 4.13.0-2021-01-20\lib\python\lib\site-packages (from requests&lt;3,&gt;=2.21.0-&gt;tensorboard~=2.4-&gt;tensorflow) (1.25.11)

Collecting requests-oauthlib&gt;=0.7.0

Using cached requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)

Collecting oauthlib&gt;=3.0.0

Using cached oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)

Collecting rsa&lt;5,&gt;=3.1.4

Downloading rsa-4.7-py3-none-any.whl (34 kB)

Collecting tensorboard-plugin-wit&gt;=1.6.0

Downloading tensorboard_plugin_wit-1.8.0-py3-none-any.whl (781 kB)

Collecting tensorflow-estimator&lt;2.5.0,&gt;=2.4.0

Downloading tensorflow_estimator-2.4.0-py2.py3-none-any.whl (462 kB)

Collecting termcolor~=1.1.0

Using cached termcolor-1.1.0-cp36-none-any.whl

Collecting typing-extensions~=3.7.4

Using cached typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)

Collecting werkzeug&gt;=0.11.15

Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)

Collecting importlib-metadata

Using cached importlib_metadata-3.4.0-py3-none-any.whl (10 kB)

Collecting zipp&gt;=0.5

Using cached zipp-3.4.0-py3-none-any.whl (5.2 kB)

Installing collected packages: pyasn1, zipp, typing-extensions, rsa, pyasn1-modules, oauthlib, cachetools, requests-oauthlib, importlib-metadata, google-auth, werkzeug, tensorboard-plugin-wit, protobuf, markdown, grpcio, google-auth-oauthlib, absl-py, termcolor, tensorflow-estimator, tensorboard, opt-einsum, keras-preprocessing, h5py, google-pasta, gast, flatbuffers, astunparse, tensorflow

WARNING: The scripts pyrsa-decrypt.exe, pyrsa-encrypt.exe, pyrsa-keygen.exe, pyrsa-priv2pub.exe, pyrsa-sign.exe and pyrsa-verify.exe are installed in 'C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-01-20\lib\Python\Scripts' which is not on PATH.

Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

WARNING: The script markdown_py.exe is installed in 'C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-01-20\lib\Python\Scripts' which is not on PATH.

Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

WARNING: The script google-oauthlib-tool.exe is installed in 'C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-01-20\lib\Python\Scripts' which is not on PATH.

Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

WARNING: The script tensorboard.exe is installed in 'C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-01-20\lib\Python\Scripts' which is not on PATH.

Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

WARNING: The scripts estimator_ckpt_converter.exe, import_pb_to_tensorboard.exe, saved_model_cli.exe, tensorboard.exe, tf_upgrade_v2.exe, tflite_convert.exe, toco.exe and toco_from_protos.exe are installed in 'C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-01-20\lib\Python\Scripts' which is not on PATH.

Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Successfully installed absl-py-0.11.0 astunparse-1.6.3 cachetools-4.2.1 flatbuffers-1.12 gast-0.3.3 google-auth-1.24.0 google-auth-oauthlib-0.4.2 google-pasta-0.2.0 grpcio-1.32.0 h5py-2.10.0 importlib-metadata-3.4.0 keras-preprocessing-1.1.2 markdown-3.3.3 oauthlib-3.1.0 opt-einsum-3.3.0 protobuf-3.14.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 requests-oauthlib-1.3.0 rsa-4.7 tensorboard-2.4.1 tensorboard-plugin-wit-1.8.0 tensorflow-2.4.1 tensorflow-estimator-2.4.0 termcolor-1.1.0 typing-extensions-3.7.4.3 werkzeug-1.0.1 zipp-3.4.0

WARNING: You are using pip version 20.3.3; however, version 21.0.1 is available.

You should consider upgrading via the 'C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-01-20\bin\python-real.exe -m pip install --upgrade pip' command.

&gt;&gt;&gt; import tensorflow

&gt;&gt;&gt;
</code></pre>

---

## Post #3 by @dSC (2021-02-02 14:07 UTC)

<p>solved by passing target folder<br>
<em>PythonSlicer.exe -m pip install tensorflow --taget=.</em></p>

---
