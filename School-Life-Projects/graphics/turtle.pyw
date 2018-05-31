�
ևLQc        O   @   s  d  Z  d Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m	 Z	 m
 Z
 m Z d d l m Z d d l Td d d	 d
 d d d d d g	 Z d d d d d d d d d d d d d d d d d  d! d" d# d$ d% d& d' d( d) g Z d* d+ d, d- d. d/ d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 d: d; d< d= d> d? d@ dA dB dC dD dE dF dG dH dI dJ dK dL dM dN dO dP dQ dR dS dT dU dV dW dX dY dZ d[ d\ d] d^ d_ d` da db dc dd de df dg dh di dj dk dl dm d% dn do dp dq dr d( d) ds dt du gO Z dv dw dx g Z dy dz d{ d| d} d~ d d� d� d� d� d� d� d� d� d� d� d� d� d� d� d� d� d� d� g Z e e e e e Z d d+ d. d; dG dK dO dU dW d\ d] d_ d` di dn dq dr g Z i d� dr 6d� d� 6d� d� 6d� d� 6e d� 6e d� 6d� d 6d� d 6d� d 6d� d� 6d� de 6d� dQ 6d� d= 6d� d[ 6e d� 6d� d� 6d� d� 6d� d� 6d� d$ 6e d� 6Z d� �  Z d� �  Z y e e � Wn d� GHn Xd e f d� �  �  YZ d� �  Z d� �  Z d� d� Z f  d� � Z  d e j! f d� �  �  YZ" e  e" e j# d� � d� e j$ f d� �  �  YZ% e j# Z# d� e& f d� �  �  YZ' d� e( f d� �  �  YZ) d� e( f d� �  �  YZ* d e& f d� �  �  YZ+ d� e& f d� �  �  YZ, d e' f d� �  �  YZ- d� e& f d� �  �  YZ. d� e& f d� �  �  YZ/ d� e& f d� �  �  YZ0 d
 e/ e. f d� �  �  YZ1 e1 Z2 d� �  Z3 d� e- f d� �  �  YZ4 d e1 f d� �  �  YZ5 e5 Z6 d� �  Z7 d� �  Z8 d� d� � Z9 d� �  Z: e d� Z; y e; d� k rOe: e; � n  Wn) e< k
 rld� Ge; GHn d� e; GHn Xd� �  Z= d� �  Z> d� �  Z? x� e D]� Z@ e= eA d� e@ � � \ ZB ZC eB d� k r�d� GeB GeC GHq�n  d� i e@ d� 6eB d� 6eC d� 6ZD eD d Ue? eA d� e@ � j  � eA e@ � _  q�Wx� e D]� Z@ e= eA d� e@ � � \ ZB ZC eB d� k rtd� GeB GeC GHq3n  d� i e@ d� 6eB d� 6eC d� 6ZD eD d Ue> eA d� e@ � j  � eA e@ � _  q3We jE ZF ZE [B [C [D eG d� k rd� �  ZH d� �  ZI d� �  ZJ eI �  eJ �  eK �  n  d S(�   s�  
Turtle graphics is a popular way for introducing programming to
kids. It was part of the original Logo programming language developed
by Wally Feurzig and Seymour Papert in 1966.

Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an ``import turtle``, give it
the command turtle.forward(15), and it moves (on-screen!) 15 pixels in
the direction it is facing, drawing a line as it moves. Give it the
command turtle.right(25), and it rotates in-place 25 degrees clockwise.

By combining together these and similar commands, intricate shapes and
pictures can easily be drawn.

----- turtle.py

This module is an extended reimplementation of turtle.py from the
Python standard distribution up to Python 2.5. (See: http://www.python.org)

It tries to keep the merits of turtle.py and to be (nearly) 100%
compatible with it. This means in the first place to enable the
learning programmer to use all the commands, classes and methods
interactively when using the module from within IDLE run with
the -n switch.

Roughly it has the following features added:

- Better animation of the turtle movements, especially of turning the
  turtle. So the turtles can more easily be used as a visual feedback
  instrument by the (beginning) programmer.

- Different turtle shapes, gif-images as turtle shapes, user defined
  and user controllable turtle shapes, among them compound
  (multicolored) shapes. Turtle shapes can be stretched and tilted, which
  makes turtles very versatile geometrical objects.

- Fine control over turtle movement and screen updates via delay(),
  and enhanced tracer() and speed() methods.

- Aliases for the most commonly used commands, like fd for forward etc.,
  following the early Logo traditions. This reduces the boring work of
  typing long sequences of commands, which often occur in a natural way
  when kids try to program fancy pictures on their first encounter with
  turtle graphics.

- Turtles now have an undo()-method with configurable undo-buffer.

- Some simple commands/methods for creating event driven programs
  (mouse-, key-, timer-events). Especially useful for programming games.

- A scrollable Canvas class. The default scrollable Canvas can be
  extended interactively as needed while playing around with the turtle(s).

- A TurtleScreen class with methods controlling background color or
  background image, window and canvas size and other properties of the
  TurtleScreen.

- There is a method, setworldcoordinates(), to install a user defined
  coordinate-system for the TurtleScreen.

- The implementation uses a 2-vector class named Vec2D, derived from tuple.
  This class is public, so it can be imported by the application programmer,
  which makes certain types of computations very natural and compact.

- Appearance of the TurtleScreen and the Turtles at startup/import can be
  configured by means of a turtle.cfg configuration file.
  The default configuration mimics the appearance of the old turtle module.

- If configured appropriately the module reads in docstrings from a docstring
  dictionary in some different language, supplied separately  and replaces
  the English ones by those read in. There is a utility function
  write_docstringdict() to write a dictionary with the original (English)
  docstrings to disc, so it can serve as a template for translations.

Behind the scenes there are some features included with possible
extensions in mind. These will be commented and documented elsewhere.

s5   turtle 1.0b1 - for Python 2.6   -  30. 5. 2008, 18:08i����N(   t   isfilet   splitt   join(   t   deepcopy(   t   *t   ScrolledCanvast   TurtleScreent   Screent	   RawTurtlet   Turtlet   RawPent   Pent   Shapet   Vec2Dt   addshapet   bgcolort   bgpict   byet   clearscreent	   colormodet   delayt   exitonclickt	   getcanvast	   getshapest   listent   modet   onkeyt   onscreenclickt   ontimert   register_shapet   resetscreent
   screensizet   setupt   setworldcoordinatest   titlet   tracert   turtlest   updatet   window_heightt   window_widtht   backt   backwardt
   begin_fillt
   begin_polyt   bkt   circlet   cleart
   clearstampt   clearstampst   clonet   colort   degreest   distancet   dott   downt   end_fillt   end_polyt   fdt   fillt	   fillcolort   forwardt   get_polyt   getpent	   getscreent	   getturtlet   gotot   headingt
   hideturtlet   homet   htt   isdownt	   isvisiblet   leftt   ltt   onclickt   ondragt	   onreleaset   pdt   pent   pencolort   pendownt   pensizet   penupt   post   positiont   put   radianst   rightt   resett
   resizemodet   rtt   setht
   setheadingt   setpost   setpositiont   settiltanglet   setundobuffert   setxt   setyt   shapet	   shapesizet
   showturtlet   speedt   stt   stampt   tiltt	   tiltanglet   towardst
   turtlesizet   undot   undobufferentriest   upt   widtht   writet   xcort   ycort   write_docstringdictt   donet   mainloopt   acost   asint   atant   atan2t   ceilt   cost   cosht   et   expt   fabst   floort   fmodt   frexpt   hypott   ldexpt   logt   log10t   modft   pit   powt   sint   sinht   sqrtt   tant   tanhg      �?g      �?t   heighti�  t	   canvwidthi,  t
   canvheightt	   leftrightt	   topbottomt   standardg      �?i
   i�  t   undobuffersizet   classict   blackt   noresizet   visiblet   englisht   languaget   turtlet   exampleturtlet   screent   examplescreens   Python Turtle Graphicst
   using_IDLEc         C   s  t  |  d � } | j �  } | j �  i  } x� | D]� } | j �  } | s2 | j d � r` q2 n  y | j d � \ } } Wn d |  | f GHq2 n X| j �  } | j �  } | d k r� t | � } n5 y+ d
 | k r� t | � } n t | � } Wn n X| | | <q2 W| S(   s/   Convert content of config-file into dictionary.t   rt   #t   =s   Bad line in config-file %s:
%st   Truet   Falset   Nones   ''s   ""t   .(   s   Trues   Falses   Nones   ''s   ""(	   t   opent	   readlinest   closet   stript
   startswithR   t   evalt   floatt   int(   t   filenamet   ft   cfglinest   cfgdictt   linet   keyt   value(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   config_dict�   s2    
c         C   s�   d } i  } i  } t  | � r- t | � } n  d | k rJ d | d } n  y% t t � \ } } t | | � } Wn d } n Xt  | � r� t | � } n  t j | � t j | � d S(   s@  Read config-files, change configuration-dict accordingly.

    If there is a turtle.cfg file in the current working directory,
    read it from there. If this contains an importconfig-value,
    say 'myway', construct filename turtle_mayway.cfg else use
    turtle.cfg and read it from the import-directory, where
    turtle.py is located.
    Update configuration dictionary first according to config-file,
    in the import directory, then according to config-file in the
    current working directory.
    If no config-file is found, the default configuration is used.
    s
   turtle.cfgt   importconfigs   turtle_%s.cfgt    N(   R    R�   R   t   __file__R   t   _CFGR%   (   R�   t   default_cfgt   cfgdict1t   cfgdict2t   headt   tailt	   cfg_file2(    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   readconfig�   s     
s"   No configfile read, reason unknownc           B   sh   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z d
 �  Z RS(   s�  A 2 dimensional vector class, used as a helper class
    for implementing turtle graphics.
    May be useful for turtle graphics programs also.
    Derived from tuple, so a vector is a tuple!

    Provides (for a, b vectors, k number):
       a+b vector addition
       a-b vector subtraction
       a*b inner product
       k*a and a*k multiplication with scalar
       |a| absolute value of a
       a.rotate(angle) rotation
    c         C   s   t  j |  | | f � S(   N(   t   tuplet   __new__(   t   clst   xt   y(    (    s    C:\Python27\lib\lib-tk\turtle.pyR�     s    c         C   s%   t  |  d | d |  d | d � S(   Ni    i   (   R   (   t   selft   other(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __add__  s    c         C   sL   t  | t � r/ |  d | d |  d | d St |  d | |  d | � S(   Ni    i   (   t
   isinstanceR   (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __mul__  s     c         C   s?   t  | t � s t  | t � r; t |  d | |  d | � Sd  S(   Ni    i   (   R�   R�   R�   R   (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __rmul__  s    c         C   s%   t  |  d | d |  d | d � S(   Ni    i   (   R   (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __sub__  s    c         C   s   t  |  d |  d � S(   Ni    i   (   R   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __neg__  s    c         C   s   |  d d |  d d d S(   Ni    i   i   g      �?(    (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __abs__  s    c         C   s}   t  |  d |  d � } | t j d } t j | � t j | � } } t  |  d | | d | |  d | | d | � S(   s.   rotate self counterclockwise by angle
        i   i    g     �f@(   R   t   mathR�   R|   R�   (   R�   t   anglet   perpt   ct   s(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   rotate  s    c         C   s   |  d |  d f S(   Ni    i   (    (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __getnewargs__&  s    c         C   s   d |  S(   Ns   (%.2f,%.2f)(    (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __repr__(  s    (   t   __name__t
   __module__t   __doc__R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR      s   									c         C   s}   t  |  j � } | j �  x | D] } t | | � q  Wx? |  j j �  D]. \ } } t | � t j k rG | | | <qG qG Wd S(   s#   helper function for Scrolled CanvasN(	   t   listt	   __bases__t   reverset   __methodDictt   __dict__t   itemst   typet   typest   FunctionType(   R�   t   _dictt   baseListt   _superR�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�   4  s    
c         C   s   i  } t  |  | � | j �  S(   s#   helper function for Scrolled Canvas(   R�   t   keys(   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   __methods>  s    s*   def %(method)s(self, *args, **kw): return s*   self.%(attribute)s.%(method)s(*args, **kw)c   
      B   s&  i  } e  | | � x> | j �  D]0 } | d  d k sF | d d k r  | | =q  q  Wx$ | D] } | | k r[ | | =q[ q[ Wx* e |  � D] } | | k r� | | =q� q� Wxw | j �  D]i \ } } i | d 6| d 6} e | � e j k re i | d 6| d 6}	 n  |	 | U| | |  j | <q� Wd S(   sn   Helper functions for Scrolled Canvas, used to forward
    ScrolledCanvas-methods to Tkinter.Canvas class.
    i   t   _i����t   methodt   funct	   attributeN(	   R�   R�   R�   R�   R�   R�   t
   StringTypet   __stringBodyR�   (
   t	   fromClasst   toClasst   toPartt   excludeR�   t   exR�   R�   t   dt
   execString(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   __forwardmethodsH  s"     c           B   s}   e  Z d  Z d d d d d � Z d d d d � Z d �  Z d �  Z d �  Z d	 �  Z	 d
 �  Z
 d �  Z d �  Z d �  Z RS(   s�   Modeled after the scrolled canvas class from Grayons's Tkinter book.

    Used as the default canvas, which pops up automatically when
    using turtle graphics functions or the Turtle class.
    i�  i^  iX  c         C   s
  t  j j |  | d | d | �|  j �  |  _ | | |  _ |  _ | | |  _ |  _ d |  _	 t  j
 | d | d | d |  j	 d t  j d d �|  _ t  j | d |  j j d	 t  j �|  _ t  j | d |  j j �|  _ |  j j d
 |  j j d |  j j � |  j d d d d d �|  j d d d d d �|  j j d d d |  d d d d d d d d d d d d � |  j j d d d |  d d d d d d d d d d d d � |  j j d d d |  d d d d d d d d d d d d � |  j �  |  j j d |  j � d  S(   NRp   R�   t   whitet   bgt   relieft   borderwidthi   t   commandt   orientt   xscrollcommandt   yscrollcommandi    t   weighti   t   minsizet   padxt   in_t   padyt   rowt   columnt   rowspant
   columnspant   stickyt   newss   <Configure>(   t   TKt   Framet   __init__t   winfo_toplevelt   _rootwindowRp   R�   R�   R�   R�   t   Canvast   SUNKENt   _canvast	   Scrollbart   xviewt
   HORIZONTALt   hscrollt   yviewt   vscrollt	   configuret   sett   rowconfiguret   columnconfiguret   gridRX   t   bindt   onResize(   R�   t   masterRp   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  g  s,    	$$$
c      	   C   s�   | r | |  _  n  | r$ | |  _ n  | r6 | |  _ n  |  j j d | d |  j  d |  j d |  j  d |  j d f � |  j j d |  j  |  j d |  j  � |  j j d |  j |  j d |  j � |  j	 �  d S(   s<   Adjust canvas and scrollbars according to given canvas size.R�   t   scrollregioni   g      �?i   N(
   R�   R�   R�   R  t   configt   xview_movetoRp   t   yview_movetoR�   t   adjustScrolls(   R�   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRX   �  s    c         C   s  |  j  j �  } |  j  j �  } |  j  j d |  j | |  j � |  j  j d |  j | |  j � | |  j k  s� | |  j k  r� |  j j d d d |  d d d d d d d	 d d
 d d d � |  j	 j d d d |  d d d d d d d	 d d
 d d d � n |  j j
 �  |  j	 j
 �  d S(   sA    Adjust scrollbars according to window- and canvas-size.
        g      �?R  i   R  R  R  R  i    R  R	  R
  R  N(   R  t   winfo_widtht   winfo_heightR$  R�   R%  R�   R  R  R  t   grid_forget(   R�   t   cwidtht   cheight(    (    s    C:\Python27\lib\lib-tk\turtle.pyR&  �  s    ""$$c         C   s   |  j  �  d S(   s   self-explanatoryN(   R&  (   R�   t   event(    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s    c         G   s   |  j  j | �  S(   s@    'forward' method, which canvas itself has inherited...
        (   R  t   bbox(   R�   t   args(    (    s    C:\Python27\lib\lib-tk\turtle.pyR-  �  s    c         O   s   |  j  j | | �  S(   s@    'forward' method, which canvas itself has inherited...
        (   R  t   cget(   R�   R.  t   kwargs(    (    s    C:\Python27\lib\lib-tk\turtle.pyR/  �  s    c         O   s   |  j  j | | �  d S(   s@    'forward' method, which canvas itself has inherited...
        N(   R  R#  (   R�   R.  R0  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR#  �  s    c         O   s   |  j  j | | �  d S(   s@    'forward' method, which canvas itself has inherited...
        N(   R  R  (   R�   R.  R0  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    c         O   s   |  j  j | | �  d S(   s@    'forward' method, which canvas itself has inherited...
        N(   R  t   unbind(   R�   R.  R0  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR1  �  s    c         C   s   |  j  j �  d S(   s@    'forward' method, which canvas itself has inherited...
        N(   R  t   focus_force(   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR2  �  s    N(   R�   R�   R�   R  R�   RX   R&  R   R-  R/  R#  R  R1  R2  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   a  s   							R  t   _Rootc           B   sM   e  Z d  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 RS(   s'   Root class for Screen based on Tkinter.c         C   s   t  j j |  � d  S(   N(   R  t   TkR  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    c         C   s8   t  |  | | | | � |  _ |  j j d d d d � d  S(   Nt   expandi   R:   t   both(   R   R  t   pack(   R�   Rp   R�   R*  R+  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   setupcanvas�  s    c         C   s   |  j  S(   N(   R  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   _getcanvas�  s    c         C   s!   |  j  d | | | | f � d  S(   Ns   %dx%d%+d%+d(   t   geometry(   R�   Rp   R�   t   startxt   starty(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   set_geometry�  s    c         C   s   |  j  d | � d  S(   Nt   WM_DELETE_WINDOW(   t   wm_protocol(   R�   t   destroy(    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   ondestroy�  s    c         C   s
   |  j  �  S(   N(   t   winfo_screenwidth(   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   win_width�  s    c         C   s
   |  j  �  S(   N(   t   winfo_screenheight(   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   win_height�  s    (
   R�   R�   R�   R  R8  R9  R=  RA  RC  RE  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR3  �  s   						t   TurtleScreenBasec           B   s[  e  Z d  Z e d �  � Z e d �  � Z d �  Z d �  Z d d d e	 d � Z
 d �  Z d d d e	 d � Z d �  Z d	 �  Z d
 �  Z d �  Z d d � Z d �  Z d d d � Z d d d � Z d d d � Z d d d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z  d d d d � Z! d �  Z" RS(    s�   Provide the basic graphics functionality.
       Interface between Tkinter and turtle.py.

       To port turtle.py to some different graphics toolkit
       a corresponding TurtleScreenBase class has to be implemented.
    c          C   s&   t  j d d d d � }  |  j �  |  S(   s$   return a blank image object
        Rp   i   R�   (   R  t
   PhotoImaget   blank(   t   img(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _blankimage�  s    
c         C   s   t  j d |  � S(   s`   return an image object containing the
        imagedata from a gif-file named filename.
        t   file(   R  RG  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _image�  s    c         C   s�   | |  _  t | t � r3 |  j  j } |  j  j } na t |  j  j d � � } t |  j  j d � � } |  j  j d | d | d | d | d f � | |  _ | |  _ d |  _ |  _	 d  S(   NRp   R�   R"  i   g      �?(
   t   cvR�   R   R�   R�   R�   R/  R#  t   xscalet   yscale(   R�   RM  t   wt   h(    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    	1		c         C   s   |  j  j d d d d d �S(   s<   Create an invisible polygon item on canvas self.cv)
        i    R:   R�   t   outline(   i    i    i    i    i    i    (   RM  t   create_polygon(   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _createpoly  s    c   
      C   s�   g  } x= | D]5 \ } }	 | j  | |  j � | j  |	 |  j � q W|  j j | | � | d k	 r~ |  j j | d | �n  | d k	 r� |  j j | d | �n  | d k	 r� |  j j | d | �n  | r� |  j j | � n  d S(   s`  Configure polygonitem polyitem according to provided
        arguments:
        coordlist is sequence of coordinates
        fill is filling color
        outline is outline color
        top is a boolean value, which specifies if polyitem
        will be put on top of the canvas' displaylist so it
        will not be covered by other items.
        R:   RR  Rp   N(   t   appendRN  RO  RM  t   coordsR�   t   itemconfiguret	   tag_raise(
   R�   t   polyitemt	   coordlistR:   RR  Rp   t   topt   clR�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   _drawpoly  s    c         C   s.   |  j  j d d d d d d d d d t j �S(   s9   Create an invisible line item on canvas self.cv)
        i    R:   R�   Rp   i   t   capstyle(   RM  t   create_lineR  t   ROUND(   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _createline$  s    $c   	      C   s�   | d k	 rh g  } x= | D]5 \ } } | j | |  j � | j | |  j � q W|  j j | | � n  | d k	 r� |  j j | d | �n  | d k	 r� |  j j | d | �n  | r� |  j j | � n  d S(   sQ  Configure lineitem according to provided arguments:
        coordlist is sequence of coordinates
        fill is drawing color
        width is width of drawn line.
        top is a boolean value, which specifies if polyitem
        will be put on top of the canvas' displaylist so it
        will not be covered by other items.
        R:   Rp   N(   R�   RU  RN  RO  RM  RV  RW  RX  (	   R�   t   lineitemRZ  R:   Rp   R[  R\  R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   _drawline*  s    
c         C   s   |  j  j | � d S(   s]   Delete graphics item from canvas.
        If item is"all" delete all graphics items.
        N(   RM  t   delete(   R�   t   item(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _deleteA  s    c         C   s   |  j  j �  d S(   s(   Redraw graphics items on canvas
        N(   RM  R%   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _updateG  s    c         C   s   |  j  j | � d S(   s-   Delay subsequent canvas actions for delay ms.N(   RM  t   after(   R�   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _delayL  s    c         C   s=   y |  j  j | � } t } Wn t j k
 r8 t } n X| S(   sC   Check if the string color is a legal Tkinter color string.
        (   RM  t	   winfo_rgbR�   R  t   TclErrorR�   (   R�   R2   t   rgbt   ok(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _iscolorstringP  s    

c         C   s@   | d k	 r, |  j j d | � |  j �  n |  j j d � Sd S(   sV   Set canvas' backgroundcolor if color is not None,
        else return backgroundcolor.R�   N(   R�   RM  R#  Rg  R/  (   R�   R2   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _bgcolorZ  s    c         C   s�   | \ } } | |  j  } | |  j } i d d 6d d 6d d 6} |  j j | d | d | d	 | | d
 | d | �}	 |  j j |	 � \ }
 } } } |  j j �  |	 | d f S(   s�   Write txt at pos in canvas with specified font
        and color.
        Return text item and x-coord of right bottom corner
        of text's bounding box.t   swRH   R�   t   centert   seRW   i   t   textt   anchorR:   t   font(   RN  RO  RM  t   create_textR-  R%   (   R�   RS   t   txtt   alignRu  RO   R�   R�   Rt  Re  t   x0t   y0t   x1t   y1(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _writec  s    'i   c            sY   �  d k r& � j j | d | � n/ �  � f d �  } � j j | d | | | � d S(   s�   Bind fun to mouse-click event on turtle.
        fun must be a function with two arguments, the coordinates
        of the clicked point on the canvas.
        num, the number of the mouse-button defaults to 1
        s   <Button-%s>c            sK   � j  j |  j � � j � j  j |  j � � j } } �  | | � d  S(   N(   RM  t   canvasxR�   RN  t   canvasyR�   RO  (   R,  R�   R�   (   t   funR�   (    s    C:\Python27\lib\lib-tk\turtle.pyt   eventfun~  s    !N(   R�   RM  t
   tag_unbindt   tag_bind(   R�   Re  R�  t   numt   addR�  (    (   R�  R�   s    C:\Python27\lib\lib-tk\turtle.pyt   _onclicku  s    c            sY   �  d k r& � j j | d | � n/ �  � f d �  } � j j | d | | | � d S(   sg  Bind fun to mouse-button-release event on turtle.
        fun must be a function with two arguments, the coordinates
        of the point on the canvas where mouse button is released.
        num, the number of the mouse-button defaults to 1

        If a turtle is clicked, first _onclick-event will be performed,
        then _onscreensclick-event.
        s   <Button%s-ButtonRelease>c            sK   � j  j |  j � � j � j  j |  j � � j } } �  | | � d  S(   N(   RM  R~  R�   RN  R  R�   RO  (   R,  R�   R�   (   R�  R�   (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  s    !N(   R�   RM  R�  R�  (   R�   Re  R�  R�  R�  R�  (    (   R�  R�   s    C:\Python27\lib\lib-tk\turtle.pyt
   _onrelease�  s
    	c            sY   �  d k r& � j j | d | � n/ �  � f d �  } � j j | d | | | � d S(   sq  Bind fun to mouse-move-event (with pressed mouse button) on turtle.
        fun must be a function with two arguments, the coordinates of the
        actual mouse position on the canvas.
        num, the number of the mouse-button defaults to 1

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.
        s   <Button%s-Motion>c            sY   yK � j  j |  j � � j � j  j |  j � � j } } �  | | � Wn n Xd  S(   N(   RM  R~  R�   RN  R  R�   RO  (   R,  R�   R�   (   R�  R�   (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  s    !N(   R�   RM  R�  R�  (   R�   Re  R�  R�  R�  R�  (    (   R�  R�   s    C:\Python27\lib\lib-tk\turtle.pyt   _ondrag�  s    	c            sS   �  d k r# � j j d | � n, �  � f d �  } � j j d | | | � d S(   sG  Bind fun to mouse-click event on canvas.
        fun must be a function with two arguments, the coordinates
        of the clicked point on the canvas.
        num, the number of the mouse-button defaults to 1

        If a turtle is clicked, first _onclick-event will be performed,
        then _onscreensclick-event.
        s   <Button-%s>c            sK   � j  j |  j � � j � j  j |  j � � j } } �  | | � d  S(   N(   RM  R~  R�   RN  R  R�   RO  (   R,  R�   R�   (   R�  R�   (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  s    !N(   R�   RM  R1  R  (   R�   R�  R�  R�  R�  (    (   R�  R�   s    C:\Python27\lib\lib-tk\turtle.pyt   _onscreenclick�  s    	c            sP   �  d k r& |  j j d | d � n& �  f d �  } |  j j d | | � d S(   s`   Bind fun to key-release event of key.
        Canvas must have focus. See method listen
        s   <KeyRelease-%s>c            s   �  �  d  S(   N(    (   R,  (   R�  (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  s    N(   R�   RM  R1  R  (   R�   R�  R�   R�  (    (   R�  s    C:\Python27\lib\lib-tk\turtle.pyt   _onkey�  s    c         C   s   |  j  j �  d S(   s=   Set focus on canvas (in order to collect key-events)
        N(   RM  R2  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _listen�  s    c         C   s6   | d k r |  j  j | � n |  j  j | | � d S(   s?   Install a timer, which calls fun after t milliseconds.
        i    N(   RM  t
   after_idleRh  (   R�   R�  t   t(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _ontimer�  s    c         C   s   |  j  j d d d | �S(   s0   Create and return image item on canvas.
        i    t   image(   RM  t   create_image(   R�   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _createimage�  s    c         C   sN   | \ } } |  j  j | | |  j | |  j f � |  j  j | d | �d S(   sZ   Configure image item as to draw image object
        at position (x,y) on canvas)
        R�  N(   RM  RV  RN  RO  t
   itemconfig(   R�   Re  t   .2R�  R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   _drawimage�  s    	(c         C   s*   |  j  j | d | �|  j  j | � d S(   s�   Configure image item as to draw image object
        at center of canvas. Set item to the first item
        in the displaylist, so it will be drawn below
        any other item .R�  N(   RM  R�  t	   tag_lower(   R�   Re  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   _setbgpic�  s    c         C   s   |  j  j | � S(   sQ   Return 'line' or 'polygon' or 'image' depending on
        type of item.
        (   RM  R�   (   R�   Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _type�  s    c         C   sT   |  j  j | � } g  t d t | � d � D] } | | | | d f ^ q+ } | S(   s   returns list of coordinate-pairs of points of item
        Example (for insiders):
        >>> from turtle import *
        >>> getscreen()._pointlist(getturtle().turtle._item)
        [(0.0, 9.9999999999999982), (0.0, -9.9999999999999982),
        (9.9999999999999982, 0.0)]
        >>> i    i   i   (   RM  RV  t   ranget   len(   R�   Re  R\  t   it   pl(    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   _pointlist�  s    >c         C   s#   |  j  j d | | | | f � d  S(   NR"  (   RM  R#  (   R�   t   srx1t   sry1t   srx2t   sry2(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _setscrollregion�  s    c   	      C   s�   |  j  j �  } x� | D]z } |  j  j | � } g  } xF | r| | d  \ } } | j | | � | j | | � | d } q7 W|  j  j | | � q Wd  S(   Ni   (   RM  t   find_allRV  RU  (	   R�   t   xscalefactort   yscalefactorR�   Re  t   coordinatest   newcoordlistR�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _rescale�  s    	c         C   s�   t  |  j t � s" |  j |  j f S| | k oD | k oD d k n r_ |  j j |  j j f S| d k	 rw | |  _ n  | d k	 r� | |  _ n  |  j j | | | � d S(   sa   Resize the canvas the turtles are drawing on. Does
        not alter the drawing window.
        N(   R�   RM  R   R�   R�   R�   RX   (   R�   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _resize  s    'c         C   s`   |  j  j �  } | d k r+ |  j  d } n  |  j  j �  } | d k rV |  j  d } n  | | f S(   s;    Return the width and height of the turtle window.
        i   Rp   R�   (   RM  R'  R(  (   R�   Rp   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _window_size  s    N(#   R�   R�   R�   t   staticmethodRJ  RL  R  RT  R�   R�   R]  Ra  Rc  Rf  Rg  Ri  Rn  Ro  R}  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  R�  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyRF  �  s@   							
												t
   Terminatorc           B   s   e  Z d  Z RS(   s�   Will be raised in TurtleScreen.update, if _RUNNING becomes False.

    This stops execution of a turtle graphics script.
    Main purpose: use in the Demo-Viewer turtle.Demo.py.
    (   R�   R�   R�   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  +  s   t   TurtleGraphicsErrorc           B   s   e  Z d  Z RS(   s   Some TurtleGraphics Error
    (   R�   R�   R�   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  4  s   c           B   s&   e  Z d  Z d d � Z d d � Z RS(   s�   Data structure modeling shapes.

    attribute _type is one of "polygon", "image", "compound"
    attribute _data is - depending on _type a poygon-tuple,
    an image or a list constructed using the addcomponent method.
    c         C   s�   | |  _  | d k r6 t | t � r� t | � } q� ny | d k r� t | t � r� | j �  j d � r� t | � r� t j	 | � } q� q� n% | d k r� g  } n t
 d | � � | |  _ d  S(   Nt   polygonR�  s   .gift   compounds   There is no shape type %s(   R�  R�   R�   R�   t   strt   lowert   endswithR    R   RL  R�  t   _data(   R�   t   type_t   data(    (    s    C:\Python27\lib\lib-tk\turtle.pyR  @  s    	!	c         C   sW   |  j  d k r% t d |  j  � � n  | d k r: | } n  |  j j | | | g � d S(   s-  Add component to a shape of type compound.

        Arguments: poly is a polygon, i. e. a tuple of number pairs.
        fill is the fillcolor of the component,
        outline is the outline color of the component.

        call (for a Shapeobject namend s):
        --   s.addcomponent(((0,0), (10,10), (-10,10)), "red", "blue")

        Example:
        >>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
        >>> s = Shape("compound")
        >>> s.addcomponent(poly, "red", "blue")
        >>> # .. add more components and then use register_shape()
        R�  s    Cannot add component to %s ShapeN(   R�  R�  R�   R�  RU  (   R�   t   polyR:   RR  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   addcomponentP  s    	N(   R�   R�   R�   R�   R  R�  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   9  s   t   Tbufferc           B   sJ   e  Z d  Z d d � Z d d � Z d �  Z d �  Z d �  Z d �  Z	 RS(	   s5   Ring buffer used as undobuffer for RawTurtle objects.i
   c         C   s2   | |  _  d  g g | |  _ d |  _ t |  _ d  S(   Ni����(   t   bufsizeR�   t   buffert   ptrR�   t   cumulate(   R�   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  j  s    		c         C   sb   | d  k r9 xF t |  j � D] } d  g |  j | <q Wn | |  _ d  g g | |  _ d |  _ d  S(   Ni����(   R�   R�  R�  R�  R�  (   R�   R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRX   o  s    	c         C   s`   |  j  d k r\ |  j sB |  j d |  j  |  _ | |  j |  j <q\ |  j |  j j | � n  d  S(   Ni    i   (   R�  R�  R�  R�  RU  (   R�   Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   pushw  s
    	c         C   sd   |  j  d k r` |  j |  j } | d  k r/ d  Sd  g |  j |  j <|  j d |  j  |  _ | Sn  d  S(   Ni    i   (   R�  R�  R�  R�   (   R�   Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   pop~  s    c         C   s   |  j  |  j j d  g � S(   N(   R�  R�  t   countR�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   nr_of_items�  s    c         C   s   t  |  j � d t  |  j � S(   Nt    (   R�  R�  R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�   �  s    N(
   R�   R�   R�   R  R�   RX   R�  R�  R�  R�   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  h  s   				c           B   sO  e  Z d  Z e Z e d e d e d d � Z d �  Z d d � Z	 d �  Z
 d d � Z d	 �  Z d
 �  Z d d � Z d �  Z d �  Z d �  Z d d d � Z d d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d d d � Z d �  Z d d d � Z d d � Z d d � Z d d d d � Z e Z  e Z! e Z" e Z# RS(    s�   Provides screen oriented methods like setbg etc.

    Only relies upon the methods of TurtleScreenBase and NOT
    upon components of the underlying graphics toolkit -
    which is Tkinter in this case.
    R   R   R   c         C   s�  i t  d d/ d0 d1 f � d 6t  d d2 d3 d4 d5 d6 d7 d8 d9 d: d; d< d= d> d? d@ dA dB dC dD dE dF dG dH dI f � d 6t  d dJ dK dL dM dN dO dP dQ dR dS dT dU dV dW dX dY dZ d[ d\ d] f � d$ 6t  d d^ d_ d` da f � d% 6t  d db dc dd f � d( 6t  d de df dg dh f � d) 6t  d* |  j �  � d+ 6|  _ i d, d- 6|  _ t j |  | � | |  _ | |  _ t d. |  _	 g  |  _
 |  j �  d  S(i   NR�  i����i    i
   t   arrowi   i����i   i����i����i   i����i	   i����i   i����i   i   i����i����i����i   i   i   R�   g��Q�#@g���Q�@g�G�z. @g��Q��@g���Q��g��Q���g�G�z. �g��Q�#�g       �g      $�R-   t   squareg�G�z�g�����'@t   triangleR�   R�  RH  R�   t   nopicR   (   i����i    (   i
   i    (   i    i
   (   i    i   (   i����i   (   i����i
   (   i����i   (   i����i	   (   i����i   (   i����i   (   i����i   (   i����i����(   i����i����(   i����i����(   i����i����(   i    i����(   i   i����(   i   i����(   i   i����(   i   i����(   i   i   (   i   i   (   i	   i   (   i   i	   (   i   i   (   i   i
   (   i   i   (   i
   i    (   g��Q�#@g���Q�@(   g�G�z. @g��Q��@(   g��Q��@g�G�z. @(   g���Q�@g��Q�#@(   i    i
   (   g���Q��g��Q�#@(   g��Q���g�G�z. @(   g�G�z. �g��Q��@(   g��Q�#�g���Q�@(   i����i    (   g��Q�#�g���Q��(   g�G�z. �g��Q���(   g��Q���g�G�z. �(   g���Q��g��Q�#�(   g       �g      $�(   g���Q�@g��Q�#�(   g��Q��@g�G�z. �(   g�G�z. @g��Q���(   g��Q�#@g���Q��(   i
   i����(   i
   i
   (   i����i
   (   i����i����(   i
   g�G�z�(   i    g�����'@(   i����g�G�z�(   i    i    (   i����i����(   i    i����(   i   i����(   R   RJ  t   _shapest   _bgpicsRF  R  t   _modet   _delayvalueR�   t
   _colormodet   _keysR.   (   R�   RM  R   R   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s4    					c         C   s�   t  d |  _ t  d |  _ |  j d � |  j d � |  _ d |  _ d |  _ d |  _ g  |  _	 |  j
 d � x d D] } |  j d | � qq Wx" |  j D] } |  j d | � q� Wd t _ d S(   sq  Delete all drawings and all turtles from the TurtleScreen.

        Reset empty TurtleScreen to its initial state: white background,
        no backgroundimage, no eventbindings and tracing on.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.clear()

        Note: this method is not available as function.
        R   R   t   allR�   R�  i   i    R�   i   i   N(   i   i   i   (   R�   R�  R�  Rf  R�  t   _bgpict
   _bgpicnamet   _tracingt   _updatecountert   _turtlesR   RJ   R�   R�  R   R	   t   _pen(   R�   t   btnR�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR.   �  s    				c         C   s�   | d k r |  j S| j �  } | d k r> t d | � � n  | |  _ | d	 k r� |  j |  j d |  j d |  j d |  j d � d |  _ |  _ n  |  j	 �  d S(
   sg  Set turtle-mode ('standard', 'logo' or 'world') and perform reset.

        Optional argument:
        mode -- on of the strings 'standard', 'logo' or 'world'

        Mode 'standard' is compatible with turtle.py.
        Mode 'logo' is compatible with most Logo-Turtle-Graphics.
        Mode 'world' uses userdefined 'worldcoordinates'. *Attention*: in
        this mode angles appear distorted if x/y unit-ratio doesn't equal 1.
        If mode is not given, return the current mode.

             Mode      Initial turtle heading     positive angles
         ------------|-------------------------|-------------------
          'standard'    to the right (east)       counterclockwise
            'logo'        upward    (north)         clockwise

        Examples:
        >>> mode('logo')   # resets turtle heading to north
        >>> mode()
        'logo'
        R�   t   logot   worlds   No turtle-graphics-mode %si   g      �?N(   R�   R�  s   world(   R�   R�  (
   R�   R�  R�  R�  R�  R�   R�   RN  RO  RX   (   R�   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s    	c         C   s  |  j  �  d k r" |  j  d � n  t | | � } t | | � } |  j �  \ } } |  j | d | d � |  j |  j }	 }
 |  j | |  _ |  j | |  _ | |  j } | |  j } |  j | } |  j | } |  j | | | | � |  j	 |  j |	 |  j |
 � |  j
 �  d S(   ss  Set up a user defined coordinate-system.

        Arguments:
        llx -- a number, x-coordinate of lower left corner of canvas
        lly -- a number, y-coordinate of lower left corner of canvas
        urx -- a number, x-coordinate of upper right corner of canvas
        ury -- a number, y-coordinate of upper right corner of canvas

        Set up user coodinat-system and switch to mode 'world' if necessary.
        This performs a screen.reset. If mode 'world' is already active,
        all drawings are redrawn according to the new coordinates.

        But ATTENTION: in user-defined coordinatesystems angles may appear
        distorted. (see Screen.mode())

        Example (for a TurtleScreen instance named screen):
        >>> screen.setworldcoordinates(-10,-0.5,50,1.5)
        >>> for _ in range(36):
        ...     left(10)
        ...     forward(0.5)
        R�  i   N(   R   R�   R�  R   RN  RO  R�   R�   R�  R�  R%   (   R�   t   llxt   llyt   urxt   uryt   xspant   yspant   wxt   wyt	   oldxscalet	   oldyscaleR�  R�  R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR!   �  s     c         C   s�   | d k rO | j �  j d � r< t d |  j | � � } qp t d d � � n! t | t � rp t d | � } n  | |  j | <d S(   s�  Adds a turtle shape to TurtleScreen's shapelist.

        Arguments:
        (1) name is the name of a gif-file and shape is None.
            Installs the corresponding image shape.
            !! Image-shapes DO NOT rotate when turning the turtle,
            !! so they do not display the heading of the turtle!
        (2) name is an arbitrary string and shape is a tuple
            of pairs of coordinates. Installs the corresponding
            polygon shape
        (3) name is an arbitrary string and shape is a
            (compound) Shape object. Installs the corresponding
            compound shape.
        To use a shape, you have to issue the command shape(shapename).

        call: register_shape("turtle.gif")
        --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

        Example (for a TurtleScreen instance named screen):
        >>> screen.register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

        s   .gifR�  s"   Bad arguments for register_shape.
s   Use  help(register_shape)R�  N(	   R�   R�  R�  R   RL  R�  R�   R�   R�  (   R�   t   nameRc   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR     s    c      
   C   s^  t  | � d k r | d } n  t | t � rf |  j | � sI | d k rM | St d t | � � � n  y | \ } } } Wn t d t | � � � n X|  j d k r� g  | | | f D] } t d | � ^ q� \ } } } n  d | k o� d k n o1d | k od k n o1d | k o/d k n sMt d	 t | � � � n  d
 | | | f S(   s  Return color string corresponding to args.

        Argument may be a string or a tuple of three
        numbers corresponding to actual colormode,
        i.e. in the range 0<=n<=colormode.

        If the argument doesn't represent a color,
        an error is raised.
        i   i    R�   s   bad color string: %ss   bad color arguments: %sg      �?g     �o@i�   s   bad color sequence: %ss   #%02x%02x%02x(   R�  R�   R�  Rn  R�  R�  t   round(   R�   R2   R�   t   gt   bR�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   _colorstrA  s    
8Tc         C   s�   | j  d � s | St | � d k rU g  d D]  } t | | | d !d � ^ q, } nS t | � d k r� g  | d D] } d t | | d � ^ qr } n t d	 | � � t g  | D] } | |  j d
 ^ q� � S(   NR�   i   i   i   i   i   i   i   s   bad colorstring: %si�   (   i   i   i   (   R�   R�  R�   R�  R�   R�  (   R�   t   cstrR�  R\  RQ  R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _color\  s    01c         C   sS   | d k r |  j S| d k r1 t | � |  _ n | d k rO t | � |  _ n  d S(   sq  Return the colormode or set it to 1.0 or 255.

        Optional argument:
        cmode -- one of the values 1.0 or 255

        r, g, b values of colortriples have to be in range 0..cmode.

        Example (for a TurtleScreen instance named screen):
        >>> screen.colormode()
        1.0
        >>> screen.colormode(255)
        >>> pencolor(240,160,80)
        g      �?i�   N(   R�   R�  R�   R�   (   R�   t   cmode(    (    s    C:\Python27\lib\lib-tk\turtle.pyR   g  s    c         C   s2   x+ |  j  D]  } | j |  j � | j �  q
 Wd S(   s�   Reset all Turtles on the Screen to their initial state.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.reset()
        N(   R�  t   _setmodeR�  RX   (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRX   |  s    c         C   s   |  j  S(   s�   Return the list of turtles on the screen.

        Example (for a TurtleScreen instance named screen):
        >>> screen.turtles()
        [<turtle.Turtle object at 0x00E11FB0>]
        (   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR$   �  s    c         G   sO   | r |  j  | � } n d } |  j | � } | d k	 rK |  j | � } n  | S(   s�  Set or return backgroundcolor of the TurtleScreen.

        Arguments (if given): a color string or three numbers
        in the range 0..colormode or a 3-tuple of such numbers.

        Example (for a TurtleScreen instance named screen):
        >>> screen.bgcolor("orange")
        >>> screen.bgcolor()
        'orange'
        >>> screen.bgcolor(0.5,0,0.5)
        >>> screen.bgcolor()
        '#800080'
        N(   R�  R�   Ro  R�  (   R�   R.  R2   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s    c         C   sc   | d k r |  j St | � |  _ d |  _ | d k	 rI t | � |  _ n  |  j r_ |  j �  n  d S(   se  Turns turtle animation on/off and set delay for update drawings.

        Optional arguments:
        n -- nonnegative  integer
        delay -- nonnegative  integer

        If n is given, only each n-th regular screen update is really performed.
        (Can be used to accelerate the drawing of complex graphics.)
        Second arguments sets delay value (see RawTurtle.delay())

        Example (for a TurtleScreen instance named screen):
        >>> screen.tracer(8, 25)
        >>> dist = 2
        >>> for i in range(200):
        ...     fd(dist)
        ...     rt(90)
        ...     dist += 2
        i    N(   R�   R�  R�   R�  R�  R%   (   R�   t   nR   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR#   �  s    		c         C   s&   | d k r |  j St | � |  _ d S(   s�    Return or set the drawing delay in milliseconds.

        Optional argument:
        delay -- positive integer

        Example (for a TurtleScreen instance named screen):
        >>> screen.delay(15)
        >>> screen.delay()
        15
        N(   R�   R�  R�   (   R�   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s    c         C   sR   t  j s t t  _ t � n  |  j d k rN |  j d 7_ |  j |  j ;_ n  d S(   s   Increment upadate counter.i    i   N(   R   t   _RUNNINGR�   t	   _RUNNNINGR�  R�  R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _incrementudc�  s    			c         C   sT   |  j  } t |  _  x( |  j �  D] } | j �  | j �  q W| |  _  |  j �  d S(   s'   Perform a TurtleScreen update.
        N(   R�  R�   R$   t   _update_datat   _drawturtleRg  (   R�   t   tracingR�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR%   �  s    		
	c         C   s   |  j  �  d S(   s�    Return the width of the turtle window.

        Example (for a TurtleScreen instance named screen):
        >>> screen.window_width()
        640
        i    (   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR'   �  s    c         C   s   |  j  �  d S(   s�    Return the height of the turtle window.

        Example (for a TurtleScreen instance named screen):
        >>> screen.window_height()
        480
        i   (   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR&   �  s    c         C   s   |  j  S(   s�   Return the Canvas of this TurtleScreen.

        No argument.

        Example (for a Screen instance named screen):
        >>> cv = screen.getcanvas()
        >>> cv
        <turtle.ScrolledCanvas instance at 0x010742D8>
        (   RM  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s    
c         C   s   t  |  j j �  � S(   s�   Return a list of names of all currently available turtle shapes.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.getshapes()
        ['arrow', 'blank', 'circle', ... , 'turtle']
        (   t   sortedR�  R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR     s    	i   c         C   s   |  j  | | | � d S(   s  Bind fun to mouse-click event on canvas.

        Arguments:
        fun -- a function with two arguments, the coordinates of the
               clicked point on the canvas.
        num -- the number of the mouse-button, defaults to 1

        Example (for a TurtleScreen instance named screen
        and a Turtle instance named turtle):

        >>> screen.onclick(goto)
        >>> # Subsequently clicking into the TurtleScreen will
        >>> # make the turtle move to the clicked point.
        >>> screen.onclick(None)
        N(   R�  (   R�   R�  R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRJ     s    c         C   sg   | d k r1 | |  j k rS |  j j | � qS n" | |  j k rS |  j j | � n  |  j | | � d S(   sm  Bind fun to key-release event of key.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example (for a TurtleScreen instance named screen):

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> screen.onkey(f, "Up")
        >>> screen.listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, consequently drawing a hexagon

        N(   R�   R�  t   removeRU  R�  (   R�   R�  R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   "  s    c         C   s   |  j  �  d S(   s  Set focus on TurtleScreen (in order to collect key-events)

        No arguments.
        Dummy arguments are provided in order
        to be able to pass listen to the onclick method.

        Example (for a TurtleScreen instance named screen):
        >>> screen.listen()
        N(   R�  (   R�   t   xdummyt   ydummy(    (    s    C:\Python27\lib\lib-tk\turtle.pyR   @  s    
i    c         C   s   |  j  | | � d S(   s�  Install a timer, which calls fun after t milliseconds.

        Arguments:
        fun -- a function with no arguments.
        t -- a number >= 0

        Example (for a TurtleScreen instance named screen):

        >>> running = True
        >>> def f():
        ...     if running:
        ...             fd(50)
        ...             lt(60)
        ...             screen.ontimer(f, 250)
        ...
        >>> f()   # makes the turtle marching around
        >>> running = False
        N(   R�  (   R�   R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   L  s    c         C   sb   | d k r |  j S| |  j k r; |  j | � |  j | <n  |  j |  j |  j | � | |  _ d S(   sF  Set background image or return name of current backgroundimage.

        Optional argument:
        picname -- a string, name of a gif-file or "nopic".

        If picname is a filename, set the corresponding image as background.
        If picname is "nopic", delete backgroundimage, if present.
        If picname is None, return the filename of the current backgroundimage.

        Example (for a TurtleScreen instance named screen):
        >>> screen.bgpic()
        'nopic'
        >>> screen.bgpic("landscape.gif")
        >>> screen.bgpic()
        'landscape.gif'
        N(   R�   R�  R�  RL  R�  R�  (   R�   t   picname(    (    s    C:\Python27\lib\lib-tk\turtle.pyR   a  s    c         C   s   |  j  | | | � S(   s�  Resize the canvas the turtles are drawing on.

        Optional arguments:
        canvwidth -- positive integer, new width of canvas in pixels
        canvheight --  positive integer, new height of canvas in pixels
        bg -- colorstring or color-tuple, new backgroundcolor
        If no arguments are given, return current (canvaswidth, canvasheight)

        Do not alter the drawing window. To observe hidden parts of
        the canvas use the scrollbars. (Can make visible those parts
        of a drawing, which were outside the canvas before!)

        Example (for a Turtle instance named turtle):
        >>> turtle.screensize(2000,1500)
        >>> # e. g. to search for an erroneously escaped turtle ;-)
        (   R�  (   R�   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   y  s    N($   R�   R�   R�   R�   R�  R�   R  R.   R�   R   R!   R   R�  R�  R   RX   R$   R   R#   R   R�  R%   R'   R&   R   R   RJ   R   R   R   R   R   R   R   R   R   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s@   	"	'$																t
   TNavigatorc           B   s�  e  Z d  Z i e d d � d 6e d d � d 6e d d � d 6Z d Z d Z d Z e d � Z d	 �  Z	 d% d
 � Z d �  Z d d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d% d � Z d �  Z d �  Z d �  Z d% d � Z d% d � Z d �  Z d  �  Z  d% d% d! � Z! d d" � Z" d% d% d# � Z# d% d$ � Z$ e Z% e Z& e Z' e Z( e Z) e Z* e Z+ e Z, e  Z- RS(&   sR   Navigation part of the RawTurtle.
    Implements methods for turtle movement.
    g      �?g        R�   R�  R�  i    i   c         C   s[   |  j  |  _ |  j |  _ | |  _ d  |  _ |  j �  d  |  _ |  j | � t	 j
 |  � d  S(   N(   t   DEFAULT_ANGLEOFFSETt   _angleOffsett   DEFAULT_ANGLEORIENTt   _angleOrientR�  R�   t
   undobufferR3   R�  R�  RX   (   R�   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    		
	c         C   s)   t  d d � |  _ t j |  j |  _ d S(   sX   reset turtle to its initial values

        Will be overwritten by parent class
        g        N(   R   t	   _positionR�  t   START_ORIENTATIONR�  t   _orient(   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRX   �  s    c         C   sj   | d k r |  j S| d	 k r# d S| |  _ | d
 k rM d |  _ d |  _ n |  j d |  _ d |  _ d S(   s:   Set turtle-mode to 'standard', 'world' or 'logo'.
        R�   R�  R�  Ni    i   g      @i����(   s   standards   logos   world(   s   standards   world(   R�   R�  R�  R�  t   _fullcircle(   R�   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  s    		c         C   sB   | |  _  d | |  _ |  j d k r1 d |  _ n | d |  _ d S(   s+   Helper function for degrees() and radians()ih  R�   i    g      @N(   R�  t   _degreesPerAUR�  R�  (   R�   t
   fullcircle(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _setDegreesPerAU�  s
    	g     �v@c         C   s   |  j  | � d S(   s>   Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Dafault value is
        360 degrees.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> turtle.degrees(400.0)
        >>> turtle.heading()
        100

        N(   R   (   R�   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR3   �  s    c         C   s   |  j  d t j � d S(   s    Set the angle measurement units to radians.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        i   N(   R   R�   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRV   �  s    c         C   s%   |  j  |  j | } |  j | � d S(   s)   move turtle forward by specified distanceN(   R�  R�  t   _goto(   R�   R4   t   ende(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _go�  s    c         C   s&   | |  j  9} |  j j | � |  _ d S(   s=   Turn turtle counterclockwise by specified angle if angle > 0.N(   R�  R�  R�   (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _rotate�  s    c         C   s   | |  _  d S(   s   move turtle to position end.N(   R�  (   R�   t   end(    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    c         C   s   |  j  | � d S(   s  Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        N(   R  (   R�   R4   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR<   �  s    c         C   s   |  j  | � d S(   s�  Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        N(   R  (   R�   R4   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR(     s    c         C   s   |  j  | � d S(   s�  Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        N(   R  (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRW   &  s    c         C   s   |  j  | � d S(   s�  Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        N(   R  (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRH   ;  s    c         C   s   |  j  S(   s�   Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        (   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRS   P  s    c         C   s   |  j  d S(   s�    Return the turtle's x coordinate.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        i    (   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRr   ]  s    c         C   s   |  j  d S(   s	   Return the turtle's y coordinate
        ---
        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        i   (   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRs   k  s    c         C   s<   | d k r" |  j t | �  � n |  j t | | � � d S(   st  Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        N(   R�   R  R   (   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRA   z  s    c         C   s!   |  j  d d � |  j d � d S(   s$  Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example (for a Turtle instance named turtle):
        >>> turtle.home()
        i    N(   RA   R\   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRD   �  s    c         C   s!   |  j  t | |  j d � � d S(   s�  Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        i   N(   R  R   R�  (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRa   �  s    c         C   s!   |  j  t |  j d | � � d S(   s�  Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
        i    N(   R  R   R�  (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRb   �  s    c         C   s�   | d k	 r t | | � } n  t | t � r6 | } n9 t | t � rT t | �  } n t | t � ro | j } n  t | |  j � S(   s�  Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
        N(   R�   R   R�   R�   R�  R�  t   abs(   R�   R�   R�   RS   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR4   �  s    	c         C   s�   | d k	 r t | | � } n  t | t � r6 | } n9 t | t � rT t | �  } n t | t � ro | j } n  | |  j \ } } t t j | | � d t j	 d � d } | |  j
 :} |  j |  j | |  j S(   sC  Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0
        g     �f@i
   g     �v@N(   R�   R   R�   R�   R�  R�  R�  R�   Rz   R�   R�  R�  R�  R�  (   R�   R�   R�   RS   t   result(    (    s    C:\Python27\lib\lib-tk\turtle.pyRk   �  s    	*c         C   s_   |  j  \ } } t t j | | � d t j d � d } | |  j :} |  j |  j | |  j S(   s�    Return the turtle's current heading.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0
        g     �f@i
   g     �v@(	   R�  R�  R�   Rz   R�   R�  R�  R�  R�  (   R�   R�   R�   R  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRB     s    
*c         C   sK   | |  j  �  |  j } |  j } | | d | | d } |  j | � d S(   s�  Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        g       @N(   RB   R�  R�  R  (   R�   t   to_angleR�   t   full(    (    s    C:\Python27\lib\lib-tk\turtle.pyR\   !  s    	c         C   s�  |  j  r+ |  j  j d g � t |  j  _ n  |  j �  } | d k rO |  j } n  | d k r� t | � |  j } d t t	 d t | � d d � | � } n  d | | } d | } d | t
 j | t
 j d	 |  j � } | d
 k  r| | | } } } n  |  j �  }	 |  j �  }
 | d
 k r:|  j d
 d
 � n |  j d
 � |  j | � xH t | � D]: } |  j | � |  j | � |  j d
 � |  j | � qaW|  j | � | d
 k r�|  j |	 |
 � n  |  j | � |  j  r�t |  j  _ n  d S(   s�   Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example (for a Turtle instance named turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle
        t   seqi   i   g      @g     �M@g      �?g      �?g       @g     �f@i    N(   R�  R�  R�   R�  Rf   R�   R�  R  R�   t   minR�   R�   R�   R�  R#   Ri  R  R�  R  R�   (   R�   t   radiust   extentt   stepsRf   t   fracRP  t   w2t   lt   trt   dlR�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR-   =  s>    	.
)	c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRf   ~  s    c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   t   aR�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR#   �  s    c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRi  �  s    N(.   R�   R�   R�   R   R�  t   DEFAULT_MODER�  R�  R  RX   R�   R�  R   R3   RV   R  R  R  R<   R(   RW   RH   RS   Rr   Rs   RA   RD   Ra   Rb   R4   Rk   RB   R\   R-   Rf   R#   Ri  R9   R,   R)   RZ   RI   RT   R]   R^   R[   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  sZ   
														#			 #		At   TPenc           B   s  e  Z d  Z e d d � Z e d e d d � Z d d � Z d d � Z d �  Z	 d	 �  Z
 d
 �  Z d d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d d � Z e d � Z e e d � Z d �  Z d �  Z e Z e	 Z e	 Z e
 Z e
 Z e Z e Z  RS(   sF   Drawing part of the RawTurtle.
    Implements drawing properties.
    RY   c         C   s#   | |  _  d  |  _ t j |  � d  S(   N(   t   _resizemodeR�   R�  R  t   _reset(   R�   RY   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    		RO   R;   c         C   sU   d |  _  t |  _ | |  _ | |  _ t |  _ d |  _ d |  _ d |  _ d |  _	 d  S(   Ni   i   i    (   i   i   (
   t   _pensizeR�   t   _shownt	   _pencolort
   _fillcolort   _drawingt   _speedt   _stretchfactort   _tiltt   _outlinewidth(   R�   RO   R;   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    								c         C   sB   | d k r |  j S| j �  } | d k r> |  j d | � n  d S(   sz  Set resizemode to one of the values: "auto", "user", "noresize".

        (Optional) Argument:
        rmode -- one of the strings "auto", "user", "noresize"

        Different resizemodes have the following effects:
          - "auto" adapts the appearance of the turtle
                   corresponding to the value of pensize.
          - "user" adapts the appearance of the turtle according to the
                   values of stretchfactor and outlinewidth (outline),
                   which are set by shapesize()
          - "noresize" no adaption of the turtle's appearance takes place.
        If no argument is given, return current resizemode.
        resizemode("user") is called by a call of shapesize with arguments.


        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'
        t   autot   userR�   RY   N(   R"  s   userR�   (   R�   R  R�  RN   (   R�   t   rmode(    (    s    C:\Python27\lib\lib-tk\turtle.pyRY   �  s
    c         C   s'   | d k r |  j S|  j d | � d S(   s!  Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        RQ   N(   R�   R  RN   (   R�   Rp   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRQ   �  s    c         C   s!   |  j  s d S|  j d t � d S(   s�   Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        NRP   (   R  RN   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRR   �  s    
	c         C   s!   |  j  r d S|  j d t � d S(   s�   Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        NRP   (   R  RN   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRP   �  s    
	c         C   s   |  j  S(   s  Return True if pen is down, False if it's up.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True
        (   R  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRF   �  s    c         C   s�   i d d 6d d 6d d 6d d 6d	 d
 6} | d k r< |  j S| | k rU | | } n7 d | k  ol d k  n r� t t | � � } n d } |  j d | � d S(   s�   Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Attention:
        speed = 0 : *no* animation takes place. forward/back makes turtle jump
        and likewise left/right make the turtle turn instantly.

        Example (for a Turtle instance named turtle):
        >>> turtle.speed(3)
        i    t   fastesti
   t   fasti   t   normali   t   slowi   t   slowestg      �?g      %@Rf   N(   R�   R  R�   R�  RN   (   R�   Rf   t   speeds(    (    s    C:\Python27\lib\lib-tk\turtle.pyRf     s    )c         G   s�   | r� t  | � } | d k r/ | d } } n4 | d k rJ | \ } } n | d k rc | } } n  |  j | � } |  j | � } |  j d | d | � n" |  j |  j � |  j |  j � f Sd S(   s�  Return or set the pencolor and fillcolor.

        Arguments:
        Several input formats are allowed.
        They use 0, 1, 2, or 3 arguments as follows:

        color()
            Return the current pencolor and the current fillcolor
            as a pair of color specification strings as are returned
            by pencolor and fillcolor.
        color(colorstring), color((r,g,b)), color(r,g,b)
            inputs as in pencolor, set both, fillcolor and pencolor,
            to the given value.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
            and analogously, if the other input format is used.

        If turtleshape is a polygon, outline and interior of that polygon
        is drawn with the newly set colors.
        For mor info see: pencolor, fillcolor

        Example (for a Turtle instance named turtle):
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')
        i   i    i   i   RO   R;   N(   R�  R�  RN   R�  R  R  (   R�   R.  R  t   pcolort   fcolor(    (    s    C:\Python27\lib\lib-tk\turtle.pyR2   *  s     c         G   sO   | r; |  j  | � } | |  j k r( d S|  j d | � n |  j |  j � Sd S(   sZ   Return or set the pencolor.

        Arguments:
        Four input formats are allowed:
          - pencolor()
            Return the current pencolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - pencolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - pencolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - pencolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the outline of that polygon is drawn
        with the newly set pencolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'
        NRO   (   R�  R  RN   R�  (   R�   R.  R2   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRO   X  s    c         G   sO   | r; |  j  | � } | |  j k r( d S|  j d | � n |  j |  j � Sd S(   s]   Return or set the fillcolor.

        Arguments:
        Four input formats are allowed:
          - fillcolor()
            Return the current fillcolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - fillcolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - fillcolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - fillcolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the interior of that polygon is drawn
        with the newly set fillcolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.fillcolor('violet')
        >>> col = turtle.pencolor()
        >>> turtle.fillcolor(col)
        >>> turtle.fillcolor(0, .5, 0)
        NR;   (   R�  R  RN   R�  (   R�   R.  R2   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR;   }  s    c         C   s   |  j  d t � d S(   s�   Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        t   shownN(   RN   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRe   �  s    c         C   s   |  j  d t � d S(   sY  Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        R-  N(   RN   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRC   �  s    c         C   s   |  j  S(   s�   Return True if the Turtle is shown, False if it's hidden.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> print turtle.isvisible():
        False
        (   R  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRG   �  s    
c   	      K   s6  i
 |  j  d 6|  j d 6|  j d 6|  j d 6|  j d 6|  j d 6|  j d 6|  j d 6|  j d	 6|  j	 d
 6} | ps | sz | St
 | t � r� | } n i  } | j | � i  } x | D] } | | | | <q� W|  j r� |  j j d | f � n  t } d | k r|  j | d k rt } qn  d | k rxt
 | d t � rY|  j | d f � | d <n  |  j | d k rxt } qxn  d | k r�|  j | d k r�t } q�n  | r�|  j �  n  d | k r�| d |  _ n  d | k r�| d |  _ n  d | k r
| d |  _ n  d | k rVt
 | d t � rF|  j | d f � | d <n  | d |  _ n  d | k rr| d |  _ n  d | k r�| d |  _ n  d | k r�| d } t
 | t t f � r�| | f } n  | |  _ n  d	 | k r�| d	 |  _ n  d | k r| d |  _  n  d
 | k r(| d
 |  _	 n  |  j �  d S(   s�  Return or set the pen's attributes.

        Arguments:
            pen -- a dictionary with some or all of the below listed keys.
            **pendict -- one or more keyword-arguments with the below
                         listed keys as keywords.

        Return or set the pen's attributes in a 'pen-dictionary'
        with the following key/value pairs:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "outline"    :   positive number
           "tilt"       :   number

        This dictionary can be used as argument for a subsequent
        pen()-call to restore the former pen-state. Moreover one
        or more of these attributes can be provided as keyword-arguments.
        This can be used to set several pen attributes in one statement.


        Examples (for a Turtle instance named turtle):
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3}
        R-  RP   RO   R;   RQ   Rf   RY   t   stretchfactorRR  Ri   RN   N(   R  R  R  R  R  R  R  R  R!  R   R�   t   dictR%   R�  R�  R�   R�   R�   R�  t   _newLineR�   R�   Rg  (	   R�   RN   t   pendictt   _pdt   pt   _p_bufR�   t   newLinet   sf(    (    s    C:\Python27\lib\lib-tk\turtle.pyRN   �  sz    .







		
c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   t   usePos(    (    s    C:\Python27\lib\lib-tk\turtle.pyR0  ?	  s    c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   R�  t   forced(    (    s    C:\Python27\lib\lib-tk\turtle.pyRg  A	  s    c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   R.  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  C	  s    c         C   s   d S(   s/   dummy method - to be overwritten by child classN(    (   R�   R.  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  E	  s    N(!   R�   R�   R�   R�   R  R  R�   RY   RQ   RR   RP   RF   Rf   R2   RO   R;   Re   RC   RG   RN   R�   R0  R�   Rg  R�  R�  Rp   Ro   RU   RM   R6   Rg   RE   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s8   			&	.	%	$			u		t   _TurtleImagec           B   s    e  Z d  Z d �  Z d �  Z RS(   s6   Helper class: Datatype to store Turtle attributes
    c         C   s#   | |  _  d  |  _ |  j | � d  S(   N(   R�   R�   R�  t	   _setshape(   R�   R�   t
   shapeIndex(    (    s    C:\Python27\lib\lib-tk\turtle.pyR  U	  s    		c         C   se  |  j  } | |  _ |  j d k o6 | j | j k n r? d  S|  j d k oc | j | j k n rl d  S|  j d k r� | j |  j � n3 |  j d k r� x! |  j D] } | j | � q� Wn  | j | j |  _ |  j d k r� | j �  |  _ nl |  j d k r#| j | j d j � |  _ n> |  j d k rag  | j | j D] } | j �  ^ qC|  _ n  d  S(   NR�  R�  R�  RH  (   s   images   polygon(	   R�   R;  R�  R�  Rf  t   _itemRT  R�  R�  (   R�   R;  R�   Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR:  Z	  s&    		))(   R�   R�   R�   R  R:  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR9  Q	  s   	c           B   s  e  Z d  Z g  Z d8 e d e d e d d � Z d �  Z d �  Z d �  Z	 d �  Z
 d	 �  Z d
 �  Z d �  Z d8 d8 d � Z d �  Z d �  Z d �  Z d �  Z d8 d � Z d8 d8 d8 d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z d8 d � Z d �  Z d �  Z d �  Z  e! d � Z" d8 d  � Z# d! �  Z$ d" �  Z% d8 d# � Z& d$ �  Z' e( d% d9 d) � Z) d* �  Z* d+ �  Z+ d, �  Z, d- �  Z- d. �  Z. e. Z/ d/ �  Z0 d0 �  Z1 d8 d1 � Z2 d2 d8 d3 � Z3 d2 d8 d4 � Z4 d2 d8 d5 � Z5 d6 �  Z6 d7 �  Z7 e Z8 RS(:   sv   Animation part of the RawTurtle.
    Puts RawTurtle upon a TurtleScreen and provides tools for
    its animation.
    Rc   R�   R�   c         C   s�  t  | t � r | |  _ n� t  | t � rX | t j k rL t j j | � n  | |  _ nz t  | t t f � r� xb t j D]" } | j	 | k rw | |  _ Pqw qw Wt | � |  _ t j j |  j � n t
 d | � � |  j } t j |  | j �  � t j |  � | j j |  � | j �  |  _ t | | � |  _ d  |  _ t |  _ d  |  _ |  _ | |  _ t |  _ | j �  |  _ |  j g |  _ |  j g |  _ g  |  _  | |  _! t" | � |  _# |  j$ �  d  S(   Ns   bad cavas argument %s(%   R�   t   _ScreenR�   R   R   t   screensRU  R   R  RM  R�  R�  R  R   R  R�  Ra  t   drawingLineItemR9  R�   R�   t   _polyR�   t   _creatingPolyt	   _fillitemt	   _fillpathR  t   _hidden_from_screent   currentLineItemR�  t   currentLineR�   t
   stampItemst   _undobuffersizeR�  R�  Rg  (   R�   t   canvasRc   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  w	  s@    								c         C   s<   t  j |  � t j |  � |  j �  |  j �  |  j �  d S(   s�  Delete the turtle's drawings and restore its default values.

        No argument.
,
        Delete the turtle's drawings from the screen, re-center the turtle
        and set variables to the default values.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0
        N(   R�  RX   R  R  t   _clearR�  Rg  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRX   �	  s
    

c         C   s+   | d k r d |  _ n t | � |  _ d S(   s�  Set or disable undobuffer.

        Argument:
        size -- an integer or None

        If size is an integer an empty undobuffer of given size is installed.
        Size gives the maximum number of turtle-actions that can be undone
        by the undo() function.
        If size is None, no undobuffer is present.

        Example (for a Turtle instance named turtle):
        >>> turtle.setundobuffer(42)
        N(   R�   R�  R�  (   R�   t   size(    (    s    C:\Python27\lib\lib-tk\turtle.pyR`   �	  s    c         C   s    |  j  d k r d S|  j  j �  S(   s�   Return count of entries in the undobuffer.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> while undobufferentries():
        ...     undo()
        i    N(   R�  R�   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRn   �	  s    	c         C   s�   d |  _ |  _ x! |  j D] } |  j j | � q W|  j j �  |  _ g  |  _ |  j	 rn |  j j
 |  j � n  |  j g |  _ |  j �  |  j |  j � d S(   s   Delete all of pen's drawingsN(   R�   RB  RC  R�   R�   Rf  Ra  RE  RF  R  RU  R�  R0   R`   RH  (   R�   Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRJ  �	  s    		
c         C   s   |  j  �  |  j �  d S(   sg  Delete the turtle's drawings from the screen. Do not move turtle.

        No arguments.

        Delete the turtle's drawings from the screen. Do not move turtle.
        State and position of the turtle as well as drawings of other
        turtles are not affected.

        Examples (for a Turtle instance named turtle):
        >>> turtle.clear()
        N(   RJ  Rg  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR.   �	  s    
c         C   sd   |  j  j �  |  j  j d k r# d  St |  j � d k r` |  j  j |  j |  j |  j |  j � n  d  S(   Ni    i   (	   R�   R�  R�  R�  RF  Rc  RE  R  R  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �	  s    c         C   s�   |  j  } | j d k r d S| j d k r\ |  j �  |  j �  | j �  | j | j � nG |  j �  | j d k r� x | j �  D] } | j �  q� W| j �  n  d S(   s&   Perform a Turtle-data update.
        i    Ni   (	   R�   R�  R�  R�  Rg  Ri  R�  R�  R$   (   R�   R�   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRg  �	  s    	



c         C   s   |  j  j | | � S(   sm  Turns turtle animation on/off and set delay for update drawings.

        Optional arguments:
        n -- nonnegative  integer
        delay -- nonnegative  integer

        If n is given, only each n-th regular screen update is really performed.
        (Can be used to accelerate the drawing of complex graphics.)
        Second arguments sets delay value (see RawTurtle.delay())

        Example (for a Turtle instance named turtle):
        >>> turtle.tracer(8, 25)
        >>> dist = 2
        >>> for i in range(200):
        ...     turtle.fd(dist)
        ...     turtle.rt(90)
        ...     dist += 2
        (   R�   R#   (   R�   t   flagR   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR#   
  s    c         C   s   |  j  j | � S(   N(   R�   R�  (   R�   R.  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  $
  s    c         C   s   |  j  j | � S(   N(   R�   R�  (   R�   R.  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  '
  s    c      	   C   s  t  | t � r | Sy | \ } } } Wn t d t | � � � n X|  j j d k r� g  | | | f D] } t d | � ^ qh \ } } } n  d | k o� d k n o� d | k o� d k n o� d | k o� d k n s� t d t | � � � n  d | | | f S(   s,   Convert colortriples to hexstrings.
        s   bad color arguments: %sg      �?g     �o@i    i�   s   bad color sequence: %ss   #%02x%02x%02x(   R�   R�  R�  R�   R�  R�  (   R�   R.  R�   R�  R�  R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _cc*
  s    8Tc         C   sI  |  j  } |  j |  j � |  j } d |  _  d |  _ t |  � } | |  _  | |  _ | | _  t | |  j j � | _ | j j	 | � | j
 |  j j j } | d k r� | j �  | j _ nr | d k r� | j | j
 d j � | j _ nD | d k r,g  | j
 |  j j j D] } | j �  ^ q| j _ n  | j �  | _ | j �  | S(   s  Create and return a clone of the turtle.

        No argument.

        Create and return a clone of the turtle with same position, heading
        and turtle properties.

        Example (for a Turtle instance named mick):
        mick = Turtle()
        joe = mick.clone()
        R�  R�  RH  R�  N(   R�   R0  R  R�   R�   R   R9  R;  R�  RU  R�  R�  RT  R<  R�  R�  Ra  RE  Rg  (   R�   R�   R�   t   qt   ttypeRe  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR1   9
  s,    							"5
c         C   s\   | d k r |  j j S| |  j j �  k r> t d | � � n  |  j j | � |  j �  d S(   s�  Set turtle shape to shape with given name / return current shapename.

        Optional argument:
        name -- a string, which is a valid shapename

        Set turtle shape to shape with given name or, if name is not given,
        return name of current shape.
        Shape with name must exist in the TurtleScreen's shape dictionary.
        Initially there are the following polygon shapes:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        To learn about how to deal with shapes see Screen-method register_shape.

        Example (for a Turtle instance named turtle):
        >>> turtle.shape()
        'arrow'
        >>> turtle.shape("turtle")
        >>> turtle.shape()
        'turtle'
        s   There is no shape named %sN(   R�   R�   R;  R�   R   R�  R:  Rg  (   R�   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRc   a
  s    
c      	   C   s�   | | k o" | k o" d k n rF |  j \ } } | | |  j f S| d k	 r| | d k rm | | f } q� | | f } n+ | d k	 r� |  j d | f } n	 |  j } | d k r� |  j } n  |  j d d d | d | � d S(   sP  Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optinonal arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        i    RY   R#  R.  RR  N(   R�   R  R!  RN   (   R�   t   stretch_widt   stretch_lenRR  R.  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRd   |
  s    '	c         C   sK   | |  j  |  j } | t j d d t j } |  j d d d | � d S(   sZ  Rotate the turtleshape to point in the specified direction

        Optional argument:
        angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).


        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.settiltangle(45)
        >>> stamp()
        >>> turtle.fd(50)
        >>> turtle.settiltangle(-45)
        >>> stamp()
        >>> turtle.fd(50)
        g     �f@i   RY   R#  Ri   N(   R�  R�  R�   R�   RN   (   R�   R�   Ri   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR_   �
  s    c         C   s.   |  j  d t j |  j } | |  j |  j S(   s�  Return the current tilt-angle.

        No argument.

        Return the current tilt-angle, i. e. the angle between the
        orientation of the turtleshape and the heading of the turtle
        (its direction of movement).

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(45)
        >>> turtle.tiltangle()
        g     �f@(   R   R�   R�   R�  R�  R�  (   R�   Ri   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRj   �
  s    c         C   s   |  j  | |  j �  � d S(   s�  Rotate the turtleshape by angle.

        Argument:
        angle - a number

        Rotate the turtleshape by angle from its current tilt-angle,
        but do NOT change the turtle's heading (direction of movement).

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        N(   R_   Rj   (   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRi   �
  s    c   
      C   s�   |  j  } |  j \ } } |  j \ } } t | | | j | j � } d t | � | \ } } g  | D]G \ } }	 | | | | |	 | j | | | | |	 | j f ^ qe S(   sl   Computes transformed polygon shapes from a shape
        according to current position and heading.
        g      �?(   R�   R�  R�  R   RO  RN  R  (
   R�   R�  R�   t   p0t   p1t   e0t   e1R~   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   _polytrafo�
  s    	c         C   s}  |  j  } | j |  j j } | j } |  j j } |  j r�| j d k r�| j d k r�t	 |  _
 | j } | d k r�|  j d k r� d } | } n� |  j d k r� t d |  j d � } } |  j } d }	 n3 |  j d k r|  j \ } } |  j } |  j }	 n  g  | D]  \ }
 } | |
 | | f ^ q	} t j |	 � t j |	 � } } g  | D]1 \ }
 } | |
 | | | |
 | | f ^ qU} |  j | � } |  j |  j } } | j | | d | d	 | d
 | d t �qy| d k r�| j | |  j | � qy| d k ry|  j \ } } |  j } x� t | | � D]� \ } \ } } } g  | D]  \ }
 } | |
 | | f ^ qN} |  j | � } | j | | d |  j | � d	 |  j | � d
 | d t �q2Wqyn� |  j
 r�d S| d k r| j | d d d f d d � nn | d k r1| j | |  j | j d j � n? | d k rpx0 | D]% } | j | d d d f d d � qDWn  t |  _
 d S(   sp   Manages the correct rendering of the turtle with respect to
        its shape, resizemode, stretch and tilt etc.i    R�  R�   i   R"  g      @R#  R:   RR  Rp   R[  R�  R�  NR�   RH  (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   R�   R�  R�   R;  R�  R<  R  R�  R�  R�   RD  R�  R  t   maxR  R  R!  R   R�   R�   R|   RV  R  R  R]  R�   R�  R�  t   zipRM  (   R�   R�   Rc   RO  t   titemt   tshapeRP  t   lxt   lyRj   R�   R�   t   t0t   t1t   fct   ocRe  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �
  s^    		'						->	%-&	"&c         C   s	  |  j  } | j |  j j } | j } | j } | d k r�| j �  } |  j d k rd d } | } n� |  j d k r� t d |  j	 d � } } |  j	 } d }	 n3 |  j d k r� |  j
 \ } } |  j } |  j }	 n  g  | D]  \ }
 } | |
 | | f ^ q� } t j |	 � t j |	 � } } g  | D]1 \ }
 } | |
 | | | |
 | | f ^ q%} |  j | � } |  j |  j } } | j | | d | d	 | d
 | d t �n6| d k r�| j d � } | j | |  j | � n| d k r�g  } x' | D] } | j �  } | j | � q�Wt | � } |  j
 \ } } |  j } x� t | | � D]� \ } \ } } } g  | D]  \ }
 } | |
 | | f ^ qi} |  j | � } | j | | d |  j | � d	 |  j | � d
 | d t �qMWn  |  j j | � |  j j d | f � | S(   s�  Stamp a copy of the turtleshape onto the canvas and return its id.

        No argument.

        Stamp a copy of the turtle shape onto the canvas at the current
        turtle position. Return a stamp_id for that stamp, which can be
        used to delete it by calling clearstamp(stamp_id).

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> turtle.stamp()
        13
        >>> turtle.fd(50)
        R�  R�   i   R"  g      @i    R#  R:   RR  Rp   R[  R�  R�   R�  Rh   (   R�   R�  R�   R;  R�  R�  RT  R  RW  R  R  R!  R   R�   R�   R|   RV  R  R  R]  R�   R�  R�  R�  RU  R�   RX  RM  RG  R�  R�  (   R�   R�   Rc   RO  RZ  t   stitemRP  R[  R\  Rj   R�   R�   R]  R^  R_  R`  t   elementRe  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRh   #  sV    							->	%-#c         C   s   | |  j  k re t | t � rB x1 | D] } |  j j | � q% Wn |  j j | � |  j  j | � n  d | f } |  j } | | j k r� d S| j j | � } | j j | � | | j	 k r� | j	 d | j
 | _	 n  | j j | j	 d | j
 d g � d S(   s9   does the work for clearstamp() and clearstamps()
        Rh   Ni   (   RG  R�   R�   R�   Rf  R�  R�  R�  t   indexR�  R�  t   insertR�   (   R�   t   stampidt   subitemRe  t   bufRc  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _clearstamp_  s    	c         C   s   |  j  | � |  j �  d S(   sD  Delete stamp with given stampid

        Argument:
        stampid - an integer, must be return value of previous stamp() call.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> astamp = turtle.stamp()
        >>> turtle.fd(50)
        >>> turtle.clearstamp(astamp)
        N(   Rh  Rg  (   R�   Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR/   u  s    c         C   sn   | d k r |  j } n) | d k r5 |  j |  } n |  j | } x | D] } |  j | � qI W|  j �  d S(   s�  Delete all or first/last n of turtle's stamps.

        Optional argument:
        n -- an integer

        If n is None, delete all of pen's stamps,
        else if n > 0 delete first n stamps
        else if n < 0 delete last n stamps.

        Example (for a Turtle instance named turtle):
        >>> for i in range(8):
        ...     turtle.stamp(); turtle.fd(30)
        ...
        >>> turtle.clearstamps(2)
        >>> turtle.clearstamps(-2)
        >>> turtle.clearstamps()
        i    N(   R�   RG  Rh  Rg  (   R�   R�  t   toDeleteRe  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR0   �  s    c         C   sf  |  j  |  j |  j t |  j t � f } |  j } d |  j | | |  j |  j	 | j
 |  j � |  j f f } |  j r� |  j j | � n  |  j } |  j r�| j d k r�| | } | d | j d | d | j d } d t | d d d |  j |  j � } | d | }	 x� t d | � D]s }
 |
 d k r=t } n t } | |	 |
 |  _ |  j  r�| j |  j | |  j f |  j |  j | � n  |  j �  q"W|  j  r�| j |  j d d f d	 d
 d |  j �q�n  |  j  r�|  j	 j | � n  t |  j t � r|  j j | � n  | |  _ |  j r6|  j j | � n  t |  j	 � d k rX|  j �  n  |  j �  d S(   s�   Move the pen to the point end, thereby drawing a line
        if pen is down. All other methodes for turtle movement depend
        on this one.
        t   goi   i    i   g      �?i   g�������?g      �?R:   R�   Rp   i*   N(   i    i    (   i    i    (   R  R  R  R�   RC  R�   R�   R�  RE  RF  R�  R�   R�  R�  R  R�  RN  RO  R�   R�  R�   R�   Rc  R?  Rg  RU  RA  R@  R�  R0  (   R�   R  t   go_modesR�   t
   undo_entryt   startt   difft   diffsqt   nhopst   deltaR�  R[  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  sR    			
(*						c         C   s  | \ } } } } | \ } } } }	 | \ }
 } } } |  j  } t |  j | � d k r` d GHn  |
 |  _ | |  _ | d d g k r� d } n | } | j |
 | d | d | �g  |  j D]- } | | k r� | j | � d k r� | ^ q� } x+ | D]# } | j | � |  j j	 | � q� W| } |  j
 rQ| j d k rQ| | } | d | j d	 | d | j d	 } d t | d d
 d |  j
 |  j
 � } | d | } x{ t d | � D]j } | d k r�t } n t } | | | |  _ | r| j |  j | |  j f | | | � n  |  j �  q�W| rQ| j |  j d d f d d d | �qQn  | |  _ |  j r�t |  j � d k r�|  j j �  n  |  j g  k r�t |  _ d |  _ q�n  |	 r�|  j g  k r�d |  _ d GHq�|  j d k	 r�|  j j �  q�n  |  j �  d S(   s)   Reverse a _goto. Used for undo()
        g      �?s$   undogoto: HALLO-DA-STIMMT-WAS-NICHT!i    R�   R:   Rp   R�   i   i   i   g�������?g      �?s   Unwahrscheinlich in _undogoto!N(   i    i    (   i    i    (   i    i    (   i    i    (   R�   R  R�  RE  RF  Rc  R�   R�  Rf  R�  R  R�  RN  RO  R�   R�  R�   R�   R?  Rg  RA  R�  R@  R�  R�   RC  (   R�   t   entryt   oldt   newRk  t   coodatat   drawingt   pct   pst   fillingt   cLIt   cLR�  R�   R�   t   usepcR�  t   todeleteRm  Rn  Ro  Rp  Rq  R�  R[  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   _undogoto�  sd    				!
(*					c         C   s�   |  j  r( |  j  j d | |  j f � n  | |  j 9} |  j j | � } |  j j } | d k r� |  j d k r� d |  j } d t t	 | � | � } d | | } x6 t
 | � D]% } |  j j | � |  _ |  j �  q� Wn  | |  _ |  j �  d S(   s&   Turns pen clockwise by angle.
        t   roti   i    g      @g      �?N(   R�  R�  R�  R�  R�   R�   R�  R  R�   R  R�  Rg  (   R�   R�   t	   neworientR�  t   anglevelR  Rq  R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR    s    		c         C   s�   t  |  j � d k rb |  j j |  j |  j |  j |  j � |  j j �  |  _ |  j j	 |  j � n |  j j |  j d t
 �g  |  _ | r� |  j g |  _ n  d S(   s�   Closes current line item and starts a new one.
           Remark: if current line became too long, animation
           performance (via _drawline) slowed down considerably.
        i   R[  N(   R�  RF  R�   Rc  RE  R  R  Ra  R�   RU  R�   R�  (   R�   R7  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR0  (  s    	c         C   sm  t  |  j t � } | d k r" | S|  j } d } } | r� t |  j � d k r� |  j j |  j |  j d |  j �d |  j f } q� n  | r� |  j j	 �  |  _ |  j
 j |  j � |  j g |  _ d |  j f } |  j �  n d |  _ |  _ |  j r_| d k r$| d	 k r\|  j j | � q\q_| d
 k rC|  j j | � q_|  j j d | | g � n  |  j �  d S(   s�  Call fill(True) before drawing a shape to fill, fill(False) when done.

        Optional argument:
        flag -- True/False (or 1/0 respectively)

        Call fill(True) before drawing the shape you want to fill,
        and  fill(False) when done.
        When used without argument: return fillstate (True if filling,
        False else)

        Example (for a Turtle instance named turtle):
        >>> turtle.fill(True)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.fill(False)
        i   R:   t   dofillt	   beginfillR
  N(    (    (    (    (   R�   RC  R�   R�   R�   R�  R]  RB  R  RT  R�   RU  R�  R0  R�  R�  Rg  (   R�   RL  Ry  R�   t   entry1t   entry2(    (    s    C:\Python27\lib\lib-tk\turtle.pyR:   8  s2    	

	c         C   s   |  j  t � d S(   s�  Called just before drawing a shape to be filled.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.end_fill()
        N(   R:   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR*   k  s    c         C   s   |  j  t � d S(   s�  Fill the shape drawn after the call begin_fill().

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.left(90)
        >>> turtle.forward(100)
        >>> turtle.end_fill()
        N(   R:   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR7   }  s    c         G   s�  | st t  | t t f � rF |  j | � } |  j t |  j d � } q� |  j } | s� |  j t |  j d � } q� n7 | d k r� |  j t |  j d � } n  |  j | � } t |  j	 d � r|  j	 j
 |  j | | � } |  j j | � |  j r�|  j j d | f � q�n� |  j �  } |  j rD|  j j d g � t |  j _ n  zT |  j �  d k rf|  j �  n  |  j �  |  j | � |  j | � |  j d � Wd |  j | � X|  j r�t |  j _ n  d S(   s�  Draw a dot with diameter size, using color.

        Optional arguments:
        size -- an integer >= 1 (if given)
        color -- a colorstring or a numeric color tuple

        Draw a circular dot with diameter size, using color.
        If size is not given, the maximum of pensize+4 and 2*pensize is used.

        Example (for a Turtle instance named turtle):
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
        i   t   _dotR5   R
  R"  i    N(   R�   R�  R�   R�  R  RW  R  R�   t   hasattrR�   R�  R�  R�   RU  R�  R�  RN   R�   R�  RY   RE   RP   RQ   RO   R<   R�   (   R�   RK  R2   Re  RN   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR5   �  s:    			
	c         C   s`   |  j  j |  j | | | |  j � \ } } |  j j | � |  j r\ |  j j d | f � n  | S(   s)   Performs the writing for write()
        t   wri(   R�   R}  R�  R  R�   RU  R�  R�  (   R�   Rw  Rx  Ru  Re  R  (    (    s    C:\Python27\lib\lib-tk\turtle.pyR}  �  s    	RH   t   Ariali   R'  c         C   s�   |  j  r+ |  j  j d g � t |  j  _ n  |  j t | � | j �  | � } | rw |  j �  \ } } |  j | | � n  |  j  r� t	 |  j  _ n  d S(   s�  Write text at the current turtle position.

        Arguments:
        arg -- info, which is to be written to the TurtleScreen
        move (optional) -- True/False
        align (optional) -- one of the strings "left", "center" or right"
        font (optional) -- a triple (fontname, fontsize, fonttype)

        Write text - the string representation of arg - at the current
        turtle position according to align ("left", "center" or right")
        and with the given font.
        If move is True, the pen is moved to the bottom-right corner
        of the text. By default, move is False.

        Example (for a Turtle instance named turtle):
        >>> turtle.write('Home = ', True, align="center")
        >>> turtle.write((0,0), True)
        R
  N(
   R�  R�  R�   R�  R}  R�  R�  RS   R]   R�   (   R�   t   argt   moveRx  Ru  R  R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRq   �  s    	!	c         C   s   |  j  g |  _ t |  _ d S(   s  Start recording the vertices of a polygon.

        No argument.

        Start recording the vertices of a polygon. Current turtle position
        is first point of polygon.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_poly()
        N(   R�  R@  R�   RA  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR+   �  s    c         C   s   t  |  _ d S(   s7  Stop recording the vertices of a polygon.

        No argument.

        Stop recording the vertices of a polygon. Current turtle position is
        last point of polygon. This will be connected with the first point.

        Example (for a Turtle instance named turtle):
        >>> turtle.end_poly()
        N(   R�   RA  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR8   �  s    c         C   s    |  j  d k	 r t |  j  � Sd S(   s�   Return the lastly recorded polygon.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> p = turtle.get_poly()
        >>> turtle.register_shape("myFavouriteShape", p)
        N(   R@  R�   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR=     s    
c         C   s   |  j  S(   s�  Return the TurtleScreen object, the turtle is drawing  on.

        No argument.

        Return the TurtleScreen object, the turtle is drawing  on.
        So TurtleScreen-methods can be called for that object.

        Example (for a Turtle instance named turtle):
        >>> ts = turtle.getscreen()
        >>> ts
        <turtle.TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")
        (   R�   (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR?     s    c         C   s   |  S(   sU  Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        (    (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR@   !  s    c         C   s   |  j  j �  d S(   s�    Returns the width of the turtle window.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.window_width()
        640
        i    (   R�   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR'   9  s    	c         C   s   |  j  j �  d S(   s�    Return the height of the turtle window.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.window_height()
        480
        i   (   R�   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR&   D  s    	c         C   s   |  j  j | � S(   sD   Set delay value which determines speed of turtle animation.
        (   R�   R   (   R�   R   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRi  O  s    i   c         C   s-   |  j  j |  j j | | | � |  j �  d S(   s�  Bind fun to mouse-click event on this turtle on canvas.

        Arguments:
        fun --  a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).
        add --  True or False. If True, new binding will be added, otherwise
                it will replace a former binding.

        Example for the anonymous turtle, i. e. the procedural way:

        >>> def turn(x, y):
        ...     left(360)
        ...
        >>> onclick(turn)  # Now clicking into the turtle will turn it.
        >>> onclick(None)  # event-binding will be removed
        N(   R�   R�  R�   R<  Rg  (   R�   R�  R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRJ   V  s    c         C   s-   |  j  j |  j j | | | � |  j �  d S(   s�  Bind fun to mouse-button-release event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
        ...     def glow(self,x,y):
        ...             self.fillcolor("red")
        ...     def unglow(self,x,y):
        ...             self.fillcolor("")
        ...
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)

        Clicking on joe turns fillcolor red, unclicking turns it to
        transparent.
        N(   R�   R�  R�   R<  Rg  (   R�   R�  R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRL   k  s    c         C   s#   |  j  j |  j j | | | � d S(   s�  Bind fun to mouse-move event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
               the coordinates of the clicked point on the canvas.
        num -- number of the mouse-button defaults to 1 (left mouse button).

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.

        Example (for a Turtle instance named turtle):
        >>> turtle.ondrag(turtle.goto)

        Subsequently clicking and dragging a Turtle will move it
        across the screen thereby producing handdrawings (if pen is
        down).
        N(   R�   R�  R�   R<  (   R�   R�  R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRK   �  s    c         C   s�  |  j  d k r d S| d k rV | \ } } |  j | | |  j � |  j  j �  } n5| d k r| | d } |  j | � n| d k r� |  j | � n� | d k r� | d } |  j j | � |  j	 j
 | � n� | d k r| d } |  j j | d d d f d	 d
 d d
 �ny | d k r[| d } d |  _ |  _ |  j j | � |  j	 j
 | � n0 | d k r�t j |  | d � |  j  j �  n  d S(   s2   Does the main part of the work for undo()
        NR  Rh   i    Rj  R�  R5   R�  R:   R�   RR  R�  RN   (   s   wris   dot(   i    i    (   i    i    (   i    i    (   R�  R�   R  R�  R�  R/   R~  R�   Rf  R�   R�  R]  RB  RC  R  RN   (   R�   t   actionR�  R�   t   degPAUt   dummyRa  Re  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _undo�  s6    



c         C   s�   |  j  d k r d S|  j  j �  } | d } | d } | d k rv xA | rr | j �  } |  j | d | d � qE Wn |  j | | � d S(   s�  undo (repeatedly) the last turtle action.

        No argument.

        undo (repeatedly) the last turtle action.
        Number of available undo actions is determined by the size of
        the undobuffer.

        Example (for a Turtle instance named turtle):
        >>> for i in range(4):
        ...     turtle.fd(50); turtle.lt(80)
        ...
        >>> for i in range(8):
        ...     turtle.undo()
        ...
        Ni    i   R
  (   R�  R�   R�  R�  (   R�   Re  R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyRm   �  s    

	N(   R�  i   s   normal(9   R�   R�   R�   R>  R�   R�   R  RX   R`   Rn   RJ  R.   R�  Rg  R#   R�  R�  RM  R1   Rc   Rd   R_   Rj   Ri   RV  R�  Rh   Rh  R/   R0   R  R~  R  R�   R0  R:   R*   R7   R5   R}  R�   Rq   R+   R8   R=   R?   R@   R>   R'   R&   Ri  RJ   RL   RK   R�  Rm   Rl   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   p	  sl   %											(&					7	<			5	A	3		3	
									c           C   s%   t  j d k r t �  t  _ n  t  j S(   s�   Return the singleton screen object.
    If none exists at the moment, create a new one and return it,
    else return the existing one.N(   R	   t   _screenR�   R=  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   �  s    R=  c           B   sp   e  Z d Z d Z e d  Z d �  Z e d e d e d e d d � Z d �  Z	 d �  Z
 d	 �  Z d
 �  Z RS(   R"   c         C   s�   t  j d  k rK t �  t  _ |  _ |  j j t  j � |  j j |  j � n  t  j d  k r� t	 d } t	 d } t	 d } t	 d } t	 d } t	 d } |  j j
 | | | | � |  j j �  t  _ t j |  t  j � |  j | | | | � n  d  S(   NRp   R�   R�   R�   R�   R�   (   R=  t   _rootR�   R3  R"   t   _titleRA  t   _destroyR  R�   R8  R9  R   R  R    (   R�   Rp   R�   R�   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  �  s    





Rp   R�   R�   R�   c      	   C   s  t  |  j d � s d S|  j j �  } |  j j �  } t | t � rl d | k oZ d k n rl | | } n  | d k r� | | d } n  t | t � r� d | k o� d k n r� | | } n  | d k r� | | d } n  |  j j | | | | � |  j �  d S(   s   Set the size and position of the main window.

        Arguments:
        width: as integer a size in pixels, as float a fraction of the screen.
          Default is 50% of screen.
        height: as integer the height in pixels, as float a fraction of the
          screen. Default is 75% of screen.
        startx: if positive, starting position in pixels from the left
          edge of the screen, if negative from the right edge
          Default, startx=None is to center window horizontally.
        starty: if positive, starting position in pixels from the top
          edge of the screen, if negative from the bottom edge
          Default, starty=None is to center window vertically.

        Examples (for a Screen instance named screen):
        >>> screen.setup (width=200, height=200, startx=0, starty=0)

        sets window to 200x200 pixels, in upper left of screen

        >>> screen.setup(width=.75, height=0.5, startx=None, starty=None)

        sets window to 75% of screen by 50% of screen and centers
        R=  Ni    i   i   (	   R�  R�  RC  RE  R�   R�   R�   R=  R%   (   R�   Rp   R�   R;  R<  Rp  t   sh(    (    s    C:\Python27\lib\lib-tk\turtle.pyR    �  s    ++c         C   s/   t  j d k	 r" t  j j | � n  | t  _ d S(   sq  Set title of turtle-window

        Argument:
        titlestring -- a string, to appear in the titlebar of the
                       turtle graphics window.

        This is a method of Screen-class. Not available for TurtleScreen-
        objects.

        Example (for a Screen instance named screen):
        >>> screen.title("Welcome to the turtle-zoo!")
        N(   R=  R�  R�   R"   R�  (   R�   t   titlestring(    (    s    C:\Python27\lib\lib-tk\turtle.pyR"   '  s    c         C   sV   |  j  } | t j  k r? d  t _ d  t _ d  t _  d  t _ n  t t _	 | j
 �  d  S(   N(   R�  R=  R�   R	   R�  R�  R  R�   R   R�  R@  (   R�   t   root(    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  8  s    					c         C   s   |  j  �  d S(   s~   Shut the turtlegraphics window.

        Example (for a TurtleScreen instance named screen):
        >>> screen.bye()
        N(   R�  (   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR   B  s    c            sW   �  f d �  } �  j  | � t d r* d Sy t �  Wn t k
 rR t d � n Xd S(   sl  Go into mainloop until the mouse is clicked.

        No arguments.

        Bind bye() method to mouseclick on TurtleScreen.
        If "using_IDLE" - value in configuration dictionary is False
        (default value), enter mainloop.
        If IDLE with -n switch (no subprocess) is used, this value should be
        set to True in turtle.cfg. In this case IDLE's mainloop
        is active also for the client script.

        This is a method of the Screen-class and not available for
        TurtleScreen instances.

        Example (for a Screen instance named screen):
        >>> screen.exitonclick()

        c            s   �  j  �  d S(   s&   Screen.bye() with two dummy-parametersN(   R   (   R�   R�   (   R�   (    s    C:\Python27\lib\lib-tk\turtle.pyt   exitGracefully]  s    R�   Ni    (   RJ   R�   Rv   t   AttributeErrort   exit(   R�   R�  (    (   R�   s    C:\Python27\lib\lib-tk\turtle.pyR   J  s    
N(   R�   R�   R�   R�  R  R�   R�  R  R    R"   R�  R   R   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR=  �  s   
	'		
	c           B   s8   e  Z d  Z d Z d Z e d e d e d d � Z RS(   s�   RawTurtle auto-creating (scrolled) canvas.

    When a Turtle object is created or a function derived from some
    Turtle method is called a TurtleScreen object is automatically created.
    Rc   R�   R�   c      	   C   sG   t  j d  k r t �  t  _ n  t j |  t  j d | d | d | �d  S(   NRc   R�   R�   (   R	   R�  R�   R   R   R  (   R�   Rc   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyR  r  s    N(   R�   R�   R�   R�   R�  R�  R�   R  (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyR	   i  s   c           C   s%   t  j d k r t  �  t  _ n  t  j S(   s5   Create the 'anonymous' turtle if not already present.N(   R	   R�  R�   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _getpen  s    c           C   s%   t  j d k r t �  t  _ n  t  j S(   s-   Create a TurtleScreen if not already present.N(   R	   R�  R�   R   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyt
   _getscreen�  s    t   turtle_docstringdictc         C   sR  i  } x+ t  D]# } d | } t | � j | | <q Wx+ t D]# } d | } t | � j | | <q; Wt d |  d � } t g  | j �  D]% } | j d � d t k r� | ^ q� � } | j	 d � x> | d  D]2 } | j	 d	 t
 | � � | j	 d
 | | � q� W| d } | j	 d	 t
 | � � | j	 d | | � | j	 d � | j �  d S(   s�  Create and write docstring-dictionary to file.

    Optional argument:
    filename -- a string, used as filename
                default value is turtle_docstringdict

    Has to be called explicitly, (not used by the turtle-graphics classes)
    The docstring dictionary will be written to the Python script <filname>.py
    It is intended to serve as a template for translation of the docstrings
    into different languages.
    s   _Screen.s   Turtle.s   %s.pyRP  R�   i   s   docsdict = {

i����s   %s :
s           """%s
""",

s           """%s
"""

s   }
N(   t   _tg_screen_functionsR�   R�   t   _tg_turtle_functionsR�   R�  R�   R   t   _alias_listRq   t   reprR�   (   R�   t   docsdictt
   methodnameR�   R�   R�   R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyRt   �  s&    

(
c         C   sn   d i |  j  �  d 6} t | � } | j } x; | D]3 } y | | t | � j _ Wq3 d | GHq3 Xq3 Wd S(   s�   Read in docstrings from lang-specific docstring dictionary.

    Transfer docstrings, translated to lang, from a dictionary-file
    to the methods of classes Screen and Turtle and - in revised form -
    to the corresponding functions.
    s!   turtle_docstringdict_%(language)sR�   s   Bad docstring-entry: %sN(   R�  t
   __import__R�  R�   t   im_funcR�   (   t   langt   modnamet   moduleR�  R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   read_docstrings�  s    	s   Cannot find docsdict fors;   Unknown Error when trying to import %s-docstring-dictionaryc   
      C   s�  d } } t  |  � t j k r1 |  j } d } n |  } d } t  | � t j t j g k r�yg| j j } t | j j	 | | !� } | j j	 | | !} | j
 p� g  } t t d �  | � � } d g t | � t | � | } t d �  | | � }	 | j j d @rF|	 j d | j j	 | � | j d | j j	 | � | d 7} n  | j j d @r�|	 j d	 | j j	 | � | j d	 | j j	 | � n  d
 j |	 � } d | } d
 j | � } d | } Wq�q�Xn  | | f S(   s9   Get strings describing the arguments for the given objectR�   i   i    c         S   s   d t  |  � S(   Ns   =%s(   R�  (   R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   <lambda>�  s    c         S   s   |  | S(   N(    (   R�  t   dflt(    (    s    C:\Python27\lib\lib-tk\turtle.pyR�  �  s    i   R   i   s   **s   , s   (%s)(   R�   R�   t
   MethodTypeR�  R�   t
   LambdaTypet	   func_codet   co_argcountR�   t   co_varnamest   func_defaultst   mapR�  t   co_flagsRU  R   (
   t   obt   argText1t   argText2t   fobt	   argOffsett   countert   items2t   realArgst   defaultst   items1(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   getmethparlist�  s:    
		!
c         C   se   d d l  } |  d k r d St d } |  j d | d � } | j d | � } | j d | � } | S(   s<   To reduce docstrings from RawTurtle class for functions
    i����NR�   s   %s.R�   s    \(.+ %s\):t   :(   t   reR�   R�   t   replacet   compilet   sub(   t   docstrR�  t
   turtlenamet	   newdocstrt   parexp(    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _turtle_docrevise�  s    
c         C   se   d d l  } |  d k r d St d } |  j d | d � } | j d | � } | j d | � } | S(   s?   To reduce docstrings from TurtleScreen class for functions
    i����NR�   s   %s.R�   s    \(.+ %s\):R�  (   R�  R�   R�   R�  R�  R�  (   R�  R�  t
   screennameR�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   _screen_docrevise�  s    
s   _Screen.R�   s   >>>>>>s6   def %(key)s%(pl1)s: return _getscreen().%(key)s%(pl2)sR�   t   pl1t   pl2s   Turtle.s3   def %(key)s%(pl1)s: return _getpen().%(key)s%(pl2)st   __main__c           C   s   t  �  r t �  n t �  d  S(   N(   RF   RU   RM   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyt	   switchpen$  s    	
c          C   s�  t  �  t t � t �  t d � t �  t d � x� t d � D]� }  |  d k r_ t d � n  x( t d � D] } t	 d � t
 d � ql W|  d k r� t d � t d	 � n  t �  t	 d
 � t �  q@ Wt d � t d � t t � t �  t d � t	 d � t d � t	 d � t d � t �  t d d � t d d � t d � x< t d � D]. }  t	 d � t
 d � t	 d � t d � qXWt t � t d � x< t d � D]. }  t	 d � t
 d � t	 d � t d � q�Wt d	 � d S(   s   Demo of old turtle.py - moduleid   i   i   i   i   i   iZ   t   marooni    i   R�   i�   t
   startstartRm  t   redi   N(   RX   R#   R�   Ro   R)   R6   Rp   R�  R:   R<   RH   R2   R�   RW   Rq   (   R�  R�   (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   demo1*  sX    






















c          C   sO  t  d � t �  t d � t t d d � � t d d � d }  t d � x( t d � D] } t �  t	 |  d � qX Wt
 d � x t �  r� t �  q� Wt �  t d � t d	 � d } t d
 � t d � t d � x� t d d � D]� } | d k rt �  t d	 d | d d | � n  x( t d � D] } t | � t d � q+W| d 7} t d � t  t  �  d d � q� Wt �  t d � t �  t d � t d � t �  t d d � t  d � t d � x? t d � D]1 } t	 d d � t d � t d � t d � q�Wt d � t d � t �  t d � t �  t d � t �  } | j d � t �  } | j d � | j d � | j �  | j d � | j  d � | j �  | j d d � | j d � | j  �  | j  d � | j d d � | j d � | j  d � t t | � � d } x� | j | � d k r�| j d � | j d  � | j | j | � � | j d � | d! d k r�| j! �  | j! �  t �  n  | d 7} q W| j
 d" d# d- d& d' �| j d( � | j d � d) �  } t" j# d � x! t �  r| j �  | j �  q�W| j d � | j
 d* d# d. �| j$ | d � d, S(/   s   Demo of some new features.i   i   i    g       @iZ   i   i
   s   wait a moment...i�   t   greeni�   i����i   i   ix   i   iF   i   R�  t   yellowi   i2   R�   R"  i  i(   i   t   bluet   orangei   g      @g333333�?i   s   CAUGHT! Ru  R�  t   boldRx  RW   R�   c         S   s   t  �  t �  d  S(   N(   R   R   (   R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   baba�  s    s     Click me!t   CourierN(   s   Ariali   s   bold(   R�  i   s   bold(%   Rf   Rg   RQ   R\   Rk   R4   RZ   R�  R�  R-   Rq   Rn   Rm   RX   RI   R   RO   R*   R;   R9   R7   RU   RM   R2   R:   Rc   R@   RY   R	   RH   Ro   RA   R6   Rh   t   timet   sleepRJ   (   R  R�   t   laengeR�  t   triR�   R�  R�  (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   demo2_  s�    






















		





	
(L   R�   t   _vert   TkinterR  R�   R�   R�  t   ost   os.pathR    R   R   t   copyR   t   _tg_classesR�  R�  t   _tg_utilitiest   _math_functionst   __all__R�  R�   R�   R�   R�   R�   R�   R�   R   R�   R�   R�   R�   R  R   R  R4  R3  t   objectRF  t	   ExceptionR�  R�  R   R�  R   R�  R  R9  R   R
   R   R=  R	   R   R�  R�  Rt   R�  t	   _LANGUAGEt   ImportErrorR�  R�  R�  R�  R�   R�  R�  t   defstrRv   Ru   R�   R�  R�  R�  R   (    (    (    s    C:\Python27\lib\lib-tk\turtle.pyt   <module>e   s  
	!

		%	4	
	c	� J	/&� � � � � �� � � � k	�		"	

	$		&&			5	b