# coding: utf-8

"""
InfluxDB OSS API Service.

The InfluxDB v2 API provides a programmatic interface for all interactions with InfluxDB. Access the InfluxDB API using the `/api/v2/` endpoint.   # noqa: E501

OpenAPI spec version: 2.0.0
Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from influxdb_client.service._base_service import _BaseService


class DeleteService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """DeleteService - a operation defined in OpenAPI."""
        super().__init__(api_client)

    def post_delete(self, delete_predicate_request, **kwargs):  # noqa: E501,D401,D403
        """Delete data.

        Deletes data from a bucket.  Use this endpoint to delete points from a bucket in a specified time range.  #### InfluxDB Cloud  - Does the following when you send a delete request:    1. Validates the request and queues the delete.   2. Returns _success_ if queued; _error_ otherwise.   3. Handles the delete asynchronously.  #### InfluxDB OSS  - Validates the request, handles the delete synchronously,   and then responds with success or failure.  #### Required permissions  - `write-buckets` or `write-bucket BUCKET_ID`.    `BUCKET_ID` is the ID of the destination bucket.  #### Rate limits (with InfluxDB Cloud)  `write` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Delete data](https://docs.influxdata.com/influxdb/v2.2/write-data/delete-data/). - Learn how to use [delete predicate syntax](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/delete-predicate/). - Learn how InfluxDB handles [deleted tags](https://docs.influxdata.com/flux/v0.x/stdlib/influxdata/influxdb/schema/measurementtagkeys/)   and [deleted fields](https://docs.influxdata.com/flux/v0.x/stdlib/influxdata/influxdb/schema/measurementfieldkeys/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_delete(delete_predicate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeletePredicateRequest delete_predicate_request: Time range parameters and an optional **delete predicate expression**.  To select points to delete within the specified time range, pass a **delete predicate expression** in the `predicate` property of the request body. If you don't pass a `predicate`, InfluxDB deletes all data with timestamps in the specified time range.  #### Related guides  - [Delete data](https://docs.influxdata.com/influxdb/v2.2/write-data/delete-data/). - Learn how to use [delete predicate syntax](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/delete-predicate/).  (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization to delete data from. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Deletes data from the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str bucket: The name or ID of the bucket to delete data from. If you pass both `bucket` and `bucketID`, `bucketID` takes precedence.
        :param str org_id: The ID of the organization to delete data from. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Deletes data from the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str bucket_id: The ID of the bucket to delete data from. If you pass both `bucket` and `bucketID`, `bucketID` takes precedence.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_delete_with_http_info(delete_predicate_request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_delete_with_http_info(delete_predicate_request, **kwargs)  # noqa: E501
            return data

    def post_delete_with_http_info(self, delete_predicate_request, **kwargs):  # noqa: E501,D401,D403
        """Delete data.

        Deletes data from a bucket.  Use this endpoint to delete points from a bucket in a specified time range.  #### InfluxDB Cloud  - Does the following when you send a delete request:    1. Validates the request and queues the delete.   2. Returns _success_ if queued; _error_ otherwise.   3. Handles the delete asynchronously.  #### InfluxDB OSS  - Validates the request, handles the delete synchronously,   and then responds with success or failure.  #### Required permissions  - `write-buckets` or `write-bucket BUCKET_ID`.    `BUCKET_ID` is the ID of the destination bucket.  #### Rate limits (with InfluxDB Cloud)  `write` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Delete data](https://docs.influxdata.com/influxdb/v2.2/write-data/delete-data/). - Learn how to use [delete predicate syntax](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/delete-predicate/). - Learn how InfluxDB handles [deleted tags](https://docs.influxdata.com/flux/v0.x/stdlib/influxdata/influxdb/schema/measurementtagkeys/)   and [deleted fields](https://docs.influxdata.com/flux/v0.x/stdlib/influxdata/influxdb/schema/measurementfieldkeys/).
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_delete_with_http_info(delete_predicate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeletePredicateRequest delete_predicate_request: Time range parameters and an optional **delete predicate expression**.  To select points to delete within the specified time range, pass a **delete predicate expression** in the `predicate` property of the request body. If you don't pass a `predicate`, InfluxDB deletes all data with timestamps in the specified time range.  #### Related guides  - [Delete data](https://docs.influxdata.com/influxdb/v2.2/write-data/delete-data/). - Learn how to use [delete predicate syntax](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/delete-predicate/).  (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization to delete data from. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Deletes data from the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str bucket: The name or ID of the bucket to delete data from. If you pass both `bucket` and `bucketID`, `bucketID` takes precedence.
        :param str org_id: The ID of the organization to delete data from. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Deletes data from the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str bucket_id: The ID of the bucket to delete data from. If you pass both `bucket` and `bucketID`, `bucketID` takes precedence.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_delete_prepare(delete_predicate_request, **kwargs)

        return self.api_client.call_api(
            '/api/v2/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    async def post_delete_async(self, delete_predicate_request, **kwargs):  # noqa: E501,D401,D403
        """Delete data.

        Deletes data from a bucket.  Use this endpoint to delete points from a bucket in a specified time range.  #### InfluxDB Cloud  - Does the following when you send a delete request:    1. Validates the request and queues the delete.   2. Returns _success_ if queued; _error_ otherwise.   3. Handles the delete asynchronously.  #### InfluxDB OSS  - Validates the request, handles the delete synchronously,   and then responds with success or failure.  #### Required permissions  - `write-buckets` or `write-bucket BUCKET_ID`.    `BUCKET_ID` is the ID of the destination bucket.  #### Rate limits (with InfluxDB Cloud)  `write` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Delete data](https://docs.influxdata.com/influxdb/v2.2/write-data/delete-data/). - Learn how to use [delete predicate syntax](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/delete-predicate/). - Learn how InfluxDB handles [deleted tags](https://docs.influxdata.com/flux/v0.x/stdlib/influxdata/influxdb/schema/measurementtagkeys/)   and [deleted fields](https://docs.influxdata.com/flux/v0.x/stdlib/influxdata/influxdb/schema/measurementfieldkeys/).
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param DeletePredicateRequest delete_predicate_request: Time range parameters and an optional **delete predicate expression**.  To select points to delete within the specified time range, pass a **delete predicate expression** in the `predicate` property of the request body. If you don't pass a `predicate`, InfluxDB deletes all data with timestamps in the specified time range.  #### Related guides  - [Delete data](https://docs.influxdata.com/influxdb/v2.2/write-data/delete-data/). - Learn how to use [delete predicate syntax](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/delete-predicate/).  (required)
        :param str zap_trace_span: OpenTracing span context
        :param str org: The organization to delete data from. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Deletes data from the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str bucket: The name or ID of the bucket to delete data from. If you pass both `bucket` and `bucketID`, `bucketID` takes precedence.
        :param str org_id: The ID of the organization to delete data from. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Deletes data from the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`.
        :param str bucket_id: The ID of the bucket to delete data from. If you pass both `bucket` and `bucketID`, `bucketID` takes precedence.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_delete_prepare(delete_predicate_request, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=[],
            files={},
            response_type=None,  # noqa: E501
            auth_settings=[],
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats={},
            urlopen_kw=kwargs.get('urlopen_kw', None))

    def _post_delete_prepare(self, delete_predicate_request, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['delete_predicate_request', 'zap_trace_span', 'org', 'bucket', 'org_id', 'bucket_id']  # noqa: E501
        self._check_operation_params('post_delete', all_params, local_var_params)
        # verify the required parameter 'delete_predicate_request' is set
        if ('delete_predicate_request' not in local_var_params or
                local_var_params['delete_predicate_request'] is None):
            raise ValueError("Missing the required parameter `delete_predicate_request` when calling `post_delete`")  # noqa: E501

        path_params = {}

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'bucket_id' in local_var_params:
            query_params.append(('bucketID', local_var_params['bucket_id']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        body_params = None
        if 'delete_predicate_request' in local_var_params:
            body_params = local_var_params['delete_predicate_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
