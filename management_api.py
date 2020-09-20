import oauth

class Filter:
    def __init__(self, f_id,f_name, f_type, f_update, f_details=None, f_rank=None):
        self.id = f_id
        self.name = f_name
        self.type = f_type
        self.update = f_update
        self.details = f_details
        self.rank = f_rank

class AnalyticsManagement:
    API_VER = 'v3'
    API_NAME = 'analytics'

    def __init__(self, account_id=None, property_id=None, view_id=None, creds=creds):
        credentials = creds
        self.analytics = googleapiclient.discovery.build(self.API_NAME, self.API_VER, credentials=credentials)
        self.account_id = account_id
        self.property_id = property_id
        self.view_id = view_id

    def list_accounts(self):
        """returns a list of management.accountSummaries Resource"""
        accounts = self.analytics.management().accounts().list().execute()
        return accounts.get('items', [])

    def list_account_users(self):
        users = self.analytics.management().accountUserLinks().list(accountId=self.account_id).execute()
        return users.get('items', [])

    def list_account_filters(self):
        filters = self.analytics.management().filters().list(accountId=self.account_id).execute() 
        return filters.get('items', [])

    def get_property(self):
        """per default pre-defined property is returned"""
        prop = self.analytics.management().webproperties().get(
            accountId=self.account_id,
            webPropertyId=self.property_id).execute()
        return prop

    def list_view_filters(self):
        """per default view filters for pre-defined property and view are returned"""
        response = self.analytics.management().profileFilterLinks().list(
            accountId=self.account_id,
            webPropertyId=self.property_id,
            profileId=self.view_id).execute()
        view_filters = response.get('items', [])
        view_filter_list = []
        for filter_obj in view_filters:
            filter_id = filter_obj['id'].split(':')[1]
            rank = filter_obj['rank']
            view_filter_list.append({'id': filter_id, 'rank': rank})
        
        return view_filter_list

    def handle_filters(self):
        account_filters = self.list_account_filters()
        filter_dict = []
        for filter in account_filters:
            filter_ins = Filter(f_id=filter['id'], f_name=filter['name'], f_type=filter['type'], f_update=filter['updated'])
            if filter['type'] == "SEARCH_AND_REPLACE":
                filter_ins.details = filter['searchAndReplaceDetails']
            elif filter['type'] == "INCLUDE":
                filter_ins.details = filter["includeDetails"]
            elif filter['type'] == "EXCLUDE":
                filter_ins.details = filter["excludeDetails"]
            elif filter['type'] == "LOWERCASE":
                filter_ins.details = filter["lowercaseDetails"]
            elif filter['type'] == "UPPERCASE":
                filter_ins.details = filter["uppercaseDetails"]
            elif filter['type'] == "ADVANCED":
                filter_ins.details = filter["advancedDetails"]
            else:
                filter_ins.details = {'key': 'value'}
            filter_dict.append(filter_ins)

        return filter_dict