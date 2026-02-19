---
topic_id: 29859
title: "Qserialport Logic Separate Reading And Writing From Module W"
date: 2023-06-06
url: https://discourse.slicer.org/t/29859
---

# QSerialPort logic (separate reading and writing from module widget)

**Topic ID**: 29859
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/qserialport-logic-separate-reading-and-writing-from-module-widget/29859

---

## Post #1 by @Mik (2023-06-06 09:47 UTC)

<p>Dear developers,</p>
<p>I’m using QSerialPort to write and read data from two serial port devices. Everything work correct when all methods are within one object (open serial device → write data into device → read response), in my case it’s a module widget inherited from <code>qSlicerAbstractModuleWidget</code>.</p>
<p>But when i split all device methods into separated class and objects and use standard Qt connect/signals technique to communicate with these slots, the Slicer program crashes on open method of QSerialPort.</p>
<p>Are there any recommendations how to work with QSerialPort slots in Slicer?</p>
<p>Here is a header part</p>
<pre><code class="lang-auto">class Q_SLICER_QTMODULES_MLCCONTROL_EXPORT qSlicerMlcControlModuleWidget :
  public qSlicerAbstractModuleWidget
{
  Q_OBJECT
  QVTK_OBJECT

public:

  typedef qSlicerAbstractModuleWidget Superclass;
  qSlicerMlcControlModuleWidget(QWidget *parent=0);
  virtual ~qSlicerMlcControlModuleWidget();
  void enter() override;
  void exit() override;


public slots:
  /// Serial port layer-1
  void serialPortLayer1BytesWritten(qint64);
  void serialPortLayer1DataReady();
  void serialPortLayer1Error(QSerialPort::SerialPortError);

  /// Serial port layer-2
  void serialPortLayer2BytesWritten(qint64);
  void serialPortLayer2DataReady();
  void serialPortLayer2Error(QSerialPort::SerialPortError);

};

#endif

</code></pre>
<p>I want to move serial port public slots into separate objects, so the ModuleWidget object only has two serial port pointers.</p>

---

## Post #2 by @lassoan (2023-06-06 23:42 UTC)

<p>We usually use the <a href="http://plustoolkit.org/">PLUS toolkit</a> for interacting with devices, including generic serial communication. This allows the application (Slicer) to run fairly independently from the devices, fully in parallel, at a different speed, and the application can even run on a different computer.</p>
<p>One Slicer extension (<a href="https://github.com/pzaffino/SlicerArduinoController/blob/master/ArduinoConnect/ArduinoConnect.py">SlicerArduino</a>) uses pyserial to connect to Arduino devices. You might consider this as an option, too.</p>
<p>Using QSerialPort is an advanced topic and difficulties you encounter are most likely unrelated to Slicer and we use alternative methods for serial port access, therefore we cannot offer much help.</p>
<p>What device do you connect to via serial port? NDI trackers? Orientation sensors? Arduinos? Maybe someone has already implemented a real-time interface for your device in Slicer and you could use that.</p>

---

## Post #3 by @Mik (2023-06-07 12:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="29859">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What device do you connect to via serial port?</p>
</blockquote>
</aside>
<p>It’s a custom made device which controls stepper motor and it position (exchange protocol is very similar to MODBUS RTU). I think the PLUS toolkit is a overhead in my case, but i try it anyway. Last time i was unable to compile it on Linux.<br>
The SlicerArduino is written on python, and i don’t want to mix python and C++ code, since most part is written on C++.</p>

---

## Post #4 by @lassoan (2023-06-07 12:44 UTC)

<p>Serial port can be quite problematic. Of there is no more RS232 connector on computers today and USB to serial converters are unreliable and there are lots of driver issues, even on Windows, so on Linux the problem is probably even worse. Even if you manage to find an USB to serial converter that works reliably on your system, you may not be able to buy it again later, or your users may not be able to get one that works for them.</p>
<p>You could consider adding a Raspberry Pi or other mini computer to your device that takes care of low level control, calibration/zeroing, emergency stop, etc. functions and communicate with Slicer via ethernet or wifi.</p>
<p>Calling Python code from C++ is easy, but I agree that if you want to optimize performance using multi-threading or need to do complex debugging then crossing a language boundary is somewhat inconvenient.</p>
<p>We don’t bundle it with PythonQt. How did you integrate QSerialPort? Have you added the QSerialPort source files into your module source code?</p>

---

## Post #5 by @Mik (2023-06-07 13:37 UTC)

<p>Agreed, it may be easier to split program as client-server.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="29859">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We don’t bundle it with PythonQt. How did you integrate QSerialPort? Have you added the QSerialPort source files into your module source code?</p>
</blockquote>
</aside>
<p>Since the QtSerialPort module is a part of Qt5 (built-in into Qt5), i have just added SerialPort module to <code>Slicer_REQUIRED_QT_MODULES</code> parameter into Slicer’s <code>CMakeLists.txt</code>  and recompiled everything.</p>
<pre><code class="lang-auto">#-----------------------------------------------------------------------------
# Qt - Slicer_REQUIRED_QT_MODULES
#-----------------------------------------------------------------------------
# Module name should be specified as they appear in FindQt5.cmake.
# For example, the module name associated with the variable QT_USE_QTXML is QTXML.
# Note that the modules will be installed when packaging.
  set(Slicer_REQUIRED_QT_MODULES
    Core Widgets
    Network OpenGL
    PrintSupport
    UiTools #no dll
    Xml XmlPatterns
    Svg Sql
    SerialPort
    )
</code></pre>
<p>After that i’ve just added <code>#include &lt;QtSerialPort/QSerialPort&gt;</code> into module widget header. Everything else is just straight-forward programming and it described in Qt documentation.</p>

---

## Post #6 by @Mik (2023-08-11 09:51 UTC)

<p>I was able to find a bug in my definition and implementation of logic class. Now everything is working separately: two logic objects (each one for a serial port device), one widget object shows the processed data from these two serial devices.</p>

---
