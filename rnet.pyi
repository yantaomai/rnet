# This file is automatically generated by pyo3_stub_gen
# ruff: noqa: E501, F401

import builtins
import typing

class Client:
    r"""
    A client for making HTTP requests.
    """
    def __new__(cls,**kwds): ...
    def get(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a GET request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.get("https://httpbin.org/get")
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def post(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a POST request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.post("://httpbin.org/post", json={"key": "value"})
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def put(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a PUT request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.put("https://httpbin.org/put", json={"key": "value"})
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def patch(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a PATCH request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.patch("https://httpbin.org/patch", json={"key": "value"})
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def delete(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a DELETE request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.delete("https://httpbin.org/delete")
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...

    def head(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a HEAD request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.head("https://httpbin.org/head")
            print(response.status_code)
        
        asyncio.run(main())
        ```
        """
        ...

    def options(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends an OPTIONS request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.options("https://httpbin.org/options")
            print(response.headers)
        
        asyncio.run(main())
        ```
        """
        ...

    def trace(self, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a TRACE request.
        
        # Arguments
        
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        
        async def main():
            client = rnet.Client()
            response = await client.trace("https://httpbin.org/trace")
            print(response.headers)
        
        asyncio.run(main())
        ```
        """
        ...

    def request(self, method:Method, url:builtins.str, **kwds) -> typing.Any:
        r"""
        Sends a request with the given method and URL.
        
        # Arguments
        
        * `method` - The HTTP method to use.
        * `url` - The URL to send the request to.
        * `**kwds` - Additional request parameters.
        
        # Returns
        
        A `Response` object.
        
        # Examples
        
        ```python
        import rnet
        import asyncio
        from rnet import Method
        
        async def main():
            client = rnet.Client()
            response = await client.request(Method.GET, "https://httpbin.org/get")
            print(await response.text())
        
        asyncio.run(main())
        ```
        """
        ...


class ClientParams:
    r"""
    The parameters for a request.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Impersonate, Version
    
    params = rnet.RequestParams(
        impersonate=Impersonate.Chrome100,
        default_headers={"Content-Type": "application/json"},
        user_agent="Mozilla/5.0",
        timeout=10,
        connect_timeout=5,
        read_timeout=15,
        no_keepalive=True,
        no_proxy=False,
        http1_only=False,
        http2_only=True,
        referer=True
    )
    
    response = await rnet.get("https://www.rust-lang.org", **params)
    body = await response.text()
    print(body)
    ```
    """
    impersonate: typing.Optional[Impersonate]
    user_agent: typing.Optional[builtins.str]
    headers_order: typing.Optional[builtins.list[builtins.str]]
    referer: typing.Optional[builtins.bool]
    timeout: typing.Optional[builtins.int]
    connect_timeout: typing.Optional[builtins.int]
    read_timeout: typing.Optional[builtins.int]
    no_keepalive: typing.Optional[builtins.bool]
    tcp_keepalive: typing.Optional[builtins.int]
    pool_idle_timeout: typing.Optional[builtins.int]
    pool_max_idle_per_host: typing.Optional[builtins.int]
    http1_only: typing.Optional[builtins.bool]
    http2_only: typing.Optional[builtins.bool]
    https_only: typing.Optional[builtins.bool]
    tcp_nodelay: typing.Optional[builtins.bool]
    danger_accept_invalid_certs: typing.Optional[builtins.bool]
    http2_max_retry_count: typing.Optional[builtins.int]
    tls_info: typing.Optional[builtins.bool]
    no_proxy: typing.Optional[builtins.bool]
    proxies: typing.Optional[builtins.list[Proxy]]
    interface: typing.Optional[builtins.str]
    gzip: typing.Optional[builtins.bool]
    brotli: typing.Optional[builtins.bool]
    deflate: typing.Optional[builtins.bool]
    zstd: typing.Optional[builtins.bool]

class HeaderMap:
    r"""
    A HTTP header map.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Method
    
    async def main():
        resp = await rnet.request(Method.GET, "https://www.google.com/")
        print("Headers: ", resp.headers.to_dict())
    
    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
    ```
    """
    def to_dict(self) -> dict:
        r"""
        Converts the header map to a Python dictionary.
        
        # Returns
        
        A Python dictionary representing the headers.
        """
        ...

    def __getitem__(self, key:builtins.str) -> typing.Optional[typing.Any]:
        r"""
        Gets the value of the specified header.
        
        # Arguments
        
        * `key` - The name of the header.
        
        # Returns
        
        An optional byte slice representing the value of the header.
        """
        ...

    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the header map.
        """
        ...


class Impersonate:
    r"""
    A impersonate.
    """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the impersonate.
        """
        ...

    def __repr__(self) -> builtins.str:
        r"""
        Returns a string representation of the impersonate.
        """
        ...


class Method:
    r"""
    A HTTP method.
    """
    ...

class Proxy:
    r"""
    A proxy server for a request.
    """
    @staticmethod
    def http(url:builtins.str) -> Proxy:
        r"""
        Creates a new HTTP proxy.
        
        # Arguments
        
        * `url` - The URL of the proxy server.
        
        # Returns
        
        A new `Proxy` instance.
        
        # Examples
        
        ```python
        import rnet
        
        proxy = rnet.Proxy.http("http://proxy.example.com")
        ```
        """
        ...

    @staticmethod
    def https(url:builtins.str) -> Proxy:
        r"""
        Creates a new HTTPS proxy.
        
        # Arguments
        
        * `url` - The URL of the proxy server.
        
        # Returns
        
        A new `Proxy` instance.
        
        # Examples
        
        ```python
        import rnet
        
        proxy = rnet.Proxy.https("https://proxy.example.com")
        ```
        """
        ...

    @staticmethod
    def all(url:builtins.str) -> Proxy:
        r"""
        Creates a new HTTPS proxy.
        
        # Arguments
        
        * `url` - The URL of the proxy server.
        
        # Returns
        
        A new `Proxy` instance.
        
        # Examples
        
        ```python
        import rnet
        
        proxy = rnet.Proxy.all("https://proxy.example.com")
        ```
        """
        ...


class RequestParams:
    r"""
    The parameters for a request.
    
    # Examples
    
    ```python
    import rnet
    from rnet import Impersonate, Version
    
    params = rnet.RequestParams(
        impersonate=Impersonate.Chrome100,
        version=Version.HTTP_2,
        user_agent="Mozilla/5.0",
        headers={"Content-Type": "application/json"},
        timeout=10,
        connect_timeout=5,
        read_timeout=15,
        no_keepalive=True,
        no_proxy=False,
        http1_only=False,
        http2_only=True,
        referer=True
    )
    
    response = await rnet.get("https://www.rust-lang.org", **params)
    body = await response.text()
    print(body)
    ```
    """
    proxy: typing.Optional[builtins.str]
    interface: typing.Optional[builtins.str]
    timeout: typing.Optional[builtins.int]
    read_timeout: typing.Optional[builtins.int]
    version: typing.Optional[Version]
    auth: typing.Optional[builtins.str]
    bearer_auth: typing.Optional[builtins.str]
    basic_auth: typing.Optional[tuple[builtins.str, typing.Optional[builtins.str]]]
    query: typing.Optional[builtins.list[tuple[builtins.str, builtins.str]]]
    form: typing.Optional[builtins.list[tuple[builtins.str, builtins.str]]]
    body: typing.Optional[builtins.list[builtins.int]]

class Response:
    r"""
    A response from a request.
    
    # Examples
    
    ```python
    import asyncio
    import rnet
    
    async def main():
        response = await rnet.get("https://www.rust-lang.org")
        print("Status Code: ", response.status_code)
        print("Version: ", response.version)
        print("Response URL: ", response.url)
        print("Headers: ", response.headers.to_dict())
        print("Content-Length: ", response.content_length)
        print("Encoding: ", response.encoding)
        print("Remote Address: ", response.remote_addr)
    
        text_content = await response.text()
        print("Text: ", text_content)
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```
    """
    url: builtins.str
    ok: builtins.bool
    status_code: typing.Any
    version: Version
    headers: HeaderMap
    content_length: builtins.int
    remote_addr: typing.Optional[SocketAddr]
    encoding: builtins.str
    cookies: dict
    def peer_certificate(self) -> typing.Optional[typing.Any]:
        r"""
        Returns the TLS peer certificate of the response.
        
        # Returns
        
        A Python object representing the TLS peer certificate of the response.
        """
        ...

    def text(self) -> typing.Any:
        r"""
        Returns the text content of the response.
        
        # Returns
        
        A Python object representing the text content of the response.
        """
        ...

    def text_with_charset(self, encoding:builtins.str) -> typing.Any:
        r"""
        Returns the text content of the response with a specific charset.
        
        # Arguments
        
        * `default_encoding` - The default encoding to use if the charset is not specified.
        
        # Returns
        
        A Python object representing the text content of the response.
        """
        ...

    def json(self) -> typing.Any:
        r"""
        Returns the JSON content of the response.
        
        # Returns
        
        A Python object representing the JSON content of the response.
        """
        ...

    def json_str(self) -> typing.Any:
        r"""
        Returns the JSON string content of the response.
        
        # Returns
        
        A Python object representing the JSON content of the response.
        """
        ...

    def json_str_pretty(self) -> typing.Any:
        r"""
        Returns the JSON pretty string content of the response.
        
        # Returns
        
        A Python object representing the JSON content of the response.
        """
        ...

    def bytes(self) -> typing.Any:
        r"""
        Returns the bytes content of the response.
        
        # Returns
        
        A Python object representing the bytes content of the response.
        """
        ...

    def stream(self) -> typing.Any:
        r"""
        Returns the stream content of the response.
        
        # Returns
        
        A Python object representing the stream content of the response.
        """
        ...

    def close(self) -> None:
        r"""
        Closes the response connection.
        """
        ...


class SocketAddr:
    r"""
    A IP socket address.
    """
    def ip(self) -> typing.Any:
        r"""
        Returns the IP address of the socket address.
        """
        ...

    def port(self) -> builtins.int:
        r"""
        Returns the port number of the socket address.
        """
        ...

    def __str__(self) -> builtins.str:
        r"""
        Returns the socket address as a string.
        """
        ...


class Streamer:
    r"""
    A streaming response.
    This is an asynchronous iterator that yields chunks of data from the response stream.
    This is used to stream the response content.
    This is used in the `stream` method of the `Response` class.
    This is used in an asynchronous for loop in Python.
    
    # Examples
    
    ```python
    import asyncio
    import rnet
    from rnet import Method, Impersonate
    
    async def main():
        resp = await rnet.get("https://httpbin.org/stream/20")
        print("Status Code: ", resp.status_code)
        print("Version: ", resp.version)
        print("Response URL: ", resp.url)
        print("Headers: ", resp.headers.to_dict())
        print("Content-Length: ", resp.content_length)
        print("Encoding: ", resp.encoding)
        print("Remote Address: ", resp.remote_addr)
    
        streamer = resp.stream()
        async for chunk in streamer:
            print("Chunk: ", chunk)
            await asyncio.sleep(0.1)
    
    if __name__ == "__main__":
        asyncio.run(main())
    ```
    """
    def __aiter__(self) -> Streamer:
        r"""
        Returns the `Streamer` instance itself to be used as an asynchronous iterator.
        
        This method allows the `Streamer` to be used in an asynchronous for loop in Python.
        
        # Returns
        
        The `Streamer` instance itself.
        """
        ...

    def __anext__(self) -> typing.Optional[typing.Any]:
        r"""
        Returns the next chunk of the response as an asynchronous iterator.
        
        This method implements the `__anext__` method for the `Streamer` class, allowing it to be
        used as an asynchronous iterator in Python. It returns the next chunk of the response or
        raises `PyStopAsyncIteration` if the iterator is exhausted.
        
        # Returns
        
        A `PyResult` containing an `Option<PyObject>`. If there is a next chunk, it returns `Some(PyObject)`.
        If the iterator is exhausted, it raises `PyStopAsyncIteration`.
        """
        ...

    def chunk(self) -> typing.Optional[typing.Any]:
        r"""
        This is a helper method to get the next chunk from the stream.
        It is used to get the next chunk from the stream.
        This method is used in __anext__ method.
        """
        ...


class Version:
    r"""
    A HTTP version.
    """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the version.
        """
        ...

    def __repr__(self) -> builtins.str:
        r"""
        Returns a string representation of the version.
        """
        ...


def delete(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `DELETE` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.delete("https://httpbin.org/anything")
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def get(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `GET` request.
    
    See also the methods on the [`rquest::Response`](./struct.Response.html)
    type.
    
    **NOTE**: This function creates a new internal `Client` on each call,
    and so should not be used if making many requests. Create a
    [`Client`](./struct.Client.html) instead.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.get("https://httpbin.org/anything")
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    
    # Errors
    
    This function fails if:
    
    - native TLS backend cannot be initialized
    - supplied `Url` cannot be parsed
    - there was an error while sending request
    - redirect limit was exhausted
    """
    ...

def head(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `HEAD` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.head("https://httpbin.org/anything")
        print(response.headers)
    
    asyncio.run(run())
    ```
    """
    ...

def options(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make an `OPTIONS` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.options("https://httpbin.org/anything")
        print(response.headers)
    
    asyncio.run(run())
    ```
    """
    ...

def patch(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `PATCH` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.patch("https://httpbin.org/anything", json={"key": "value"})
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def post(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `POST` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.post("https://httpbin.org/anything", json={"key": "value"})
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def put(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `PUT` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.put("https://httpbin.org/anything", json={"key": "value"})
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def request(method:Method, url:builtins.str, **kwds) -> typing.Any:
    r"""
    Make a request with the given parameters.
    
    This function allows you to make a request with the specified parameters encapsulated in a `Request` object.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    from rnet import Method
    
    async def run():
        response = await rnet.request(Method.GET, "https://www.rust-lang.org")
        body = await response.text()
        print(body)
    
    asyncio.run(run())
    ```
    """
    ...

def trace(url:builtins.str, **kwds) -> typing.Any:
    r"""
    Shortcut method to quickly make a `TRACE` request.
    
    # Examples
    
    ```python
    import rnet
    import asyncio
    
    async def run():
        response = await rnet.trace("https://www.rust-lang.org")
        print(response.headers)
    
    asyncio.run(run())
    ```
    """
    ...

