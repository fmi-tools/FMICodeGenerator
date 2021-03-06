#!/usr/bin/python
# -*- coding: utf-8 -*-

# Implementation of the final generation page wizard page.
#
#
# This file is part of FMICodeGenerator (https://github.com/ghorwin/FMICodeGenerator)
#
# BSD 3-Clause License
#
# Copyright (c) 2018, Andreas Nicolai
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import platform

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont

from Ui_WizardPageGenerate import Ui_WizardPageGenerate

class WizardPageGenerate(QWidget):
	def __init__(self):
		super(WizardPageGenerate, self).__init__()
		self.ui = Ui_WizardPageGenerate()
		self.ui.setupUi(self)

		# customize font of log window
		f = QFont()
		if platform.system() == 'Windows':
			f.setFamily("Courier New")
			f.setPointSize(9)
		elif platform.system() == 'Darwin':
			f.setFamily("Monaco")
			f.setPointSize(12)
		else:
			f.setFamily("monospace");
			f.setPointSize(9);
		self.ui.plainTextEditLog.setFont(f)

		self.show()
