# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUsername
# Update an account username.
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

class UpdateUsername(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUsername Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateUsername, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Profile/UpdateUsername')


    def new_input_set(self):
        return UpdateUsernameInputSet()

    def _make_result_set(self, result, path):
        return UpdateUsernameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUsernameChoreographyExecution(session, exec_id, path)

class UpdateUsernameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUsername
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(UpdateUsernameInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(UpdateUsernameInputSet, self)._set_input('APIUser', value)
    def set_NewUsername(self, value):
        """
        Set the value of the NewUsername input for this Choreo. ((required, string) The new username, to be used for authenticating on the SendGrid SMTP servers and website. Must not exceed 100 characters. The username cannot be already taken or contain the SendGrid.com domain)
        """
        super(UpdateUsernameInputSet, self)._set_input('NewUsername', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(UpdateUsernameInputSet, self)._set_input('ResponseFormat', value)


class UpdateUsernameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUsername Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class UpdateUsernameChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateUsernameResultSet(response, path)
