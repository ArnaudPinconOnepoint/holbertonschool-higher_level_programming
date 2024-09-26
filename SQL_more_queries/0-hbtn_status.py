#!/usr/bin/python3
"""Module to get status"""
import urllib.request


if __name__ == "__main__":
    """Module to call api https://intranet.hbtn.io/status"""
    url = 'https://intranet.hbtn.io/status'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'cookie': '_ga=GA1.2.880046347.1720274840; introjs-dontShowAgain=true; timezone=8; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik5EVXpORGc9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--91c078be9390b8fcadbc186a8e757eefd86776b4; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik16TXciLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--06ed7e72881a4e3f11e1ed7f60dca2e7162ad662; _gid=GA1.2.1432147884.1727271632; _ga_E61MDMQF4S=GS1.2.1727271631.28.1.1727271659.32.0.0; cf_clearance=7_rBiVGxDh3AFqxntCV.XKw0Dls_6J_ykkKm_XG_TGc-1727331473-1.2.1.1-SbQe9lXX9kLQv5O8s7AV06u2FNcDPVd53aBArXlaD3fwiCzGppP9lgCkhD4yUbs8oqn_P_SQPN5dR3d0LH4ZunolDVnknRzppRCWFT6Kpy1nW9tdxCPi6cbSlnrDNiAYhJHrN9W3xbuFUL6dRVy4aHgh9XhpG79Edb6aC566EN.gTEBOciMmitp6f1KrHVMVmp02rgH9oQk7gExiEZSBni1A1jIPIrdJjc8X6NiAo2ZxdfVc9LtOB6x3bQ40rmIVa1Npv_du34wFyUynqihaFUHy6Q.1muLN67ld9dMMF.iYMp4Y.VOi2LitFOaJPVM.QyQsZoZC3WmLhMMbC7kuN3bSHtUSQrVIzUzz8f0SPcqWbGQb3uv5BOE3KI.HrBkT40rDCvQkWbAk7RSAfBejLOUYn3cxislZBPskU5BMLQLTu4McQfAqYUapZcc3s5hu; _holberton_intranet_session=RXy6hdu3nqm4uUqkvqfilqobAiMXHlXyp6oA3zjGBrdozFWfvMNbmhdh0okSQNd62YR64ipjf30doC%2F036c95sJ%2FSgqt2h1iQyUfR8cFCY1Xtrd6%2B6xJIL8B0ENMunb5aOF2J6ovS4lJVY1yrZ1Mg83lgqzARg%2FqMdS9nBlgI49dxBOaQfa2vCgYxMlrZaH95VSEE5rp48ReiQIZI9HsjiU70P9lpV25Dgt7H6%2FVTdoGFyIO684%2B%2BBb8AlLJ0PdDJg63X8VRiONVhG%2FfHDFRxUeqgo8jBDeNZk1XFAu4gcRcb8Jbyvi%2BrG4GH2%2B5yfL%2BjQVgi0kAzxFcUxTtso%2BQI%2Fop5tpTDZ9ocA1uIK9dg6t68NOD%2BRVdWGwWgqbHx9%2FD%2BjwE1v1OEnqGGmgmiVbvL%2F8GCNIl%2FuOdRnGs34fWsoBytw0JcjOWd6mtBjenLWSx6fuyrXaJEMfoBFdcEt6WuKW%2BEoP2v6mRIB3%2B39ipItJiU1idzJ7UGJmEbg%3D%3D--v55jeNBQCwkEz2k9--h9FPY3UEK%2BD7rPprV5GN2w%3D%3D'
    }

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
