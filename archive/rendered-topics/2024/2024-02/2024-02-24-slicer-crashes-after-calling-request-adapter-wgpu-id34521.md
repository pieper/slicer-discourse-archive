# Slicer crashes after calling request_adapter (wgpu)

**Topic ID**: 34521
**Date**: 2024-02-24
**URL**: https://discourse.slicer.org/t/slicer-crashes-after-calling-request-adapter-wgpu/34521

---

## Post #1 by @lscoder (2024-02-24 15:16 UTC)

<p><strong>Operating system:</strong> Ubuntu 22.04.4 LTS (kernel 6.5.0-18-generic)<br>
<strong>Slicer version:</strong> 5.6.1 r32438 / 117ce5f and 5.7.0-2024-02-20 r32729 / 2762f0c</p>
<p>I am trying to run a python script (WebGPU) on Slicer but it crashes consistently and closes after calling  <em>request_adapter()</em>.</p>
<pre><code class="lang-auto">import wgpu
import wgpu.backends.auto
import wgpu.utils

# [code]

adapter = wgpu.gpu.request_adapter(canvas=None, power_preference="high-performance")
</code></pre>
<p>I tried with different parameters (<a href="https://wgpu-py.readthedocs.io/en/stable/generated/wgpu.GPU.html" rel="noopener nofollow ugc">docs</a>) with no success but the same code works if I run it on a terminal using python 3.10.12.</p>
<p>I do not see any log on Slicer but this is the error I am getting when I start slicer from the terminal (RUST_BACKTRACE set to “full”)</p>
<pre><code class="lang-auto">thread '&lt;unnamed&gt;' panicked at /root/.cargo/git/checkouts/wgpu-53e70f8674b08dd4/b8a8ff6/wgpu-hal/src/gles/egl.rs:305:14:
called `Result::unwrap()` on an `Err` value: BadAccess
stack backtrace:
   0:     0x7f58a7c794fc - std::backtrace_rs::backtrace::libunwind::trace::ha637c64ce894333a
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/../../backtrace/src/backtrace/libunwind.rs:104:5
   1:     0x7f58a7c794fc - std::backtrace_rs::backtrace::trace_unsynchronized::h47f62dea28e0c88d
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/../../backtrace/src/backtrace/mod.rs:66:5
   2:     0x7f58a7c794fc - std::sys_common::backtrace::_print_fmt::h9eef0abe20ede486
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/sys_common/backtrace.rs:67:5
   3:     0x7f58a7c794fc - &lt;std::sys_common::backtrace::_print::DisplayBacktrace as core::fmt::Display&gt;::fmt::hed7f999df88cc644
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/sys_common/backtrace.rs:44:22
   4:     0x7f58a7c9ff70 - core::fmt::rt::Argument::fmt::h1539a9308b8d058d
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/core/src/fmt/rt.rs:142:9
   5:     0x7f58a7c9ff70 - core::fmt::write::h3a39390d8560d9c9
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/core/src/fmt/mod.rs:1120:17
   6:     0x7f58a7c7761f - std::io::Write::write_fmt::h5fc9997dfe05f882
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/io/mod.rs:1762:15
   7:     0x7f58a7c792e4 - std::sys_common::backtrace::_print::h894006fb5c6f3d45
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/sys_common/backtrace.rs:47:5
   8:     0x7f58a7c792e4 - std::sys_common::backtrace::print::h23a2d212c6fff936
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/sys_common/backtrace.rs:34:9
   9:     0x7f58a7c7a607 - std::panicking::default_hook::{{closure}}::h8a1d2ee00185001a
  10:     0x7f58a7c7a36f - std::panicking::default_hook::h6038f2eba384e475
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/panicking.rs:292:9
  11:     0x7f58a7c7aa88 - std::panicking::rust_panic_with_hook::h2b5517d590cab22e
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/panicking.rs:779:13
  12:     0x7f58a7c7a96e - std::panicking::begin_panic_handler::{{closure}}::h233112c06e0ef43e
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/panicking.rs:657:13
  13:     0x7f58a7c799c6 - std::sys_common::backtrace::__rust_end_short_backtrace::h6e893f24d7ebbff8
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/sys_common/backtrace.rs:170:18
  14:     0x7f58a7c7a6d2 - rust_begin_unwind
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/std/src/panicking.rs:645:5
  15:     0x7f58a7887995 - core::panicking::panic_fmt::hbf0e066aabfa482c
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/core/src/panicking.rs:72:14
  16:     0x7f58a7887e73 - core::result::unwrap_failed::hddb4fea594200c52
                               at /rustc/82e1608dfa6e0b5569232559e3d385fea5a93112/library/core/src/result.rs:1653:5
  17:     0x7f58a7b01427 - &lt;wgpu_hal::gles::egl::Instance as wgpu_hal::Instance&lt;wgpu_hal::gles::Api&gt;&gt;::enumerate_adapters::h83045dba19c3de8f
  18:     0x7f58a79b0a1a - wgpu_core::instance::&lt;impl wgpu_core::global::Global&lt;G&gt;&gt;::request_adapter::gather::h58cc1cda55a2bbe7
  19:     0x7f58a78d0d99 - wgpu_core::instance::&lt;impl wgpu_core::global::Global&lt;G&gt;&gt;::request_adapter::hdb260c23e50e5dae
  20:     0x7f58a79493e7 - wgpuInstanceRequestAdapter
  21:     0x7f59a4027052 - ffi_call_unix64
  22:     0x7f59a40251bc - ffi_call_int
  23:     0x7f59a40230af - cdata_call
                               at /project/src/c/_cffi_backend.c:3201:5
  24:     0x7f5983897aba - _PyObject_Call
  25:     0x7f59838786a6 - _PyEval_EvalFrameDefault
  26:     0x7f59839c0b37 - _PyEval_EvalCode
  27:     0x7f5983897c41 - _PyFunction_Vectorcall
  28:     0x7f5983876597 - &lt;unknown&gt;
  29:     0x7f598387d070 - _PyEval_EvalFrameDefault
  30:     0x7f59839c0b37 - _PyEval_EvalCode
  31:     0x7f5983897c41 - _PyFunction_Vectorcall
  32:     0x7f59838b06a3 - &lt;unknown&gt;
  33:     0x7f598387c176 - _PyEval_EvalFrameDefault
  34:     0x7f59839c0b37 - _PyEval_EvalCode
  35:     0x7f5983897c41 - _PyFunction_Vectorcall
  36:     0x7f59838b06a3 - &lt;unknown&gt;
  37:     0x7f598387c176 - _PyEval_EvalFrameDefault
  38:     0x7f59839c0b37 - _PyEval_EvalCode
  39:     0x7f59839c0ed2 - _PyEval_EvalCodeWithName
  40:     0x7f59839c0f1e - PyEval_EvalCodeEx
  41:     0x7f59839c0f4b - PyEval_EvalCode
  42:     0x7f5983a172bc - PyRun_StringFlags
  43:     0x7f59ad8d1a5a - _ZN8PythonQt10evalScriptEP7_objectRK7QStringi
  44:     0x7f59ad96ec50 - _ZN17PythonQtObjectPtr10evalScriptERK7QStringi
  45:     0x7f59aec06c58 - _ZN24ctkAbstractPythonManager13executeStringERK7QStringNS_17ExecuteStringModeE
  46:     0x7f59bfa089d3 - _ZN16ctkPythonConsole13executeStringERK7QString
  47:     0x7f59bf0cd9cc - _ZN17ctkConsolePrivate9pasteTextERK7QString
  48:     0x7f59bf0cebdd - _ZN17ctkConsolePrivate18insertFromMimeDataEPK9QMimeData
  49:     0x7f59bf0ce4ec - _ZN17ctkConsolePrivate13keyPressEventEP9QKeyEvent
  50:     0x7f59bdfa20a7 - _ZN7QWidget5eventEP6QEvent
  51:     0x7f59be04a21e - _ZN6QFrame5eventEP6QEvent
  52:     0x7f59be04cef3 - _ZN19QAbstractScrollArea5eventEP6QEvent
  53:     0x7f59be118f7a - _ZN9QTextEdit5eventEP6QEvent
  54:     0x7f59bdf6343c - _ZN19QApplicationPrivate13notify_helperEP7QObjectP6QEvent
  55:     0x7f59bdf6ab55 - _ZN12QApplication6notifyEP7QObjectP6QEvent
  56:     0x7f59c0c8c126 - _ZN18qSlicerApplication6notifyEP7QObjectP6QEvent
  57:     0x7f59bce9d808 - _ZN16QCoreApplication15notifyInternal2EP7QObjectP6QEvent
  58:     0x7f59bdfbdd0b - &lt;unknown&gt;
  59:     0x7f59bdf6343c - _ZN19QApplicationPrivate13notify_helperEP7QObjectP6QEvent
  60:     0x7f59bdf69f20 - _ZN12QApplication6notifyEP7QObjectP6QEvent
  61:     0x7f59c0c8c126 - _ZN18qSlicerApplication6notifyEP7QObjectP6QEvent
  62:     0x7f59bce9d808 - _ZN16QCoreApplication15notifyInternal2EP7QObjectP6QEvent
  63:     0x7f59bd56be1b - _ZN22QGuiApplicationPrivate15processKeyEventEPN29QWindowSystemInterfacePrivate8KeyEventE
  64:     0x7f59bd570935 - _ZN22QGuiApplicationPrivate24processWindowSystemEventEPN29QWindowSystemInterfacePrivate17WindowSystemEventE
  65:     0x7f59bd54c8ab - _ZN22QWindowSystemInterface22sendWindowSystemEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE
  66:     0x7f596ac6569a - &lt;unknown&gt;
  67:     0x7f59c151bd3b - g_main_context_dispatch
  68:     0x7f59c1571258 - &lt;unknown&gt;
  69:     0x7f59c15193e3 - g_main_context_iteration
  70:     0x7f59bcef91cc - _ZN20QEventDispatcherGlib13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE
  71:     0x7f59bce9c21a - _ZN10QEventLoop4execE6QFlagsINS_17ProcessEventsFlagEE
  72:     0x7f59bcea51d3 - _ZN16QCoreApplication4execEv
  73:     0x7f59be85635a - _ZN22qSlicerCoreApplication4execEv
  74:           0x404be7 - &lt;unknown&gt;
  75:     0x7f5974029d90 - __libc_start_call_main
                               at ./csu/../sysdeps/nptl/libc_start_call_main.h:58:16
  76:     0x7f5974029e40 - __libc_start_main_impl
error: [/media/lscoder/SSD/Applications/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>Does anyone know if there is anything I can do to get it working?</p>
<p>Thanks,<br>
Leonardo Campos</p>

---

## Post #2 by @pieper (2024-02-26 00:20 UTC)

<p>Hi - I’ve been playing with wgpu in Slicer for a while and haven’t seen that.  Maybe you an try one of the experiments <a href="https://github.com/pieper/SlicerWGPU/blob/main/Experiments/slicer-render.py">like this simple render example</a>.  I’ve tested on mac, linux, and windows and have had a pretty good experience all around, but the ecosystem is still evolving so maybe some bug has crept in lately.</p>
<p>This repo has some slicer experiments for compute and render shaders:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerWGPU">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerWGPU" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/46b7e08176dd62907279eda2251fad7b2889e316d923dbc80872374585fea68d/pieper/SlicerWGPU" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerWGPU" target="_blank" rel="noopener">GitHub - pieper/SlicerWGPU: Use wgpu, a rust-python WebGPU implementation, in...</a></h3>

  <p>Use wgpu, a rust-python WebGPU implementation, in 3D Slicer - pieper/SlicerWGPU</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This repo has some changes so you can render wgpu in a PythonQt widget in Slicer.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/wgpu-py">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/wgpu-py" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/f2c5a5910d00ab23530bd6c66027f049fe9085fed72baed7285d87d4d9965b96/pieper/wgpu-py" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/wgpu-py" target="_blank" rel="noopener">GitHub - pieper/wgpu-py: Next generation GPU API for Python</a></h3>

  <p>Next generation GPU API for Python. Contribute to pieper/wgpu-py development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
