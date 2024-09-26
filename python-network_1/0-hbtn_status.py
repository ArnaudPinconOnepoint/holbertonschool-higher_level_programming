#!/usr/bin/python3
"""Module to get status"""
import urllib.request


if __name__ == "__main__":
    """Module to call api https://intranet.hbtn.io/status"""
    url = 'https://intranet.hbtn.io/status'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'cookie': 'introjs-dontShowAgain=true; cf_clearance=mWF6beaKVDITL8yMjeFDWptonfgZoKXE6dhmXjpJjCg-1727393804-1.2.1.1-KSnP9EwjcC8KnvRMVZsyDJhcs15eRvjSHv82l_tPIB.2bmlXwiN.TaxN.ueqRdXLFo..vwTfhCbIqIsEwVQ2edJk_lF6.NwlXUWQGfdrKQtHETqJBrlv22y3V0Pt62CEdscYWhDqiDNu0CWaAS3LAb3d.Xp3HpbEzLCG9rGog_J5BmZLL4OCHHEKzQxbn8IoXJrFTSSWqNH2nCS2y1wEspbMFMGaeQFntbU3gQz30C44Car5nu2dYUyyHN7a10xHtLwj7rNPY0MwWHsH1KbK6psYtMjpyV.Kb6q1J0Ep9sHJCIYDYAZ5GTQ4xt16sKvoww.BJvFievXhHQ7K2eg3ARspsy_pCy4Rj3etfHhBNbKagLmR_fwg1uKKlTsoAss11AIGDFc9XvNBCLxK9NRjA.3FEOEDXkh5BKyfUEFOJJ7R0zfpr8hARdXcvTwOO14b; timezone=10; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik16QTNNVEU9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--a4e332e7a660b1de6e9e9f787d5261d4f6168f2c; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1qazEiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--cbb9fb9823fc13cb7c544a7ee1db56b8b315e066; _holberton_intranet_session=n%2B0z08iG31Dc8veqSHefJerWUdV2Z9UsZf6Ia%2FhI6nYIJSQ%2Bv7%2BhJPrcaQmlgaVHur7U7JdOgiouMvx%2Fr%2BbOW6nbsyXLmb1MN8sao%2BD6fnnOV1kWah5SCfhp%2B6krq8STb05CT69Uh1Q4lW3140jr4MJv1ZqJDb%2BAJQ9hpG18uUPyGYgAR09xTLCgFggLa1zY8%2BdK%2BeUKeZYUAPlx57K3HHEsHfRTMcHA9GTPYmY%2FJBBBtkrRxPcJWvW1flh97cnie1ZxqZMfdWQbX1l7jNqsagZCjxkpK8odBwK6KVA4U0HIBm5OPwigT6NR2f%2B7fJ%2F4OCn28uq2OOAZVqCt4nknIAci038RitpbLBAAUEM1ZdHQc5J1vp8lRAkh5Q%2F4N1q8FJmNC1i9EC1kIt6MAavclNLb62x2Lg7oSbrrC%2BhsgKXgik56iEZgReXgIVAdD8yugw3LE72cSczDWV%2BVSX8TDEOW23x1U60%3D--YdQa9fL4dou6dGtB--hh6oBdj5JZ1qCYf9atK1Sw%3D%3D'
    }

    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
