# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyLocations
# Returns a list of mailing addresses, business addresses, and jurisdiction of incorporation associated with a given company.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCompanyLocations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCompanyLocations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCompanyLocations, self).__init__(temboo_session, '/Library/CorpWatch/Company/GetCompanyLocations')


    def new_input_set(self):
        return GetCompanyLocationsInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyLocationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyLocationsChoreographyExecution(session, exec_id, path)

class GetCompanyLocationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCompanyLocations
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        super(GetCompanyLocationsInputSet, self)._set_input('APIKey', value)
    def set_CWID(self, value):
        """
        Set the value of the CWID input for this Choreo. ((required, string) CoprWatch ID for the company. Format looks like: cw_8484.)
        """
        super(GetCompanyLocationsInputSet, self)._set_input('CWID', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        super(GetCompanyLocationsInputSet, self)._set_input('Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        super(GetCompanyLocationsInputSet, self)._set_input('Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        super(GetCompanyLocationsInputSet, self)._set_input('ResponseType', value)

class GetCompanyLocationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCompanyLocations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class GetCompanyLocationsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCompanyLocationsResultSet(response, path)
