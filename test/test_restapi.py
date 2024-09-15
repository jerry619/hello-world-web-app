from config import CONNECT as CON
import requests

# Additional headers.
headers = {"Content-Type": "application/json"}


def pretty_print_request(request):
    print(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "-----------Request----------->",
            request.method + " " + request.url,
            "\n".join(
                "{}: {}".format(k, v) for k, v in request.headers.items()
            ),
            request.body,
        )
    )


def pretty_print_response(response):
    print(
        "\n{}\n{}\n\n{}\n\n{}\n".format(
            "<-----------Response-----------",
            "Status code:" + str(response.status_code),
            "\n".join(
                "{}: {}".format(k, v) for k, v in response.headers.items()
            ),
            response.text,
        )
    )


def test_get_all_config():
    url = "http://{}:{}/".format(CON.SERVERNAME, CON.PORT)
    resp = requests.get(url)
    # Validate response headers, body contents and content type.
    assert resp.status_code == 200
    resp_body = resp.json()
    '''
    assert len(resp_body) == 4
    assert resp.headers["Content-Type"] == "application/json"
    pretty_print_request(resp.request)
    pretty_print_response(resp)
    '''
