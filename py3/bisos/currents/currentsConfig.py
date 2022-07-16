# -*- coding: utf-8 -*-

""" #+begin_org
* *[Summary]* :: A =CmndLib= for providing currents.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of Blee ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Libre-Halaal Foundation. Subject to AGPL.
** It is not part of Emacs. It is part of Blee.
** Best read and edited  with Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: NOTYET
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:python:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
icmInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['currentsConfig'], }
icmInfo['version'] = '202207114151'
icmInfo['status']  = 'inUse'
icmInfo['panel'] = 'currentsConfig-Panel.org'
icmInfo['groupingType'] = 'IcmGroupingType-pkged'
icmInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* /[[elisp:(org-cycle)][| Description |]]/ :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
Module description comes here.
** Relevant Panels:
** Status: In use with blee3
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:python:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=PyImports= " :itemTitle "*Py Library IMPORTS*"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmBleepG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__

from blee.icmPlayer import bleep
####+END:

import os
import collections
#import enum

import shutil

from bisos import bpf

####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "Obtain Package Bases"  :extraInfo ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *Obtain Package Bases:* |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:icm:python:func :funcName "configBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /configBaseDir_obtain/ retType=bool argsList=nil  [[elisp:(org-cycle)][| ]]
#+end_org """
def configBaseDir_obtain():
####+END:

    outcome =  bpf.subProc.WOpW(invedBy=None, log=0).bash(
        f"""usgBpos.sh -i usgBpos_usageEnvs_fullUse_bxoPath""")

    if outcome.isProblematic():
        icm.EH_badOutcome(outcome)
        return None

    retVal = outcome.stdout.rstrip('\n')

    return retVal


####+BEGIN: bx:icm:python:func :funcName "configUsgCursBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /configUsgCursBaseDir_obtain/ retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
#+end_org """
def configUsgCursBaseDir_obtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return os.path.abspath(os.path.join(configBaseDir, "control/currents"))


####+BEGIN: bx:icm:python:func :funcName "configUsgCursFpBaseDir_obtain" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /configUsgCursFpBaseDir_obtain/ retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
#+end_org """
def configUsgCursFpBaseDir_obtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return os.path.abspath(os.path.join(configBaseDir,"control/currents/fp"))



####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "File Parameters Obtain"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *File Parameters Obtain:* |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: bx:icm:python:func :funcName "bxoId_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /bxoId_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
#+end_org """
def bxoId_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/usgCurs/fp".format(configBaseDir)),
            parName="bxoId")
    )


####+BEGIN: bx:icm:python:func :funcName "sr_fpObtain" :comment "Configuration Parameter" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /sr_fpObtain/ =Configuration Parameter= retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
#+end_org """
def sr_fpObtain(
    configBaseDir,
):
####+END:
    if not configBaseDir:
        configBaseDir = configBaseDir_obtain()

    return(
        icm.FILE_ParamValueReadFrom(
            parRoot= os.path.abspath("{}/usgCurs/fp".format(configBaseDir)),
            parName="sr")
    )


####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "Common Command Parameter Specification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *Common Command Parameter Specification:* |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: bx:icm:python:func :funcName "commonParamsSpecify" :funcType "void" :retType "bool" :deco "" :argsList "icmParams"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-void     [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/ retType=bool argsList=(icmParams)  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
    icmParams,
):
####+END:

    icmParams.parDictAdd(
        parName='configBaseDir',
        parDescription="Root Of usgCurs/fp from which file parameters will be read",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--configBaseDir',
    )

    icmParams.parDictAdd(
        parName='bxoId',
        parDescription="BISOS Default UserName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--bxoId',
    )

    icmParams.parDictAdd(
        parName='sr',
        parDescription="BISOS Default GroupName",
        parDataType=None,
        parDefault=None,
        parChoices=["any"],
        parScope=icm.ICM_ParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--sr',
    )

####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "Common Command Examples Sections"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *Common Command Examples Sections:* |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: bx:icm:python:func :funcName "examples_usgCursParsFull" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "configBaseDir"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /examples_usgCursParsFull/ retType=bool argsList=(configBaseDir)  [[elisp:(org-cycle)][| ]]
#+end_org """
def examples_usgCursParsFull(
    configBaseDir,
):
####+END:
    """
** Auxiliary examples to be commonly used.
"""

    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity=verbosity,
                             comment='none', icmWrapper=None, icmName=None) # verbosity: 'little' 'basic' 'none'
    def execLineEx(cmndStr): icm.ex_gExecMenuItem(execLine=cmndStr)

    icm.cmndExampleMenuChapter(' =FP Values=  *usgCurs Clear InfoBase --- Deletes All FPs*')

    cmndName = "usgCursParsDelete" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsDelete" ; cmndArgs = "" ; cps=cpsInit(); menuItem(verbosity='none')

    cmndName = "usgCursParsDelete" ; cmndArgs = "anyName" ;
    cps = collections.OrderedDict() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='little')


    icm.cmndExampleMenuChapter(' =FP Values=  *usgCurs Get Parameters*')

    cmndName = "usgCursParsGet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsGet" ; cmndArgs = "" ; cps=cpsInit(); menuItem(verbosity='none')

    icm.cmndExampleMenuChapter(' =FP Values=  *UsgCurs Defaults ParsSet  --*')

    cmndName = "usgCursParsDefaultsSet" ; cmndArgs = "bxoPolicy /" ;
    cpsInit(); menuItem('none')

    cmndName = "usgCursParsDefaultsSet" ; cmndArgs = "bxoPolicy /tmp" ;
    cpsInit(); menuItem('none')

    icm.cmndExampleMenuChapter(' =FP Values=  *UsgCurs ParsSet -- Set Parameters Explicitly*')

    cmndName = "usgCursParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['bxoId'] = "mcm"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['bxoId'] = "ea-59043"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['sr'] = "marme/dsnProc"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsSet" ; cmndArgs = "" ;
    cps = collections.OrderedDict() ;  cps['sr'] = "apache2/plone3"
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    # cmndName = "usgCursParsSet" ; cmndArgs = "" ;
    # cps = collections.OrderedDict() ;  cps['configBaseDir'] = configBaseDir ; cps['platformControlBaseDir'] = "${HOME}/bisosControl"
    # icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsSet" ; cmndArgs = "anyName=anyValue" ;
    cps = collections.OrderedDict() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, verbosity='little')

    cmndName = "usgCursParsSet" ; cmndArgs = "anyName=anyValue" ;
    cps = collections.OrderedDict() ;
    icm.ex_gCmndMenuItem(cmndName, cps, cmndArgs, icmWrapper="echo", verbosity='little')


####+BEGIN: blee:bxPanel:foldingSection :outLevel 1 :title "File Parameters Get/Set -- Commands"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*       [[elisp:(outline-show-subtree+toggle)][| *File Parameters Get/Set -- Commands:* |]]    [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: bx:icm:python:func :funcName "FP_readTreeAtBaseDir_CmndOutput" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "interactive fpBaseDir cmndOutcome"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /FP_readTreeAtBaseDir_CmndOutput/ retType=bool argsList=(interactive fpBaseDir cmndOutcome)  [[elisp:(org-cycle)][| ]]
#+end_org """
def FP_readTreeAtBaseDir_CmndOutput(
    interactive,
    fpBaseDir,
    cmndOutcome,
):
####+END:
    """Invokes FP_readTreeAtBaseDir.cmnd as interactive-output only."""
    #
    # Interactive-Output + Chained-Outcome Command Invokation
    #
    FP_readTreeAtBaseDir = icm.FP_readTreeAtBaseDir()
    FP_readTreeAtBaseDir.cmndLineInputOverRide = True
    FP_readTreeAtBaseDir.cmndOutcome = cmndOutcome

    return FP_readTreeAtBaseDir.cmnd(
        interactive=interactive,
        FPsDir=fpBaseDir,
    )

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "usgCursParsDelete" :comment "" :parsMand "" :parsOpt "configBaseDir" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] /usgCursParsDelete/ parsMand= parsOpt=configBaseDir argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class usgCursParsDelete(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'configBaseDir': configBaseDir, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Remove The entire infoBaseDir
        #+end_org """)

        if not configBaseDir:
            configBaseDir = configUsgCursFpBaseDir_obtain(None)

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        if len(cmndArgs) == 0:
            try:
                shutil.rmtree(configBaseDir)
            except OSError as e:
                print(f"Error: {configBaseDir} : {e.strerror}")
            bpf.dir.createIfNotThere(configBaseDir)

        else:
            for each in cmndArgs:
                parNameFullPath = os.path.join(
                        configBaseDir,
                        each
                )
                try:
                    shutil.rmtree(parNameFullPath)
                except OSError as e:
                    print(f"Error: {parNameFullPath} : {e.strerror}")


        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of parNames"
        )

        return cmndArgsSpecDict

####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "usgCursParsGetK1" :comment "" :parsMand "" :parsOpt "configBaseDir" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] /usgCursParsGetK1/ parsMand= parsOpt=configBaseDir argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class usgCursParsGetK1(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'configBaseDir': configBaseDir, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  it reads from ../usgCurs/fp.
        #+end_org """)

        if not configBaseDir:
            configBaseDir = configUsgCursFpBaseDir_obtain(None)

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        if len(cmndArgs) == 0:
            FP_readTreeAtBaseDir_CmndOutput(
                interactive=interactive,
                fpBaseDir=configBaseDir,
                cmndOutcome=cmndOutcome,
            )
            print(f"{cmndOutcome.results}")
            for eachFpName in cmndOutcome.results:
                eachFpValue = cmndOutcome.results[eachFpName].parValueGet()
                print(f"{eachFpName} {eachFpValue}")
        else:
            for each in cmndArgs:
                parNameFullPath = os.path.join(
                        configBaseDir,
                        each
                )
                parValue = icm.FILE_ParamValueReadFromPath(parNameFullPath)

                if interactive:
                    #icm.ANN_here("usgCursParsGet: {parValue} at {parNameFullPath}".
                    #     format(parValue=parValue, parNameFullPath=parNameFullPath))
                    print(f"{each}={parValue}")

        return cmndOutcome


####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "usgCursParsGet" :comment "" :parsMand "" :parsOpt "configBaseDir" :argsMin "0" :argsMax "9999" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] /usgCursParsGet/ parsMand= parsOpt=configBaseDir argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class usgCursParsGet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'configBaseDir': configBaseDir, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  it reads from ../usgCurs/fp.
        #+end_org """)

        if not configBaseDir:
            configBaseDir = configUsgCursFpBaseDir_obtain(None)

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        FP_readTreeAtBaseDir_CmndOutput(
            interactive=False,
            fpBaseDir=configBaseDir,
            cmndOutcome=cmndOutcome,
        )

        results = cmndOutcome.results

        if len(cmndArgs) == 0:
            for eachFpName in results:
                eachFpValue = results[eachFpName].parValueGet()
                print(f"{eachFpName} {eachFpValue}")
        else:
            for each in cmndArgs:
                eachFpValue = results[each].parValueGet()
                print(f"{each} {eachFpValue}")

        return cmndOutcome

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of parNames"
        )

        return cmndArgsSpecDict




####+BEGIN: bx:icm:python:cmnd:classHead :cmndName "usgCursParsSet" :comment "" :parsMand "" :parsOpt "configBaseDir bxoId sr" :argsMin "0" :argsMax "1000" :asFunc "" :interactiveP ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc    [[elisp:(outline-show-subtree+toggle)][||]] /usgCursParsSet/ parsMand= parsOpt=configBaseDir bxoId sr argsMin=0 argsMax=1000 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
#+end_org """
class usgCursParsSet(icm.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'configBaseDir', 'bxoId', 'sr', ]
    cmndArgsLen = {'Min': 0, 'Max': 1000,}

    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        configBaseDir=None,         # or Cmnd-Input
        bxoId=None,         # or Cmnd-Input
        sr=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ) -> icm.OpOutcome:
        cmndOutcome = self.getOpOutcome()
        if interactive:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs  # type: ignore
        else:
            effectiveArgsList = argsList

        callParamsDict = {'configBaseDir': configBaseDir, 'bxoId': bxoId, 'sr': sr, }
        if not icm.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        configBaseDir = callParamsDict['configBaseDir']
        bxoId = callParamsDict['bxoId']
        sr = callParamsDict['sr']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Args are in the form of a list of varName=varValue. Well known pars can also be set.
=configBaseDir= defaults to ~configBaseDir_obtain()~
        #+end_org """)

        if not configBaseDir:
            configBaseDir = configBaseDir_obtain()

        cmndArgs = self.cmndArgsGet("0&-1", cmndArgsSpecDict, effectiveArgsList)

        parNameFullPath = ""

        def createPathAndFpWrite(
                fpPath,
                valuePath,
        ):
            valuePath = os.path.abspath(valuePath)
            try:
                os.makedirs(valuePath)
            except OSError:
                if not os.path.isdir(valuePath):
                    raise

            icm.FILE_ParamWriteToPath(
                parNameFullPath=fpPath,
                parValue=valuePath,
            )
            parNameFullPath = fpPath


        # Any number of Name=Value can be passed as args
        for each in cmndArgs:
            varNameValue = each.split('=')
            parNameFullPath = os.path.join(
                    configUsgCursFpBaseDir_obtain(configBaseDir=configBaseDir),
                    varNameValue[0],
            )
            icm.FILE_ParamWriteToPath(
                parNameFullPath=parNameFullPath,

                parValue=varNameValue[1],
            )


        if bxoId:
             parNameFullPath = icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(
                    configUsgCursFpBaseDir_obtain(configBaseDir=configBaseDir),
                    "bxoId",
                ),
                parValue=bxoId,
            )

        if sr:
             parNameFullPath = icm.FILE_ParamWriteToPath(
                parNameFullPath=os.path.join(configUsgCursFpBaseDir_obtain(configBaseDir=configBaseDir),
                             "sr",
                ),
                parValue=sr,
            )

        if interactive:
            parValue = icm.FILE_ParamValueReadFromPath(parNameFullPath)
            icm.ANN_here("usgCursParsSet: {parValue} at {parNameFullPath}".
                         format(parValue=parValue, parNameFullPath=parNameFullPath))


        return cmndOutcome.set(
            opError=icm.OpError.Success,
            opResults=True,
        )

####+BEGIN: bx:icm:python:method :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
    @icm.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = icm.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="cmndArgs",
            argDefault=None,
            argChoices='any',
            argDescription="A sequence of varName=varValue"
        )

        return cmndArgsSpecDict

####+BEGIN: b:prog:file/endOfFile :extraParams nil
""" #+begin_org
* *[[elisp:(org-cycle)][| END-OF-FILE |]]* :: emacs and org variables and control parameters
#+end_org """
### local variables:
### no-byte-compile: t
### end:
####+END:
