# -*- coding: utf-8 -*-

###############################################################################
#
# UserIsFollowedBy
# Retrieve the list of users following the authenticating user.
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

class UserIsFollowedBy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserIsFollowedBy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UserIsFollowedBy, self).__init__(temboo_session, '/Library/Instagram/UserIsFollowedBy')


    def new_input_set(self):
        return UserIsFollowedByInputSet()

    def _make_result_set(self, result, path):
        return UserIsFollowedByResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserIsFollowedByChoreographyExecution(session, exec_id, path)

class UserIsFollowedByInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserIsFollowedBy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(UserIsFollowedByInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        super(UserIsFollowedByInputSet, self)._set_input('ClientID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user associated with the list to return. Defaults to 'self' indicating that the authenticating user is assumed.)
        """
        super(UserIsFollowedByInputSet, self)._set_input('UserID', value)

class UserIsFollowedByResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserIsFollowedBy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class UserIsFollowedByChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UserIsFollowedByResultSet(response, path)
