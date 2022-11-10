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


class WriteService(_BaseService):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):  # noqa: E501,D401,D403
        """WriteService - a operation defined in OpenAPI."""
        super().__init__(api_client)

    def post_write(self, org, bucket, body, **kwargs):  # noqa: E501,D401,D403
        """Write data.

        Writes data to a bucket.  Use this endpoint to send data in [line protocol](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/line-protocol/) format to InfluxDB.  #### InfluxDB Cloud  - Takes the following steps when you send a write request:    1. Validates the request and queues the write.   2. If the write is queued, responds with an HTTP `204` status code.   3. Handles the write asynchronously and reaches eventual consistency.    An HTTP `2xx` status code acknowledges that the write or delete is queued.   To ensure that InfluxDB Cloud handles writes and deletes in the order you request them,   wait for a response before you send the next request.    Because writes are asynchronous, data might not yet be written   when you receive the response.  #### InfluxDB OSS  - Validates the request, handles the write synchronously,   and then responds with success or failure. - If all points were written successfully, returns `204`,   otherwise returns the first line that failed.  #### Required permissions  - `write-buckets` or `write-bucket BUCKET_ID`.    `BUCKET_ID` is the ID of the destination bucket.  #### Rate limits (with InfluxDB Cloud)  `write` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Write data with the InfluxDB API](https://docs.influxdata.com/influxdb/v2.2/write-data/developer-tools/api). - [Optimize writes to InfluxDB](https://docs.influxdata.com/influxdb/v2.2/write-data/best-practices/optimize-writes/). - [Troubleshoot issues writing data](https://docs.influxdata.com/influxdb/v2.2/write-data/troubleshoot/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_write(org, bucket, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: The destination organization for writes. InfluxDB writes all points in the batch to this organization. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Writes to the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`. - InfluxDB writes all points in the batch to this organization. (required)
        :param str bucket: The destination bucket for writes. InfluxDB writes all points in the batch to this bucket. (required)
        :param str body: Data in line protocol format.  To send compressed data, do the following:    1. Use [GZIP](https://www.gzip.org/) to compress the line protocol data.   2. In your request, send the compressed data and the      `Content-Encoding: gzip` header.  #### Related guides  - [Best practices for optimizing writes](https://docs.influxdata.com/influxdb/v2.2/write-data/best-practices/optimize-writes/).  (required)
        :param str zap_trace_span: OpenTracing span context
        :param str content_encoding: The compression applied to the line protocol in the request payload. To send a GZIP payload, pass `Content-Encoding: gzip` header.
        :param str content_type: The format of the data in the request body. To send a line protocol payload, pass `Content-Type: text/plain; charset=utf-8`.
        :param int content_length: The size of the entity-body, in bytes, sent to InfluxDB. If the length is greater than the `max body` configuration option, the server responds with status code `413`.
        :param str accept: The content type that the client can understand. Writes only return a response body if they fail--for example, due to a formatting problem or quota limit.  #### InfluxDB Cloud    - Returns only `application/json` for format and limit errors.   - Returns only `text/html` for some quota limit errors.  #### InfluxDB OSS    - Returns only `application/json` for format and limit errors.  #### Related guides   - [Troubleshoot issues writing data](https://docs.influxdata.com/influxdb/v2.2/write-data/troubleshoot/).
        :param str org_id: The ID of the destination organization for writes. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Writes to the bucket in the organization associated with the authorization (API token).   #### InfluxDB OSS  - Requires either `org` or `orgID`. - InfluxDB writes all points in the batch to this organization.
        :param WritePrecision precision: The precision for unix timestamps in the line protocol batch.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_write_with_http_info(org, bucket, body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_write_with_http_info(org, bucket, body, **kwargs)  # noqa: E501
            return data

    def post_write_with_http_info(self, org, bucket, body, **kwargs):  # noqa: E501,D401,D403
        """Write data.

        Writes data to a bucket.  Use this endpoint to send data in [line protocol](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/line-protocol/) format to InfluxDB.  #### InfluxDB Cloud  - Takes the following steps when you send a write request:    1. Validates the request and queues the write.   2. If the write is queued, responds with an HTTP `204` status code.   3. Handles the write asynchronously and reaches eventual consistency.    An HTTP `2xx` status code acknowledges that the write or delete is queued.   To ensure that InfluxDB Cloud handles writes and deletes in the order you request them,   wait for a response before you send the next request.    Because writes are asynchronous, data might not yet be written   when you receive the response.  #### InfluxDB OSS  - Validates the request, handles the write synchronously,   and then responds with success or failure. - If all points were written successfully, returns `204`,   otherwise returns the first line that failed.  #### Required permissions  - `write-buckets` or `write-bucket BUCKET_ID`.    `BUCKET_ID` is the ID of the destination bucket.  #### Rate limits (with InfluxDB Cloud)  `write` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Write data with the InfluxDB API](https://docs.influxdata.com/influxdb/v2.2/write-data/developer-tools/api). - [Optimize writes to InfluxDB](https://docs.influxdata.com/influxdb/v2.2/write-data/best-practices/optimize-writes/). - [Troubleshoot issues writing data](https://docs.influxdata.com/influxdb/v2.2/write-data/troubleshoot/)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_write_with_http_info(org, bucket, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: The destination organization for writes. InfluxDB writes all points in the batch to this organization. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Writes to the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`. - InfluxDB writes all points in the batch to this organization. (required)
        :param str bucket: The destination bucket for writes. InfluxDB writes all points in the batch to this bucket. (required)
        :param str body: Data in line protocol format.  To send compressed data, do the following:    1. Use [GZIP](https://www.gzip.org/) to compress the line protocol data.   2. In your request, send the compressed data and the      `Content-Encoding: gzip` header.  #### Related guides  - [Best practices for optimizing writes](https://docs.influxdata.com/influxdb/v2.2/write-data/best-practices/optimize-writes/).  (required)
        :param str zap_trace_span: OpenTracing span context
        :param str content_encoding: The compression applied to the line protocol in the request payload. To send a GZIP payload, pass `Content-Encoding: gzip` header.
        :param str content_type: The format of the data in the request body. To send a line protocol payload, pass `Content-Type: text/plain; charset=utf-8`.
        :param int content_length: The size of the entity-body, in bytes, sent to InfluxDB. If the length is greater than the `max body` configuration option, the server responds with status code `413`.
        :param str accept: The content type that the client can understand. Writes only return a response body if they fail--for example, due to a formatting problem or quota limit.  #### InfluxDB Cloud    - Returns only `application/json` for format and limit errors.   - Returns only `text/html` for some quota limit errors.  #### InfluxDB OSS    - Returns only `application/json` for format and limit errors.  #### Related guides   - [Troubleshoot issues writing data](https://docs.influxdata.com/influxdb/v2.2/write-data/troubleshoot/).
        :param str org_id: The ID of the destination organization for writes. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Writes to the bucket in the organization associated with the authorization (API token).   #### InfluxDB OSS  - Requires either `org` or `orgID`. - InfluxDB writes all points in the batch to this organization.
        :param WritePrecision precision: The precision for unix timestamps in the line protocol batch.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_write_prepare(org, bucket, body, **kwargs)

        return self.api_client.call_api(
            '/api/v2/write', 'POST',
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

    async def post_write_async(self, org, bucket, body, **kwargs):  # noqa: E501,D401,D403
        """Write data.

        Writes data to a bucket.  Use this endpoint to send data in [line protocol](https://docs.influxdata.com/influxdb/v2.2/reference/syntax/line-protocol/) format to InfluxDB.  #### InfluxDB Cloud  - Takes the following steps when you send a write request:    1. Validates the request and queues the write.   2. If the write is queued, responds with an HTTP `204` status code.   3. Handles the write asynchronously and reaches eventual consistency.    An HTTP `2xx` status code acknowledges that the write or delete is queued.   To ensure that InfluxDB Cloud handles writes and deletes in the order you request them,   wait for a response before you send the next request.    Because writes are asynchronous, data might not yet be written   when you receive the response.  #### InfluxDB OSS  - Validates the request, handles the write synchronously,   and then responds with success or failure. - If all points were written successfully, returns `204`,   otherwise returns the first line that failed.  #### Required permissions  - `write-buckets` or `write-bucket BUCKET_ID`.    `BUCKET_ID` is the ID of the destination bucket.  #### Rate limits (with InfluxDB Cloud)  `write` rate limits apply. For more information, see [limits and adjustable quotas](https://docs.influxdata.com/influxdb/cloud/account-management/limits/).  #### Related guides  - [Write data with the InfluxDB API](https://docs.influxdata.com/influxdb/v2.2/write-data/developer-tools/api). - [Optimize writes to InfluxDB](https://docs.influxdata.com/influxdb/v2.2/write-data/best-practices/optimize-writes/). - [Troubleshoot issues writing data](https://docs.influxdata.com/influxdb/v2.2/write-data/troubleshoot/)
        This method makes an asynchronous HTTP request.

        :param async_req bool
        :param str org: The destination organization for writes. InfluxDB writes all points in the batch to this organization. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Writes to the bucket in the organization associated with the authorization (API token).  #### InfluxDB OSS  - Requires either `org` or `orgID`. - InfluxDB writes all points in the batch to this organization. (required)
        :param str bucket: The destination bucket for writes. InfluxDB writes all points in the batch to this bucket. (required)
        :param str body: Data in line protocol format.  To send compressed data, do the following:    1. Use [GZIP](https://www.gzip.org/) to compress the line protocol data.   2. In your request, send the compressed data and the      `Content-Encoding: gzip` header.  #### Related guides  - [Best practices for optimizing writes](https://docs.influxdata.com/influxdb/v2.2/write-data/best-practices/optimize-writes/).  (required)
        :param str zap_trace_span: OpenTracing span context
        :param str content_encoding: The compression applied to the line protocol in the request payload. To send a GZIP payload, pass `Content-Encoding: gzip` header.
        :param str content_type: The format of the data in the request body. To send a line protocol payload, pass `Content-Type: text/plain; charset=utf-8`.
        :param int content_length: The size of the entity-body, in bytes, sent to InfluxDB. If the length is greater than the `max body` configuration option, the server responds with status code `413`.
        :param str accept: The content type that the client can understand. Writes only return a response body if they fail--for example, due to a formatting problem or quota limit.  #### InfluxDB Cloud    - Returns only `application/json` for format and limit errors.   - Returns only `text/html` for some quota limit errors.  #### InfluxDB OSS    - Returns only `application/json` for format and limit errors.  #### Related guides   - [Troubleshoot issues writing data](https://docs.influxdata.com/influxdb/v2.2/write-data/troubleshoot/).
        :param str org_id: The ID of the destination organization for writes. If you pass both `orgID` and `org`, they must both be valid.  #### InfluxDB Cloud  - Doesn't require `org` or `orgID`. - Writes to the bucket in the organization associated with the authorization (API token).   #### InfluxDB OSS  - Requires either `org` or `orgID`. - InfluxDB writes all points in the batch to this organization.
        :param WritePrecision precision: The precision for unix timestamps in the line protocol batch.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """  # noqa: E501
        local_var_params, path_params, query_params, header_params, body_params = \
            self._post_write_prepare(org, bucket, body, **kwargs)

        return await self.api_client.call_api(
            '/api/v2/write', 'POST',
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

    def _post_write_prepare(self, org, bucket, body, **kwargs):  # noqa: E501,D401,D403
        local_var_params = locals()

        all_params = ['org', 'bucket', 'body', 'zap_trace_span', 'content_encoding', 'content_type', 'content_length', 'accept', 'org_id', 'precision']  # noqa: E501
        self._check_operation_params('post_write', all_params, local_var_params)
        # verify the required parameter 'org' is set
        if ('org' not in local_var_params or
                local_var_params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `post_write`")  # noqa: E501
        # verify the required parameter 'bucket' is set
        if ('bucket' not in local_var_params or
                local_var_params['bucket'] is None):
            raise ValueError("Missing the required parameter `bucket` when calling `post_write`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_write`")  # noqa: E501

        path_params = {}

        query_params = []
        if 'org' in local_var_params:
            query_params.append(('org', local_var_params['org']))  # noqa: E501
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))  # noqa: E501
        if 'precision' in local_var_params:
            query_params.append(('precision', local_var_params['precision']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501
        if 'content_encoding' in local_var_params:
            header_params['Content-Encoding'] = local_var_params['content_encoding']  # noqa: E501
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']  # noqa: E501
        if 'content_length' in local_var_params:
            header_params['Content-Length'] = local_var_params['content_length']  # noqa: E501
        if 'accept' in local_var_params:
            header_params['Accept'] = local_var_params['accept']  # noqa: E501

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html', ])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        return local_var_params, path_params, query_params, header_params, body_params
