import abc
import logging

import six

logger = logging.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class CaseMapper(object):
    def describe_testrail_case(self, case):
        return {
            k: v
            for k, v in case.data.items() if isinstance(v, six.string_types)
        }


class TemplateCaseMapper(CaseMapper):
    """Template string based mapper."""
    def __init__(self, xunit_name_template, testrail_name_template, **kwargs):
        super(TemplateCaseMapper, self).__init__(**kwargs)
        self.xunit_name_template = xunit_name_template
        self.testrail_name_template = testrail_name_template
