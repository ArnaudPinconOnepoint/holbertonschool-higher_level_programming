#!/usr/bin/python3
"""Module to get status"""
import urllib.request


if __name__ == "__main__":
    """Module to call api https://intranet.hbtn.io/status"""
    url = 'https://intranet.hbtn.io/status'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'cookie': 'introjs-dontShowAgain=true; timezone=10; context_user_curriculum_status_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik16QTNNVEU9IiwiZXhwIjpudWxsLCJwdXIiOiJjb29raWUuY29udGV4dF91c2VyX2N1cnJpY3VsdW1fc3RhdHVzX2lkIn19--a4e332e7a660b1de6e9e9f787d5261d4f6168f2c; context_curriculum_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1qazEiLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5jb250ZXh0X2N1cnJpY3VsdW1faWQifX0%3D--cbb9fb9823fc13cb7c544a7ee1db56b8b315e066; cf_clearance=d86L2dMjda6nCdkMUMG4YttzaBc9huHL_dHNI.KteOY-1727324389-1.2.1.1-SXH.fWjG6aSI_NzOSNiSULz.xRpS0WjvuA45ouAua93.GIXBefn34ASn809ihI2n6HMfyj8sEO6OAYkSzGxVJvkXo0lEEOl2X8QA3rHtaSqUjGgrUcvJOs4nGpn3GJkYZ932YQ0alpqWtUw.7VdIWSzO4Rtfjm8My05Le4QfIkyy21xGhKYy0Mpf8NoKGCIgPNNDCUn47h8qQkPwZjQiwJ563OiasUE6UnJ_SJJdwtLySoocTssWi7DHuTtSta8_jJU83etzK5BsXP6bFwaQYrjsofbzIi.75uvRWqsFa5ALJh.5K3RW21PkfyLEnqUWMT.89IEGypxSZ5wSIRJjSHgwCpLu2f_Nok5f_Aq5pMcW0x8Dl2HXvcdvddeFJGFRw_haZJQo1l0upRjUqlkuy0UQ4cXh_IAq1UenCpbmXNKVUjLg4GyfDHFPT3gV8Y6Z; _holberton_intranet_session=n2bvxiPhHHY6F7BhQ1Vnf9bVMhaa5vpn0xtXuzo712rHTwAmpcrByc4%2BIxIOOI1q%2BHxRePKtKQMiNkxAqw7%2FbSucKmJ4ZI3wTV8GqNezN48gfevsCzuW1QEcFkwhsB2AtS%2BFM3KtQF1%2Fp%2Bo4rQ4I%2BiPwvhVVyQkwObY%2BFrJwWs%2BwC6ALKqnpplTIM45rZGoc7uGtC%2BuMPjLndSTiqnwCEt8hGiSrMMdHnII7t%2BBYH%2Fx9Nq7S%2FW2F70EIjOEz9AkBRcoDF15GOzsSHvonndBAj4Qqbe1KyPlpgIxGz0ITOag%2Bfpnh45MS%2FPu48MF%2FZ8Xh5xfaTteMUkd72WhNdb6IFtfJ6O5xN8LGFQTiX36Yz%2BpWup67%2BgCZz8mtuC%2Bj4wuxjUhx4CwqnlG%2F4Y9j9AdCcpIDlJ3Wo4hYHwHQXHbJDZ6w2juV%2BfqsV6EJ8vOBZOU7XHGmPe7CdulemTzW7BLMK2Rig5K%2F4iI%3D--12QeUSyRbLHydMuw--VyzoCj2u5cWDJpbrRk7vZA%3D%3D'
    }

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
