# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class StatementSubject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, semantic_group: str=None):  # noqa: E501
        """StatementSubject - a model defined in Swagger

        :param id: The id of this StatementSubject.  # noqa: E501
        :type id: str
        :param name: The name of this StatementSubject.  # noqa: E501
        :type name: str
        :param semantic_group: The semantic_group of this StatementSubject.  # noqa: E501
        :type semantic_group: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'semantic_group': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'semantic_group': 'semanticGroup'
        }

        self._id = id
        self._name = name
        self._semantic_group = semantic_group

    @classmethod
    def from_dict(cls, dikt) -> 'StatementSubject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatementSubject of this StatementSubject.  # noqa: E501
        :rtype: StatementSubject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this StatementSubject.

        CURIE-encoded identifier of concept   # noqa: E501

        :return: The id of this StatementSubject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this StatementSubject.

        CURIE-encoded identifier of concept   # noqa: E501

        :param id: The id of this StatementSubject.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this StatementSubject.

        human readable label of subject concept  # noqa: E501

        :return: The name of this StatementSubject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this StatementSubject.

        human readable label of subject concept  # noqa: E501

        :param name: The name of this StatementSubject.
        :type name: str
        """

        self._name = name

    @property
    def semantic_group(self) -> str:
        """Gets the semantic_group of this StatementSubject.

        a semantic group for the subject concept (specified as a code CHEM, GENE, etc. - see [Semantic Groups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)   # noqa: E501

        :return: The semantic_group of this StatementSubject.
        :rtype: str
        """
        return self._semantic_group

    @semantic_group.setter
    def semantic_group(self, semantic_group: str):
        """Sets the semantic_group of this StatementSubject.

        a semantic group for the subject concept (specified as a code CHEM, GENE, etc. - see [Semantic Groups](https://metamap.nlm.nih.gov/Docs/SemGroups_2013.txt) for the full list of codes)   # noqa: E501

        :param semantic_group: The semantic_group of this StatementSubject.
        :type semantic_group: str
        """

        self._semantic_group = semantic_group