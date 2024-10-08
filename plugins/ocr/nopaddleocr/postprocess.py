

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import copy

__all__ = ["build_post_process"]

from .db_postprocess import DBPostProcess
from .rec_postprocess import CTCLabelDecode



def build_post_process(config, global_config=None):
    support_dict = [
        "DBPostProcess",
        "EASTPostProcess",
        "SASTPostProcess",
        "FCEPostProcess",
        "CTCLabelDecode",
        "AttnLabelDecode",
        "ClsPostProcess",
        "SRNLabelDecode",
        "PGPostProcess",
        "DistillationCTCLabelDecode",
        "TableLabelDecode",
        "DistillationDBPostProcess",
        "NRTRLabelDecode",
        "SARLabelDecode",
        "SEEDLabelDecode",
        "VQASerTokenLayoutLMPostProcess",
        "VQAReTokenLayoutLMPostProcess",
        "PRENLabelDecode",
        "DistillationSARLabelDecode",
        "ViTSTRLabelDecode",
        "ABINetLabelDecode",
        "TableMasterLabelDecode",
        "SPINLabelDecode",
        "DistillationSerPostProcess",
        "DistillationRePostProcess",
        "VLLabelDecode",
        "PicoDetPostProcess",
        "CTPostProcess",
        "RFLLabelDecode",
        "DRRGPostprocess",
        "CANLabelDecode",
        "SATRNLabelDecode",
        "ParseQLabelDecode",
        "CPPDLabelDecode",
        "LaTeXOCRDecode",
    ]

    config = copy.deepcopy(config)
    module_name = config.pop("name")
    if module_name == "None":
        return
    if global_config is not None:
        config.update(global_config)
    assert module_name in support_dict, Exception(
        "post process only support {}".format(support_dict)
    )
    module_class = eval(module_name)(**config)
    return module_class
