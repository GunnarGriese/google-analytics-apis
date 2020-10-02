# Automated Google Analytics Audits

## API Authentication

TBD

## To Do List

### Authentication

- [x] Enable simple OAuth flow

### Account Settings

- [x] List accounts, properties, views associated with the authenticated account
- [ ] Account permissions of authenticated user
- [ ] List of account level filters

### Property Settings

- [ ] List of referral exclusions
- [ ] Data Retention Settings
- [ ] List of linked Google Ads accounts (& other GMP products)
- [ ] List of available audiences
- [ ] Check if Advertising Features / Google Signals is enabled
- [ ] List of Custom Dimensions & Metrics
- [ ] List of Data Import files

### View Settings

- [ ] List of applied view filters
- [ ] Check if EEC is enabled
- [ ] Get Checkout Step Labeling
- [ ] Time Zone & CUrrency Settings
- [ ] List of Excluded URL parameters
- [ ] List of Query Parameters (enabling Site Search reports)
- [ ] Check if Query Parameters are stripped from page dimension
- [x] List of goals (& their configuration)
- [ ] Channel Grouping Settings

## Ressources

Check [GA Management API Reference](https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference) for all available functionality.
Check Python [examples from Google] (https://github.com/googleapis/google-api-python-client/blob/master/samples/analytics/management_v3_reference.py).
