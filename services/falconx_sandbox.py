################################################################################################################
# CROWDSTRIKE FALCON COMPLETE                                                                                  #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# falconx_sandbox - Falcon X Sandbox API Interface Class                                                       #
################################################################################################################
import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class FalconX_Sandbox:
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """

    def __init__(self, access_token, base_url='https://api.crowdstrike.com'):
        """ Instantiates the base class, ingests the authorization token, 
            and initializes the headers and base_url global variables. 
        """
        self.headers = { 'Authorization': 'Bearer {}'.format(access_token) }
        self.base_url = base_url

    class Result:
        """ Subclass to handle parsing of result client output. """
        def __init__(self):
            """ Instantiates the subclass and initializes the result object. """
            self.result_obj = {}
            
        def __call__(self, status_code, headers, body):
            """ Formats values into a properly formatted result object. """
            self.result_obj['status_code'] = status_code
            self.result_obj['headers'] = dict(headers)
            self.result_obj['body'] = body
            
            return self.result_obj

    def GetArtifacts(self, parameters):#This function will probably need to not do a result.json() if used... See Swagger
        """ Download IOC packs, PCAP files, and other analysis artifacts. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetArtifacts
        FULL_URL = self.base_url+'/falconx/entities/artifacts/v1'
        HEADERS = copy.deepcopy(self.headers)
        HEADERS['Accept-Encoding'] = 'gzip'
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def GetSummaryReports(self, parameters):
        """ Get a short summary version of a sandbox report. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSummaryReports
        FULL_URL = self.base_url+'/falconx/entities/report-summaries/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def GetSubmissions(self, parameters):
        """ Check the status of a sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/GetSubmissions
        FULL_URL = self.base_url+'/falconx/entities/submissions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def Submit(self, body):
        """ Submit an uploaded file or a URL for sandbox analysis. Time required for analysis varies but is usually less than 15 minutes. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/Submit
        FULL_URL = self.base_url+'/falconx/entities/submissions/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def QueryReports(self, parameters):
        """ Find sandbox reports by providing an FQL filter and paging details. Returns a set of report IDs that match your criteria. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QueryReports
        FULL_URL = self.base_url+'/falconx/queries/reports/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def QuerySubmissions(self, parameters):
        """ Find submission IDs for uploaded files by providing an FQL filter and paging details. 
            Returns a set of submission IDs that match your criteria. 
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/QuerySubmissions
        FULL_URL = self.base_url+'/falconx/queries/submissions/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def UploadSampleV2(self, parameters, body):
        """ Upload a file for sandbox analysis. After uploading, use `/falconx/entities/submissions/v1` to start analyzing the file. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/falconx-sandbox/UploadSampleV2
        FULL_URL = self.base_url+'/samples/entities/samples/v2'
        HEADERS = self.headers
        BODY = body
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, params=PARAMS, data=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
