SoundSwallower: an even smaller speech recognizer
-------------------------------------------------

"Time and change have a voice; eternity is silent. The human ear is
always searching for one or the other."
- Leena Krohn, *Datura, or a delusion we all see*

SoundSwallower is a refactored version of PocketSphinx.  The goal is
not to provide a fast implementation of large-vocabulary continuous
speech recognition, but rather to provide a *small* implementation of
simple, useful speech technologies.

With that in mind the current version is limited to finite-state
grammar recognition and force alignment.  It is also implemented in
Python, using NumPy for numeric computations.  A future version may be
reimplemented in JavaScript.

We have kept the CMU Sphinx features and models for the time being,
although this limits us to strictly GMM-based acoustic modeling.  In
the future we may support DNN acoustic models, but we are unlikely to
ever implement WFSTs or end-to-end neural networks.
