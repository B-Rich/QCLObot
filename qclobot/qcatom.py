#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2002-2014 The ProteinDF project
# see also AUTHORS and README.
#
# This file is part of ProteinDF.
#
# ProteinDF is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ProteinDF is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ProteinDF.  If not, see <http://www.gnu.org/licenses/>.

import logging

import pdfbridge as bridge
import pdfpytools as pdf

class QcAtom(bridge.Atom):
    def __init__(self, *args, **kwargs):
        super(QcAtom, self).__init__(*args, **kwargs)

        self._logger = logging.getLogger(__name__)
        if kwargs.get('debug'):
            self._logger.addHandler(logging.StreamHandler())
            self._logger.setLevel(logging.DEBUG)
        else:
            self._logger.addHandler(logging.NullHandler())
            self._logger.setLevel(logging.INFO)

        suffix = "." + self.symbol
        self.basisset = kwargs.get('basisset', 'O-DZVP2' + suffix)
        self.basisset_j = kwargs.get('basisset_j', 'A-DZVP2' + suffix)
        self.basisset_xc = kwargs.get('basisset_xc', 'A-DZVP2' + suffix)
        self.basisset_gridfree = kwargs.get('basisset_gridfree', 'O-DZVP2' + suffix)

        self._qc_parent = kwargs.get('qc_parent', None)

    # transform to bridge.Atom
    def get_Atom(self):
        atm = bridge.Atom(self)
        return atm
        
    #
    def get_number_of_AOs(self):
        basis2 = pdf.Basis2()
        bs = basis2.get_basisset(self.basisset)
        return bs.get_number_of_AOs()
        
    # basisset -------------------------------------------------------
    def _get_basisset(self):
        return self._basisset

    def _set_basisset(self, name):
        self._basisset = bridge.Utils.byte2str(name)

    basisset = property(_get_basisset, _set_basisset)

    # basisset_j ------------------------------------------------------
    def _get_basisset_j(self):
        return self._basisset_j

    def _set_basisset_j(self, name):
        self._basisset_j = bridge.Utils.byte2str(name)

    basisset_j = property(_get_basisset_j, _set_basisset_j)

    # basisset_xc -----------------------------------------------------
    def _get_basisset_xc(self):
        return self._basisset_xc

    def _set_basisset_xc(self, name):
        self._basisset_xc = bridge.Utils.byte2str(name)

    basisset_xc = property(_get_basisset_xc, _set_basisset_xc)

    # basisset_gridfree -----------------------------------------------
    def _get_basisset_gridfree(self):
        return self._basisset_gridfree

    def _set_basisset_gridfree(self, name):
        self._basisset_gridfree = bridge.Utils.byte2str(name)

    basisset_gridfree = property(_get_basisset_gridfree, _set_basisset_gridfree)

    # atom label ------------------------------------------------------
    def _get_atomlabel(self):
        symbol = self.symbol
        label = self.label
        kind = symbol
        if len(label) > 0:
            kind = '{}@{}'.format(symbol, label)
        return kind

    atomlabel = property(_get_atomlabel)



